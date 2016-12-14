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
Ryhmämme kokoonpano kasattiin kurssihenkilökunnan puolesta samasta aiheesta, meidän tapauksessamme 3D-mallintamisesta, kiinnostuneiden opiskelijoiden joukosta eri koulutusaloilta. Näin ollen monet ryhmämme jäsenet eivät tunteneet entuudestaan toisiaan saatikka olleet olleet yhteyksissä keskenään aiemmin. Ryhmätyön onnistumisen kannalta on kuitenkin tärkeää mahdollistaa ryhmän keskinen kommunikaatio mahdollisimman kivuttomasti. Ensimmäinen kommunikaatioon liittyvä haaste olikin saada kaikki ryhmän jäsenet kiinni ja valita jokin kaikille sopiva tapa pitää yhteyttä. Nykyisen pikaviestien aikakauden ansiosta tämä haaste selätettiin kuitenkin nopeasti, sillä jo ennen ensimmäistä yhteistä tapaamista Markus perusti Telegram-ryhmän, jonne lähetti kutsun sähköpostitse ryhmän muille jäsenille. Telegrammin käyttö oli kaikille tuttua ja ryhmä olikin nopeasti koolla.


Telegram osoittautuikin nopeasti luonnolliseksi keskustelukanavaksi ryhmällemme, sillä se mahdollisti kysymysten ja kommenttien vaihtamisen reaaliaikaisesti koko ryhmän kesken. Lisäksi yhteisen kanavan kautta oli helppo tavoittaa myös yksittäisiä ryhmän jäseniä Telegrammiin määriteltyjen nimimerkkien ja yksityisviestien avulla. Myös tiedostojen jakaminen ryhmän kesken onnistui kätevästi Telegrammin kautta. Tärkeiden tiedostojen kokoamiseen ja jäsentelyyn käytimme lisäksi Google Driven pilvipalveluita, joskin siellä ei varsinaista kommukaatiota ryhmän kesken tapahtunut.


Telegrammin helppoudesta huolimatta oli kuitenkin selvää, että ryhmän keskinäisen sidoksen lisäämiseksi ja saatujen tuloksien kokoamiseksi yhteen oli tarpeen tavata säännöllisesti kasvotusten. Organisoinnin helpottamiseksi sovimme viikottaisen vakioajan, jolloin ryhmämme kokoontui yhteen johonkin sopivaan työtilaan koululla. Näistä torstaitapaamisista on kerrottu tarkemmin seuraavassa kappaleessa. Tapaamisissa ajatuksia voitiin vaihtaa niin, että niistä syntyi keskustelua ryhmän kesken. Saatoimme välillä jutustella hetken projektin ulkopuolisistakin asioista ja näin tiivistää ryhmähenkeämme.


Pääasiassa kommunikointi toimi odotetulla tavalla. Projektiin liittyvät asiat hoidettiin yhteisellä kanavalla, jolloin kukaan ryhmän jäsenistä ei joutunut pimentoon muidenkaan puuhasteluista. Torstain tapaamiset toimivat erinomaisena yhteenvetona viikon mittaan saaduista tuloksista ja ponnahduslautana tulevan viikon tavoitteiden asettamiseen.


Kehittyminen
------------
Ryhmätyömme oli aluksi varsin rosoista: elimme varsin anarkistista unelmaa, jossa jokainen ryhmän jäsen oli samanarvoinen. Alun ideointiin tällainen työskentelytapa kenties toimiikin ja idean rajaaminen sujui varsin hyvin ilman varsinaista johtamista. Hieman sattumalta ja Herran armosta laskeutui kuitenkin keskuuteemme se kohtalokas päivä, jolloin Misa-Matista tuli pienen joukkiomme johtaja. Työskentelytapamme mukautui hyväksi havaittuihin normeihin ja erityisesti mukaan tulivat torstaiset tiimipalaverit.


