import streamlit as st
import requests

st.title("Real-Time Human Pose Estimation")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.subheader("Original Image")
    st.image(uploaded_file, use_container_width=True)

    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict/image",
        files=files
    )

    result = response.json()

    st.success(result["message"])

    st.metric(
        label="People Detected",
        value=result["people_detected"]
    )

    st.subheader("Pose Estimation Output")

    image_response = requests.get(
        "http://127.0.0.1:8000/output/latest"
    )

    if image_response.status_code == 200:

        st.image(
            image_response.content,
            use_container_width=True
        )

        st.download_button(
            label="Download Processed Image",
            data=image_response.content,
            file_name="pose_output.jpg",
            mime="image/jpeg"
        )

    else:
        st.warning("Could not load processed image.")