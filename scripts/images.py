import os, sys, io, shutil
from PIL import Image
import fitz
import numpy as np

def test(args): # pdf_file to folder
	# Extract folder name and extension
	path = args[0] 
	folder_preffix, file_suffix = os.path.split(path) 
	folder_suffix, _ = os.path.splitext(file_suffix)
	folder_path = os.path.join(folder_preffix, folder_suffix)

	pdf_file = fitz.open(path)
        # Recorre cada página del archivo PDF
	nf = 0
	for page_num in range(pdf_file.page_count):
		page = pdf_file[page_num]
		images = page.get_images()


		for image_num, image in enumerate(images):
			xref = image[0]
			base_image = pdf_file.extract_image(xref)
			image_bytes = base_image['image']
			image_ext = base_image['ext']
			image_name = f"img_p{page_num}_n{image_num}.{image_ext}"

			with open(os.path.join(folder_path, image_name), 'wb') as image_file:
				image_file.write(image_bytes)
				image_file.close()
			nf += 1		
		
	return nf

def arguments():
	file = input("PDF File: ")
	return [file]
	
def execute():
	print("IMAGE EXTRACTOR TEST: ")
	args = arguments()

	if validate(args):
		print("-> Valid Arguments!")
		nf = test(args)
		function = lambda n: n if n is not None else 0 
		nf = function(nf)
		print("-> Number of Images Extracted: {}".format(nf))
	else:
		print("-- Error Found: --")
		print("-- Required Arguments: Valid PDF File and Not Existing Folder Called The Same as The PDF File --")
	
def validate(args):
	if len(args) != 1:
		return False

	# Extract folder name and extension
	path = args[0] 
	folder_preffix, file_suffix = os.path.split(path) 
	folder_suffix, ext = os.path.splitext(file_suffix)
	folder_path = os.path.join(folder_preffix, folder_suffix)
	
	# Doesn't exist or isn't pdf
	if not os.path.exists(path) or ext != ".pdf":
		return False

	# Check for already existing folder
	if os.path.exists(folder_path):
			print("?? Folder called {} already exists.".format(folder_path))
			response = input("?? Continue (y/n)?: ")
			if response.lower() != "y":
				return False
			else:
				shutil.rmtree(folder_path)
				os.makedirs(folder_path)
	else:
		os.makedirs(folder_path)

	return True

if __name__ == "__main__":
	execute(sys.argv)	