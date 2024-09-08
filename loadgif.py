import requests
import random

def fetch_laugh(api_key, save_path='laughing_gif.gif', limit=100):
    # Giphy API endpoint for search
    url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q=laughing&limit={limit}&rating=g"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data['data']:
            random_gif = random.choice(data['data'])
            gif_url = random_gif['images']['original']['url']
            print(f"Downloading GIF from: {gif_url}")

            gif_response = requests.get(gif_url)

            if gif_response.status_code == 200:
                with open(save_path, 'wb') as f:
                    f.write(gif_response.content)
                print(f"GIF successfully downloaded and saved as {save_path}")
            else:
                print(f"Failed to download GIF. Status code: {gif_response.status_code}")
    else:
        print(f"Failed to fetch GIFs. Status code: {response.status_code}")

