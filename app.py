import streamlit as st

# Page config
st.set_page_config(page_title="🩺 Smart Medical Assistant", layout="centered")

# Header image or emoji
st.markdown("<h1 style='text-align: center;'>🧬 Smart Medical Assistant</h1>", unsafe_allow_html=True)
st.image("https://cdn.pixabay.com/photo/2017/08/06/09/49/doctor-2596210_960_720.jpg", use_column_width=True)

# Patient details
with st.expander("👤 Patient Info", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Patient Name")
    with col2:
        age = st.number_input("Age", min_value=0, max_value=120, step=1)

# Symptom selection with columns
st.subheader("🩺 Select Symptoms:")
col1, col2 = st.columns(2)

with col1:
    fever = st.checkbox("🌡️ Fever")
    cough = st.checkbox("😷 Cough")
    sore_throat = st.checkbox("🤒 Sore Throat")
    headache = st.checkbox("🤕 Headache")
    chills = st.checkbox("🥶 Chills or Shivering")

with col2:
    fatigue = st.checkbox("💤 Fatigue")
    body_pain = st.checkbox("🦴 Body Pain")
    runny_nose = st.checkbox("🤧 Runny Nose")
    shortness_breath = st.checkbox("😮‍💨 Shortness of Breath")
    loss_taste = st.checkbox("👅 Loss of Taste/Smell")

# Diagnose button
if st.button("🔍 Diagnose Now"):
    st.subheader("📋 Result")

    # Rule-based logic
    if fever and cough and sore_throat and loss_taste:
        diagnosis = "🦠 Likely COVID-19"
        emoji = "😷"
        color = "red"
    elif fever and body_pain and chills:
        diagnosis = "🦟 Possible Dengue or Viral Fever"
        emoji = "🤒"
        color = "orange"
    elif runny_nose and sore_throat and cough:
        diagnosis = "🤧 Common Cold"
        emoji = "🤧"
        color = "green"
    elif headache and fatigue:
        diagnosis = "💤 Could be Migraine or Fatigue"
        emoji = "😴"
        color = "blue"
    elif fever and shortness_breath:
        diagnosis = "⚠️ Possible Respiratory Infection"
        emoji = "😤"
        color = "darkred"
    else:
        diagnosis = "🔍 No clear diagnosis. Please consult a doctor."
        emoji = "🩺"
        color = "gray"

    st.markdown(
        f"""
        <div style='
            padding: 20px;
            border-radius: 10px;
            background-color: {color};
            color: white;
            text-align: center;
            font-size: 22px;'>
            {emoji} <b>Diagnosis:</b> {diagnosis}
        </div>
        """, unsafe_allow_html=True)

    # Patient summary
    st.markdown("### 📝 Patient Summary:")
    st.write(f"**Name**: {name or 'N/A'}")
    st.write(f"**Age**: {age} years")
    st.write(f"**Symptoms selected**: {[s for s, checked in zip(['Fever','Cough','Sore Throat','Headache','Chills','Fatigue','Body Pain','Runny Nose','Shortness of Breath','Loss of Taste/Smell'], [fever, cough, sore_throat, headache, chills, fatigue, body_pain, runny_nose, shortness_breath, loss_taste]) if checked] or ['None']}")

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>👩‍⚕️ Created by Niranjan • Powered by AI • Not a substitute for medical advice</p>", unsafe_allow_html=True)
