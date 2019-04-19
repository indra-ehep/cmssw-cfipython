import FWCore.ParameterSet.Config as cms

L3MuonProducer = cms.EDProducer('L3MuonProducer',
  ServiceParameters = cms.PSet(
    Propagators = cms.untracked.vstring(
      'hltESPSmartPropagatorAny',
      'SteppingHelixPropagatorAny',
      'hltESPSmartPropagator',
      'hltESPSteppingHelixPropagatorOpposite'
    ),
    RPCLayers = cms.bool(True),
    UseMuonNavigation = cms.untracked.bool(True)
  ),
  MuonCollectionLabel = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
  TrackLoaderParameters = cms.PSet(
    PutTkTrackIntoEvent = cms.untracked.bool(False),
    TTRHBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    beamSpot = cms.InputTag('hltOnlineBeamSpot'),
    SmoothTkTrack = cms.untracked.bool(False),
    MuonSeededTracksInstance = cms.untracked.string('L2Seeded'),
    Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
    MuonUpdatorAtVertexParameters = cms.PSet(
      MaxChi2 = cms.double(1000000),
      Propagator = cms.string('hltESPSteppingHelixPropagatorOpposite'),
      BeamSpotPositionErrors = cms.vdouble(
        0.1,
        0.1,
        5.3
      )
    ),
    VertexConstraint = cms.bool(False),
    DoSmoothing = cms.bool(False)
  ),
  L3TrajBuilderParameters = cms.PSet(
    ScaleTECyFactor = cms.double(-1),
    tkTrajVertex = cms.InputTag('hltPixelVertices'),
    tkTrajUseVertex = cms.bool(False),
    GlbRefitterParameters = cms.PSet(
      TrackerSkipSection = cms.int32(-1),
      DoPredictionsOnly = cms.bool(False),
      PropDirForCosmics = cms.bool(False),
      HitThreshold = cms.int32(1),
      MuonHitsOption = cms.int32(1),
      RefitFlag = cms.bool(True),
      Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
      SkipStation = cms.int32(-1),
      TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
      Chi2CutRPC = cms.double(1),
      MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
      RefitDirection = cms.string('insideOut'),
      CSCRecSegmentLabel = cms.InputTag('hltCscSegments'),
      GEMRecHitLabel = cms.InputTag('gemRecHits'),
      ME0RecHitLabel = cms.InputTag('me0Segments'),
      DYTthrs = cms.vint32(
        30,
        15
      ),
      DYTselector = cms.int32(1),
      DYTupdator = cms.bool(False),
      DYTuseAPE = cms.bool(False),
      DYTuseThrsParametrization = cms.bool(False),
      DYTthrsParameters = cms.PSet(
        eta0p8 = cms.vdouble(
          1,
          -0.919853,
          0.990742
        ),
        eta1p2 = cms.vdouble(
          1,
          -0.897354,
          0.987738
        ),
        eta2p0 = cms.vdouble(
          1,
          -0.986855,
          0.998516
        ),
        eta2p2 = cms.vdouble(
          1,
          -0.940342,
          0.992955
        ),
        eta2p4 = cms.vdouble(
          1,
          -0.947633,
          0.993762
        )
      ),
      Chi2CutCSC = cms.double(150),
      Chi2CutDT = cms.double(10),
      Chi2CutGEM = cms.double(1),
      Chi2CutME0 = cms.double(1),
      RefitRPCHits = cms.bool(True),
      DTRecSegmentLabel = cms.InputTag('hltDt4DSegments'),
      Propagator = cms.string('hltESPSmartPropagatorAny'),
      TrackerSkipSystem = cms.int32(-1)
    ),
    tkTrajMaxChi2 = cms.double(9999),
    ScaleTECxFactor = cms.double(-1),
    TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
    tkTrajBeamSpot = cms.InputTag('hltOnlineBeamSpot'),
    MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
    tkTrajMaxDXYBeamSpot = cms.double(9999),
    TrackerPropagator = cms.string('SteppingHelixPropagatorAny'),
    MuonTrackingRegionBuilder = cms.PSet(
      precise = cms.bool(True),
      Eta_fixed = cms.bool(True),
      Eta_min = cms.double(0.1),
      Z_fixed = cms.bool(False),
      MeasurementTrackerName = cms.InputTag('hltESPMeasurementTracker'),
      maxRegions = cms.int32(2),
      Pt_min = cms.double(3),
      Rescale_Dz = cms.double(4),
      PhiR_UpperLimit_Par1 = cms.double(0.6),
      PhiR_UpperLimit_Par2 = cms.double(0.2),
      vertexCollection = cms.InputTag('pixelVertices'),
      Phi_fixed = cms.bool(True),
      input = cms.InputTag('hltL2Muons', 'UpdatedAtVtx'),
      DeltaR = cms.double(0.025),
      OnDemand = cms.int32(-1),
      DeltaZ = cms.double(24.2),
      Rescale_phi = cms.double(3),
      Rescale_eta = cms.double(3),
      DeltaEta = cms.double(0.04),
      DeltaPhi = cms.double(0.15),
      Phi_min = cms.double(0.1),
      UseVertex = cms.bool(False),
      EtaR_UpperLimit_Par1 = cms.double(0.25),
      EtaR_UpperLimit_Par2 = cms.double(0.15),
      beamSpot = cms.InputTag('hltOnlineBeamSpot'),
      EscapePt = cms.double(3),
      Pt_fixed = cms.bool(False)
    ),
    RefitRPCHits = cms.bool(True),
    PCut = cms.double(2.5),
    TrackTransformer = cms.PSet(
      DoPredictionsOnly = cms.bool(False),
      Fitter = cms.string('hltESPL3MuKFTrajectoryFitter'),
      Smoother = cms.string('hltESPKFTrajectorySmootherForMuonTrackLoader'),
      Propagator = cms.string('hltESPSmartPropagatorAny'),
      RefitDirection = cms.string('insideOut'),
      RefitRPCHits = cms.bool(True),
      TrackerRecHitBuilder = cms.string('hltESPTTRHBWithTrackAngle'),
      MuonRecHitBuilder = cms.string('hltESPMuonTransientTrackingRecHitBuilder'),
      MTDRecHitBuilder = cms.string('MTDRecHitBuilder')
    ),
    GlobalMuonTrackMatcher = cms.PSet(
      Quality_3 = cms.double(7),
      DeltaRCut_1 = cms.double(0.1),
      MinP = cms.double(2.5),
      MinPt = cms.double(1),
      Quality_2 = cms.double(15),
      Pt_threshold2 = cms.double(999999999),
      LocChi2Cut = cms.double(0.001),
      Eta_threshold = cms.double(1.2),
      Pt_threshold1 = cms.double(0),
      Chi2Cut_1 = cms.double(50),
      Quality_1 = cms.double(20),
      Chi2Cut_3 = cms.double(200),
      DeltaRCut_3 = cms.double(1),
      DeltaRCut_2 = cms.double(0.2),
      DeltaDCut_1 = cms.double(40),
      DeltaDCut_2 = cms.double(10),
      DeltaDCut_3 = cms.double(15),
      Chi2Cut_2 = cms.double(50),
      Propagator = cms.string('hltESPSmartPropagator')
    ),
    PtCut = cms.double(1),
    matchToSeeds = cms.bool(True),
    tkTrajLabel = cms.InputTag('hltBRSMuonSeededTracksOutIn')
  )
)
