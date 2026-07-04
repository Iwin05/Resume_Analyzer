import streamlit as st

st.set_page_config(page_icon="📃",page_title="Resume ATS Analyzer",layout="wide")

st.title("📃 Resume ATS Analyzer")

st.write("Analyze your resume here and get feeback")

#file upload
upload_file = st.file_uploader("Upload your resume (PDF/DOCX)",type=["pdf","docx"])

#paste jd section
jd = st.text_area("Paste Job Description",height=200)

analyze_button = st.button("Analyze Resume")

#backend
from utils.parser import extract_text
from utils.preprocessing import preprocess_text
from utils.extractor import extract_keywords
from utils.matcher import match_keywords
from utils.scorer import calculate_score, score_label
from utils.feedback import generate_feedback

if analyze_button:

    if upload_file is None or jd.strip() == "":
        st.warning("Please upload a resume and enter job description")
    
    else:
        resume_text = extract_text(upload_file,upload_file.name)

        resume_clean = preprocess_text(resume_text)
        jd_clean = preprocess_text(jd)

        resume_keywords = extract_keywords(resume_clean)
        jd_keywords = extract_keywords(jd_clean)

        match_result = match_keywords(resume_keywords,jd_keywords)

        score = calculate_score(match_result)
        label = score_label(score)

        feedback_result = generate_feedback(match_result,score)

        st.subheader("📊 Score : ")
        st.progress(int(score))
        st.write(f"Score : {score}% ({label})")
        
        st.subheader("🖋️ Feedback : ")
        for f in feedback_result["feedback"]:
            st.write(f"- {f}")
        
        st.subheader("💪 Strenght : ")
        for s in feedback_result["strength"]:
            st.write(f"- {s}")
            
        st.subheader("🚀 Suggestions : ")
        for s in feedback_result["suggestions"]:
            st.write(f"- {s}")
            
        st.subheader("✨ Note : ")
        for i in feedback_result["inspire"]:
            st.write(f"- {i}")

