"""
Heart Disease Prediction - Streamlit Web Application
Interactive dashboard for heart disease risk assessment
"""

import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os

# Page configuration
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    h1 {
        color: #e74c3c;
        text-align: center;
    }
    .success-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
    }
    .danger-box {
        padding: 1rem;
        border-radius: 0.5rem;
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        color: #721c24;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("❤️ Heart Disease Prediction System")
st.markdown("### AI-Powered Risk Assessment Tool")
st.markdown("---")

# Load models
@st.cache_resource
def load_models():
    try:
        # Try to load the tuned model first, fall back to regular model
        model_paths = [
            'models/random_forest_tuned.pkl',
            'models/k-nearest_neighbors_tuned.pkl',
            'models/random_forest.pkl',
            'models/k-nearest_neighbors.pkl'
        ]
        
        model = None
        model_name = None
        for path in model_paths:
            if os.path.exists(path):
                model = joblib.load(path)
                model_name = os.path.basename(path).replace('.pkl', '').replace('_', ' ').title()
                break
        
        if model is None:
            return None, None, None, False
        
        scaler = joblib.load('models/scaler.pkl')
        return model, scaler, model_name, True
    except Exception as e:
        st.error(f"Error loading models: {e}")
        return None, None, None, False

model, scaler, model_name, loaded = load_models()

if not loaded:
    st.error("⚠️ Models not found. Please run main.py first to train models.")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("📋 Navigation")
    page = st.radio("Choose a page:", ["🔍 Prediction", "📊 Model Info", "📁 Batch Prediction", "ℹ️ About"])
    
    st.markdown("---")
    st.header("🤖 Active Model")
    st.info(f"**{model_name}**")
    
    st.markdown("---")
    st.header("ℹ️ Quick Info")
    st.info("""
    **Features:**
    - Individual predictions
    - Batch predictions
    - Model performance
    - Feature explanations
    
    **Dataset:**
    UCI Heart Disease (303 patients)
    """)
    
    st.markdown("---")
    st.caption("Built with Streamlit 🎈")
    st.caption("Powered by Machine Learning")

# Page 1: Individual Prediction
if page == "🔍 Prediction":
    st.header("🔍 Individual Patient Prediction")
    
    st.markdown("""
    Enter patient information below to predict heart disease risk.
    All fields are required for accurate prediction.
    """)
    
    # Create two columns for input
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📝 Demographics & Vitals")
        age = st.slider("Age (years)", 20, 100, 50, help="Patient's age in years")
        sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x==0 else "Male")
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3], 
                         format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"][x],
                         help="Type of chest pain experienced")
        
        trestbps = st.slider("Resting Blood Pressure (mm Hg)", 90, 200, 120,
                            help="Blood pressure at rest")
        
        chol = st.slider("Cholesterol (mg/dl)", 100, 400, 200,
                        help="Serum cholesterol level")
        
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1],
                          format_func=lambda x: "No" if x==0 else "Yes",
                          help="Is fasting blood sugar > 120 mg/dl?")
        
        restecg = st.selectbox("Resting ECG", [0, 1, 2],
                              format_func=lambda x: ["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"][x],
                              help="Resting electrocardiographic results")
    
    with col2:
        st.subheader("🏥 Clinical Measurements")
        thalach = st.slider("Max Heart Rate Achieved", 60, 220, 150,
                           help="Maximum heart rate during exercise")
        
        exang = st.selectbox("Exercise Induced Angina", [0, 1],
                            format_func=lambda x: "No" if x==0 else "Yes",
                            help="Does exercise induce angina?")
        
        oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0, 0.1,
                           help="ST depression induced by exercise relative to rest")
        
        slope = st.selectbox("Slope of Peak Exercise ST Segment", [0, 1, 2],
                            format_func=lambda x: ["Upsloping", "Flat", "Downsloping"][x],
                            help="Slope of peak exercise ST segment")
        
        ca = st.selectbox("Number of Major Vessels (0-3)", [0, 1, 2, 3],
                         help="Number of major vessels colored by fluoroscopy")
        
        thal = st.selectbox("Thalassemia", [0, 1, 2, 3],
                           format_func=lambda x: ["Normal", "Fixed Defect", "Reversible Defect", "Unknown"][x],
                           help="Thalassemia status")
    
    st.markdown("---")
    
    # Predict button
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        predict_button = st.button("🔮 Predict Heart Disease Risk", type="primary", use_container_width=True)
    
    if predict_button:
        # Prepare input
        input_data = pd.DataFrame({
            'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps],
            'chol': [chol], 'fbs': [fbs], 'restecg': [restecg],
            'thalach': [thalach], 'exang': [exang], 'oldpeak': [oldpeak],
            'slope': [slope], 'ca': [ca], 'thal': [thal]
        })
        
        # Scale and predict
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0]
        
        # Display results
        st.markdown("---")
        st.header("📊 Prediction Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Prediction", 
                     "⚠️ High Risk" if prediction == 1 else "✅ Low Risk")
        
        with col2:
            st.metric("Confidence", 
                     f"{max(probability):.1%}")
        
        with col3:
            risk_level = "🔴 High" if probability[1] > 0.6 else ("🟡 Moderate" if probability[1] > 0.3 else "🟢 Low")
            st.metric("Risk Level", risk_level)
        
        # Risk gauge
        st.subheader("Risk Assessment")
        risk_percentage = probability[1]
        
        if prediction == 1:
            st.markdown(f"""
            <div class="danger-box">
                <h3>⚠️ High Risk of Heart Disease Detected</h3>
                <p>The model predicts a <strong>{probability[1]:.1%}</strong> probability of heart disease.</p>
                <p><strong>🏥 Recommendation:</strong> Consult with a healthcare professional immediately for proper evaluation and treatment.</p>
                <p><strong>⚡ Action Items:</strong></p>
                <ul>
                    <li>Schedule an appointment with a cardiologist</li>
                    <li>Get comprehensive cardiac tests</li>
                    <li>Review lifestyle and medication</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="success-box">
                <h3>✅ Low Risk of Heart Disease</h3>
                <p>The model predicts a <strong>{probability[0]:.1%}</strong> probability of no heart disease.</p>
                <p><strong>💚 Recommendation:</strong> Maintain a healthy lifestyle and regular check-ups.</p>
                <p><strong>📋 Continue to:</strong></p>
                <ul>
                    <li>Exercise regularly</li>
                    <li>Eat a balanced diet</li>
                    <li>Monitor blood pressure and cholesterol</li>
                    <li>Schedule annual check-ups</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Progress bar
        st.progress(probability[1], text=f"Disease Risk: {probability[1]:.1%}")
        
        # Feature summary
        st.markdown("---")
        st.subheader("📋 Patient Summary")
        
        summary_col1, summary_col2, summary_col3 = st.columns(3)
        
        with summary_col1:
            st.markdown("**👤 Demographics:**")
            st.write(f"• Age: {age} years")
            st.write(f"• Sex: {'Male' if sex == 1 else 'Female'}")
            
            st.markdown("\n**💉 Blood Tests:**")
            st.write(f"• Cholesterol: {chol} mg/dl")
            st.write(f"• Fasting Blood Sugar: {'High (>120)' if fbs == 1 else 'Normal'}")
        
        with summary_col2:
            st.markdown("**❤️ Cardiac:**")
            st.write(f"• Blood Pressure: {trestbps} mm Hg")
            st.write(f"• Max Heart Rate: {thalach} bpm")
            st.write(f"• ST Depression: {oldpeak}")
            st.write(f"• Major Vessels: {ca}")
        
        with summary_col3:
            st.markdown("**🏥 Clinical:**")
            st.write(f"• Chest Pain: {['Typical', 'Atypical', 'Non-anginal', 'Asymptomatic'][cp]}")
            st.write(f"• Exercise Angina: {'Yes' if exang == 1 else 'No'}")
            st.write(f"• ECG: {['Normal', 'ST-T Abnormality', 'LV Hypertrophy'][restecg]}")
            st.write(f"• Thalassemia: {['Normal', 'Fixed', 'Reversible', 'Unknown'][thal]}")

# Page 2: Model Information
elif page == "📊 Model Info":
    st.header("📈 Model Information & Performance")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Performance", "🎯 Feature Importance", "📖 Dataset Info", "🔬 About ML"])
    
    with tab1:
        st.subheader("Model Performance Metrics")
        
        # Try to load test results
        results_path = 'results/model_results.csv'
        tuning_path = 'results/tuning_results.csv'
        
        if os.path.exists(results_path):
            results_df = pd.read_csv(results_path)
            
            st.markdown("### 📊 All Models Comparison")
            st.dataframe(
                results_df.style.highlight_max(axis=0, color='lightgreen').format(precision=4),
                use_container_width=True
            )
            
            # Visualize metrics
            st.markdown("### 📈 Visual Comparison")
            fig, ax = plt.subplots(figsize=(12, 6))
            results_df.set_index('Model').plot(kind='bar', ax=ax, width=0.8)
            ax.set_title('Model Performance Comparison', fontsize=14, fontweight='bold')
            ax.set_ylabel('Score', fontsize=12)
            ax.set_xlabel('Model', fontsize=12)
            ax.legend(loc='lower right')
            ax.grid(axis='y', alpha=0.3)
            ax.set_ylim([0, 1.1])
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)
            
            # Show tuning results if available
            if os.path.exists(tuning_path):
                st.markdown("### 🎯 Hyperparameter Tuning Results")
                tuning_df = pd.read_csv(tuning_path, index_col=0)
                st.dataframe(tuning_df.style.format(precision=4), use_container_width=True)
        else:
            st.info("📝 Model results not found. Run main.py to generate metrics.")
            
            # Show sample metrics
            st.markdown("### Expected Performance")
            st.write("Typical accuracy range: **75-90%**")
            st.write("Best models: Random Forest, KNN, SVM")
    
    with tab2:
        st.subheader("🎯 Feature Importance")
        
        if hasattr(model, 'feature_importances_'):
            feature_names = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
            importances = model.feature_importances_
            
            # Create DataFrame
            importance_df = pd.DataFrame({
                'Feature': feature_names,
                'Importance': importances
            }).sort_values('Importance', ascending=False)
            
            # Plot
            fig, ax = plt.subplots(figsize=(10, 8))
            colors = plt.cm.viridis(np.linspace(0, 1, len(importance_df)))
            bars = ax.barh(importance_df['Feature'], importance_df['Importance'], color=colors)
            ax.set_xlabel('Importance Score', fontsize=12)
            ax.set_title('Feature Importance Analysis', fontsize=14, fontweight='bold')
            ax.grid(axis='x', alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)
            
            # Show table
            st.markdown("### 📋 Feature Importance Table")
            st.dataframe(importance_df.reset_index(drop=True), use_container_width=True)
            
            # Insights
            st.markdown("### 💡 Key Insights")
            top_feature = importance_df.iloc[0]
            st.success(f"**Most Important Feature:** {top_feature['Feature']} (Importance: {top_feature['Importance']:.4f})")
            
            top_3 = importance_df.head(3)['Feature'].tolist()
            st.info(f"**Top 3 Features:** {', '.join(top_3)}")
        else:
            st.info("Feature importance not available for this model type.")
            st.write("Feature importance is available for tree-based models like Random Forest and Decision Trees.")
    
    with tab3:
        st.subheader("📖 About the Dataset")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
            ### UCI Heart Disease Dataset
            
            **Source:** UCI Machine Learning Repository  
            **Domain:** Healthcare / Cardiology  
            **Type:** Classification
            
            **Dataset Statistics:**
            - 📊 **Instances:** 303 patients
            - 🔢 **Features:** 13 clinical features
            - 🎯 **Target:** Binary (Disease / No Disease)
            - 📅 **Year:** 1988
            - 🏥 **Location:** Cleveland Clinic
            """)
        
        with col2:
            st.markdown("""
            ### Citation
            
            Detrano, R., et al. (1989).  
            *International application of a new probability algorithm for the diagnosis of coronary artery disease.*  
            American Journal of Cardiology, 64, 304-310.
            
            ### Usage
            
            This dataset has been widely used in:
            - Medical research
            - Machine learning studies
            - Educational purposes
            """)
        
        st.markdown("---")
        st.markdown("### 📋 Feature Descriptions")
        
        feature_info = {
            'Feature': ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
                       'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'],
            'Description': [
                'Age in years',
                'Sex (1 = male, 0 = female)',
                'Chest pain type (0-3)',
                'Resting blood pressure (mm Hg)',
                'Serum cholesterol (mg/dl)',
                'Fasting blood sugar > 120 mg/dl',
                'Resting electrocardiographic results (0-2)',
                'Maximum heart rate achieved',
                'Exercise induced angina (1 = yes, 0 = no)',
                'ST depression induced by exercise',
                'Slope of peak exercise ST segment (0-2)',
                'Number of major vessels (0-3)',
                'Thalassemia (0-3)'
            ],
            'Type': ['Numeric', 'Binary', 'Categorical', 'Numeric', 'Numeric', 'Binary', 
                    'Categorical', 'Numeric', 'Binary', 'Numeric', 'Categorical', 
                    'Categorical', 'Categorical']
        }
        
        feature_df = pd.DataFrame(feature_info)
        st.dataframe(feature_df, use_container_width=True, hide_index=True)
    
    with tab4:
        st.subheader("🔬 About Machine Learning")
        
        st.markdown("""
        ### What is Machine Learning?
        
        Machine Learning (ML) is a subset of artificial intelligence that enables computers to learn patterns from data without being explicitly programmed.
        
        ### How Does This Model Work?
        
        1. **Training Phase:**
           - The model learns from 303 patient records
           - Identifies patterns between medical features and heart disease
           - Optimizes parameters to make accurate predictions
        
        2. **Prediction Phase:**
           - Takes new patient data as input
           - Applies learned patterns
           - Outputs probability of heart disease
        
        ### Model Types Used
        
        - **Random Forest:** Ensemble of decision trees
        - **K-Nearest Neighbors:** Similarity-based classification
        - **Support Vector Machine:** Finds optimal decision boundary
        - **Logistic Regression:** Probabilistic linear classifier
        
        ### Performance Metrics
        
        - **Accuracy:** Overall correctness
        - **Precision:** Correct positive predictions
        - **Recall:** Detected actual positives
        - **F1-Score:** Balance of precision and recall
        - **ROC-AUC:** Overall discrimination ability
        
        ### ⚠️ Important Notes
        
        - This tool is for **educational purposes**
        - **Not a replacement** for professional medical diagnosis
        - Always consult healthcare professionals
        - Model accuracy: ~80-90% (not 100%)
        """)

