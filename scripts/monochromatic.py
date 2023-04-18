import os
import sys
from PIL import Image

def test(args): # Returns nnm, nf
	f = args[0]
	files = os.listdir(f)
	nf = len(files) # Number of Files
	nnm = 0 # Number of Colored Files

	for file in files:
		image_path = os.path.join(f, file)
		image = Image.open(image_path)
		if image.mode != "L": # Not Monochromatic Image
			nnm += 1	
		
	return nnm, nf

def arguments():
	folder = input("Database Folder: ")
	return [folder]

def execute():
	print("MONOCHROMATIC TEST: ")
	args = arguments()

	if validate(args):
		print("-> Valid Arguments!")
		nnm, nf = test(args)
		p = (nnm/nf)*100
		print("Coloured Files {}, All Files {} ({:.2f}%)".format(nnm, nf,p))
	else:
		print("-- Error Found: --")
		print("-- Required Arguments: Valid Folder --")
	
def validate(args):
	if len(args) != 1:
		return False
	
	f = args[0]
	if not os.path.exists(f):
		return False

	return True
	

# Executed as main
if __name__ == "__main__":
	args = len(sys.argv)
	if args != 2:
		print("Instructions: py monochromatic.py folder")
		sys.exit(-1)

	nnm, nf = test(sys.argv)
	p = (nnm/nf)*100
	print("Coloured Files {}, All Files {} ({:.2f}%)".format(nnm, nf,p))
	
	