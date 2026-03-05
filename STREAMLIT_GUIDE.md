# 🎈 Streamlit Dashboard Guide

## Overview

This guide will help you use the Heart Disease Prediction Streamlit dashboard. The app provides an interactive web interface for making predictions, viewing model performance, and analyzing results.

## 🚀 Quick Start

### 1. Install Dependencies

First, make sure you have all required packages installed:

```bash
pip install -r requirements.txt
```

### 2. Train Models

Before running the dashboard, train the models by running:

```bash
python main.py
```

This will:
- Download and process the dataset
- Train all 5 machine learning models
- Save models to the `models/` directory
- Generate performance metrics in `results/`

### 3. Launch the Dashboard

Start the Streamlit app:

```bash
streamlit run app.py
```

The dashboard will open automatically in your browser at `http://localhost:8501`

If it doesn't open automatically, navigate to the URL shown in your terminal.

## 📋 Dashboard Features

### Page 1: 🔍 Prediction

**Purpose:** Make predictions for individual patients

**How to Use:**
1. Fill in all 13 patient parameters using the interactive controls
2. Click "Predict Heart Disease Risk"
3. View results including:
   - Risk level (High/Low)
   - Confidence score
   - Detailed recommendations
   - Patient summary

**Input Parameters:**

| Parameter | Description | Range |
|-----------|-------------|-------|
| Age | Patient's age in years | 20-100 |
| Sex | 0 = Female, 1 = Male | 0 or 1 |
| Chest Pain Type | Type of chest pain | 0-3 |
| Resting BP | Blood pressure at rest (mm Hg) | 90-200 |
| Cholesterol | Serum cholesterol (mg/dl) | 100-400 |
| Fasting Blood Sugar | > 120 mg/dl | 0 or 1 |
| Resting ECG | ECG results | 0-2 |
| Max Heart Rate | Maximum heart rate achieved | 60-220 |
| Exercise Angina | Exercise induced angina | 0 or 1 |
| ST Depression | ST depression (oldpeak) | 0.0-6.0 |
| Slope | Slope of peak exercise ST | 0-2 |
| Major Vessels | Number colored by fluoroscopy | 0-3 |
| Thalassemia | Thalassemia status | 0-3 |

**Example Use Case:**
```
Patient Profile:
- 55-year-old male
- Blood pressure: 140 mm Hg
- Cholesterol: 240 mg/dl
- Experiences chest pain during exercise
```

### Page 2: 📊 Model Info

**Purpose:** View model performance and feature importance

**Tabs:**

1. **Performance Tab:**
   - View metrics for all 5 models
   - Compare accuracy, precision, recall, F1-score
   - See visual performance comparisons
   - View hyperparameter tuning results

2. **Feature Importance Tab:**
   - See which features most influence predictions
   - Interactive bar charts
   - Detailed importance scores
   - Key insights about top features

3. **Dataset Info Tab:**
   - Learn about the UCI Heart Disease Dataset
   - View feature descriptions
   - Understand data types
   - See dataset statistics

4. **About ML Tab:**
   - Learn how machine learning works
   - Understand different model types
   - Learn about performance metrics
   - Important disclaimers

### Page 3: 📁 Batch Prediction

**Purpose:** Predict risk for multiple patients at once

**How to Use:**

1. **Prepare CSV File:**
   - Download the sample template
   - Add your patient data
   - Ensure all 13 columns are present

2. **Upload File:**
   - Click "Choose a CSV file"
   - Select your prepared file
   - Preview the data

3. **Generate Predictions:**
   - Click "Generate Predictions"
   - View summary statistics
   - Examine detailed results table
   - Download results as CSV

**CSV Format:**
```csv
age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal
63,1,3,145,233,1,0,150,0,2.3,0,0,1
45,0,0,120,200,0,0,170,0,0.5,1,0,2
```

**Results Include:**
- Patient ID
- All input features
- Prediction (High/Low Risk)
- Disease probability
- No disease probability
- Risk level categorization

**Visualizations:**
- Risk distribution pie chart
- Probability distribution histogram
- Risk level bar chart
- Statistical summary

### Page 4: ℹ️ About

**Purpose:** Learn about the application

**Contents:**
- Application purpose and goals
- Technology stack information
- Feature list
- Model performance summary
- Medical disclaimer
- Support resources
- Health tips

## 💡 Tips for Best Results

### Input Quality
- Use accurate, measured values when possible
- Avoid extreme outliers
- Ensure all values are within valid ranges
- Double-check units (mm Hg, mg/dl, etc.)

### Interpreting Results

**High Risk:**
- Probability > 50% indicates disease presence
- Red indicators show high risk
- Follow medical consultation recommendations

**Low Risk:**
- Probability < 50% indicates no disease
- Green indicators show low risk
- Continue healthy lifestyle practices

**Moderate Risk:**
- Probability 30-60% requires attention
- Yellow indicators suggest monitoring
- Consider preventive measures