# Page 3: Batch Prediction
elif page == "📁 Batch Prediction":
    st.header("📊 Batch Prediction")
    
    st.markdown("""
    Upload a CSV file with patient data to get predictions for multiple patients at once.
    
    **Required columns:** age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
    """)
    
    # Sample data download
    col1, col2 = st.columns([3, 1])
    with col1:
        st.info("💡 Don't have a file? Download our sample template to get started.")
    with col2:
        sample_data = pd.DataFrame({
            'age': [63, 45, 58],
            'sex': [1, 0, 1],
            'cp': [3, 0, 2],
            'trestbps': [145, 120, 130],
            'chol': [233, 200, 250],
            'fbs': [1, 0, 1],
            'restecg': [0, 0, 1],
            'thalach': [150, 170, 140],
            'exang': [0, 0, 1],
            'oldpeak': [2.3, 0.5, 1.5],
            'slope': [0, 1, 2],
            'ca': [0, 0, 1],
            'thal': [1, 2, 2]
        })
        csv = sample_data.to_csv(index=False)
        st.download_button(
            label="📥 Download Sample",
            data=csv,
            file_name="sample_patients.csv",
            mime="text/csv",
        )
    
    st.markdown("---")
    
    # File uploader
    uploaded_file = st.file_uploader("📁 Choose a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        try:
            # Read the file
            batch_data = pd.read_csv(uploaded_file)
            
            st.success(f"✅ File uploaded successfully! Found {len(batch_data)} patients.")
            
            # Show preview
            with st.expander("📋 View Data Preview (first 10 rows)"):
                st.dataframe(batch_data.head(10), use_container_width=True)
            
            # Predict button
            if st.button("🔮 Generate Predictions", type="primary", use_container_width=True):
                with st.spinner("Processing predictions..."):
                    # Scale data
                    batch_scaled = scaler.transform(batch_data)
                    
                    # Predictions
                    predictions = model.predict(batch_scaled)
                    probabilities = model.predict_proba(batch_scaled)
                    
                    # Add results to dataframe
                    results = batch_data.copy()
                    results.insert(0, 'Patient_ID', range(1, len(results) + 1))
                    results['Prediction'] = predictions
                    results['Disease_Probability'] = probabilities[:, 1]
                    results['No_Disease_Probability'] = probabilities[:, 0]
                    results['Diagnosis'] = results['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                    results['Risk_Level'] = results['Disease_Probability'].apply(
                        lambda x: 'High' if x > 0.6 else ('Moderate' if x > 0.3 else 'Low')
                    )
                
                # Display results
                st.markdown("---")
                st.subheader("📊 Prediction Results")
                
                # Summary metrics
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Total Patients", len(results))
                
                with col2:
                    high_risk = (predictions == 1).sum()
                    st.metric("High Risk", high_risk, 
                             delta=f"{high_risk/len(results)*100:.1f}%",
                             delta_color="inverse")
                
                with col3:
                    low_risk = (predictions == 0).sum()
                    st.metric("Low Risk", low_risk,
                             delta=f"{low_risk/len(results)*100:.1f}%",
                             delta_color="normal")
                
                with col4:
                    avg_risk = results['Disease_Probability'].mean()
                    st.metric("Avg Risk Score", f"{avg_risk:.1%}")
                
                # Results table
                st.markdown("### 📋 Detailed Results")
                
                # Color coding function
                def highlight_diagnosis(row):
                    if row['Diagnosis'] == 'High Risk':
                        return ['background-color: #f8d7da'] * len(row)
                    else:
                        return ['background-color: #d4edda'] * len(row)
                
                st.dataframe(
                    results.style.apply(highlight_diagnosis, axis=1).format(
                        {'Disease_Probability': '{:.2%}', 'No_Disease_Probability': '{:.2%}'}
                    ),
                    use_container_width=True,
                    height=400
                )
                
                # Download button
                st.markdown("### 💾 Export Results")
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write("Download the complete results with predictions")
                with col2:
                    csv_results = results.to_csv(index=False)
                    st.download_button(
                        label="📥 Download Results",
                        data=csv_results,
                        file_name="heart_disease_predictions.csv",
                        mime="text/csv",
                        use_container_width=True
                    )
                
                # Visualization
                st.markdown("---")
                st.subheader("📈 Risk Distribution Analysis")
                
                fig, axes = plt.subplots(1, 3, figsize=(18, 5))
                
                # Pie chart
                diagnosis_counts = results['Diagnosis'].value_counts()
                axes[0].pie(diagnosis_counts, labels=diagnosis_counts.index, autopct='%1.1f%%',
                           colors=['#d4edda', '#f8d7da'], startangle=90)
                axes[0].set_title('Risk Distribution', fontsize=14, fontweight='bold')
                
                # Histogram
                axes[1].hist(results['Disease_Probability'], bins=20, edgecolor='black', 
                            alpha=0.7, color='steelblue')
                axes[1].set_xlabel('Disease Probability', fontsize=12)
                axes[1].set_ylabel('Number of Patients', fontsize=12)
                axes[1].set_title('Probability Distribution', fontsize=14, fontweight='bold')
                axes[1].grid(axis='y', alpha=0.3)
                
                # Risk level bar chart
                risk_counts = results['Risk_Level'].value_counts()
                colors_risk = {'Low': '#28a745', 'Moderate': '#ffc107', 'High': '#dc3545'}
                axes[2].bar(risk_counts.index, risk_counts.values,
                           color=[colors_risk.get(x, 'gray') for x in risk_counts.index],
                           edgecolor='black')
                axes[2].set_xlabel('Risk Level', fontsize=12)
                axes[2].set_ylabel('Number of Patients', fontsize=12)
                axes[2].set_title('Risk Level Distribution', fontsize=14, fontweight='bold')
                axes[2].grid(axis='y', alpha=0.3)
                
                plt.tight_layout()
                st.pyplot(fig)
                
                # Statistics
                st.markdown("### 📊 Statistical Summary")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.markdown("**Risk Probability Statistics:**")
                    st.write(f"• Mean: {results['Disease_Probability'].mean():.2%}")
                    st.write(f"• Median: {results['Disease_Probability'].median():.2%}")
                    st.write(f"• Std Dev: {results['Disease_Probability'].std():.2%}")
                    st.write(f"• Min: {results['Disease_Probability'].min():.2%}")
                    st.write(f"• Max: {results['Disease_Probability'].max():.2%}")
                
                with col2:
                    st.markdown("**Risk Level Breakdown:**")
                    for level in ['Low', 'Moderate', 'High']:
                        count = (results['Risk_Level'] == level).sum()
                        pct = count / len(results) * 100
                        st.write(f"• {level}: {count} patients ({pct:.1f}%)")
        
        except Exception as e:
            st.error(f"❌ Error processing file: {str(e)}")
            st.info("💡 Please ensure your CSV has all required columns with correct names.")

# Page 4: About
elif page == "ℹ️ About":
    st.header("ℹ️ About This Application")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### Heart Disease Prediction System
        
        This application uses machine learning to assess the risk of heart disease based on clinical parameters.
        
        #### 🎯 Purpose
        
        - Educational demonstration of ML in healthcare
        - Quick risk assessment tool
        - Understanding heart disease risk factors
        
        #### 🔬 Technology Stack
        
        - **Frontend:** Streamlit
        - **ML Framework:** Scikit-learn
        - **Models:** Random Forest, KNN, SVM
        - **Dataset:** UCI Heart Disease Dataset
        
        #### ⚙️ Features
        
        - ✅ Individual patient predictions
        - ✅ Batch processing for multiple patients
        - ✅ Model performance metrics
        - ✅ Feature importance analysis
        - ✅ Interactive visualizations
        - ✅ Risk level categorization
        - ✅ Detailed explanations
        
        #### 📊 Model Performance
        
        - Accuracy: 80-90%
        - F1-Score: 80-88%
        - ROC-AUC: 90-95%
        
        Based on 5-fold cross-validation
        """)
        
        st.markdown("---")
        
        st.markdown("""
        ### ⚠️ Disclaimer
        
        **IMPORTANT:** This application is for educational and informational purposes only.
        
        - ❌ **NOT a medical device**
        - ❌ **NOT a substitute for professional medical advice**
        - ❌ **NOT for clinical diagnosis**
        
        **Always consult qualified healthcare professionals for:**
        - Medical diagnosis
        - Treatment decisions
        - Health concerns
        - Cardiac symptoms
        
        The predictions are based on machine learning models and may not be 100% accurate.
        """)
    
    with col2:
        st.markdown("""
        ### 📞 Support
        
        For questions or issues:
        - Check the documentation
        - Review the model info page
        - Consult the dataset details
        
        ### 📚 Resources
        
        - [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/heart+Disease)
        - [Scikit-learn Docs](https://scikit-learn.org/)
        - [Streamlit Docs](https://docs.streamlit.io/)
        
        ### 🔄 Version
        
        **Version:** 2.0  
        **Last Updated:** December 2025  
        **Model:** {model_name}
        
        ### 👨‍💻 Development
        
        Built with:
        - Python 3.8+
        - Streamlit
        - Machine Learning
        - Medical Data Science
        
        ### 📖 Citation
        
        If using this application for research or education, please cite the UCI Heart Disease Dataset.
        """.format(model_name=model_name))
        
        st.markdown("---")
        
        st.success("""
        ### 💚 Health Tips
        
        **Maintain heart health:**
        - 🏃 Regular exercise
        - 🥗 Balanced diet
        - 😴 Adequate sleep
        - 🚭 No smoking
        - 🧘 Stress management
        - 📊 Regular check-ups
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p><strong>⚠️ Medical Disclaimer:</strong> This is a predictive model and should not replace professional medical advice. 
    Always consult with a healthcare professional for proper diagnosis and treatment.</p>
    <hr style='margin: 1rem 0; border: none; border-top: 1px solid #ddd;'>
    <p>Made with ❤️ using Streamlit | Data: UCI Heart Disease Dataset | Powered by Machine Learning</p>
    <p style='font-size: 0.9em;'>© 2025 Heart Disease Prediction System | Educational Use Only</p>
</div>
""", unsafe_allow_html=True)
