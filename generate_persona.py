# import praw
# from config import client_id, client_secret, user_agent
# from urllib.parse import urlparse
# import openai
# from openai import OpenAI
# from config import openrouter_api_key
# import os

# openai.api_key = openrouter_api_key
# openai.api_base = "https://openrouter.ai/api/v1"



# def build_prompt(username, posts, comments):
#     content = f"Reddit profile: u/{username}\n\n"

#     content += "=== POSTS ===\n"
#     for post in posts:
#         content += f"Title: {post['title']}\nText: {post['text']}\nURL: {post['url']}\n\n"

#     content += "=== COMMENTS ===\n"
#     for comment in comments:
#         content += f"{comment['body']}\nURL: {comment['url']}\n\n"

#     prompt = f"""
# You are an expert analyst tasked with building a user persona.

# Based on the Reddit posts and comments below from u/{username}, generate a detailed persona. Include:

# - Interests
# - Tone & Writing Style
# - Goals & Needs
# - Behavior & Habits
# - Frustrations
# - Personality traits (MBTI if guessable)
# - Motivations (in bullet or table format)
# - Include **citations** (quote and link) after each trait.

# Structure it in clear text. Keep the tone human-readable.

# {content}
# """

#     return prompt


# def generate_persona_with_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
#     try:
#         response = openai.ChatCompletion.create(
#             model=model,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.7
#         )
#         return response['choices'][0]['message']['content']
#     except Exception as e:
#         print(f"LLM generation error: {e}")
#         return None


# def save_persona(username, persona_text):
#     path = os.path.join("users", f"{username}_persona.txt")
#     with open(path, "w", encoding="utf-8") as f:
#         f.write(persona_text)
#     print(f"\n✅ Persona saved to: {path}")

# def extract_username_from_url(profile_url):
#     """
#     Extracts 'u/username' from Reddit profile URL.
#     Ex: https://www.reddit.com/user/kojied → kojied
#     """
#     return profile_url.rstrip("/").split("/")[-1]


# def fetch_user_data(username):
#     """
#     Fetch latest 50 posts and comments from a Reddit user.
#     Returns: (list_of_posts, list_of_comments)
#     """
#     reddit = praw.Reddit(client_id=client_id,
#                          client_secret=client_secret,
#                          user_agent=user_agent)

#     user = reddit.redditor(username)

#     posts = []
#     comments = []

#     try:
#         for submission in user.submissions.new(limit=50):
#             posts.append({
#                 'title': submission.title,
#                 'text': submission.selftext,
#                 'url': f"https://www.reddit.com{submission.permalink}"
#             })

#         for comment in user.comments.new(limit=50):
#             comments.append({
#                 'body': comment.body,
#                 'url': f"https://www.reddit.com{comment.permalink}"
#             })

#     except Exception as e:
#         print(f"Error fetching data: {e}")

#     return posts, comments


# def test_openrouter_connection():
#     from openai import OpenAI
#     from config import openrouter_api_key

#     client = OpenAI(
#         api_key=openrouter_api_key,
#         base_url="https://openrouter.ai/api/v1"
#     )

#     response = client.chat.completions.create(
#         model="mistralai/mistral-7b-instruct",
#         messages=[{"role": "user", "content": "Say hello!"}],
#         temperature=0.7
#     )

#     print("✅ OpenRouter LLM Response:", response.choices[0].message.content)


# Call this at the bottom:
# test_openrouter_connection()



# if __name__ == "__main__":
#     profile_url = input("Enter Reddit profile URL: ").strip()
#     username = extract_username_from_url(profile_url)
#     print(f"\nFetching data for user: {username}...\n")

#     posts, comments = fetch_user_data(username)

#     if not posts and not comments:
#         print("❌ No data found.")
#         exit()

#     print("🧠 Generating prompt...")
#     prompt = build_prompt(username, posts, comments)

#     print("⚡ Sending to LLM...")
#     persona = generate_persona_with_openrouter(prompt)

#     if persona:
#         save_persona(username, persona)
#     else:
#         print("❌ Persona generation failed.")



import os
import openai
import praw
from config import (
    client_id,
    client_secret,
    user_agent,
    openrouter_api_key
)

