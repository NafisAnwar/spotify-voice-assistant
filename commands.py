import sys
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
self.spotify.previous()
self.voice.say("Previous track.")
elif name == "volume_up":
v = self.spotify.change_volume(+10)
self.voice.say(f"Volume {v}%.")
elif name == "volume_down":
v = self.spotify.change_volume(-10)
self.voice.say(f"Volume {v}%.")
elif name == "set_volume":
v = int(p.get("level", 50))
v = self.spotify.set_volume(v)
self.voice.say(f"Volume {v}%.")
elif name == "shuffle":
on = p.get("state", True)
self.spotify.set_shuffle(on)
self.voice.say("Shuffle on." if on else "Shuffle off.")
elif name == "repeat":
on = p.get("state", True)
self.spotify.set_repeat(on)
self.voice.say("Repeat on." if on else "Repeat off.")
elif name == "what_song":
info = self.spotify.current_track_info()
if info:
self.voice.say(f"This is {info['name']} by {info['artist']} on {info['album']}.")
else:
self.voice.say("No track is currently playing.")
elif name == "save_track":
ok = self.spotify.save_current_track()
self.voice.say("Saved." if ok else "Couldn't save the current track.")
elif name == "list_devices":
names = self.spotify.list_devices()
if names:
self.voice.say("Available devices: " + ", ".join(names))
else:
self.voice.say("No devices found. Open Spotify on one of your devices.")
elif name == "switch_device":
target = p.get("device")
ok = self.spotify.switch_device_by_name(target) if target else False
self.voice.say(f"Switched to {target}." if ok else "Couldn't switch device.")
else:
self.voice.say("Command not implemented.")