from pytube import YouTube

url = input("Url:")
print("Downloading...")
# main fuctions:
#YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
YouTube(url).streams.get_audio_only().download()
#YouTube(url).streams.get_highest_resolution().download()
print("The download was finished succesfuly!!")






