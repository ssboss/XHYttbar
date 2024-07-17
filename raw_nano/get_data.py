from TIMBER.Tools.Common import ExecuteCmd
import sys

das = {
    '16APV' : {
        'JetHTDataBv1':  '/JetHT/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'JetHTDataBv2':  '/JetHT/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'JetHTDataC':  '/JetHT/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'JetHTDataD':  '/JetHT/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'JetHTDataE':  '/JetHT/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'JetHTDataF':  '/JetHT/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataBv1': '/SingleMuon/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataBv2': '/SingleMuon/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataC': '/SingleMuon/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataD': '/SingleMuon/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataE': '/SingleMuon/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataF': '/SingleMuon/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleElectronDataBv1' : '/SingleElectron/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleElectronDataBv2' : '/SingleElectron/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD', 
        'SingleElectronDataC' : '/SingleElectron/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleElectronDataD' : '/SingleElectron/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleElectronDataE' : '/SingleElectron/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleElectronDataF' : '/SingleElectron/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SinglePhotonDataBv1' : '/SinglePhoton/Run2016B-ver1_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SinglePhotonDataBv2' : '/SinglePhoton/Run2016B-ver2_HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SinglePhotonDataC' : '/SinglePhoton/Run2016C-HIPM_UL2016_MiniAODv2_NanoAODv9-v4/NANOAOD',
        'SinglePhotonDataD' : '/SinglePhoton/Run2016D-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SinglePhotonDataE' : '/SinglePhoton/Run2016E-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SinglePhotonDataF' : '/SinglePhoton/Run2016F-HIPM_UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD'
    },
    '16' : {
        'JetHTDataF':  '/JetHT/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataG':  '/JetHT/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataH':  '/JetHT/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataF': '/SingleMuon/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataG': '/SingleMuon/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataH': '/SingleMuon/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataF' : '/SingleElectron/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataG' : '/SingleElectron/Run2016G-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataH' : '/SingleElectron/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataF' : '/SinglePhoton/Run2016F-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataG' : '/SinglePhoton/Run2016G-UL2016_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SinglePhotonDataH' : '/SinglePhoton/Run2016H-UL2016_MiniAODv2_NanoAODv9-v1/NANOAOD'
    },
    '17' : {
        'JetHTDataB': '/JetHT/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataC': '/JetHT/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataD': '/JetHT/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataE': '/JetHT/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataF': '/JetHT/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataB': '/SingleMuon/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataC': '/SingleMuon/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataD': '/SingleMuon/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataE': '/SingleMuon/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleMuonDataF': '/SingleMuon/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataB' : '/SingleElectron/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataC' : '/SingleElectron/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataD' : '/SingleElectron/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataE' : '/SingleElectron/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SingleElectronDataF' : '/SingleElectron/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataB' : '/SinglePhoton/Run2017B-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataC' : '/SinglePhoton/Run2017C-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataD' : '/SinglePhoton/Run2017D-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataE' : '/SinglePhoton/Run2017E-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'SinglePhotonDataF' : '/SinglePhoton/Run2017F-UL2017_MiniAODv2_NanoAODv9-v1/NANOAOD'
    },
    '18' : {
        'JetHTDataA': '/JetHT/Run2018A-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'JetHTDataB': '/JetHT/Run2018B-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataC': '/JetHT/Run2018C-UL2018_MiniAODv2_NanoAODv9-v1/NANOAOD',
        'JetHTDataD': '/JetHT/Run2018D-UL2018_MiniAODv2_NanoAODv9-v2/NANOAOD',
        'SingleMuonDataA': '/SingleMuon/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD',
        'SingleMuonDataB': '/SingleMuon/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD',
        'SingleMuonDataC': '/SingleMuon/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD',
        'SingleMuonDataD': '/SingleMuon/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD',
        'EGammaDataA' : '/EGamma/Run2018A-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD', 
        'EGammaDataB' : '/EGamma/Run2018B-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD',
        'EGammaDataC' : '/EGamma/Run2018C-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD',
        'EGammaDataD' : '/EGamma/Run2018D-UL2018_MiniAODv2_NanoAODv9_GT36-v1/NANOAOD'
    }
}

def GetFiles(das_name,setname,year):
    ExecuteCmd('dasgoclient -query "file dataset=%s" > %s_%s_temp.txt'%(das_name,setname,year),'dryrun' in sys.argv)
    f = open('%s_%s_temp.txt'%(setname,year),'r')
    fout = open('raw_nano/%s_%s.txt'%(setname,year),'w')
    for l in f.readlines():
        fout.write('root://cmsxrootd.fnal.gov/'+l)
    f.close()
    fout.close()
    if 'dryrun' not in sys.argv:
        ExecuteCmd('rm %s_%s_temp.txt'%(setname,year),'dryrun' in sys.argv)

latex_lines = {"16":[],"16APV":[],"17":[],"18":[]}
for year in das.keys():
    for setname in das[year].keys():
        GetFiles(das[year][setname],setname,year)
        latex_lines[year].append('| %s | %s |'%(setname,das[year][setname]))

for y in sorted(latex_lines.keys()):
    print ('\n20%s'%y)
    print ('| Setname | DAS location |')
    print ('|---------|--------------|')
    for l in latex_lines[y]: print (l)
