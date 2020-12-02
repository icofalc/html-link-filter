import bs4
import glob
import os
import os.path

d = os.getcwd()
for root, dirs, files in os.walk(d):
    for file in files:
        if file.endswith('.htm') or file.endswith('.html'):

            filei = str(file)
            with open(filei, encoding="utf8") as f:
                print("\n\n\n")
                print(filei)
                print("\n\n\n")
                soup = bs4.BeautifulSoup(f,features="html.parser")
                mydivs = soup.findAll('a')
                for link in mydivs:
                    print(str(link) + "\n")



    
    
    
