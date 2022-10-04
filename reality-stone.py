#from curses.ascii import alt
import cv2
import pytesseract as tesseract
import time
#tesseract.pytesseract.tesseract_cmd = "/usr/local/lib/python3.9/dist-packages"
'''
img = cv2.imread("literatura.jpg")
#texto = tesseract.image_to_string(img, lang='por', nice = 1, timeout=1000000)

print(img)
cv2.imshow('Result', img)
time.sleep(60*60)
'''
def ler():
    img = cv2.imread("questao2.jpg")
    #img = cv2.resize(img, (1080, 1080))
    conteudo = tesseract.image_to_string(img, lang='por')
    print(conteudo)
    #cv2.imshow('Result', img)
    #cv2.waitKey(0)
    #time.sleep(60)
    print(conteudo.find("a) "))
    print( conteudo.find("e) "))
    question_finder(conteudo, diferenca)

def question_finder(texto, func):
    letras = ['a','b','c','d','e']
    global alternativas
    alternativas = {}
    for letra in letras:
        alternativas[letra] = texto.find(f'{letra})'),texto.count(f'{letra})')
     
    func(alternativas['a'][0], alternativas['a'][1])
    #diferenca(alternativas['a'][0], alternativas['a'][1])


def diferenca(alternativaf, alternativac):
     ###Essa funcao tem como objetivo fazer o programa saber se existe mais de uma alternativa "a)" por exemplo,
     ###E caso exista a funcao tem que pegar a alternativa certa uma por uma 
     ###Exemplo: Pegar todas as alternativas "a)" de cada questao respectivamente
     ###Entao a funcao pegaria a alternativa "a)" da questao 1, a alternativa "a)" da questao 2 e etc.
     ###O motivo de nos estarmos fazendo isso e porque nos iremos usar as alternativas para buscar a resposta para uma pergunta e nao o contrario
     ###E quando nos conseguirmos pegar todas as alternativas com uma taxa de acerto de 10/10, nos iremos implementar isso no arquivo "requisicao (3).py"
     ###Dps que isso for feito o sistema de reconhecimento e busca estara completo
     ###Entao so faltara terminar de programar o "main.py" e o "servidor.py" servidor esse que tambem ira ser implementado no "requisicao (3).py"


    if (alternativac!=alternativas['a'][1]):               
        print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'a\'][1]"')
        if alternativac < alternativas['a'][1]:
            print(f'A quantidade de {alternativac} e menor do que a quantidade da variavel "alternativas[\'a\'][1]\n\n')
        elif alternativac > alternativas['a'][1]:
            print(f'A quantiade de {alternativac} e maior do que a quantidade da variavel "alternativas[\'a\'][1]')            


    elif (alternativac!=alternativas['b'][1]):
        print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'b\'][1]"')
        if alternativac < alternativas['b'][1]:
            print(f'A quantidade de {alternativac} e menor do que a quantidade da variavel "alternativas[\'b\'][1]"')
        elif alternativac > alternativas['b'][1]:
            print(f'A quantidade de {alternativac} e maior do que a quantidade da variavel "alternativas[\'b\'][1]"')


    elif (alternativac!=alternativas['c'][1]):
        print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'c\'][1]"')
        if alternativac < alternativas['c'][1]:
            print(f'A quantidade de {alternativac} e menor do que a quantidade da variavel "alternativas[\'c\'][1]"')
        elif alternativac > alternativas['c'][1]:
            print(f'A quantidade de {alternativac} e maior do que a quantidade da variavel "alternativas[\'c\'][1]"')
        

    elif (alternativac!=alternativas['d'][1]):
        print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'d\'][1]"')
        if alternativac < alternativas['d'][1]:
            print(f'A quantidade de {alternativac} e menor do que a quantidade da variavel "alternativas[\'d\'][1]"')
        elif alternativac > alternativas['d'][1]:
            print(f'A quantidade de {alternativac} e maior do que a quantidade da variavel "alternativas[\'d\'][1]')
   

    elif (alternativac!=alternativas['e'][1]):
        print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'e\'][1]"')
        if alternativac < alternativas['e'][1]:
            print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'e\'][1]"')
        elif alternativac > alternativas['e'][1]:
            print(f'A quantidade de {alternativac} e diferente da variavel "alternativas[\'e\'][1]"')


    else:
        alternativa_encontrada = texto.find(alternativaf, alternativaf+100)
        print(alternativa_encontrada)
        

ler()
