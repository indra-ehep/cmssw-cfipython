import FWCore.ParameterSet.Config as cms

LepInJetProducer = cms.EDProducer('LepInJetProducer',
  src = cms.required.InputTag,
  srcEle = cms.required.InputTag,
  srcMu = cms.required.InputTag,
  mightGet = cms.optional.untracked.vstring
)
