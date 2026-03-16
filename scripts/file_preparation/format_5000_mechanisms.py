from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap

import cantera as ct

import os
import sys

def main():

    # specify the file path that all of the mechanism files are in

    mechanism_directory = 'data/mechanism_files'

    # get a list of all of the directories 

    directories = os.listdir(mechanism_directory)

    progress = 0

    # iterate over all of the files and format them

    for directory in directories:

        file_in = f'{mechanism_directory}/{directory}/chem_covdep.yaml'
        file_out = f'{mechanism_directory}/{directory}/chem_covdep_formatted.yaml'

        yaml = YAML()

        # Reading data from the YAML file
        with open(file_in, 'r') as file:
            data = yaml.load(file)

        #fix the formatting in the yaml file
        format_yaml_file(data)

        #save the formatted yaml file
        with open(file_out,'w') as f_out:
            yaml.dump(data,f_out)

        #Print out the progress

        progress = progress + 1
        print(f"Percent Complete: {progress / len(directories) * 100:.2f}%", end="\r")

    print()
    print('Percent Complete: 100%')
    print('All files formatted')

    progress = 0
    
    # iterate over all of the files to verify that the files load and verify that the coverage effects are working

    for directory in directories:

        # specify the filepath

        file_in = f'{mechanism_directory}/{directory}/chem_covdep_formatted.yaml'

        # try to load in the file

        try:
            surf = ct.Interface(file_in, 'surface1')

        except Exception as e:

            print(f"Error occured while loading {directory}")
            print(e)

        #test out the coverage effects

        passed_test = test_coverage_effects(surf)

        if not passed_test:
            
            print(f'{directory} failed the coverage depenency test')
            sys.exit(0)

        # Print out the progress

        progress = progress + 1
        print(f"Percent Complete: {progress / len(directories) * 100:.2f}%", end="\r")

    print()
    print('Percent Complete: 100%')
    print('All files loaded succesfully and all coverage effects are working')

def test_coverage_effects(surf):

    # Test the coverage effects for OX(10)

    species_name = 'OX(10)'
    i_sp = surf.species_index(species_name)
    h_rt_nocov = surf.standard_enthalpies_RT[i_sp]
    
    surf.coverages = {species_name: 1, 'CX(14)':1}
    h_rt_halfcov = surf.standard_enthalpies_RT[i_sp]

    passed_ox10 = h_rt_nocov != h_rt_halfcov

    # Test the coverage effects for OCX(11)

    species_name = 'OCX(11)'
    i_sp = surf.species_index(species_name)
    h_rt_nocov = surf.standard_enthalpies_RT[i_sp]

    surf.coverages = {species_name: 1, 'CX(14)':1}
    h_rt_halfcov = surf.standard_enthalpies_RT[i_sp]

    passed_ocx11 = h_rt_nocov != h_rt_halfcov

    return passed_ox10 and passed_ocx11

def format_yaml_file(data):
    # add the following to the surface phase :   adjacent-phases: [gas]
    for phase in data['phases']:
        if phase['name'] == 'surface1':
            phase['adjacent-phases'] = ['gas']

    #change the coverage dependency formatting
    for specie in data['species']:
        if specie['name'] == 'OX(10)':

            ox = specie.get('coverage-dependencies')
            dep = ox.get('OX(10)')
            h1 = dep.get('enthalpy-1st-order')
            h2 = dep.get('enthalpy-2nd-order')
            
            new_dep = CommentedMap()        
            new_dep["model"] = 'polynomial'
            new_dep["units"] = CommentedMap([("energy", 'eV'), ("quantity", "molec")])
            new_dep["enthalpy-coefficients"] = [h1, h2, 0, 0.0]

            new_dep.fa.set_flow_style()
            new_dep["units"].fa.set_flow_style()

            ox[specie['name']] = new_dep

        if specie['name'] == 'OCX(11)':
            
            ocx = specie.get('coverage-dependencies')
            dep = ocx.get('OCX(11)')
            h1 = dep.get('enthalpy-1st-order')
            h2 = dep.get('enthalpy-2nd-order')
            
            new_dep = CommentedMap()        
            new_dep["model"] = 'polynomial'
            new_dep["units"] = CommentedMap([("energy", 'eV'), ("quantity", "molec")])
            new_dep["enthalpy-coefficients"] = [h1, h2, 0, 0.0]

            new_dep.fa.set_flow_style()
            new_dep["units"].fa.set_flow_style()

            ocx[specie['name']] = new_dep

if __name__ == '__main__':
    main()