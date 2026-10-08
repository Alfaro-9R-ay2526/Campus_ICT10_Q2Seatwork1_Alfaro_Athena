# Working with Lists
from pyscript import document
# Variables
country = ["Philippines", "Cambodia", "Thailand", "Singapore", "laos", "Indonesia", "Myanmar", "Malaysia"]
nickname = ["The Pearl of the Orient Seas","The Kingdom Of Wonder", "The Land of Smiles", "The Lion City","The Land of a Million Elephants","The Emerald of the Equator", "The Golden Land", "the Land of Diversity"]
# Function
def show_name(e):
    selected_country = document.getElementById("place").value

    index = country.index(selected_country)
    selected_nickname = nickname[index]

    document.getElementById("result").innerText = selected_nickname