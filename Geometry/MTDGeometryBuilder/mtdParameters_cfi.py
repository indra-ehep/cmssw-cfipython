import FWCore.ParameterSet.Config as cms

mtdParameters = cms.ESProducer('MTDParametersESModule',
  appendToDataLabel = cms.string('')
)
