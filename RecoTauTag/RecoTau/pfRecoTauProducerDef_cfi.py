import FWCore.ParameterSet.Config as cms

pfRecoTauProducerDef = cms.EDProducer('PFRecoTauProducer',
  Rphi = cms.double(2),
  LeadTrack_minPt = cms.double(0),
  PVProducer = cms.InputTag('offlinePrimaryVertices'),
  ECALSignalConeSizeFormula = cms.string('0.15'),
  TrackerIsolConeMetric = cms.string('DR'),
  TrackerSignalConeMetric = cms.string('DR'),
  EcalStripSumE_deltaPhiOverQ_minValue = cms.double(-0.1),
  smearedPVsigmaX = cms.double(0.0015),
  smearedPVsigmaY = cms.double(0.0015),
  MatchingConeMetric = cms.string('DR'),
  TrackerSignalConeSizeFormula = cms.string('0.07'),
  MatchingConeSizeFormula = cms.string('0.1'),
  TrackerIsolConeSize_min = cms.double(0),
  MatchingConeSize_min = cms.double(0),
  ElectronPreIDProducer = cms.InputTag('elecpreid'),
  ChargedHadrCandLeadChargedHadrCand_tksmaxDZ = cms.double(1),
  TrackerIsolConeSize_max = cms.double(0.6),
  TrackerSignalConeSize_max = cms.double(0.07),
  HCALIsolConeMetric = cms.string('DR'),
  AddEllipseGammas = cms.bool(False),
  maximumForElectrionPreIDOutput = cms.double(-0.1),
  TrackerSignalConeSize_min = cms.double(0),
  JetPtMin = cms.double(0),
  HCALIsolConeSizeFormula = cms.string('0.50'),
  AreaMetric_recoElements_maxabsEta = cms.double(2.5),
  HCALIsolConeSize_max = cms.double(0.6),
  Track_IsolAnnulus_minNhits = cms.uint32(3),
  HCALSignalConeMetric = cms.string('DR'),
  ElecPreIDLeadTkMatch_maxDR = cms.double(0.01),
  PFTauTagInfoProducer = cms.InputTag('pfRecoTauTagInfoProducer'),
  ECALIsolConeMetric = cms.string('DR'),
  ECALIsolConeSizeFormula = cms.string('0.50'),
  UseChargedHadrCandLeadChargedHadrCand_tksDZconstraint = cms.bool(True),
  Algorithm = cms.string('ConeBased'),
  ECALIsolConeSize_max = cms.double(0.6),
  ECALSignalConeMetric = cms.string('DR'),
  EcalStripSumE_deltaPhiOverQ_maxValue = cms.double(0.5),
  HCALSignalConeSize_max = cms.double(0.6),
  ECALSignalConeSize_min = cms.double(0),
  EcalStripSumE_minClusEnergy = cms.double(0.1),
  EcalStripSumE_deltaEta = cms.double(0.03),
  TrackerIsolConeSizeFormula = cms.string('0.50'),
  LeadPFCand_minPt = cms.double(5),
  HCALSignalConeSize_min = cms.double(0),
  ECALSignalConeSize_max = cms.double(0.6),
  HCALSignalConeSizeFormula = cms.string('0.10'),
  putNeutralHadronsInP4 = cms.bool(False),
  TrackLeadTrack_maxDZ = cms.double(1),
  ChargedHadrCand_IsolAnnulus_minNhits = cms.uint32(0),
  ECALIsolConeSize_min = cms.double(0),
  UseTrackLeadTrackDZconstraint = cms.bool(True),
  MaxEtInEllipse = cms.double(2),
  DataType = cms.string('AOD'),
  smearedPVsigmaZ = cms.double(0.005),
  MatchingConeSize_max = cms.double(0.6),
  HCALIsolConeSize_min = cms.double(0)
)