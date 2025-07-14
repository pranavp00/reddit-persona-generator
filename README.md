====================================================================
REDDET PERSONA GENERATOR – BEYONDCHATS INTERNSHIP ASSIGNMENT
====================================================================

This project was developed as part of the Generative AI Internship 
Assignment for BeyondChats.

It accepts a Reddit user profile URL, scrapes the user's recent 
posts and comments using the Reddit API, and uses a hosted 
open-source LLM (via OpenRouter) to generate a detailed persona. 
Each insight is supported by quotes and links to the user's Reddit 
activity. The output is saved as a plain .txt file.

====================================================================
FEATURES
====================================================================

- Scrapes Reddit user posts and comments using the Reddit API (PRAW)
- Uses hosted open-source LLMs (Mistral 7B via OpenRouter)
- Generates clean, structured user personas in .txt format
- Includes citations for every major insight (quote + Reddit link)
- Complies with all assignment requirements

====================================================================
PROJECT STRUCTURE
====================================================================

reddit-persona-generator/
├── generate_persona.py        → Main script
├── config.py                  → API keys (excluded from Git)
├── requirements.txt           → Python dependencies
├── README.txt                 → This file
├── .gitignore                 → Ignores config.py, .venv, pycache
└── users/
    └── kojied_persona.txt     → Sample persona output

====================================================================
SETUP INSTRUCTIONS
====================================================================

1. Clone the repository:

   git clone https://github.com/pranavp00/reddit-persona-generator.git
   cd reddit-persona-generator

2. Install dependencies:

   pip install -r requirements.txt

3. Create a config.py file and add your API keys:

   # config.py
   openrouter_api_key = "sk-..."  # Get from https://openrouter.ai/keys
   client_id = "..."              # Reddit API client_id
   client_secret = "..."          # Reddit API client_secret
   user_agent = "reddit_persona_app by u/yourusername"

====================================================================
USAGE
====================================================================

To generate a persona, run:

   python generate_persona.py

When prompted, enter a Reddit profile URL like:

   https://www.reddit.com/user/kojied/

The persona will be saved as a plain text file:

   users/kojied_persona.txt

====================================================================
SAMPLE OUTPUT
====================================================================

A sample persona file is included:

   users/kojied_persona.txt

Each section of the persona includes insights derived from the 
user’s Reddit content, supported by direct quotes and Reddit links 
(as required by the assignment).

====================================================================
TECHNOLOGIES USED
====================================================================

- Python 3
- PRAW (Python Reddit API Wrapper)
- OpenRouter.ai (Hosted LLMs)
- Mistral-7B Instruct (Open-source LLM via OpenRouter API)

====================================================================
ASSIGNMENT REQUIREMENTS MET
====================================================================

✓ Accepts Reddit profile URL as input  
✓ Scrapes posts and comments using Reddit API  
✓ Builds a structured user persona  
✓ Backs each insight with quote + Reddit link  
✓ Saves output in plain .txt file  
✓ Uses hosted open-source LLM (no local model required)

====================================================================
AUTHOR
====================================================================

Pranav Pillai  
GitHub:   https://github.com/pranavp00  
LinkedIn: https://www.linkedin.com/in/pranavpillai/

====================================================================
DISCLAIMER
====================================================================

This project was created as a submission for the BeyondChats 
internship assignment.  
All insights are based on publicly available Reddit data.  
This project is not intended for production use unless selected.
