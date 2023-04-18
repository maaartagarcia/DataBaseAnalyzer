import os
import sys
from PIL import Image

def test(args):
	f = args[0]
	files = os.listdir(f)
	nf = len(files)
	sizes = (0,0)

	for file in files:
		image_path = os.path.join(f, file)
		if os.path.isfile(image_path):
			try:
				image = Image.open(image_path)
				width, height = image.size
				sizes = sizes[0] + width, sizes[1] + height
			except:
				pass
		
		
	return sizes[0]/nf, sizes[1]/nf

def arguments():
	folder = input("Database Folder: ")
	return [folder]

def execute():
	print("SIZES TEST: ")
	args = arguments()

	if validate(args):
		print("-> Valid Arguments!")
		w, h = test(args)
		print("Mean Dimension Files: ({:.2f},{:.2f})".format(w, h))
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
		print("Instructions: py sizes.py folder")
		sys.exit(-1)

	width, height = test(sys.argv)
	print("Mean Dimension Files: ({:.2f},{:.2f})".format(width, height))
	
	