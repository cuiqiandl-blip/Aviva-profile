import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# --- DARK MODE & EDITORIAL CSS ---
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
        font-size: 1.8rem; /* Headline size */
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: -0.5px;
        margin-top: 0px;
        margin-bottom: 3rem; /* Extra space below title */
        color: #ffffff;
        text-align: center;
    }
    
    .job-desc {
        font-weight: 300;
        line-height: 1.8;
        color: #cccccc; 
        font-size: 0.95rem;
        text-align: justify; 
        margin: 0 auto;
        max-width: 800px; /* Constrains the text width for easy reading */
    }
    
    /* Overall layout width */
    .main .block-container {
        padding-top: 2rem !important;
        padding-bottom: 4rem !important;
        max-width
