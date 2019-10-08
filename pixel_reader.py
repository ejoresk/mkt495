from PIL import Image

def pixel_reader():
	# open list of image filenames + read by line
	image_list = open(input("Path to image filenames?"), "r")

	for i in image_list:
		# create image-wise rgba arrays
		image = Image.open(i)
		pixel_value_array = str(list(image.getdata()))
		filename.write(pixel_value_array)

		# create + write image-wise rgba arrays to files
		image_name = i + ".pixels"
		filename = open(image_name, "r+")

