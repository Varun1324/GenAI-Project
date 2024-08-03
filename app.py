import streamlit as st
from script import get_data

def main():
    # URL of the image
    st.title("Dog Breed identifier using Generative AI")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Display success message
        st.success(f"File {uploaded_file.name} uploaded successfully")
        st.image(uploaded_file,caption='uploaded image', use_column_width=False, width=200)
        result_ = get_data(uploaded_file)
        st.markdown(result_)
    else:
        st.error("Upload a image")
if __name__ == "__main__":
    main()

