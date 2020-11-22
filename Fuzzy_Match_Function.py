################################
# Fuzzy Matcher Function
# Francisco Javier Carrera Arias
# 04/26/2018
# V2.2
################################

"""
Fuzzy matches strings between two dataframe columns using levenshtein distance

Arguments
- Target: csv file with the column whose names are the targets of fuzzy matching
- Original" csv file with the column whose names are the ones that want to be retrieved
- col_1 and col_2: Strings with the column names
- out_name: String with the desired name of the output file
- mode: String either "ratio" or "partial ratio"
- thresh: an integer (0-100) with the minimum similarity percentage between 2 strings
- n: an integer indicating the top n desired results

Outputs:
- A file named as outlined in out_name in your working directory
- DF: a data frame with the matches

"""

import pandas as pd
import numpy as np
from joblib import Parallel, delayed
from utils import CalcRatio_Advanced

def fuzzy_matcher(Target, Original, col_1, col_2,out_name,mode,thresh,n):

    target_names = pd.read_csv(Target,encoding = 'utf-8')
    original_names = pd.read_csv(Original,encoding = 'utf-8')

    targets = target_names[col_1]
    targets = targets.dropna()
    targetsOrig = np.sort(list(targets.values))
    targetsOrig = set(targetsOrig)
    targetsOrig = list(targetsOrig)
    targetsOrig = np.sort(targetsOrig)
    targets = np.array([x.lower() for x in targetsOrig])

    truNames = original_names[col_2]
    truNamesOrig = np.sort(list(truNames.values))
    truNamesOrig = set(truNamesOrig)
    truNamesOrig = list(truNamesOrig)
    truNamesOrig = np.sort(truNamesOrig)
    truNames = np.array([x.lower() for x in truNamesOrig])

    results = Parallel(n_jobs = -1, verbose = 50)(
                delayed(CalcRatio_Advanced)(truNames,truNamesOrig,targets,i,mode,thresh,n) for i in range(len(targets)))

    DF = pd.DataFrame(data = {'Original':targetsOrig, 'Matches':results})
    DF.to_csv(out_name,encoding = 'utf-8')  
    return DF