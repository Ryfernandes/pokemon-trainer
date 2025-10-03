import requests

file_name = "pokemon.in"
url = "https://pokeapi.co/api/v2/pokemon/"

with open(file_name, "w") as file:
  for i in range(1025):
    try:
      response = requests.get(url + str(i + 1));
      data = response.json()
      name = data["name"]
      file.write(f"{i + 1} {name}\n")
      if (i > 0) & (i % 50 == 0):
        print(f"Completed {i}")
    except:
      print(f"Error getting Pokémon [{i + 1}]")
      break
