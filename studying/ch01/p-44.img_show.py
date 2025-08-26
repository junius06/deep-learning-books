import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('p-44.ai-seoul_plogging_women.png')

plt.imshow(img)
#plt.show()
plt.savefig("p-44.ai-seoul_plogging_women.result.png")