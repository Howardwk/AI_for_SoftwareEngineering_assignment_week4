# AI in Software Engineering - Assignment

**Course**: PLP 2 - AI Course Work  
**Week**: 4  
**Assignment**: AI Applications in Software Engineering

---

## 📋 Overview

This assignment demonstrates AI applications in software engineering through theoretical analysis, practical implementation, and ethical reflection. The project showcases how AI can automate tasks, enhance decision-making, and address challenges in software development.

### Submission Components

1. **Code**: Well-commented scripts and notebooks (GitHub)
2. **Report**: PDF with answers, screenshots, and reflections (Community article)
3. **Presentation**: 3-minute video demo (Groups for peer review)

### Grading Criteria

| Criteria | Weight |
|----------|--------|
| Theoretical Depth & Accuracy | 30% |
| Code Functionality & Quality | 50% |
| Ethical Reflection | 10% |
| Creativity & Presentation | 10% |

---

## 🗂️ Project Structure

```
assignment/
│
├── theoretical_analysis.md          # Q1-Q3 answers + case study
├── ethical_reflection.md            # Bias analysis + AIF360 discussion
│
├── task1_code_completion.py         # AI-powered code completion demo
├── task1_analysis.md                # Code comparison analysis
│
├── task2_automated_testing.py       # Selenium automated testing
├── task2_analysis.md                # Testing coverage analysis
├── task2_test_results.json          # Test execution results
│
├── task3_predictive_analytics.py    # Random Forest classification
├── task3_predictive_analytics.ipynb # Jupyter notebook version
├── task3_performance_metrics.csv    # Model evaluation metrics
│
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
│
└── screenshots/                     # Visual outputs
    ├── task1_*.png
    ├── task2_*.png
    └── task3_*.png
```

---

## 📚 Part 1: Theoretical Analysis (30%)

### Questions Covered

**Q1: AI-Driven Code Generation Tools**
- How GitHub Copilot reduces development time
- Limitations and security concerns
- Use cases and best practices

**Q2: Supervised vs Unsupervised Learning for Bug Detection**
- Comparative analysis of both approaches
- Advantages and disadvantages
- Real-world applications

**Q3: Bias Mitigation in Personalization**
- Importance of fairness in AI systems
- Legal and ethical implications
- Business impacts

**Case Study: AIOps in DevOps**
- How AI improves deployment efficiency
- Two concrete examples with metrics
- Benefits and ROI

**📄 See**: `theoretical_analysis.md`

---

## 💻 Part 2: Practical Implementation (60%)

### Task 1: AI-Powered Code Completion

**Objective**: Compare AI-suggested code with manual implementation for sorting dictionaries.

**Files**:
- `task1_code_completion.py`: Implementation with manual and AI versions
- `task1_analysis.md`: 200-word efficiency analysis

**Run**:
```bash
python task1_code_completion.py
```

**Key Findings**:
- AI-suggested `itemgetter` is 10-30% more efficient than lambda
- Better memory usage and Pythonic code
- Compiled C implementation advantage

---

### Task 2: Automated Testing with AI

**Objective**: Automate login page testing with Selenium WebDriver.

**Files**:
- `task2_automated_testing.py`: Complete test suite
- `task2_analysis.md`: Coverage analysis (150 words)
- `task2_test_results.json`: Execution results

**Run**:
```bash
python task2_automated_testing.py
```

**Features**:
- Valid login test
- Invalid username/password tests
- Empty credentials validation
- JSON results export

**Key Findings**:
- 10-100x faster than manual testing
- 100% consistency
- Comprehensive edge case coverage
- Automated regression testing

**⚠️ Prerequisites**:
```bash
pip install selenium
# Install ChromeDriver from https://chromedriver.chromium.org/
```

---

### Task 3: Predictive Analytics for Resource Allocation

**Objective**: Train Random Forest model on breast cancer dataset to predict issue priority.

**Files**:
- `task3_predictive_analytics.py`: Python script version
- `task3_predictive_analytics.ipynb`: Jupyter notebook
- `task3_performance_metrics.csv`: Evaluation results

**Run**:
```bash
python task3_predictive_analytics.py
```

**Or use Jupyter Notebook**:
```bash
jupyter notebook task3_predictive_analytics.ipynb
```

**Model Performance**:
- **Accuracy**: ~95-98%
- **F1-Score**: ~0.96-0.98
- **Precision**: ~0.96
- **Recall**: ~0.97
- **ROC AUC**: ~0.99

**Outputs Generated**:
- Target distribution plots
- Correlation heatmap
- Confusion matrix
- Feature importance visualization
- ROC curve

---

## 🤔 Part 3: Ethical Reflection (10%)

**Objective**: Analyze potential biases and discuss fairness mitigation.

**File**: `ethical_reflection.md`

### Topics Covered

**Part 1: Potential Biases**
1. Demographics and representation bias
2. Age and socioeconomic bias
3. Data collection and medical practice bias
4. Labeling and ground truth bias

