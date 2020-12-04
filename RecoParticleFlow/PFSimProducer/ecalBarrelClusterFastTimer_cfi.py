import FWCore.ParameterSet.Config as cms

ecalBarrelClusterFastTimer = cms.EDProducer('EcalBarrelClusterFastTimer',
  ecalDepth = cms.double(7),
  resolutionModels = cms.VPSet(
    cms.PSet(
      modelName = cms.string('PerfectResolutionModel')
    )
  ),
  timedVertices = cms.InputTag('offlinePrimaryVertices4D'),
  minFractionToConsider = cms.double(0.1),
  ebClusters = cms.InputTag('particleFlowClusterECALUncorrected'),
  minEnergyToConsider = cms.double(0),
  ebTimeHits = cms.InputTag('ecalDetailedTimeRecHit', 'EcalRecHitsEB'),
  mightGet = cms.optional.untracked.vstring
)
