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
        font-size: 1.3rem; /* Made smaller */
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: -0.5px;
        margin-top: 0px;
        margin-bottom: 10px;
        color: #ffffff;
        text-align: center; /* Centered */
    }
    
    .job-desc {
        font-weight: 300;
        line-height: 1.7;
        color: #cccccc; 
        font-size: 0.85rem; /* Made significantly smaller */
        text-align: center; /* Centered text */
        margin: 0 auto; 
        max-width: 85%; /* Pushes text into the middle, adding breathing room */
    }
    
    /* Expand the layout slightly */
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
       "OPEN BOOK" EDITORIAL SPREAD
       ========================================= */
    .open-book-container {
        display: flex;
        width: 100%;
        max-width: 900px; /* Fixed width to guarantee the journal shape */
        height: 550px; /* Fixed height to guarantee the journal shape */
        margin: 4rem auto;
        border: 1px solid #333333;
        background-color: #050505;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }
    
    .book-left-page {
        flex: 1;
        border-right: 1px solid #333333;
        position: relative;
        padding: 2rem; /* Creates elegant padding inside the page */
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    .image-frame {
        position: relative;
        width: 100%;
        height: 100%;
        overflow: hidden;
        border: 1px solid #222222; /* Frame around the photo */
    }
    
    .book-right-page {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 3rem;
    }
    
    .fade-img {
        position: absolute;
        top: 0; left: 0; 
        width: 100%; height: 100%;
        object-fit: cover;
        opacity: 0; /* Hidden by default, controlled by animation */
    }
    
    /* MASSIVE breathing room between sections */
    hr {
        border-top: 1px solid #333333;
        margin-top: 5rem;
        margin-bottom: 5rem;
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
        font-size: 0.7rem;
        letter-spacing: 1px;
        padding: 0.5rem 1.2rem;
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
    </style>
    """, unsafe_allow_html=True)

# --- EDITORIAL MARQUEE (Moved to very top) ---
st.markdown("""
<div style="width: 100%; overflow: hidden; background-color: #000000; color: #ffffff; border-top: 1px solid #333333; border-bottom: 1px solid #333333; padding: 12px 0; white-space: nowrap; display: flex;">
    <div style="animation: scroll-left 25s linear infinite; font-family: 'Inter', sans-serif; font-weight: 700; font-size: 0.85rem; letter-spacing: 2px; text-transform: uppercase; display: flex; flex-shrink: 0;">
        <span style="padding-right: 40px;">COMMUNITY BUILDING &nbsp;&nbsp;•&nbsp;&nbsp; CONTENT CREATION & STORYTELLING &nbsp;&nbsp;•&nbsp;&nbsp; AUDIENCE BEHAVIOUR & PSYCHOLOGY &nbsp;&nbsp;•&nbsp;&nbsp; CROSS-CULTURAL ENGAGEMENT &nbsp;&nbsp;•&nbsp;&nbsp; AI-DRIVEN CURIOSITY & INNOVATION</span>
        <span style="padding-right: 40px;">COMMUNITY BUILDING &nbsp;&nbsp;•&nbsp;&nbsp; CONTENT CREATION & STORYTELLING &nbsp;&nbsp;•&nbsp;&nbsp; AUDIENCE BEHAVIOUR & PSYCHOLOGY &nbsp;&nbsp;•&nbsp;&nbsp; CROSS-CULTURAL ENGAGEMENT &nbsp;&nbsp;•&nbsp;&nbsp; AI-DRIVEN CURIOSITY & INNOVATION</span>
    </div>
</div>
""", unsafe_allow_html=True)


# --- "A JOURNAL ON" OPEN BOOK SPREAD ---
# Using the exact 6 photos requested
journal_images = [
    "IMG_0433.jpeg", 
    "IMG_9583.jpeg",
    "IMG_9584.jpeg",
    "IMG_9586.jpeg",
    "Image_20260601223856_28_1.png",
    "Image_20260602213535_35_1.jpg"
]

valid_b64s = []
for img_path in journal_images:
    b64 = get_base64_of_file(img_path)
    if b64:
        ext = img_path.split('.')[-1]
        if ext.lower() == 'jpg': ext = 'jpeg'
        valid_b64s.append((ext, b64))

if valid_b64s:
    n = len(valid_b64s)
    time_per_slide = 3.5 # Seconds each image is shown
    total_time = n * time_per_slide
    pct_visible = 100.0 / n
    fade_dur = 5.0 # Smoothness of fade

    # Generate CSS keyframes for 6 photos
    keyframes = f"""
    <style>
    @keyframes fadeAnim {{
        0% {{ opacity: 0; }}
        {fade_dur}% {{ opacity: 1; }}
        {pct_visible - fade_dur}% {{ opacity: 1; }}
        {pct_visible}% {{ opacity: 0; }}
        100% {{ opacity: 0; }}
    }}
    </style>
    """
    
    images_html = ""
    for i, (ext, b64) in enumerate(valid_b64s):
        delay = i * time_per_slide
        images_html += f'<img class="fade-img" src="data:image/{ext};base64,{b64}" style="animation: fadeAnim {total_time}s infinite {delay}s;" />'
    
    editorial_hero_html = f"""
    {keyframes}
    <div class="open-book-container">
        <div class="book-left-page">
            <div class="image-frame">
                {images_html}
            </div>
        </div>
        <div class="book-right-page">
            <h1 style="font-family: 'Inter', sans-serif; font-size: 4.5rem; font-weight: 800; color: #ffffff; letter-spacing: 2px; margin: 0 0 10px 0; line-height: 1; text-align: center;">AVIVA<br>CUI</h1>
            <p style="font-family: 'Inter', sans-serif; font-size: 1rem; color: #888888; letter-spacing: 4px; text-transform: uppercase; margin: 0;">Portfolio</p>
            <hr style="width: 40px; border-top: 2px solid #555555; margin-top: 30px;">
        </div>
    </div>
    """
    st.markdown(editorial_hero_html, unsafe_allow_html=True)
else:
    st.warning("Please ensure your hero images are uploaded to GitHub.")

st.markdown("---")

# --- ROLE 1: CHRISTCHURCH CITY COUNCIL ---
col_ccc_text, col_ccc_img = st.columns([1, 1], gap="large")

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

# --- ROLE 2: DIGITAL CONTENT CREATOR ---
col_dcc_img, col_dcc_text = st.columns([1, 1], gap="large")

with col_dcc_img:
    subcol3, subcol4, subcol5 = st.columns(3)
    with subcol3:
        st.image("IMG_9583.jpeg", use_container_width=True)
        st.markdown("<p style='font-size: 0.75rem; font-weight: 300; margin-top: 0px; text-align: center; color: #ffffff;'>Leapmotor High-Ticket</p>", unsafe_allow_html=True)
        st.link_button("VIEW POST", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")
        st.markdown("<p style='font-size: 0.6rem; color: #888888; text-align: center; margin-top: -5px;'>*Close login to view*</p>", unsafe_allow_html=True)
    
    with subcol4:
        st.image("IMG_9584.jpeg", use_container_width=True)
        st.markdown("<p style='font-size: 0.75rem; font-weight: 300; margin-top: 0px; text-align: center; color: #ffffff;'>New Zealand Residency</p>", unsafe_allow_html=True)
        st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
        st.markdown("<p style='font-size: 0.6rem; color: #888888; text-align: center; margin-top: -5px;'>*Close login to view*</p>", unsafe_allow_html=True)

    with subcol5:
        st.image("IMG_9586.jpeg", use_container_width=True)
        st.markdown("<p style='font-size: 0.75rem; font-weight: 300; margin-top: 0px; text-align: center; color: #ffffff;'>Radiance Collab</p>", unsafe_allow_html=True)
        st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
        st.markdown("<p style='font-size: 0.6rem; color: #888888; text-align: center; margin-top: -5px;'>*Close login to view*</p>", unsafe_allow_html=True)

with col_dcc_text:
    st.markdown("""
    <div style="margin-top: 1rem;">
        <div class='job-title'>Digital Content Creator</div>
        <div class='job-desc'>
        Outside of my professional roles, I build and manage a cross-cultural content platform on Xiaohongshu (RedNote) with 4,000+ followers and 140,000+ likes. I create short-form videos and livestream content that connect Chinese audiences with New Zealand culture, products, work life, and outdoor lifestyles.<br><br>
        I have collaborated with a range of New Zealand and international brands, including Radiance Collagen, Lorna Jane, Untouched World, Blackmores, Flavooo Protein, BioTrace, Partridge Jewellers, and Leapmotor. Through these collaborations, I have also begun supporting community engagement activities for Flavooo Protein.<br><br>
        Managing my own platform has strengthened my commercial awareness, content creation skills, audience engagement strategies, and understanding of emerging social media trends and algorithms. Please see examples of my content and brand collaborations from my account.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- ROLE 3: CIVIL DEFENCE ---
col_cd_text, col_cd_video = st.columns([1, 1], gap="large")

with col_cd_text:
    st.markdown("""
    <div style="margin-top: 1rem;">
        <div class='job-title'>Community Resilience Coordinator</div>
        <div class='job-desc'>
        I designed and delivered clear, accessible, and interactive community resilience programmes that translated complex emergency information into practical actions to strengthen emergency preparedness across diverse communities in Ōtautahi. My work also focused on building trusted partnerships with community leaders, organisations, and agencies through hui, events, workshops, and planning sessions to co-design community response plans and empower community resilience. See the preparedness video I was involved in for the Welcoming Package.<br><br>
        This experience strengthened my leadership, project coordination, and communication skills, requiring me to balance multiple responsibilities and stakeholders while working in complex and high-pressure environments.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_cd_video:
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p style="font-family: 'Inter', sans-serif; font-weight: 800; font-size: 1.5rem; margin-bottom: 15px; color: #ffffff; text-transform: uppercase; letter-spacing: -0.5px;">Let's build something beautiful together.</p>
    <p style="font-size: 0.85rem; font-weight: 500; color: #aaaaaa; text-transform: uppercase; letter-spacing: 1px;">
        cuiqiandl@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; 021 086 68972 &nbsp;&nbsp;|&nbsp;&nbsp; Ōtautahi Christchurch
    </p>
</div>
""", unsafe_allow_html=True)
