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
    
    .job-title {
        font-family: 'Playfair Display', serif;
        font-size: 1.3rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 15px;
        margin-bottom: 10px;
        color: #111;
    }
    
    .job-desc {
        font-weight: 300;
        line-height: 1.8;
        color: #333333;
        font-size: 0.95rem;
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
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION WITH TEXT OVERLAY ---
st.image("IMG_0433.jpeg", use_container_width=True)

# CSS trick to pull the title and profile text up over the image
# If the text needs to go higher or lower, change the "-42rem" value
st.markdown("""
    <div style="margin-top: -42rem; margin-bottom: 18rem; text-align: center; position: relative; z-index: 999; padding: 0 10%;">
        <h1 style="font-family: 'Playfair Display', serif; font-size: 4.5rem; color: #ffffff !important; letter-spacing: 8px; text-shadow: 2px 2px 10px rgba(0,0,0,0.6); margin: 0;">AVIVA CUI</h1>
        <p style="color: #ffffff !important; text-shadow: 1px 1px 6px rgba(0,0,0,0.9); font-size: 1.1rem; line-height: 1.8; font-weight: 400; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        Grounded in Te Tiriti o Waitangi principles, I design and deliver engagement that is authentic, inclusive, and strategic, ensuring decisions are well-informed and outcomes are optimised. Alongside this, my emergency management and Duty Officer experience has strengthened my ability to communicate clearly, build trust, and support effective delivery in complex and high-stakes environments.
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("") # Spacer

# --- EXPERIENCE SECTION 1 & 2 (SIDE-BY-SIDE) ---
col_job1, col_job2 = st.columns([1, 1], gap="large")

with col_job1:
    st.image("Image_20260602072626_31_1.jpeg", use_container_width=True)
    st.markdown("<div class='job-title'>Engagement - Christchurch City Council</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='job-desc'>
    Leading stakeholder engagement across infrastructure, transport, and consultation projects. Skilled at translating complex information into accessible content, analysing community insights to inform decision-making, and building strong relationships between communities, contractors, and local government.
    </div>
    """, unsafe_allow_html=True)

with col_job2:
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")
    st.markdown("<div class='job-title'>Community Resilience Coordinator</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class='job-desc'>
    Community resilience and emergency management specialist with experience leading preparedness initiatives, building trusted partnerships, and delivering community-centred engagement across diverse populations. Adept at bringing together communities, iwi, government agencies, emergency services, and infrastructure providers to improve preparedness, response, and recovery outcomes. Combines strategic engagement, public communications, and emergency management expertise to support resilient and well-informed communities.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- EXPERIENCE SECTION 3: DIGITAL CONTENT CREATOR ---
st.markdown("<h2 style='text-align: center; font-size: 1.8rem; letter-spacing: 2px; margin-bottom: 10px;'>DIGITAL CONTENT CREATOR</h2>", unsafe_allow_html=True)
st.markdown("""
<div class='job-desc' style='text-align: center; max-width: 800px; margin: 0 auto 3rem auto;'>
Create engaging short-form video content, livestreams, and digital campaigns, using audience insights and storytelling techniques to strengthen engagement, grow communities, and deliver effective brand and communication outcomes.
</div>
""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; font-size: 1.1rem; letter-spacing: 1px; color: #555; margin-bottom: 2rem;'>EXAMPLE POSTS FOR MY OWN CHINESE SOCIAL MEDIA</h4>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("IMG_9584.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>The Journey</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; margin-top: -10px; text-align: center;'>Getting New Zealand Residency</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.7rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit the log in pop up to view the video*</p>", unsafe_allow_html=True)

with col2:
    st.image("IMG_9586.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Wellness</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; margin-top: -10px; text-align: center;'>Radiance Collagen Collab</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.7rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit the log in pop up to view the video*</p>", unsafe_allow_html=True)

with col3:
    st.image("IMG_9583.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center;'>Reach</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.8rem; margin-top: -10px; text-align: center;'>Leapmotor High-Ticket</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")
    st.markdown("<p style='font-size: 0.7rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit the log in pop up to view the video*</p>", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION 4: METRICS & CLOSED-LOOP FEEDBACK ---
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
