import pytube 
from moviepy.editor import VideoFileClip
import random
import os

def clean_string(file):
	file = file.replace(":","")
	file = file.replace("/","")
	file = file.replace("|","")
	file = file.replace("%","")
	file = file.replace("#","")
	return file

def New_folder(Folder_name):
	try:

		dir = os.path.join("C:\\","Users\\hamza\\python",Folder_name)
		if not os.path.exists(dir):
			os.mkdir(dir)
			print("created folder")
	except Exception as e:
		pass
		print("folder not created")
	
	

def Move_files():
	
	import shutil

	# absolute path
	src_path = r"C:\Users\hamza\python\Part" 
	dst_path = r"C:\Users\hamza\python"
	

	
	for i in range(number_of_splits):
		shutil.move(src_path+str(i+1)+r+".mp4", dst_path+"\\"+mp4_file[:15])  #

def download_vid(url):
	
	global title
	myVideo = pytube.YouTube(url)
	title = myVideo.title
	myVideo = pytube.YouTube(url)
	thm = myVideo.thumbnail_url
	dwnl = myVideo.streams.get_highest_resolution()
	dwnl.download()
	

	

def split_vid(file_name):
	global r
	global mp4_file, number_of_splits
	mp4_file = (file_name+".mp4")
	mp4_file = clean_string(mp4_file)	

	print("In how many sections do you want to split this video? ")
	number_of_splits = int(input("Number of splits: "))
	for i in range (number_of_splits):
		from_ = int(input("From: "))
		to_ = int(input("To: "))
		clips = VideoFileClip(mp4_file).subclip(from_,to_)
		r="_"+str(random.randint(0,100))
		saving_title=str("Part"+str(i+1)+r+".mp4")
		clips.write_videofile(saving_title)



url = input("link : ")
download_vid(url)

split_vid(title)

New_folder(mp4_file[:15])
#print(mp4_file[:5])
Move_files()