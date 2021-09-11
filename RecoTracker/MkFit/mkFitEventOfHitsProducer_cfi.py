import FWCore.ParameterSet.Config as cms

mkFitEventOfHitsProducer = cms.EDProducer('MkFitEventOfHitsProducer',
  pixelHits = cms.InputTag('mkFitSiPixelHits'),
  stripHits = cms.InputTag('mkFitSiStripHits'),
  usePixelQualityDB = cms.bool(True),
  useStripStripQualityDB = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
