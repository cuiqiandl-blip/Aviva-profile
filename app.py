import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | ZURU Edge Application", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main .block-container { padding-top: 2rem; }
    div.stButton > button:first-child { background-color: #000000; color: white; border: 1px solid transparent; }
    div.stButton > button:hover { border: 1px solid #000000; background-color: white; color: #000000; }
    h1 { color: #111111; }
    h2 { color: #222222; border-bottom: 2px solid #f0f2f6; padding-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.title("Aviva Cui — Community Manager Portfolio")
st.subheader("Cultivating Authentic Communities & Data-Driven Growth")

st.markdown("""
> **The Pitch:** I bridge the gap between high-stakes stakeholder engagement and organic digital growth. 
> By leveraging audience psychology, cross-cultural consumer insights, and transparent storytelling, 
> I turn passive viewers into highly engaged, loyal brand communities.
""")

st.divider()

# --- SECTION 1: THE CONTENT STRATEGY ---
st.header("1. Core Case Studies: The Three Pillars of Community")
st.write("""
*A successful community strategy requires a balance of credibility, empathy, and commercial viability.* Here is how my content consistently hits all three marks on Xiaohongshu.
""")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🎙️ Organic Storytelling")
    st.markdown("""
    **Focus:** High-trust narrative building and deep community engagement.
    * **The Strategy:** Relatable, peer-level storytelling that drives intense audience empathy and organic shares.
    * **ZURU Value:** Proves an innate understanding of audience psychology and how to foster self-sustaining, interactive communities.
    """)
    st.link_button("View Post on Xiaohongshu ↗", "https://www.xiaohongshu.com/explore/69b39551000000001d01a139?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBQjm4fpq5mn1gNaXvSmqHEycceO2k-imt_Fbpuwvq6H8=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181402&share_id=53e9fd52d8c04b7dae101bdce8eb1d6d&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")

with col2:
    st.subheader("✨ FMCG Alignment: Wellness")
    st.markdown("""
    **Focus:** Seamless integration of health/wellness FMCG products (Radiance Collagen).
    * **The Strategy:** Integrating a brand's value proposition into my established lifestyle aesthetic without losing audience trust.
    * **ZURU Value:** Direct experience managing the exact product categories and target demographics relevant to ZURU Edge.
    """)
    st.link_button("View Radiance Collab ↗", "https://www.xiaohongshu.com/explore/6997fc1b000000000a03cdd9?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=video&xsec_token=CBgL-TXLpQOrDbz-8xDbRzFiDAhVtJE6woP0LxvZXLPPY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780181502&share_id=335f634135904b8d9cbae1b42238a444&wechatWid=435edd56e9ec82ab602023bc63e060ea&wechatOrigin=menu")

with col3:
    st.subheader("🚗 High-Ticket Partnerships")
    st.markdown("""
    **Focus:** Executing B2B brand alignment for high-value industries (Leapmotor).
    * **The Strategy:** Delivering high production value and clear commercial messaging for significant financial investments.
    * **ZURU Value:** Demonstrates versatility across verticals and the ability to manage strict corporate brand guidelines.
    """)
    st.link_button("View Leapmotor Collab ↗", "https://www.xiaohongshu.com/discovery/item/679b28f2000000002902bb7a?app_platform=ios&app_version=9.32.2&share_from_user_hidden=true&xsec_source=app_share&type=normal&xsec_token=CBmfg0EZN8pQGy56tj00S8Vk68ZE7QU07VM89gXHHbIjY=&author_share=1&xhsshare=WeixinSession&shareRedId=N0czNkc5Nj43OEdHOjgxSjkzQjxISzZC&apptime=1780306736&share_id=28fdb21358f64eaeb70787e4de81bf1e")

st.divider()

# --- SECTION 2: METRICS & CLOSED-LOOP FEEDBACK ---
st.header("2. Data Insights & Product Management Realities")

col4, col5 = st.columns([1, 1])

with col4:
    st.markdown("""
    ### Turning Feedback into Brand Strategy
    * **Analytical Rigor:** Experienced in tracking audience engagement metrics to continuously pivot communication strategies and maximize reach.
    * **Campaign Scaling:** Proven track record of executing targeted digital campaigns, delivering a **55% engagement boost**.
    * **Founder Mindset:** As a startup founder managing a consumer product brand, I handle the operational reality—from customer satisfaction to supply chains—giving me a comprehensive view of the FMCG lifecycle.
    """)

with col5:
    metrics_data = pd.DataFrame({
        'Content Category': ['Organic Storytelling', 'FMCG Collaborations (Collagen)', 'High-Ticket Collaborations (Auto)'],
        'Community Goal': ['Deep Trust & Empathy', 'Product Discovery & Conversion', 'Brand Awareness & Aspiration'],
        'Primary Action': ['High Comment Velocity', 'High Save/Share Rate', 'Link Clicks/Inquiries']
    })
    st.write("#### Platform Performance Breakdown")
    st.dataframe(metrics_data, hide_index=True, use_container_width=True)

st.divider()

# --- FOOTER ---
st.markdown("""
<div style="text-align: center; padding: 10px;">
    <strong>Let's Build Something Impactful Together</strong><br>
    📧 cuiqiandl@gmail.com | 📱 021 086 68972 | 📍 Ōtautahi Christchurch
</div>
""", unsafe_allow_html=True)
