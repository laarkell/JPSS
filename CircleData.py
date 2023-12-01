import numpy as np
import matplotlib.pyplot as plt
import spectral.io.envi as envi
import pandas as pd

# Import DATA from files
#img = envi.open('/home/GES/larkell/Downloads/MM-Rshape/MM-Rshape.bip.hdr', '/home/GES/larkell/Downloads/MM-Rshape/MM-Rshape.bip')
img = envi.open('/home/GES/larkell/JPSS/Spectronon/DataAnalysis/PikaXC2.bil.hdr', '/home/GES/larkell/JPSS/Spectronon/DataAnalysis/PikaXC2.bil')
arr = img.load()


#manually import fro hdr file for photo - this is for the Pika XC2 camera
wavelength = np.array([395.95, 397.26, 398.57, 399.88, 401.19, 402.5, 403.81, 405.12, 406.43, 407.74, 409.05, 410.36, 411.67, 412.98, 414.29, 415.6, 416.92, 418.23, 419.54, 420.85, 422.16, 423.47, 424.79, 426.1, 427.41, 428.72, 430.04, 431.35, 432.66, 433.97, 435.29, 436.6, 437.91, 439.23, 440.54, 441.85, 443.17, 444.48, 445.8, 447.11, 448.42, 449.74, 451.05, 452.37, 453.68, 455.0, 456.31, 457.63, 458.94, 460.26, 461.57, 462.89, 464.21, 465.52, 466.84, 468.15, 469.47, 470.79, 472.1, 473.42, 474.74, 476.05, 477.37, 478.69, 480.01, 481.32, 482.64, 483.96, 485.28, 486.59, 487.91, 489.23, 490.55, 491.87, 493.19, 494.51, 495.82, 497.14, 498.46, 499.78, 501.1, 502.42, 503.74, 505.06, 506.38, 507.7, 509.02, 510.34, 511.66, 512.98, 514.3, 515.62, 516.94, 518.27, 519.59, 520.91, 522.23, 523.55, 524.87, 526.19, 527.52, 528.84, 530.16, 531.48, 532.81, 534.13, 535.45, 536.77, 538.1, 539.42, 540.74, 542.07, 543.39, 544.71, 546.04, 547.36, 548.69, 550.01, 551.33, 552.66, 553.98, 555.31, 556.63, 557.96, 559.28, 560.61, 561.93, 563.26, 564.58, 565.91, 567.23, 568.56, 569.89, 571.21, 572.54, 573.87, 575.19, 576.52, 577.85, 579.17, 580.5, 581.83, 583.15, 584.48, 585.81, 587.14, 588.46, 589.79, 591.12, 592.45, 593.78, 595.11, 596.43, 597.76, 599.09, 600.42, 601.75, 603.08, 604.41, 605.74, 607.07, 608.4, 609.73, 611.06, 612.39, 613.72, 615.05, 616.38, 617.71, 619.04, 620.37, 621.7, 623.03, 624.36, 625.69, 627.03, 628.36, 629.69, 631.02, 632.35, 633.69, 635.02, 636.35, 637.68, 639.02, 640.35, 641.68, 643.01, 644.35, 645.68, 647.01, 648.35, 649.68, 651.02, 652.35, 653.68, 655.02, 656.35, 657.69, 659.02, 660.36, 661.69, 663.03, 664.36, 665.7, 667.03, 668.37, 669.7, 671.04, 672.37, 673.71, 675.05, 676.38, 677.72, 679.05, 680.39, 681.73, 683.06, 684.4, 685.74, 687.08, 688.41, 689.75, 691.09, 692.43, 693.76, 695.1, 696.44, 697.78, 699.12, 700.46, 701.79, 703.13, 704.47, 705.81, 707.15, 708.49, 709.83, 711.17, 712.51, 713.85, 715.19, 716.53, 717.87, 719.21, 720.55, 721.89, 723.23, 724.57, 725.91, 727.25, 728.59, 729.94, 731.28, 732.62, 733.96, 735.3, 736.64, 737.99, 739.33, 740.67, 742.01, 743.36, 744.7, 746.04, 747.38, 748.73, 750.07, 751.41, 752.76, 754.1, 755.44, 756.79, 758.13, 759.48, 760.82, 762.17, 763.51, 764.85, 766.2, 767.54, 768.89, 770.23, 771.58, 772.93, 774.27, 775.62, 776.96, 778.31, 779.65, 781.0, 782.35, 783.69, 785.04, 786.39, 787.73, 789.08, 790.43, 791.77, 793.12, 794.47, 795.82, 797.16, 798.51, 799.86, 801.21, 802.56, 803.9, 805.25, 806.6, 807.95, 809.3, 810.65, 812.0, 813.35, 814.7, 816.05, 817.39, 818.74, 820.09, 821.44, 822.79, 824.14, 825.5, 826.85, 828.2, 829.55, 830.9, 832.25, 833.6, 834.95, 836.3, 837.65, 839.01, 840.36, 841.71, 843.06, 844.41, 845.77, 847.12, 848.47, 849.82, 851.18, 852.53, 853.88, 855.24, 856.59, 857.94, 859.3, 860.65, 862.0, 863.36, 864.71, 866.07, 867.42, 868.77, 870.13, 871.48, 872.84, 874.19, 875.55, 876.9, 878.26, 879.61, 880.97, 882.33, 883.68, 885.04, 886.39, 887.75, 889.11, 890.46, 891.82, 893.18, 894.53, 895.89, 897.25, 898.6, 899.96, 901.32, 902.68, 904.03, 905.39, 906.75, 908.11, 909.47, 910.83, 912.18, 913.54, 914.9, 916.26, 917.62, 918.98, 920.34, 921.7, 923.06, 924.42, 925.78, 927.14, 928.5, 929.86, 931.22, 932.58, 933.94, 935.3, 936.66, 938.02, 939.38, 940.74, 942.1, 943.46, 944.83, 946.19, 947.55, 948.91, 950.27, 951.64, 953.0, 954.36, 955.72, 957.09, 958.45, 959.81, 961.18, 962.54, 963.9, 965.27, 966.63, 967.99, 969.36, 970.72, 972.08, 973.45, 974.81, 976.18, 977.54, 978.91, 980.27, 981.64, 983.0, 984.37, 985.73, 987.1, 988.46, 989.83, 991.2, 992.56, 993.93, 995.29, 996.66, 998.03, 999.39, 1000.76, 1002.13, 1003.49, 1004.86, 1006.23, 1007.6, 1008.96, 1010.33, 1011.7, 1013.07])

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
print(circle)
circle /= pixelSize #pixels
circle = round(circle)
r = int(circle/2) #radius of circle
print('radius of circle:',r)

