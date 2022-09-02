import requests
from bs4 import BeautifulSoup
result=input("Search: ")
arr=result.split(' ')
result="+".join(arr)
print(result)
r = requests.get("https://www.ebay.com/sch/i.html?_nkw="+result+"&_ipg=240")
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find("ul", {"class":"srp-results"}).find_all("li",{"class":"s-item"})
i=1
for result in results:
    nameSpan= result.find("span",{"role":"heading"}).text
    priceSpan = result.find("span",{"class":"s-item__price"}).text
    print(i-1, priceSpan, nameSpan)
    i+=1
if (i-1==0):
    print("No results found! ")
else:
    print("Total results: ", i-1)