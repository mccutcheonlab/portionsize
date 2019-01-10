# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:15:41 2018

@author: James Rig
"""
import os
os.chdir(os.path.dirname(__file__))
cwd = os.getcwd()

import sys
sys.path.insert(0,cwd)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import JM_general_functions as jmf
import JM_custom_figs as jmfig

import portionsize_figs as psfig


usr = jmf.getuserhome()

savefigs=False
statson=False

datafolder = usr + '\Dropbox\Publications in Progress\Pinder_portionsize\\'
savefolder = usr + '\Dropbox\Publications in Progress\Pinder_portionsize\Figs\\'

myers_xlfile = datafolder + 'myers_data.xlsx'

jmf.metafilemaker(myers_xlfile, 'myers1', sheetname='expt1')
df = pd.read_csv('myers1.csv', index_col='rat')

f = psfig.ps_myers_fig(df, ['Small', 'Large'])

if savefigs: f.savefig(savefolder + 'myers_expt1.pdf')

if statson:
    print('Paired t-test for Myers experiment # 1')
    psfig.ps_ttest_paired(df, 'Small', 'Large')


jmf.metafilemaker(myers_xlfile, 'myers2', sheetname='expt2')
df = pd.read_csv('myers2.csv', index_col='rat')


f = psfig.ps_myers_fig(df, ['Medium', 'Large'])

if savefigs: f.savefig(savefolder + 'myers_expt2.pdf')

f = psfig.ps_myers_figB(df, ['Small', 'Medium', 'Large'])

if savefigs: f.savefig(savefolder + 'myers_expt2B.pdf')

if statson:
    print('Paired t-test for Myers experiment # 2')
    psfig.ps_ttest_paired(df, 'Medium', 'Large')

mccutcheon_xlfile = datafolder + 'mccutcheon_data.xlsx'

jmf.metafilemaker(mccutcheon_xlfile, 'mcc1', sheetname='mcc_expt1')
df = pd.read_csv('mcc1.csv', index_col='rat')
cols = list(df.columns)

f = psfig.ps_mcc1_fig(df, cols)

if savefigs: f.savefig(savefolder + 'mcc_expt1.pdf')

if statson:
    print('One-way ANOVA for McCutcheon expt #1')
    cols_for_stats = cols[2:]
    psfig.ps_ANOVA_1way(df, cols_for_stats,
                        usr + '\\Documents\\GitHub\\portionsize\\df_mcc_expt1.csv')


jmf.metafilemaker(mccutcheon_xlfile, 'mcc2', sheetname='mcc_expt2')
df = pd.read_csv('mcc2.csv', index_col='rat')
cols = list(df.columns)

f = psfig.ps_mcc2_fig(df, cols)

if savefigs: f.savefig(savefolder + 'mcc_expt2.pdf')

if statson:
    print('One-way ANOVA for McCutcheon expt #2')
    psfig.ps_ANOVA_1way(df, cols,
                        usr + '\\Documents\\GitHub\\portionsize\\df_mcc_expt2.csv')

jmf.metafilemaker(mccutcheon_xlfile, 'mcc3', sheetname='mcc_expt3')
df = pd.read_csv('mcc3.csv', index_col='rat')
cols = list(df.columns)

f = psfig.ps_mcc3_fig(df, cols)

if savefigs: f.savefig(savefolder + 'mcc_expt3.pdf')

if statson:
    print('One-way ANOVA for McCutcheon expt #3')
    psfig.ps_ANOVA_1way(df, cols,
                        usr + '\\Documents\\GitHub\\portionsize\\df_mcc_expt3.csv')