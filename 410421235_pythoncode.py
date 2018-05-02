from PIL import Image
import numpy as np
import imageio as im
dataI = Image.open("I.png")
dataE = Image.open("E.png")
dataEprime = Image.open("Eprime.png")
datakey1 = Image.open("key1.png")
datakey2 = Image.open("key2.png")

data = np.zeros((120000,3),int)
e = np.zeros((120000), int)
w, h = datakey1.size
for i in range(h):
    for j in range(w):
        data[i*400+j][0] = datakey1.getpixel((j,i))
        data[i*400+j][1] = datakey2.getpixel((j,i))
        data[i*400+j][2] = dataI.getpixel((j,i))
        e[i*400+j] = dataEprime.getpixel((j,i))
w = np.array([0,0,0])
epoch = 1
maxlimit = 5
a = 0.00001
grad = [0, 0, 0]
stop = True
while (epoch <= maxlimit):
    for i,x in enumerate(data):
        ak = w[0]*x[0] + w[1]*x[1] + w[2] * x[2]
        ek = e[i] - ak
        w = w + a * ek * x
        print(w)
    epoch = epoch + 1
I = np.asarray(dataI).copy()
we, h = dataI.size
print(we,h)
for k in range(h):
    for j in range(we):
        I[k][j] = (dataEprime.getpixel((j,k)) - datakey1.getpixel((j,k))*w[0] - datakey2.getpixel((j,k))*w[1]) / w[2]
print(I)
im.imwrite('finalpicture.jpg', I)
