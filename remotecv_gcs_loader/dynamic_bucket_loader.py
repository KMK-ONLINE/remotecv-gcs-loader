from google.cloud import storage
from thumbor.utils import logger


def load_sync(path):
    url_by_piece = path.split('/')
    bucket_name = url_by_piece[0]
    file_path = '/'.join(url_by_piece[1:])

    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.get_blob(file_path)

    if blob == None:
        return "image does not exists in {}".format(path)
    else:
        image = blob.download_as_string()

    return image
