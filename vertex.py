from math import sqrt
from DataFormats.FWLite import Handle, Events
import ROOT

events = Events("tracks_and_vertices.root")
primaryVertices = Handle("std::vector<reco::Vertex>")


rho_z_histogram = ROOT.TH2F("rho_z", "rho_z", 100, 0, 30, 100, 0, 10)
events.toBegin()
for event in events:
    event.getByLabel("offlinePrimaryVertices", primaryVertices)
    for vertex in primaryVertices.product():
        rho_z_histogram.Fill(abs(vertex.z()), sqrt(vertex.x()**2 + vertex.y()**2))
c = ROOT.TCanvas ( "c" , "c" , 800, 800 )
c.cd()
rho_z_histogram.Draw()
c.Print("rho_z.png")

input("Press Enter to continue...")

deltaz_histogram = ROOT.TH1F("deltaz", "deltaz", 1000, -20, 20)

events.toBegin()
for event in events:
    event.getByLabel("offlinePrimaryVertices", primaryVertices)
    pv = primaryVertices.product()
    for i in xrange(0, pv.size()):
        for j in xrange(i + 1, pv.size()):
            deltaz_histogram.Fill(pv[i].z() - pv[j].z())
c = ROOT.TCanvas ( "c" , "c" , 800, 800 )
c.cd()
deltaz_histogram.Draw()
c.Print("deltaz.png")

