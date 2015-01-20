import FWCore.ParameterSet.Config as cms

process = cms.Process("RUN")

process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring("file://tracks_and_vertices.root"))
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(5))

process.MessageLogger = cms.Service("MessageLogger",
    destinations = cms.untracked.vstring("cout"),
    cout = cms.untracked.PSet(threshold = cms.untracked.string("ERROR")))

process.PrintOutTracks = cms.EDAnalyzer("PrintOutTracks")

process.path = cms.Path(process.PrintOutTracks)

