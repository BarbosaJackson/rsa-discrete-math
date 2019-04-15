# Como executar

Para executar instale o python 3 na sua máquina caso ainda não o tenha, para tal basta seguir o [tutorial](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/install-linux-python.html).
Depois de instalar o python, execute o comando: 
```sh
python3 rsa.py
```
Feito isso vai aparecer um menu, primeiramente gere a chave pública (digitando 1).

Em seguida você já pode criptografar ou descriptografar qualquer arquivo de texto, para criptografar, escolha 2 e o programa vai usar os valores definidos previamente para criptografar o arquivo, como os caracteres válidos são apenas as letras do alfabeto em maiúsculo e o espaço o programa vai rodar um programa secundário para deixar o arquivo de entrada válido para executar a criptografia (programa que se encontra na pasta utils denominado validate_rsa) o que ele faz é:
  - garantir que todas as letras vão estar maiúsculas
  - remover caracteres inválidos

Para descriptografar digite 3 no menu, será solicitado o nome do arquivo criptografado para a descriptografia ser executada, digite o nome do arquivo e a descriptografia acontece.

# Como funciona a "mágica"


## Criptografia


## Descriptografia