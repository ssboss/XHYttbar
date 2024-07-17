bool isLeptonPreselected(int nElectron, RVec<float> elePt, RVec<float> eleEta, RVec<float> eleIso, int nMuon, RVec<float> muPt, RVec<float> muEta, RVec<float> muIso){
    if (nElectron < 1 && nMuon < 1) {return false;}
    bool isLepPre = false;
    for (int idx=0; idx<elePt.size(); idx++){
        if (elePt[idx] > 20 && std::abs(eleEta[idx]) < 2.5 && eleIso[idx] < 0.5){
            isLepPre = true;
            return isLepPre;
        }
    }
    for (int idx=0; idx<muPt.size(); idx++){
        if (muPt[idx] > 20 && std::abs(muEta[idx]) < 2.4 && muIso[idx] < 0.5){
            isLepPre = true;
            break;
        }
    }   
    return isLepPre;
}


bool isJetPreselected(int nFatJet, RVec<float> FatJet_pt, RVec<float> FatJet_eta, RVec<float> FatJet_mass) {
    bool isJetPre = false;
    // perform standard jet pre-selection
    if (nFatJet < 2) {return isJetPre;}
    int idx1 = -1;
    for (int idx=0; idx<FatJet_pt.size(); idx++) {
        //check if first ak8 jets exists
        if (FatJet_pt[idx] > 200 && std::abs(FatJet_eta[idx]) < 2.4 && FatJet_mass[idx] > 50) {
            idx1 = idx;
            break;
        }
    }
    if (idx1 == -1) {return isJetPre;}
    for (int idx=idx1+1; idx<FatJet_pt.size(); idx++) {
        if (FatJet_pt[idx] > 200 && std::abs(FatJet_eta[idx]) < 2.4 && FatJet_mass[idx] > 50) {
            isJetPre = true;
            break;
        }
    }
    return isJetPre;
}

