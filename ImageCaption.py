import streamlit as st
from PIL import Image
import google.generativeai as genai
import io

# Configure the API key (replace 'YOUR_API_KEY' with your actual API key)
genai.configure(api_key='AIzaSyCnMwd4OFPd0ndKbVWbylWwuZEGU3Q1y3A')

# Function to generate image captions
def generate_image_caption(image: Image.Image):
    # Create the prompt for generating captions
    prompt = "Generate a caption for this image in a sentence."

    # Choose the Gemini model
    model = genai.GenerativeModel(model_name="gemini-1.5-pro")

    # Make the LLM request for generating the caption
    response = model.generate_content([image, prompt], request_options={"timeout": 600})
    caption_text = response.text

    return caption_text

# Streamlit UI
st.title("Image Caption Generator")

# Option to either upload an image or take a picture using the camera
st.write("Upload an image or take a picture from your camera:")

# Upload an image file
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Take a picture using the camera
camera_file = st.camera_input("Take a picture")

# Determine which image to use: uploaded or camera capture
if uploaded_file is not None:
    image = Image.open(uploaded_file)
elif camera_file is not None:
    image = Image.open(camera_file)

# If an image has been provided (either uploaded or captured), process it
if uploaded_file is not None or camera_file is not None:
    # Display the uploaded or captured image
    st.image(image, caption="Selected Image", use_column_width=True)
    
    # Generate and display the caption
    if st.button("Generate Caption"):
        caption = generate_image_caption(image)
        st.write("Generated Caption:")
        st.write(caption)
