import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(page_title="Aviva Cui | ZURU Edge Application", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS FOR BRANDING ---
st.markdown("""
    <style>
    .main .block-container { padding-top: 2rem; }
    div.stButton > button:first-child { background-color: #000000; color: white; }
    h1 { color: #111111; }
    h2 { color: #222222; border-bottom: 2px solid #f0f2f6; padding-bottom: 10px; }
    </style>
    """, unsafe_html=True)

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
st.header("1. Core Case Studies: Organic Trust vs. Sponsored Reach")
st.write("""
*True community management relies on emotional equity.* While I successfully collaborate with commercial brands, 
my highest-performing content leverages authentic narrative hooks that drive deep community trust, saves, and active discussions.
""")

col1, col2 = st.columns(2)

with col1:
    st.subheader("🎙️ Case Study A: Authority & Complex Storytelling")
    # Replace with your video filename if local (e.g., "book_video.mp4") or a URL
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
    st.markdown("""
    **Focus:** Translating my published research and academic milestones into highly engaging short-form digital content.
    * **The Strategy:** Distilling dense, high-level themes into sharp, accessible video hooks.
    * **Community Metric:** Exceptional save-to-view ratio and long-term authority building.
    * **ZURU Value:** Demonstrates the ability to command attention, establish brand credibility, and clearly communicate complex concepts.
    """)

with col2:
    st.subheader("🌱 Case Study B: Vulnerability & Peer-to-Peer Trust")
    # Replace with your video filename if local (e.g., "residency_video.mp4") or a URL
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") 
    st.markdown("""
    **Focus:** Documenting the real, transparent journey of navigating complex residency transitions.
    * **The Strategy:** Relatable, peer-level storytelling that encourages viewers to participate directly in the comments section.
    * **Community Metric:** High comment velocity, intense audience empathy, and organic shares.
    * **ZURU Value:** Proves an innate understanding of audience psychology and how to foster self-sustaining, interactive communities.
    """)

st.divider()

# --- SECTION 2: METRICS & CLOSED-LOOP FEEDBACK ---
st.header("2. Data Insights & Product Management Realities")

col3, col4 = st.columns([1, 1])

with col3:
    st.markdown("""
    ### Turning Feedback into Brand Strategy
    * **Analytical Rigor:** Experienced in tracking audience engagement metrics to continuously pivot communication strategies and maximize reach.
    * **Campaign Scaling:** Proven track record of executing targeted digital campaigns, delivering a **55% engagement boost**.
    * **Founder Mindset:** As a startup founder managing a consumer product brand, I handle the operational reality—from customer satisfaction to supply chains—giving me a comprehensive view of the FMCG lifecycle.
    """)

with col4:
    # Quick comparative dataframe to visually back up your point
    metrics_data = pd.DataFrame({
        'Content Category': ['Organic Storytelling (Residency/Book)', 'Standard Brand Collaborations'],
        'Avg. Comment Velocity': ['Very High (Community-Led)', 'Moderate (Inquiry-Led)'],
        'Save & Share Rate': ['15% - 20%', '3% - 5%'],
        'Primary Audience Action': ['Community building & Peer Support', 'Product Discovery']
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
""", unsafe_html=True)
