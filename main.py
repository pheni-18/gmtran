from google.cloud import translate as gcp_translate

import argparse
import google.auth
import inspect
import os
import sys

LANG_LIST = {'ja', 'en'}
GCP_CRED_KEY = 'GOOGLE_APPLICATION_CREDENTIALS'


class CredNothingError(Exception):
    def __init__(self):
        self.message = inspect.cleandoc(f'''ERROR!!!
        Please set environment {GCP_CRED_KEY}.
        ex.) export {GCP_CRED_KEY}="your_credentials_key_place.json"
        ''')


def translate(args):
    gcp_cred = os.getenv(GCP_CRED_KEY)
    if gcp_cred is None:
        raise CredNothingError()

    parser = argparse.ArgumentParser(description='translator')

    parser.add_argument('target', help='target ex.) ja', choices=LANG_LIST)
    parser.add_argument('texts', nargs='+', help='text ex.) hello')
    args = parser.parse_args(args)

    _, project_id = google.auth.default()
    text = ' '.join(args.texts)
    data = {
        'contents': [text],
        'parent': f'projects/{project_id}',
        'target_language_code': args.target,
    }

    translate_client = gcp_translate.TranslationServiceClient()
    rsp = translate_client.translate_text(**data)

    return rsp.translations[0].translated_text


def main():
    try:
        translated = translate(sys.argv[1:])
        print(translated)
    except CredNothingError as e:
        print(e.message)


if __name__ == '__main__':
    main()
