
import streamlit as st

def capture_food_image():
    option = st.radio("Choose Input Method:", ["Upload Image", "Camera"], horizontal=True)
    if option == "Upload Image":
        uploaded_file = st.file_uploader("Upload your food image", type=["jpg", "png"])
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    else:
        camera_img = st.camera_input("Take a picture of your meal")
        if camera_img:
            st.image(camera_img, caption="Captured Image", use_column_width=True)
