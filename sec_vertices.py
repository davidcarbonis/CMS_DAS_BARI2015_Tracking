from DataFormats.FWLite import Handle, Events, ROOT
events = Events("output.root")
secondaryVertices = Handle("std::vector<reco::VertexCompositeCandidate>")

i = 0
events.toBegin()
for event in events:
    print "Event:", i
    event.getByLabel("SecondaryVerticesFromHighPurityTracks", "Kshort", secondaryVertices)
    j = 0
    for vertex in secondaryVertices.product():
        print "    Vertex:", j, vertex.vx(), vertex.vy(), vertex.vz()
        j += 1
    i += 1

mass_histogram = ROOT.TH1F("mass", "mass", 100, 0.4, 0.6)
events.toBegin()
for event in events:
    event.getByLabel("SecondaryVerticesFromLooseTracks", "Kshort", secondaryVertices)
    for vertex in secondaryVertices.product():
        mass_histogram.Fill(vertex.mass())

mass_histogram.Draw()
