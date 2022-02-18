import moviepy.editor

#LOAD ARCHIVE
video = moviepy.editor.VideoFileClip("video.mp4") #VARIABLE EXTENSION

#EXTRACT AUDIO
audio = video.audio

#SAVE THE AUDIO ARCHIVE
audio.write_audiofile("audio.mp3")  