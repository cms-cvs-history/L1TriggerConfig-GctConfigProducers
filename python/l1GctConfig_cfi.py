import FWCore.ParameterSet.Config as cms

from L1TriggerConfig.GctConfigProducers.l1GctJetCounterConfig_cfi import *
L1GctConfigProducers = cms.ESProducer("L1GctConfigProducers",
    JetFinderCentralJetSeed = cms.uint32(1),
    # The CalibrationStyle should be either "PowerSeries", "ORCAStyle" or "PiecewiseCubic"
    CalibrationStyle = cms.string('ORCAStyle'),
    L1CaloHtScaleLsbInGeV = cms.double(1.0),
    PowerSeriesCoefficients = cms.PSet(
        nonTauJetCalib10 = cms.vdouble(),
        tauJetCalib0 = cms.vdouble(),
        nonTauJetCalib0 = cms.vdouble(),
        tauJetCalib3 = cms.vdouble(),
        tauJetCalib1 = cms.vdouble(),
        tauJetCalib4 = cms.vdouble(),
        nonTauJetCalib8 = cms.vdouble(),
        nonTauJetCalib9 = cms.vdouble(),
        tauJetCalib2 = cms.vdouble(),
        tauJetCalib5 = cms.vdouble(),
        nonTauJetCalib2 = cms.vdouble(),
        nonTauJetCalib3 = cms.vdouble(),
        tauJetCalib6 = cms.vdouble(),
        nonTauJetCalib1 = cms.vdouble(),
        nonTauJetCalib6 = cms.vdouble(),
        nonTauJetCalib7 = cms.vdouble(),
        nonTauJetCalib4 = cms.vdouble(),
        nonTauJetCalib5 = cms.vdouble()
    ),
    JetFinderForwardJetSeed = cms.uint32(1),
    PiecewiseCubicCoefficients = cms.PSet(
        nonTauJetCalib10 = cms.vdouble(150.0, 80.0, 1.70475, -0.142171, 0.00104963, -1.62214e-05, 5.0, 1.70475, -0.142171, 0.00104963, -1.62214e-05),
        tauJetCalib0 = cms.vdouble(500.0, 100.0, 17.7409, 0.351901, -0.000701462, 5.77204e-07, 5.0, 0.720604, 1.25179, -0.0150777, 7.13711e-05),
        nonTauJetCalib0 = cms.vdouble(500.0, 100.0, 17.7409, 0.351901, -0.000701462, 5.77204e-07, 5.0, 0.720604, 1.25179, -0.0150777, 7.13711e-05),
        tauJetCalib3 = cms.vdouble(500.0, 100.0, 27.7822, 0.155986, -0.000266441, 6.69814e-08, 5.0, 2.64613, 1.30745, -0.0180964, 8.83567e-05),
        tauJetCalib1 = cms.vdouble(500.0, 100.0, 20.0549, 0.321867, -0.00064901, 5.50042e-07, 5.0, 1.30465, 1.2774, -0.0159193, 7.64496e-05),
        tauJetCalib4 = cms.vdouble(500.0, 100.0, 26.6384, 0.0567369, -0.000416292, 2.60929e-07, 5.0, 2.63299, 1.16558, -0.0170351, 7.95703e-05),
        nonTauJetCalib8 = cms.vdouble(250.0, 150.0, 1.38861, 0.0362661, 0.0, 0.0, 5.0, 1.87993, 0.0329907, 0.0, 0.0),
        nonTauJetCalib9 = cms.vdouble(200.0, 80.0, 35.0095, -0.669677, 0.00208498, -1.50554e-06, 5.0, 3.16074, -0.114404, 0.0, 0.0),
        tauJetCalib2 = cms.vdouble(500.0, 100.0, 24.3454, 0.257989, -0.000450184, 3.09951e-07, 5.0, 2.1034, 1.32441, -0.0173659, 8.50669e-05),
        tauJetCalib5 = cms.vdouble(500.0, 100.0, 29.5396, 0.001137, -0.000145232, 6.91445e-08, 5.0, 4.16752, 1.08477, -0.016134, 7.69652e-05),
        nonTauJetCalib2 = cms.vdouble(500.0, 100.0, 24.3454, 0.257989, -0.000450184, 3.09951e-07, 5.0, 2.1034, 1.32441, -0.0173659, 8.50669e-05),
        nonTauJetCalib3 = cms.vdouble(500.0, 100.0, 27.7822, 0.155986, -0.000266441, 6.69814e-08, 5.0, 2.64613, 1.30745, -0.0180964, 8.83567e-05),
        tauJetCalib6 = cms.vdouble(500.0, 100.0, 30.1405, -0.14281, 0.000555849, -7.52446e-07, 5.0, 4.79283, 0.672125, -0.00879174, 3.65776e-05),
        nonTauJetCalib1 = cms.vdouble(500.0, 100.0, 20.0549, 0.321867, -0.00064901, 5.50042e-07, 5.0, 1.30465, 1.2774, -0.0159193, 7.64496e-05),
        nonTauJetCalib6 = cms.vdouble(500.0, 100.0, 30.1405, -0.14281, 0.000555849, -7.52446e-07, 5.0, 4.79283, 0.672125, -0.00879174, 3.65776e-05),
        nonTauJetCalib7 = cms.vdouble(300.0, 80.0, 30.2715, -0.539688, 0.00499898, -1.2204e-05, 5.0, 1.97284, 0.0610729, 0.00671548, -7.22583e-05),
        nonTauJetCalib4 = cms.vdouble(500.0, 100.0, 26.6384, 0.0567369, -0.000416292, 2.60929e-07, 5.0, 2.63299, 1.16558, -0.0170351, 7.95703e-05),
        nonTauJetCalib5 = cms.vdouble(500.0, 100.0, 29.5396, 0.001137, -0.000145232, 6.91445e-08, 5.0, 4.16752, 1.08477, -0.016134, 7.69652e-05)
    ),
    OrcaStyleCoefficients = cms.PSet(
        nonTauJetCalib10 = cms.vdouble(9.3, 1.3, 0.2719, 0.003418),
        tauJetCalib0 = cms.vdouble(47.4, -20.7, 0.7922, 9.53e-05),
        nonTauJetCalib0 = cms.vdouble(47.4, -20.7, 0.7922, 9.53e-05),
        tauJetCalib3 = cms.vdouble(49.3, -22.9, 0.7331, 0.0001221),
        tauJetCalib1 = cms.vdouble(49.4, -22.5, 0.7867, 9.6e-05),
        tauJetCalib4 = cms.vdouble(48.2, -24.5, 0.7706, 0.000128),
        nonTauJetCalib8 = cms.vdouble(13.1, -4.5, 0.7071, 7.26e-05),
        nonTauJetCalib9 = cms.vdouble(12.4, -3.8, 0.6558, 0.000489),
        tauJetCalib2 = cms.vdouble(47.1, -22.2, 0.7645, 0.0001209),
        tauJetCalib5 = cms.vdouble(42.0, -23.9, 0.7945, 0.0001458),
        nonTauJetCalib2 = cms.vdouble(47.1, -22.2, 0.7645, 0.0001209),
        nonTauJetCalib3 = cms.vdouble(49.3, -22.9, 0.7331, 0.0001221),
        tauJetCalib6 = cms.vdouble(33.8, -22.1, 0.8202, 0.0001403),
        nonTauJetCalib1 = cms.vdouble(49.4, -22.5, 0.7867, 9.6e-05),
        nonTauJetCalib6 = cms.vdouble(33.8, -22.1, 0.8202, 0.0001403),
        nonTauJetCalib7 = cms.vdouble(17.1, -6.6, 0.6958, 6.88e-05),
        nonTauJetCalib4 = cms.vdouble(48.2, -24.5, 0.7706, 0.000128),
        nonTauJetCalib5 = cms.vdouble(42.0, -23.9, 0.7945, 0.0001458)
    ),
    # Get the jet counter setup from a separate file
    jetCounterSetup = cms.PSet(
        jcSetup1
    ),
    L1CaloJetZeroSuppressionThresholdInGeV = cms.double(5.0),
    ConvertEtValuesToEnergy = cms.bool(False)
)


