from DataFormats.FWLite import Handle, Events
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
        if track.quality(track.qualityByName("loose")): numLoose += 1
        if track.quality(track.qualityByName("tight")): numTight += 1
        if track.quality(track.qualityByName("highPurity")): numHighPurity += 1
    print "numTotal", numTotal, "numLoose", numLoose, "numTight", numTight, "numHighPurity", numHighPurity 
    i += 1
    if i > 100: break

import ROOT
histogram = ROOT.TH1F("histogram", "histogram", 100, 0, 10)
i = 0
for event in events:
    event.getByLabel("generalTracks", tracks)
    for track in tracks.product():
        histogram.Fill(track.normalizedChi2())
    i += 1
    if i > 1000: break
c = ROOT.TCanvas ( "c" , "c" , 800, 800 )
c.cd()
histogram.Draw()

