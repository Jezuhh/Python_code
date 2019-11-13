import subprocess

def transcode file (request, filename):
    command = 'ffmpeg -i "{source}" output file.mpg'.format(source=filename)
    subprocess.call(command, shell=True)

print("Hello World")


