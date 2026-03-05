"""
Main pipeline for Heart Disease Prediction
End-to-end machine learning workflow
"""
import os
import sys
import time
import warnings
warnings.filterwarnings('ignore')

# Add src directory to path
sys.path.append(os.path.dirname(__file__))

from src.data_preprocessing import DataPreprocessor
from src.model_training import ModelTrainer
from src.model_evaluation import ModelEvaluator, ModelSelector
from src.utils import create_directories, save_model, print_separator


def main():
    """
    Main function to run the complete heart disease prediction pipeline
    """
    start_time = time.time()
    
    print("\n" + "="*80)
    print(" "*20 + "HEART DISEASE PREDICTION SYSTEM")
    print(" "*15 + "Machine Learning End-to-End Pipeline")
    print("="*80)
    
    # Create necessary directories
    create_directories()
    
    # ========================================================================
    # STEP 1: DATA PREPROCESSING
    # ========================================================================
    print_separator()
    print("STEP 1: DATA PREPROCESSING")
    print_separator()
    
    preprocessor = DataPreprocessor()
    
    # Load data
    print("\n📥 Loading dataset...")
    df = preprocessor.load_data()
    
    # Explore data
    print("\n🔍 Exploring data...")
    preprocessor.explore_data(df, save_plots=True)
    
    # Clean data
    print("\n🧹 Cleaning data...")
    df_clean = preprocessor.clean_data(df)
    
    # Prepare features
    print("\n⚙️ Preparing features...")
    X_train, X_test, y_train, y_test = preprocessor.prepare_features(df_clean)
    
    # Save processed data
    preprocessor.save_processed_data(X_train, X_test, y_train, y_test)
    
    # ========================================================================
    # STEP 2: MODEL TRAINING
    # ========================================================================
    print_separator()
    print("STEP 2: MODEL TRAINING")
    print_separator()
    
    trainer = ModelTrainer()
    
    # Initialize models
    print("\n🤖 Initializing models...")
    trainer.initialize_models()
    
    # Train basic models
    print("\n🚀 Training models with default parameters...")
    models = trainer.train_basic_models(X_train, y_train)
    
    # Perform cross-validation
    print("\n📊 Performing cross-validation...")
    cv_scores = trainer.perform_cross_validation(X_train, y_train, cv=5)
    
    # Optional: Hyperparameter tuning (uncomment if needed - takes longer)
    print("\n⚡ Do you want to perform hyperparameter tuning? (takes longer)")
    print("   Skipping for now... (uncomment in code to enable)")
    # models = trainer.tune_hyperparameters(X_train, y_train, cv=5)
    
    # ========================================================================
    # STEP 3: MODEL EVALUATION
    # ========================================================================
    print_separator()
    print("STEP 3: MODEL EVALUATION")
    print_separator()
    
    evaluator = ModelEvaluator()
    
    # Evaluate all models
    print("\n📈 Evaluating all models...")
    results = evaluator.evaluate_all_models(
        models, X_test, y_test, 
        feature_names=preprocessor.feature_names,
        save_plots=True
    )
    
    # Save results
    evaluator.save_results()
    
    # ========================================================================
    # STEP 4: MODEL SELECTION
    # ========================================================================
    print_separator()
    print("STEP 4: MODEL SELECTION")
    print_separator()
    
    selector = ModelSelector(evaluator)
    
    print("\n🎯 Model Selection Recommendations:")
    print("\n1. Best Overall Performance (F1-Score):")
    best_overall = selector.select_best_overall()
    
    print("\n2. Best for Sensitivity (Recall - minimize false negatives):")
    best_sensitivity = selector.select_for_sensitivity()
    
    print("\n3. Best for Specificity (Precision - minimize false positives):")
    best_specificity = selector.select_for_specificity()
    
    print("\n4. Best Accuracy:")
    best_accuracy = selector.select_for_accuracy()
    
    # ========================================================================
    # STEP 5: SAVE BEST MODELS
    # ========================================================================
    print_separator()
    print("STEP 5: SAVING MODELS")
    print_separator()
    
    print("\n💾 Saving trained models...")
    for name, model in models.items():
        model_filename = name.lower().replace(' ', '_')
        save_model(model, model_filename)
    
    # Save scaler
    print("💾 Saving scaler...")
    save_model(preprocessor.scaler, 'scaler')
    
    # ========================================================================
    # FINAL SUMMARY
    # ========================================================================
    print_separator()
    print("PIPELINE COMPLETED")
    print_separator()
    
    elapsed_time = time.time() - start_time
    
    print(f"\n✅ Pipeline executed successfully!")
    print(f"\n⏱️  Total execution time: {elapsed_time:.2f} seconds")
    
    print("\n📁 Generated Files:")
    print("   • Data: data/train_data.csv, data/test_data.csv")
    print("   • Models: models/*.pkl")
    print("   • Results: results/*.png, results/model_results.csv")
    
    print("\n🎓 Next Steps:")
    print("   1. Review the results in the 'results' directory")
    print("   2. Check model_results.csv for detailed metrics")
    print("   3. Explore visualizations (confusion matrices, ROC curves)")
    print("   4. Use the saved models for predictions")
    print("   5. Open the Jupyter notebook for interactive analysis")
    
    print("\n" + "="*80)
    print(" "*25 + "Thank you for using the system!")
    print("="*80 + "\n")
    
    return models, results, evaluator


if __name__ == "__main__":
    try:
        models, results, evaluator = main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Pipeline interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
