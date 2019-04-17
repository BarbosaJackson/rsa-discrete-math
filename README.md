# Algoritmo RSA - Matemática Discreta (2018.02)
Alunos: 

- Jackson Barbosa da Silva (jbs@ic.ufal.br);

- Letícia Melquíades dos Santos Medeiros (lmsm@ic.ufal.br);

- Lucas Montenegro Andrade Assunção (lmaa@ic.ufal.br).

# Como executar

Para executar instale o python 3 na sua máquina caso ainda não o tenha, para tal basta seguir o [tutorial](https://docs.aws.amazon.com/pt_br/cli/latest/userguide/install-linux-python.html).
Depois de instalar o python, execute o comando: 
```sh
python3 rsa.py
```

Feito isso vai aparecer um menu, primeiramente gere a chave pública (digitando 1).

![Captura%20de%20tela%20de%202019-04-17%2008-35-52.png](Captura%20de%20tela%20de%202019-04-17%2008-35-52.png)

Em seguida você já pode criptografar ou descriptografar qualquer arquivo de texto, para criptografar, escolha 2 e o programa vai usar os valores definidos previamente para criptografar o arquivo, como os caracteres válidos são apenas as letras do alfabeto em __maiúsculo__ e o espaço o programa vai utilizar uma função para deixar o arquivo de entrada válido para executar a criptografia o código da função se encontra na pasta utils denominada validate contida no arquivo validate_rsa) o que ela faz é:
  - garantir que todas as letras vão estar maiúsculas
  - remover caracteres inválidos

Para descriptografar digite 3 no menu, será solicitado o nome do arquivo criptografado para a descriptografia ser executada, digite o nome do arquivo e a descriptografia acontece.

# Como funciona a "mágica"

## Criptografia
  Para criptografar a mensagem, utilizamos a fórmula
  ```sh
  C = Cod(m) = m^e mod N
  ```
  Em que :
  
  -  _m_ é um caractere;
    
  -  _e_ é o primo entre si de (_p_-1)(_q_-1);
    
  -  _N_ é a multiplicação de _p_ e _q_;
   
  -  _C_ é o caractere criptografado.
   
## Descriptografia
   Para descriptografar a mensagem, utilizamos a fórmula
  ```sh
  m = Decod(C) = C^d mod N
  ```
  Em que :
  
  -  _C_ é o caractere a ser descriptografado em formato de número
   
  -  _d_ é o inverso de _e_ calculado como:     
  ```sh
  e.d mod fiN = 1
  ```
  -  _N_ é a multiplicação de _p_ e _q_;
   
  -  _m_ é o caractere descriptografado.
    
