from gtts import gTTS
import os
import moviepy.editor

print("Type video/text to convert it to audio format")
opt = input("Type here:").lower()

if opt == 'video':
    video = moviepy.editor.VideoFileClip("pygame_projects.mp4")

    audio = video.audio
    audio.write_audiofile("extractedSong.mp3")
    os.system("extractedSong.mp3")

elif opt == 'text':

    # text = "Hello guys. How are you. All Fine?"
    abc = open('sample.txt')
    text = abc.read()


    language = 'en'

    obj = gTTS(text = text, lang = language, slow= False)

    obj.save("sample.mp3")

    os.system("sample.mp3")

else:
    print("please choose between video or text to get it converted into audio!!!")