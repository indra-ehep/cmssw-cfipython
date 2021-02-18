import FWCore.ParameterSet.Config as cms

hltEgammaHLTExtraProducer = cms.EDProducer('EgammaHLTExtraProducer',
  minPtToSaveHits = cms.double(0),
  saveHitsPlusPi = cms.bool(False),
  saveHitsPlusHalfPi = cms.bool(True),
  egCands = cms.VPSet(
    cms.PSet(
      ecalCands = cms.InputTag('hltEgammaCandidates'),
      gsfTracks = cms.InputTag('hltEgammaGsfTracks'),
      label = cms.string(''),
      pixelSeeds = cms.InputTag('hltEgammaElectronPixelSeeds')
    )
  ),
  ecal = cms.VPSet(
    cms.PSet(
      label = cms.string('EcalRecHitsEB'),
      src = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEB')
    ),
    cms.PSet(
      label = cms.string('EcalRecHitsEE'),
      src = cms.InputTag('hltEcalRecHit', 'EcalRecHitsEE')
    )
  ),
  hcal = cms.VPSet(
    cms.PSet(
      label = cms.string(''),
      src = cms.InputTag('hltHbhereco')
    )
  ),
  trks = cms.VPSet(
    cms.PSet(
      label = cms.string(''),
      src = cms.InputTag('generalTracks')
    )
  ),
  pfClusIso = cms.VPSet(
    cms.PSet(
      label = cms.string('Ecal'),
      src = cms.InputTag('hltParticleFlowClusterECALL1Seeded')
    ),
    cms.PSet(
      label = cms.string('EcalUnseeded'),
      src = cms.InputTag('hltParticleFlowClusterECALUnseeded')
    ),
    cms.PSet(
      label = cms.string('Hcal'),
      src = cms.InputTag('hltParticleFlowClusterHCAL')
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
