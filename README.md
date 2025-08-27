# 📚 Bookstore-QA  

Bookstore-QA is a simple project that demonstrates how to generate synthetic bookstore data, query it using natural language, and process queries via the **Groq API**.  

---

## 🚀 Setup Instructions  

### 1. Clone the Repository
```bash
git clone <your_repo_url>
cd bookstore-qa
```

### 2. Create a Virtual Environment
```bash
# Linux / Mac
python -m venv .venv
source .venv/bin/activate  

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables  
Set your **Groq API Key**:  

```bash
# Linux / Mac
export GROQ_API_KEY="your_key_here"

# Windows (Command Prompt)
set GROQ_API_KEY=your_key_here

# Windows (PowerShell)
$env:GROQ_API_KEY="your_key_here"
```

---

## 📊 Generate Synthetic Data
Create sample CSVs for the bookstore schema:  
```bash
python src/generate_data.py
```

---

## 💡 Run Queries
Once the data is generated, you can run queries using:  
```bash
python src/query_runner.py
```

---

## 📂 Project Structure
```
bookstore-qa/
|── data/
│── src/
│   ├── generate_data.py      # Generate synthetic CSV bookstore data
│   ├── query_runner.py       # Run queries using Groq API
│── README.md                 # Documentation
```

---

## 📝 Notes
- Ensure you have a valid **Groq API key** before running queries.  
- The synthetic CSV data will be generated inside the project folder.  
- This project is meant for demonstration and experimentation purposes.  

---