# Set up OpenRouter (through OpenAI's new SDK)
from openai import OpenAI
client = OpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1"
)

# Extract Reddit username from URL
def extract_username_from_url(profile_url):
    return profile_url.rstrip("/").split("/")[-1]

# Fetch Reddit posts and comments using PRAW
def fetch_user_data(username):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    user = reddit.redditor(username)

    posts = []
    comments = []

    try:
        for submission in user.submissions.new(limit=50):
            posts.append({
                'title': submission.title,
                'text': submission.selftext,
                'url': f"https://www.reddit.com{submission.permalink}"
            })

        for comment in user.comments.new(limit=50):
            comments.append({
                'body': comment.body,
                'url': f"https://www.reddit.com{comment.permalink}"
            })

    except Exception as e:
        print(f"❌ Error fetching Reddit data: {e}")

    return posts, comments

# Build the prompt for OpenRouter LLM
def build_prompt(username, posts, comments):
    content = f"Reddit profile: u/{username}\n\n"

    content += "=== POSTS ===\n"
    for post in posts:
        content += f"Title: {post['title']}\nText: {post['text']}\nURL: {post['url']}\n\n"

    content += "=== COMMENTS ===\n"
    for comment in comments:
        content += f"{comment['body']}\nURL: {comment['url']}\n\n"

        prompt = f"""
You are an expert behavior analyst.

Based on Reddit posts and comments from user u/{username}, generate a detailed, professional user persona.

You MUST include direct **quotes** and **Reddit links** as **evidence** for every key trait, frustration, behavior, and motivation. The persona should be grounded in Reddit content only — avoid speculation.

Please include these sections, each backed by one or more quotes and links:

---

User Persona for u/{username}

Age (estimated):  
Occupation (if inferable):  
Status (e.g. Single, Student, Married):  
Location (if mentioned):  
Tier: Beginner / Enthusiast / Expert  
Archetype: (e.g. The Analyst, The Creator, The Explorer)  
Personality Traits: Practical, Curious, Sarcastic, etc. — each with 1 quote and link

---

Motivations  
What drives this user? Each motivation must include a quote and Reddit link showing intent, desire, or drive.

---

Personality  
Describe emotional and cognitive traits. Use at least one comment or post that reflects their personality — with quote and link.

---

Tone and Communication Style  
Describe how they express themselves. Provide 1–2 quotes and link(s) that support this analysis.

---

Behavior and Habits  
- Subreddits they post in  
- Post/comment style  
- Active hours (if inferable)  
- Interaction behavior  
Each pattern should be backed by a real example and link.

---

Frustrations  
List 2–5 things the user dislikes. For each, give a quote and Reddit link where they express that frustration.

---

Goals and Needs  
What are they trying to achieve on Reddit or in life? Show quotes that prove what matters to them.

---

External Links (Optional)  
List GitHub, blog, portfolio, or image links if the user shares them in any post or comment.

---

Ensure the final persona is written in clear text and saved as a plain .txt file. Do not hallucinate information. Every claim must be backed by Reddit content from u/{username} below.

Here is the Reddit data:
{content}
"""




    return prompt

# Send the prompt to OpenRouter
def generate_persona_with_openrouter(prompt, model="mistralai/mistral-7b-instruct"):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ LLM generation error: {e}")
        return None

# Save output to users/username_persona.txt
def save_persona(username, persona_text):
    os.makedirs("users", exist_ok=True)
    file_path = os.path.join("users", f"{username}_persona.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(persona_text)
    print(f"\n✅ Persona saved to: {file_path}")

# Main execution
if __name__ == "__main__":
    profile_url = input("Enter Reddit profile URL: ").strip()
    username = extract_username_from_url(profile_url)

    print(f"\n🔍 Fetching data for user: {username}...\n")
    posts, comments = fetch_user_data(username)

    if not posts and not comments:
        print("❌ No data found. Exiting.")
        exit()

    print("🧠 Building prompt...")
    prompt = build_prompt(username, posts, comments)

    print("⚡ Generating persona via OpenRouter LLM...")
    persona = generate_persona_with_openrouter(prompt)

    if persona:
        save_persona(username, persona)
    else:
        print("❌ Persona generation failed.")
