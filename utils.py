################################
# Fuzzy Matcher Utils
# Francisco Javier Carrera Arias
# 03/23/2020
# V2.2
################################

"""
Util functions for the fuzzy matching program

CalcRatio_Alter
Uses cython to quickly calculet string similarity ratios between large files of strings.
Currently, not mantained as the underlying C functions must change to accomodate
the length of different files. If its used is desired please contact Francisco Carrera Arias
(fcarrera@motionpoint.com)

CalcRatio_Advanced
Main function to calculate the partial similiarity ratio between 2 strings
as implemented in the fuzzywuzzy package

Arguments:
- truNames: lower case origina list of strings
- truNamesOrig: original case list of strings
- Company: list of desired strings to match
- i: integer of the list index
- mode: string that is either "ratio" or "partial_ratio"
- thresh: an integer (0-100) with the minimum similarity percentage between 2 strings
- n: an integer with the top n results

Output
- items: Matched names

clean_company_names
Cleans company names by removing words such as coprporation or inc. that may confuse algorithms

Arguments:
- company_names: list with strings containing company names

Output
- company_names: list of strings with clean company names
"""

import numpy as np
#import TestVisits
import re
from fuzzywuzzy import fuzz

#def CalcRatio_Alter(truNames,truNamesOrig,Company,i):
#    ratiosx = TestVisits.ratMatch_Leven(truNames,str(Company[i]))*100
#    ratios3 = ratiosx.flatten()
#    extract = np.argmax(ratios3)
#    items = truNamesOrig[extract.astype(int)]
#    return items

def CalcRatio_Advanced(truNames,truNamesOrig,Company,i,mode,thresh,n):
    # Calculate the partial ratio or ratio across all the desired strings as implemented in fuzzywuzzy
    if mode == "ratio":
    	ratios = [fuzz.ratio(truNames[m],Company[i]) for m in range(len(truNames))]
    else:
        ratios = [fuzz.partial_ratio(truNames[m],Company[i]) for m in range(len(truNames))]
    # Gather the ratios and flatten the array
    ratios = np.array(ratios)
    ratios3 = ratios.flatten()
    # Extract the index of the highest similarity ratio
    extract = (-ratios3).argsort()[:n]
    # If the ratio is over the threshold add it to the results list otherwise
    # place a "None" string
    if np.any(ratios3[extract.astype(int)] >= thresh):
        items = truNamesOrig[extract.astype(int)]
    else:
        items = "None"
    #return_rat = ratios3[extract.astype(int)]
    return items #, return_rat

def clean_company_names(company_names):
    for p in range(len(company_names)):
        replaced = re.sub("inc.|llc.|corporation|incorporated|holdings|holding|n.v|technologies|ltd.|industries|limited|incorporation|company|group","",company_names[p])
        replaced = re.sub('[^\w\s]','',replaced)
        replaced = replaced.strip()
        company_names[p] = replaced
    return company_names