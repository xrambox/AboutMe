import streamlit as st

# Page Configuration
st.set_page_config(page_title="Ankit Anand Portfolio", layout="wide")

# Sidebar for Navigation
st.sidebar.title("Navigation")
sections = ["Home", "About Me", "Experience", "Education", "Skills", "Certifications & Projects"]
section = st.sidebar.radio("Go to", sections)

# Home Section
if section == "Home":
    st.title("Welcome to Ankit Anand's Portfolio")
    st.markdown(
        """
        **Hi there!** I am a passionate professional with expertise in **Machine Learning**, **Deep Learning**, and **Software Development**.
        """
    )
    st.image("placeholder.jpg", caption="Your Photo Here", use_column_width=True)

# About Me Section
elif section == "About Me":
    st.header("About Me")
    st.markdown(
        """
        I am currently a **Research Assistant** at Bauhaus University, specializing in **Machine Learning** and **Computer Vision**.
        With a Master's degree in **Digital Engineering**, I possess strong programming skills in Python and hands-on experience with
        frameworks like TensorFlow and PyTorch.

        My journey includes significant roles in leading teams, developing scalable solutions, and contributing to impactful projects
        in various domains like AI, IoT, and workplace well-being.
        """
    )

# Experience Section
elif section == "Experience":
    st.header("Professional Experience")
    st.subheader("Research Assistant - ML and DL (Computer Vision)")
    st.write("**Bauhaus University**, Weimar, Germany | July 2024 – Present")
    st.markdown(
        """
        - Assisted in research projects focused on **Machine Learning** and **Computer Vision**.
        - Developed and optimized deep learning models using **TensorFlow** and **PyTorch**.
        - Maintained code in Git repositories and presented research findings in meetings.
        """
    )

    st.subheader("Senior Software Engineer")
    st.write("**LTI Mindtree**, Pune, India | Aug 2021 – Sep 2023")
    st.markdown(
        """
        - Led a team of 8 developers for **Machine Learning** and software development projects.
        - Implemented solutions with **Django**, **Flask**, and ML algorithms like **SVMs** and **CNNs**.
        - Improved product features and performance by integrating ML models.
        """
    )

    st.subheader("Network Engineer")
    st.write("**Orange Business Services**, Gurgaon, India | July 2018 – Aug 2021")
    st.markdown(
        """
        - Advanced from Graduate Engineer Trainee to Network Engineer.
        - Developed in-house software solutions and collaborated on network optimization.
        - Gained expertise in Python, MongoDB, and software tools.
        """
    )

# Education Section
elif section == "Education":
    st.header("Education")
    st.subheader("Master in Digital Engineering")
    st.write("**Bauhaus University**, Weimar, Thuringia | Oct 2023 – Jun 2025")
    st.markdown(
        """
        - Specialized in **Machine Learning**, **Deep Learning**, and **Computer Vision**.
        - Proficient in frameworks like **PyTorch** and **OpenCV**.
        """
    )

    st.subheader("Bachelor in Electronics and Communication")
    st.write("**Lakshmi Narain College of Technology**, Bhopal, India | Sep 2014 – Jun 2018")
    st.markdown(
        """
        - Graduated with honors, completing coursework in **Electronics**, **JAVA**, and **C++**.
        - Demonstrated integration of programming with hardware concepts through various projects.
        """
    )

# Skills Section
elif section == "Skills":
    st.header("Skills")
    st.markdown(
        """
        - **Programming Languages**: Python, C++, JAVA, C#, MATLAB, JavaScript
        - **Tools**: Docker, GitHub, Jenkins, Gradle
        - **Machine Learning Algorithms**: CNNs, SVMs, Decision Trees, Random Forests
        - **Deep Learning**: RNNs, LSTMs, GANs
        - **Computer Vision**: TensorFlow, Keras, PyTorch, OpenCV
        - **Management Tools**: JIRA, HPALM
        - **Languages**: German, English, Hindi
        """
    )

# Certifications & Projects Section
elif section == "Certifications & Projects":
    st.header("Certifications & Projects")

    st.subheader("Certifications")
    st.markdown(
        """
        - Data Manipulation with Pandas Python (DataCamp)
        - Intermediate Python (DataCamp)
        - Introduction to Python (DataCamp)
        - CCNA (Credly)
        """
    )

    st.subheader("Projects")
    st.markdown(
        """
        - **WorkSense**: AI-driven workplace stress detection.
        - **Neurodegenerative Disorder Analysis**: Published research on Parkinson's disease using neural networks.
        - **IoTech Homes**: IoT-based home automation system.
        - **Smart Parking System**: Real-time parking slot management using Raspberry Pi.
        """
    )