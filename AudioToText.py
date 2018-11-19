import io
import os
from google.cloud import speech
from google.cloud.speech import enums, types


def TranscriptNarration(gcs_uri):
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='ja-JP')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=180)

    for result in response.results:
        # The first alternative is the most likely one for this portion.
        narration_text = result.alternatives[0].transcript
        print('Confidence: {}'.format(result.alternatives[0].confidence))
    return narration_text
