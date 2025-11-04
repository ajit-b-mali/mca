import streamlit as st
import numpy as np
from PIL import Image
import plotly.express as px
import pandas as pd
from model import FashionStyleClassifier
from utils import preprocess_image, get_fashion_categories, validate_image, get_color_palette, get_style_description

# Configure page
st.set_page_config(
    page_title="Fashion Style Classifier",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state for the classifier model
if 'classifier' not in st.session_state:
    with st.spinner("Loading fashion classification model..."):
        st.session_state.classifier = FashionStyleClassifier()
    st.toast("Model loaded successfully!", icon="✅")

def main():
    st.title("👗 Fashion Style Classification")
    st.markdown("Upload an image of a fashion item to classify its style with AI-powered predictions!")
    
    # Sidebar for controls
    with st.sidebar:
        st.header("🎛️ Controls")
        
        # Confidence threshold slider
        confidence_threshold = st.slider(
            "Confidence Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.2, # Lowered default to show more results initially
            step=0.05,
            help="Only show predictions above this confidence level"
        )
        
        # Model information
        st.header("📊 Model Info")
        st.info("""
        **Model:** MobileNetV2 Fine-tuned
        **Categories:** 8 Fashion Styles
        **Input Size:** 224x224 pixels
        """)
        
        # Disclaimer for the mock model
        st.warning("Note: This app uses a simulated model. Predictions are for demonstration purposes only.")
        
        # Fashion categories
        st.header("🏷️ Style Categories")
        categories = get_fashion_categories()
        for i, category in enumerate(categories, 1):
            st.write(f"{i}. {category.title()}")
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📸 Upload Fashion Image")
        
        # File uploader
        uploaded_file = st.file_uploader(
            "Choose a fashion image...",
            type=['png', 'jpg', 'jpeg'],
            help="Upload images in PNG, JPG, or JPEG format"
        )
        
        # Image display and processing
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            
            # **IMPROVEMENT: Validate the uploaded image first**
            is_valid, message = validate_image(image)
            
            if not is_valid:
                st.error(f"Image validation failed: {message}")
                st.image(image, caption="Invalid Image Uploaded", use_column_width=True)
            else:
                st.image(image, caption="Uploaded Fashion Item", use_column_width=True)
                
                # Image info
                st.write(f"**Image Size:** {image.size[0]}x{image.size[1]} pixels")
                st.write(f"**File Size:** {len(uploaded_file.getvalue()) / 1024:.1f} KB")

                # **IMPROVEMENT: Display dominant color palette**
                with st.spinner("Extracting dominant colors..."):
                    st.subheader("🎨 Dominant Colors")
                    colors = get_color_palette(image)
                    color_cols = st.columns(len(colors))
                    for i, color in enumerate(colors):
                        with color_cols[i]:
                            st.markdown(
                                f'<div style="background-color: rgb({color[0]}, {color[1]}, {color[2]}); '
                                f'width:100%; height:50px; border:1px solid #ccc; border-radius:5px;"></div>',
                                unsafe_allow_html=True
                            )

                # Process image and make prediction
                processed_image = preprocess_image(image)
                with st.spinner("Analyzing fashion style..."):
                    predictions = st.session_state.classifier.predict(processed_image)
                    
                # Store results in session state for the other column to use
                st.session_state.predictions = predictions
                st.session_state.confidence_threshold = confidence_threshold
        else:
            # Placeholder when no image is uploaded
            st.info("👆 Please upload a fashion image to get started!")
            st.image("https://via.placeholder.com/400x300/f0f2f6/666666?text=Upload+Fashion+Image", 
                     caption="Waiting for image upload...", use_column_width=True)
    
    with col2:
        st.header("🎯 Prediction Results")
        
        if 'predictions' in st.session_state and 'confidence_threshold' in st.session_state:
            predictions = st.session_state.predictions
            threshold = st.session_state.confidence_threshold
            categories = get_fashion_categories()
            
            # Filter predictions by confidence threshold
            filtered_predictions = []
            for i, (category, confidence) in enumerate(zip(categories, predictions[0])):
                if confidence >= threshold:
                    filtered_predictions.append({
                        'Style': category.title(),
                        'Confidence': confidence,
                        'Percentage': f"{confidence * 100:.1f}%"
                    })
            
            if filtered_predictions:
                # Sort by confidence
                filtered_predictions = sorted(filtered_predictions, key=lambda x: x['Confidence'], reverse=True)
                
                # Display top prediction prominently
                top_prediction = filtered_predictions[0]
                st.success(f"**Primary Style:** {top_prediction['Style']}")
                st.metric("Confidence", top_prediction['Percentage'])

                # **IMPROVEMENT: Add style description expander**
                with st.expander(f"What is '{top_prediction['Style']}' style?"):
                    description = get_style_description(top_prediction['Style'])
                    st.write(description)
                
                # Create dataframe for visualization
                df = pd.DataFrame(filtered_predictions)
                
                # Interactive bar chart
                fig = px.bar(
                    df, 
                    x='Confidence', 
                    y='Style',
                    orientation='h',
                    title="Fashion Style Predictions",
                    labels={'Confidence': 'Confidence Score', 'Style': 'Fashion Style'},
                    color='Confidence',
                    color_continuous_scale='Viridis'
                )
                fig.update_layout(
                    height=400,
                    showlegend=False,
                    yaxis={'categoryorder': 'total ascending'}
                )
                fig.update_traces(
                    hovertemplate='<b>%{y}</b><br>Confidence: %{x:.3f}<extra></extra>'
                )
                st.plotly_chart(fig, use_container_width=True)
                
                # Detailed results table
                st.subheader("📋 Detailed Results")
                st.dataframe(
                    df[['Style', 'Percentage']], 
                    use_container_width=True,
                    hide_index=True
                )
                
                # Style Insights
                st.subheader("💡 Style Insights")
                if len(filtered_predictions) > 1:
                    second_best = filtered_predictions[1]
                    confidence_diff = top_prediction['Confidence'] - second_best['Confidence']
                    
                    if confidence_diff < 0.2:
                        st.warning(f"The model shows some uncertainty. The item could also be classified as **{second_best['Style']}** with {second_best['Percentage']} confidence.")
                    else:
                        st.info(f"High confidence prediction! The model is quite certain this is a **{top_prediction['Style']}** item.")
                else:
                    st.info(f"Only **{top_prediction['Style']}** meets the confidence threshold of {threshold:.1%}.")
                    
            else:
                st.warning(f"No predictions meet the confidence threshold of {threshold:.1%}. Try lowering the threshold.")
                
        else:
            st.info("📊 Upload an image to see prediction results here!")
            
            # Placeholder chart
            placeholder_data = pd.DataFrame({
                'Style': ['Casual', 'Formal', 'Sporty', 'Vintage', 'Bohemian'],
                'Confidence': [0.0, 0.0, 0.0, 0.0, 0.0]
            })
            fig = px.bar(
                placeholder_data,
                x='Confidence',
                y='Style',
                orientation='h',
                title="Fashion Style Predictions (Awaiting Image)"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    **How it works:** This application uses a fine-tuned MobileNetV2 deep learning model to classify fashion items. 
    The model analyzes visual features like patterns, colors, and textures to make predictions.
    
    **Tips for best results:**
    - Use clear, well-lit images.
    - Focus on a single fashion item.
    - Avoid cluttered backgrounds.
    """)

if __name__ == "__main__":
    main()