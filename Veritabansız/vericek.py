import requests
from bs4 import BeautifulSoup
from firebase import firebase




def temizle():
		sil = open('urun_bilgi.txt', 'w')
		sil.write("")
		sil.close()
		
def kategoriListe():
	r = requests.get("https://www.cavlak.com")
	soup = BeautifulSoup(r.content,"lxml")

	for a in soup.find_all('a',attrs={"class":"ty-menu__item-link"},href=True): #kategorilerin a taglerini alıyorz
    		urunListe(a['href']) # urunlisteye gonderiyorz
	

def urunListe(kategori):
	
	r = requests.get(kategori)
	soup = BeautifulSoup(r.content,"lxml")
	urun = soup.find("a",attrs={"class":"urun-title"})
	
	for a in soup.find_all('a',attrs={"class":"urun-title"},href=True):
    		stokKontrol(a['href'],a,"Sira")
    		
    		
    		
def stokKontrol(urun,isim,siraSayisi):
	r = requests.get(urun)
	soup = BeautifulSoup(r.content,"lxml")

	stok = soup.find("span",attrs={"class":"ty-qty-out-of-stock ty-control-group__item"})
	stokKod = soup.find("span",attrs={"class":"ty-control-group__item"})
	isim = isim
	
	try:
		print(isim.text + " " + stokKod.text + " " + stok.text) #stok.text yapisini bozma.try except bloklari ona gore calisiyor.
		with open("urun_bilgi.txt","a",encoding="utf-8") as dosya:
			
				dosya.write(str(siraSayisi) + "\n")				
				dosya.write(isim.text + "\n")
				dosya.write(stokKod.text + "\n")
				dosya.write(stok.text + "\n")
				
			
	except AttributeError:
		print(isim.text + " " + stokKod.text + " " + "Stok Mevcut")
		
		with open("urun_bilgi.txt","a",encoding="utf-8") as dosya:
				
				dosya.write(str(siraSayisi) + "\n")
				dosya.write(isim.text + "\n")
				dosya.write(stokKod.text + "\n")
				dosya.write("Stok Mevcut" + "\n")


def main():

	temizle()
	kategoriListe()
	
	
main()
