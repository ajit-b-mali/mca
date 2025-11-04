import numpy as np
from PIL import Image
import tensorflow as tf

def get_fashion_categories():
    """
    Return the list of fashion style categories that the model can classify.
    
    Returns:
        list: List of fashion style category names
    """
    return [
        'casual',
        'formal',
        'sporty',
        'vintage',
        'bohemian',
        'streetwear',
        'minimalist',
        'glamorous'
    ]

def preprocess_image(image):
    """
    Preprocess an image for the fashion classification model.
    
    Args:
        image (PIL.Image): Input image
        
    Returns:
        np.ndarray: Preprocessed image array ready for model prediction
    """
    try:
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize to model input size
        image = image.resize((224, 224), Image.Resampling.LANCZOS)
        
        # Convert to numpy array
        image_array = np.array(image, dtype=np.float32)
        
        # Normalize pixel values to [0, 1] (MobileNetV2 expects this range)
        image_array = image_array / 255.0
        
        # Add batch dimension
        image_array = np.expand_dims(image_array, axis=0)
        
        return image_array
        
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        # Return a default image array
        return np.zeros((1, 224, 224, 3), dtype=np.float32)

def validate_image(image):
    """
    Validate if an image is suitable for fashion classification.
    
    Args:
        image (PIL.Image): Input image
        
    Returns:
        tuple: (is_valid, message)
    """
    try:
        # Check image format
        if image.format not in ['JPEG', 'PNG', 'JPG']:
            return False, "Image format not supported. Please use JPEG or PNG."
        
        # Check image size
        width, height = image.size
        if width < 100 or height < 100:
            return False, "Image too small. Please use images larger than 100x100 pixels."
        
        if width > 4000 or height > 4000:
            return False, "Image too large. Please use images smaller than 4000x4000 pixels."
        
        # Check if image has content (not all black or all white)
        image_array = np.array(image.convert('L'))  # Convert to grayscale for checking
        if np.std(image_array) < 10:  # Very low standard deviation means uniform color
            return False, "Image appears to be uniform in color. Please use a more detailed image."
        
        return True, "Image is valid for classification."
        
    except Exception as e:
        return False, f"Error validating image: {str(e)}"

def get_color_palette(image, num_colors=5):
    """
    Extract dominant colors from an image.
    
    Args:
        image (PIL.Image): Input image
        num_colors (int): Number of dominant colors to extract
        
    Returns:
        list: List of RGB color tuples
    """
    try:
        # Resize image to speed up processing
        image = image.resize((150, 150))
        
        # Convert to RGB if necessary
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Get image data
        image_array = np.array(image)
        pixels = image_array.reshape(-1, 3)
        
        # Use k-means clustering to find dominant colors
        from sklearn.cluster import KMeans
        
        kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init=10)
        kmeans.fit(pixels)
        
        # Get the dominant colors
        colors = kmeans.cluster_centers_.astype(int)
        
        return [tuple(color) for color in colors]
        
    except Exception as e:
        print(f"Error extracting color palette: {e}")
        # Return default colors
        return [(128, 128, 128)] * num_colors

def format_confidence_score(confidence):
    """
    Format confidence score for display.
    
    Args:
        confidence (float): Confidence score between 0 and 1
        
    Returns:
        str: Formatted confidence string
    """
    percentage = confidence * 100
    if percentage >= 90:
        return f"{percentage:.1f}% (Very High)"
    elif percentage >= 70:
        return f"{percentage:.1f}% (High)"
    elif percentage >= 50:
        return f"{percentage:.1f}% (Moderate)"
    elif percentage >= 30:
        return f"{percentage:.1f}% (Low)"
    else:
        return f"{percentage:.1f}% (Very Low)"

def get_style_description(style_name):
    """
    Get a description of a fashion style.
    
    Args:
        style_name (str): Name of the fashion style
        
    Returns:
        str: Description of the style
    """
    descriptions = {
        'casual': 'Relaxed, comfortable clothing suitable for everyday activities. Features simple cuts, comfortable fabrics, and practical designs.',
        'formal': 'Elegant, sophisticated attire appropriate for business, special occasions, or professional settings. Emphasizes clean lines and refined details.',
        'sporty': 'Athletic-inspired clothing designed for active lifestyles. Includes performance fabrics, functional design, and comfortable fit.',
        'vintage': 'Fashion styles inspired by or from previous decades. Features classic patterns, traditional cuts, and nostalgic elements.',
        'bohemian': 'Free-spirited, artistic style with flowing fabrics, earth tones, and eclectic patterns. Often includes natural materials and relaxed fits.',
        'streetwear': 'Urban-inspired casual fashion with influences from hip-hop, skateboarding, and youth culture. Features bold designs and comfortable fits.',
        'minimalist': 'Clean, simple designs with neutral colors and uncluttered aesthetics. Focuses on quality, fit, and versatile pieces.',
        'glamorous': 'Eye-catching, luxurious styles with sophisticated details, rich fabrics, and statement pieces designed to make an impression.'
    }
    
    return descriptions.get(style_name.lower(), 'A distinctive fashion style with its own unique characteristics.')
