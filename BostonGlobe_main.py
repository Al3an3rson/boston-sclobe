from bs4 import BeautifulSoup
import requests

# Setup variables
result = requests.get("https://www.bostonglobe.com/2020/01/25/nation/looking-diversity-presidential-race-its-with-alexandria-ocasio-cortez-other-surrogates-all-white-top-democratic-candidates/")
src = result.content
ParsedPars = []
# Implements BeautifulSoup for the content of the webstite with an html parser
soup = BeautifulSoup(src, features="html.parser")


# Checks if website loaded correctly and end program if it is not
if result.status_code != 200:
    print("This is an invalid link")
    exit()

# All of the actual paragraphs are stored in a "span class" within a "p class", but sometimes "p class"
# has other stuff as well, so this finds all the span classes (also uses attrs to specify even further)
paragraphs = soup.findAll("span", {"class": "html-render"})

# Removes the tags from the beginnings and ends of the paragraphs so it's actually readable
for index in paragraphs:
    ParsedPars.append(str(index)[25:-7])

# Prints readable paragraphs
for index in ParsedPars:
    print(index)