# ATS-resume-guider
An AI-powered ATS Resume Guider built with Streamlit and Google Gemini. It analyzes resumes against job descriptions, provides professional evaluation, match percentage, missing keywords, skill improvement suggestions, and recommends perfect real-world projects to boost hiring chances.
<img width="1859" height="865" alt="Screenshot 2025-10-29 164935" src="https://github.com/user-attachments/assets/59bfd6fb-012e-4880-828d-8e6e506b70d1" />
<img width="1878" height="900" alt="Screenshot 2025-10-29 164947" src="https://github.com/user-attachments/assets/e9c7ab59-d01f-4486-b699-701b1ccbebf2" />
<img width="1783" height="792" alt="Screenshot 2025-10-29 165103" src="https://github.com/user-attachments/assets/0e796594-4282-48e4-82d3-804e4e66b5af" />
<img width="1808" height="348" alt="Screenshot 2025-10-29 165116" src="https://github.com/user-attachments/assets/bcf29c4c-2d13-44b1-8395-1b3b60c21139" />
# 🧠 ATS Resume Guider

An **AI-powered Resume Evaluation System** built using **Google Gemini API** and **Streamlit**.  
It helps candidates and recruiters assess how well a resume matches a given job description — and even suggests **skills to improve**, **missing keywords**, and **ideal real-world projects** to strengthen the candidate’s portfolio.

## 🚀 Features
✅ Resume Evaluation – Get an expert-style HR review of your resume.  
✅ ATS Score Calculation – See how closely your resume matches the job description (in %).  
✅ Skill Gap Analysis – Identify missing keywords and technical skills.  
✅ Improvement Suggestions – Get personalized advice on tools, skills, and learning paths.  
✅ Project Recommendations – Discover practical project ideas that fit your target job.

## 🧩 Tech Stack
- Python 3.10+
- Streamlit – For interactive web app UI
- Google Generative AI (Gemini API) – For AI evaluation and content generation
- pdf2image – To convert PDF resumes into images for Gemini Vision
- Pillow (PIL) – Image processing
- Base64 / io – Data encoding and file handling

## ⚙️ Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ats-resume-guider.git
   cd ats-resume-guider
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your Google API key:**
   Create a `.env` file in the root directory:
   ```
   GOOGLE_API_KEY=your_google_api_key_here
   ```

5. **Install Poppler (for PDF to image conversion):**
   - **Windows:** Download from https://github.com/oschwartz10612/poppler-windows/releases  
     and add the `bin` folder path (e.g., `C:\path\to\poppler\Library\bin`) to your system **PATH**.
   - **macOS/Linux:**
     ```bash
     brew install poppler    # macOS
     sudo apt install poppler-utils  # Ubuntu/Debian
     ```

## ▶️ Run the App
```bash
streamlit run app.py
```

(Replace `app.py` with your actual file name if different.)

## 🧠 Prompts Used
- **Evaluation Prompt:** For detailed HR-style resume review.
- **Improvement Prompt:** For skill and learning recommendations.
- **ATS Match Prompt:** For percentage and missing keyword detection.
- **Project Prompt:** For recommending real-world projects aligned with the job role.

## 💡 Future Enhancements
- Multi-page resume support  
- Automatic resume parsing for text extraction  
- Job description scraping from LinkedIn  
- Export results as PDF reports