Torstaiset tiimipalaverit olivatkin erinomainen kehityksen paikka: vähittelen, viikojen myötä kehittyi ryhmätyömme. Alussa keskityimme varsin vahvasti omiin tontteihimme (ja teekkarimaisesti erityisesti tekniseen puoleen - tosin tähän projektin aikataulukin ohjasi), mutta loppua kohti teimme huomattavasti enemmän ideointia ja ideoiden jakamista juuri ryhmänä. Varsin luonnollisesta painovoimaa noudattaen solahdimme karkeisiin tiimeihin: toiset tekivät enemmän teknistä toteutusta kuin muut. Toki tehtäviä vaihdettiin ja tehtiin ristiin, mutta nämä karkeat suuntaviivat pysyivät.


Kuitenkin tiimijaosta huolimatta kenties tärkein yhteinen oppi ryhmällemme oli kuitenkin ideoiden jakamisen voima: monesti ryhmän paras edistyminen tapahtui juuri ryhmätapaamisessa ryhmän jäsenten jakaessa omia edistymisaskeliaan. Yllättäen aivan ulkopuolinen näkemys moneen ongelmaan auttoi jos ei suoraan ratkaisemaan ongelmaan niin vähintään viitoitti meille oikean polun ongelman ratkaisemiseksi. Tästäpä viesti työelämään: kommunikaatio tiimin eri jäsenten välillä, erityisesti teknisyyden akselin poikki, voi osoittautua hedelmälliseksi monissa, yllättävissäkin asioissa. Tämä osio ryhmätyöstämme kehittyi erityisen paljon kurssin aikana, kunhan opimme puhumaan toisillemme omasta edistymisestämme.


Hyvänä harjoitteluna toimi varsin luonnollinen roolien vaihtaminen ja eri tehtävien tekeminen: fyysikko pohti liiketoimintaa ja tutalainen työsti 3D-mallia leikkikaivureista. Oli silmiä avaavaa ja toisaalta rohkaisevaa, miten paljon uusista asioista pystyi oppimaan yksinkertaisesti niitä tekemällä. Vaikka harvalla ryhmäläisellä oli kokemusta monista tekemistämme asioista, niitä tekemällä olemme saavuttaneet varsin hyvät pohjatiedot kurssilla käsitellyistä aiheista.


Loppuvaiheessa projektia oli ryhmätyöskentelymme luovaa ja tarkoitushakuista - tosin ehkä myös lähestyvillä kalmanrajoilla oli vaikutusta asiaan. Misa-Matin lempeässä ohjauksessa eri ihmiset tekivät ristiin erityyppisiä tehtäviä ja tulosta todella syntyi: vedimme kasaan hyvän posterin ja vaikuttavan demon Grande Finalea varten. Ryhmätyömme oli vapaata parhaalla mahdollisella tavalla: hommille löytyivät omat tekijänsä ja kaverit paikkasivat siinä, missä joku ei ehtinyt.


Henkilökohtainen kehitys
------------------------

Markus
^^^^^^
Toimin ryhmässä pääasiassa varsinaista teknistä toteutusta tukevissa osa-alueissa, kuten liiketoimintapotentiaalin analysoimisessa, projektin etenemisen organisoinnissa ja esitysten pitämisessä. Tämän vuoksi omalta osaltani osa teknisistä yksityiskohdista jäi jokseenkin pimentoon, mutta koen silti oppineeni paljon valokuviin pohjautuvasta 3D-mallintamisesta ja siihen liittyvistä haasteista. Ennen kurssia käsitykseni mallintamisen mahdollisuuksista oli varsin rajallinen, mutta pidin kuitenkin teknologiaa mielenkiintoisena ja potentiaalisena tulevaisuuden sovelluksia silmällä pitäen. Kurssin jälkeen hallitsen keskeisimmät vaiheet 3D-mallin muodostamisessa ja tiedän, mitä asioita tulee ottaa huomioon valokuvia otettaessa ja itse mallia luotaessa. Olin myös varsin positiivisesti yllättynyt avoimen lähdekoodin työkalujen tasosta ja tarjoamista mahdollisuuksista.


Mitä taas tulee tukitoimiin, koen että suurin kehitys tapahtui henkilökohtaisen esiintymisen saralla. Koen kurssin aikana saaneeni arvokasta kokemusta suurelle yleisölle esiintymisestä ja esitysten rakenteen suunnittelemisesta yleisöä silmällä pitäen. Tämän lisäksi osa liiketoimintapotentiaalin arvioimiseen käytetyistä työkaluista oli uusia, vaikka itse ajatus prosessin taustalla olikin tullut jo tutuksi aiemmilta kursseilta.


