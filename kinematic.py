from DataFormats.FWLite import Handle, Events
import ROOT
events = Events("tracks_and_vertices.root")
tracks = Handle("std::vector<reco::Track>")

i = 0
for event in events:
    event.getByLabel("generalTracks", tracks)
    numTotal = tracks.product().size()
    numLoose = 0
    numTight = 0
    numHighPurity = 0
    for track in tracks.product():
        print track.pt(), track.p(), track.px(), track.py(), track.pz()
    i = i + 1
    if i > 100: break
