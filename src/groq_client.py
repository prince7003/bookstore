import os
from groq import Groq

# client = Groq(api_key=os.getenv("GROQ_API_KEY")) #please put your groq api key here
client = Groq(api_key="") #please put your groq api key here

def ask_groq(system_prompt, user_query, model="llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
        temperature=0
    )
    return response.choices[0].message.content.strip()