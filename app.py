import streamlit as st
import pandas as pd
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# --- HELPER FUNCTION FOR IMAGES ---
def get_base64_of_file(file_path):
    """Reads a local image and converts it to base64 for HTML injection."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# --- DARK MODE & A JOURNAL ON EDITORIAL CSS ---
st.markdown("""
    <style>
    /* Importing bold, modern Sans-Serif fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;800&display=swap');

    /* DARK MODE OVERRIDES */
    html, body, [class*="css"], .stApp, .main {
        font-family: 'Inter', sans-serif;
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Editorial Scrolling Marquee Animation */
    @keyframes scroll-left {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    
    /* Bold, heavy Sans-Serif Headers */
    h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif;
        color: #ffffff !important;
        font-weight: 800;
        letter-spacing: -0.5px;
        text-transform: uppercase;
    }
    
    .job-title {
        font-family: 'Inter', sans-serif;
        font-size: 1.8rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: -0.5px;
        margin-top: 0px;
        margin-bottom: 15px;
        color: #ffffff;
    }
    
    .job-desc {
        font-weight: 300;
        line-height: 1.8;
        color: #cccccc; 
        font-size: 1.05rem;
        text-align: justify;
    }
    
    /* Expand the layout slightly to accommodate side-by-side columns */
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px; 
    }
    
    /* Hide standard Streamlit branding */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* =========================================
       "A JOURNAL ON" PHYSICAL BOOK LAYOUT
       ========================================= */
    .journal-book {
        display: flex;
        width: 100%;
        max-width: 1100px;
        height: 75vh;
        margin: 3rem auto 5rem auto;
        border: 1px solid #333333;
        background-color: #050505;
        box-shadow: 0 30px 60px rgba(0,0,0,0.8); /* Gives it a physical drop shadow */
    }
    .journal-left-page {
        width: 45%;
        height: 100%;
        border-right: 1px solid #333333;
        overflow: hidden;
        position: relative;
        background-color: #000000;
    }
    .journal-right-page {
        width: 55%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 0 10%;
        background-color: #050505;
    }
    
    /* Smooth, Padded Vertical Scroll (Editorial Style) */
    .scroll-track {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding-top: 2rem;
        animation: verticalScroll 40s linear infinite;
    }
    .scroll-track img {
        width: 80%; /* Leaves negative space on the sides like a printed page */
        aspect-ratio: 4 / 5; /* Creates a uniform portrait shape for all photos */
        object-fit: cover;
        margin-bottom: 3rem; /* Creates elegant negative space between photos */
        border: 1px solid #222222;
        padding: 10px; /* Creates a subtle photo frame effect */
        background: #111111;
    }
    @keyframes verticalScroll {
        0% { transform: translateY(0); }
        100% { transform: translateY(-50%); }
    }
    
    /* MASSIVE breathing room between sections */
    hr {
        border-top: 1px solid #333333;
        margin-top: 7rem;
        margin-bottom: 7rem;
        width: 100%;
    }
    
    /* Chic, dark-mode buttons */
    div.stButton {
        display: flex;
        justify-content: center;
    }
    div.stButton > button:first-child {
        background-color: transparent;
        color: #ffffff;
        border: 2px solid #ffffff;
        border-radius: 0px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 1px;
        padding: 0.6rem 1.5rem;
        margin-top: 10px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #ffffff;
        color: #000000;
    }
    
    /* Link styling */
    a {
        color: #ffffff !important;
        text-decoration: none;
        border-bottom: 2px solid #ffffff;
        padding-bottom: 2px;
        font-weight: 500;
    }
    
    /* Image spacing */
    .stImage {
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAME HEADER (TOP) ---
st.markdown("""
<h1 style="font-family: 'Inter', sans-serif; font-size: 5rem; font-weight: 800; color: #ffffff; letter-spacing: 4px; text-align: center; margin-bottom: 1rem; line-height: 1;">AVIVA CUI</h1>
""", unsafe_allow_html=True)

# --- EDITORIAL MARQUEE ---
st.markdown("""
<div style="width: 100%; overflow: hidden; background-color: #000000; color: #ffffff; border-top: 1px solid #333333; border-bottom: 1px solid #333333; padding: 12px 0; white-space: nowrap; display: flex;">
    <div style="animation: scroll-left 25s linear infinite; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; display: flex; flex-shrink: 0;">
        <span style="padding-right: 40px;">COMMUNITY BUILDING &nbsp;&nbsp;•&nbsp;&nbsp; CONTENT CREATION & STORYTELLING &nbsp;&nbsp;•&nbsp;&nbsp; AUDIENCE BEHAVIOUR & PSYCHOLOGY &nbsp;&nbsp;•&nbsp;&nbsp; CROSS-CULTURAL ENGAGEMENT &nbsp;&nbsp;•&nbsp;&nbsp; AI-DRIVEN CURIOSITY & INNOVATION</span>
        <span style="padding-right: 40px;">COMMUNITY BUILDING &nbsp;&nbsp;•&nbsp;&nbsp; CONTENT CREATION & STORYTELLING &nbsp;&nbsp;•&nbsp;&nbsp; AUDIENCE BEHAVIOUR & PSYCHOLOGY &nbsp;&nbsp;•&nbsp;&nbsp; CROSS-CULTURAL ENGAGEMENT &nbsp;&nbsp;•&nbsp;&nbsp; AI-DRIVEN CURIOSITY & INNOVATION</span>
    </div>
</div>
""", unsafe_allow_html=True)


# --- DYNAMIC IMAGE LOADER ---
# This automatically finds EVERY image currently in your GitHub folder.
# It explicitly excludes the specific images used in your job sections below, 
# so the hero flipbook only shows your lifestyle/portrait photos!

all_files = os.listdir('.')
job_images = [
    "Image_20260602213535_35_1.jpg", 
    "Image_20260602214021_36_1.jpg", 
    "IMG_9583.jpeg", 
    "IMG_9584.jpeg", 
    "IMG_9586.jpeg"
]

# Create a list of all images that are NOT in the job_images list
dynamic_hero_images = [f for f in all_files if f.lower().endswith(('.png', '.jpg', '.jpeg')) and f not in job_images]

valid_b64s = []
for img_path in dynamic_hero_images:
    b64 = get_base64_of_file(img_path)
    if b64:
        valid_b64s.append((img_path, b64))

if valid_b64s:
    # Generate HTML image tags
    images_html = ""
    for path, b64 in valid_b64s:
        ext = path.split('.')[-1]
        images_html += f'<img src="data:image/{ext};base64,{b64}" />'
    
    # Duplicate for infinite scroll loop
    infinite_scroll_html = images_html + images_html

    editorial_hero_html = f"""
    <div class="journal-book">
        <div class="journal-left-page">
            <div class="scroll-track">
                {infinite_scroll_html}
            </div>
        </div>
        <div class="journal-right-page">
            <h1 style="font-family: 'Inter', sans-serif; font-size: 4rem; font-weight: 800; color: #ffffff; letter-spacing: -2px; margin: 0 0 20px 0; line-height: 1;">PORTFOLIO.</h1>
            <p style="font-family: 'Inter', sans-serif; color: #cccccc; font-size: 1.15rem; line-height: 1.8; font-weight: 300; margin: 0; text-align: justify;">
            Grounded in Te Tiriti o Waitangi principles, I design and deliver engagement that is authentic, inclusive, and strategic, ensuring decisions are well-informed and outcomes are optimised. Alongside this, my emergency management and Duty Officer experience has strengthened my ability to communicate clearly, build trust, and support effective delivery in complex and high-stakes environments.
            </p>
        </div>
    </div>
    """
    st.markdown(editorial_hero_html, unsafe_allow_html=True)
else:
    st.warning("Please upload your portrait/hero photos to GitHub!")

st.markdown("---")

# --- ROLE 1: CHRISTCHURCH CITY COUNCIL (Text Left, Image Right) ---
col_ccc_text, col_ccc_img = st.columns([1.1, 1], gap="large")

with col_ccc_text:
    st.markdown("""
    <div style="margin-top: 1rem;">
        <div class='job-title'>Engagement - Christchurch City Council</div>
        <div class='job-desc'>
        I work across multiple infrastructure and consultation projects to deliver community engagement, customer support, and communications. My role involves managing enquiries and coordinating with internal teams to ensure issues are resolved and community members feel heard and informed. I also translate complex technical information into clear, accessible messaging, build trusted relationships with stakeholders, and ensure community feedback is reflected in project decisions. See the Reels examples I created for the Welcome Back to the Ōtākaro Avon River Corridor campaign.<br><br>
        This role has strengthened my ability to engage diverse audiences, balance competing perspectives, and deliver positive community experiences across projects including the Lincoln Road Wastewater and Road Upgrade, Central City Coach Tour Bus Parking, and Halswell Junction Road cul-de-sac renaming project.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_ccc_img:
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.image("Image_20260602213535_35_1.jpg", use_container_width=True)
        st.link_button("VIEW REEL 1", "
