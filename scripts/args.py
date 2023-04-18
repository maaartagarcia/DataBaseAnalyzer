import pickle

import monochromatic as mc
import sizes as sz
import region as rg
import images as img

args = {1:"monochromatic", 2: "sizes", 3: "region", 4: "images"}

with open("dict.pickle","wb") as f:
	pickle.dump(args, f)
