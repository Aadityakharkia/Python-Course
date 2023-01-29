# Day 45
# Goal - Read the Web using Beautiful Soup

from bs4 import BeautifulSoup

with open("index.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents,"html.parser")
print(soup.a)

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())
    print(tag.get("href"))