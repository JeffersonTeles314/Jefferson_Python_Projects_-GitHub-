def progA(varaA,varaB,varaI,varaU): 
    varlist1 = [] 
    ecovar1 = varaA+varaB*varaI 
    varlist1.append(ecovar1) 
    for varcont1 in range(varaI,varaU): 
        ecovar1 = varaB+ecovar1 
        varlist1.append(ecovar1) 
    return varlist1 
def progG(vargA,vargB,vargI,vargU): 
    varlist2 = [] 
    ecovar2 = vargA*vargB**vargI 
    varlist2.append(ecovar2) 
    for varcont2 in range(vargI,vargU): 
        ecovar2 = vargB*ecovar2 
        varlist2.append(ecovar2) 
    return varlist2
