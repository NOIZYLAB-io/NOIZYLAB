# 🔍 GEMINI CODE ANALYZER

## ✅ **NEW CODE ANALYSIS SYSTEM!**

Using Gemini 3 Pro to analyze code for bugs, race conditions, and issues!

---

## 🚀 **QUICK START**

### **1. Install:**
```bash
pip install -q -U google-genai
```

### **2. Set API Key:**
```bash
export GEMINI_API_KEY='your-api-key-here'
```

### **3. Use:**
```python
from gemini_database.gemini_code_analyzer import GeminiCodeAnalyzer

analyzer = GeminiCodeAnalyzer()

# Find race conditions
result = analyzer.find_race_conditions(cpp_code, "C++")

# Find bugs
result = analyzer.find_bugs(python_code)

# Find security issues
result = analyzer.find_security_issues(code)

# Analyze performance
result = analyzer.analyze_performance(code)

# Analyze file
result = analyzer.analyze_file("mycode.py", "bugs")
```

---

## 💻 **EXAMPLE USAGE**

### **Basic Pattern (from your example):**
```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="Find the race condition in this multi-threaded C++ snippet: [code here]"
)

print(response.text)
```

### **Using the Analyzer Class:**
```python
from gemini_database.gemini_code_analyzer import GeminiCodeAnalyzer

analyzer = GeminiCodeAnalyzer()

# Analyze C++ code
cpp_code = """
#include <thread>
int counter = 0;
void increment() { counter++; }
"""

result = analyzer.find_race_conditions(cpp_code, "C++")
print(result)
```

---

## 🎯 **FEATURES**

- ✅ **Race Condition Detection** - Find threading issues
- ✅ **Bug Detection** - Find all bugs
- ✅ **Security Analysis** - Find vulnerabilities
- ✅ **Performance Analysis** - Optimize code
- ✅ **File Analysis** - Analyze entire files
- ✅ **Multi-Language** - Python, C++, Java, JavaScript, etc.

---

## 📁 **FILES**

- `gemini_code_analyzer.py` - Full analyzer class
- `example_race_condition.py` - Example using your pattern

---

## ✅ **READY TO USE!**

**Get API key:** https://aistudio.google.com/app/api-keys

**Run example:**
```bash
python3 gemini_database/example_race_condition.py
```

