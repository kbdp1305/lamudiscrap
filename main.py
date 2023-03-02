from bs4 import BeautifulSoup
import requests
from csv import writer

# url='https://www.lamudi.co.id/yogyakarta/house/buy/'
url='https://www.lamudi.co.id/yogyakarta/house/buy/?page=0'
page=requests.get(url)
start=2
with open("house_scraped.csv",'w',encoding='utf8',newline='') as f :
    writers=writer(f)
    header=['rumah','alamat',"harga","temppat_tidur","luas_bangunan","luas_lahan"]
    writers.writerow(header)
    while page.ok and start < 101 :
        soup=BeautifulSoup(page.content, 'html.parser')

        lists=soup.find_all('div',class_="ListingCell-AllInfo ListingUnit")
        for list in lists :
            nama_rumah=list.find('h2',class_="ListingCell-KeyInfo-title").text.replace("\n","").lstrip().strip().replace(".",'')
            location=list.find('span',class_="ListingCell-KeyInfo-address-text").getText().lstrip().strip()
            harga=list.find('span',class_='PriceSection-FirstPrice').text.lstrip().strip()
    # tempat_tidur=list.find('span',class_='KeyInformation-value_v2').text.replace(" ","").replace("\n","")[0]
            tempat_tidur=int(list.find('span',class_='KeyInformation-value_v2').find_next('span').next_sibling.strip())
            luas_bangunan_m_kuadrat=int(list.find('span',class_="KeyInformation-value_v2").find_next('span','icon-livingsize').next_sibling.strip().replace(" ","").replace("m²",""))
            luas_lahan=list.find('span',class_="KeyInformation-value_v2").find_next('span','icon-land_size').next_sibling.strip().replace(" ","").replace("m²","").lstrip().strip()
            writers.writerow([nama_rumah,location,harga,tempat_tidur,luas_bangunan_m_kuadrat,luas_lahan])
         
        url='https://www.lamudi.co.id/yogyakarta/house/buy/?page=0'
        url=url.replace('0',str(start))
        start+=1
        page=requests.get(url)

soup=BeautifulSoup(page.content, 'html.parser')
lists=soup.find_all('div',class_="ListingCell-AllInfo ListingUnit")
for list in lists:
    s=list.find('a',class_="ListingCell-moreInfo-button-v2_redesign")
    print(s)

    
    


