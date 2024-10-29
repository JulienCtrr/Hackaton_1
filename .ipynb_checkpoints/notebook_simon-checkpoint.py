# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('data/bonheur.csv', index_col = ['Country name', 'year'], decimal = ',')
df.head(5)


# %% [markdown]
# Mon but est de montrer l'impact de la richesse d'un pays sur les differents parametres

# %%
def largentfaitlebonheur() :
    tableau = df.dropna(subset = ['Life Ladder', 'Log GDP per capita'])
    xtempo = tableau['Log GDP per capita'].astype(float).values
    ytempo= tableau['Life Ladder'].astype(float).values
    order = np.argsort(xtempo)
    x = xtempo[order]
    y = ytempo[order]
    a, b = np.polyfit(x, y, 1)
    y_pred = a*x + b
    residus = y - y_pred
    std_residus = np.std(residus)
    intervalle_confiance = 1.96 * std_residus
    plt.scatter(x, y, s = 10, alpha = 0.5)
    plt.plot(x, y_pred, color = 'red')
    plt.fill_between(x, y_pred - intervalle_confiance, y_pred + intervalle_confiance, color = 'green', alpha = 0.3)
    plt.xlabel('Log GDP per capita')
    plt.ylabel('Life Ladder')
    plt.title('Evolution du bonheur moyen des individus en fonction du PIB moyen par habitant')
    plt.grid()
    plt.show()

largentfaitlebonheur()


# %%
def largentfaitlaliberte() :
    tableau = df.dropna(subset = ['Log GDP per capita', 'Freedom to make life choices'])
    xtempo = tableau['Log GDP per capita'].astype(float).values
    ytempo= tableau['Freedom to make life choices'].astype(float).values
    order = np.argsort(xtempo)
    x = xtempo[order]
    y = ytempo[order]
    a, b = np.polyfit(x, y, 1)
    y_pred = a*x + b
    residus = y - y_pred
    std_residus = np.std(residus)
    intervalle_confiance = 1.96 * std_residus
    plt.scatter(x, y, s = 10, alpha = 0.5)
    plt.plot(x, y_pred, color = 'red')
    plt.fill_between(x, y_pred - intervalle_confiance, y_pred + intervalle_confiance, color = 'green', alpha = 0.3)
    plt.xlabel('Log GDP per capita')
    plt.ylabel('Freedom to make life choices')
    plt.title('Evolution de la liberté des individus en fonction du PIB moyen par habitant')
    plt.grid()
    plt.show()

largentfaitlaliberte()


# %%
def largentfaitlagenerosite() :
    tableau = df.dropna(subset = ['Generosity', 'Log GDP per capita'])
    xtempo = tableau['Log GDP per capita'].astype(float).values
    ytempo= tableau['Generosity'].astype(float).values
    order = np.argsort(xtempo)
    x = xtempo[order]
    y = ytempo[order]
    a, b, c, d= np.polyfit(x, y, 3)
    y_pred = a*x**3 + b*x**2 + c*x + d
    residus = y - y_pred
    std_residus = np.std(residus)
    intervalle_confiance = 1.96 * std_residus
    plt.scatter(x, y, s = 10, alpha = 0.5)
    plt.plot(x, y_pred, color = 'red')
    plt.fill_between(x, y_pred - intervalle_confiance, y_pred + intervalle_confiance, color = 'green', alpha = 0.3)
    plt.xlabel('Log GDP per capita')
    plt.ylabel('Generosity')
    plt.title('Evolution de la générosité moyenne des individus en fonction du PIB moyen par habitant')
    plt.xlim(6.5,12)
    plt.ylim(-0.6, 0.6)
    plt.grid()
    plt.show()

largentfaitlagenerosite()


# %%
def largentfaitlasante() :
    tableau = df.dropna(subset = ['Log GDP per capita', 'Healthy life expectancy at birth'])
    xtempo = tableau['Log GDP per capita'].astype(float).values
    ytempo= tableau['Healthy life expectancy at birth'].astype(float).values
    order = np.argsort(xtempo)
    x = xtempo[order]
    y = ytempo[order]
    a, b= np.polyfit(x, y, 1)
    y_pred = a*x + b
    residus = y - y_pred
    std_residus = np.std(residus)
    intervalle_confiance = 1.96 * std_residus
    plt.scatter(x, y, s = 10, alpha = 0.5)
    plt.plot(x, y_pred, color = 'red')
    plt.fill_between(x, y_pred - intervalle_confiance, y_pred + intervalle_confiance, color = 'green', alpha = 0.3)
    plt.xlabel('Log GDP per capita')
    plt.ylabel('Generosity')
    plt.title('Esperance de vie saine moyenne des individus en fontion du PIB par habitant moyen')
    plt.grid()
    plt.show()

largentfaitlasante()


# %%
def largentfaitlespotos() :
    tableau = df.dropna(subset = ['Log GDP per capita', 'Social support'])
    xtempo = tableau['Log GDP per capita'].astype(float).values
    ytempo= tableau['Social support'].astype(float).values
    order = np.argsort(xtempo)
    x = xtempo[order]
    y = ytempo[order]
    a, b= np.polyfit(x, y, 1)
    y_pred = a*x + b
    residus = y - y_pred
    std_residus = np.std(residus)
    intervalle_confiance = 1.96 * std_residus
    plt.scatter(x, y, s = 10, alpha = 0.5)
    plt.plot(x, y_pred, color = 'red')
    plt.fill_between(x, y_pred - intervalle_confiance, y_pred + intervalle_confiance, color = 'green', alpha = 0.3)
    plt.xlabel('Log GDP per capita')
    plt.ylabel('Social support')
    plt.title('Support social moyen des individus en fontion du PIB par habitant moyen')
    plt.grid()
    plt.show()

largentfaitlespotos()
