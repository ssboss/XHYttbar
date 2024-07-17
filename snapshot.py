'''
Script to generate a smaller snapshot from a main dataset.
'''
from XHY_class import XHY
from argparse import ArgumentParser
from TIMBER.Tools.Common import CompileCpp

# Input to the script
parser = ArgumentParser()
parser.add_argument('-s', type=str, dest='setname',
                    action='store', required=True,
                    help='Setname to process.')
parser.add_argument('-y', type=str, dest='year',
                    action='store', required=True,
                    help='Year of set (16, 17, 18).')
parser.add_argument('-j', type=int, dest='ijob',
                    action='store', default=1,
                    help='Job number')
parser.add_argument('-n', type=int, dest='njobs',
                    action='store', default=1,
                    help='Number of jobs')
args = parser.parse_args()

# Instantiate the XHY file I/O class
X = XHY(f'raw_nano/{args.setname}_{args.year}.txt',args.ijob,args.njobs)

# Compile the custom C++ to help preselection
CompileCpp('HWWmodules.cc')

#NSTART = self.getNweighted()
#self.AddCutflowColumn(self.NSTART,'NSTART')

flags = [
    'Flag_goodVertices',
    'Flag_globalSuperTightHalo2016Filter',
    'Flag_HBHENoiseFilter',
    'Flag_HBHENoiseIsoFilter',
    'Flag_EcalDeadCellTriggerPrimitiveFilter',
    'Flag_BadPFMuonFilter',
    'Flag_BadPFMuonDzFilter',
    'Flag_eeBadScFilter'
]

if args.year == '17' or args.year == '18':
    flags.append('Flag_ecalBadCalibFilter')

MET_filters = X.a.GetFlagString(flags)       # string valid (existing in RDataFrame node) flags together w logical and
X.a.Cut('flags', MET_filters)
#self.NFLAGS = self.getNweighted()
#self.AddCutflowColumn(self.NFLAGS, "NFLAGS")

# at least one lepton passing pre-selection criteria
X.a.Define('isLeptonPre','isLeptonPreselected(nElectron, Electron_pt, Electron_eta, Electron_miniPFRelIso_all, nMuon, Muon_pt, Muon_eta, Muon_miniPFRelIso_all)')
X.a.Cut('isLeptonPreselected','isLeptonPre')
#self.LEPPRE=self.getNweighted()
#self.AddCutflowColumn(self.LEPPRE,'LEPPRE')

#events pass jet preselection
X.a.Define('isJetPre','isJetPreselected(nFatJet,FatJet_pt,FatJet_eta,FatJet_msoftdrop)')    
X.a.Cut('isJetPreselected','isJetPre')
#self.JETPRE = self.getNweighted()
#self.AddCutflowColumn(self.JETPRE,'JETPRE') 

#MET cut
X.a.Cut('MET_cut','MET_pt > 25')
#self.METPT = self.getNweighted()
#self.AddCutflowColumn(self.METPT, "METPT")


# Generate the actual snapshot
columns = [       
    'nJet','Jet_btagDeepFlavB','Jet_pt','Jet_eta','Jet_phi','Jet_mass','Jet_btagDeepB','Jet_jetId',
    'nFatJet','FatJet_eta','FatJet_msoftdrop','FatJet_pt','FatJet_phi','FatJet_JES_nom','FatJet_particleNetMD*', 'FatJet_rawFactor','FatJet_particleNet_mass',
    'FatJet_subJetIdx1','FatJet_subJetIdx2','FatJet_hadronFlavour','FatJet_nBHadrons','FatJet_nCHadrons','SubJet*'
    'FatJet_jetId','nCorrT1METJet','CorrT1METJet_*','nMuon','Muon_*','nElectron','Electron_*',
    'RawMET_phi','RawMET_pt','RawMET_sumEt','ChsMET_phi','ChsMET_pt','ChsMET_sumEt','MET_phi','MET_pt','MET_sumEt',
    'genWeight','event','eventWeight','luminosityBlock','run','NSTART','NFLAGS','LEPPRE','JETPRE','METPT'
]
columns.extend(['nGenJet','nSoftActivityJet','nSubJet'])
columns.extend(['HLT_AK8*','HLT_PFHT*','HLT_PFJet*','HLT_Iso*','HLT_Mu*','HLT_TkMu*','HLT_OldMu*','HLT_Ele*','HLT_Photon*','HLT_MET*','HLT_PFMET*'])

outfile = f'{args.setname}_{args.year}_{args.ijob}of{args.njobs}snapshot.root'

X.a.Snapshot(columns, outfile, 'Events', openOption='RECREATE', saveRunChain=True)


