# basic script to analyze ttbar-allhad and ttbar-semilep

import ROOT, sys
from argparse import ArgumentParser
from TIMBER.Analyzer import HistGroup, analyzer
from TIMBER.Tools.Plot import *


# sets arguments for file input and saves filename
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


setname=args.setname
year=args.year
ijob=args.ijob
njobs=args.njobs



# names of desired variables to plot
varnames = {
        'lead_Jetmass': 'leading_jet_mass',
        'lead_JetPT': 'leading_jet_PT',
        'sublead_Jetmass': 'sublead_jet_mass',
        'sublead_JetPT': 'sublead_jet_PT',
        'lead_Muonmass': 'leading_Muon_mass',
        'lead_MuonPT': 'leading_Muon_PT',
        'lead_Emass': 'leading_electron_mass',
        'lead_EPT': 'leading_electron_PT',
        }

# main function that handles cuts and selections on desired variables 
def selection():

    # 
    file_name = f"{setname}_{year}_{ijob}of{njobs}snapshot.root"
    a = analyzer(file_name)

    # insert flags and triggers for pre-selection
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
    if year == '17' or year == '18':
        flags.append('Flag_ecalBadCalibFilter')
   
    MET_filters = a.GetFlagString(flags)

    # initial cut along these flags
    a.Cut('flags', MET_filters)

    # defining desired variables to plot
    a.Define('lead_Jetmass', 'FatJet_mass[0]')
    a.Define('lead_JetPT', 'FatJet_pt[0]')
    a.Define('sublead_Jetmass', 'FatJet_mass[1]')
    a.Define('sublead_JetPT', 'FatJet_pt[1]')
    a.Define('lead_Muonmass', 'Muon_mass')
    a.Define('lead_MuonPT', 'Muon_pt')
    a.Define('lead_Emass', 'Electron_mass')
    a.Define('lead_EPT', 'Electron_pt')


    out = HistGroup("%s_%s"%(setname,year))
    print('start')
    for varname in varnames.keys():
        print('saving varname: %s'%(varname))
        histname = '%s_%s_%s'%(setname,year,varname)
        print('a')
        # Arguments for binning that you would normally pass to a TH1 (histname, histname, number of bins, min bin, max bin)
        hist_tuple = (histname,histname,30,40,200)
        print('b')
        hist = a.GetActiveNode().DataFrame.Histo1D(hist_tuple,varname) # Project dataframe into a histogram (hist name/binning tuple, variable to plot from dataframe, weight)
        hist.SetXTitle(f"{varnames[varname]}")
        hist.SetYTitle("Events")
        print('c')
        hist.GetValue() # This gets the actual TH1 instead of a pointer to the TH1
        print('d')
        out.Add(varname,hist) # Add it to our group

    # Return the group
    print('done')
    return out


if __name__ == "__main__":
    # histgroups = {} # all of the HistGroups we want to track
    # Perform selection and write out histograms
    histgroup = selection()
    outfile = ROOT.TFile("selection.root", 'RECREATE')
    #outfile.cd()
    histgroup.Do("Write")# This will call TH1.Write() for all of the histograms in the group
    outfile.Close()
    # del histgroup # Now that they are saved out, drop from memory
            
    # # Open histogram files that we saved
    # infile = ROOT.TFile.Open("rootfiles/exercise1.root")
    # # ... raise exception if we forgot to run with --select!
    # if infile == None:
    #     raise TypeError("rootfiles/exercise1.root does not exist")
    # # Put histograms back into HistGroups
    # histgroups[setname] = HistGroup(setname)
    # for key in infile.GetListOfKeys(): # loop over histograms in the file
    #     keyname = key.GetName()
    #     if setname not in keyname: continue # skip if it's not for the current set we are on
    #     varname = keyname[len(setname+'_'+options.year)+1:] # get the variable name (ex. lead_tau32)
    #     inhist = infile.Get(key.GetName()) # get it from the file
    #     inhist.SetDirectory(0) # set the directory so hist is stored in memory and not as reference to TFile (this way it doesn't get tossed by python garbage collection when infile changes)
    #     histgroups[setname].Add(varname,inhist) # add to our group

    # # For each variable to plot...
    # for varname in varnames.keys():
    #     plot_filename = '/exercise1_{}.png'.format(varname)

    #     # Plot everything together!
    # EasyPlots(
    #     name = plot_filename, 
    #     histlist = [signal_hists[sig]],
    #     xtitle = varnames[varname],
    #     ytitle = 'Events',
    #     datastyle = 'hist'
    # )
