def main():
    import requests
    from bs4 import BeautifulSoup
    result=input("Search: ")
    result="+".join(result.split(' '))
    print(result)
    r = requests.get("https://www.ebay.com/sch/i.html?_nkw="+result+"&_sacat=0&LH_TitleDesc=0&_ipg=240")
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find("ul", {"class":"srp-results"}).find_all("li",{"class":"s-item"})
    i=0
    for result in results:
        nameSpan= result.find("h3",{"class":"s-item__title"})
        priceSpan = result.find("span",{"class":"s-item__price"})
        print(i,priceSpan.text, nameSpan.text)
        i+=1
    print("Total results: ", i-1)

if __name__ == "__main__":
    main()