import FWCore.ParameterSet.Config as cms

siPixelCondObjForHLTReader = cms.EDAnalyzer('SiPixelCondObjForHLTReader',
  useSimRcd = cms.bool(False),
  maxRangeDeadPixHist = cms.untracked.double(0.001),
  mightGet = cms.optional.untracked.vstring
)