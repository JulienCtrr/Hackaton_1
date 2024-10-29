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
from scipy.stats import linregress

# %% [markdown]
# L'objectif est de nous intéresser à la perception de la corruption selon différents critères

# %%
df = pd.read_csv("data/bonheur.csv", index_col=["Country name"], decimal = ",")
df.head()

# %%
espagne= df.loc[("Spain")]
portugal = df.loc[("Portugal")]
argentine = df.loc[("Argentina")]
portugal.head()

# %%

# %%
plt.plot( espagne["year"],espagne["Perceptions of corruption"])
plt.plot( portugal["year"],portugal["Perceptions of corruption"])
plt.plot( argentine["year"],argentine["Perceptions of corruption"]);

# %%
la il y a des problemes car les donnees sont des objets et pas des float


# %%

# %% [markdown]
# On construit une fonction qui permet de comparer l'évolution de la perception de la corruption entre deux pays

# %%
def evol_corruption(country1, country2):
    c1=df.loc[(country1)]
    c2=df.loc[(country2)]
    plt.plot(c1["year"], np.array(c1["Perceptions of corruption"]).astype("float"), label = country1)
    plt.plot(c2["year"], np.array(c2["Perceptions of corruption"]).astype("float"), label = country2)
    plt.legend()


# %%
evol_corruption("Spain", "France")


# %%
def relation_liberte_corruption(df):
    plt.scatter(np.array(df["Freedom to make life choices"]).astype("float"), np.array(df["Perceptions of corruption"]).astype("float"), s=10, alpha = 0.40)
    plt.ylabel("Perception de la corruption")
    plt.xlabel("Liberté")
    plt.title("Perception de la corruption en fonction de la liberté de faire des choix");

relation_liberte_corruption(df)


# %% [markdown]
# On retrouve un résultat intéressant. En effet, on serait tentés de penser que plus un pays présente des libertés de choix, plus la corruption du pays serait basse et donc avec elle la perception de la corruption. C'est à dire on s'attendrait à une corrélation négative.
# Si bien on observe une légère tendance, la grande majorité des pays, indépendamment de ses libertés, perçoivent un très grand niveau de corruption.
# Or on observe aussi que pour les pays les plus autoritaires, la perception de la corruption fait unanimité.

# %% [markdown]
# Un autre aspect intéressant est voir si les pays les plus riches sont les moins corruptes:

# %%
def relation_pib_corruption(df):
    plt.scatter(np.array(df["Log GDP per capita"]).astype("float"), np.array(df["Perceptions of corruption"]).astype("float"), s=10, alpha = 0.40)
    plt.ylabel("Perception de la corruption")
    plt.xlabel("PIB")
    plt.title("Perception de la corruption en fonction du PIB");

relation_pib_corruption(df)


# %% [markdown]
# On retrouve des resultats qui ont une tendance similaire, un grand PIB semble être une condition nécessaire mais pas suffisante pour avoir une basse perception de la corruption

# %%
def relation_joie_corruption(df):
    plt.scatter(np.array(df["Life Ladder"]).astype("float"), np.array(df["Perceptions of corruption"]).astype("float"), s=10, alpha = 0.40)
    plt.ylabel("Perception de la corruption")
    plt.xlabel("Bonheur")
    plt.title("Perception de la corruption en fonction du bonheur");

relation_joie_corruption(df)


# %% [markdown]
# On trouve donc une nouvelle implication. Où il y a une basse perception de la corruption il y a en grande majorité un grand indice de bonheur. Une basse perception de la corruption est une condition suffisante pour être heureux

# %%
def relation_annee_corruption(df):
    x=df["year"].astype("float").values
    y=df["Perceptions of corruption"].astype("float").values
    plt.scatter(x,y, s=10, alpha = 0.10)
    plt.ylabel("Perception de la corruption")
    plt.xlabel("Année")
    plt.title("Évolution de la perception de la corruption");
    
relation_annee_corruption(df)

# %%

pays=df.index.values
def plotevol(coutry):
    c1=df.loc[(coutry)]
    plt.plot(c1["year"], np.array(c1["Perceptions of corruption"]).astype("float"))
for i in pays:
    plotevol(i)


# %%
def relation_vie_corruption(df):
    y=df["Healthy life expectancy at birth"].astype("float").values
    x=df["Perceptions of corruption"].astype("float").values
    plt.scatter(x,y, s=10, alpha = 0.10)
    plt.ylabel("Espérance de vie")
    plt.xlabel("Perception de la corruption")
    plt.title("Espérance de vie en fonction de la corruption");
    
relation_vie_corruption(df)

# %% [markdown]
# À nouveau des conclusions qu'on peut tirer, pas forcément vraies, mais qui suivent les données. Une petite perception de la corruption est une condition suffisante pour une longue espérance de vie

# %%
df["Perceptions of corruption"].describe()

# %%
df[df["Perceptions of corruption"]<0.036]
