import sys
import logging
from src.voice_io import VoiceIO
from src.commands import IntentParser
from src.spotify_client import SpotifyClient


logging.basicConfig(
level=logging.INFO,
format="[%(levelname)s] %(message)s"
)


class MusicAssistant:
def __init__(self):
self.voice = VoiceIO()
self.parser = IntentParser()
self.spotify = SpotifyClient()


def run(self):
self.voice.say("Spotify voice assistant ready. Press Enter and speak a command. Say 'quit' to exit.")
try:
while True:
input("") # push-to-talk
text = self.voice.listen()
if not text:
self.voice.say("Sorry, I didn't catch that.")
continue


logging.info(f"Heard: {text}")
if text.lower().strip() in {"quit", "exit", "stop"}:
self.voice.say("Goodbye!")
break


intent = self.parser.parse(text)
if not intent:
self.voice.say("I couldn't understand that command.")
continue


try:
self._execute_intent(intent)
except Exception as e:
logging.exception(e)
self.voice.say("I hit an error executing that command.")
except KeyboardInterrupt:
self.voice.say("Goodbye!")
sys.exit(0)


# --- Intent Execution ---
def _execute_intent(self, intent):
name = intent.name
p = intent.params


if name == "play_track":
ok = self.spotify.play_track(query=p.get("track"), artist=p.get("artist"))
self.voice.say("Playing" + (f" {p['track']}" if p.get('track') else "") + (f" by {p['artist']}" if p.get('artist') else "") if ok else "Couldn't play that.")
elif name == "play_album":
ok = self.spotify.play_album(p["album"]) if p.get("album") else False
self.voice.say("Playing album." if ok else "Couldn't find that album.")
elif name == "play_playlist":
ok = self.spotify.play_playlist(p["playlist"]) if p.get("playlist") else False
self.voice.say("Playing playlist." if ok else "Couldn't find that playlist.")
elif name == "pause":
self.spotify.pause()
self.voice.say("Paused.")
elif name == "resume":
self.spotify.resume()
self.voice.say("Resumed.")
elif name == "next":
self.spotify.next()
self.voice.say("Skipping.")
elif name == "previous":
self.voice.say("Command not implemented.")