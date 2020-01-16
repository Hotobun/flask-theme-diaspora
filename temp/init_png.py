import numpy as np 
from PIL import Image

target = np.array(Image.open("logo.png" ))


for i in target:
    if sum(i) > 0:
        print(i)
        
print(target)
print(type(target))
print(target.dtype)
print(target.shape)
