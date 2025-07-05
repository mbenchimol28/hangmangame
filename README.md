Jogo da Forca com Vocabulário Extenso e Dicas (Python)
Este é um projeto de um clássico Jogo da Forca desenvolvido em Python, utilizando os princípios de Programação Orientada a Objetos.

O grande diferencial deste jogo é que ele não depende de uma lista de palavras manual. Em vez disso, ele utiliza a poderosa biblioteca NLTK (Natural Language Toolkit) para acessar um vocabulário com milhares de palavras em português. Além disso, ele usa a WordNet para gerar dicas de categoria automaticamente, tornando o jogo desafiador, mas justo.

Demonstração do Jogo
Uma imagem de demonstração do jogo em execução.

Plaintext

>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|   |
     |
     |
=========

Dica: A palavra é um tipo de 'Fruta'

Palavra: _ _ r a n _ _

Letras Erradas:  s l p
Letras Corretas:  a r n

Digite uma letra:
Funcionalidades
Linguagem: Totalmente em Português-BR.

Paradigma: Desenvolvido com Programação Orientada a Objetos (POO), encapsulando a lógica do jogo em uma classe Hangman.

Vocabulário Gigante: Utiliza o corpus mac_morpho do NLTK para um banco de palavras com milhares de opções.

Dicas Automáticas: Usa a WordNet para gerar uma dica de categoria para cada palavra (ex: "Fruta", "Animal", "Ferramenta"), tornando o jogo muito mais divertido.

Autossuficiente: Não requer a criação manual de arquivos de texto com palavras (palavras.txt).

Como Colocar para Funcionar
Para rodar este projeto na sua máquina, siga os passos abaixo.

Pré-requisitos
Python 3.7 ou superior instalado em sua máquina.

Guia de Instalação
1. Clone o Repositório

Primeiro, clone este repositório para a sua máquina local usando Git. Abra seu terminal e digite:

Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
(Lembre-se de substituir seu-usuario/seu-repositorio pelo caminho real do seu projeto)

Depois, navegue para a pasta do projeto:

Bash

cd seu-repositorio
2. (Opcional, mas Recomendado) Crie um Ambiente Virtual

É uma boa prática criar um ambiente virtual para isolar as dependências do projeto.

Bash

# Criar o ambiente
python -m venv venv

# Ativar o ambiente
# No Windows:
venv\Scripts\activate
# No MacOS/Linux:
source venv/bin/activate
3. Instale a Biblioteca NLTK

O projeto depende da biblioteca NLTK. Instale-a usando o pip:

Bash

pip install nltk
4. Baixe os Pacotes NLTK Necessários

Após instalar a biblioteca, você precisa baixar os pacotes de dados específicos que o jogo utiliza (o corpus de palavras e a base de dados da WordNet).

Você pode fazer isso de forma fácil executando um único comando no seu terminal (com o ambiente virtual ativado, se você criou um):

Bash

python -c "import nltk; nltk.download('mac_morpho'); nltk.download('wordnet'); nltk.download('omw-1.4')"
Este comando executa um pequeno script Python que baixa e instala automaticamente os três pacotes necessários. Você só precisa fazer isso uma vez.

Como Jogar
Com tudo instalado, basta executar o arquivo principal do jogo:

Bash

python nome_do_arquivo.py
(Troque nome_do_arquivo.py pelo nome real do seu script Python, ex: jogo_forca.py)

Pronto! O jogo irá iniciar no seu terminal. Divirta-se!

Como o Código Funciona
Classe Hangman: Encapsula todo o estado e comportamento do jogo, como a palavra secreta, as letras erradas/corretas e os métodos para adivinhar letras e verificar o fim do jogo.

nltk.corpus.mac_morpho: É a fonte de milhares de palavras em português. O código filtra essa lista para selecionar apenas palavras adequadas para o jogo (com mais de 4 letras e sem caracteres especiais).

nltk.corpus.wordnet: É um grande banco de dados lexical. Usamos a função de "hiperônimos" (relações "é um tipo de") para encontrar a categoria de uma palavra e usá-la como dica. Por exemplo, a WordNet sabe que cachorro é um tipo de canino.
