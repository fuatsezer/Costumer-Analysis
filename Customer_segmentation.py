import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%% import data
df = pd.read_csv("WA_Fn-UseC_-Marketing-Customer-Value-Analysis.csv")
#%% Tabulate your data
# Cross-tabbing
cross_tab = pd.crosstab(df["State"],df["Sales Channel"],normalize='index')
cross_tab2 = pd.crosstab(df["State"],df["Sales Channel"],normalize='columns')
#%%
df=pd.get_dummies(df,columns=["State","Response","Coverage","Education",
                              "EmploymentStatus","Gender","Location Code",
                              "Marital Status","Policy Type","Policy","Renew Offer Type",
                              "Sales Channel","Vehicle Class","Vehicle Size"])
#%%
pd.DataFrame.to_csv(df,"Customer_Segmentation.csv")