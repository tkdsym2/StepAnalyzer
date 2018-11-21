import urllib.request
import sys
import os
# url sample:
# https://crest-multimedia-web.s3.amazonaws.com/tsuka/fabnavi5-staging/uploads/attachment/movie/file/5724/2018-08-18_13_29_02.mp4


def DownloadMovie(url=''):
    if not url:
        return None
    file_name = url.split('/')[-1]
    save_path = './download/movie/' + file_name
    if not os.path.exists('./download/movie'):
        os.makedirs('./download/movie')
    urllib.request.urlretrieve(url, save_path)
    return save_path


def DownloadThumb(url=''):
    if not url:
        return None
    file_name = url.split('/')[-1]
    save_path = './download/thumb/' + file_name
    if not os.path.exists('./download/thumb'):
        os.makedirs('./download/thumb')
    urllib.request.urlretrieve(url, save_path)
    return save_path
