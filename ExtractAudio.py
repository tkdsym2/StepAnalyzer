import os
import sys
import subprocess

# converting property
bitrate = 128
hz = 44100


def ExtractedAudio(input_file, output_file):
    if not input_file:
        return None
    extracted_audio = 'ffmpeg -i {} -vn  {}'.format(
        input_file, output_file)
    result = subprocess.check_output(extracted_audio, shell=True)


def ConvertMP3toFLAC(input_file, output_file):
    if not input_file:
        return None
    print('---------converting-----------')
    convert_audio = 'sox {} --rate 16k --bits 16 --channels 1 {}'.format(
        input_file, output_file)
    result = subprocess.check_output(convert_audio, shell=True)


def GetAudio(filepath, filename):
    if not filepath:
        return None
    input_file = filepath
    _filename = filename.split('.')[0]

    if not os.path.exists('./mp3'):
        os.makedirs('./mp3')
    ExtractedAudio(input_file, './mp3/{}.mp3'.format(_filename))

    if not os.path.exists('./audiofile'):
        os.makedirs('./audiofile')

    audio_resouce = './audiofile/{}.flac'.format(_filename)
    ConvertMP3toFLAC('./mp3/{}.mp3'.format(_filename), audio_resouce)
    return audio_resouce
