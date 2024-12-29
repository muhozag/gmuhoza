import streamlit as st

# Set page config
st.set_page_config(
    page_title="Gustave Muhoza",
    page_icon="👨‍💻",
    layout="wide"
)

# Custom CSS for navigation buttons and layout
st.markdown("""
    <style>
    div.block-container {
        padding-top: 0;
    }
    header {
        visibility: hidden;
    }
    #MainMenu {
        visibility: hidden;
    }
    .sticky-top {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: white;
        z-index: 999;
        border-bottom: 1px solid #dee2e6;
    }
    .main-content {
        margin-top: 180px;
    }
    .connect-section {
        text-align: right;
        padding: 10px 20px;
        background-color: white;
    }
    /* New mobile-friendly navigation styles */
    .nav-menu {
        display: flex;
        overflow-x: auto;
        white-space: nowrap;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none; /* Firefox */
        -ms-overflow-style: none; /* IE and Edge */
        padding: 10px 5px;
        background-color: white;
    }
    .nav-menu::-webkit-scrollbar {
        display: none; /* Chrome, Safari, Opera */
    }
    .nav-button {
        display: inline-block;
        flex: 0 0 auto;
        padding: 10px 20px;
        margin: 0 5px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        min-width: max-content;
    }
    .nav-button-1 {
        background-color: #e6e6e6;
        color: black;
    }
    .nav-button-2 {
        background-color: #f2f2f2;
        color: black;
    }
    .content-section {
        padding: 20px 40px;
    }
    /* Responsive connect section */
    @media (max-width: 768px) {
        .connect-section {
            text-align: center;
            padding: 10px;
        }
        .connect-section img {
            height: 30px;
        }
        .main-content {
            margin-top: 160px;
        }
    }
    /* Add scroll margin for section anchors */
    #home, #education, #certifications, #skills, #projects, #beyond {
        scroll-margin-top: 180px;
    }
    </style>
""", unsafe_allow_html=True)
# Connect With Me section and Navigation Menu
st.markdown("""
    <div class="sticky-top">
        <div class="connect-section">
            <h3>Connect With Me:</h3>
            <a href="https://github.com/muhozag"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></a>
            <a href="https://gitlab.com/muhozag"><img src="https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white"></a>
            <a href="https://www.linkedin.com/in/gustave-muhoza/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white"></a>
        </div>
        <div class="nav-menu">
            <a href="#home" class="nav-button nav-button-1">Home</a>
            <a href="#education" class="nav-button nav-button-2">Education</a>
            <a href="#certifications" class="nav-button nav-button-1">Certifications</a>
            <a href="#skills" class="nav-button nav-button-2">Technical Skills</a>
            <a href="#projects" class="nav-button nav-button-1">Projects</a>
            <a href="#beyond" class="nav-button nav-button-2">Beyond Tech</a>
        </div>
    </div>
    <div class="main-content">
""", unsafe_allow_html=True)

# Welcome section
st.markdown('<div id="home">', unsafe_allow_html=True)
st.title("Welcome! 👋")
st.header("I'm Gustave Muhoza")
st.subheader("Data Engineer/Data Scientist")

