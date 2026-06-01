import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | Portfolio", layout="wide", initial_sidebar_state="collapsed")

# --- CHÂLON PARIS INSPIRED CSS ---
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
    
    .intro-text {
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
        max-width: 1000px; 
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
        justify-content: center;
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
    
    /* Image styling */
    .stImage img {
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION WITH TEXT OVERLAY ---
st.image("IMG_0433.jpeg", use_container_width=True)

# CSS trick to pull the title up over the image with crisp white text
# Changed margin-top to -25rem to push the text much higher up the page
st.markdown("""
    <div style="margin-top: -25rem; margin-bottom: 15rem; text-align: center; position: relative; z-index: 999;">
        <h1 style="font-family: 'Playfair Display', serif; font-size: 4.5rem; color: #ffffff !important; letter-spacing: 8px; text-shadow: 2px 2px 10px rgba(0,0,0,0.6); margin: 0;">AVIVA CUI</h1>
    </div>
""", unsafe_allow_html=True)

st.write("") # Spacer

# --- PROFILE & VIDEO (SIDE-BY-SIDE) ---
col_text, col_video = st.columns([1, 1], gap="large")

with col_text:
    st.markdown("""
    <div class="intro-text">
    Grounded in Te Tiriti o Waitangi principles, I design and deliver engagement that is authentic, inclusive, and strategic, ensuring decisions are well-informed and outcomes are optimised. Alongside this, my emergency management and Duty Officer experience has strengthened my ability to communicate clearly, build trust, and support effective delivery in complex and high-stakes environments.
    </div>
    """, unsafe_allow_html=True)

with col_video:
    st.markdown("<h3 style='text-align: left; font-size: 1.2rem; margin-top: 0px; margin-bottom: 15px;'>A community engagement project for Christchurch city Chinese communities</h3>", unsafe_allow_html=True)
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")

st.markdown("---")

# --- SECTION 1: THE CONTENT STRATEGY ---
st.markdown("<h2 style='text-align: center; font-size: 1.8rem; letter-spacing: 2px;'>EXAMPLE POSTS FOR MY OWN CHINESE SOCIAL MEDIA</h2>", unsafe_allow_html=True)
st.write("") # Spacer

col1, col2, col3 = st.columns(3)

with col1:
    st.image("IMG_9584.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>The Journey</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; margin-top: -10px; text-align: center;'>Getting New Zealand Residency</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")

with col2:
    st.image("IMG_9586.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Wellness</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; margin-top: -10px; text-align: center;'>Radiance Collagen Collab</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")

with col3:
    st.image("IMG_9583.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Reach</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; margin-top: -10px; text-align: center;'>Leapmotor High-Ticket</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")

st.markdown("---")

# --- SECTION 2: METRICS & CLOSED-LOOP FEEDBACK ---
st.markdown("<h2 style='text-align: center; font-size: 1.8rem; letter-spacing: 2px;'>DATA & REALITY</h2>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 0.9rem; text-align: center; max-width: 700px; margin: auto;'>
<strong>Analytical Rigor:</strong> Tracking engagement metrics to pivot strategies and maximize reach.<br>
<strong>Campaign Scaling:</strong> Executing targeted campaigns to deliver massive engagement boosts.<br>
<strong>Founder Mindset:</strong> As the founder of a startup protein powder brand, I handle the operational reality—from customer satisfaction to supply chain logistics.
</p>
""", unsafe_allow_html=True)

st.write("")

# Minimalist light custom table, centered
metrics_html = """
<div style="display: flex; justify-content: center;">
<table style="width:90%; text-align:center; border-collapse: collapse; font-size: 0.85rem; color: #000000;">
  <tr style="border-bottom: 1px solid #000000;">
    <th style="padding: 15px 0; text-transform: uppercase; letter-spacing: 1px;">Content Category</th>
    <th style="padding: 15px 0; text-transform: uppercase; letter-spacing: 1px;">Community Goal</th>
    <th style="padding: 15px 0; text-transform: uppercase; letter-spacing: 1px;">Primary Action</th>
  </tr>
  <tr style="border-bottom: 1px solid #eaeaea;">
    <td style="padding: 15px 0;">Organic Storytelling</td>
    <td style="padding: 15px 0;">Deep Trust & Empathy</td>
    <td style="padding: 15px 0;">High Comment Velocity</td>
  </tr>
  <tr style="border-bottom: 1px solid #eaeaea;">
    <td style="padding: 15px 0;">FMCG Collabs (Collagen)</td>
    <td style="padding: 15px 0;">Product Discovery</td>
    <td style="padding: 15px 0;">High Save/Share Rate</td>
  </tr>
  <tr>
    <td style="padding: 15px 0;">High-Ticket (Auto)</td>
    <td style="padding: 15px 0;">Brand Awareness</td>
    <td style="padding: 15px 0;">Link Clicks/Inquiries</td>
  </tr>
</table>
</div>
"""
st.markdown(metrics_html, unsafe_allow_html=True)

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p style="font-family: 'Playfair Display', serif; font-size: 1.2rem; margin-bottom: 15px; color: #000000;">Let's build something beautiful together.</p>
    <p style="font-size: 0.75rem; color: #888888; text-transform: uppercase; letter-spacing: 1px;">
        cuiqiandl@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; 021 086 68972 &nbsp;&nbsp;|&nbsp;&nbsp; Ōtautahi Christchurch
    </p>
</div>
""", unsafe_allow_html=True)
