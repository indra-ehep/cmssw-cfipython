import FWCore.ParameterSet.Config as cms

materialBudgetVolumeAnalysis = cms.EDAnalyzer('MaterialBudgetVolumeAnalysis',
  names = cms.vstring(
    'BEAM',
    'BEAM1',
    'BEAM2',
    'BEAM3',
    'BEAM4',
    'Tracker',
    'ECAL',
    'HCal',
    'MUON',
    'VCAL',
    'MGNT',
    'OQUA',
    'CALOEC'
  ),
  inputTag = cms.InputTag('g4SimHits', 'MaterialInformation'),
  nBinEta = cms.int32(300),
  nBinPhi = cms.int32(180),
  etaLow = cms.double(-6),
  etaHigh = cms.double(6),
  mightGet = cms.optional.untracked.vstring
)
