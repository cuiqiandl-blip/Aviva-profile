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
        border-bottom: 2px solid #000000;
        padding-bottom: 2px;
        font-weight: 500;
    }
    
    /* Image spacing */
    .stImage {
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HERO SECTION WITH TEXT OVERLAY ---
st.image("IMG_0433.jpeg", use_container_width=True)

# CSS trick to pull the title and profile text up over the image
st.markdown("""
    <div style="margin-top: -42rem; margin-bottom: 22rem; text-align: center; position: relative; z-index: 999; padding: 0 10%;">
        <h1 style="font-family: 'Inter', sans-serif; font-size: 5rem; font-weight: 800; color: #ffffff !important; letter-spacing: 4px; text-shadow: 2px 2px 10px rgba(0,0,0,0.6); margin: 0;">AVIVA CUI</h1>
        <p style="font-family: 'Inter', sans-serif; color: #ffffff !important; text-shadow: 1px 1px 6px rgba(0,0,0,0.9); font-size: 1.1rem; line-height: 1.8; font-weight: 400; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        Grounded in Te Tiriti o Waitangi principles, I design and deliver engagement that is authentic, inclusive, and strategic, ensuring decisions are well-informed and outcomes are optimised. Alongside this, my emergency management and Duty Officer experience has strengthened my ability to communicate clearly, build trust, and support effective delivery in complex and high-stakes environments.
        </p>
    </div>
""", unsafe_allow_html=True)

# --- ROLE 1: CHRISTCHURCH CITY COUNCIL ---
col_ccc_text, col_ccc_img = st.columns([1, 1], gap="large")

with col_ccc_text:
    st.markdown("""
    <div style="margin-top: 3.5rem;">
        <div class='job-title'>Engagement - Christchurch City Council</div>
        <div class='job-desc'>
        I work across multiple infrastructure and consultation projects to design and deliver audience-focused engagement, customer support, and communications. My role involves translating complex technical information into clear and accessible messaging, building trusted relationships with communities and stakeholders, and ensuring feedback is captured and reflected in decision-making. See the Reels examples that I created for the Welcome Back to the Ōtākaro Avon River Corridor campaign.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_ccc_img:
    subcol1, subcol2 = st.columns(2)
    with subcol1:
        st.image("Image_20260602213535_35_1.jpg", use_container_width=True)
        st.link_button("VIEW REEL 1", "https://www.instagram.com/reel/CqbP8tLvxkX/?igsh=MzU0cTF0MzV2amR1")
    with subcol2:
        st.image("Image_20260602214021_36_1.jpg", use_container_width=True)
        st.link_button("VIEW REEL 2", "https://www.instagram.com/reel/Cpo0bQNvE91/?igsh=MWVqM2VyNTBkaGMxYg==")

st.markdown("---")

# --- ROLE 2: CIVIL DEFENCE ---
col_cd_video, col_cd_text = st.columns([1, 1], gap="large")

with col_cd_video:
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")

with col_cd_text:
    st.markdown("""
    <div style="margin-top: 2rem;">
        <div class='job-title'>Community Resilience Coordinator</div>
        <div class='job-desc'>
        I design and deliver community resilience programmes that strengthen emergency preparedness and participation across diverse communities. My work focuses on building trusted partnerships with community leaders, organisations, and agencies to co-design inclusive and culturally responsive initiatives. I facilitate training, workshops, and planning sessions that translate complex emergency information into clear, practical guidance, and I support coordinated multi-agency efforts during response and recovery events while maintaining effective community communication. See the preparedness video I was involved in for the Welcoming Package.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- ROLE 3: DIGITAL CONTENT CREATOR ---
st.markdown("<div class='job-title' style='text-align: center; font-size: 2.2rem;'>DIGITAL CONTENT CREATOR</div>", unsafe_allow_html=True)
st.markdown("""
<div class='job-desc' style='text-align: center; max-width: 900px; margin: 0 auto 4rem auto;'>
I build and manage a cross-cultural digital content platform with 4,000+ followers and 140,000+ likes, creating engaging short-form videos and livestream content that connect Kiwi and Chinese audiences through culture, products, work life, and outdoor lifestyles. My work focuses on storytelling, audience engagement, and community building, supported by regular analysis of engagement metrics to refine content strategy and improve reach. I also collaborate with local and international brands on sponsored content and campaigns, ensuring alignment between audience interests and brand objectives while delivering authentic and engaging digital experiences.
</div>
""", unsafe_allow_html=True)

st.markdown("<h4 style='text-align: center; font-size: 1.1rem; letter-spacing: 1px; color: #555; margin-bottom: 2.5rem;'>EXAMPLE POSTS FOR MY OWN CHINESE SOCIAL MEDIA</h4>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.image("IMG_9584.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center; font-size: 1.1rem; margin-bottom: 0px;'>The Journey</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.85rem; font-weight: 300; margin-top: 0px; text-align: center;'>Getting New Zealand Residency</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.75rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit the log in pop up to view the video*</p>", unsafe_allow_html=True)

with col2:
    st.image("IMG_9586.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center; font-size: 1.1rem; margin-bottom: 0px;'>Wellness</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.85rem; font-weight: 300; margin-top: 0px; text-align: center;'>Radiance Collagen Collab</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.75rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit the log in pop up to view the video*</p>", unsafe_allow_html=True)

with col3:
    st.image("IMG_9583.jpeg", use_container_width=True)
    st.markdown("<h4 style='text-align: center; font-size: 1.1rem; margin-bottom: 0px;'>Reach</h4>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.85rem; font-weight: 300; margin-top: 0px; text-align: center;'>Leapmotor High-Ticket</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")
    st.markdown("<p style='font-size: 0.75rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit the log in pop up to view the video*</p>", unsafe_allow_html=True)

st.markdown("---")

# --- DATA & REALITY ---
st.markdown("<div class='job-title' style='text-align: center;'>DATA & REALITY</div>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size: 1rem; font-weight: 300; text-align: center; max-width: 700px; margin: auto;'>
<strong>Analytical Rigor:</strong> Tracking engagement metrics to pivot strategies and maximize reach.<br>
<strong>Campaign Scaling:</strong> Executing targeted campaigns to deliver massive engagement boosts.<br>
<strong>Founder Mindset:</strong> As the founder of a startup protein powder brand, I handle the operational reality—from customer satisfaction to supply chain logistics.
</p>
""", unsafe_allow_html=True)

st.write("")

# Minimalist light custom table, centered
metrics_html = """
<div style="display: flex; justify-content: center;">
<table style="width:90%; text-align:center; border-collapse: collapse; font-size: 0.9rem; color: #000000; font-family: 'Inter', sans-serif;">
  <tr style="border-bottom: 2px solid #000000;">
    <th style="padding: 15px 0; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Content Category</th>
    <th style="padding: 15px 0; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Community Goal</th>
    <th style="padding: 15px 0; font-weight: 800; text-transform: uppercase; letter-spacing: 0.5px;">Primary Action</th>
  </tr>
  <tr style="border-bottom: 1px solid #eaeaea;">
    <td style="padding: 15px 0; font-weight: 300;">Organic Storytelling</td>
    <td style="padding: 15px 0; font-weight: 300;">Deep Trust & Empathy</td>
    <td style="padding: 15px 0; font-weight: 300;">High Comment Velocity</td>
  </tr>
  <tr style="border-bottom: 1px solid #eaeaea;">
    <td style="padding: 15px 0; font-weight: 300;">FMCG Collabs (Collagen)</td>
    <td style="padding: 15px 0; font-weight: 300;">Product Discovery</td>
    <td style="padding: 15px 0; font-weight: 300;">High Save/Share Rate</td>
  </tr>
  <tr>
    <td style="padding: 15px 0; font-weight: 300;">High-Ticket (Auto)</td>
    <td style="padding: 15px 0; font-weight: 300;">Brand Awareness</td>
    <td
