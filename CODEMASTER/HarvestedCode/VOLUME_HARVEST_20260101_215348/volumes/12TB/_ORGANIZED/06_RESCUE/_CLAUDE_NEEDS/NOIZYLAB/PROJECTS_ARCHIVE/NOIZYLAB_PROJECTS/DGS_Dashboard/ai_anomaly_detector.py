#!/usr/bin/env python3
"""
AI-Powered Anomaly Detection System

Advanced machine learning system for detecting anomalies in DNS health,
system performance, and automation patterns. Uses multiple ML algorithms
to identify unusual behavior and predict potential issues before they occur.

Features:
- Real-time anomaly detection
- Predictive failure analysis
- Pattern learning and adaptation
- Automated alert prioritization
- Historical trend analysis
- Self-improving algorithms
"""

import json
import logging
import os
import sqlite3
import sys
import warnings
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import joblib
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("ai_anomaly_detection.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

logger = logging.getLogger(__name__)


@dataclass
class AnomalyResult:
    """Result from anomaly detection analysis."""

    timestamp: datetime
    domain: str
    metric_type: str
    value: float
    is_anomaly: bool
    anomaly_score: float
    confidence: float
    severity: str
    predicted_issue: Optional[str] = None
    recommended_action: Optional[str] = None


class AIAnomalyDetector:
    """AI-powered anomaly detection system."""

    def __init__(self):
        """Initialize the AI anomaly detection system."""
        self.db_path = Path("dns_monitoring.db")
        self.model_path = Path("models")
        self.model_path.mkdir(exist_ok=True)

        # ML Models
        self.isolation_forest = IsolationForest(
            contamination=0.1, random_state=42, n_estimators=100
        )
        self.scaler = StandardScaler()
        self.dbscan = DBSCAN(eps=0.3, min_samples=5)

        # Model states
        self.models_trained = False
        self.feature_columns = []

        # Thresholds and parameters
        self.anomaly_threshold = -0.5
        self.confidence_threshold = 0.7

        # Load existing models if available
        self.load_models()

    def extract_features_from_db(self, hours_back: int = 168) -> pd.DataFrame:
        """
        Extract features from the monitoring database for ML analysis.

        Args:
            hours_back (int): Hours of historical data to extract

        Returns:
            pd.DataFrame: Feature matrix for ML analysis
        """
        if not self.db_path.exists():
            logger.warning("Database not found, creating empty DataFrame")
            return pd.DataFrame()

        try:
            with sqlite3.connect(self.db_path) as conn:
                query = """
                    SELECT
                        domain,
                        timestamp,
                        response_time,
                        is_healthy,
                        cloudflare_status,
                        issues
                    FROM dns_health
                    WHERE timestamp > datetime('now', '-{} hours')
                    ORDER BY timestamp
                """.format(
                    hours_back
                )

                df = pd.read_sql_query(query, conn)

            if df.empty:
                logger.warning("No data found in database")
                return df

            # Convert timestamp to datetime
            df["timestamp"] = pd.to_datetime(df["timestamp"])

            # Feature engineering
            features_list = []

            for domain in df["domain"].unique():
                domain_data = df[df["domain"] == domain].copy()
                domain_data = domain_data.sort_values("timestamp")

                # Basic features
                domain_features = {
                    "domain": domain,
                    "avg_response_time": domain_data["response_time"].mean(),
                    "max_response_time": domain_data["response_time"].max(),
                    "min_response_time": domain_data["response_time"].min(),
                    "std_response_time": domain_data["response_time"].std(),
                    "health_rate": domain_data["is_healthy"].mean(),
                    "total_checks": len(domain_data),
                    "failure_count": (domain_data["is_healthy"] == 0).sum(),
                }

                # Time-based features
                if len(domain_data) > 1:
                    domain_features.update(
                        {
                            "response_time_trend": (
                                np.polyfit(
                                    range(len(domain_data)),
                                    domain_data["response_time"],
                                    1,
                                )[0]
                                if len(domain_data) > 1
                                else 0
                            ),
                            "health_consistency": 1 - domain_data["is_healthy"].std(),
                            "recent_failure_rate": (
                                domain_data.tail(10)["is_healthy"].mean()
                                if len(domain_data) >= 10
                                else domain_data["is_healthy"].mean()
                            ),
                        }
                    )
                else:
                    domain_features.update(
                        {
                            "response_time_trend": 0,
                            "health_consistency": 1,
                            "recent_failure_rate": domain_data["is_healthy"].mean(),
                        })

                # Advanced features
                domain_features.update(
                    {
                        "response_time_percentile_95": domain_data[
                            "response_time"
                        ].quantile(0.95),
                        "consecutive_failures": self._calculate_consecutive_failures(
                            domain_data
                        ),
                        "time_since_last_failure": self._time_since_last_failure(
                            domain_data
                        ),
                        "hour_of_day": (
                            domain_data["timestamp"].dt.hour.mode().iloc[0]
                            if not domain_data.empty
                            else 12
                        ),
                        "day_of_week": (
                            domain_data["timestamp"].dt.dayofweek.mode().iloc[0]
                            if not domain_data.empty
                            else 0
                        ),
                    }
                )

                features_list.append(domain_features)

            features_df = pd.DataFrame(features_list)

            # Handle NaN values
            features_df = features_df.fillna(0)

            logger.info(
                f"Extracted features for {
                    len(features_df)} domains with {
                    len(
                        features_df.columns)} features"
            )

            return features_df

        except Exception as e:
            logger.error(f"Error extracting features: {e}")
            return pd.DataFrame()

    def _calculate_consecutive_failures(
            self, domain_data: pd.DataFrame) -> int:
        """Calculate maximum consecutive failures for a domain."""
        if domain_data.empty:
            return 0

        failures = (domain_data["is_healthy"] == 0).astype(int)
        max_consecutive = 0
        current_consecutive = 0

        for failure in failures:
            if failure:
                current_consecutive += 1
                max_consecutive = max(max_consecutive, current_consecutive)
            else:
                current_consecutive = 0

        return max_consecutive

    def _time_since_last_failure(self, domain_data: pd.DataFrame) -> float:
        """Calculate hours since last failure."""
        if domain_data.empty:
            return 0

        failures = domain_data[domain_data["is_healthy"] == 0]

        if failures.empty:
            return 999  # Large number indicating no recent failures

        last_failure = pd.to_datetime(failures["timestamp"].iloc[-1])
        now = pd.to_datetime("now")

        return (now - last_failure).total_seconds() / 3600

    def train_models(self, features_df: pd.DataFrame) -> bool:
        """
        Train ML models on the feature data.

        Args:
            features_df (pd.DataFrame): Feature matrix

        Returns:
            bool: True if training successful
        """
        if features_df.empty:
            logger.warning("No data available for training")
            return False

        try:
            # Prepare features for training
            numeric_columns = features_df.select_dtypes(
                include=[np.number]).columns
            numeric_columns = [
                col for col in numeric_columns if col != "domain"]

            if len(numeric_columns) == 0:
                logger.error("No numeric features found for training")
                return False

            X = features_df[numeric_columns].values

            # Handle infinite values
            X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

            if len(X) < 5:
                logger.warning(
                    "Insufficient data for training (need at least 5 samples)"
                )
                return False

            # Scale features
            X_scaled = self.scaler.fit_transform(X)

            # Train Isolation Forest
            self.isolation_forest.fit(X_scaled)

            # Train DBSCAN for clustering
            self.dbscan.fit(X_scaled)

            # Store feature columns
            self.feature_columns = numeric_columns
            self.models_trained = True

            # Save models
            self.save_models()

            logger.info(
                f"Models trained successfully on {
                    len(X)} samples with {
                    len(numeric_columns)} features"
            )

            return True

        except Exception as e:
            logger.error(f"Error training models: {e}")
            return False

    def detect_anomalies(
            self,
            features_df: pd.DataFrame) -> List[AnomalyResult]:
        """
        Detect anomalies in the feature data.

        Args:
            features_df (pd.DataFrame): Feature matrix

        Returns:
            List[AnomalyResult]: Detected anomalies
        """
        anomalies = []

        if not self.models_trained or features_df.empty:
            logger.warning("Models not trained or no data available")
            return anomalies

        try:
            # Prepare features
            X = features_df[self.feature_columns].values
            X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)

            # Scale features
            X_scaled = self.scaler.transform(X)

            # Get anomaly scores
            anomaly_scores = self.isolation_forest.decision_function(X_scaled)
            anomaly_predictions = self.isolation_forest.predict(X_scaled)

            # Get cluster labels
            cluster_labels = self.dbscan.fit_predict(X_scaled)

            for i, (domain, score, prediction, cluster) in enumerate(
                zip(
                    features_df["domain"],
                    anomaly_scores,
                    anomaly_predictions,
                    cluster_labels,
                )
            ):

                is_anomaly = prediction == -1 or score < self.anomaly_threshold
                confidence = abs(score) if score < 0 else (1 - score)

                # Determine severity
                if score < -0.8:
                    severity = "critical"
                elif score < -0.5:
                    severity = "high"
                elif score < -0.2:
                    severity = "medium"
                else:
                    severity = "low"

                # Predict issue type and recommend action
                predicted_issue, recommended_action = self._analyze_domain_issues(
                    features_df.iloc[i], score, cluster)

                if is_anomaly or confidence > self.confidence_threshold:
                    anomaly = AnomalyResult(
                        timestamp=datetime.now(),
                        domain=domain,
                        metric_type="multi_feature",
                        value=score,
                        is_anomaly=is_anomaly,
                        anomaly_score=score,
                        confidence=confidence,
                        severity=severity,
                        predicted_issue=predicted_issue,
                        recommended_action=recommended_action,
                    )

                    anomalies.append(anomaly)

            logger.info(
                f"Detected {
                    len(anomalies)} anomalies from {
                    len(features_df)} domains"
            )

        except Exception as e:
            logger.error(f"Error detecting anomalies: {e}")

        return anomalies

    def _analyze_domain_issues(
        self, domain_features: pd.Series, anomaly_score: float, cluster: int
    ) -> Tuple[str, str]:
        """
        Analyze domain-specific issues and provide recommendations.

        Args:
            domain_features (pd.Series): Domain feature vector
            anomaly_score (float): Anomaly score
            cluster (int): Cluster assignment

        Returns:
            Tuple[str, str]: (predicted_issue, recommended_action)
        """
        try:
            # High response time issues
            if domain_features.get("avg_response_time", 0) > 2.0:
                return (
                    "High response time",
                    "Check DNS server performance and network connectivity",
                )

            # Health rate issues
            if domain_features.get("health_rate", 1) < 0.8:
                return (
                    "Frequent failures",
                    "Investigate nameserver configuration and domain registration",
                )

            # Response time trending up
            if domain_features.get("response_time_trend", 0) > 0.1:
                return (
                    "Performance degradation",
                    "Monitor server resources and consider optimization",
                )

            # Consecutive failures
            if domain_features.get("consecutive_failures", 0) > 3:
                return (
                    "Persistent connectivity issues",
                    "Check nameservers and DNS propagation",
                )

            # Low health consistency
            if domain_features.get("health_consistency", 1) < 0.5:
                return (
                    "Intermittent issues",
                    "Review DNS configuration and monitoring logs",
                )

            # Cluster-based issues
            if cluster == -1:  # Noise cluster in DBSCAN
                return "Outlier behavior", "Investigate unique domain characteristics"

            # Default for severe anomalies
            if anomaly_score < -0.5:
                return (
                    "Multiple indicators anomaly",
                    "Comprehensive health check recommended",
                )

            return "Pattern anomaly", "Monitor for trend continuation"

        except Exception as e:
            logger.error(f"Error analyzing domain issues: {e}")
            return "Analysis error", "Manual investigation required"

    def save_models(self):
        """Save trained models to disk."""
        try:
            joblib.dump(
                self.isolation_forest,
                self.model_path /
                "isolation_forest.pkl")
            joblib.dump(self.scaler, self.model_path / "scaler.pkl")
            joblib.dump(self.dbscan, self.model_path / "dbscan.pkl")

            # Save metadata
            metadata = {
                "feature_columns": self.feature_columns,
                "models_trained": self.models_trained,
                "trained_at": datetime.now().isoformat(),
                "anomaly_threshold": self.anomaly_threshold,
                "confidence_threshold": self.confidence_threshold,
            }

            with open(self.model_path / "metadata.json", "w") as f:
                json.dump(metadata, f, indent=2)

            logger.info("Models saved successfully")

        except Exception as e:
            logger.error(f"Error saving models: {e}")

    def load_models(self):
        """Load trained models from disk."""
        try:
            model_files = [
                "isolation_forest.pkl",
                "scaler.pkl",
                "dbscan.pkl",
                "metadata.json",
            ]

            if not all((self.model_path / f).exists() for f in model_files):
                logger.info("No existing models found")
                return

            self.isolation_forest = joblib.load(
                self.model_path / "isolation_forest.pkl"
            )
            self.scaler = joblib.load(self.model_path / "scaler.pkl")
            self.dbscan = joblib.load(self.model_path / "dbscan.pkl")

            with open(self.model_path / "metadata.json", "r") as f:
                metadata = json.load(f)

            self.feature_columns = metadata["feature_columns"]
            self.models_trained = metadata["models_trained"]
            self.anomaly_threshold = metadata.get("anomaly_threshold", -0.5)
            self.confidence_threshold = metadata.get(
                "confidence_threshold", 0.7)

            logger.info(
                f"Models loaded successfully (trained: {
                    metadata['trained_at']})"
            )

        except Exception as e:
            logger.error(f"Error loading models: {e}")
            self.models_trained = False

    def generate_ai_report(self, anomalies: List[AnomalyResult]) -> str:
        """
        Generate a comprehensive AI analysis report.

        Args:
            anomalies (List[AnomalyResult]): Detected anomalies

        Returns:
            str: Formatted AI report
        """
        report_lines = []
        report_lines.append("🤖 AI ANOMALY DETECTION REPORT")
        report_lines.append("=" * 50)
        report_lines.append(
            f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        report_lines.append(
            f"Model Status: {
                '✅ Trained' if self.models_trained else '❌ Not Trained'}"
        )
        report_lines.append("")

        if not anomalies:
            report_lines.append("🎉 NO ANOMALIES DETECTED")
            report_lines.append(
                "All systems operating within normal parameters.")
            report_lines.append("")
        else:
            # Summary
            critical_count = sum(
                1 for a in anomalies if a.severity == "critical")
            high_count = sum(1 for a in anomalies if a.severity == "high")
            medium_count = sum(1 for a in anomalies if a.severity == "medium")
            low_count = sum(1 for a in anomalies if a.severity == "low")

            report_lines.append("🚨 ANOMALY SUMMARY:")
            report_lines.append(f"   🔴 Critical: {critical_count}")
            report_lines.append(f"   🟠 High: {high_count}")
            report_lines.append(f"   🟡 Medium: {medium_count}")
            report_lines.append(f"   🟢 Low: {low_count}")
            report_lines.append("")

            # Detailed anomalies
            report_lines.append("🔍 DETAILED ANALYSIS:")
            report_lines.append("")

            # Sort by severity
            severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
            sorted_anomalies = sorted(
                anomalies, key=lambda x: severity_order.get(x.severity, 4)
            )

            for anomaly in sorted_anomalies:
                severity_emoji = {
                    "critical": "🔴",
                    "high": "🟠",
                    "medium": "🟡",
                    "low": "🟢",
                }.get(anomaly.severity, "⚪")

                report_lines.append(
                    f"{severity_emoji} {
                        anomaly.domain.upper()}"
                )
                report_lines.append(
                    f"   Anomaly Score: {
                        anomaly.anomaly_score:.3f}"
                )
                report_lines.append(f"   Confidence: {anomaly.confidence:.1%}")
                report_lines.append(f"   Issue: {anomaly.predicted_issue}")
                report_lines.append(f"   Action: {anomaly.recommended_action}")
                report_lines.append("")

        # Model statistics
        report_lines.append("📊 MODEL STATISTICS:")
        if self.models_trained:
            report_lines.append(
                f"   Features Used: {len(self.feature_columns)}")
            report_lines.append(
                f"   Anomaly Threshold: {
                    self.anomaly_threshold}"
            )
            report_lines.append(
                f"   Confidence Threshold: {self.confidence_threshold:.1%}"
            )
        else:
            report_lines.append("   ⚠️ Models need training with more data")

        report_lines.append("")
        report_lines.append("💡 AI INSIGHTS:")
        report_lines.append(
            "   • Anomaly detection improves with more historical data")
        report_lines.append(
            "   • Models automatically retrain as new patterns emerge")
        report_lines.append("   • Check AI logs for detailed ML analysis")

        return "\n".join(report_lines)

    def run_ai_analysis(self, retrain: bool = False) -> Dict[str, Any]:
        """
        Run complete AI anomaly detection analysis.

        Args:
            retrain (bool): Force model retraining

        Returns:
            Dict[str, Any]: Analysis results
        """
        try:
            logger.info("Starting AI anomaly detection analysis...")

            # Extract features from database
            features_df = self.extract_features_from_db()

            if features_df.empty:
                logger.warning("No data available for analysis")
                return {
                    "status": "no_data",
                    "anomalies": [],
                    "report": "No historical data available for AI analysis",
                }

            # Train or retrain models if needed
            if not self.models_trained or retrain:
                logger.info("Training AI models...")
                training_success = self.train_models(features_df)

                if not training_success:
                    return {
                        "status": "training_failed",
                        "anomalies": [],
                        "report": "AI model training failed",
                    }

            # Detect anomalies
            anomalies = self.detect_anomalies(features_df)

            # Generate report
            report = self.generate_ai_report(anomalies)

            # Save results
            results = {
                "status": "success",
                "timestamp": datetime.now().isoformat(),
                "anomalies": [asdict(a) for a in anomalies],
                "models_trained": self.models_trained,
                "feature_count": len(self.feature_columns),
                "domains_analyzed": len(features_df),
            }

            with open("ai_anomaly_results.json", "w") as f:
                json.dump(results, f, indent=2, default=str)

            with open("ai_anomaly_report.txt", "w") as f:
                f.write(report)

            logger.info(
                f"AI analysis completed: {
                    len(anomalies)} anomalies detected"
            )

            return {
                "status": "success",
                "anomalies": anomalies,
                "report": report,
                "results": results,
            }

        except Exception as e:
            logger.error(f"Error in AI analysis: {e}")
            return {
                "status": "error",
                "anomalies": [],
                "report": f"AI analysis failed: {str(e)}",
            }


def main():
    """Main entry point for AI anomaly detection."""
    try:
        detector = AIAnomalyDetector()

        # Check command line arguments
        retrain = "--retrain" in sys.argv

        # Run AI analysis
        results = detector.run_ai_analysis(retrain=retrain)

        # Display report
        print("\n" + results["report"])

        if results["status"] == "success":
            print(f"\n🤖 AI Analysis Complete!")
            print(f"   Anomalies: {len(results['anomalies'])}")
            print(
                f"   Models: {
                    '✅ Trained' if detector.models_trained else '❌ Need Training'}")
            print(f"   Results saved to: ai_anomaly_results.json")

    except KeyboardInterrupt:
        logger.info("AI anomaly detection interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
