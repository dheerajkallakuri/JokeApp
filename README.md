# Joke App

## Description

Joke App is a fun application that fetches jokes from an API and displays them on a GUI. It supports two types of jokes: single-part and two-part jokes. The app also reads the jokes aloud using a text-to-speech (TTS) library. For two-part jokes, the app switches between different accents for each part. At the end of each joke, the app fetches and displays a random laughing GIF from an API. The TTS functionality is handled with timers and threading to ensure smooth and real-time playback.

<img width="622" alt="res" src="https://github.com/user-attachments/assets/67ed5cb7-0343-4397-8a69-cf9b9bcc7972">


## Features

- **Two Types of Jokes**: Fetches and displays single-part or two-part jokes.
- **Text-to-Speech (TTS)**: Reads jokes aloud, using different accents for two-part jokes.
- **GIF Integration**: Displays a random laughing GIF after the joke, fetched from the Giphy API.
- **Accents**: TTS supports 5 accents: American, Australian, British, Canadian, and Indian.
- **Real-time Audio and Visual Sync**: The joke is read aloud in sync with the text on the screen using threading and a timer mechanism.

## File Structure

### `app.py`
This is the main GUI file of the application. It handles:
- Displaying the joke on the screen.
- Showing the random GIF after the joke.
- A button labeled "Tell me a joke!" that fetches a new joke and reads it aloud.

### `loadgif.py`
Handles the API call to Giphy. It fetches a random laughing GIF using a keyword ("laughing") from the Giphy API. You will need to generate an API key from the Giphy website to use this.

### `tts_world.py`
This file handles the text-to-speech conversion. It:
- Select a random accent from 5 predefined accents (American, Australian, British, Canadian, Indian).
- Converts the joke text to an MP3 file.
- Plays the MP3 file and deletes it after playback.

### `jokedata.py`
Fetches a random joke from the open-source [JokeAPI](https://v2.jokeapi.dev/joke/Any). This API provides both single-part and two-part jokes.

## Requirements

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/dheerajkallakuri/JokeApp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd JokeApp
   ```
3. Run the app:
   ```bash
   python app.py
   ```

4. Click the **Tell me a joke!** button to fetch, display, and hear a random joke, along with a laughing GIF.

## Learnings & Takeaways

This app demonstrates how to handle:
- Multiple API calls (for jokes and GIFs).
- Synchronizing text-to-speech with the visual display of the joke.
- Managing TTS conversion with multiple accents.
- Threading and timers are used to ensure seamless synchronization between audio playback and the text displayed on the screen.