Lauri
^^^^^
Toimin ryhmässä lähinnä tukitoimissa: kirjoitin blogia ja ideoin eri tehtäviä yhdessä muiden kanssa. Uskon kuitenkin, että juuri näiden tukitoimien kautta pääsin varsin syvälle mukaan projektiin. Pääsin myös kokeilemaan paljon eri rooleja projektia tehdessä: perinteisestä kirjallisuustutkimuksesta teknologien vertailupostausta varten bisnesmallin kehittämispöhinään. Minusta ideamme myynnin ja liiketoiminnan pohtiminen oli mielenkiintoinen ongelma, jonka parissa en ole päässyt työskentelemään ennen tätä projektia (Tuotantotalous 1-kurssia lukuunottamatta). Näin fyysikkona on myönnettävä, että yllättävän paljon ajatustyötä ja ideointia tähän kuuluisaan käsienheilutteluunkin menee. Lisäksi oli yllättävää, miten paljon ulkopuolinen näkemys ryhmätapaamisissa auttoi omien ongelmien ratkaisemisessa.


Lisäksi pääsin luonnollisesti tutustumaan varsin yksityiskohtaisesti eri sisätilapaikannusmetodeihin. Lisäksi on sanottava minunkin vaikuttuneen mahdollisuuksista, joita avoimen lähdekoodin kirjastot tarjoavat. Kuten kuulin jutellessani Grande Finalessa muiden ryhmien kanssa: miksi tehdä itse jos joku muu on jo kerran tehnyt?


Jaan
^^^^
Toimin ryhmässä blogin teknisestä puolesta vastaavana. Tähän kuului blogin visuaalisesta lookista huolehtiminen, blogi kirjoitusten lukeminen, editointi julkaistavaan muotoon, kuvien ja linkkien lisääminen, kirjoitusten julkaiseminen sekä 3D mallien laittaminen nettiin. Autoin myös kirjoitusten kirjoittamisessa.


Tarve tutustua 3D mallintamiseen ja siihen liittyviin ohjelmistoihin kehitti taitoja tällä alueella. Ilman tätä projektia en olisi välttämättä joutunut opettelemaan näitä taitoja enkä olisi nähnyt alaan liittyviä haasteita.


Blogista huolehtiminen kehitti web development taitojani, koska käytimme staattista blog generaattoria valmiin platformin sijaan.


Misamatti
^^^^^^^^^
Pääasiallinen roolini oli toimia ryhmämme vetäjänä ja auttaa tarpeen mukaan projektin eri osa-alueissa, painottuen kuitenkin tukitoimiin. Ryhmänvetäjänä koin vastuukseni huolehtia siitä, että kaikilla ryhmän jäsenillä oli tasapuolinen mahdollisuus osallistua aktiivisesti projektin työstämiseen ja jokseenkin selkeä käsitys projektin kulloisestakin vaiheesta. Tämä oli kieltämättä hieman haastavaa itsellenikin, sillä projektin edetessä pienet korjausliikkeet tavoitteissamme olivat yleisiä tietojen lisääntyessä tai ongelmatilanteen kohdatessamme. Lisäksi ryhmänvetäjän tehtäviin kuului myös varmistaa viikottaisen tavoitteen täyttyminen (blogipostaus konkreettisimpana esimerkkinä kurssin puitteissa). Tässä ei kuitenkaan ollut suurta ongelmaa motivoituneen ryhmämme ansiosta.


Projektin alkaessa perehdyin vastuuopettajamme tutkimusryhmän tuloksiin ja näin sain hyvän käsityksen valokuviin pohjautuvan paikantamisen mahdollisuuksista. Projektissa autoin blogipostausten suunnittelussa, kirjoittamisessa ja materiaalin keräämisessä. Pääsin myös hyödyntämään aiempaa osaamista mm. posterin suunnittelussa, ja näin vahvistin käsitystäni siitä, että ryhmätyöskentelyn hyödyt syntyvät ryhmän keskisestä synergiasta; kun jokainen tuo soppaan omaa osaamistaan, saadaan tuloksia nopeasti ja tehokkaasti.



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
