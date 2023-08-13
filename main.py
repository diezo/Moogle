from moogle import Search

results = Search("justin")

GREEN = "\033[92m"
END = "\033[0m"

for result in results:
    print(f"{GREEN}URL: {END}{result.destination}")
    print(f"{GREEN}Title: {END}{result.title}")
    print(f"{GREEN}Description: {END}{result.description}\n\n")
