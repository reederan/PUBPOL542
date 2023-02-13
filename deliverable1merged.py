#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:40:14 2023

@author: annareeder
"""

#load pandas
import pandas as pd 

#read files
gitCloudRepo='https://github.com/Drops-of-Jupyter/PUBPOL542/raw/main/'
fileName1='distribution-human-rights-vdem.csv'
fileName2='infectious-disease-death-rates.csv'
fileName3='water-and-sanitation.csv'
humrightscsv=pd.read_csv(gitCloudRepo + fileName1)
infdeathscsv=pd.read_csv(gitCloudRepo + fileName2)
sanitationcsv=pd.read_csv(gitCloudRepo + fileName3)

## Human rights dataset
# Remove unneeded columns
humrightscsv.columns
bye=[1,4]
humrightscsv.drop(columns=humrightscsv.columns[bye],inplace=True)
humrightscsv.columns

# Filter rows to years 2015 - 2019
humrightscsv = humrightscsv[(humrightscsv['Year'] >= 2015) & (humrightscsv['Year'] <= 2019)]
humrightscsv.head()

humrightscsv.columns.str.replace(pat="civ_libs_vdem_owid", 
                                 repl="VDEM", 
                                 regex=False)
humrightscsv.columns=humrightscsv.columns.str.replace("civ_libs_vdem_owid",
                                                      "VDEM",
                                                      regex=False)
humrightscsv.columns

humrightscsv.columns.str.replace(pat="Entity", 
                                 repl="Country", 
                                 regex=False)
humrightscsv.columns=humrightscsv.columns.str.replace("Entity",
                                                      "Country",
                                                      regex=False)

humrightscsv=humrightscsv.reset_index(drop=True)
humrightscsv.head()

humrightscsv.iloc[:,:2]

# Sanitations dataset
sanitationcsv.head()
sanitationcsv = sanitationcsv[[
    'Entity',
    'Year',
    'Access to limited drinking water',
    'Access to limited sanitation services',
]]

sanitationcsv.head()
sanitationcsv = sanitationcsv[(sanitationcsv['Year'] == 2019)]
sanitationcsv.head()
sanitationcsv=sanitationcsv.reset_index(drop=True)
sanitationcsv.head()
sanitationcsv.columns.str.replace(pat="Access to limited drinking water", 
                                  repl="LDW", 
                                  regex=False)
sanitationcsv.columns=sanitationcsv.columns.str.replace("Access to limited drinking water",
                                                        "LDW",
                                                        regex=False)
sanitationcsv.columns.str.replace(pat="Access to limited sanitation services", 
                                  repl="LSS", 
                                  regex=False)
sanitationcsv.columns=sanitationcsv.columns.str.replace("Access to limited sanitation services",
                                                        "LSS",
                                                        regex=False)
sanitationcsv.columns.str.replace(pat="Entity", 
                                  repl="Country", 
                                  regex=False)
sanitationcsv.columns=sanitationcsv.columns.str.replace("Entity",
                                                        "Country",
                                                        regex=False)
sanitationcsv.head()
sanitationcsv.iloc[:,:2]
infdeathscsv.head()
infdeathscsv = infdeathscsv[(infdeathscsv['Year'] >= 2015) & (infdeathscsv['Year'] <= 2019)]
infdeathscsv.head()
infdeathscsv.columns
bye=[1]
infdeathscsv.drop(columns=infdeathscsv.columns[bye],inplace=True)
infdeathscsv.columns
infdeathscsv.columns.str.replace(pat="Deaths - Infectious diseases - OWID - Sex: Both - Age: Age-standardized (Rate)", 
                                 repl="Death Rate", 
                                 regex=False)
infdeathscsv.columns=infdeathscsv.columns.str.replace("Deaths - Infectious diseases - OWID - Sex: Both - Age: Age-standardized (Rate)",
                                                      "Death Rate",
                                                      regex=False)
infdeathscsv.columns.str.replace(pat="Entity", 
                                 repl="Country", 
                                 regex=False)
infdeathscsv.columns=infdeathscsv.columns.str.replace("Entity",
                                                      "Country",
                                                      regex=False)
infdeathscsv.columns
infdeathscsv=infdeathscsv.reset_index(drop=True)
infdeathscsv.head()
" Afghanistan ".strip()


infdeathscsv.head()
sanitationcsv.head()
humrightscsv.head()

###ATTEMPTING TO MERGE

infdeathscsv.info()
sanitationcsv.info()
humrightscsv.info()

infdeathscsv.shape,sanitationcsv.shape

infdeathscsv.merge(sanitationcsv).shape

infdeaths_sanitation=infdeathscsv.merge(sanitationcsv)

infdeaths_sanitation.shape,humrightscsv.shape

merged=infdeaths_sanitation.merge(humrightscsv)

merged.info()

merged.head()

merged

merged


merged.to_csv("mergeddeliverable2.csv", index=False)




