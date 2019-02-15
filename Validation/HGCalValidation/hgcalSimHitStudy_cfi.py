import FWCore.ParameterSet.Config as cms

hgcalSimHitStudy = cms.EDAnalyzer('HGCalSimHitStudy',
  detectorNames = cms.vstring(
    'HGCalEESensitive',
    'HGCalHESiliconSensitive',
    'Hcal'
  ),
  caloHitSources = cms.vstring(
    'HGCHitsEE',
    'HGCHitsHEfront',
    'HcalHits'
  ),
  rMin = cms.untracked.double(0),
  rMax = cms.untracked.double(3000),
  zMin = cms.untracked.double(3000),
  zMax = cms.untracked.double(6000),
  etaMin = cms.untracked.double(1),
  etaMax = cms.untracked.double(3),
  nBinR = cms.untracked.int32(300),
  nBinZ = cms.untracked.int32(300),
  nBinEta = cms.untracked.int32(200),
  verbosity = cms.untracked.int32(0),
  ifNose = cms.untracked.bool(False)
)