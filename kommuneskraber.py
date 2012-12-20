from BeautifulSoup import BeautifulSoup
from mechanize import Browser
br = Browser()
#opretter fil til at gemme data i
f = open("kommunedata1.txt", "w")
#�bner en hjemmeside og gemmer den i variable 'page'
page = br.open("https://bdkv2.borger.dk/foa/Sider/default.aspx?fk=22&foaid=11541520")
#l�ser indholdet af page og gemmer det i variablen html
html = page.read()
#forvandler indholdet af html til BeautifulSoup-struktureret data og gemmer i variablen soup
soup = BeautifulSoup(html)
#finder alle links
link = soup.findAll('a')
#laver en liste over alle links fra 21 til 216
kommunelink = link[21:216]
#k�rer igennem listen med links
for kommune in kommunelink:
    #�bner links med Mechanize Browser 
    kommuneside = br.open(kommune['href'])
    #l�ser indholdet af hver underside
    html2 = kommuneside.read()
    #forvandler indholdet til Beautiful Soup-struktur
    soup2 = BeautifulSoup(html2)
    #finder et specifikt link 
    hjemmesidelink = soup2.find('a', id='_uscAncHomesite')
    #finder alle links p� siden    
    emailadresse = soup2.findAll('a')
    #gemmer det 20. link i variablen email
    email = emailadresse[20]   
    #hvis der b�de findes et hjemmesidelink OG det 20. link indeholdet tekst, s�: 
    if hjemmesidelink and email.text:
        #gemmes hjemmesidelink og emailadresse i tekstfil
        print >> f, hjemmesidelink['href']+";"+email.text
#tekstfil gemmes  
f.close()
        




