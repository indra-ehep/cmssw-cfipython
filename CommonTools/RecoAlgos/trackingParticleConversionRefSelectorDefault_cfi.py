import FWCore.ParameterSet.Config as cms

trackingParticleConversionRefSelectorDefault = cms.EDProducer('TrackingParticleConversionRefSelector',
  src = cms.InputTag('mix', 'MergedTrackTruth')
)
