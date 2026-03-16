import pandas as pd
import matplotlib.pyplot as plt


def plot_CO2_profiles (df, mechanism_number):


    plt.plot(df['Distance (mm)'], df['CO2(2)'],linewidth=0.5, label=f'{mechanism_number}')

    plt.title('Gas Profile of CO2')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 1])
