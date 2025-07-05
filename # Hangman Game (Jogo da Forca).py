import random
import nltk
from nltk.corpus import wordnet
from string import ascii_lowercase


def setup_nltk():
    try:
        nltk.data.find('corpora/mac_morpho.zip')
        nltk.data.find('corpora/wordnet.zip')
        nltk.data.find('corpora/omw-1.4.zip')
    except LookupError:
        print("\n" + "="*60)
        print("ERRO: Pacotes NLTK necessários não encontrados.")
        print("Por favor, execute o seguinte comando em um console Python:")
        print(">>> import nltk")
        print(">>> nltk.download('mac_morpho')")
        print(">>> nltk.download('wordnet')")
        print(">>> nltk.download('omw-1.4')")
        print("="*60 + "\n")
        return False
    return True


if not setup_nltk():
    exit()

todas_as_palavras = nltk.corpus.mac_morpho.words()


board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


def get_random_word_and_hint():
    """
    Busca uma palavra aleatória e sua categoria (dica) usando a WordNet.
    Continua tentando até encontrar uma palavra que tenha uma categoria válida.
    Retorna:
        (tuple): Uma tupla contendo (palavra, dica).
    """
    palavras_validas = list(set([
        p.lower() for p in todas_as_palavras if len(p) > 4 and p.isalpha()
    ]))
    
    while True:
        palavra = random.choice(palavras_validas)
        
        synsets = wordnet.synsets(palavra, lang='por')
        
        if synsets:
            
            hypernyms = synsets[0].hypernyms()
            
            if hypernyms:
                
                dica = hypernyms[0].lemmas('por')[0].name().replace('_', ' ')
                return (palavra, dica)
            

class Hangman:
    def __init__(self, word, category):
        self.word = word
        self.category = category 
        self.missed_letters = []
        self.guessed_letters = []

    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    def game_over(self):
        return self.game_won() or (len(self.missed_letters) == 6)

    def game_won(self):
        return '_' not in self.hide_word()

    def hide_word(self):
        rtn = ''
        for letter in self.word:
            if letter not in self.guessed_letters:
                rtn += '_'
            else:
                rtn += letter
        return rtn

    
    def print_game_status(self):
        print(board[len(self.missed_letters)])
        print(f"\nDica: A palavra é um tipo de '{self.category.capitalize()}'") 
        print('\nPalavra: ' + self.hide_word())
        print('\nLetras Erradas: ', ' '.join(self.missed_letters))
        print('Letras Corretas: ', ' '.join(self.guessed_letters))
        print()



def main():

    palavra, dica = get_random_word_and_hint()
    
   
    game = Hangman(palavra, dica)

    while not game.game_over():
        game.print_game_status()
        
        user_input = input('\nDigite uma letra: ').lower()

        if len(user_input) == 1 and user_input in ascii_lowercase:
            game.guess(user_input)
        else:
            print("Entrada inválida. Por favor, digite apenas uma letra.")

    game.print_game_status()

    if game.game_won():
        print('\nParabéns! Você venceu!!')
    else:
        print('\nGame over! Você perdeu.')
        print('A palavra era ' + game.word)
    
    print('\nFoi bom jogar com você! Agora vá estudar!\n')


if __name__ == "__main__":
    main()