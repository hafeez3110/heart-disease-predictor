# Heart Disease Prediction Using Machine Learning

## Project Overview
This project implements an end-to-end machine learning solution for predicting heart disease using various classification algorithms. The system analyzes patient medical data to predict the presence or absence of heart disease.

## Dataset
The project uses the UCI Heart Disease dataset, which contains 14 attributes:
- **age**: Age in years
- **sex**: Sex (1 = male; 0 = female)
- **cp**: Chest pain type (0-3)
- **trestbps**: Resting blood pressure (mm Hg)
- **chol**: Serum cholesterol (mg/dl)
- **fbs**: Fasting blood sugar > 120 mg/dl (1 = true; 0 = false)
- **restecg**: Resting electrocardiographic results (0-2)
- **thalach**: Maximum heart rate achieved
- **exang**: Exercise induced angina (1 = yes; 0 = no)
- **oldpeak**: ST depression induced by exercise relative to rest
- **slope**: Slope of peak exercise ST segment (0-2)
- **ca**: Number of major vessels colored by fluoroscopy (0-3)
- **thal**: Thalassemia (0-3)
- **target**: Heart disease presence (1 = disease; 0 = no disease)

## Machine Learning Models Implemented
1. **Logistic Regression**
2. **K-Nearest Neighbors (KNN)**
3. **Support Vector Machine (SVM)**
4. **Decision Tree Classifier**
5. **Random Forest Classifier**

## Project Structure
```
ml_proj2/
├── data/                   # Dataset directory
├── src/                    # Source code
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── model_evaluation.py
│   └── utils.py
├── notebooks/              # Jupyter notebooks for exploration
├── models/                 # Saved models
├── results/                # Results and visualizations
├── main.py                 # Main pipeline script
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Installation

1. Clone this repository
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

### 1. Run the complete pipeline:
```bash
python main.py
```
This will train all models, evaluate them, and save results.

### 2. Run the Streamlit web dashboard:
```bash
streamlit run app.py
```
Interactive web interface for predictions and analysis. See [STREAMLIT_GUIDE.md](STREAMLIT_GUIDE.md) for details.

### 3. Make predictions on new data:
```bash
python predict.py
```
Interactive prediction tool for individual patients.

### 4. Run the Jupyter notebook for exploration:
```bash
jupyter notebook notebooks/heart_disease_analysis.ipynb
```
Comprehensive analysis with hyperparameter tuning and SHAP explainability.

## Results
The models are evaluated using:
- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix
- ROC-AUC Score

Typical performance: **80-90% accuracy** with K-Nearest Neighbors and Random Forest performing best.

## Features

### Core Features
- ✅ Comprehensive data preprocessing and cleaning
- ✅ Exploratory Data Analysis (EDA)
- ✅ Multiple ML algorithms comparison (5 models)
- ✅ Model evaluation and visualization
- ✅ Cross-validation
- ✅ Feature importance analysis

### Advanced Features (v2.0)
- ✅ **Hyperparameter Tuning**: GridSearchCV optimization for top models
- ✅ **SHAP Explainability**: Model interpretation with multiple visualization types
- ✅ **Streamlit Dashboard**: Interactive web interface with:
  - Individual patient predictions
  - Batch prediction from CSV
  - Model performance metrics
  - Risk visualization and analysis
  - Feature importance displays

## Quick Start

1. **Setup Environment:**
```bash
pip install -r requirements.txt
```

2. **Train Models:**
```bash
python main.py
```

3. **Launch Dashboard:**
```bash
streamlit run app.py
```

4. **Make Predictions:**
Visit `http://localhost:8501` in your browser or use `predict.py`

## Documentation

- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [STREAMLIT_GUIDE.md](STREAMLIT_GUIDE.md) - Dashboard usage guide
- [IMPLEMENTATION.md](IMPLEMENTATION.md) - Technical implementation details
- [WORKFLOW.md](WORKFLOW.md) - Development workflow

## Requirements
- Python 3.8+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- jupyter
- joblib
- scipy
- **shap** (for explainability)
- **streamlit** (for web dashboard)

See [requirements.txt](requirements.txt) for specific versions.

## Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| K-Nearest Neighbors | 88.33% | 92.00% | 82.14% | 86.79% | 93.25% |
| Random Forest | 86.67% | 86.67% | 86.67% | 86.67% | 94.68% |
| Support Vector Machine | 85.00% | 84.00% | 87.50% | 85.71% | 92.86% |

*Results from latest training run. May vary slightly due to randomization.*

## Project Timeline

- **v1.0**: Basic ML pipeline with 5 models
- **v2.0**: Added hyperparameter tuning, SHAP explainability, Streamlit dashboard

## Disclaimer

⚠️ **IMPORTANT:** This project is for educational and research purposes only. It is NOT a medical diagnostic tool and should NOT be used for clinical decision-making. Always consult qualified healthcare professionals for medical advice and diagnosis.

## Author
Machine Learning Heart Disease Prediction Project

## License
MIT License

