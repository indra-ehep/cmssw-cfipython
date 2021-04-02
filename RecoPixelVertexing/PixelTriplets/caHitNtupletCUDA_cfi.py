import FWCore.ParameterSet.Config as cms

caHitNtupletCUDA = cms.EDProducer('CAHitNtupletCUDA',
  onGPU = cms.bool(True),
  pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingCUDA'),
  ptmin = cms.double(0.89999997615814209),
  CAThetaCutBarrel = cms.double(0.0020000000949949026),
  CAThetaCutForward = cms.double(0.0030000000260770321),
  hardCurvCut = cms.double(0.032840722495894911),
  dcaCutInnerTriplet = cms.double(0.15000000596046448),
  dcaCutOuterTriplet = cms.double(0.25),
  earlyFishbone = cms.bool(True),
  lateFishbone = cms.bool(False),
  idealConditions = cms.bool(True),
  fillStatistics = cms.bool(False),
  minHitsPerNtuplet = cms.uint32(4),
  maxNumberOfDoublets = cms.uint32(524288),
  includeJumpingForwardDoublets = cms.bool(False),
  fit5as4 = cms.bool(True),
  doClusterCut = cms.bool(True),
  doZ0Cut = cms.bool(True),
  doPtCut = cms.bool(True),
  useRiemannFit = cms.bool(False),
  trackQualityCuts = cms.PSet(
    chi2MaxPt = cms.double(10),
    chi2Coeff = cms.vdouble(
      0.68177776,
      0.74609577,
      -0.08035491,
      0.00315399
    ),
    chi2Scale = cms.double(30),
    tripletMinPt = cms.double(0.5),
    tripletMaxTip = cms.double(0.3),
    tripletMaxZip = cms.double(12),
    quadrupletMinPt = cms.double(0.3),
    quadrupletMaxTip = cms.double(0.5),
    quadrupletMaxZip = cms.double(12)
  ),
  mightGet = cms.optional.untracked.vstring
)
