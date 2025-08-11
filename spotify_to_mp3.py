import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yt_dlp
from mutagen.easyid3 import EasyID3
import re
from pathlib import Path
import time

# Load credentials from .env
load_dotenv()
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

def sanitize_filename(s):
    return re.sub(r'[\\/:"*?<>|]+', '', s)

def get_spotify_client():
    return spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-read-private"
    ))

def get_playlist_tracks(sp, playlist_id):
    tracks = []
    results = sp.playlist_tracks(playlist_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks

def download_song(query, output_dir):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{query}"])

def main():
    playlist_url = input("Enter Spotify playlist URL: ").strip()
    sp = get_spotify_client()
    playlist = sp.playlist(playlist_url)
    playlist_name = sanitize_filename(playlist['name'])
    output_dir = Path(playlist_name)
    output_dir.mkdir(exist_ok=True)
    tracks = get_playlist_tracks(sp, playlist_url)

    print(f"Found {len(tracks)} tracks in '{playlist_name}'")
    for idx, item in enumerate(tracks, start=1):
        track = item['track']
        name = track['name']
        artist = track['artists'][0]['name']
        query = f"{name} {artist}"
        print(f"[{idx}/{len(tracks)}] Downloading {query}...")
        download_song(query, output_dir)
        time.sleep(1)  # avoid hitting YouTube rate limit

if __name__ == "__main__":
    main()
