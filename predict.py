"""
Prediction script for Heart Disease Prediction
Use trained models to make predictions on new patient data
"""
import sys
import os
import joblib
import pandas as pd
import numpy as np

# Add src to path
sys.path.append(os.path.dirname(__file__))

from src.utils import print_separator


def load_best_model(model_dir='models'):
    """Load the best trained model"""
    import glob
    
    # Try to find saved models
    model_files = glob.glob(os.path.join(model_dir, '*.pkl'))
    
    if not model_files:
        print("❌ No trained models found!")
        print("Please run 'python main.py' first to train models.")
        return None, None
    
    # Load Random Forest by default (usually best performing)
    rf_path = os.path.join(model_dir, 'random_forest.pkl')
    
    if os.path.exists(rf_path):
        model_path = rf_path
    else:
        # Load first available model
        model_path = model_files[0]
    
    print(f"Loading model: {model_path}")
    model = joblib.load(model_path)
    
    # Try to load scaler
    scaler_path = os.path.join(model_dir, 'scaler.pkl')
    scaler = None
    if os.path.exists(scaler_path):
        scaler = joblib.load(scaler_path)
        print(f"Loading scaler: {scaler_path}")
    
    return model, scaler


def create_patient_data():
    """
    Create sample patient data for prediction
    You can modify these values to test different scenarios
    """
    # Feature names in order
    feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 
                    'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 
                    'ca', 'thal']
    
    # Example patient 1: Higher risk profile
    patient1 = {
        'age': 63,        # Age in years
        'sex': 1,         # 1 = male, 0 = female
        'cp': 3,          # Chest pain type (0-3)
        'trestbps': 145,  # Resting blood pressure
        'chol': 233,      # Serum cholesterol
        'fbs': 1,         # Fasting blood sugar > 120 mg/dl
        'restecg': 0,     # Resting ECG results (0-2)
        'thalach': 150,   # Maximum heart rate achieved
        'exang': 0,       # Exercise induced angina
        'oldpeak': 2.3,   # ST depression
        'slope': 0,       # Slope of peak exercise ST segment
        'ca': 0,          # Number of major vessels (0-3)
        'thal': 1         # Thalassemia (0-3)
    }
    
    # Example patient 2: Lower risk profile
    patient2 = {
        'age': 45,
        'sex': 0,
        'cp': 0,
        'trestbps': 120,
        'chol': 200,
        'fbs': 0,
        'restecg': 0,
        'thalach': 170,
        'exang': 0,
        'oldpeak': 0.5,
        'slope': 1,
        'ca': 0,
        'thal': 2
    }
    
    # Convert to DataFrame
    patients = pd.DataFrame([patient1, patient2])
    
    return patients, ['Patient 1 (Higher Risk)', 'Patient 2 (Lower Risk)']


def predict_heart_disease(patient_data, model, scaler=None):
    """
    Make predictions on patient data
    
    Args:
        patient_data: DataFrame with patient features
        model: Trained ML model
        scaler: Fitted scaler (optional)
    
    Returns:
        predictions, probabilities
    """
    # Scale data if scaler is available
    if scaler is not None:
        patient_data_scaled = scaler.transform(patient_data)
    else:
        patient_data_scaled = patient_data
    
    # Make predictions
    predictions = model.predict(patient_data_scaled)
    
    # Get probabilities if available
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(patient_data_scaled)
    else:
        probabilities = None
    
    return predictions, probabilities


def print_prediction_results(patient_names, predictions, probabilities):
    """Print prediction results in a readable format"""
    print_separator()
    print("PREDICTION RESULTS")
    print_separator()
    
    for i, name in enumerate(patient_names):
        print(f"\n{name}:")
        print("-" * 60)
        
        prediction = predictions[i]
        print(f"Prediction: {'⚠️  HEART DISEASE DETECTED' if prediction == 1 else '✅ NO HEART DISEASE'}")
        
        if probabilities is not None:
            prob_no_disease = probabilities[i][0]
            prob_disease = probabilities[i][1]
            
            print(f"\nConfidence Scores:")
            print(f"  No Disease:  {prob_no_disease:.2%} {'█' * int(prob_no_disease * 50)}")
            print(f"  Disease:     {prob_disease:.2%} {'█' * int(prob_disease * 50)}")
            
            print(f"\nRisk Level: ", end="")
            if prob_disease < 0.3:
                print("🟢 LOW")
            elif prob_disease < 0.6:
                print("🟡 MODERATE")
            else:
                print("🔴 HIGH")


def interactive_prediction():
    """Interactive mode to input patient data"""
    print("\n" + "="*80)
    print(" "*25 + "INTERACTIVE PREDICTION MODE")
    print("="*80)
    
    print("\nEnter patient data (press Enter for default values):\n")
    
    try:
        age = input("Age [63]: ") or "63"
        sex = input("Sex (0=female, 1=male) [1]: ") or "1"
        cp = input("Chest pain type (0-3) [3]: ") or "3"
        trestbps = input("Resting blood pressure [145]: ") or "145"
        chol = input("Serum cholesterol [233]: ") or "233"
        fbs = input("Fasting blood sugar > 120 (0/1) [1]: ") or "1"
        restecg = input("Resting ECG (0-2) [0]: ") or "0"
        thalach = input("Max heart rate [150]: ") or "150"
        exang = input("Exercise induced angina (0/1) [0]: ") or "0"
        oldpeak = input("ST depression [2.3]: ") or "2.3"
        slope = input("Slope of peak exercise ST (0-2) [0]: ") or "0"
        ca = input("Number of major vessels (0-3) [0]: ") or "0"
        thal = input("Thalassemia (0-3) [1]: ") or "1"
        
        patient_data = pd.DataFrame([{
            'age': float(age),
            'sex': float(sex),
            'cp': float(cp),
            'trestbps': float(trestbps),
            'chol': float(chol),
            'fbs': float(fbs),
            'restecg': float(restecg),
            'thalach': float(thalach),
            'exang': float(exang),
            'oldpeak': float(oldpeak),
            'slope': float(slope),
            'ca': float(ca),
            'thal': float(thal)
        }])
        
        return patient_data, ['Custom Patient']
        
    except ValueError:
        print("❌ Invalid input! Please enter numeric values.")
        return None, None


def main():
    """Main prediction function"""
    print("\n" + "="*80)
    print(" "*20 + "HEART DISEASE PREDICTION SYSTEM")
    print(" "*25 + "Prediction Module")
    print("="*80)
    
    # Load model
    print("\n📥 Loading trained model...")
    model, scaler = load_best_model()
    
    if model is None:
        return
    
    print("✓ Model loaded successfully!\n")
    
    # Choose mode
    print("Select mode:")
    print("1. Predict on sample patients")
    print("2. Interactive mode (enter custom data)")
    
    choice = input("\nEnter choice (1 or 2) [1]: ") or "1"
    
    if choice == "2":
        patient_data, patient_names = interactive_prediction()
        if patient_data is None:
            return
    else:
        patient_data, patient_names = create_patient_data()
        
        print("\n📊 Sample Patient Data:")
        print(patient_data.to_string())
    
    # Make predictions
    print("\n🔮 Making predictions...")
    predictions, probabilities = predict_heart_disease(patient_data, model, scaler)
    
    # Print results
    print_prediction_results(patient_names, predictions, probabilities)
    
    print("\n" + "="*80)
    print("⚕️  Note: This is a prediction tool and should not replace professional")
    print("   medical diagnosis. Consult a healthcare provider for accurate assessment.")
    print("="*80 + "\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Prediction interrupted by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error occurred: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
