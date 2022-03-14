import requests
import json
from bs4 import BeautifulSoup
from datetime import datetime

page = requests.get("https://www.republika.co.id")
obj = BeautifulSoup(page.text, 'html.parser')
now = datetime.now()

tanggal = now.strftime("%d %B %Y %H:%M:%S")

print ('Menampilkan objek html')
print ('========================')
print (obj)

print ('\nMenampilkan title browser dengan tag')
print ('=======================================')
print (obj.title)

print ('\nMenampilkan title browser tanpa tag')
print ('=======================================')
print (obj.title.text)

print ('\nMenampilkan semua tag h2')
print ('===========================')
print (obj.find_all('h2'))

print ('\nMenampilkan headline berdasarkan div class')
print ('=============================================')
print (obj.find_all('div',class_='bungkus_txt_headline_center'))

print ('\nMenampilkan semua teks headline')
print ('===================================')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	print(headline.find('h2').text)

print ('\nMenyimpan headline pada file text')
print ('=====================================')
f=open('D:\Polban\SEMESTER 2\PROYEK1 PPLD SEM2\WebScript\headline.txt','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	f.write(headline.find('h2').text)
	f.write('\n')
f.close()


data=[]
# lokasi file json
f=open('D:\Polban\SEMESTER 2\PROYEK1 PPLD SEM2\WebScript\headline.json','w')
for headline in obj.find_all('div',class_='bungkus_txt_headline_center'):
	# append headline ke variabel data
	data.append({"judul":headline.find('h2').text})
# dump list dictionary menjadi json
jdumps=json.dumps(data)
f.writelines(jdumps)
f.close()


infoTerkini=[]
# lokasi file json
f=open('D:\Polban\SEMESTER 2\PROYEK1 PPLD SEM2\WebScript\infoTerkini.json','w')
for info in obj.find_all('div',class_='teaser_conten1_center'):
	# append headline ke variabel data
	infoTerkini.append({"judul":info.find('h2').text,"kategori":info.find('h1').text,"waktu_publish":info.find('div',class_='date').text,"waktu_scraping":tanggal})
# dump list dictionary menjadi json
jdumps=json.dumps(infoTerkini)
f.writelines(jdumps)
f.close()

