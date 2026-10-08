# Working with Lists
from pyscript import document

country = ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana","Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
nickname = ["Land of Silver","The Heart of South America", "Land of the Palms", "the Land of Poets","the Gateway to South America","The Equator", "Land of Many Waters","The Island Surrounded by Land", "Land of the Incas", "Beating Heart of the Amazon", "La Celeste", "Land of Grace"]

def show_name(e):
    selected_country = document.getElementById("country").value

    index = country.index(selected_country)
    selected_nickname = nickname[index]

    document.getElementById("result").innerText = selected_nickname