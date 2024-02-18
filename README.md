# Moogle - Google Search API
This is a python package that uses [**BeautifulSoup4**](https://pypi.org/project/beautifulsoup4/) to perform google text search and scrape results from the webpage.

![Banner](https://raw.githubusercontent.com/diezo/moogle/master/assets/banner.png)

## 📦 Installation
```shell
$ pip install moogle
```

## 🚀 Usage
To perform a google search:
```python
from moogle import Search

results = Search("the rock")

for result in results:
    print(result.title)
    print(result.description)
    print(result.destination)
```

## 🧔 About Me
Hey! 👋 I'm a software hobbyist, currently living in India. Some of my top projects include:

- **Rooms** - Android Social Media App
- **iRoom** - Realtime Android Room Chat App
- [**Ensta**](https://github.com/diezo/ensta) - Python Package For Instagram API
- [**ProGPT**](https://github.com/diezo/progpt) - Python Package For ChatGPT API
- [**Moogle**](https://github.com/diezo/moogle) - Python Package For Google Search API
- **ShieldPass** - Offline Android Password Manager

**Reach me at: sonniiii@outlook.com**
