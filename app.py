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
        max-width: 1100px; 
    }
    
    /* Hide standard Streamlit branding */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* MASSIVE breathing room between sections */
    hr {
        border-top: 1px solid #333333;
        margin-top: 6rem;
        margin-bottom: 6rem;
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
        margin-top: 15px;
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
    
    /* Image subtle zoom */
    [data-testid="stImage"] img {
        transition: transform 0.3s ease;
    }
    [data-testid="stImage"] img:hover {
        transform: scale(1.02);
    }
    .stImage {
        margin-bottom: 0.5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAME HEADER & CONTACT INFO (TOP) ---
st.markdown("""
<div style="position: relative; width: 100%; padding-top: 2rem;">
    <div style="position: absolute; top: 0; left: 0; text-align: left; font-family: 'Inter', sans-serif; font-size: 0.85rem; font-weight: 500; color: #aaaaaa; letter-spacing: 1px; line-height: 1.6;">
        cuiqiandl@gmail.com<br>02108668972
    </div>
    <h1 style="font-family: 'Inter', sans-serif; font-size: 5rem; font-weight: 800; color: #ffffff; letter-spacing: 4px; text-align: center; margin-bottom: 1rem; line-height: 1;">AVIVA CUI</h1>
</div>
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


# --- EDITORIAL TYPOGRAPHY HERO ("A JOURNAL ON" STYLE) ---
st.markdown("""
<div style="width: 100%; max-width: 900px; margin: 8rem auto 8rem auto; padding: 0 20px;">
    <h2 style="font-family: 'Inter', sans-serif; font-size: 4rem; font-weight: 800; color: #ffffff; letter-spacing: -2px; line-height: 1.1; margin-bottom: 2rem;">
        I want you to have all of the nice things and experiences that you deserve.
    </h2>
    <p style="font-family: 'Inter', sans-serif; font-size: 1.3rem; font-weight: 300; color: #888888; letter-spacing: 1px; margin: 0;">
        Let me help you.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- ROLE 1: CHRISTCHURCH CITY COUNCIL ---
st.markdown("<div class='job-title'>Engagement - Christchurch City Council</div>", unsafe_allow_html=True)

# ROW 1: IMAGES (Wrapped in spacers to make them smaller and add negative space)
spacer_left, col1, col2, spacer_right = st.columns([1.5, 2, 2, 1.5], gap="large")
with col1:
    st.image("Image_20260602213535_35_1.jpg", use_container_width=True)
    st.link_button("VIEW REEL 1", "https://www.instagram.com/reel/CqbP8tLvxkX/?igsh=MzU0cTF0MzV2amR1")
with col2:
    st.image("Image_20260602214021_36_1.jpg", use_container_width=True)
    st.link_button("VIEW REEL 2", "https://www.instagram.com/reel/Cpo0bQNvE91/?igsh=MWVqM2VyNTBkaGMxYg==")

# ROW 2: TEXT
st.markdown("""
<div style="margin-top: 3.5rem;">
    <div class='job-desc'>
    Christchurch is undergoing significant infrastructure upgrades and investment in new community facilities. While these projects deliver long-term benefits, they can also create disruption for residents, businesses, and road users during construction. My role is to help bridge the gap between project teams and communities by planning and delivering strategic engagement, providing clear and authentic communications, and ensuring stakeholder concerns and feedback are understood and addressed throughout the project lifecycle.<br><br>
    A core part of this is managing public enquiries, ensuring every community member feels heard and respected. Even when an issue falls outside my direct scope, I take ownership of the query, coordinating with internal teams to ensure the resident receives a clear response and a tangible solution. To see this approach in action, take a look at the Reels I created for the Welcome Back to the Ōtākaro Avon River Corridor campaign above.<br><br>
    This role has strengthened my ability to engage diverse audiences, balance competing perspectives, and deliver positive community experiences across projects including the Lincoln Road Wastewater and Road Upgrade, Central City Coach Tour Bus Parking, and the Halswell Junction Road cul-de-sac renaming project.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- ROLE 2: DIGITAL CONTENT CREATOR ---
st.markdown("<div class='job-title'>Digital Content Creator</div>", unsafe_allow_html=True)

# ROW 1: IMAGES (Wrapped in spacers to squeeze them into magazine-style thumbnails)
spacer_left2, col3, col4, col5, spacer_right2 = st.columns([0.8, 1.5, 1.5, 1.5, 0.8], gap="medium")
with col3:
    st.image("IMG_9583.jpeg", use_container_width=True)
    st.markdown("<p style='font-size: 0.75rem; font-weight: 300; margin-top: 0px; text-align: center; color: #ffffff;'>Your new vehicle choice - Leapmotor C10</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")
    st.markdown("<p style='font-size: 0.6rem; color: #888888; text-align: center; margin-top: -5px;'>*When the login window appears, close it and click the first post.*</p>", unsafe_allow_html=True)
with col4:
    st.image("IMG_9584.jpeg", use_container_width=True)
    st.markdown("<p style='font-size: 0.75rem; font-weight: 300; margin-top: 0px; text-align: center; color: #ffffff;'>I got New Zealand residency! How to get it</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.6rem; color: #888888; text-align: center; margin-top: -5px;'>*When the login window appears, close it and click the first post.*</p>", unsafe_allow_html=True)
with col5:
    st.image("IMG_9586.jpeg", use_container_width=True)
    st.markdown("<p style='font-size: 0.75rem; font-weight: 300; margin-top: 0px; text-align: center; color: #ffffff;'>Radiance Collagen is the essence of your day</p>", unsafe_allow_html=True)
    st.link_button("VIEW POST", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.6rem; color: #888888; text-align: center; margin-top: -5px;'>*When the login window appears, close it and click the first post.*</p>", unsafe_allow_html=True)

# ROW 2: TEXT
st.markdown("""
<div style="margin-top: 3.5rem;">
    <div class='job-desc'>
    Outside of my government roles, I have built and managed a cross-cultural digital platform on Xiaohongshu (RedNote), growing a highly engaged community with over 4,000 followers and 140,000+ likes. By creating authentic short-form video and livestream content, I connect Chinese audiences with New Zealand’s culture, lifestyle, and premium products.<br><br>
    This platform operates as a fully functioning digital business. I pitch, negotiate, and execute brand collaborations with major New Zealand and international companies, including Radiance Collagen, Lorna Jane, Untouched World, Blackmores, BioTrace, Partridge Jewellers, and Leapmotor. I also leverage this audience to drive community engagement and brand growth for Flavooo Protein.<br><br>
    Running this channel has sharpened my commercial acumen, storytelling capabilities, and ability to read social algorithms—proving I can build deep audience trust and translate that attention into measurable brand impact.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- ROLE 3: CIVIL DEFENCE ---
st.markdown("<div class='job-title'>Community Resilience Coordinator</div>", unsafe_allow_html=True)

# ROW 1: VIDEO (Wrapped in massive spacers to make it smaller)
spacer_vid1, col_vid, spacer_vid2 = st.columns([1.5, 2, 1.5]) 
with col_vid:
    st.video("https://youtu.be/-5L7fV-XE00?si=92H8znN8mAvgQznN")

# ROW 2: TEXT
st.markdown("""
<div style="margin-top: 3.5rem;">
    <div class='job-desc'>
    Effective emergency management relies on communities being prepared, informed, and connected before a crisis hits. In this role, I designed and delivered interactive resilience programmes across Ōtautahi, ensuring diverse communities had the tools and knowledge to protect themselves during high-stakes events.<br><br>
    My focus was on building deep, trusted partnerships with local leaders, organisations, and response agencies. Through hui, workshops, and planning sessions, we co-designed community response plans that translated complex, bureaucratic emergency procedures into clear, actionable, and culturally responsive steps. To see how we communicated this to new residents, take a look at the preparedness video I helped produce for the Welcoming Package above.<br><br>
    Operating in a complex, high-pressure emergency management environment sharpened my project coordination and stakeholder management skills. It taught me how to lead with empathy, align multiple agencies, and empower communities to take ownership of their own resilience.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<div style="width: 100%; max-width: 900px; margin: 4rem auto 8rem auto; padding: 0 20px; text-align: center;">
    <h2 style="font-family: 'Inter', sans-serif; font-size: 4rem; font-weight: 800; color: #ffffff; letter-spacing: -2px; line-height: 1.1; margin-bottom: 0;">
        Let's build something beautiful together.
    </h2>
</div>
""", unsafe_allow_html=True)
