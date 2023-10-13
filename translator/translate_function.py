from googletrans import Translator

translator = Translator()


def translation(text, language='en'):
    tranlated_text = translator.translate(text, dest=language)
    return tranlated_text.text


