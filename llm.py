# llm.py
import requests, os

def call_llm(prompt, model="sonar-pro"):
    r = requests.post(
        "https://api.perplexity.ai/chat/completions",
        headers={
            "Authorization": f"Bearer {os.getenv('PERPLEXITY_API_KEY')}",
            "Content-Type": "application/json"
        },
        json={
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a presentation intelligence agent."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
