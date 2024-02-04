Gerador de Chave e Criptografia de Mensagem
Este simples script em Python permite gerar uma chave com base em uma semente, escolher um nível de dificuldade e criptografar uma mensagem usando a chave gerada. A geração de chave suporta diferentes níveis de dificuldade, proporcionando flexibilidade no tipo de caracteres incluídos.

Utilização
Execute o script.
Insira uma semente para a geração da chave.
Escolha o modo:
Insira 1 ou criptografar para criptografar uma mensagem.
Insira qualquer outro valor para um modo não reconhecido.
Insira o comprimento desejado para a criptografia.
Escolha o nível de dificuldade:
Insira 1 para Apenas Números.
Insira 2 para Apenas Letras Minúsculas.
Insira 3 para Apenas Letras Maiúsculas.
Insira 4 para Letras Minúsculas e Maiúsculas.
Insira 5 para Letras e Números.
Insira 6 para Letras, Números e Caracteres Especiais.
Insira a mensagem que deseja criptografar.
O script então gerará uma chave com base na semente, nível de dificuldade e comprimento fornecidos. Se o modo escolhido for criptografar, ele criptografará a mensagem inserida usando a chave gerada.

Estrutura do Código
O script consiste em duas funções principais:

generate_key(seed, difficulty, tamanho)
Gera uma chave com base na semente, nível de dificuldade e comprimento fornecidos.
Retorna um dicionário onde cada caractere mapeia para uma string aleatória do comprimento especificado.
encrypt(message, key)
Criptografa uma mensagem fornecida usando a chave fornecida.
Substitui cada caractere na mensagem pelo seu valor correspondente na chave.
Sinta-se à vontade para modificar e adaptar o script de acordo com seus requisitos específicos.
