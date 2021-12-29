## Projeto 1 - Jogo da Forca ☠️😲

O algorítimo foi desenvolvido com o intuito de fortalecer conceitos de lógica de programação, foi montado apenas com Python e utiliza apenas a biblioteca **unicodedata** -  é utilizada para aceitar diversos tipos de caracteres especiais, fazendo com que o código não quebre.

O jogo é composto basicamente por duas funções:
1. Função que passa uma mensagem ao usuário, caso ele não queira iniciar o jogo.
2. Função do jogo - Faz a validação da entrada do usuário; recolhe a palavra chave/segredo; desenha a forca a cada erro do usuário; mostra a palavra conforme o usuário for acertando as letras.

### Regras do jogo:
* 2 jogadores - 1 coloca a palavra chave, o outro chuta as letras e a palavra.
* O jogador 'chutador' tem um total de 6 vidas.
* Chuta-se uma letra por vez.
* Pode chutar uma palavra por vez - conta como uma parte do corpo.
* Ç será o mesmo que C e os acentos não serão representados, serão letras normais.
