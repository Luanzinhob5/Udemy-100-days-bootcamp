from bs4 import BeautifulSoup
# import lxml

with open("website.html") as site:
    contents = site.read()

soup = BeautifulSoup(contents, "html.parser")  #Mandar o conteudo do html escolhido
# print(soup.title)         Ler a marcacao selecionada (completamente)
# print(soup.title.name)    Ler o nome da marcacao selecionada
# print(soup.title.string)  Ler a string da marcacao selecionada
# print(soup.prettify())    Ler o conteudo de maneira mais atrativa


all_anchor_tags = soup.find_all(name="a")  # Encontrar todas as marcacoes com essa string


for tag in all_anchor_tags: 
    # print(tag.getText()) # Pega o texto de cada tag que passou no loop
    tag.get("href") #Pegar o conteudo de algo especifico da marcacao

heading = soup.find(name="h1", id="name") #Especifica o ID e o nome da marcacao
# print(heading)

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get("class"))  #Para pegar a classe da marcacao

name = soup.select_one(selector="#name") #Selecionar algo especifico
# print(name)

headings = soup.select(".heading") #Seleciona mais de um de algo especifico
print(headings)