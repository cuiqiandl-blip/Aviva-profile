import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# --- CHÂLON PARIS & ZURU EDGE INSPIRED CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,500;1,400&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Montserrat', sans-serif;
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Elegant Serif Headers */
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: #000000 !important;
        font-weight: 400;
        letter-spacing: 1px;
    }
    
    /* ZURU Edge Style "Video" Animation for Hero Image */
    @keyframes subtleZoom {
        0% { transform: scale(1); }
        100% { transform: scale(1.08); }
    }
    [data-testid="stImage"] img {
        animation: subtleZoom 15s ease-in-out infinite alternate;
    }
    
    .job-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-top: 0px;
        margin-bottom: 15px;
        color: #111;
    }
    
    .job-desc {
        font-weight: 300;
        line-height: 1.8;
        color: #333333;
        font-size: 1.05rem;
        text-align: justify;
    }
    
    /* Expand the layout slightly to accommodate side-by-side columns */
    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 4rem !important;
        max-width: 1100px; 
    }
    
    /* Hide standard Streamlit branding */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* Minimalist thin lines */
    hr {
        border-top: 1px solid #e0e0e0;
        margin-top: 4rem;
        margin-bottom: 4rem;
        width: 100%;
    }
    
    /* Chic, thin-bordered buttons */
    div.stButton {
        display: flex;
        justify-content: flex-start;
    }
    div.stButton > button:first-child {
        background-color: transparent;
        color: #000000;
        border: 1px solid #000000;
        border-radius: 0px;
        font-family: 'Montserrat', sans-serif;
        text-transform: uppercase;
        font-size: 0.7rem;
        letter-spacing: 2px;
        padding: 0.6rem 1.5rem;
        margin-top: 15px;
        margin-right: 10px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* Link styling */
    a {
        color: #000000 !important;
        text-decoration: none;
        border-bottom: 1px solid #000000;
        padding-bottom: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION WITH TEXT OVERLAY ---
st.image("IMG_0433.jpeg", use_container_width=True)

# CSS trick to pull the title and profile text up over the image
st.markdown("""
    <div style="margin-top: -42rem; margin-bottom: 18rem; text-align: center; position: relative; z-index: 999; padding: 0 10%;">
        <h1 style="font-family: 'Playfair Display', serif; font-size: 4.5rem; color: #ffffff !important; letter-spacing: 8px; text-shadow: 2px 2px 10px rgba(0,0,0,0.6); margin: 0;">AVIVA CUI</h1>
        <p style="color: #ffffff !important; text-shadow: 1px 1px 6px rgba(0,0,0,0.9); font-size: 1.1rem; line-height: 1.8; font-weight: 400; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        Grounded in Te Tiriti o Waitangi principles, I design and deliver engagement that is authentic, inclusive, and strategic, ensuring decisions are well-informed and outcomes are optimised. Alongside this, my emergency management and Duty Officer experience has strengthened my ability to communicate clearly, build trust, and support effective delivery in complex and high-stakes environments.
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("") # Spacer

# --- ROLE 1: CHRISTCHURCH CITY COUNCIL ---
col_ccc_img, col_ccc_text = st.columns([1, 1], gap="large")

with col_ccc_img:
    st.image("Image_20260602072626_31_1.jpeg", use_container_width=True)

with col_ccc_text:
    st.markdown("<div class='job-title'>Engagement - Christchurch City Council</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='job-desc'>
    I work across multiple infrastructure and consultation projects to design and deliver audience-focused engagement, customer support, and communications. My role involves translating complex technical information into clear and accessible messaging, building trusted relationships with communities and stakeholders, and ensuring feedback is captured and reflected in decision-making.
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.markdown("<strong style='font-size: 0.85rem; text-transform: uppercase; letter-spacing: 1px;'>Engagement Campaign Examples:</strong>", unsafe_allow_html=True)
    btn_col1, btn_col2 = st.columns([1, 1])
    with btn_col1:
         st.link_button("VIEW INSTAGRAM REEL 1", "https://www.instagram.com/reel/CqbP8tLvxkX/?igsh=MzU0cTF0MzV2amR1")
    with btn_col2:
         st.link_button("VIEW INSTAGRAM REEL 2", "https://www.instagram.com/reel/Cpo0bQNvE91/?igsh=MWVqM2VyNTBkaGMxYg==")

st.markdown("---")

# --- ROLE 2: CIVIL DEFENCE ---
col_cd_text, col_cd_video = st.columns([1, 1], gap="large")

with col_cd_text:
    st.markdown("<div class='job-title'>Community Resilience Coordinator</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='job-desc'>
    Community resilience and emergency management specialist with experience leading preparedness initiatives, building trusted partnerships, and delivering community-centred engagement across diverse populations. Adept at bringing together communities, iwi, government agencies, emergency services, and infrastructure providers to improve preparedness, response, and recovery outcomes. Combines strategic engagement, public communications, and emergency management expertise to support resilient and well-informed communities.
    </div>
    """, unsafe_allow_html=True)

with col_cd_video:
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")

st.markdown("---")

# --- ROLE 3: DIGITAL CONTENT CREATOR ---
st.markdown("<h2 style='text-align: center; font-size: 1.8rem; letter-spacing: 2px; margin-bottom: 10px;'>DIGITAL CONTENT CREATOR</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='job-desc' style='text-align: center; max-width: 800px; margin: 0 auto 3rem auto;'>
Create engaging short-form video content, livestreams, and digital campaigns, using audience insights and storytelling techniques to strengthen engagement, grow communities, and deliver effective brand and communication outcomes.
</div>
""", unsafe_
