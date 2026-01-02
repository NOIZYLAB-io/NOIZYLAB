#!/usr/bin/env python3
"""
AI-Powered Anomaly Detection System

Advanced machine learning system for detecting anomalies in DNS health,
system performance, and automation patterns. Features:

- Time-series anomaly detection
- Pattern recognition for DNS issues
- Predictive maintenance alerts
- Automated threshold adjustment
- Smart alerting with reduced false positives
- Trend analysis and forecasting
"""

import json
import logging
import os
import sqlite3
import sys
import warnings
from collections import defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

try:
    import joblib
    from sklearn.cluster import DBSCAN
    from sklearn.ensemble import IsolationForest
    from sklearn.preprocessing import StandardScaler

    ML_AVAILABLE = True
except ImportError:
    print(
        "ML libraries not available. Install with: pip install scikit-learn pandas numpy joblib"
    )
    ML_AVAILABLE = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class Anomaly:
    """Represents a detected anomaly."""

    timestamp: datetime
    component: str
    metric: str
    value: float
    expected_range: Tuple[float, float]
    severity: str  # low, medium, high, critical
    confidence: float
    description: str
    suggested_action: str


class AIAnomalyDetector:
    """AI-powered anomaly detection system."""

    def __init__(self):
        """Initialize the AI anomaly detector."""
        self.db_path = Path("dns_monitoring.db")
        self.models_path = Path("ml_models")
        self.models_path.mkdir(exist_ok=True)

        # ML models
        self.models = {
            "dns_health": None,
            "response_time": None,
            "system_health": None}

        # Scalers for normalization
        self.scalers = {
            "dns_health": None,
            "response_time": None,
            "system_health": None,
        }

        # Anomaly thresholds
        self.thresholds = {
            "response_time": {"warning": 2.0, "critical": 5.0},
            "health_rate": {"warning": 0.8, "critical": 0.6},
            "system_score": {"warning": 70, "critical": 50},
        }

        # Pattern recognition
        self.patterns = {
            "dns_failures": [],
            "response_spikes": [],
            "system_degradation": [],
        }

        if not ML_AVAILABLE:
            logger.warning(
                "Machine learning libraries not available. Using statistical methods only."
            )

    def load_historical_data(self, days: int = 30) -> pd.DataFrame:
        """Load historical data for analysis."""
        if not self.db_path.exists():
            logger.warning("No historical data available")
            return pd.DataFrame()

        try:
            with sqlite3.connect(self.db_path) as conn:
                query = """
                    SELECT
                        domain,
                        timestamp,
                        is_healthy,
                        response_time,
                        cloudflare_status,
                        issues
                    FROM dns_health
                    WHERE timestamp > datetime('now', '-{} days')
                    ORDER BY timestamp
                """.format(
                    days
                )

                df = pd.read_sql_query(query, conn)

            if not df.empty:
                df["timestamp"] = pd.to_datetime(df["timestamp"])
                df["hour"] = df["timestamp"].dt.hour
                df["day_of_week"] = df["timestamp"].dt.dayofweek
                df["response_time"] = df["response_time"].fillna(0)

                logger.info(
                    f"Loaded {
                        len(df)} historical records for analysis"
                )

            return df

        except Exception as e:
            logger.error(f"Error loading historical data: {e}")
            return pd.DataFrame()

    def train_anomaly_models(self, df: pd.DataFrame) -> bool:
        """Train ML models for anomaly detection."""
        if not ML_AVAILABLE or df.empty:
            return False

        try:
            # Prepare features for DNS health model
            dns_features = self._prepare_dns_features(df)

            if not dns_features.empty:
                # Train Isolation Forest for DNS anomalies
                scaler = StandardScaler()
                scaled_features = scaler.fit_transform(dns_features)

                model = IsolationForest(
                    contamination=0.1,  # Expect 10% anomalies
                    random_state=42,
                    n_estimators=100,
                )
                model.fit(scaled_features)

                # Save models
                self.models["dns_health"] = model
                self.scalers["dns_health"] = scaler

                joblib.dump(model, self.models_path / "dns_health_model.pkl")
                joblib.dump(scaler, self.models_path / "dns_health_scaler.pkl")

                logger.info("DNS health anomaly model trained successfully")

            # Train response time model
            response_features = self._prepare_response_features(df)

            if not response_features.empty:
                scaler = StandardScaler()
                scaled_features = scaler.fit_transform(response_features)

                model = IsolationForest(
                    contamination=0.05,  # Expect 5% response time anomalies
                    random_state=42,
                )
                model.fit(scaled_features)

                self.models["response_time"] = model
                self.scalers["response_time"] = scaler

                joblib.dump(
                    model,
                    self.models_path /
                    "response_time_model.pkl")
                joblib.dump(
                    scaler,
                    self.models_path /
                    "response_time_scaler.pkl")

                logger.info("Response time anomaly model trained successfully")

            return True

        except Exception as e:
            logger.error(f"Error training anomaly models: {e}")
            return False

    def _prepare_dns_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Prepare features for DNS health analysis."""
        try:
            # Aggregate by hour for each domain
            features = (
                df.groupby(["domain", "hour"])
                .agg(
                    {
                        "is_healthy": "mean",
                        "response_time": ["mean", "std", "max"],
                        "day_of_week": "first",
                    }
                )
                .reset_index()
            )

            # Flatten column names
            features.columns = [
                "_".join(col).strip() if col[1] else col[0]
                for col in features.columns.values
            ]

            # Fill NaN values
            features = features.fillna(0)

            # Select numeric columns only
            numeric_cols = features.select_dtypes(include=[np.number]).columns
            return features[numeric_cols]

        except Exception as e:
            logger.error(f"Error preparing DNS features: {e}")
            return pd.DataFrame()

    def _prepare_response_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Prepare features for response time analysis."""
        try:
            # Create rolling statistics
            df_sorted = df.sort_values(["domain", "timestamp"])

            features = []
            for domain in df["domain"].unique():
                domain_df = df_sorted[df_sorted["domain"] == domain].copy()

                # Rolling statistics
                domain_df["rt_rolling_mean"] = (
                    domain_df["response_time"].rolling(
                        window=10, min_periods=1).mean())
                domain_df["rt_rolling_std"] = (
                    domain_df["response_time"].rolling(
                        window=10, min_periods=1).std())
                domain_df["rt_rolling_max"] = (
                    domain_df["response_time"].rolling(
                        window=10, min_periods=1).max())

                # Time-based features
                domain_df["rt_diff"] = domain_df["response_time"].diff()
                domain_df["rt_pct_change"] = domain_df["response_time"].pct_change()

                features.append(domain_df)

            combined_df = pd.concat(features, ignore_index=True)

            # Select relevant columns
            feature_cols = [
                "response_time",
                "rt_rolling_mean",
                "rt_rolling_std",
                "rt_rolling_max",
                "rt_diff",
                "rt_pct_change",
                "hour",
                "day_of_week",
            ]

            result = combined_df[feature_cols].fillna(0)
            return result

        except Exception as e:
            logger.error(f"Error preparing response time features: {e}")
            return pd.DataFrame()

    def load_trained_models(self) -> bool:
        """Load previously trained models."""
        try:
            model_files = [
                ("dns_health",
                 "dns_health_model.pkl",
                 "dns_health_scaler.pkl"),
                ("response_time",
                    "response_time_model.pkl",
                    "response_time_scaler.pkl",
                 ),
            ]

            loaded = 0
            for model_name, model_file, scaler_file in model_files:
                model_path = self.models_path / model_file
                scaler_path = self.models_path / scaler_file

                if model_path.exists() and scaler_path.exists():
                    self.models[model_name] = joblib.load(model_path)
                    self.scalers[model_name] = joblib.load(scaler_path)
                    loaded += 1

            logger.info(f"Loaded {loaded} trained models")
            return loaded > 0

        except Exception as e:
            logger.error(f"Error loading models: {e}")
            return False

    def detect_anomalies(self, recent_hours: int = 24) -> List[Anomaly]:
        """Detect anomalies in recent data."""
        anomalies = []

        try:
            # Load recent data
            df = self.load_historical_data(
                days=7)  # Load more data for context
            if df.empty:
                return anomalies

            recent_df = df[df["timestamp"] > (
                datetime.now() - timedelta(hours=recent_hours))]

            # Statistical anomaly detection (always available)
            anomalies.extend(self._detect_statistical_anomalies(recent_df, df))

            # ML-based detection (if available)
            if ML_AVAILABLE and self.models["dns_health"]:
                anomalies.extend(self._detect_ml_anomalies(recent_df))

            # Pattern-based detection
            anomalies.extend(self._detect_pattern_anomalies(df))

            logger.info(f"Detected {len(anomalies)} anomalies in recent data")

        except Exception as e:
            logger.error(f"Error detecting anomalies: {e}")

        return anomalies

    def _detect_statistical_anomalies(
        self, recent_df: pd.DataFrame, full_df: pd.DataFrame
    ) -> List[Anomaly]:
        """Detect anomalies using statistical methods."""
        anomalies = []

        try:
            for domain in recent_df["domain"].unique():
                domain_recent = recent_df[recent_df["domain"] == domain]
                domain_full = full_df[full_df["domain"] == domain]

                if len(domain_full) < 10:  # Need enough data
                    continue

                # Response time anomalies
                rt_mean = domain_full["response_time"].mean()
                rt_std = domain_full["response_time"].std()

                for _, row in domain_recent.iterrows():
                    rt = row["response_time"]

                    # Z-score based detection
                    if rt_std > 0:
                        z_score = abs(rt - rt_mean) / rt_std

                        if z_score > 3:  # 3-sigma rule
                            severity = "critical" if z_score > 5 else "high"
                            anomalies.append(
                                Anomaly(
                                    timestamp=row["timestamp"],
                                    component="dns",
                                    metric="response_time",
                                    value=rt,
                                    expected_range=(
                                        rt_mean - 2 * rt_std,
                                        rt_mean + 2 * rt_std,
                                    ),
                                    severity=severity,
                                    confidence=min(z_score / 5, 1.0),
                                    description=f"Response time anomaly for {domain}: {rt:.3f}s (Z-score: {z_score:.2f})",
                                    suggested_action=f"Check network connectivity and DNS configuration for {domain}",
                                )
                            )

                # Health rate anomalies
                recent_health_rate = domain_recent["is_healthy"].mean()
                historical_health_rate = domain_full["is_healthy"].mean()

                if recent_health_rate < historical_health_rate * 0.7:  # 30% drop
                    severity = "critical" if recent_health_rate < 0.5 else "high"
                    anomalies.append(
                        Anomaly(
                            timestamp=datetime.now(),
                            component="dns",
                            metric="health_rate",
                            value=recent_health_rate,
                            expected_range=(
                                historical_health_rate * 0.8,
                                1.0),
                            severity=severity,
                            confidence=0.9,
                            description=f"Health rate drop for {domain}: {
                                recent_health_rate:.1%} vs expected {
                                historical_health_rate:.1%}",
                            suggested_action=f"Investigate DNS configuration and nameserver status for {domain}",
                        ))

        except Exception as e:
            logger.error(f"Error in statistical anomaly detection: {e}")

        return anomalies

    def _detect_ml_anomalies(self, recent_df: pd.DataFrame) -> List[Anomaly]:
        """Detect anomalies using ML models."""
        anomalies = []

        try:
            if not self.models["dns_health"] or not self.scalers["dns_health"]:
                return anomalies

            # Prepare features for recent data
            dns_features = self._prepare_dns_features(recent_df)

            if not dns_features.empty:
                # Scale features
                scaled_features = self.scalers["dns_health"].transform(
                    dns_features)

                # Predict anomalies
                predictions = self.models["dns_health"].predict(
                    scaled_features)
                scores = self.models["dns_health"].score_samples(
                    scaled_features)

                # Convert predictions to anomalies
                for i, (prediction, score) in enumerate(
                        zip(predictions, scores)):
                    if prediction == -1:  # Anomaly detected
                        confidence = 1 - (score + 0.5)  # Normalize score
                        severity = (
                            "critical"
                            if confidence > 0.8
                            else "high" if confidence > 0.6 else "medium"
                        )

                        anomalies.append(
                            Anomaly(
                                timestamp=datetime.now(),
                                component="dns",
                                metric="ml_health_pattern",
                                value=score,
                                expected_range=(-0.1, 0.1),
                                severity=severity,
                                confidence=confidence,
                                description=f"ML model detected anomalous DNS health pattern (score: {score:.3f})",
                                suggested_action="Review DNS health metrics and check for configuration issues",
                            )
                        )

        except Exception as e:
            logger.error(f"Error in ML anomaly detection: {e}")

        return anomalies

    def _detect_pattern_anomalies(self, df: pd.DataFrame) -> List[Anomaly]:
        """Detect pattern-based anomalies."""
        anomalies = []

        try:
            # Check for recurring failure patterns
            for domain in df["domain"].unique():
                domain_df = df[df["domain"] == domain].sort_values("timestamp")

                # Look for consecutive failures
                failures = domain_df[domain_df["is_healthy"] == 0]

                if len(failures) >= 3:
                    # Check if failures are recent and consecutive
                    recent_failures = failures[failures["timestamp"] > (
                        datetime.now() - timedelta(hours=6))]

                    if len(recent_failures) >= 2:
                        anomalies.append(
                            Anomaly(
                                timestamp=datetime.now(),
                                component="dns",
                                metric="failure_pattern",
                                value=len(recent_failures),
                                expected_range=(
                                    0,
                                    1),
                                severity="high",
                                confidence=0.85,
                                description=f"Pattern of consecutive DNS failures detected for {domain}: {
                                    len(recent_failures)} failures in 6 hours",
                                suggested_action=f"Urgent: Check nameserver configuration and network connectivity for {domain}",
                            ))

                # Look for response time spikes
                if len(domain_df) > 10:
                    rt_median = domain_df["response_time"].median()
                    recent_rt = domain_df.tail(5)["response_time"].mean()

                    if recent_rt > rt_median * 3 and rt_median > 0:
                        anomalies.append(
                            Anomaly(
                                timestamp=datetime.now(),
                                component="dns",
                                metric="response_spike",
                                value=recent_rt,
                                expected_range=(0, rt_median * 2),
                                severity="medium",
                                confidence=0.75,
                                description=f"Response time spike detected for {domain}: {
                                    recent_rt:.3f}s vs median {
                                    rt_median:.3f}s",
                                suggested_action=f"Monitor network performance and DNS server load for {domain}",
                            )
                        )

        except Exception as e:
            logger.error(f"Error in pattern anomaly detection: {e}")

        return anomalies

    def generate_anomaly_report(
            self, anomalies: List[Anomaly]) -> Dict[str, Any]:
        """Generate a comprehensive anomaly report."""
        if not anomalies:
            return {
                "timestamp": datetime.now().isoformat(),
                "summary": "No anomalies detected",
                "total_anomalies": 0,
                "severity_breakdown": {},
                "recommendations": ["System is operating normally"],
            }

        # Categorize by severity
        severity_counts = defaultdict(int)
        component_counts = defaultdict(int)

        for anomaly in anomalies:
            severity_counts[anomaly.severity] += 1
            component_counts[anomaly.component] += 1

        # Generate recommendations
        recommendations = []

        if severity_counts["critical"] > 0:
            recommendations.append(
                "🚨 Critical anomalies detected - immediate action required"
            )
        if severity_counts["high"] > 2:
            recommendations.append(
                "⚠️ Multiple high-severity issues - prioritize investigation"
            )
        if component_counts["dns"] > len(anomalies) * 0.7:
            recommendations.append(
                "🌐 DNS-focused issues - check nameserver configurations"
            )

        recommendations.extend(
            [
                "📊 Review historical trends for patterns",
                "🔄 Consider adjusting monitoring thresholds",
                "📱 Ensure alert channels are working properly",
            ]
        )

        return {
            "timestamp": datetime.now().isoformat(),
            "summary": f"Detected {
                len(anomalies)} anomalies across {
                len(component_counts)} components",
            "total_anomalies": len(anomalies),
            "severity_breakdown": dict(severity_counts),
            "component_breakdown": dict(component_counts),
            "anomalies": [asdict(anomaly) for anomaly in anomalies],
            "recommendations": recommendations,
            "ml_status": "enabled" if ML_AVAILABLE else "statistical_only",
        }

    def run_analysis(self, train_models: bool = False) -> Dict[str, Any]:
        """Run complete anomaly analysis."""
        logger.info("Starting AI-powered anomaly analysis...")

        try:
            # Load or train models
            if train_models or not self.load_trained_models():
                logger.info("Training new anomaly detection models...")
                df = self.load_historical_data(days=30)
                self.train_anomaly_models(df)

            # Detect anomalies
            anomalies = self.detect_anomalies(recent_hours=24)

            # Generate report
            report = self.generate_anomaly_report(anomalies)

            # Save report
            with open("ai_anomaly_report.json", "w") as f:
                json.dump(report, f, indent=2, default=str)

            logger.info(
                f"Anomaly analysis complete - found {len(anomalies)} anomalies")

            return report

        except Exception as e:
            logger.error(f"Error in anomaly analysis: {e}")
            return {
                "timestamp": datetime.now().isoformat(),
                "error": str(e),
                "total_anomalies": 0,
            }


def main():
    """Main entry point for AI anomaly detection."""
    try:
        detector = AIAnomalyDetector()

        # Check for train flag
        train_models = "--train" in sys.argv

        # Run analysis
        report = detector.run_analysis(train_models=train_models)

        # Display summary
        print(f"\n🤖 AI ANOMALY DETECTION REPORT")
        print(f"Timestamp: {report['timestamp']}")
        print(f"Total Anomalies: {report['total_anomalies']}")

        if "severity_breakdown" in report:
            print(f"Severity Breakdown: {report['severity_breakdown']}")

        if "recommendations" in report:
            print(f"\nRecommendations:")
            for rec in report["recommendations"]:
                print(f"  • {rec}")

        print(f"\n📄 Full report saved to ai_anomaly_report.json")

    except KeyboardInterrupt:
        logger.info("AI anomaly detection interrupted by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