# somehow need to find the top corner of the light, from there we can use this info
# in pixels, and its over and then down
topCorner = [5, 50]
center = [round(topCorner[0] + circle/2), round(topCorner[1] + circle/2)] # the middle of the first circle
print('center of circle:', center)

# first chop pixels to the square that is rxr centered at center
#print((center[0]-r)-(center[0]+r))
#print((center[1]-r)-(center[1]+r))

# get avg square data to confirm the values look right! just to check intensity values!
square = img[(center[0]-r):(center[0]+r), (center[1]-r):(center[1]+r)]
lengthS = len(square[0,0,:])
avgSquare = np.empty(lengthS)
stdSquare = np.empty(lengthS)
for x in range(lengthS): 
    avgSquare[x] = np.average(square[:,:,x])
    stdSquare[x] = np.std(square[:,:,x])


# Take only the pixels in the circle and average them!
pixelList = np.empty(462)
z = r
counter = 0
for i in range(0,r+1):
    x = i
    y = np.sqrt((z**2)-(x**2))
    y = int(y)
    #print(x+center[0], y+center[1])
    for j in range(-y,y):
        if (i==r and y<0):
            continue
        pixelList += img[i+center[0],j+center[1]]
        if i !=0:
            pixelList += img[-i+center[0],j+center[1]]
            counter+=1
        # pixelList += img[i,-j]
        # pixelList += img[-i,-j]
        counter +=1
print(pixelList.size)
pixelList /= counter
print(pixelList.size)


# plotting to check that it looks right!
plt.xlabel('Wavelength (nm)')
plt.ylabel('Intensity')
plt.title('Example Data')
plt.plot(wavelength, pixelList, label = 'Circle Data')
plt.plot(wavelength, avgSquare, label = 'Square Data')
plt.legend()
plt.show()

