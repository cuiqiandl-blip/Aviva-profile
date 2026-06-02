import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# --- ZURU EDGE INSPIRED CSS ---
st.markdown("""
    <style>
    /* Importing bold, modern Sans-Serif fonts matching ZURU Edge */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;700;800&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Inter', sans-serif;
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* ZURU Edge Style "Video" Animation for Hero Image */
    @keyframes subtleZoom {
        0% { transform: scale(1); }
        100% { transform: scale(1.08); }
    }
    [data-testid="stImage"] img {
        animation: subtleZoom 15s ease-in-out infinite alternate;
    }
    
    /* Bold, heavy Sans-Serif Headers */
    h1, h2, h3, h4 {
        font-family: 'Inter', sans-serif;
        color: #000000 !important;
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
        color: #000000;
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
    
    /* MASSIVE breathing room between sections */
    hr {
        border-top: 1px solid #e0e0e0;
        margin-top: 7rem;
        margin-bottom: 7rem;
        width: 100%;
    }
    
    /* Chic, thin-bordered buttons */
    div.stButton {
        display: flex;
        justify-content: center; /* Centered under images */
    }
    div.stButton > button:first-child {
        background-color: transparent;
        color: #000000;
        border: 2px solid #000000;
        border-radius: 0px;
        font-family: 'Inter', sans-serif;
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 1px;
        padding: 0.6rem 1.5rem;
        margin-top: 10px;
        transition: all 0.3s
