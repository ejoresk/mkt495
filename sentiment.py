from os import chdir, getcwd, listdir, mkdir, rename
from os.path import join
from textblob import TextBlob

# navigate to directory w/ txt files
directory = input("Directory name?")
chdir(join(getcwd(), directory))
ls = listdir()
write_fl_name = directory + ".sentiment"
write_fl = open(write_fl_name, "w")

# iteratively sentiment-analyze txt files
for i in ls:
	read_fl = open(i, "r").read()
	read_fl = TextBlob(read_fl)
	sentiment_obj = read_fl.sentiment
	sentiment_array = [sentiment_obj[0], sentiment_obj[1]]
	write_fl.write(str(sentiment_array) + "\n")

write_fl.close()

# navigate down a directory + move list of sentiment arrays to own directory
chdir("..")
mkdir("sentiments")
rename(join(directory, write_fl_name), join("sentiments", write_fl_name))

