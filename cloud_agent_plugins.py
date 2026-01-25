#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║   🔌 NOIZYLAB CLOUD AGENT PLUGIN SYSTEM                                  ║
║                                                                           ║
║   Extensible plugin architecture for custom task handlers               ║
║   and integrations                                                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import asyncio
import importlib
import inspect
import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass

# ═══════════════════════════════════════════════════════════════════════════
# PLUGIN BASE CLASS
# ═══════════════════════════════════════════════════════════════════════════

class CloudAgentPlugin(ABC):
    """
    Base class for cloud agent plugins.
    
    Plugins can register custom task handlers, middleware, and hooks.
    """
    
    def __init__(self):
        self.name = self.__class__.__name__
        self.logger = logging.getLogger(f"Plugin.{self.name}")
    
    @abstractmethod
    def get_handlers(self) -> Dict[str, Callable]:
        """
        Return dict of task type -> handler function mappings.
        
        Example:
            return {
                "my-custom-task": self.handle_custom_task,
                "another-task": self.handle_another
            }
        """
        pass
    
    def on_load(self):
        """Called when plugin is loaded"""
        self.logger.info(f"✅ Plugin {self.name} loaded")
    
    def on_unload(self):
        """Called when plugin is unloaded"""
        self.logger.info(f"👋 Plugin {self.name} unloaded")
    
    def before_task(self, task_type: str, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Hook called before task execution.
        Can modify task_data and return it.
        """
        return task_data
    
    def after_task(self, task_type: str, result: Any) -> Any:
        """
        Hook called after task execution.
        Can modify result and return it.
        """
        return result
    
    def on_error(self, task_type: str, error: Exception):
        """Hook called when task fails"""
        self.logger.error(f"Task {task_type} failed: {error}")

# ═══════════════════════════════════════════════════════════════════════════
# PLUGIN MANAGER
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class PluginMetadata:
    """Plugin metadata"""
    name: str
    version: str
    author: str
    description: str
    task_types: List[str]

class PluginManager:
    """
    Manages plugin lifecycle, discovery, and task routing.
    """
    
    def __init__(self, plugin_dir: Optional[Path] = None):
        """
        Initialize plugin manager.
        
        Args:
            plugin_dir: Directory to search for plugins
        """
        self.plugin_dir = plugin_dir or Path("plugins")
        self.plugins: Dict[str, CloudAgentPlugin] = {}
        self.handlers: Dict[str, Callable] = {}
        self.logger = logging.getLogger("PluginManager")
    
    def discover_plugins(self) -> List[str]:
        """
        Discover available plugins in plugin directory.
        
        Returns:
            List of discovered plugin module names
        """
        if not self.plugin_dir.exists():
            self.logger.warning(f"Plugin directory not found: {self.plugin_dir}")
            return []
        
        discovered = []
        
        for file_path in self.plugin_dir.glob("*.py"):
            if file_path.name.startswith("_"):
                continue
            
            module_name = file_path.stem
            discovered.append(module_name)
        
        self.logger.info(f"🔍 Discovered {len(discovered)} plugins: {discovered}")
        return discovered
    
    def load_plugin(self, module_name: str):
        """
        Load a plugin from module name.
        
        Args:
            module_name: Name of plugin module to load
        """
        try:
            # Import module
            module = importlib.import_module(f"plugins.{module_name}")
            
            # Find plugin class (subclass of CloudAgentPlugin)
            plugin_class = None
            for name, obj in inspect.getmembers(module):
                if (inspect.isclass(obj) and 
                    issubclass(obj, CloudAgentPlugin) and 
                    obj != CloudAgentPlugin):
                    plugin_class = obj
                    break
            
            if plugin_class is None:
                self.logger.error(f"No plugin class found in {module_name}")
                return
            
            # Instantiate plugin
            plugin = plugin_class()
            
            # Register handlers
            handlers = plugin.get_handlers()
            for task_type, handler in handlers.items():
                if task_type in self.handlers:
                    self.logger.warning(
                        f"Task type '{task_type}' already registered, overwriting"
                    )
                self.handlers[task_type] = handler
                self.logger.info(f"  ✅ Registered handler: {task_type}")
            
            self.plugins[module_name] = plugin
            plugin.on_load()
            
            self.logger.info(f"🔌 Plugin loaded: {module_name}")
        
        except Exception as e:
            self.logger.error(f"Failed to load plugin {module_name}: {e}")
    
    def unload_plugin(self, module_name: str):
        """
        Unload a plugin.
        
        Args:
            module_name: Name of plugin to unload
        """
        if module_name not in self.plugins:
            self.logger.warning(f"Plugin {module_name} not loaded")
            return
        
        plugin = self.plugins[module_name]
        
        # Remove handlers
        handlers = plugin.get_handlers()
        for task_type in handlers.keys():
            if task_type in self.handlers:
                del self.handlers[task_type]
        
        # Call unload hook
        plugin.on_unload()
        
        # Remove plugin
        del self.plugins[module_name]
        
        self.logger.info(f"🔌 Plugin unloaded: {module_name}")
    
    def load_all_plugins(self):
        """Discover and load all available plugins"""
        plugins = self.discover_plugins()
        for plugin_name in plugins:
            self.load_plugin(plugin_name)
    
    async def execute_task(
        self,
        task_type: str,
        task_data: Dict[str, Any]
    ) -> Any:
        """
        Execute task through appropriate handler.
        
        Args:
            task_type: Type of task to execute
            task_data: Task input data
        
        Returns:
            Task result
        
        Raises:
            ValueError: If no handler found for task type
        """
        if task_type not in self.handlers:
            raise ValueError(f"No handler registered for task type: {task_type}")
        
        handler = self.handlers[task_type]
        
        # Call before_task hooks
        for plugin in self.plugins.values():
            task_data = plugin.before_task(task_type, task_data)
        
        try:
            # Execute handler
            if asyncio.iscoroutinefunction(handler):
                result = await handler(task_data)
            else:
                result = handler(task_data)
            
            # Call after_task hooks
            for plugin in self.plugins.values():
                result = plugin.after_task(task_type, result)
            
            return result
        
        except Exception as e:
            # Call error hooks
            for plugin in self.plugins.values():
                plugin.on_error(task_type, e)
            
            raise
    
    def get_available_tasks(self) -> List[str]:
        """Get list of all available task types"""
        return list(self.handlers.keys())
    
    def get_plugin_info(self) -> Dict[str, Any]:
        """Get information about loaded plugins"""
        return {
            "loaded_plugins": len(self.plugins),
            "registered_handlers": len(self.handlers),
            "plugins": {
                name: {
                    "class": plugin.__class__.__name__,
                    "handlers": list(plugin.get_handlers().keys())
                }
                for name, plugin in self.plugins.items()
            }
        }

# ═══════════════════════════════════════════════════════════════════════════
# EXAMPLE PLUGINS
# ═══════════════════════════════════════════════════════════════════════════

class DataProcessingPlugin(CloudAgentPlugin):
    """Example plugin for data processing tasks"""
    
    def get_handlers(self) -> Dict[str, Callable]:
        return {
            "csv-parser": self.parse_csv,
            "json-merger": self.merge_json,
            "data-validator": self.validate_data
        }
    
    async def parse_csv(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Parse CSV data"""
        import csv
        import io
        
        csv_content = data.get("content", "")
        delimiter = data.get("delimiter", ",")
        
        reader = csv.DictReader(io.StringIO(csv_content), delimiter=delimiter)
        rows = list(reader)
        
        return {
            "row_count": len(rows),
            "columns": reader.fieldnames if reader.fieldnames else [],
            "data": rows[:100]  # Limit to first 100 rows
        }
    
    async def merge_json(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Merge multiple JSON objects"""
        objects = data.get("objects", [])
        
        if not objects:
            return {}
        
        merged = {}
        for obj in objects:
            if isinstance(obj, dict):
                merged.update(obj)
        
        return merged
    
    async def validate_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate data against rules"""
        value = data.get("value")
        rules = data.get("rules", {})
        
        errors = []
        
        if "type" in rules:
            expected_type = rules["type"]
            if expected_type == "string" and not isinstance(value, str):
                errors.append(f"Expected string, got {type(value).__name__}")
            elif expected_type == "number" and not isinstance(value, (int, float)):
                errors.append(f"Expected number, got {type(value).__name__}")
        
        if "min_length" in rules and isinstance(value, str):
            if len(value) < rules["min_length"]:
                errors.append(f"String length {len(value)} < minimum {rules['min_length']}")
        
        if "max_length" in rules and isinstance(value, str):
            if len(value) > rules["max_length"]:
                errors.append(f"String length {len(value)} > maximum {rules['max_length']}")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors
        }

class AIPlugin(CloudAgentPlugin):
    """Example plugin for AI/ML tasks"""
    
    def get_handlers(self) -> Dict[str, Callable]:
        return {
            "text-summarizer": self.summarize_text,
            "keyword-extractor": self.extract_keywords,
            "sentiment-scorer": self.score_sentiment
        }
    
    async def summarize_text(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Summarize text (simple extractive summary)"""
        text = data.get("text", "")
        max_sentences = data.get("max_sentences", 3)
        
        sentences = text.split(". ")
        summary_sentences = sentences[:max_sentences]
        
        return {
            "summary": ". ".join(summary_sentences),
            "original_length": len(text),
            "summary_length": len(". ".join(summary_sentences)),
            "compression_ratio": len(". ".join(summary_sentences)) / len(text) if len(text) > 0 else 0
        }
    
    async def extract_keywords(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract keywords from text"""
        text = data.get("text", "").lower()
        max_keywords = data.get("max_keywords", 10)
        
        # Simple word frequency
        words = text.split()
        stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for"}
        
        word_freq: Dict[str, int] = {}
        for word in words:
            word = word.strip(".,!?;:")
            if word and word not in stopwords and len(word) > 3:
                word_freq[word] = word_freq.get(word, 0) + 1
        
        keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:max_keywords]
        
        return {
            "keywords": [{"word": k, "frequency": v} for k, v in keywords],
            "total_words": len(words),
            "unique_words": len(word_freq)
        }
    
    async def score_sentiment(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Score text sentiment"""
        text = data.get("text", "").lower()
        
        positive = ["good", "great", "excellent", "amazing", "wonderful", "love", "best"]
        negative = ["bad", "terrible", "awful", "horrible", "hate", "worst", "poor"]
        
        pos_count = sum(text.count(word) for word in positive)
        neg_count = sum(text.count(word) for word in negative)
        
        if pos_count > neg_count:
            sentiment = "positive"
            score = min(1.0, pos_count / (pos_count + neg_count))
        elif neg_count > pos_count:
            sentiment = "negative"
            score = max(-1.0, -neg_count / (pos_count + neg_count))
        else:
            sentiment = "neutral"
            score = 0.0
        
        return {
            "sentiment": sentiment,
            "score": round(score, 2),
            "positive_indicators": pos_count,
            "negative_indicators": neg_count
        }

# ═══════════════════════════════════════════════════════════════════════════
# DEMO
# ═══════════════════════════════════════════════════════════════════════════

async def main():
    """Demo plugin system"""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    
    # Create manager and register plugins
    manager = PluginManager()
    
    # Manually register example plugins
    data_plugin = DataProcessingPlugin()
    ai_plugin = AIPlugin()
    
    manager.plugins["data_processing"] = data_plugin
    manager.plugins["ai"] = ai_plugin
    
    # Register handlers
    for plugin in manager.plugins.values():
        for task_type, handler in plugin.get_handlers().items():
            manager.handlers[task_type] = handler
            plugin.on_load()
    
    print("\n" + "="*70)
    print("🔌 PLUGIN SYSTEM DEMO")
    print("="*70)
    
    info = manager.get_plugin_info()
    print(f"\n📊 Plugin Info:")
    print(f"  Loaded Plugins: {info['loaded_plugins']}")
    print(f"  Registered Handlers: {info['registered_handlers']}")
    print(f"\n  Available Tasks:")
    for task in manager.get_available_tasks():
        print(f"    - {task}")
    
    # Test data processing plugin
    print("\n" + "="*70)
    print("Testing Data Processing Plugin")
    print("="*70)
    
    csv_result = await manager.execute_task("csv-parser", {
        "content": "name,age,city\nAlice,30,NYC\nBob,25,LA",
        "delimiter": ","
    })
    print(f"\nCSV Parser Result:")
    print(f"  Rows: {csv_result['row_count']}")
    print(f"  Columns: {csv_result['columns']}")
    
    # Test AI plugin
    print("\n" + "="*70)
    print("Testing AI Plugin")
    print("="*70)
    
    sentiment_result = await manager.execute_task("sentiment-scorer", {
        "text": "This product is amazing! I love it. Best purchase ever!"
    })
    print(f"\nSentiment Analysis:")
    print(f"  Sentiment: {sentiment_result['sentiment']}")
    print(f"  Score: {sentiment_result['score']}")
    
    keywords_result = await manager.execute_task("keyword-extractor", {
        "text": "Cloud computing enables scalable infrastructure. Cloud services provide flexibility.",
        "max_keywords": 5
    })
    print(f"\nKeyword Extraction:")
    for kw in keywords_result['keywords']:
        print(f"  - {kw['word']}: {kw['frequency']}")
    
    print("\n✅ Plugin system demo complete!")


if __name__ == "__main__":
    asyncio.run(main())
