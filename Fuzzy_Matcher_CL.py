#########################
# Fuzzy Matcher script
# Francisco Javier Carrera Arias
# 04/26/2018
# V2.2
#########################

import sys
from Fuzzy_Match_Function import fuzzy_matcher

# Parameters
Target = sys.argv[1] 
Original = sys.argv[2] 
col_1 = sys.argv[3]
col_2 = sys.argv[4]
out_name = sys.argv[5]
mode = sys.argv[6]
thresh = int(sys.argv[7])
n = int(sys.argv[8])

# DF fuzzy match
Matches = fuzzy_matcher(Target, Original, col_1, col_2,out_name,mode,thresh,n)

