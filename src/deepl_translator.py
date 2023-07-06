import deepl

import settings


class DeeplTranslator:
    def __init__(self):
        self.translator = deepl.Translator(settings.DEEPL_KEY)

    def translate_text(self, text, target='ZH', source='EN'):
        return self.translator.translate_text(text, target_lang=target).text
