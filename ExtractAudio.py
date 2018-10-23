import os
import sys
import subprocess

input_file = './uploads/sample.mp4'  # this is uploaded audio
bitrate = 128  # bitrate
# output audio filename. must to be randomized name(but, write over is good too)
output_file = './resources/hoge.mp3'
# converted audio file for uploading gcs from mp3 audio file
convert_file = './resources/hoge.flac'

# first, mp3 is extracted from movie(mp4) file
cmd = "ffmpeg -y -i {} -ab {}k {}".format(
    input_file, bitrate, output_file)
# output file
resp = subprocess.check_output(cmd, shell=True)
print('first step is done')

# nextly, mp3 file is converted to flac file fot uploading gcs
# here is problem
convert = 'ffmpeg -i {} -vn -ar 44100 -ac 2 -acodec flac -f flac {}'.format(
    output_file, convert_file
)
_resp = subprocess.check_output(convert, shell=True)

print('second step is done')
