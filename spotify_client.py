import os
import logging
from typing import List, Optional
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth


load_dotenv()


SCOPES = [
"user-read-playback-state",
"user-modify-playback-state",
"user-read-currently-playing",
"playlist-read-private",
"user-library-modify",
]


class SpotifyClient:
def __init__(self):
client_id = os.getenv("SPOTIPY_CLIENT_ID")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI", "http://localhost:8080/callback")
username = os.getenv("SPOTIFY_USERNAME", "default")
cache_path = f".cache-{username}"


if not client_id:
raise RuntimeError("SPOTIPY_CLIENT_ID not set. See README.")


self.oauth = SpotifyOAuth(
client_id=client_id,
client_secret=None, # PKCE (no secret)
redirect_uri=redirect_uri,
scope=" ".join(SCOPES),
cache_path=cache_path,
open_browser=True,
show_dialog=True,
requests_timeout=10,
)
self.sp = spotipy.Spotify(auth_manager=self.oauth)


# --- Devices ---
def _active_device_id(self) -> Optional[str]:
devices = self.sp.devices().get("devices", [])
for d in devices:
if d.get("is_active"):
return d.get("id")
return devices[0]["id"] if devices else None


def list_devices(self) -> List[str]:
devices = self.sp.devices().get("devices", [])
return [d.get("name") for d in devices]


def switch_device_by_name(self, name: str) -> bool:
devices = self.sp.devices().get("devices", [])
for d in devices:
if d.get("name", "").lower() == name.lower():
self.sp.transfer_playback(d["id"], force_play=False)
return True
return False


# --- Playback Controls ---
def pause(self):
did = self._active_device_id()
if did:
self.sp.pause_playback(device_id=did)


def resume(self):
did = self._active_device_id()
if did:
self.sp.start_playback(device_id=did)


def next(self):
return True