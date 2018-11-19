from google.cloud import storage


def UploadGStorage(filepath):
    client = storage.Client()
    bucket = client.get_bucket('analyze_audio')
    blob = bucket.blob(filepath.split('/')[-1])
    blob.upload_from_filename(filepath)
    gsutil_url = 'gs://analyze_audio/' + blob.public_url.split('/')[-1]
    return gsutil_url
