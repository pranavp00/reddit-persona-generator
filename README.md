Reddit Persona Generator – BeyondChats Internship Assignment

This project was built as part of the Generative AI Internship Assignment for BeyondChats.

It takes a Reddit user profile URL as input, scrapes the user's latest posts and comments using the Reddit API, and then generates a detailed user persona using a hosted open-source LLM via OpenRouter (Mistral-7B). The output is saved as a plain .txt file with clear citations (quotes and links) supporting each insight.

------------------------------------------------------------

FEATURES

- Scrapes Reddit user posts and comments using the Reddit API (PRAW)
- Uses hosted open-source LLMs (Mistral via OpenRouter)
- Generates a clean, structured persona in .txt format
- Includes quote + link citations for every major insight
- Complies with all assignment requirements

------------------------------------------------------------

FOLDER STRUCTURE

reddit-persona-generator/
├── generate_persona.py        → Main script
├── config.py                  → API keys (excluded from Git)
├── requirements.txt           → Python dependencies
├── README.txt                 → This file
├── .gitignore                 → Ignores config, .venv, pycache
└── users/
    └── kojied_persona.txt     → Sample output

------------------------------------------------------------

SETUP INSTRUCTIONS

1. Clone the repository

    git clone https://github.com/pranavp00/reddit-persona-generator.git
    cd reddit-persona-generator

2. Install Python packages

    pip install -r requirements.txt

3. Create your config.py file

    # config.py

    openrouter_api_key = "sk-..."  # Get from https://openrouter.ai/keys
    client_id = "..."              # Reddit API client_id
    client_secret = "..."          # Reddit API client_secret
    user_agent = "reddit_persona_app by u/yourusername"

------------------------------------------------------------

USAGE

Run:

    python generate_persona.py

You will be prompted to enter a Reddit profile URL like:

    https://www.reddit.com/user/kojied/

The output will be saved in:

    users/kojied_persona.txt

------------------------------------------------------------

EXAMPLE OUTPUT

A sample persona file is included:

    users/kojied_persona.txt

Each section (e.g., personality, motivations, frustrations) includes direct quotes and Reddit post links to support the analysis.

------------------------------------------------------------

TECHNOLOGIES USED

- Python 3
- PRAW – Reddit API wrapper
- OpenRouter.ai – Hosted open-source LLM platform
- Mistral-7B Instruct – Used via OpenRouter API

------------------------------------------------------------

ASSIGNMENT GOALS MET

- Takes Reddit profile URL as input
- Scrapes posts and comments using Reddit API
- Generates detailed user persona
- Includes quote + link citations for every insight
- Saves persona as plain .txt file
- Uses hosted open-source LLM (no local model required)

------------------------------------------------------------

AUTHOR

Pranav Pillai  
GitHub: https://github.com/pranavp00  
LinkedIn: https://www.linkedin.com/in/pranavpillai/

------------------------------------------------------------

DISCLAIMER

This project is a submission for the BeyondChats internship assignment.  
All insights are generated based on publicly available Reddit data.  
This repository is not intended for commercial use unless selected.
