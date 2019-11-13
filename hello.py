import subprocess

def transcode_file (request, filename):
    command = 'ffmpeg -i "{source}" output file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)

print("Hello World")

file = input("Enter filename: ")
transcode_file("Request", file)

