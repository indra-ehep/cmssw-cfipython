import FWCore.ParameterSet.Config as cms

pixelTrackDumpCUDA = cms.EDAnalyzer('PixelTrackDumpCUDA',
  onGPU = cms.bool(True),
  pixelTrackSrc = cms.InputTag('caHitNtupletCUDA'),
  pixelVertexSrc = cms.InputTag('pixelVertexCUDA'),
  mightGet = cms.optional.untracked.vstring
)
