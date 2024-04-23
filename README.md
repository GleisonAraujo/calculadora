#Projeto Calculadora

Um calculadora que faz apenas operações de aritmética básica (adição, subtração, multiplicação, divisão)
Possui uma interface gráfica simples 

Para a criação da interface foi utilizado a biblioteca Kivy 
Instalação: python -m pip install kivy

Para a lógica da calculadora, utilizamos a função eval() do Python que permite avaliar uma expressão Python a partir de uma string e retornar o resultado.

Dentro da pasta "App" tem um pasta "Dist" com um executável da calculadora.
Para criar o exeutável, primeiro instalei o "pip install pyinstaller" e em seguida criei o executável com o comando "pyinstaller --onefile seu_script.py"

