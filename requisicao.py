import requests

requisicao = requests.get("https://www.google.com/search", params={"q":"python"})
print(requisicao.content)
