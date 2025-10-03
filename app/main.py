from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

GITHUB_API = "https://api.github.com/users/{username}/gists"

@app.get("/users/{username}")
def get_user_gists(username: str):
    response = requests.get(GITHUB_API.format(username=username))
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Error fetching gists")

    gists = response.json()
    return {
        "user": username,
        "gists": [
            {"id": g["id"], "description": g["description"], "url": g["html_url"]}
            for g in gists
        ]
    }