### Confidence Scores
- Higher confidence = more certain prediction
- Confidence < 60% = borderline case
- Confidence > 85% = strong prediction

## 🔧 Troubleshooting

### Models Not Found
**Error:** "Models not found. Please run main.py first."

**Solution:**
```bash
python main.py
```

### Port Already in Use
**Error:** "Port 8501 is already in use"

**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Module Not Found
**Error:** "No module named 'streamlit'" or similar

**Solution:**
```bash
pip install -r requirements.txt
```

### Slow Performance
**Issue:** Dashboard loads slowly

**Solutions:**
- Reduce batch prediction size
- Clear browser cache
- Restart the Streamlit server
- Check system resources

### File Upload Errors
**Issue:** CSV upload fails

**Solutions:**
- Verify CSV format matches template
- Check all 13 columns are present
- Ensure no missing values
- Use UTF-8 encoding

## 📊 Understanding Visualizations

### Confusion Matrix
- **True Positives (TP):** Correctly identified disease cases
- **True Negatives (TN):** Correctly identified healthy cases
- **False Positives (FP):** Healthy predicted as disease
- **False Negatives (FN):** Disease predicted as healthy

### ROC Curve
- **AUC Score:** Area Under Curve (0-1)
- Higher AUC = better discrimination
- Diagonal line = random guessing
- Perfect model = AUC of 1.0

### Feature Importance
- Bars show relative importance (0-1)
- Taller bars = more influential features
- Based on model's learned patterns
- Available for tree-based models only

## 🎯 Best Practices

### For Individual Predictions
1. Enter complete, accurate data
2. Verify values before predicting
3. Review patient summary
4. Consider confidence scores
5. Follow medical recommendations

### For Batch Processing
1. Use the template as a guide
2. Validate data before upload
3. Review preview before predicting
4. Download results for records
5. Analyze distribution patterns

### For Research/Education
1. Read the dataset documentation
2. Understand model limitations
3. Compare multiple models
4. Note the disclaimers
5. Cite sources appropriately

## 🔒 Privacy & Security

### Data Handling
- No data is permanently stored by the app
- Predictions are processed in memory
- Session data is cleared on refresh
- No internet connection required after setup

### Medical Information
- This is NOT a diagnostic tool
- Not HIPAA compliant
- For educational use only
- Do not use for clinical decisions

## 🆘 Support & Resources

### Documentation
- [README.md](README.md) - Project overview
- [QUICKSTART.md](QUICKSTART.md) - Getting started
- [IMPLEMENTATION.md](IMPLEMENTATION.md) - Technical details
- [WORKFLOW.md](WORKFLOW.md) - Development workflow

### External Resources
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- [SHAP Documentation](https://shap.readthedocs.io/)

### Common Questions

**Q: How accurate is the model?**
A: Typically 80-90% accuracy on test data. Not 100% - always consult professionals.

**Q: Can I use this for real patients?**
A: No. This is for educational purposes only, not clinical use.

**Q: What model is currently active?**
A: Check the sidebar - it shows the loaded model (usually best performing).

**Q: Can I add more features?**
A: The model is trained on specific 13 features. Adding more requires retraining.

**Q: How do I save my predictions?**
A: Use the batch prediction page and click "Download Results".

**Q: Can I change the model parameters?**
A: Yes, but you need to modify and retrain via main.py or the notebook.

## 🚀 Advanced Usage

### Custom Ports
```bash
streamlit run app.py --server.port 8080
```

### Headless Mode
```bash
streamlit run app.py --server.headless true
```

### Custom Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor="#e74c3c"
backgroundColor="#ffffff"
secondaryBackgroundColor="#f0f2f6"
textColor="#262730"
font="sans serif"
```

### Performance Optimization
```bash
streamlit run app.py --server.maxUploadSize 200
```

## 📝 Version History

### Version 2.0 (Current)
- ✅ Added hyperparameter tuning support
- ✅ Added SHAP explainability
- ✅ Enhanced batch predictions
- ✅ Improved visualizations
- ✅ Added risk categorization

### Version 1.0
- ✅ Initial release
- ✅ Basic prediction interface
- ✅ Model performance metrics
- ✅ Batch processing

## 🎓 Educational Use Cases

### For Students
- Learn ML applications in healthcare
- Understand classification models
- Practice data analysis
- Explore medical datasets

### For Educators
- Demonstrate ML concepts
- Show real-world applications
- Teach model evaluation
- Discuss ethical AI use

### For Researchers
- Benchmark new models
- Test preprocessing techniques
- Compare feature engineering
- Study explainability methods

## ⚠️ Final Reminder

**THIS APPLICATION IS FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**

- Not FDA approved
- Not a medical device
- Not for clinical diagnosis
- Always consult healthcare professionals

---

**Need Help?** Check the About page in the app or review the project documentation.

**Found a Bug?** Review the code in `app.py` or consult the troubleshooting section.

**Want to Contribute?** Modify the source code and test thoroughly before deployment.

---

*Made with ❤️ using Streamlit | Powered by Machine Learning*