**Part 2: IBM AI Fairness 360 Solutions**
1. **Metrics**: Statistical Parity, Equalized Odds, Calibration
2. **Algorithms**:
   - Reweighing (pre-processing)
   - Adversarial Debiasing
   - Post-processing calibration
3. **Implementation**: Complete code examples

**Part 3: Ethical Considerations**
1. Transparency and explainability
2. Continuous monitoring
3. Human-in-the-loop design
4. Regulatory compliance
5. Patient autonomy

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- ChromeDriver (for Task 2)

### Install Dependencies

```bash
# Clone or download this repository
cd assignment

# Install Python packages
pip install -r requirements.txt
```

### Setup ChromeDriver (Task 2)

**Option 1: Using webdriver-manager** (recommended)
```bash
pip install webdriver-manager
```

**Option 2: Manual installation**
1. Download from: https://chromedriver.chromium.org/
2. Add to system PATH
3. Or specify path in script

---

## 🚀 Running the Project

### Run All Tasks

```bash
# Task 1: Code Completion
python task1_code_completion.py

# Task 2: Automated Testing
python task2_automated_testing.py

# Task 3: Predictive Analytics
python task3_predictive_analytics.py
```

### Individual Task Execution

#### Task 1
```bash
python task1_code_completion.py
```
**Output**: Performance comparison analysis

#### Task 2
```bash
python task2_automated_testing.py
```
**Output**: Test results saved to `task2_test_results.json`

#### Task 3
```bash
python task3_predictive_analytics.py
```
**Output**: 
- Performance metrics CSV
- Visualization PNGs
- Model evaluation report

**Or use Jupyter Notebook**:
```bash
jupyter notebook task3_predictive_analytics.ipynb
```

---

## 📊 Results Summary

### Task 1: Code Completion
- ✅ Manual vs AI implementation comparison
- ✅ Performance benchmarking
- ✅ Correctness validation
- **Outcome**: AI version 10-30% more efficient

### Task 2: Automated Testing
- ✅ 4 test cases executed
- ✅ 100% success rate
- ✅ JSON results export
- **Outcome**: Comprehensive coverage, 10-100x speed improvement

### Task 3: Predictive Analytics
- ✅ Data preprocessing and visualization
- ✅ Random Forest classifier trained
- ✅ Model evaluation metrics
- ✅ Feature importance analysis
- **Outcome**: 95-98% accuracy, F1-score 0.96-0.98

### Part 3: Ethical Reflection
- ✅ Bias identification in healthcare AI
- ✅ AIF360 solutions implementation
- ✅ Ethical framework discussion
- **Outcome**: Comprehensive bias mitigation strategy

---

## 📝 Deliverables Checklist

### Code & Implementation
- [x] Well-commented Python scripts
- [x] Jupyter notebook for Task 3
- [x] Test suite with results
- [x] Performance metrics
- [x] Visualizations generated

### Documentation
- [x] README.md with setup instructions
- [x] Theoretical analysis with answers
- [x] Task-specific analyses
- [x] Ethical reflection document
- [x] Requirements.txt

### Presentation Materials
- [x] Screenshot-ready outputs
- [x] Code demonstrations
- [x] Test results visualization
- [x] Model performance charts

---

## 🎯 Key Learnings

### Technical Skills
1. **AI Code Generation**: Understanding optimization through AI suggestions
2. **Test Automation**: Selenium WebDriver for comprehensive testing
3. **Predictive Modeling**: Random Forest for classification tasks
4. **Bias Mitigation**: AI Fairness 360 toolkit application

### AI Impact
- **Speed**: 10-100x improvement in testing
- **Quality**: Higher accuracy through optimized algorithms
- **Coverage**: Comprehensive edge case testing
- **Ethics**: Understanding and addressing bias

### Career Relevance
- GitHub Copilot proficiency
- Selenium automation expertise
- ML model development
- Ethical AI practices

---

## 📚 Resources & References

### Documentation
- [Selenium WebDriver Docs](https://www.selenium.dev/documentation/)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [IBM AI Fairness 360](https://aif360.mybluemix.net/)

### Datasets
- [Breast Cancer Wisconsin Dataset](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29)
- Built-in sklearn dataset (load_breast_cancer)

### Tools
- GitHub Copilot
- Selenium IDE
- Jupyter Notebook
- Google Colab

---

## 👥 Author

**Name**: [Your Name]  
**Course**: PLP 2 - AI Course Work  
**Week**: 4  
**Assignment**: AI in Software Engineering

---

## 📅 Timeline

- **Start Date**: [Date]
- **Completion Date**: [Date]
- **Deadline**: 7 days from start

---

## ⚖️ License

This project is for educational purposes as part of PLP 2 coursework.

---

## 🎓 Acknowledgments

- Course instructors for guidance
- PLP 2 program for comprehensive AI curriculum
- Open-source community for tools and libraries
- Selenium and sklearn maintainers

---

## 📞 Contact & Support

For questions or issues:
- Course forum
- GitHub issues
- Peer group discussions

---

**Good luck with your AI journey! 🚀**

