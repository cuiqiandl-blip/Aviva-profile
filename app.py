import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | Portfolio", layout="centered", initial_sidebar_state="collapsed")

# --- PREMIUM EDITORIAL CSS ---
st.markdown("""
    <style>
    /* Import elegant Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap');

    /* Global styling for stark, clean look */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #ffffff;
        color: #111111;
    }
    
    /* Elegant Serif Headers */
    h1, h2, h3, h4 {
        font-family: 'Playfair Display', serif;
        color: #000000 !important;
        font-weight: 400;
        letter-spacing: 0.5px;
    }
    
    /* Center and narrow the main content column to read like an editorial article */
    .main .block-container {
        padding-top: 4rem !important;
        padding-bottom: 4rem !important;
        max-width: 800px; 
    }
    
    /* Hide all standard Streamlit branding */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    
    /* Minimalist sharp lines */
    hr {
        border-top: 1px solid #eeeeee;
        margin-top: 3rem;
        margin-bottom: 3rem;
    }
    
    /* Sharp, high-fashion style buttons */
    div.stButton > button:first-child {
        background-color: transparent;
        color: #000000;
        border: 1px solid #000000;
        border-radius: 0px;
        font-family: 'Inter', sans-serif;
        text-transform: uppercase;
        font-size: 0.75rem;
        letter-spacing: 1px;
        padding: 0.5rem 1rem;
    }
    div.stButton > button:hover {
        background-color: #000000;
        color: #ffffff;
        border: 1px solid #000000;
    }
    
    /* Style markdown links to look clean */
    a {
        color: #000000 !important;
        text-decoration: underline;
        text-underline-offset: 4px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("Aviva Cui.")
st.markdown("<p style='font-size: 1.2rem; font-weight: 300; color: #555555;'>Cultivating Authentic Communities & Data-Driven Growth.</p>", unsafe_allow_html=True)

st.markdown("""
I bridge the gap between high-stakes stakeholder engagement and organic digital growth. 
By leveraging audience psychology, cross-cultural consumer insights, and transparent storytelling, 
I turn passive viewers into highly engaged, loyal brand communities.
""")

st.markdown("---")

# --- SECTION 1: THE CONTENT STRATEGY ---
st.header("The Three Pillars of Community.")
st.markdown("""
<p style='font-size: 0.9rem; color: #555555;'>
A successful community strategy requires a balance of credibility, empathy, and commercial viability. 
Here is how my content consistently hits all three marks.
</p>
""", unsafe_allow_html=True)
st.write("") # Spacer

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### I. Authority")
    st.markdown("""
    **Organic Storytelling**
    Translating published research into engaging short-form content. Distilling dense themes into sharp video hooks.
    """)
    st.link_button("View Post", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.7rem; color: #888888; margin-top: -10px;'>*If prompted, click the red button on XHS to view.*</p>", unsafe_allow_html=True)

with col2:
    st.markdown("### II. Empathy")
    st.markdown("""
    **FMCG Alignment**
    Seamless integration of health & wellness products (Radiance Collagen) without losing audience trust.
    """)
    st.link_button("View Post", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")
    st.markdown("<p style='font-size: 0.7rem; color: #888888; margin-top: -10px;'>*If prompted, click the red button on XHS to view.*</p>", unsafe_allow_html=True)

with col3:
    st.markdown("### III. Reach")
    st.markdown("""
    **High-Ticket Partnerships**
    Executing B2B brand alignment for high-value industries (Leapmotor). Delivering clear commercial messaging.
    """)
    st.link_button("View Post", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")
    st.markdown("<p style='font-size: 0.7rem; color: #888888; margin-top: -10px;'>*Opens directly in web viewer.*</p>", unsafe_allow_html=True)

st.markdown("---")

# --- SECTION 2: METRICS & CLOSED-LOOP FEEDBACK ---
st.header("Data Insights & Operational Reality.")

st.markdown("""
**Turning Feedback into Brand Strategy**
*   **Analytical Rigor:** Experienced in tracking audience engagement metrics to continuously pivot communication strategies and maximize reach.
*   **Campaign Scaling:** Proven track record of executing targeted digital campaigns, delivering a **55% engagement boost**.
*   **Founder Mindset:** As a startup founder managing a consumer product brand, I handle the operational reality—from customer satisfaction to supply chains—giving me a comprehensive view of the FMCG lifecycle.
""")

st.write("") # Spacer

# Minimalist custom table
metrics_html = """
<table style="width:100%; text-align:left; border-collapse: collapse; font-size: 0.9rem;">
  <tr style="border-bottom: 1px solid #000;">
    <th style="padding: 10px 0;">Content Category</th>
    <th style="padding: 10px 0;">Community Goal</th>
    <th style="padding: 10px 0;">Primary Action</th>
  </tr>
  <tr style="border-bottom: 1px solid #eee;">
    <td style="padding: 10px 0;">Organic Storytelling</td>
    <td style="padding: 10px 0;">Deep Trust & Empathy</td>
    <td style="padding: 10px 0;">High Comment Velocity</td>
  </tr>
  <tr style="border-bottom: 1px solid #eee;">
    <td style="padding: 10px 0;">FMCG Collabs (Collagen)</td>
    <td style="padding: 10px 0;">Product Discovery</td>
    <td style="padding: 10px 0;">High Save/Share Rate</td>
  </tr>
  <tr>
    <td style="padding: 10px 0;">High-Ticket (Auto)</td>
    <td style="padding: 10px 0;">Brand Awareness</td>
    <td style="padding: 10px 0;">Link Clicks/Inquiries</td>
  </tr>
</table>
"""
st.markdown(metrics_html, unsafe_allow_html=True)

st.markdown("---")

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p style="font-family: 'Playfair Display', serif; font-size: 1.5rem; margin-bottom: 5px;">Let's build something impactful together.</p>
    <p style="font-size: 0.85rem; color: #555555;">cuiqiandl@gmail.com &nbsp;&nbsp;|&nbsp;&nbsp; 021 086 68972 &nbsp;&nbsp;|&nbsp;&nbsp; Ōtautahi Christchurch</p>
</div>
""", unsafe_allow_html=True)
