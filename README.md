# AI-Powered Music Voice Assistant (Spotify + Voice)


Control Spotify with your voice. Uses Google Speech Recognition (free tier) for ASR and `pyttsx3` for offline text‑to‑speech.


## Features
- Play/pause/resume/next/previous
- "Play *<song>* by *<artist>*"; "Play album *<name>*"; "Play playlist *<name>*"
- Device control: "switch to device *<name>*"
- Volume control: "volume up/down", "set volume to *<0-100>*"
- Shuffle/repeat: "shuffle on/off", "repeat on/off"
- Track info: "what song is this?"
- Library action: "like/save this song"


## Requirements
- Python 3.10+
- Spotify Premium account
- An active Spotify device (desktop, phone, or web player)
- Microphone connected to your computer


## Install
```bash
# 1) Clone repo and enter it
pip install -U pip
python -m venv .venv && . .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt