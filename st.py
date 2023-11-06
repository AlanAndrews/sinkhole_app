
import streamlit as st
import tensorflow as tf

import segmentation_models as sm

from PIL import Image
import numpy as np
from tensorflow import keras
from keras import backend as K

# %env SM_FRAMEWORK="tf.keras"

# Load model
custom_objects = {'iou_score': sm.metrics.iou_score}
model = tf.keras.models.load_model('sinkhole_model2.h5', custom_objects=custom_objects)  # Load your model here

# Define a function to preprocess the input image
# def preprocess_input_image(image):
#     img = Image.open(image)
#     img = img.resize((model.input_shape[1], model.input_shape[2]))  # Resize the input image to match the model's input size
#     img = np.array(img)
#     img = img / 255.0  # Normalize the image
#     img = np.expand_dims(img, axis=0)  # Add batch dimension
#     return img


st.title("Sinkhole Prediction App")

# Upload an input image
input_image = st.file_uploader("Upload a JPG of Digital Elevation Model", type=["jpg", "jpeg"])

if input_image is not None:
    st.image(input_image, caption="Uploaded Image", use_column_width=True)
    st.write("")

    if st.button("Process"):
        st.write("Processing...")

        # Preprocess the uploaded input image
        # processed_input = preprocess_input_image(input_image)

        # Perform image processing with the model
        # output_image = model.predict(processed_input)[0]
        output_image = model.predict(input_image)

        st.image(output_image, caption="Processed Image", use_column_width=True)
