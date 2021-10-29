import FWCore.ParameterSet.Config as cms

layerClusterAssociatorByEnergyScore = cms.EDProducer('LCToCPAssociatorByEnergyScoreProducer',
  hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
  hardScatterOnly = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
