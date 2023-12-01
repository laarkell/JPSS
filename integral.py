import spectral.io.envi as envi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# print(arr.info())
VIIRS = pd.read_excel('/home/GES/larkell/JPSS/VIIRS/J3 GLAMR RSR.xlsx')
print("Data sucessfully imported")

# Cleanup VIIRS Data
VIIRS = np.array(VIIRS)
VIIRS = VIIRS[1:,:]
# VIIRS = VIIRS[:,1:32] #chop off first wrong row and only keep first 32
BandM1Wave = VIIRS[:230,1:3]
BandM2Wave = VIIRS[:166,3:5]
BandM3Wave = VIIRS[:186,5:7]
BandM4Wave = VIIRS[:245,7:9]
BandM5Wave = VIIRS[:198,9:11]
BandM6Wave = VIIRS[:121,11:13]
BandM7Wave = VIIRS[:192,13:15]
BandM8Wave = VIIRS[:113,15:17]
BandM9Wave = VIIRS[:72,17:19]
BandM10Wave = VIIRS[:283,19:21]
BandM11Wave = VIIRS[:203,21:23]
BandI1Wave = VIIRS[:382,23:25]
BandI2Wave = VIIRS[:199,25:27]
BandI3Wave = VIIRS[:283,27:29]
BandDNBLGSWave = VIIRS[:1110,29:31]
BandDNBMGSWave = VIIRS[:750,31:33]
# print(BandM1Wave.shape)

# combine all potential bands
AllBands = [BandM1Wave, BandM2Wave, BandM3Wave, BandM4Wave, BandM5Wave, BandM6Wave, BandM7Wave, BandI1Wave, BandI2Wave]

# variables that can be changed:
CUTOFF = 0.2 # to limit the bands to 0.5 so they dont go to 0

# get rid of all the ones below 0.5 bc they dont matter
savex = np.empty(0, dtype = int)
for y in range(len(AllBands)):
    for x in range(len(AllBands[y])):
        if AllBands[y][x,1] <= CUTOFF:
            savex = np.append(savex,x)
    AllBands[y] = np.delete(AllBands[y],savex,0)
    savex = np.empty(0, dtype = int)

# .............OPTION 1 ............
# scale so average is 1 w/ integral
for x in range(len(AllBands)):
    IntSum = np.trapz(AllBands[x][:,1], AllBands[x][:,0])
    diff = AllBands[x][len(AllBands[x])-1,0] - AllBands[x][0,0]
    scalar = IntSum/diff
    AllBands[x][:,1] = AllBands[x][:,1]*(1/scalar)
    print(1/scalar)

# .............OPTION 2 .............
# scale the values to be average = 1
# for x in range(len(AllBands)):
#     avg = np.average(AllBands[x][:,1])
#     AllBands[x][:,1] = AllBands[x][:,1]*(1/avg)
#     print(avg)
# # print(AllBands[0].shape)