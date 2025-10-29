from dotenv import load_dotenv
load_dotenv()
import os
import io
import base64
import streamlit as st
from PIL import Image
import pdf2image
import google.generativeai as genai

API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="ATS Resume Guider", layout="wide")
st.title("ATS Resume Guider")

def get_gemini_response(prompt, pdf_parts, job_description):
    model = genai.GenerativeModel("gemini-2.5-flash")
    content = [prompt] + pdf_parts + [job_description]
    response = model.generate_content(content)
    return response.text

@st.cache_data
def input_pdf_setup(uploaded_file):
    if uploaded_file is None:
        raise FileNotFoundError("No file uploaded")
    images = pdf2image.convert_from_bytes(
        uploaded_file.read(),
        poppler_path=r"C:\Users\user\Downloads\Release-25.07.0-0\poppler-25.07.0\Library\bin"
    )
    pdf_parts = []
    for page in images:
        img_byte_arr = io.BytesIO()
        page.save(img_byte_arr, format="JPEG")
        img_bytes = img_byte_arr.getvalue()
        pdf_parts.append({"mime_type": "image/jpeg", "data": base64.b64encode(img_bytes).decode()})
    return pdf_parts

input_text = st.text_area("Job Description:", key="job_desc")
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
if uploaded_file is not None:
    st.write("PDF uploaded successfully")

col1, col2, col3, col4 = st.columns(4)
with col1:
    submit1 = st.button("Tell me about this resume")
with col2:
    submit2 = st.button("How can I improve my skills")
with col3:
    submit3 = st.button("Percentage match")
with col4:
    submit4 = st.button("Perfect Projects for This Job")

input_prompt1 = """
You are an experienced HR professional with hands-on technical expertise in AI Engineering, Agentic AI Systems, Data Science, Full Stack Web Development, Big Data Engineering, DevOps, and Data Analytics. Since you come from these technical fields yourself, you understand the skills, tools, and mindset required for success in such roles. Review the provided resume (image/PDF) against the given job description and provide a professional evaluation describing alignment with the role, highlighting strengths, technical depth, and areas needing improvement to excel in AI-driven and DevOps-focused environments.
"""

input_prompt2 = """
You are an AI career advisor with deep knowledge of AI Engineering, Agentic AI, Data Science, DevOps, Big Data, and Full-Stack development. Analyze the resume and job description and provide the top 5 actionable skill improvements, concrete learning resources or tools to learn, practical projects to build, and a recommended timeline to increase employability for these roles.
"""

input_prompt3 = """
You are an expert ATS evaluator. Analyze the resume against the provided job description and return: (1) a single overall match percentage score between 0 and 100, (2) a short explanation of the score, and (3) a bullet list of important keywords/skills present in the job description but missing from the resume.
"""

input_prompt4 = """
You are an expert AI career coach specializing in project-based learning for AI Engineers, Data Scientists, DevOps Engineers, and Full Stack Developers. 
Based on the provided resume and job description, suggest 3 to 5 real-world project ideas that would perfectly match the job role and strengthen the candidate’s portfolio.
For each project, include:
1. A creative project title.
2. Short one-line description.
3. Technologies and tools to use.
4. Which skill or job requirement it strengthens.
"""

if submit1 or submit2 or submit3 or submit4:
    if not API_KEY:
        st.error("GOOGLE_API_KEY not set in environment.")
    elif uploaded_file is None:
        st.error("Please upload a resume PDF first.")
    elif not input_text or input_text.strip() == "":
        st.error("Please paste the job description in the text area.")
    else:
        try:
            with st.spinner("Processing..."):
                pdf_parts = input_pdf_setup(uploaded_file)
                if submit1:
                    resp = get_gemini_response(input_prompt1, pdf_parts, input_text)
                    st.subheader("Evaluation:")
                    st.write(resp)
                elif submit2:
                    resp = get_gemini_response(input_prompt2, pdf_parts, input_text)
                    st.subheader("Improvement Suggestions:")
                    st.write(resp)
                elif submit3:
                    resp = get_gemini_response(input_prompt3, pdf_parts, input_text)
                    st.subheader("Match Analysis:")
                    st.write(resp)
                elif submit4:
                    resp = get_gemini_response(input_prompt4, pdf_parts, input_text)
                    st.subheader("Perfect Project Recommendations:")
                    st.write(resp)
        except Exception as e:
            st.error(f"Error: {e}")
