from google.cloud import translate

import argparse
import google.auth
import os
import sys

LANG_LIST = {'ja', 'en'}
GCP_CRED_KEY = 'GOOGLE_APPLICATION_CREDENTIALS'


def main():
    gcp_cred = os.getenv(GCP_CRED_KEY)
    if gcp_cred is None:
        print('ERROR!!!')
        print(f'Please set environment {GCP_CRED_KEY}.')
        print(f'ex.) export {GCP_CRED_KEY}="your_credentials_key_place.json"')
        sys.exit(1)

    parser = argparse.ArgumentParser(description='translator')

    parser.add_argument('target', help='target ex.) ja', choices=LANG_LIST)
    parser.add_argument('texts', nargs='+', help='text ex.) hello')
    args = parser.parse_args()

    _, project_id = google.auth.default()
    text = ' '.join(args.texts)
    data = {
        'contents': [text],
        'parent': f'projects/{project_id}',
        'target_language_code': args.target,
    }

    translate_client = translate.TranslationServiceClient()
    rsp = translate_client.translate_text(**data)
    translated = rsp.translations[0].translated_text

    print(translated)


if __name__ == '__main__':
    main()
