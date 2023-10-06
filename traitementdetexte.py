import re

def treat_text(text) :
        final_text = ""
        for character in text :
            if character.isalnum() == True and re.match('^[a-zA-Z_]+$', character):
                final_text += character
        return final_text.upper() 
class text :
    def __init__(self, text : str) -> None:
        self._text = text

    def treat_text(self) :
        final_text = ""
        for character in self._text :
            if character.isalnum() == True and re.match('^[a-zA-Z_]+$', character):
                final_text += character
        self._treated_text = final_text.upper()   

    def chiffrer_cesar(self) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.treat_text()
        text_cesar = ""
        for letter in self._treated_text :
            text_cesar += alphabet[(alphabet.index(letter) + 3) % 26]
        self._text_cesar = text_cesar
        return text_cesar    
    
    def chiffrer_vigenere(self, key) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.treat_text()
        text_vigenere = ""
        key = treat_text(key)
        len_key = len(key)
        while len(key) < len(self._treated_text):
            key += key[len(key) - len_key]
        print(key)  
        for i in range(len(self._treated_text)) :
            text_vigenere += alphabet[(alphabet.index(self._treated_text[i]) + alphabet.index(key[i])) % 25]
        self._text_vigenere = text_vigenere
        self._key_vigenere = key
        return text_vigenere
    
    def dechiffrer_cesar(self) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.treat_text()
        new_text = ""
        for letter in self._treated_text :
            new_text += alphabet[(alphabet.index(letter) - 3) % 26]
        self._decrypted_cesar = new_text
        return new_text
    
    def dechiffrer_vigenere(self, key) :
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.treat_text()
        text_vigenere = ""
        key = treat_text(key)
        len_key = len(key)
        while len(key) < len(self._treated_text):
            key += key[len(key) - len_key]
        print(key)  
        for i in range(len(self._treated_text)) :
            text_vigenere += alphabet[(alphabet.index(self._treated_text[i]) - alphabet.index(key[i])) % 25]
        self._text_vigenere = text_vigenere
        self._key_vigenere = key
        return text_vigenere
        

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
        

my_text = text("Bonjour !")
new_text = my_text.chiffrer_vigenere("fdp")
print(new_text)


