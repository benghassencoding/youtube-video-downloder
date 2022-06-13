from pytube import YouTube
from colorama import init , Fore

def on_complete(stream,filepath) :
    print('download completed')
    print(filepath)

def on_progress(stream,chunks,bytes_remaining):
    progress = round(100-((bytes_remaining / stream.filesize)*100),2)
    print(f'{progress} %')

init()
#where to save
path = 'c:\\' #to do

url = input("type your url: ")
try :
    video = YouTube(url,on_complete_callback = on_complete , on_progress_callback = on_progress)
except :
    print("connection error !") #to handle expectations


# information
print("************info********")

print(Fore.RED+ f'title: \033[39m {video.title}')
print(Fore.RED + f"length : \033[39m{video.length / 60} minute ")
print(Fore.RED + f"views : \033[39m {video.views / 1000} K view")
print(Fore.RED + f"author : \033[39m {video.author}")

#download
print("************downloading********")
print(
    Fore.RED + "download : " +
    Fore.GREEN +"(b)est  \033[39m |" +
    Fore.YELLOW + " (w)orst \033[39m | " + 
    Fore.BLUE + "(a)udio  \033[39m  " "|(e)xit" )

choice = input('choice :')
try :
    match choice :
        case 'b' :
            video.streams.get_highest_resolution().download(path)
        case 'w' :
            video.streams.get_lowest_resolution().download(path)
        case 'a' :
            video.streams.get_audio_only.download(path)
except :
    print(" some error !")