import numpy as np
import matplotlib.pyplot as plt
import spectral.io.envi as envi
import pandas as pd

# Import DATA from files
img = envi.open('/home/GES/larkell/Downloads/MM-Rshape/MM-Rshape.bip.hdr', '/home/GES/larkell/Downloads/MM-Rshape/MM-Rshape.bip')
arr = img.load()
# print(arr.info())
VIIRS = pd.read_excel('/home/GES/larkell/JPSS/VIIRS/J3 GLAMR RSR.xlsx')
print("Data sucessfully imported")

# Import Data from Bip file
pixel = img[698,639] #max
pixel2 = img[0,0] #min
pixel = np.array(pixel)
pixel2 = np.array(pixel2)

#imputing needed info
print("Input lens focal length in mm:")
#focalLength = input()
focalLength = 50
focalLength = int(focalLength)/1000 # convert to m

print("Object distance in m from camera lens:")
#objectDistance = input()
objectDistance = 2
#objectDistance = int(focalLength)/100 # convert to m

#resonon data
pixelSize = 5.86 #μm
pixelSize = pixelSize/1000000 #m
print("Pixel size:", pixelSize, "m")
PixelsPerLine = 1600

# size of FPI in real life
ObjectLength = 0.15 #m
ObjectWidth = 0.1 #m

# Calculations from object to image size
ImageLength = focalLength*ObjectLength/objectDistance
ImageWidth = focalLength*ObjectWidth/objectDistance

# convert to pixels
ImageLength /= pixelSize # pixels
ImageWidth /= pixelSize # pixels
#print(ImageLength)
#print(ImageWidth)

# VIIRS takes 6in circles of data, make those circles 
circle = 6 #in, the diameter of the circle
circle *= 0.0254 #m
circle = focalLength*circle/objectDistance # convert from object to image
circle /= pixelSize #pixels
circle = round(circle)
rad = int(circle/2)
#print(rad)

# somehow need to find the top corner of the light, from there we can use this info
# in pixels, and its over and then down
topCorner = [5, 50]
FirstC = [round(topCorner[0] + circle/2), round(topCorner[1] + circle/2)] # the middle of the first circle
#print(FirstC)

FullCircle1 =[]
for j in range(rad):
    for i in range(rad):
        FullCircle1.append([FirstC[0]+i,FirstC[1]+j])
        FullCircle1.append([FirstC[0]-i,FirstC[1]-j])
        FullCircle1.append([FirstC[0]+i,FirstC[1]-j])
        FullCircle1.append([FirstC[0]-i,FirstC[1]+j])


FullCircle1 = FullCircle1[1:] # it does 0,0 twice so remove one of them!

#print(len(FullCircle1))

# get rid of the ones where the distance to them is greater than the radius, so chop the corners
bad = []
for x in range(len(FullCircle1)):
    d = np.sqrt(((FirstC[0]-FullCircle1[x][0])**2) +((FirstC[1]-FullCircle1[x][1])**2))
    d = round(d)
    if d >= rad:
        bad.append(x)
FullCircle1 = np.array(FullCircle1)
FullCircle1 = np.delete(FullCircle1, bad,0)

# collection of points that make up the circle
#print(len(FullCircle1))
FullCircle1 = np.array(FullCircle1)
#img = np.array(img)
print('Circle of points created')

#select which pixels to average
print('min x:')
print(min(FullCircle1[:,0]))
print('max x:')
print(max(FullCircle1[:,0]))
print('min y:')
print(min(FullCircle1[:,1]))
print('max :')
print(max(FullCircle1[:,1]))

pixel3 = img[min(FullCircle1[:,0]):max(FullCircle1[:,0]), min(FullCircle1[:,1]):max(FullCircle1[:,1])]
#pixel3 = img[100:150,100:150]
pixel3 = np.array(pixel3)
print(pixel3.shape)
print(len(pixel3))
print(len(pixel3[0]))

print(pixel3[0,0])
# pixel4 = pixel3[:,:,0:1]
# pixel4 = np.delete(pixel4,0,2)
# print(pixel4.shape)

badp = []
for x in range(len(pixel3)):
    for y in range(len(pixel3[0])):
        d = np.sqrt(((FirstC[0]-x)**2) +((FirstC[1]-y)**2))
    d = round(d)
    if d >= rad:
        badp.append(x)


