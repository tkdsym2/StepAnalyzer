import io
import os
from google.cloud import speech
from google.cloud.speech import enums, types


def TranscriptNarration(audiofile=''):
    if not audiofile:
        return None
    client = speech.SpeechClient()  # initialize client
    filename = os.path.join(
        os.path.dirname(__file__),
        'uploads',
        audiofile
    )

    with io.open(filename, 'rb') as audiofile:
        content = audiofile.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='ja-JP'
    )

    response = client.recognize(config, audio)
    for result in response.results:
        narration_text = result.alternatives[0].transcript
    return narration_text
