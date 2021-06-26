import sys
import google.auth
from google.cloud import translate


def main():
    args = sys.argv

    source, target = args[1].split('2')
    lang_map = {
        'ja': 'Japanese',
        'en': 'English',
    }
    text = args[2:]

    _, PROJECT_ID = google.auth.default()
    TRANSLATE = translate.TranslationServiceClient()
    PARENT = 'projects/{}'.format(PROJECT_ID)
    SOURCE, TARGET = (source, lang_map[source]), (target, lang_map[target])
    data = {
        'contents': text,
        'parent': PARENT,
        'target_language_code': TARGET[0],
    }

    rsp = TRANSLATE.translate_text(**data)
    translated = rsp.translations[0].translated_text

    print(translated)


if __name__ == '__main__':
    main()
