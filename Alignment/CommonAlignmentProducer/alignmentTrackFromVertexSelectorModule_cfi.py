import FWCore.ParameterSet.Config as cms

alignmentTrackFromVertexSelectorModule = cms.EDFilter('AlignmentTrackFromVertexSelectorModule',
  src = cms.InputTag('generalTracks'),
  filter = cms.bool(False),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  leptonTracks = cms.InputTag('ALCARECOTkAlDiMuon'),
  useClosestVertexToDilepton = cms.bool(False),
  vertexIndex = cms.uint32(0),
  mightGet = cms.optional.untracked.vstring
)