from os import chdir, getcwd
from os.path import join

def rgba_averager():
	pass

def rgba_parser(batch, image_list_file):
	# commas in rgba array by platform
	total_commas = {"Facebook": 2267999, "Instagram": 4665599, "Twitter": 1572863}

	# iteratively parse rgba array files
	chdir(join(getcwd, batch))
	image_list_file = open(image_list_file, "r").readlines()

	for i in image_file_list:
		image_file = i.rstrip() + ".pixels"
		rgba_array_file = i[:len(i) - 4] + ".pixels" #TODO << check if newline char fucks this
		rgba_array = open(image_file, "r").read()
		rgba_file = open(rgba_array_file, "w")

		# parse out rgba values into line-delimited list
		comma_count = 0
		open_parens_index = 0
		closed_parens_index = 0
		previous_index = 0
		for k in enumerate(rgba_array[1:]):
			if k[1] == "(":
				# record opening parens as comma-equiv.
				open_parens_index += 1
			elif k[1] == ",":
				# disregard a of rgba
				if comma_count = 3:
					pass
				# record comma, extract value delimited
				# by comma + opening parens, comma + comma
				pass

		# write extracted values to file as rgb triad

