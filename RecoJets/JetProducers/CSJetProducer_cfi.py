import FWCore.ParameterSet.Config as cms

CSJetProducer = cms.EDProducer('CSJetProducer',
  csRParam = cms.double(-1),
  csAlpha = cms.double(2),
  etaMap = cms.InputTag('hiFJRhoProducer', 'mapEtaEdges'),
  rho = cms.InputTag('hiFJRhoProducer', 'mapToRho'),
  rhom = cms.InputTag('hiFJRhoProducer', 'mapToRhoM'),
  jetCollInstanceName = cms.string(''),
  src = cms.InputTag('particleFlow'),
  srcPVs = cms.InputTag(''),
  jetType = cms.string('PFJet'),
  jetAlgorithm = cms.string('AntiKt'),
  rParam = cms.double(0.4),
  inputEtMin = cms.double(0),
  inputEMin = cms.double(0),
  jetPtMin = cms.double(5),
  doPVCorrection = cms.bool(False),
  doAreaFastjet = cms.bool(False),
  doRhoFastjet = cms.bool(False),
  doPUOffsetCorr = cms.bool(False),
  puPtMin = cms.double(10),
  nSigmaPU = cms.double(1),
  radiusPU = cms.double(0.5),
  subtractorName = cms.string(''),
  useExplicitGhosts = cms.bool(False),
  doAreaDiskApprox = cms.bool(False),
  voronoiRfact = cms.double(-0.9),
  Rho_EtaMax = cms.double(4.4),
  Ghost_EtaMax = cms.double(5),
  Active_Area_Repeats = cms.int32(1),
  GhostArea = cms.double(0.01),
  restrictInputs = cms.bool(False),
  maxInputs = cms.uint32(1),
  writeCompound = cms.bool(False),
  writeJetsWithConst = cms.bool(False),
  doFastJetNonUniform = cms.bool(False),
  useDeterministicSeed = cms.bool(False),
  minSeed = cms.uint32(14327),
  verbosity = cms.int32(0),
  puWidth = cms.double(0),
  nExclude = cms.uint32(0),
  maxBadEcalCells = cms.uint32(9999999),
  maxBadHcalCells = cms.uint32(9999999),
  maxProblematicEcalCells = cms.uint32(9999999),
  maxProblematicHcalCells = cms.uint32(9999999),
  maxRecoveredEcalCells = cms.uint32(9999999),
  maxRecoveredHcalCells = cms.uint32(9999999),
  puCenters = cms.vdouble(),
  sumRecHits = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
