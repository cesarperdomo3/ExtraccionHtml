import requests
from bs4 import BeautifulSoup

# URL de la página web a la que deseas acceder
url = "https://www.youtube.com"

# Realiza una solicitud GET a la página web
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extrae las etiquetas IMG y Meta
img_tags = soup.find_all("img")
meta_tags = soup.find_all("meta")

print("Etiquetas IMG:")
for img in img_tags:
    print(img)

print("\nEtiquetas Meta:")
for meta in meta_tags:
    print(meta)

# Extrae los formularios en HTML
form_tags = soup.find_all("form")
print("\nFormularios en HTML:")
for form in form_tags:
    print(form)

# Extrae los enlaces en documentos HTML
link_tags = soup.find_all("a")
print("\nEnlaces en documentos HTML:")
for link in link_tags:
    print(link)