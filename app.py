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
    
    /* ZURU Edge Style "Video" Animation for Images */
    @keyframes subtleZoom {
        0% { transform: scale(1); }
        100% { transform: scale(1.05); }
    }
    [data-testid="stImage"] img {
        animation: subtleZoom 12s ease-in-out infinite alternate;
        transition: transform 0.3s ease;
    }
    [data-testid="stImage"] img:hover {
        transform: scale(1.02);
        animation-play-state: paused;
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

st.markdown("""
    <div style="margin-top: -42rem; margin-bottom: 22rem; text-align: center; position: relative; z-index: 999; padding: 0 10%;">
        <h1 style="font-family: 'Inter', sans-serif; font-size: 5rem; font-weight: 800; color: #ffffff !important; letter-spacing: 4px; text-shadow: 2px 2px 10px rgba(0,0,0,0.6); margin: 0;">AVIVA CUI</h1>
        <p style="font-family: 'Inter', sans-serif; color: #ffffff !important; text-shadow: 1px 1px 6px rgba(0,0,0,0.9); font-size: 1.1rem; line-height: 1.8; font-weight: 400; margin-top: 2rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        Grounded in Te Tiriti o Waitangi principles, I design and deliver engagement that is authentic, inclusive, and strategic, ensuring decisions are well-informed and outcomes are optimised. Alongside this, my emergency management and Duty Officer experience has strengthened my ability to communicate clearly, build trust, and support effective delivery in complex and high-stakes environments.
        </p>
    </div>
""", unsafe_allow_html=True)

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
        st.link_button("VIEW REEL 1", "https://www.instagram.com/reel/CqbP8tLvxkX/?igsh=MzU0cTF0MzV2amR1")
    with subcol2:
        st.image("Image_20260602214021_36_1.jpg", use_container_width=True)
        st.link_button("VIEW REEL 2", "https://www.instagram.com/reel/Cpo0bQNvE91/?igsh=MWVqM2VyNTBkaGMxYg==")

st.markdown("---")

# --- ROLE 2: DIGITAL CONTENT CREATOR (Image Left, Text Right) ---
col_dcc_img, col_dcc_text = st.columns([1.2, 1], gap="large")

with col_dcc_img:
    subcol3, subcol4, subcol5 = st.columns(3)
    with subcol3:
        st.image("IMG_9584.jpeg", use_container_width=True)
        st.markdown("<h4 style='text-align: center; font-size: 0.9rem; margin-bottom: 0px;'>The Journey</h4>", unsafe_allow_html=True)
        st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
        st.markdown("<p style='font-size: 0.65rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit log in to view*</p>", unsafe_allow_html=True)
    
    with subcol4:
        st.image("IMG_9586.jpeg", use_container_width=True)
        st.markdown("<h4 style='text-align: center; font-size: 0.9rem; margin-bottom: 0px;'>Wellness</h4>", unsafe_allow_html=True)
        st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
        st.markdown("<p style='font-size: 0.65rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit log in to view*</p>", unsafe_allow_html=True)

    with subcol5:
        st.image("IMG_9583.jpeg", use_container_width=True)
        st.markdown("<h4 style='text-align: center; font-size: 0.9rem; margin-bottom: 0px;'>Reach</h4>", unsafe_allow_html=True)
        st.link_button("VIEW POST", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")
        st.markdown("<p style='font-size: 0.65rem; color: #888888; text-align: center; margin-top: -5px;'>*Exit log in to view*</p>", unsafe_allow_html=True)

with col_dcc_text:
    st.markdown("""
    <div style="margin-top: 1rem;">
        <div class='job-title'>Digital Content Creator - Self-Employed</div>
        <div class='job-desc'>
        Outside of my professional roles, I build and manage a cross-cultural content platform on Xiaohongshu (RedNote) with 4,000+ followers and 140,000+ likes. I create short-form videos and livestream content that connect Chinese audiences with New Zealand culture, products, work life, and outdoor lifestyles.<br><br>
        I have collaborated with a range of New Zealand and international brands, including Radiance Collagen, Lorna Jane, Untouched World, Blackmores, Flavooo Protein, BioTrace, Partridge Jewellers, and Leapmotor. Through these collaborations, I have also begun supporting community engagement activities for Flavooo Protein.<br><br>
        Managing my own platform has strengthened my commercial awareness, content creation skills, audience engagement strategies, and understanding of emerging social media trends and algorithms. Please see examples of my content and brand collaborations from my account.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- ROLE 3: CIVIL DEFENCE (Text Left, Video Right) ---
col_cd_text, col_cd_video = st.columns([1, 1], gap="large")

with col_cd_text:
    st.markdown("""
    <div style="margin-top: 1rem;">
        <div class='job-title'>Community Resilience Coordinator - Christchurch City Council</div>
        <div class='job-desc'>
        I designed and delivered clear, accessible, and interactive community resilience programmes that translated complex emergency information into practical actions to strengthen emergency preparedness across diverse communities in Ōtautahi. My work also focused on building trusted partnerships with community leaders, organisations, and agencies through hui, events, workshops, and planning sessions to co-design community response plans and empower community resilience. See the preparedness video I was involved in for the Welcoming Package.<br><br>
        This experience strengthened my leadership, project coordination, and communication skills, requiring me to balance multiple responsibilities and stakeholders while working in complex and high-pressure environments.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_cd_video:
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")

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
    <td style="padding: 15px 0; font-weight: 300;">Link Clicks/Inquiries</td>
  </tr>
</table>
</div>
"""
st.markdown(metrics_html, unsafe_allow_html=True)

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 1.5rem; margin-bottom: 15px; color: #000000; text-transform: uppercase; letter-spacing: -0.5px;">Let's build something beautiful together.</p>
    <p style="font-size: 0.85rem; font-weight: 500; color: #555555; text-transform: uppercase; letter-spacing: 1px;">
        cuiqiandl@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; 021 086 68972 &nbsp;&nbsp;|&nbsp;&nbsp; Ōtautahi Christchurch
    </p>
</div>
""", unsafe_allow_html=True)
