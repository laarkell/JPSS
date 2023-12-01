import spectral.io.envi as envi
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Import DATA from files
img = envi.open('/home/GES/larkell/Downloads/MM-Rshape/MM-Rshape.bip.hdr', '/home/GES/larkell/Downloads/MM-Rshape/MM-Rshape.bip')
arr = img.load()
#print(arr.info())
VIIRS = pd.read_excel('/home/GES/larkell/JPSS/VIIRS/J3 GLAMR RSR.xlsx')
print("Data sucessfully imported")

# Cleanup VIIRS Data
VIIRS = np.array(VIIRS)
VIIRS = VIIRS[1:,:]
#VIIRS = VIIRS[:,1:32] #chop off first wrong row and only keep first 32
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
#print(BandM1Wave.shape)
#print(BandDNBMGSWave.shape)

# Import Data from Bip file
pixel = img[698,639] #max
pixel2 = img[0,0] #min
pixel = np.array(pixel)
pixel2 = np.array(pixel2)

#select which pixels to average
pixel3 = img[100:150,100:150]
pixel3 = np.array(pixel3)
#print(pixel3)
#print(pixel3.shape)
#print(len(pixel3))
lengthP3 = len(pixel3[0,0,:])

# Manually Import wavelength data from hdr file
wavelength = np.array([397.24, 403.348, 409.456, 415.564, 421.672, 427.78, 433.888, 439.996, 446.104, 452.212, 458.32, 464.428, 470.536, 476.644, 482.752, 488.86, 494.968, 501.076, 507.184, 513.292, 519.4, 525.508, 531.616, 537.724, 543.832, 549.94, 556.048, 562.156, 568.264, 574.372, 580.48, 586.588, 592.696, 598.804, 604.912, 611.02, 617.128, 623.236, 629.344, 635.452, 641.56, 647.668, 653.776, 659.884, 665.992, 672.1, 678.208, 684.316, 690.424, 696.532, 702.64, 708.748, 714.856, 720.964, 727.072, 733.18, 739.288, 745.396, 751.504, 757.612, 763.72, 769.828, 775.936, 782.044, 788.152, 794.26, 800.368, 806.476, 812.584, 818.692, 824.8, 830.908, 837.016, 843.124, 849.232, 855.34, 861.448, 867.556, 873.664, 879.772])
#print(wavelength)
#print(len(wavelength))
#np.transpose(wavelength)

#calculations of averages
avgPixel3 = np.empty(lengthP3) #80 long
stdPixel3 = np.empty(lengthP3)
#creating an average of all selected pixels
for x in range(lengthP3): #250 values to average
    avgPixel3[x] = np.average(pixel3[:,:,x])
    stdPixel3[x] = np.std(pixel3[:,:,x])

# PLOT of avg pixel spectra

plt.plot(wavelength, pixel, label='Max')
plt.plot(wavelength, pixel2, label='Min')
plt.errorbar(wavelength, avgPixel3, stdPixel3, label = 'Average with Std', ecolor='yellow')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.legend()
plt.title('Average Pixel Intensity vs. Wavelength for 50x50 zone')
plt.savefig('myplot.png')
#plt.show()
print("Plot 1 created")
plt.close()

# PLOT of VIIRS data

plt.plot(BandM1Wave[:,0], BandM1Wave[:,1], label='M1')
plt.plot(BandM2Wave[:,0], BandM2Wave[:,1], label='M2')
plt.plot(BandM3Wave[:,0], BandM3Wave[:,1], label='M3')
plt.plot(BandM4Wave[:,0], BandM4Wave[:,1], label='M4')
plt.plot(BandM5Wave[:,0], BandM5Wave[:,1], label='M5')
plt.plot(BandM6Wave[:,0], BandM6Wave[:,1], label='M6')
plt.plot(BandM7Wave[:,0], BandM7Wave[:,1], label='M7')
#plt.plot(BandM8Wave[:,0], BandM8Wave[:,1], label='M8')
#plt.plot(BandM9Wave[:,0], BandM9Wave[:,1], label='M9')
#plt.plot(BandM10Wave[:,0], BandM10Wave[:,1], label='M10')
#plt.plot(BandM11Wave[:,0], BandM11Wave[:,1], label='M11')
plt.plot(BandI1Wave[:,0], BandI1Wave[:,1], label='I1')
plt.plot(BandI2Wave[:,0], BandI2Wave[:,1], label='I2')
#plt.plot(BandI3Wave[:,0], BandI3Wave[:,1], label='I3')
#plt.plot(BandDNBLGSWave[:,0], BandDNBLGSWave[:,1], label='DNBLGS')
#plt.plot(BandDNBMGSWave[:,0], BandDNBMGSWave[:,1], label='DNBMGS')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('VIIRS Band Data')
plt.legend()
plt.savefig('myplot2.png')
#plt.show()
print("Plot 2 created")


