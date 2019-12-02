import FWCore.ParameterSet.Config as cms

studyHLT = cms.EDAnalyzer('StudyHLT',
  particleSource = cms.InputTag('genParticles'),
  verbosity = cms.untracked.int32(0),
  triggers = cms.untracked.vstring(),
  newNames = cms.untracked.vstring(
    'HLT',
    'PixelTracks_Multiplicity',
    'HLT_Physics_',
    'HLT_JetE',
    'HLT_ZeroBias'
  ),
  trackQuality = cms.untracked.string('highPurity'),
  minTrackPt = cms.untracked.double(1),
  maxDxyPV = cms.untracked.double(0.02),
  maxDzPV = cms.untracked.double(0.02),
  maxChi2 = cms.untracked.double(5),
  maxDpOverP = cms.untracked.double(0.1),
  minOuterHit = cms.untracked.int32(4),
  minLayerCrossed = cms.untracked.int32(8),
  maxInMiss = cms.untracked.int32(0),
  maxOutMiss = cms.untracked.int32(0),
  minTrackP = cms.untracked.double(1),
  maxTrackEta = cms.untracked.double(2.6),
  timeMinCutECAL = cms.untracked.double(-500),
  timeMaxCutECAL = cms.untracked.double(500),
  timeMinCutHCAL = cms.untracked.double(-500),
  timeMaxCutHCAL = cms.untracked.double(500),
  isItAOD = cms.untracked.bool(False),
  vetoTrigger = cms.untracked.bool(False),
  doTree = cms.untracked.bool(False),
  puWeights = cms.untracked.vdouble(),
  mightGet = cms.optional.untracked.vstring
)
