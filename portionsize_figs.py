# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:27:29 2018

@author: James Rig
"""
import JM_general_functions as jmf
import JM_custom_figs as jmfig

import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy import stats

from subprocess import PIPE, run

Rscriptpath = 'C:\\Program Files\\R\\R-3.5.1\\bin\\Rscript'

mpl.rcParams['savefig.transparent'] = True

color_scheme = ['xkcd:light grey', 'xkcd:baby blue', 'xkcd:azure']

def ps_myers_fig(df, keys):
    data = [df[keys[0]], df[keys[1]]]
    
    f, ax = plt.subplots(figsize=(3,3))
    f.subplots_adjust(left=0.2)
    
    colors = [color_scheme[1], color_scheme[2]]
    
    jmfig.barscatter(data,
                     paired=True,
                     barwidth = .7,
                     barfacecoloroption = 'individual',
                     barfacecolor = colors,
                     barlabels = keys,
                     ax=ax)
#    ax.set_xlim([0.2,2.8])
    ax.set_ylabel('Food consumed (g)')
    ax.set_yticks([0,10,20,30])
    
    return f

def ps_myers_figB(df, keys):
    data = [df[keys[0]], df[keys[1]], df[keys[2]]]
    
    f, ax = plt.subplots(figsize=(3,3))
    f.subplots_adjust(left=0.2)
    
    colors = color_scheme
    
    jmfig.barscatter(data,
                     paired=True,
                     barwidth = .7,
                     barfacecoloroption = 'individual',
                     barfacecolor = colors,
                     barlabels = keys,
                     ax=ax)
#    ax.set_xlim([0.2,2.8])
    ax.set_ylabel('Food consumed (g)')
    ax.set_yticks([0,10,20,30])
    
    return f
    
def ps_mcc1_fig(df, keys):
    data = []
    for key in keys:
        data.append(df[key])
    
    f, ax = plt.subplots(figsize=(5,3))
    f.subplots_adjust(left=0.1, bottom=0.2)

    colors = [color_scheme[0]]*2 + [color_scheme[2]]*5
    print(colors)
    
    jmfig.barscatter(data,
                     paired=True,
                     barwidth = .8,
                     barfacecoloroption = 'individual',
                     barfacecolor = colors,
                     barlabels = keys,
                     ax=ax)

    ax.set_ylabel('Pellets consumed')
    ax.set_yticks([0,10,20,30])
    ax.set_xlabel('Number of pellets given')
    ax.xaxis.set_label_coords(0.5, -0.13)
    
    return f

def ps_mcc2_fig(df, keys):
    data = []
    for key in keys:
        data.append(df[key])
    
    f, ax = plt.subplots(figsize=(3, 3))
    f.subplots_adjust(left=0.2, bottom=0.2)

    colors = [color_scheme[2]]*4
    
    jmfig.barscatter(data,
                     paired=True,
                     barwidth = .8,
                     barfacecoloroption = 'individual',
                     barfacecolor = colors,
                     barlabels = keys,
                     ax=ax)

    ax.set_ylabel('Peanut butter consumed (g)')
    ax.set_yticks([0,1,2,3])
    ax.set_xlabel('Amount of peanut butter given (g)')
    ax.xaxis.set_label_coords(0.5, -0.13)
    
    return f

def ps_mcc3_fig(df, keys):
    data = []
    for key in keys:
        data.append(df[key])
    
    f, ax = plt.subplots(figsize=(3,3))
    f.subplots_adjust(left=0.2, bottom=0.2)

    colors = [color_scheme[2]]*4
    
    jmfig.barscatter(data,
                     paired=True,
                     barwidth = .8,
                     barfacecoloroption = 'individual',
                     barfacecolor = colors,
                     barlabels = keys,
                     ax=ax)

    ax.set_ylabel('Chow consumed (g)')
#    ax.set_yticks([0,1,2,3])
    ax.set_xlabel('Amount of chow given (g)')
    ax.xaxis.set_label_coords(0.5, -0.13)
    
    return f

def ps_ttest_paired(df, key1, key2):
    result = stats.ttest_rel(df[key1], df[key2])
    print(result, '\n')
    return result

def extractandstack(df, cols_to_stack, new_cols=[]):
    new_df = df.loc[:,cols_to_stack]
    new_df = new_df.stack()
    new_df = new_df.to_frame()
    new_df.reset_index(inplace=True)

    if len(new_cols) > 1:
        try:
            new_df.columns = new_cols
        except ValueError:
            print('Wrong number of labels for new columns given as argument.')
            
    return new_df

def ps_ANOVA_1way(df, cols, csvfile):   
    df = extractandstack(df, cols, new_cols=['rat', 'amountgiven', 'value'])
    df.to_csv(csvfile)
    result = run([Rscriptpath, "--vanilla", "ps_ANOVA_1way.R", csvfile], stdout=PIPE, stderr=PIPE, universal_newlines=True)
    print(result.returncode, result.stderr, result.stdout)
    return result