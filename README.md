# Spotify-Playlist-Downloader
### Spotify Playlist to MP3 Downloader 🎵

A Python script that fetches songs from a **Spotify playlist** using the Spotify Web API, searches for them on **YouTube**, downloads the audio as MP3 using `yt-dlp`, and saves them with proper naming.

---

## 📌 Features
- Fetch all songs from any **Spotify playlist** (public or private with auth).
- Search YouTube for each song and download the best quality audio.
- Save files as **MP3 (192kbps)** with cleaned file names.
- Automatically create a folder for the playlist.

---

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
Downloading copyrighted content without permission is illegal in many countries.  
Use it only for **personal, non-commercial purposes** and ensure you have the rights to the content.

---

## 📂 Project Structure
```spotify_youtube_downloader/
│
├── spotify_to_mp3.py # Main script
├── .env # API keys (DO NOT share)
├── requirements.txt # Dependencies ( pip install spotipy yt-dlp mutagen python-dotenv )
└── README.md # Documentation ( Not Neccessary in directory but refer this for execution instructions)
```
---

## 🔑 Prerequisites
1. **Python** 3.8 or higher
2. **Spotify Developer Account**:  
   - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
   - Create a new app.
   - Set **Redirect URI** to:  
     ```
     http://127.0.0.1:8888/callback
     ```
   - Get **Client ID** and **Client Secret**.
3. **.env file** (create in the same directory as `spotify_to_mp3.py`):
   ```.env
   SPOTIPY_CLIENT_ID=your_client_id_here
   SPOTIPY_CLIENT_SECRET=your_client_secret_here
   SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback
   ```

---

## 1. Clone the repository
git clone https://github.com/yourusername/spotify-youtube-downloader.git
cd spotify-youtube-downloader

## 2. Install dependencies
pip install -r requirements.txt


---

▶️ Usage
Run the script:


```python spotify_to_mp3.py```


