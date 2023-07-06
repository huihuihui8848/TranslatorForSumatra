import time

import pyperclip
from pynput import keyboard

import deepl_translator
import settings
import tools
import window


class TranslatorInSumatra:
    def __init__(self):
        self.hotkey = keyboard.HotKey(
            keyboard.HotKey.parse('<ctrl>+c'),
            self._on_activate)
        self.listener = keyboard.Listener(
            on_press=self._for_canonical(self.hotkey.press),
            on_release=self._for_canonical(self.hotkey.release))
        self.translator = deepl_translator.DeeplTranslator()

    def _for_canonical(self, f):
        return lambda k: f(self.listener.canonical(k))

    def _on_activate(self):
        if tools.get_active_window_class() == settings.SUMATRA_CLASS_NAME:
            time.sleep(0.1)
            text = self.translator.translate_text(pyperclip.paste().strip().replace('\n', ''))
            print(text)
            window.show_window_with_text(text)

    def run(self):
        self.listener.start()
        self.listener.join()
