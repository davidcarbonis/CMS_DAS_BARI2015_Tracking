from DataFormats.FWLite import Handle, Events
import ROOT
events = Events("tracks_and_vertices.root")
tracks = Handle("std::vector<reco::Track>")

from math import sqrt

p_histogram = ROOT.TH1F("", "", 100, 0.0, 5.0)

i = 0
events.toBegin()
for event in events:
    print "Event", i
    event.getByLabel("globalMuons", tracks)
    if tracks.product().size() == 2:

   		one = tracks.product()[0]
    		two = tracks.product()[1]

		total_energy = sqrt(0.140**2 + one.p()**2) + sqrt(0.140**2 + two.p()**2)
		total_px = one.px() + two.px()
		total_py = one.py() + two.py()
		total_pz = one.pz() + two.pz()
		mass = sqrt(total_energy**2 - total_px**2 - total_py**2 - total_pz**2)
		p_histogram.Fill(mass)		
    i += 1

c = ROOT.TCanvas ( "c" , "c" , 800, 800 )
c.cd()
p_histogram.Draw()
c.Print("p_histogram.png")
