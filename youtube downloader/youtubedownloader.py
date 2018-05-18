import pytube

print("Enter the video link")
link = input()

yt = pytube.YouTube(link)
stream = yt.streams.first()

#videos = yt.get_videos()

#s=1
#for v in videos:
 #   print(str(s)+". "+str(v)) 
  #  s += 1

#print("Enter the number of videos: ")
#n = int(input())
#vid = videos[n-1]

print("Enter the location:")
destination = input()
stream.download(destination)
print("\nhas been successfully downloaded ")


