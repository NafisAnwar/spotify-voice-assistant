# Spotify Voice Assistant (Speech → Spotify)

Control Spotify with your voice. Say commands like “play blinding lights by the weeknd”, “pause”, “next”, “shuffle on”, “save this song”, or “switch to device living room tv”. Uses Google Speech Recognition for ASR and `pyttsx3` for local text‑to‑speech.


> **Requires:** Spotify Premium and an **active device** signed into the same account (desktop, mobile, or web player).


## ✨ Features
- Play/pause/next/previous
- Play songs, artists, albums, or playlists by name
- Volume control (up/down or exact value 0–100)
- Shuffle & repeat toggles
- “What song is this?” track info
- Save (like) current track
- List/switch Spotify devices


## 🧩 Tech Stack
- **Python 3.10+**
- **Spotify Web API** via `spotipy` (OAuth PKCE; no client secret)
- **SpeechRecognition** (Google Web Speech API)
- **PyAudio** (mic capture)
- **pyttsx3** (offline TTS)
- **dotenv** for env config


## 📦 Install
```bash
git clone https://github.com/your-username/spotify-voice-assistant.git
cd spotify-voice-assistant
python -m venv .venv && . .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
