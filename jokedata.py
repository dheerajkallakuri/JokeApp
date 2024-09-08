import requests
url="https://v2.jokeapi.dev/joke/Any"
def fetch_joke():
    response=requests.get(url)
    if response.status_code == 200:
        jokeData=response.json()
        return jokeData