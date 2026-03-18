import random
import Simulation_Methods

import plotting_methods

import pandas as pd
import matplotlib.pyplot as plt



#get a random list of 100 mechanims to try, use a specific seed to make it reproducible
random.seed(33)
mechanism_numbers = random.sample(range(0,5000),100)
print(mechanism_numbers)

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

#add the experimental results for the CO2 profile

df = pd.read_csv('data/CO2.csv', names=['X', 'Y'])
plt.figure(1)
plt.plot(df['X'], df['Y'].transform(lambda x: x / 100), 'r', label='Experiment')
plt.legend()
plt.savefig('results/Gas_Profile_CO2.png')

#add the experimental results for the H2 profile

df = pd.read_csv('data/H2.csv', names=['X', 'Y'])
plt.figure(2)
plt.plot(df['X'], df['Y'].transform(lambda x: x / 100), 'r', label='Experiment')
plt.legend()
plt.savefig('results/Gas_Profile_H2.png')

#add the experimental results for the Ar profile

df = pd.read_csv('data/Ar.csv', names=['X', 'Y'])
plt.figure(3)
plt.plot(df['X'], df['Y'].transform(lambda x: x / 100), 'r', label='Experiment')
plt.legend()
plt.savefig('results/Gas_Profile_Ar.png')

#add the experimental results for the H20 profile

df = pd.read_csv('data/H20.csv', names=['X', 'Y'])
plt.figure(4)
plt.plot(df['X'], df['Y'].transform(lambda x: x / 100), 'r', label='Experiment')
plt.legend()
plt.savefig('results/Gas_Profile_H2O.png')

#add the experimental results for the CH4 profile

df = pd.read_csv('data/CH4.csv', names=['X', 'Y'])
plt.figure(5)
plt.plot(df['X'], df['Y'].transform(lambda x: x / 100), 'r', label='Experiment')
plt.legend()
plt.savefig('results/Gas_Profile_CH4.png')

#add the experimental results for the CO profile

df = pd.read_csv('data/CO.csv', names=['X', 'Y'])
plt.figure(6)
plt.plot(df['X'], df['Y'].transform(lambda x: x / 100), 'r', label='Experiment')
plt.legend()
plt.savefig('results/Gas_Profile_CO.png')

plt.show()

