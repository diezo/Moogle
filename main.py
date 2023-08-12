from moogle import Search

search = Search("justin bieber")
destinations = [item.destination for item in search]

print("\n".join(destinations))
