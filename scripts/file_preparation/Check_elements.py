from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

import cantera as ct

import os
import sys

# specify the file path that all of the mechanism files are in

mechanism_directory = 'data/mechanism_files'

# get a list of all of the directories 

directories = os.listdir(mechanism_directory)

progress = 0

# iterate over all of the files and format them

yaml = YAML()

with open('data/File_0_chem_covdep_unmodified.yaml', 'r') as file:
    og_data = yaml.load(file)


for directory in directories:

    file_in = f'{mechanism_directory}/{directory}/chem_covdep.yaml'
    file_out = f'{mechanism_directory}/{directory}/chem_covdep_formatted.yaml'


    # Reading data from the YAML file
    with open(file_in, 'r') as file:
        data = yaml.load(file)


    #check if the elements are the same

    same = og_data['elements'] == data['elements']

    if not same:
        print(f'error on file {directory}')

    #Print out the progress

    progress = progress + 1
    print(f"Percent Complete: {progress / len(directories) * 100:.2f}%", end="\r")

print()
print('Percent Complete: 100%')
print('All files formatted')