# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 16:04:51 2025

@author: Sheena Cumberbatch
"""

AzCounties = ["Apache","La Paz","Maricopa","Pima","Pinal","Santa Cruz","Yuma"]
PediatricAsthma = [1344,206,81703,16534,8381,995,4195]
ParticlePollution = [0,.3,6.3,5.2,1.5,2.7,3.0]

#%%
import numpy as np
np.median(PediatricAsthma)
print(np.median(PediatricAsthma)) #4195

np.median(ParticlePollution)
print(np.median(ParticlePollution)) #2.1

#%%
prompt = "Enter an Arizona County to learn about Pediatric Asthma in that county:\n"
prompt += "If you wish to learn about Particle pollution type 'other': "

pollution_prompt = "\nEnter an Arizona County to learn about Particle Pollution in that county or type 'Done' to exit: \n"

county = input(prompt)
while county.lower() != "other":
    found = False
    for i, Az_county in enumerate(AzCounties):
        if county.lower() == Az_county.lower():
            asthma = PediatricAsthma[i]
            if asthma > 4195:
                print(f"\n {county} county is higher than the median for Pediatriac Asthma with a number of {asthma}\n")
               
            elif asthma == 4195:
                print(f" \n{county} county is the median for Pediatriac Asthma with a number of {asthma}\n")
            else:
                print(f"\n{county} county is lower than the median for Pediatriac Asthma with a number of {asthma}\n")
            found = True
            break
    if not found:
            print("\nThis county is not found.\n")

    county = input(prompt)

county = input(pollution_prompt)


while county.lower() != "done":
    found = False
    for i, az_county in enumerate(AzCounties):
        if county.lower() == az_county.lower():
            pollution = ParticlePollution[i]
            if pollution >= 2.1:
                print(f"\n {county} county has a higher median for particle pollution cases with a number of "+str(pollution))
            else:
                print(f"\n{county} county has a lower median for particle pollution cases with a number of "+str(pollution))
            found = True
            break 
    if not found: 
        print("\nThis county is not in our system.\n")
    county = input(pollution_prompt)
print("\n Thank you for using this database.\n")
        
