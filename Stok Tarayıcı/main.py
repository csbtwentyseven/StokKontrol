import requests
from bs4 import BeautifulSoup
from firebase import firebase

def veriTabani(stok,stokKod,isim):
	data = {
	'isim':isim,
	'stok':stok,
	'stokKod':stokKod,
	}

	vt = firebase.FirebaseApplication('https://cyberinnovacavlak.firebaseio.com/', None)
	vt.post('/cyberinnovacavlak/urun',data)
	

def kategoriListe():
	r = requests.get("https://www.cavlak.com")
	soup = BeautifulSoup(r.content,"lxml")

	for a in soup.find_all('a',attrs={"class":"ty-menu__item-link"},href=True):
    		urunListe(a['href'])

def stokKontrol(urun,isim):
	r = requests.get(urun)
	soup = BeautifulSoup(r.content,"lxml")

	stok = soup.find("span",attrs={"class":"ty-qty-out-of-stock ty-control-group__item"})
	stokKod = soup.find("span",attrs={"class":"ty-control-group__item"})
	isim = isim

	
	try:
		print(isim.text + " " + stokKod.text + " " + stok.text) #stok.text yapisini bozma.try except bloklari ona gore calisiyor.
		veriTabani(stok.text,stokKod.text,isim.text) 
	except AttributeError:
		print(isim.text + " " + stokKod.text + " " + "Stok Mevcut")
		veriTabani("Stok Mevcut",stokKod.text,isim.text) 
	
def urunListe(kategori):
	r = requests.get(kategori)
	soup = BeautifulSoup(r.content,"lxml")
	urun = soup.find("a",attrs={"class":"urun-title"})
	

	for a in soup.find_all('a',attrs={"class":"urun-title"},href=True):
    		stokKontrol(a['href'],a)


kategoriListe()


