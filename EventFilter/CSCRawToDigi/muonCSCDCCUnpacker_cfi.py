import FWCore.ParameterSet.Config as cms

muonCSCDCCUnpacker = cms.EDProducer('CSCDCCUnpacker',
  InputObjects = cms.InputTag('rawDataCollector'),
  UseExaminer = cms.bool(True),
  ExaminerMask = cms.uint32(535557110),
  UseSelectiveUnpacking = cms.bool(True),
  ErrorMask = cms.uint32(0),
  UnpackStatusDigis = cms.bool(False),
  UseFormatStatus = cms.bool(True),
  useRPCs = cms.bool(False),
  useGEMs = cms.bool(True),
  useCSCShowers = cms.bool(True),
  Debug = cms.untracked.bool(False),
  PrintEventNumber = cms.untracked.bool(False),
  runDQM = cms.untracked.bool(False),
  VisualFEDInspect = cms.untracked.bool(False),
  VisualFEDShort = cms.untracked.bool(False),
  FormatedEventDump = cms.untracked.bool(False),
  SuppressZeroLCT = cms.untracked.bool(True),
  DisableMappingCheck = cms.untracked.bool(False),
  B904Setup = cms.untracked.bool(False),
  mightGet = cms.optional.untracked.vstring
)
