# Quick Start Guide

## 🚀 Getting Started in 3 Steps

### Step 1: Install Python (if not already installed)

**Windows**:
```bash
# Download from https://www.python.org/downloads/
# Or use Microsoft Store
python --version  # Should be 3.8 or higher
```

**Mac/Linux**:
```bash
python3 --version
```

---

### Step 2: Install Dependencies

```bash
# Navigate to assignment directory
cd assignment

# Install all required packages
pip install -r requirements.txt

# Or install individually:
pip install pandas numpy matplotlib seaborn scikit-learn selenium jupyter
```

---

### Step 3: Run the Tasks

#### Option A: Run All Tasks (Full Demo)

```bash
# Task 1: AI-Powered Code Completion
python task1_code_completion.py

# Task 2: Automated Testing (requires ChromeDriver)
python task2_automated_testing.py

# Task 3: Predictive Analytics
python task3_predictive_analytics.py
```

#### Option B: Use Jupyter Notebook (Interactive)

```bash
# Start Jupyter
jupyter notebook

# Then open: task3_predictive_analytics.ipynb
# Run cells interactively
```

---

## 📋 ChromeDriver Setup (Task 2 Only)

### Automated Method (Recommended)

```bash
pip install webdriver-manager
```

Then modify `task2_automated_testing.py` line 35:
```python
# Change from:
self.driver = webdriver.Chrome(options=options)

# To:
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
self.driver = webdriver.Chrome(service=service, options=options)
```

### Manual Method

1. Visit: https://chromedriver.chromium.org/
2. Download version matching your Chrome
3. Extract to a folder in PATH
4. Or specify path in script

---

## ✅ Verification

### Quick Test

```bash
# Test Python installation
python -c "import pandas, sklearn, selenium; print('✓ All imports OK!')"

# Test individual tasks
python task1_code_completion.py  # Should run in ~5 seconds
python task3_predictive_analytics.py  # Should run in ~10 seconds
```

### Expected Outputs

**Task 1**:
```
✓ Performance comparison completed
✓ All tests passed
✓ Analysis generated
```

**Task 2**:
```
✓ WebDriver initialized
✓ Tests executed (4 passed)
✓ task2_test_results.json created
```

**Task 3**:
```
✓ Model trained
✓ Accuracy: ~0.96
✓ F1-Score: ~0.97
✓ Visualizations saved
✓ task3_performance_metrics.csv created
```

---

## 🐛 Troubleshooting

### Problem: "Python not found"

**Solution**:
- Install Python from https://python.org
- Add to PATH during installation
- Restart terminal

---

### Problem: "Module not found"

**Solution**:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Problem: "ChromeDriver not found" (Task 2)

**Solution**:
```bash
pip install webdriver-manager
# See ChromeDriver Setup above
```

---

### Problem: "Permission denied" (Mac/Linux)

**Solution**:
```bash
chmod +x task*.py
python3 task1_code_completion.py
```

---

### Problem: "Memory error" (Task 3)

**Solution**:
```bash
# Reduce dataset size in script
# Or run in Google Colab
```

---

## 📚 Additional Resources

### Google Colab (Cloud Alternative)

If local setup fails, use Google Colab:
1. Upload files to Google Drive
2. Open Google Colab
3. Run: `!pip install -r requirements.txt`
4. Execute cells

---

### Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run tasks
python task1_code_completion.py
```

---

## 📞 Need Help?

1. Check `README.md` for detailed documentation
2. Review task-specific analysis files
3. Consult course materials
4. Ask in peer group discussions

---

**Good luck! 🎉**