# Brief introduction
st.markdown("""
I specialize in building secure data pipelines, implementing machine learning solutions, 
and transforming raw data into actionable insights. With an interdisciplinary background 
spanning Computer Science and International Studies, I bring a unique perspective to 
data-driven solutions.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Education Section
st.markdown("---")
st.markdown('<div id="education">', unsafe_allow_html=True)
st.markdown("""
### Education
- **Chief Data and Analytics Officer Executive Certificate** (Expected 2025)
- **Master of Arts in International Studies** (2007)
- **Bachelor of Science in Computer Science** (2004)
""")
st.markdown('</div>', unsafe_allow_html=True)

# Certifications Section
st.markdown("---")
st.markdown('<div id="certifications">', unsafe_allow_html=True)
st.markdown("### Certifications")

# AWS Certifications
st.markdown("#### AWS Certifications")
st.markdown("[AWS Solutions Architect Associate](https://www.credly.com/badges/c3ba01d1-8684-4f6d-aed2-3742d69f6ceb/public_url)")
st.markdown("[AWS Certified AI Practitioner](https://www.credly.com/badges/b0e5ba36-4cd6-4c2e-94fe-2fc11c0d177f/public_url)")

# Azure Certifications
st.markdown("#### Azure Certifications")
st.markdown("[Microsoft Certified: Azure Fundamentals ](https://learn.microsoft.com/api/credentials/share/en-us/GustaveMuhoza-6210/A63DF903563675DF?sharingId=611A5E0F1512DF0F)")

# Kubernetes & Cloud Native
st.markdown("#### Kubernetes & Cloud Native")
st.markdown("[Certified Kubernetes Application Developer (CKAD)](https://www.credly.com/badges/2454ddd1-d3c2-42ad-8786-54ad13f3fb1f/public_url)")
st.markdown("[Kubernetes and Cloud Native Associate (KCNA)](https://www.credly.com/badges/42d74ff4-4dfa-4c32-a69b-b1a0a975c1ed/public_url)")

# Security
st.markdown("#### Security")
st.markdown("[CompTIA Security+](https://www.credly.com/badges/efba6f70-0835-4cb5-8aeb-1e6d8b91f244/public_url)")

# Project Management
st.markdown("#### Project Management")
st.markdown("[Certified SAFe 5 Government Practitioner](https://www.credly.com/badges/3c850285-15e8-435d-865a-53669e7a0c9f/public_url)")

# Data Science
st.markdown("#### Data Science")
st.markdown("[IBM Professional Data Science Certificate](https://www.credly.com/badges/3efe72b3-d511-4b0a-b0ed-2db53c696ba6/public_url)")

# Supply Chain Security
st.markdown("#### Supply Chain Security")
st.markdown("[Painless Vulnerability Management with Chainguard](https://www.credly.com/badges/aa4040e1-e054-4b2d-96b3-2f476bc3e066/public_url)")
st.markdown("[Securing the AI/ML Supply Chain with Chainguard](https://www.credly.com/badges/80f5e9d5-bbd2-495e-992c-98eb044faac2/public_url)")
st.markdown('</div>', unsafe_allow_html=True)

# Technical Skills Section
st.markdown("---")
st.markdown('<div id="skills">', unsafe_allow_html=True)
st.markdown("""
### Technical Skills

#### Data Engineering & Big Data
- **Core Technologies:** ETL/ELT, Data Warehousing, Data Modeling
- **Big Data Tools:** PySpark, Apache Kafka
- **Cloud & Platforms:** AWS, Azure, Databricks

#### Development & DevOps
- **Programming Languages and Frameworks:** Python, SQL, JavaScript, Node.js, Django, Flask, React
- **Version Control & CI/CD:** Git, GitHub, GitLab, CI/CD Pipelines
- **Data Visualization:** PowerBI, QuickSight, Streamlit

#### Data Science
- **Core Skills:** Machine Learning, Statistical Analysis
- **Tools:** SageMaker
""")
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown("---")
st.markdown('<div id="projects">', unsafe_allow_html=True)
st.markdown("""
### Featured Projects
Always trying exciting data projects to learn the newest technologies of interest! Check my GitHub and GitLab profiles for more details.
""")
st.markdown('</div>', unsafe_allow_html=True)

# Beyond Tech Section
st.markdown("---")
st.markdown('<div id="beyond">', unsafe_allow_html=True)
st.markdown("""
### Beyond Tech
I believe in maintaining a well-rounded lifestyle that combines technical expertise with cultural interests:

- ***Languages:*** Fluent in English, French, Kinyarwanda and Spanish; Currently learning Amharic
- **Sports:** Passionate follower of La Liga soccer
- **Dance:** Salsa Dura, Bachata Classica
""")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Feel free to reach out for collaborations or discussions!")

# Close the main-content div
st.markdown("""
    </div>
""", unsafe_allow_html=True)

