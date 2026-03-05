# Heart Disease Prediction - Project Workflow

## 🔄 Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    HEART DISEASE PREDICTION SYSTEM                       │
│                         End-to-End ML Pipeline                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 1: DATA ACQUISITION                                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  UCI Repository  ──→  Download Dataset  ──→  Load into DataFrame        │
│                       (303 patients)         (14 attributes)            │
│                                                                          │
│  Module: data_preprocessing.py → load_data()                            │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 2: EXPLORATORY DATA ANALYSIS (EDA)                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ├─ Statistical Summary         ├─ Correlation Heatmap                  │
│  ├─ Missing Value Analysis      ├─ Feature Distributions                │
│  ├─ Target Distribution         ├─ Age vs Disease Analysis              │
│  └─ Data Quality Checks         └─ Visualizations                       │
│                                                                          │
│  Module: data_preprocessing.py → explore_data()                         │
│  Output: results/target_distribution.png, correlation_heatmap.png, etc. │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 3: DATA CLEANING & PREPROCESSING                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Raw Data ──→ Remove Missing Values ──→ Handle Duplicates               │
│                                    ↓                                     │
│              Convert Target to Binary ──→ Remove Outliers               │
│                                    ↓                                     │
│                          Clean Dataset (~297 samples)                   │
│                                                                          │
│  Module: data_preprocessing.py → clean_data()                           │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 4: FEATURE ENGINEERING                                             │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Clean Data ──→ Separate Features & Target                              │
│              ──→ Train-Test Split (80/20, stratified)                   │
│              ──→ Feature Scaling (StandardScaler)                       │
│                                                                          │
│  Training Set: ~237 samples    |    Test Set: ~60 samples              │
│                                                                          │
│  Module: data_preprocessing.py → prepare_features()                     │
│  Output: data/train_data.csv, data/test_data.csv                       │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 5: MODEL TRAINING                                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐     │
│  │ Logistic         │  │ K-Nearest        │  │ Support Vector   │     │
│  │ Regression       │  │ Neighbors        │  │ Machine          │     │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘     │
│                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐                            │
│  │ Decision         │  │ Random           │                            │
│  │ Tree             │  │ Forest           │                            │
│  └──────────────────┘  └──────────────────┘                            │
│                                                                          │
│  Options:                                                                │
│  ├─ Basic Training (default parameters)                                │
│  ├─ Cross-Validation (5-fold)                                          │
│  └─ Hyperparameter Tuning (GridSearchCV)                               │
│                                                                          │
│  Module: model_training.py → train_basic_models()                       │
│  Output: models/*.pkl (5 trained models)                               │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 6: MODEL EVALUATION                                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  For Each Model:                                                         │
│  ├─ Make Predictions on Test Set                                       │
│  ├─ Calculate Metrics: Accuracy, Precision, Recall, F1, ROC-AUC        │
│  ├─ Generate Confusion Matrix                                          │
│  ├─ Plot ROC Curve                                                      │
│  └─ Analyze Feature Importance (if applicable)                         │
│                                                                          │
│  Metrics Calculated:                                                     │
│  ┌─────────────┬──────────┬───────────┬────────┬──────────┬──────────┐ │
│  │ Model       │ Accuracy │ Precision │ Recall │ F1-Score │ ROC-AUC  │ │
│  ├─────────────┼──────────┼───────────┼────────┼──────────┼──────────┤ │
│  │ Log Reg     │  0.850   │   0.875   │ 0.825  │  0.850   │  0.880   │ │
│  │ KNN         │  0.800   │   0.825   │ 0.775  │  0.800   │  0.830   │ │
│  │ SVM         │  0.825   │   0.850   │ 0.800  │  0.825   │  0.860   │ │
│  │ Dec Tree    │  0.775   │   0.800   │ 0.750  │  0.775   │  0.800   │ │
│  │ Rand Forest │  0.875   │   0.900   │ 0.850  │  0.875   │  0.905   │ │
│  └─────────────┴──────────┴───────────┴────────┴──────────┴──────────┘ │
│  (Example values - actual results may vary)                             │
│                                                                          │
│  Module: model_evaluation.py → evaluate_all_models()                    │
│  Output: results/confusion_matrix_*.png, roc_curve_*.png,              │
│          model_comparison.png, model_results.csv                        │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 7: MODEL SELECTION                                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Best Model Selection Criteria:                                         │
│  ├─ Best Overall: Highest F1-Score (balance)                           │
│  ├─ Best Sensitivity: Highest Recall (minimize false negatives)        │
│  ├─ Best Specificity: Highest Precision (minimize false positives)     │
│  └─ Best Accuracy: Overall correctness                                  │
│                                                                          │
│  🏆 Recommended: Random Forest (typically best overall)                 │
│                                                                          │
│  Module: model_evaluation.py → ModelSelector                            │
└─────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────┐
│ STEP 8: MODEL DEPLOYMENT & PREDICTION                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  New Patient Data ──→ Load Best Model ──→ Scale Features               │
│                                      ↓                                   │
│                            Make Prediction                               │
│                                      ↓                                   │
│          ┌──────────────────────────┴──────────────────────────┐       │
│          │                                                      │       │
│     ✅ No Disease                              ⚠️  Disease Detected     │
│     (Probability: 85%)                         (Probability: 75%)      │
│     Risk Level: 🟢 LOW                         Risk Level: 🔴 HIGH     │
│                                                                          │
│  Module: predict.py → predict_heart_disease()                           │
│  Modes: Sample predictions, Interactive input                           │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│ INTERACTIVE ANALYSIS (Optional)                                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  Jupyter Notebook: notebooks/heart_disease_analysis.ipynb               │
│                                                                          │
│  Features:                                                               │
│  ├─ Step-by-step interactive analysis                                  │
│  ├─ Customizable visualizations                                        │
│  ├─ Experiment with different parameters                               │
│  ├─ In-depth exploration and learning                                  │
│  └─ Export results and insights                                         │
└─────────────────────────────────────────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════════════

                            📁 OUTPUT FILES

results/
  ├─ target_distribution.png      (Target class distribution)
  ├─ correlation_heatmap.png       (Feature correlations)
  ├─ age_distribution.png          (Age vs disease)
  ├─ feature_distributions.png     (All feature histograms)
  ├─ confusion_matrix_*.png        (5 confusion matrices)
  ├─ roc_curve_*.png               (5 ROC curves)
  ├─ feature_importance_*.png      (Tree-based models)
  ├─ model_comparison.png          (Side-by-side comparison)
  └─ model_results.csv             (Detailed metrics table)

models/
  ├─ logistic_regression.pkl       (Trained LR model)
  ├─ k_nearest_neighbors.pkl       (Trained KNN model)
  ├─ support_vector_machine.pkl    (Trained SVM model)
  ├─ decision_tree.pkl             (Trained DT model)
  └─ random_forest.pkl             (Trained RF model)

data/
  ├─ train_data.csv                (Processed training data)
  └─ test_data.csv                 (Processed test data)

═══════════════════════════════════════════════════════════════════════════

                        🚀 QUICK START COMMANDS

1. Install dependencies:
   pip install -r requirements.txt

2. Run complete pipeline:
   python main.py

3. Make predictions:
   python predict.py

4. Interactive analysis:
   jupyter notebook notebooks/heart_disease_analysis.ipynb

═══════════════════════════════════════════════════════════════════════════

                          📊 EXPECTED PERFORMANCE

┌──────────────────┬──────────┬───────────┬─────────┬──────────┬──────────┐
│ Model            │ Accuracy │ Precision │ Recall  │ F1-Score │ ROC-AUC  │
├──────────────────┼──────────┼───────────┼─────────┼──────────┼──────────┤
│ Logistic Reg     │  75-85%  │  75-90%   │ 70-85%  │  75-85%  │  80-90%  │
│ KNN              │  70-80%  │  70-85%   │ 65-80%  │  70-80%  │  75-85%  │
│ SVM              │  75-85%  │  75-90%   │ 70-85%  │  75-85%  │  80-90%  │
│ Decision Tree    │  70-80%  │  70-85%   │ 65-80%  │  70-80%  │  75-85%  │
│ Random Forest    │  80-90%  │  80-95%   │ 75-90%  │  80-90%  │  85-95%  │
└──────────────────┴──────────┴───────────┴─────────┴──────────┴──────────┘

🏆 Best Performer: Random Forest (typically)

═══════════════════════════════════════════════════════════════════════════
```

## 🎯 Key Success Factors

1. **Data Quality**: Clean, well-preprocessed data
2. **Feature Engineering**: Proper scaling and transformation
3. **Model Selection**: Multiple algorithms for comparison
4. **Evaluation**: Comprehensive metrics and validation
5. **Documentation**: Clear code and extensive documentation
6. **Reproducibility**: Consistent results with random seed
7. **Modularity**: Well-organized, reusable code
8. **Visualization**: Professional, informative plots

## 🔄 Iteration Loop

```
Data → Train → Evaluate → Analyze → Improve
  ↑                                      ↓
  └──────────────────────────────────────┘
```

Continuously iterate to improve model performance!

---

**Project Status**: ✅ Complete & Production Ready
