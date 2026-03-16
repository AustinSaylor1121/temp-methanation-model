import pandas as pd
import matplotlib.pyplot as plt


def plot_CO2_profiles (df, mechanism_number,figure_number):

    plt.figure(figure_number)

    min_dist = 25
    max_dist = 95

    filtered = df[(df["Distance (mm)"] >= min_dist) & (df["Distance (mm)"] <= max_dist)]    
    plt.plot(filtered['Distance (mm)'].transform(lambda x: x - 35), filtered['CO2(2)'],
             'b',
             linewidth=0.5, 
             label=f'{mechanism_number}')

    plt.title('Gas Profile of CO2')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 0.7])

def plot_H2_profiles (df, mechanism_number,figure_number):

    plt.figure(figure_number)

    min_dist = 25
    max_dist = 95

    filtered = df[(df["Distance (mm)"] >= min_dist) & (df["Distance (mm)"] <= max_dist)]    
    plt.plot(filtered['Distance (mm)'].transform(lambda x: x - 35), filtered['H2(4)'],
             'b',
             linewidth=0.5, 
             label=f'{mechanism_number}')

    plt.title('Gas Profile of H2')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 0.7])

def plot_Ar_profiles (df, mechanism_number,figure_number):

    plt.figure(figure_number)

    min_dist = 25
    max_dist = 95

    filtered = df[(df["Distance (mm)"] >= min_dist) & (df["Distance (mm)"] <= max_dist)]    
    plt.plot(filtered['Distance (mm)'].transform(lambda x: x - 35), filtered['Ar'],
             'b',
             linewidth=0.5, 
             label=f'{mechanism_number}')

    plt.title('Gas Profile of Ar')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 0.7])

def plot_H2O_profiles (df, mechanism_number,figure_number):

    plt.figure(figure_number)

    min_dist = 25
    max_dist = 95

    filtered = df[(df["Distance (mm)"] >= min_dist) & (df["Distance (mm)"] <= max_dist)]    
    plt.plot(filtered['Distance (mm)'].transform(lambda x: x - 35), filtered['H2O(3)'],
             'b',
             linewidth=0.5, 
             label=f'{mechanism_number}')

    plt.title('Gas Profile of H2O')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 0.7])

def plot_CH4_profiles (df, mechanism_number,figure_number):

    plt.figure(figure_number)

    min_dist = 25
    max_dist = 95

    filtered = df[(df["Distance (mm)"] >= min_dist) & (df["Distance (mm)"] <= max_dist)]    
    plt.plot(filtered['Distance (mm)'].transform(lambda x: x - 35), filtered['CH4(1)'],
             'b',
             linewidth=0.5, 
             label=f'{mechanism_number}')

    plt.title('Gas Profile of CH4')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 0.7])
    
def plot_CO_profiles (df, mechanism_number,figure_number):

    plt.figure(figure_number)

    min_dist = 25
    max_dist = 95

    filtered = df[(df["Distance (mm)"] >= min_dist) & (df["Distance (mm)"] <= max_dist)]    
    plt.plot(filtered['Distance (mm)'].transform(lambda x: x - 35), filtered['CO(5)'],
             'b',
             linewidth=0.5, 
             label=f'{mechanism_number}')

    plt.title('Gas Profile of CO')
    plt.xlabel('Distance (mm)')
    plt.ylabel('Mole Fraction')
    plt.ylim([0, 0.02])


