import streamlit as st

# Page Configuration
st.set_page_config(page_title="Ankit Anand Portfolio", layout="wide")

# Custom CSS for Styling
def add_custom_css():
    st.markdown(
        """
        <style>
        body {
            background-color: black;
            color: #00FF00;
            font-family: "Courier New", Courier, monospace;
        }
        .css-18e3th9 {
            padding-top: 1rem;
        }
        .css-1d391kg h1, h2, h3, h4, h5, h6 {
            color: #00FF00 !important;
        }
        .css-1d391kg p {
            color: white !important;
        }
        .menu-bar {
            background-color: black;
            color: #00FF00;
            display: flex;
            justify-content: center;
            padding: 10px;
            font-size: 18px;
            margin-bottom: 30px;
            border-bottom: 1px solid #00FF00;
        }
        .menu-bar a {
            color: #00FF00;
            text-decoration: none;
            margin: 0 20px;
        }
        .menu-bar a:hover {
            text-decoration: underline;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Add CSS
add_custom_css()

# Create Horizontal Menu
def menu_bar():
    st.markdown(
        """
        <div class="menu-bar">
            <a href="/" target="_self">Home</a>
            <a href="#about-me" target="_self">About Me</a>
            <a href="#experience" target="_self">Experience</a>
            <a href="#education" target="_self">Education</a>
            <a href="#skills" target="_self">Skills</a>
            <a href="#certifications-projects" target="_self">Certifications & Projects</a>
        </div>
        """,
        unsafe_allow_html=True
    )

menu_bar()

# Sections
st.title("Welcome to Ankit Anand's Portfolio")
st.markdown(
    """
    **Hi there!** I am a passionate professional with expertise in **Machine Learning**, **Deep Learning**, and **Software Development**.
    """
)
st.image("ankit.jpg", caption="Your Photo Here", use_container_width=True)

st.header("About Me", anchor="about-me")
st.markdown(
    """
    I am currently a **Research Assistant** at Bauhaus University, specializing in **Machine Learning** and **Computer Vision**.
    With a Master's degree in **Digital Engineering**, I possess strong programming skills in Python and hands-on experience with
    frameworks like TensorFlow and PyTorch.

    My journey includes significant roles in leading teams, developing scalable solutions, and contributing to impactful projects
    in various domains like AI, IoT, and workplace well-being.
    """
)

st.header("Professional Experience", anchor="experience")
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

st.header("Education", anchor="education")
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

st.header("Skills", anchor="skills")
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

st.header("Certifications & Projects", anchor="certifications-projects")

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
