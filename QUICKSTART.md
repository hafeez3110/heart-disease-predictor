# Quick Start Guide - Heart Disease Prediction

## 🚀 Getting Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Complete Pipeline
```bash
python main.py
```

This will:
- Download and load the UCI Heart Disease dataset
- Perform exploratory data analysis
- Clean and preprocess the data
- Train 5 different ML models
- Evaluate and compare all models
- Generate visualizations and reports
- Save trained models

### Step 3: Explore Results
- Check `results/` folder for visualizations
- Review `results/model_results.csv` for metrics comparison
- View saved models in `models/` directory

---

## 📊 Interactive Analysis

For interactive exploration, use the Jupyter notebook:

```bash
jupyter notebook notebooks/heart_disease_analysis.ipynb
```

---

## 📁 Project Structure

```
ml_proj2/
├── data/                   # Dataset storage
├── src/                    # Source code modules
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── utils.py
├── notebooks/              # Jupyter notebooks
│   └── heart_disease_analysis.ipynb
├── models/                 # Saved models
├── results/                # Evaluation results
├── main.py                 # Main pipeline script
├── requirements.txt        # Dependencies
└── README.md              # Documentation
```

---

## 🎯 Using Individual Modules

### Data Preprocessing
```python
from src.data_preprocessing import DataPreprocessor

preprocessor = DataPreprocessor()
df = preprocessor.load_data()
df_clean = preprocessor.clean_data(df)
X_train, X_test, y_train, y_test = preprocessor.prepare_features(df_clean)
```

### Model Training
```python
from src.model_training import ModelTrainer

trainer = ModelTrainer()
trainer.initialize_models()
models = trainer.train_basic_models(X_train, y_train)
```

### Model Evaluation
```python
from src.model_evaluation import ModelEvaluator

evaluator = ModelEvaluator()
results = evaluator.evaluate_all_models(models, X_test, y_test)
```

---

## 🔮 Making Predictions

```python
import joblib

# Load the saved model and scaler
model = joblib.load('models/random_forest.pkl')
scaler = joblib.load('models/scaler.pkl')

# Prepare new patient data
new_patient = [[63, 1, 3, 145, 233, 1, 0, 150, 0, 2.3, 0, 0, 1]]
new_patient_scaled = scaler.transform(new_patient)

# Make prediction
prediction = model.predict(new_patient_scaled)
probability = model.predict_proba(new_patient_scaled)

print(f"Prediction: {'Disease' if prediction[0] == 1 else 'No Disease'}")
print(f"Probability: {probability[0][1]:.2%}")
```

---

## 📈 Expected Results

The pipeline typically achieves:
- **Accuracy**: 75-85%
- **Precision**: 75-90%
- **Recall**: 70-85%
- **F1-Score**: 75-85%

Best performing models are usually:
1. Random Forest
2. Logistic Regression
3. Support Vector Machine

---

## 🛠️ Customization

### Change test size:
In `main.py` or modules, modify:
```python
X_train, X_test, y_train, y_test = preprocessor.prepare_features(df_clean, test_size=0.3)
```

### Enable hyperparameter tuning:
Uncomment in `main.py`:
```python
models = trainer.tune_hyperparameters(X_train, y_train, cv=5)
```

### Add more models:
In `src/model_training.py`, add to `initialize_models()`:
```python
'Gradient Boosting': GradientBoostingClassifier(random_state=42)
```

---

## 🐛 Troubleshooting

**Issue**: Dataset download fails
**Solution**: The script will automatically download from UCI repository. Check internet connection.

**Issue**: Missing packages
**Solution**: Run `pip install -r requirements.txt`

**Issue**: Jupyter notebook won't open
**Solution**: Run `pip install jupyter notebook`

---

## 📚 Learn More

- [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Project README](README.md)

---

**Happy Predicting! 🎉**
