from app.models.event import *

event1 = Event("23/09/20", "CodeClan W3D3", 25, "Castle Terrace", "CSS")
event2 = Event("24/09/20", "CodeClan W3D4", 25, "Castle Terrace", "Flask")

events = [event1, event2]

def add_new_event(event):
    events.append(event)

