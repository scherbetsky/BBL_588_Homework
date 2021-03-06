import PIL
from PIL import Image
import numpy as np
color_img = np.array(Image.open('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\Noisy_1.png'))
img = np.mean(color_img, axis=2)
grayscale_img = np.zeros((300,400,3)) # creating a all zeros array in the same format with image
for h in range(300): # Each RGB value of the pixels will be replaced with average value
        for w in range(400):
                for avg in range(3):
                        grayscale_img[h][w][avg] = img[h][w]

I = Image.fromarray(grayscale_img.astype('uint8'))
I.show()
I.save('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\I_1.png')

color_img = np.array(Image.open('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\Noisy_5.png'))
img = np.mean(color_img, axis=2)
grayscale_img = np.zeros((300,400,3)) # creating a all zeros array in the same format with image
for h in range(300): # Each RGB value of the pixels will be replaced with average value
        for w in range(400):
                for avg in range(3):
                        grayscale_img[h][w][avg] = img[h][w]

I = Image.fromarray(grayscale_img.astype('uint8'))
I.show()
I.save('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\I_5.png')

color_img = np.array(Image.open('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\Noisy_10.png'))
img = np.mean(color_img, axis=2)
grayscale_img = np.zeros((300,400,3)) # creating a all zeros array in the same format with image
for h in range(300): # Each RGB value of the pixels will be replaced with average value
        for w in range(400):
                for avg in range(3):
                        grayscale_img[h][w][avg] = img[h][w]

I = Image.fromarray(grayscale_img.astype('uint8'))
I.show()
I.save('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\I_10.png')

color_img = np.array(Image.open('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\Noisy_20.png'))
img = np.mean(color_img, axis=2)
grayscale_img = np.zeros((300,400,3)) # creating a all zeros array in the same format with image
for h in range(300): # Each RGB value of the pixels will be replaced with average value
        for w in range(400):
                for avg in range(3):
                        grayscale_img[h][w][avg] = img[h][w]

I = Image.fromarray(grayscale_img.astype('uint8'))
I.show()
I.save('C:\\Users\\tcmserbetci\\Desktop\\BBL588 ödev\\I_20.png')
