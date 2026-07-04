
# 📃 Resume ATS Analyzer

a simple NLP based tool that analyze your Resume against the Job Description and 
provides match scores, feedback, and improvement suggestions


## 💻 Tech Stack

- Python
- spaCy (for NLP)
- PyPDF2
- Python-docx

you can check the requirements.txt file for all the tools and required versions

## ⚙️ Run Locally

Clone the project

```bash
  git clone https://github.com/your-username/resume-ats-analyzer.git
```

Go to the project directory

```bash
  cd resume-ats-analyzer
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Download spaCy model

```bash
  python -m spacy download en_core_web_sm
```

Start the server

```bash
  streamlit run app.py
```


## 🧑‍💻 Working

- Upload your resume (PDF/DOCX)
- Paste the job description
- Click **Analyze**
- Get:
   1. Match Score
   2. Missing Skills
   3. Strengths
   4. Suggestions

## ⚠️ Limitations

- Keyword-based matching (basic NLP)
- Extraction accuracy depends on resume format
## 🚀 Improvements

- Semantic matching using embeddings
- AI-generated personalized suggestions
- Better skill or keyword extraction 
- Export results as PDF


## ⭐ Acknowledgements

Built as a hands-on NLP project to understand how ATS systems work.
