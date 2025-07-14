
# Reddit Persona Generator – BeyondChats Internship Assignment

This project was developed as part of the **Generative AI Internship Assignment for BeyondChats**.

It accepts a Reddit user profile URL, scrapes the user's latest posts and comments using the Reddit API, and then uses a hosted open-source LLM (Mistral 7B via OpenRouter) to generate a detailed user persona. Each insight is supported by quotes and links to the user's Reddit activity. The output is saved as a clean, human-readable `.txt` file.

---

## 🚀 Features

- ✅ Scrapes Reddit posts and comments using the Reddit API (PRAW)
- ✅ Uses hosted open-source LLMs (Mistral via OpenRouter)
- ✅ Generates a structured `.txt` persona
- ✅ Includes Reddit quote + link for every insight (citation)
- ✅ Requires no GPU or local LLM installation
- ✅ Complies with all instructions from the assignment PDF

---

## 📁 Project Structure

```
reddit-persona-generator/
├── generate_persona.py        # Main script
├── config.py                  # API keys (excluded via .gitignore)
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Ignores .venv, config.py, pycache
└── users/
    └── kojied_persona.txt     # Sample persona output
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pranavp00/reddit-persona-generator.git
cd reddit-persona-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `config.py` with Your API Keys

```python
# config.py

openrouter_api_key = "sk-..."  # Get from https://openrouter.ai/keys
client_id = "..."              # Reddit API client_id
client_secret = "..."          # Reddit API client_secret
user_agent = "reddit_persona_app by u/yourusername"
```

> ⚠️ Make sure `config.py` is included in `.gitignore` and not pushed to GitHub.

---

## 🧪 How to Use

Run the script:

```bash
python generate_persona.py
```

You will be prompted to enter a Reddit profile URL, such as:

```
https://www.reddit.com/user/kojied/
```

The script will scrape data and generate the persona, saved here:

```
users/kojied_persona.txt
```

---

## 📄 Sample Output

A sample output is included in:

```
users/kojied_persona.txt
```

Each section (e.g., Personality, Behavior, Frustrations) includes direct quotes and Reddit links to support the analysis.

---

## 🧠 Technologies Used

- Python 3
- [PRAW](https://praw.readthedocs.io/) – Reddit API wrapper
- [OpenRouter](https://openrouter.ai) – Hosted LLMs (Mistral 7B)
- [Mistral-7B Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)

---

## ✅ Assignment Goals Met

- [x] Accepts Reddit profile URL
- [x] Scrapes posts and comments
- [x] Builds a detailed user persona
- [x] Backs every claim with quotes and Reddit links
- [x] Outputs clean, structured `.txt` file
- [x] Uses hosted open-source LLM (no GPU/local install required)

---

## 🙋‍♂️ Author

**Pranav Pillai**  
GitHub: [@pranavp00](https://github.com/pranavp00)  
LinkedIn: [linkedin.com/in/pranavpillai](https://www.linkedin.com/in/pranavpillai/)

---

## 🔐 Disclaimer

This repository is part of the BeyondChats internship submission.  
All data used is publicly available on Reddit.  
This project is not intended for commercial or production use unless selected.
