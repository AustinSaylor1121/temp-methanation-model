import random
import Simulation_Methods

import plotting_methods

import pandas as pd
import matplotlib.pyplot as plt



#get a random list of 100 mechanims to try
mechanism_numbers = random.sample(range(0,5000),100)

progress = 0
error_number = 0

for mechanism_number in mechanism_numbers:

    # specify the file path
    
    file_path = f'data/mechanism_files/File_{mechanism_number}/chem_covdep_formatted.yaml'

    # run the simulation

    try:

        headers, data = Simulation_Methods.profile_simulation(file_path)

    except Exception as e:

        print(e)
        print(f'error occured on mechanism {mechanism_number}')

        error_number = error_number + 1

    df = pd.DataFrame(data=data, columns= headers)

    plotting_methods.plot_CO2_profiles(df,mechanism_number, 1)
    plotting_methods.plot_H2_profiles(df, mechanism_number, 2)
    plotting_methods.plot_Ar_profiles(df, mechanism_number, 3)
    plotting_methods.plot_H2O_profiles(df, mechanism_number, 4)
    plotting_methods.plot_CH4_profiles(df, mechanism_number, 5)
    plotting_methods.plot_CO_profiles(df, mechanism_number, 6)

    progress = progress + 1
    print(f"Percent Complete: {progress / len(mechanism_numbers) * 100:.2f}%", end="\r")

print()
print('Percent Complete: 100%')

print(f'error rate of {error_number / len(mechanism_numbers)}')

plt.show()

