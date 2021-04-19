import FWCore.ParameterSet.Config as cms

trackstersFromSimClustersProducer = cms.EDProducer('TrackstersFromSimClustersProducer',
  detector = cms.string('HGCAL'),
  layer_clusters = cms.InputTag('hgcalLayerClusters'),
  time_layerclusters = cms.InputTag('hgcalLayerClusters', 'timeLayerCluster'),
  filtered_mask = cms.InputTag('filteredLayerClustersSimTracksters', 'ticlSimTracksters'),
  simclusters = cms.InputTag('mix', 'MergedCaloTruth'),
  layerClusterSimClusterAssociator = cms.untracked.InputTag('layerClusterSimClusterAssociationProducer'),
  mightGet = cms.optional.untracked.vstring
)
