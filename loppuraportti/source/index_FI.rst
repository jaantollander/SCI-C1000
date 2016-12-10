.. SCI-C1000 documentation master file, created by
   sphinx-quickstart on Thu Dec  8 11:32:07 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SCI-C1000 - Loppuraportti
*************************
.. SCI-projektikurssin tavoitteena on, että jokainen ryhmä omassa tehtävässään huomaa kehittyvänsä epämääräisen haasteen selkeyttämisessä, toimintasuunnitelmansa toteuttamisessa, ideansa liiketoimintapotentiaalin kartoittamisessa, ideansa kommunikoinnissa sekä ennen kaikkea ryhmänä työskentelemisessä.

.. Loppuraportin tavoitteena on kuvata saavuttamanne tulos, mutta ennen kaikkea dokumentoida ryhmänne oppimis- ja kehittymispolun reflektointi ryhmänä sekä ryhmän jäsenittäin. Loppuraportti on pohdinta prosessista ja edistymisestänne, jonka ryhmänä kävitte läpi:

.. 1) tiivistetty kuvaus haasteestanne ja ratkaisusta, johon päädyitte;

.. 2) miten kehityitte ryhmänä esim. yhteisten 'pelisääntöjen', työskentelytapojen, kommunikointitapojen suhteen, konfliktien ratkaisuissa;

.. 3) mitä opitte ryhmänä haasteeseenne ja ratkaisun liiketoimintamahdollisuuden arvioimiseen liittyen, mitä opitte ryhmänä toimimisesta sekä

.. 4) miten kukin ryhmän jäsen koki kehittyvänsä kurssin aikana ryhmän jäsenenä sekä mitä koki oppivansa ryhmän käsittelemästä teemasta. Hyödyntäkää esim. alla olevaa toiminnan arviointilomaketta.

.. Loppuraportin laajuus on noin 5-7 sivua riippuen. ryhmän jäsenten määrästä. Loppuraportti on oma erillinen dokumentti, joka voi olla linkitettynä ryhmän blogiin. Määräaika 16.12 klo 23.59.

Tiivistelmä
===========

.. csv-table::

   "Ryhmä", "*3+4Dudes*"
   "Aihe", "*Sisätilapaikannus kuvien avulla*"
   "Blog", "`https://jaantollander.github.io/SCI-C1000/ <https://jaantollander.github.io/SCI-C1000/>`_"

Ongelma
-------
GPS järjestelmää ei voida käyttää sisätilapaikannukseen esteiden tukkiessa satellien suoran näköyhteyden tehden siitä epätarkan ja epäluotettavan. Tämän takia sisätilapaikannukseen on kehitetty monia muita menetelmiä kuten

- *WIFI Kolmiomittaus*
- *Bluetooth Signaalitolpat*
- *Maan magneettikentän mittaus*
- *Pedestrian Dead Reckoning*
- *Sisätilapaikannus kuvien avulla*

Osa järjestelmistä kuten *bluetooth signaalitolpat* tai *WIFI kolmiomittaus* edellyttävät kalliin infrastruktuurin asentamista tilaan. Toisaalta *Pedestrian Dead Reckoning* menetelmän virhe on kasautuva eikä sitä voida käyttää paikantamiseen yksinään. `Indoor Atlas <http://www.indooratlas.com/>`_ on kehittänyt *maan magneettikentän mittaukseen* perustuvan järjestelmän joka on toimiva ja pelkästään paikantamiseen *kuvista paikantamista* parempi ratkaisu, mutta se ei tarjoa mahdollisuutta virtuaali- tai lisättyyn todellisuuteen eikä se kerro käyttäjän suuntaa.


Ratkaisu
--------
Ryhmän esittämä ratkaisu ongelmaan *sisätilapaikannus kuvien avulla*, joka perustuu 3-ulotteisen pistepilven rakentamiseen valokuvista. Pistepilven avulla käyttäjä voidaan paikantaa kun käyttäjän ottama kuva sijoitetaan pistepilveen vertaamalla sitä olemassa oleviin kuviin.


Vahvuudet
^^^^^^^^^

