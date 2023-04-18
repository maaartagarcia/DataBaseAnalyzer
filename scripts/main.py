import sys
import os
import pickle

import monochromatic as mc
import sizes as sz
import region as rg
import images as img

def test(args):
	mask = args[1:]
	nop = sum(1 for x in mask if x == "1") # Num of Operations
	nop_c = 0 # Current Num of Operations

	packages = {"monochromatic": mc, "sizes": sz, "region": rg, "images": img}

	with open("dict.pickle", "rb") as f:
	    args = pickle.load(f)

	for i in range(1, len(mask) + 1):
		f = mask[i-1]
		if f == "1":
			function = packages[args[i]]	
			function.execute()
			nop_c += 1

		if nop_c != nop:
			print()

def execute(args):
	if validate(args):
		print("**** ANALYZER LAUNCHED ****")
		test(args)
	else:
		print("-- Error Found: --")
		print("-- Instructions: py {} monochromatic sizes region images --".format(sys.argv[0]))
		
def validate(args):
	if len(args) != 5:
		return False
	
	return True

if __name__ == "__main__":
	execute(sys.argv)

	'''
	# For Sizes, Monochromatic and Region
	folder = "../resources/database/TRAINING_CG-1050/TRAINING/ORIGINAL"

	real_ph = "../resources/database/TRAINING_CG-1050/TRAINING/ORIGINAL/Im1_2.jpg"
	fake_ph = "../resources/database/TRAINING_CG-1050/TRAINING/TAMPERED/Im1_f2.jpg"

	# For Images
	pdf_f = "../resources/articles/file.pdf"
	'''
	

