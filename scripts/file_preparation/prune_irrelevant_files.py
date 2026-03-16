# The purpose of the script is to prune the mechanism file so that it only includes the coverage dependent yaml file. 
# This is done because the file is very large and only 10% of the total filesize is useful to me. I also do not
# have very much free space on my virtual machine.

import os

# get a list of all the folders in the main directory that holds the mechanism files

all_files = os.listdir('data/mechanism_files')

#iterate over every folder in that list

for folder in all_files:

    # now that we're in the folder, we need a list of all the files in that folder

    file_path = f"data/mechanism_files/{folder}"

    files = os.listdir(file_path)

    #now we need to iterate over all of the files in delete all the ones that are not the cov dependent yaml file

    for file_name in files:

        if file_name != 'chem_covdep.yaml':

            os.remove(f"{file_path}/{file_name}")

