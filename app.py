import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page title
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to", ["Overall", "Introduction", "Methodology", "Results", "Recommendations", "test"])

# Ensure directories exist
data_dir = "data"
image_dir = "images"
plot_dir = "plots"

os.makedirs(data_dir, exist_ok=True)
os.makedirs(image_dir, exist_ok=True)
os.makedirs(plot_dir, exist_ok=True)

# Overall Section
if menu == "Overall":
    st.title("Overall Summary")
    st.write("This is an overview of the project.")

    # Display an image from images folder
    overall_img_path = os.path.join(image_dir, "word_cloud.png")
    if os.path.exists(overall_img_path):
        st.image(overall_img_path, caption="Project Overview", use_column_width=True)
    else:
        st.warning("No overview image found. Please add an image to `images/` directory.")

    # Test here on displaying a table

    st.write("Here's our first attempt at using data to create a table:")
    st.write(pd.DataFrame({
        'first column': [1, 2, 3, 4],
        'second column': [10, 20, 30, 40]
    }))


# Introduction Section
elif menu == "Introduction":
    st.title("Introduction")
    st.write("Project background and objectives.")

# Methodology Section
elif menu == "Methodology":
    st.title("Methodology")
    st.write("Describe the approach, techniques, and tools used.")

    st.markdown("""
    - **Step 1**: Data Collection
    - **Step 2**: Data Cleaning
    - **Step 3**: Model Training
    - **Step 4**: Evaluation
    """)

# Results Section
elif menu == "Results":
    st.title("Results")
    st.write("Findings and visualizations.")

    # Load sample data
    data_path = os.path.join(data_dir, "sample_data.csv")
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        st.table(df)
    else:
        st.warning("No data file found. Please add a CSV file to `data/` directory.")

# Recommendations Section
elif menu == "Recommendations":
    st.title("Recommendations")
    st.write("Provide insights and future recommendations.")


# test Section
elif menu == "test":
    st.title("test")
    st.write("This is a test")

    st.markdown("""
    - **Step 1**: Data Collection
    - **Step 2**: Data Cleaning
    - **Step 3**: Model Training
    - **Step 4**: Evaluation
    """)

# Footer
st.sidebar.write("Developed using Streamlit")
