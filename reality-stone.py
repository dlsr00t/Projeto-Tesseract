from curses.ascii import alt
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
    question_finder(conteudo)

def question_finder(texto):
    a = texto.find("a)")
    b = texto.find("b)")
    c = texto.find("c)")
    d = texto.find("d)")
    e = texto.find("e)")
    a2 = texto.count("a)")
    b2 = texto.count("b)")
    c2 = texto.count("c)")
    d2 = texto.count("d)")
    e2 = texto.count("e)")

    #a2 = 2
    #c2 = 1

def diferenca(alternativaf, alternativac):
     ###Essa funcao tem como objetivo fazer o programa saber se existe mais de uma alternativa "a)" por exemplo,
     ###E caso exista a funcao tem que pegar a alternativa certa uma por uma 
     ###Exemplo: Pegar todas as alternativas "a)" de cada questao respectivamente
     ###Entao a funcao pegaria a alternativa "a)" da questao 1, a alternativa "a)" da questao 2 e etc.
     ###O motivo de nos estarmos fazendo isso e porque nos iremos usar as alternativas para buscar a resposta para uma pergunta e nao o contrario
     ###E quando nos conseguirmos pegar todas as alternativas com uma taxa de acerto de 10/10, nos iremos implementar isso no arquivo "requisicao (3).py"
     ###Dps que isso for feito o sistema de reconhecimento e busca estara completo
     ###Entao so faltara terminar de programar o "main.py" e o "servidor.py" servidor esse que tambem ira ser implementado no "requisicao (3).py"


    if (alternativaf!=a2):                 
        print(f'A quantidade de {alternativaf} e diferente da variavel "a2"')
    elif (alternativaf!=b2):
        print(f'A quantidade de {alternativaf} e diferente da variavel "b2"')
    elif (alternativaf!=c2):
        print(f'A quantidade de {alternativaf} e diferente da variavel "c2"')
    elif (alternativaf!=d2):
        print(f'A quantidade de {alternativaf} e diferente da variavel "d2"')
    elif (alternativaf!=e2):
        print(f'A quantidade de {alternativaf} e diferente da variavel "e2"')
    else:
        alternativa_encontrada = texto.find(alternativaf, alternativaf+10)


ler()
