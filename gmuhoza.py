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
    /* Base styles */
    div.block-container {
        padding-top: 0;
        max-width: 100%;
    }
    header {
        visibility: hidden;
    }
    #MainMenu {
        visibility: hidden;
    }
    
    /* Sticky navigation */
    .sticky-top {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        background-color: white;
        z-index: 999;
        border-bottom: 1px solid #dee2e6;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Main content spacing */
    .main-content {
        margin-top: 180px;
        padding: 0 15px;
    }
    
    /* Connect section */
    .connect-section {
        text-align: right;
        padding: 10px 20px;
        background-color: white;
    }
    
    /* Navigation menu */
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
    
    /* Navigation buttons */
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
        -webkit-tap-highlight-color: rgba(0,0,0,0.1); /* Better touch feedback on iOS */
        transition: background-color 0.2s ease;
    }
    .nav-button-1 {
        background-color: #e6e6e6;
        color: black;
    }
    .nav-button-2 {
        background-color: #f2f2f2;
        color: black;
    }
    .nav-button:active {
        opacity: 0.8; /* Visual feedback when tapped */
    }
    
    /* Content sections */
    .content-section {
        padding: 20px;
    }
    
    /* Responsive styles */
    @media (max-width: 992px) {
        .main-content {
            margin-top: 170px;
        }
        .content-section {
            padding: 15px;
        }
    }
    
    @media (max-width: 768px) {
        .connect-section {
            text-align: center;
            padding: 10px;
        }
        .connect-section h3 {
            font-size: 1.2rem;
            margin-bottom: 8px;
        }
        .connect-section img {
            height: 30px;
        }
        .main-content {
            margin-top: 160px;
            padding: 0 10px;
        }
        .nav-button {
            padding: 8px 15px;
            font-size: 0.9rem;
        }
    }
    
    @media (max-width: 576px) {
        .main-content {
            margin-top: 150px;
        }
        h1 {
            font-size: 1.8rem !important;
        }
        h2 {
            font-size: 1.5rem !important;
        }
        h3 {
            font-size: 1.3rem !important;
        }
        p, li {
            font-size: 0.95rem !important;
        }
        .connect-section img {
            height: 25px;
        }
        .nav-button {
            padding: 6px 12px;
            margin: 0 3px;
            font-size: 0.85rem;
        }
    }
    
    /* Add scroll margin for section anchors */
    #home, #education, #certifications, #skills, #projects, #beyond {
        scroll-margin-top: 180px;
    }
    
    @media (max-width: 768px) {
        #home, #education, #certifications, #skills, #projects, #beyond {
            scroll-margin-top: 160px;
        }
    }
    
    @media (max-width: 576px) {
        #home, #education, #certifications, #skills, #projects, #beyond {
            scroll-margin-top: 150px;
        }
    }
    
    /* Improve touch targets for mobile */
    a {
        padding: 2px 0;
        display: inline-block;
    }
    
    /* Optimize images for mobile */
    img {
        max-width: 100%;
        height: auto;
    }
    
    /* Section styling */
    .section-header {
        padding: 10px 15px;
        margin-bottom: 10px;
        background-color: #f8f9fa;
        border-left: 5px solid #0077B5;
        border-radius: 0 5px 5px 0;
    }
    
    .section-header h3 {
        margin: 0;
        color: #333;
        font-weight: 600;
    }
    
    .section-content {
        padding: 0 15px 15px 15px;
        margin-bottom: 10px;
    }
    
    /* Section dividers */
    .section-divider {
        height: 2px;
        background-color: #f0f0f0;
        margin: 20px 0;
        border: none;
    }
    
    /* Subsection styling */
    .subsection-header {
        margin-top: 20px;
        margin-bottom: 10px;
        color: #555;
        border-bottom: 2px solid #eaeaea;
        padding-bottom: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Add viewport meta tag for mobile responsiveness
st.markdown("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
""", unsafe_allow_html=True)

# Connect With Me section and Navigation Menu
st.markdown("""
    <div class="sticky-top">
        <div class="connect-section">
            <h3>Connect With Me:</h3>
            <a href="https://github.com/muhozag" aria-label="GitHub Profile"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
            <a href="https://gitlab.com/muhozag" aria-label="GitLab Profile"><img src="https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white" alt="GitLab"></a>
            <a href="https://www.linkedin.com/in/gustave-muhoza/" aria-label="LinkedIn Profile"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
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
st.markdown('<div class="section-header"><h3>Welcome!</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)
st.title("Hello! 👋 I'm Gustave Muhoza")
st.subheader("Analytics Leader | Data Engineer and Scientist")

# Brief introduction
st.markdown("""
I specialize in building secure data pipelines, implementing machine learning solutions, 
and transforming raw data into actionable insights. With an interdisciplinary background 
spanning Computer Science and International Studies, I bring a unique perspective to 
data-driven solutions.
""")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Education Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div id="education">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h3>Education</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)
st.markdown("""
- **Chief Data and Analytics Officer Executive Certificate** (Expected 2025)
- **Master of Arts in International Studies** (2007)
- **Bachelor of Science in Computer Science** (2004)
""")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Certifications Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div id="certifications">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h3>Certifications</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)

# AWS Certifications
st.markdown('<div class="subsection-header">AWS Certifications</div>', unsafe_allow_html=True)
st.markdown("[AWS Solutions Architect Associate](https://www.credly.com/badges/c3ba01d1-8684-4f6d-aed2-3742d69f6ceb/public_url)")
st.markdown("[AWS Certified AI Practitioner](https://www.credly.com/badges/b0e5ba36-4cd6-4c2e-94fe-2fc11c0d177f/public_url)")

# Azure Certifications
st.markdown('<div class="subsection-header">Azure Certifications</div>', unsafe_allow_html=True)
st.markdown("[Microsoft Certified: Azure Fundamentals ](https://learn.microsoft.com/api/credentials/share/en-us/GustaveMuhoza-6210/A63DF903563675DF?sharingId=611A5E0F1512DF0F)")

# Kubernetes & Cloud Native
st.markdown('<div class="subsection-header">Kubernetes & Cloud Native</div>', unsafe_allow_html=True)
st.markdown("[Certified Kubernetes Application Developer (CKAD)](https://www.credly.com/badges/2454ddd1-d3c2-42ad-8786-54ad13f3fb1f/public_url)")
st.markdown("[Kubernetes and Cloud Native Associate (KCNA)](https://www.credly.com/badges/42d74ff4-4dfa-4c32-a69b-b1a0a975c1ed/public_url)")

# Security
st.markdown('<div class="subsection-header">Security</div>', unsafe_allow_html=True)
st.markdown("[CompTIA Security+](https://www.credly.com/badges/efba6f70-0835-4cb5-8aeb-1e6d8b91f244/public_url)")

# Project Management
st.markdown('<div class="subsection-header">Project Management</div>', unsafe_allow_html=True)
st.markdown("[Johns Hopkins University AI Strategy and Project Management](https://www.coursera.org/account/accomplishments/specialization/GKINAQPFA23R)")
st.markdown("[Certified SAFe 5 Government Practitioner](https://www.credly.com/badges/3c850285-15e8-435d-865a-53669e7a0c9f/public_url)")

# Data Science
st.markdown('<div class="subsection-header">Data Science</div>', unsafe_allow_html=True)
st.markdown("[IBM Professional Data Science Certificate](https://www.credly.com/badges/3efe72b3-d511-4b0a-b0ed-2db53c696ba6/public_url)")

# Supply Chain Security
st.markdown('<div class="subsection-header">Supply Chain Security</div>', unsafe_allow_html=True)
st.markdown("[Painless Vulnerability Management with Chainguard](https://www.credly.com/badges/aa4040e1-e054-4b2d-96b3-2f476bc3e066/public_url)")
st.markdown("[Securing the AI/ML Supply Chain with Chainguard](https://www.credly.com/badges/80f5e9d5-bbd2-495e-992c-98eb044faac2/public_url)")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Technical Skills Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div id="skills">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h3>Technical Skills</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)
st.markdown('<div class="subsection-header">Data Engineering & Big Data</div>', unsafe_allow_html=True)
st.markdown("""
- **Core Technologies:** ETL/ELT, Data Warehousing, Data Modeling
- **Big Data Tools:** PySpark, Apache Kafka
- **Cloud & Platforms:** AWS, Azure, Databricks
""")

