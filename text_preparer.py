from os import chdir, getcwd, listdir, remove
from os.path import join
from PIL import Image
from pytesseract import image_to_string

# navigate to target directory
directory = input("Directory name?:  ")
chdir(join(getcwd(), directory))
ls = listdir()

# iteratively read image to string, write string to file, + delete image file
for i in ls:
	if i != ".DS_Store" and i[(len(i) - 3):] != "txt":
		# read image to string, remove newline chars
		image_string = image_to_string(i)
		image_string = image_string.replace("\n", " ")
		image_string = image_string.strip(" ")
		#image_string = " ".join(image_string)

		# write string to txt file
		write_fl = open(i[:(len(i) - 4)] + ".txt", "w")
		write_fl.write(image_string)
		write_fl.close()

		# remove image file
		remove(i)

