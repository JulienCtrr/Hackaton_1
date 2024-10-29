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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
df=pd.read_csv('data/bonheur.csv', index_col=['Country name','year'], decimal=',')
df.head(5)

# %% [markdown]
# # La guerre rend-elle malheureux ??

# %%
df.loc[('Ukraine',)]

# %% [markdown]
# je voulais m'appuyer sur le conflit Ukraine-Russie mais les données ne sont pas assez récentes, je vais donc m'appuyer sur la guerre civile Syrienne qui a débuté en 2011.

# %%
df_syrie=df.loc[('Syria',)]
df_syrie

# %%
plt.plot(df_syrie.index, df_syrie["Life Ladder"])

# %% [markdown]
# # Lien entre la note de bonheur et le système de notation à l'école

# %%
df.xs(2022, level='year')['Life Ladder'].mean()

# %% [markdown]
# en moyenne les gens se considèrent un peu trop heureux (il faudrait une moyenne à 5). Mais on voudrait un moyenne à 5 car en france on considère que la note moyenne est de 5/10, voyons si le système de notation à l'école influe sur la réponse que donnent les gens.

# %%
df.loc[('France',2022),]['Life Ladder'].mean()

# %%
df.loc[('China',)]

# %%
notation={'Albania':5.5,'Algeria':5,'Argentina':4.5,'Brazil':5,'Colombia':6,'France':5, 'Japan':6, 'Mexico':6.2,'China':6.7,'Greece':4,'Italy':6,'Turkiye':7,'Ukraine':3.5}
bonheur=[df.loc[(pays,),'Life Ladder'].mean() for pays in notation.keys()]
#/10+df.loc[(pays,),'Social support'].mean()+df.loc[(pays,),'Freedom to make life choices'].mean()+df.loc[(pays,),'Perceptions of corruption'].mean()+df.loc[(pays,),'Positive affect'].mean()+df.loc[(pays,),'Perceptions of corruption'].mean())/6*10

# %%
plt.plot(notation.keys(),notation.values(), linestyle=' ', marker='x', label='quelle note pour valider')
plt.plot(notation.keys(),bonheur, linestyle=' ', marker='x', label='moyenne des notes données')
plt.legend()

# %%
plt.scatter(notation.values(),bonheur)

# %%

# %%
