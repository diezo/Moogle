from moogle import Search
from moogle.DataStructures import SearchResult

GREEN, END = "\033[92m", "\033[0m"

query: str = input(f"{GREEN}Query:{END} ")

print("\n")

results: list[SearchResult] = Search(query)

for result in results:
    print(f"{GREEN}URL: {END}{result.destination}")
    print(f"{GREEN}Title: {END}{result.title}")
    print(f"{GREEN}Description: {END}{result.description}\n")
