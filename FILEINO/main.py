from translate import Translator
# ok we want to translate in japanese the text in the file
# careful that there is a max for the api call
with open("test_file.txt", mode="r") as file:
    content = file.read()
    translator = Translator(to_lang="en", from_lang="fr")
    text_translated = translator.translate(content)
    print(text_translated)
