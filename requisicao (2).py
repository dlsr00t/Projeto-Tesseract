from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


#profile = webdriver.FirefoxProfile()
#profile.set_preference("javascript.enabled", False)
#driver = webdriver.Firefox(profile)
#op = Options()
#op.set_preference('javascript.enable', False)
navegador = webdriver.Firefox()
perguntas = ['A analissse das figuras e seus conhecimentos sobre o setor de transporte brasileiro permitem afirmar que', 'O contexto da citacao acima se refere a uma das principais caracteristicas do capitalismo', 'Um turista ingles tem duas possibilidades de viagem Punta Cana ou lencois maranhenses. Analise essas possibilidades apresentadas no mapa', 'Assinale a alternativa que nao indica um dos fatores que contribuem para o problema abordado no texto', 'a ilustracao, a seguir, mostra a distribuicao da malha ferroviaria em alguns paises com base nas informacoes obtidas no texto e nos desenhos, acima, so e correto afirmar que', 'A hidrovia tiete-parana escoa mercadorias, produtos agricolas e pessoas ate os paises vizinhos do brasil. portanto, essa hidrovia intrega os paises', 'A decadencia do transporte ferroviario esta associada a problemas inerentes de seu proprio desempenho e especialmente, da concorrencia do ramo rodoviario. Contribuem para compreendermos a atual situacao do sistema ferroviario, exceto', 'e a atmosfera cultural marcada pelo surgimento da bossa nova. A que governo tal periodo esta associado']

def searchGG(pergunta):
	navegador.get("https://google.com")
	#sleep(1)
	try:
		input_do_google = navegador.find_element(by='css selector', value='.gLFyf')
		input_do_google.click()
	except:
		input_do_google = navegador.find_element(by='css selector', value='.lst')
		input_do_google.click()

	input_do_google.send_keys(pergunta)
	input_do_google.send_keys(Keys.ENTER)

def desactivatejs():
	navegador.get("about:config")
	sleep(0.5)
	navegador.find_element(by='css selector', value='#warningButton').click()
	preference_config = navegador.find_element(by='css selector', value='#about-config-search')
	preference_config.send_keys('javascript')
	sleep(1)
	navegador.find_element(by='css selector', value='tr.odd:nth-child(2) > td:nth-child(3) > button:nth-child(1)').click()
	sleep(1)
	#navegador.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'T')

def onBrainly(pergunta):
	searchGG(pergunta+' site:brainly.com.br')
	sleep(1.5)
	try:
		navegador.find_element(by='css selector', value='#main > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1) > div:nth-child(1)').click()
	except:
		navegador.find_element(by='css selector', value='#main > div:nth-child(6) > div:nth-child(1) > div:nth-child(1) > a:nth-child(1) > h3:nth-child(1) > div:nth-child(1)').click()

	global resp
	#sleep(2)
	resp = navegador.find_element(by='css selector', value='div.brn-qpage-next-answer-box:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)').text
	sleep(1)

def respfinder():
	global fatiamento
	fatiamento = resp.split()
	for x in fatiamento:
		if len(x) == 1:
			global respf
			respf = x
			print(respf)
			break

dicionario_de_resp = {}

desactivatejs()
numero_de_questoes = len(perguntas)
for c in range(0,numero_de_questoes):
	onBrainly(perguntas[c])
	print(f'questao {c+1} ja foi')
	dicionario_de_resp[c+1] = resp

print(dicionario_de_resp)
