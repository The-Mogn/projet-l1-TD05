import re
class text :
    def __init__(self, text : str) -> None:
        self._text = text

    def remove_accents_special_characters(self) :
        final_text = ""
        for character in self._text :
            if character.isalnum() == True and re.match('^[a-zA-Z_]+$', character):
                final_text += character
        self._text = final_text

    def upper(self) :
        self._text = self._text.upper()    


def get_sentences(text) :
    sentences1 = text.split(".")
    sentences2 = []
    sentences3 = []
    for sentence1 in sentences1 :
        sentences2 += sentence1.split("!")
    for sentence2 in sentences2  :
        sentences3 += sentence2.split("?") 
    return sentences3    

def sentence_in_common(text1, text2) :
    text1_sentences = get_sentences(text1)
    text2_sentences = get_sentences(text2)

    for sentence in text1_sentences :
        if sentence in text2_sentences :
            return True
        else :
            return False

def get_text(path) :
    with open(path, mode='r') as file :
        return file.read()

# print(get_text("C:/Users/const/OneDrive/Bureau/Cours UVSQ S1/Info/projet-l1-TD05/text.txt"))