# Manually Import wavelength data from hdr file
wavelength = np.array([397.24, 403.348, 409.456, 415.564, 421.672, 427.78, 433.888, 439.996, 446.104, 452.212, 458.32, 464.428, 470.536, 476.644, 482.752, 488.86, 494.968, 501.076, 507.184, 513.292, 519.4, 525.508, 531.616, 537.724, 543.832, 549.94, 556.048, 562.156, 568.264, 574.372, 580.48, 586.588, 592.696, 598.804, 604.912, 611.02, 617.128, 623.236, 629.344, 635.452, 641.56, 647.668, 653.776, 659.884, 665.992, 672.1, 678.208, 684.316, 690.424, 696.532, 702.64, 708.748, 714.856, 720.964, 727.072, 733.18, 739.288, 745.396, 751.504, 757.612, 763.72, 769.828, 775.936, 782.044, 788.152, 794.26, 800.368, 806.476, 812.584, 818.692, 824.8, 830.908, 837.016, 843.124, 849.232, 855.34, 861.448, 867.556, 873.664, 879.772])

ImgData = [wavelength,pixel2]
ImgData = np.array(ImgData)

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

#calculations of averages
lengthP3 = len(pixel3[0,0,:])
avgPixel3 = np.empty(lengthP3) #80 long
stdPixel3 = np.empty(lengthP3)
#creating an average of all selected pixels
for x in range(lengthP3): #250 values to average
    avgPixel3[x] = np.average(pixel3[:,:,x])
    stdPixel3[x] = np.std(pixel3[:,:,x])

# get rid of all the ones below 0.5 bc they dont matter
savex = np.empty(0, dtype = int)
for y in range(len(AllBands)):
    for x in range(len(AllBands[y])):
        if AllBands[y][x,1] <= CUTOFF:
            savex = np.append(savex,x)
    AllBands[y] = np.delete(AllBands[y],savex,0)
    savex = np.empty(0, dtype = int)

# scale so average is 1 w/ integral
# IntSum = np.trapz(BandM2Wave[:,1], BandM2Wave[:,0])
# diff = BandM2Wave[len(BandM2Wave)-1,0] - BandM2Wave[0,0]
# scalar = IntSum/diff

# scale the values to be average = 1
for x in range(len(AllBands)):
    avg = np.average(AllBands[x][:,1])
    AllBands[x][:,1] = AllBands[x][:,1]*(1/avg)
    #print(1/avg)
# print(AllBands[0].shape)


# limit wavelength and pixels to the specific VIIRS bands!
base = []
wave = []
baseNew = []
waveNew = []
for y in range(len(AllBands)):
    for x in range(len(wavelength)):
        if wavelength[x] >= AllBands[y][0,0]:
            if wavelength[x] <= AllBands[y][len(AllBands[y])-1,0]:
                baseNew.append(avgPixel3[x])
                waveNew.append(wavelength[x])
    base.append(baseNew)
    wave.append(waveNew)
    baseNew = []
    waveNew = []

# Correlate the wavelength from the pixel data to the closest data point wavelength in the 
# VIIRS data and then multiply them to scale the pixel data to the pattern of the VIIRS
baseScaled = []
waveScaled = []
list = []
oldDiff = 1000
for y in range(len(wave)):
    for x in range(len(wave[y])):
        for i in range(len(AllBands[y])):
            diff = abs(wave[y][x]-AllBands[y][i,0]) # compare the all bands wavelength to pixel wavelength to find the closest one
            if diff < oldDiff: # only save best one
                scaledBase = base[y][x]*AllBands[y][i,1]
                oldDiff = diff
        list.append(scaledBase)
        oldDiff = 1000
    baseScaled.append(list) #save into new list to replace base
    list = []


plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Example Data limited to VIIRS bands w/o scaling')
plt.plot(wavelength, avgPixel3, label = 'Img Data')
plt.plot(wave[0], base[0], label='M1')
plt.plot(wave[0], baseScaled[0], label='M1 scaled')
plt.plot(wave[1], base[1], label='M2')
plt.plot(wave[1], baseScaled[1], label='M2 Scaled ')
plt.plot(wave[2], base[2], label='M3')
plt.plot(wave[2], baseScaled[2], label='M3 Scaled')
plt.plot(wave[3], base[3], label='M4')
plt.plot(wave[3], baseScaled[3], label='M4 Scaled')
plt.plot(wave[4], base[4], label='M5')
plt.plot(wave[4], baseScaled[4], label='M5 Scaled')
plt.plot(wave[5], base[5], label='M6')
plt.plot(wave[5], baseScaled[5], label='M6 Scaled')
plt.plot(wave[6], base[6], label='M7')
plt.plot(wave[6], baseScaled[6], label='M7 Scaled')
plt.plot(wave[7], base[7], label='I1')
plt.plot(wave[7], baseScaled[7], label='I1 Scaled')
plt.plot(wave[8], base[8], label='I2')
plt.plot(wave[8], baseScaled[8], label='I2 Scaled')
plt.legend()
plt.show()