st.markdown('<div class="subsection-header">Development & DevOps</div>', unsafe_allow_html=True)
st.markdown("""
- **Programming Languages and Frameworks:** Python, SQL, JavaScript, Node.js, Django, Flask, React
- **Version Control & CI/CD:** Git, GitHub, GitLab, CI/CD Pipelines
- **Data Visualization:** PowerBI, QuickSight, Streamlit
""")

st.markdown('<div class="subsection-header">Data Science</div>', unsafe_allow_html=True)
st.markdown("""
- **Core Skills:** Machine Learning, Statistical Analysis
- **Tools:** SageMaker
""")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div id="projects">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h3>Featured Projects</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)
st.markdown("""
Always trying exciting data projects to learn the newest technologies of interest! Check my GitHub and GitLab profiles for more details.
""")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Beyond Tech Section
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.markdown('<div id="beyond">', unsafe_allow_html=True)
st.markdown('<div class="section-header"><h3>Beyond Tech</h3></div>', unsafe_allow_html=True)
st.markdown('<div class="section-content">', unsafe_allow_html=True)
st.markdown("""
I believe in maintaining a well-rounded lifestyle that combines technical expertise with cultural interests:

- ***Languages:*** Fluent in English, French, Kinyarwanda and Spanish; more than basic Swahili; currently learning Amharic
- **Sports:** Passionate follower of La Liga soccer and Pittsburgh Steelers football
- **Dance:** Salsa Dura, Bachata Classica
""")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)
st.write("Feel free to reach out for collaborations or discussions!")

# Close the main-content div
st.markdown("""
    </div>
    
    <!-- Add JavaScript for better mobile experience -->
    <script>
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 160,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Fix for iOS momentum scrolling
        document.querySelector('.nav-menu').addEventListener('touchmove', function(e) {
            e.stopPropagation();
        }, { passive: true });
    </script>
""", unsafe_allow_html=True)