- Mahdollisuus rakentaa 3-ulotteinen malli tekstuureineen virtuaali- ja lisättyä todellisuutta varten.
- Kykenee ratkaisemaan käyttäjän katseen suunnan
- Perustuu jo olemassa olevaan infrastruktuuriin, kuten kännykkä kamerat
- Ratkaisu on ohjelmistoon perustuva (vastakohtana laitteistoon perustuva) tehden siitä paremmin *skaalautuvan* ja pienentäen *ylläpito kustannuksia*


Haasteet
^^^^^^^^

- Teknologisesti haastava
- Vaatii laskentatehoa ja aikaa
- Helppo käytettävyys vaatii teknologiaa jonka avulla on mahdollista ottaa kuvia ympäristöstä hyvin vaivattomasti, esimerkiksi älylasit.
- 3D mallien rakentamiseen käytettyyn *Structure from motion* algoritmin hahmon tunnistukseen pitäisi tehdä parannuksia, jotta suuria malleja rakentaessa mallista tulisi yhtenäinen. Ongelmana suurien mallien rakentamisessa on ollut että algoritmit saattavat rakentaa monta pienempää mallia jos en eivät tunnista riittävästi yksityiskohtia kuvista.
- Algoritmien tehokkuutta voisi parantaa sekä rakentaa spesialisoitua teknologiaa 3D mallien kuvaamiseen, jotta laskenta aikaa saataisin pienemmäksi
- Linssien aiheuttamea vääristymiä pitäisi korjata korjaavilla algoritmeilla


Bisness ja tuotteen kaupallistaminen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- Kiinnitetty aloitushinta ja kuukausittaiset päivitys ja ylläpitökustannukset
- Aloitushinta perustuu mallinettavan alueen kokoon ja monimutkaisuuteen
- Ylläpitökustannukset perustuvat arvoituun käyttäjämäärään ja käyttäjäkohtaisiin ominaisuuksiin


Yhteenveto
^^^^^^^^^^
Käytännössä teknologia kuviin perustuvassa navigoinnissa on jo olemassa, mutta käytännön sovellukseen, varsinkin ei ammatti käyttöön, on vielä matkaa. Teknologialle on kuitenkin kysyntää ja markkina potentiaalia virtuaali ja lisätty todellisuus sovellusten, sekä älylasien kehityksen, takia joten on todennäkoistä että näemme teknologiaan pohjautuvia sovelluksia jo lähitulevaisuudessa.


Ryhmätyö
========

Menetelmät
----------


.. csv-table:: Työtehtävien jako
   :header: "**Nimi**", "**Tehtävä**"

   "Lauri", "Teknologioiden vertailu, blogin kirjoittaminen, kilpailijoihin yhteydenotto"
   "Markus", "Presentaatiot, blogin kirjoittaminen, organisointi"
   "Misamatti", "Teknologioihin tutustuminen, blogin kirjoittelu, sähköpostihaastatteluja"
   "Aapo", "Valokuvaus, mallien rakentaminen, teknologioihin tutustuminen"
   "Jaan", "Blogin hallinointia ja kirjoittelua, potree malli, "
   "Juhani", "Lähdemateriaalin hankkiminen, Yritysten haastattelu, 3D-malli (potree/JS)"
   "Antti", "Haastis pohja, yleisiä suunnitteluja ja pohdintoja"


Kommunikaatio
-------------


Kehittyminen
------------


Arviointimatriisi
-----------------

.. csv-table::
   :header: "Mielestäni...", "tämä onnistui todella hyvin", "tämä sujui ihan OK", "tämä meni pieleen"

   "ymmärsimme, mitä projektissamme pitäisi tehdä samalla tavalla", "", "", ""
   "ymmärsimme asiakkaamme tarpeet", "", "", ""
   "keskustelimme riittävästi keskenämme", "", "", ""
   "osasimme ratkaista konfliktit", "", "", ""
   "meillä oli yhtenevät tavoitteet projektimme suhteen", "", "", ""
   "ymmärsin hyvin, mitä muut ryhmässäni tekevät", "", "", ""
   "olimme sopineet yhteisistä toimintatavoistamme", "", "", ""
   "olimme laatineet yhteisen aikataulun", "", "", ""
   "minulla oli hyvä käsitys, mitä muut odottavat minulta", "", "", ""
   "ryhmällämme oli johtaja", "", "", ""
   "kaikki ryhmän jäsenet työskentelivät tasapuolisesti", "", "", ""
   "saimme projektiimme riittävästi tukea", "", "", ""
