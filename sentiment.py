from os import chdir, getcwd, listdir, mkdir, rename
from os.path import join
import textblob

directory = input("Directory name?")
chdir(join(getcwd(), directory))
ls = listdir()
write_fl_name = directory + ".sentiment"
write_fl = open(write_fl_name, "w")

for i in ls:
	read_fl = open(i, "r").read()
	read_fl = textblob.TextBlob(read_fl)
	sentiment_obj = read_fl.sentiment
	sentiment_array = [sentiment_obj[0], sentiment_obj[1]]
	write_fl.write(str(sentiment_array) + "\n")

write_fl.close()

chdir("..")
mkdir("sentiments")
current_directory = join(getcwd(), directory)
sentiments_directory = join(getcwd(), "sentiments")
rename(join(current_directory, write_fl_name), join(sentiments_directory, write_fl_name))

