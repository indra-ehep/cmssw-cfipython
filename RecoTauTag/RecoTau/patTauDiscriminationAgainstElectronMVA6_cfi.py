import FWCore.ParameterSet.Config as cms

patTauDiscriminationAgainstElectronMVA6 = cms.EDProducer('PATTauDiscriminationAgainstElectronMVA6',
  minMVANoEleMatchWOgWOgsfBL = cms.double(0),
  minMVANoEleMatchWgWOgsfBL = cms.double(0),
  vetoEcalCracks = cms.bool(True),
  usePhiAtEcalEntranceExtrapolation = cms.bool(False),
  mvaName_wGwGSF_EC = cms.string('gbr_wGwGSF_EC'),
  minMVAWgWgsfBL = cms.double(0),
  mvaName_woGwGSF_EC = cms.string('gbr_woGwGSF_EC'),
  minMVAWOgWgsfEC = cms.double(0),
  mvaName_wGwGSF_BL = cms.string('gbr_wGwGSF_BL'),
  mvaName_woGwGSF_BL = cms.string('gbr_woGwGSF_BL'),
  returnMVA = cms.bool(True),
  loadMVAfromDB = cms.bool(True),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  mvaName_NoEleMatch_woGwoGSF_BL = cms.string('gbr_NoEleMatch_woGwoGSF_BL'),
  srcElectrons = cms.InputTag('slimmedElectrons'),
  minMVANoEleMatchWOgWOgsfEC = cms.double(0),
  mvaName_NoEleMatch_wGwoGSF_BL = cms.string('gbr_NoEleMatch_wGwoGSF_BL'),
  PATTauProducer = cms.InputTag('slimmedTaus'),
  minMVAWOgWgsfBL = cms.double(0),
  minMVAWgWgsfEC = cms.double(0),
  verbosity = cms.int32(0),
  mvaName_NoEleMatch_wGwoGSF_EC = cms.string('gbr_NoEleMatch_wGwoGSF_EC'),
  method = cms.string('BDTG'),
  mvaName_NoEleMatch_woGwoGSF_EC = cms.string('gbr_NoEleMatch_woGwoGSF_EC'),
  minMVANoEleMatchWgWOgsfEC = cms.double(0),
  mightGet = cms.optional.untracked.vstring
)
