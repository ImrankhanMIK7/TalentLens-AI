import streamlit as st

from resume_parser import extract_text
from skill_matcher import (
    extract_skills,
    calculate_score
)

st.set_page_config(
    page_title="TalentLens AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 TalentLens AI")
st.subheader("AI-Powered Resume ATS Optimizer")

st.write(
    "Upload your resume and compare it "
    "against real-world Data Analyst job market demand."
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text(uploaded_file)

    skills = extract_skills(text)

    score, matched, missing = calculate_score(skills)

    st.metric(
        "ATS Score",
        f"{score}%"
    )

    st.progress(score / 100)

    col1, col2 = st.columns(2)

    with col1:

        st.success("Matched Skills")

        for skill in sorted(matched):
            st.write(f"✅ {skill.title()}")

    with col2:

        st.error("Missing Skills")

        for skill in sorted(missing):
            st.write(f"❌ {skill.title()}")

    st.divider()

    # -----------------------------
    # Resume Statistics
    # -----------------------------

    st.subheader("📊 Resume Statistics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Skills Found",
            len(matched)
        )

    with c2:
        st.metric(
            "Missing Skills",
            len(missing)
        )

    with c3:
        st.metric(
            "Market Skills",
            len(matched) + len(missing)
        )

    st.divider()

    # -----------------------------
    # Resume Summary
    # -----------------------------

    st.subheader("📈 Resume Summary")

    st.write(f"**Skills Found:** {len(matched)}")
    st.write(f"**Skills Missing:** {len(missing)}")

    if score >= 80:
        st.success(
            "Excellent resume alignment with market demand."
        )
        st.balloons()

    elif score >= 60:
        st.warning(
            "Good profile. Adding a few skills could improve your ATS score."
        )

    else:
        st.error(
            "Resume requires improvement to match current market trends."
        )

    st.divider()

    # -----------------------------
    # Top Recommendations
    # -----------------------------

    st.subheader("🎯 Top Recommendations")

    recommendations = list(sorted(missing))[:5]

    for item in recommendations:
        st.write(f"• {item.title()}")

    st.divider()

    # -----------------------------
    # Resume Preview
    # -----------------------------

    with st.expander("📄 Resume Text Preview"):
        st.text(text[:3000])
    st.subheader("🎯 Top Recommendations")

    recommendations = list(sorted(missing))[:5]

    for item in recommendations:
        st.write(f"• {item.title()}")

    