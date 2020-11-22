# Fuzzy-Matching-Function
This is a command line utility to fuzzy match text columns. For instance, this could be use to match company names that are spelled differently in two databases. In order for this to function you must have Python 3.7+ installed on your system as well as the standard data science stack (numpy, pandas etc.) and the fuzzywuzzy package.

If you meet the prerequisite just download the three python scripts in this repository and place them in your desired directory. Once that is done, simply navigate to that folder within the command line and call the "Fuzzy_Matcher_CL.py" script with the following arguments:

*python Fuzzy_Matcher_CL.py target_file original_file col_1 col_2 output_filename mode thresh*

Where

- **target_file:** csv file with the column whose names are the targets of fuzzy matching
- **original_file:** csv file with the column whose names are the ones that want to be retrieved
- **col_1 and col_2:** Strings with the column names
- **output_filename:** String with the desired name of the output file
- **mode:** String that is either "ratio" or "partial_ratio"
- **thresh:** an integer (0-100) with the minimum similarity percentage between 2 strings
- **n:** and integer indicating the top n results to retrieve
