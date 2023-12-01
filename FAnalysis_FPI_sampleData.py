import numpy as np
import matplotlib.pyplot as plt
import spectral.io.envi as envi
import pandas as pd

img = pd.read_excel('/home/GES/larkell/JPSS/VIIRS/0a3Lmax_FPI1_DemoUnitxlsm.xlsm')
VIIRS = pd.read_excel('/home/GES/larkell/JPSS/VIIRS/J3 GLAMR RSR.xlsx')
print("Data sucessfully imported")

#process FPI data
img = np.array(img)
img = img[11:,:] #chop off the top
wavelength = img[:,0]
FPI_lvl1 = img[:,2]
Demo_LED = img[:,3]
Demo_QTH = img[:,4]
Lmax = img[:,11]

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
AllBands = [BandM1Wave, BandM2Wave, BandM3Wave, BandM4Wave, BandM5Wave, BandM6Wave, BandM7Wave, BandM8Wave, BandM9Wave, BandM10Wave, BandM11Wave, BandI1Wave, BandI2Wave, BandI3Wave, BandDNBLGSWave, BandDNBMGSWave]

# # variables that can be changed:
# CUTOFF = 0.2 # to limit the bands to 0.5 so they dont go to 0

# # get rid of all the ones below 0.5 bc they dont matter
# savex = np.empty(0, dtype = int)
# for y in range(len(AllBands)):
#     for x in range(len(AllBands[y])):
#         if AllBands[y][x,1] <= CUTOFF:
#             savex = np.append(savex,x)
#     AllBands[y] = np.delete(AllBands[y],savex,0)
#     savex = np.empty(0, dtype = int)

# scale so average is 1 w/ integral
# IntSum = np.trapz(BandM2Wave[:,1], BandM2Wave[:,0])
# diff = BandM2Wave[len(BandM2Wave)-1,0] - BandM2Wave[0,0]
# scalar = IntSum/diff

# # scale the values to be average = 1
# for x in range(len(AllBands)):
#     avg = np.average(AllBands[x][:,1])
#     AllBands[x][:,1] = AllBands[x][:,1]*(1/avg)
#     #print(1/avg)
# # print(AllBands[0].shape)

# limit wavelength and pixels to the specific VIIRS bands!
# base = []
# wave = []
# baseNew = []
# waveNew = []
# for y in range(len(AllBands)):
#     for x in range(len(wavelength)):
#         if wavelength[x] >= AllBands[y][0,0]:
#             if wavelength[x] <= AllBands[y][len(AllBands[y])-1,0]:
#                 baseNew.append(pixelList[x])
#                 waveNew.append(wavelength[x])
#     base.append(baseNew)
#     wave.append(waveNew)
#     baseNew = []
#     waveNew = []

# Correlate the wavelength from the pixel data to the closest data point wavelength in the 
# VIIRS data and then multiply them to scale the pixel data to the pattern of the VIIRS
# baseScaled = []
# waveScaled = []
# list = []
# oldDiff = 1000
# for y in range(len(wave)):
#     for x in range(len(wave[y])):
#         for i in range(len(AllBands[y])):
#             diff = abs(wave[y][x]-AllBands[y][i,0]) # compare the all bands wavelength to pixel wavelength to find the closest one
#             if diff < oldDiff: # only save best one
#                 scaledBase = base[y][x]*AllBands[y][i,1]
#                 oldDiff = diff
#         list.append(scaledBase)
#         oldDiff = 1000
#     baseScaled.append(list) #save into new list to replace base
#     list = []


#plotting data
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Example FPI Data with VIIRS bands')
# plt.plot(wavelength, pixelList, label = 'Img Circle Data')
# plt.plot(wave[0], base[0], label='M1')
# plt.plot(wave[1], base[1], label='M2')
# plt.plot(wave[2], base[2], label='M3')
# plt.plot(wave[3], base[3], label='M4')
# plt.plot(wave[4], base[4], label='M5')
# plt.plot(wave[5], base[5], label='M6')
# plt.plot(wave[6], base[6], label='M7')
# plt.plot(wave[7], base[7], label='I1')
# plt.plot(wave[8], base[8], label='I2')
# plt.plot(wave[0], baseScaled[0], label='M1 scaled')
# plt.plot(wave[1], baseScaled[1], label='M2 Scaled ')
# plt.plot(wave[2], baseScaled[2], label='M3 Scaled')
# plt.plot(wave[3], baseScaled[3], label='M4 Scaled')
# plt.plot(wave[4], baseScaled[4], label='M5 Scaled')
# plt.plot(wave[5], baseScaled[5], label='M6 Scaled')
# plt.plot(wave[6], baseScaled[6], label='M7 Scaled')
# plt.plot(wave[7], baseScaled[7], label='I1 Scaled')
# plt.plot(wave[8], baseScaled[8], label='I2 Scaled')
# plt.plot(AllBands[0][:,0], AllBands[0][:,1], label='VIIRS M1')
# plt.plot(AllBands[1][:,0], AllBands[1][:,1], label='VIIRS M2')
# plt.plot(AllBands[2][:,0], AllBands[2][:,1], label='VIIRS M3')
# plt.plot(AllBands[3][:,0], AllBands[3][:,1], label='VIIRS M4')
# plt.plot(AllBands[4][:,0], AllBands[4][:,1], label='VIIRS M5')
# plt.plot(AllBands[5][:,0], AllBands[5][:,1], label='VIIRS M6')
# plt.plot(AllBands[6][:,0], AllBands[6][:,1], label='VIIRS M7')
# plt.plot(AllBands[7][:,0], AllBands[7][:,1], label='VIIRS M8')
# plt.plot(AllBands[8][:,0], AllBands[8][:,1], label='VIIRS M9')
# plt.plot(AllBands[9][:,0], AllBands[9][:,1], label='VIIRS M10')
# plt.plot(AllBands[10][:,0], AllBands[10][:,1], label='VIIRS M11')
# plt.plot(AllBands[11][:,0], AllBands[11][:,1], label='VIIRS I1')
# plt.plot(AllBands[12][:,0], AllBands[12][:,1], label='VIIRS I2')
# plt.plot(AllBands[13][:,0], AllBands[13][:,1], label='VIIRS I3')
# plt.plot(AllBands[14][:,0], AllBands[14][:,1], label='VIIRS DNBLGS')
# plt.plot(AllBands[15][:,0], AllBands[15][:,1], label='VIIRS DNBMGS')
plt.plot(wavelength, FPI_lvl1, label = 'FPI lvl 1')
plt.plot(wavelength, Demo_LED, label = 'Demo LED')
plt.plot(wavelength, Demo_QTH, label = 'Demo QTH')
plt.plot(wavelength, Lmax, label='Lmax')
plt.legend()
plt.show()