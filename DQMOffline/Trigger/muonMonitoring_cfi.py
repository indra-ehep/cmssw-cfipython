import FWCore.ParameterSet.Config as cms

muonMonitoring = cms.EDProducer('MuonMonitor',
  FolderName = cms.string('HLT/Muon'),
  requireValidHLTPaths = cms.bool(True),
  met = cms.InputTag('pfMet'),
  muons = cms.InputTag('muons'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  electrons = cms.InputTag('gedGsfElectrons'),
  metSelection = cms.string('pt > 0'),
  muonSelection = cms.string('pt > 6 && eta<2.4'),
  eleSelection = cms.string('pt > 0'),
  nmuons = cms.uint32(0),
  nelectrons = cms.uint32(0),
  numGenericTriggerEventPSet = cms.PSet(
    ReadPrescalesFromFile = cms.bool(False),
    andOr = cms.bool(False),
    andOrDcs = cms.bool(False),
    andOrHlt = cms.bool(False),
    andOrL1 = cms.bool(False),
    errorReplyDcs = cms.bool(False),
    errorReplyHlt = cms.bool(False),
    errorReplyL1 = cms.bool(False),
    l1BeforeMask = cms.bool(False),
    stage2 = cms.bool(False),
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    dbLabel = cms.string(''),
    hltDBKey = cms.string(''),
    dcsPartitions = cms.vint32(),
    hltPaths = cms.vstring(),
    l1Algorithms = cms.vstring(),
    verbosityLevel = cms.uint32(0)
  ),
  denGenericTriggerEventPSet = cms.PSet(
    ReadPrescalesFromFile = cms.bool(False),
    andOr = cms.bool(False),
    andOrDcs = cms.bool(False),
    andOrHlt = cms.bool(False),
    andOrL1 = cms.bool(False),
    errorReplyDcs = cms.bool(False),
    errorReplyHlt = cms.bool(False),
    errorReplyL1 = cms.bool(False),
    l1BeforeMask = cms.bool(False),
    stage2 = cms.bool(False),
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    dbLabel = cms.string(''),
    hltDBKey = cms.string(''),
    dcsPartitions = cms.vint32(),
    hltPaths = cms.vstring(),
    l1Algorithms = cms.vstring(),
    verbosityLevel = cms.uint32(0)
  ),
  histoPSet = cms.PSet(
    muonPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    muonBinning = cms.vdouble(
      0,
      20,
      40,
      60,
      80,
      90,
      100,
      110,
      120,
      130,
      140,
      150,
      160,
      170,
      180,
      190,
      200,
      220,
      240,
      260,
      280,
      300,
      350,
      400,
      450,
      1000
    ),
    muonetaBinning = cms.vdouble(
      -3,
      -2.5,
      -2,
      -1.5,
      -1,
      -0.5,
      0,
      0.5,
      1,
      1.5,
      2,
      2.5,
      3
    ),
    elePtBinning2D = cms.vdouble(
      0,
      40,
      80,
      100,
      120,
      140,
      160,
      180,
      200,
      240,
      280,
      350,
      450,
      1000
    ),
    muPtBinning2D = cms.vdouble(
      0,
      40,
      80,
      100,
      120,
      140,
      160,
      180,
      200,
      240,
      280,
      350,
      450,
      1000
    ),
    eleEtaBinning2D = cms.vdouble(
      -3,
      -2,
      -1,
      0,
      1,
      2,
      3
    ),
    muEtaBinning2D = cms.vdouble(
      -3,
      -2,
      -1,
      0,
      1,
      2,
      3
    ),
    lsPSet = cms.PSet(
      nbins = cms.uint32(2500),
      xmin = cms.double(0),
      xmax = cms.double(2500)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
