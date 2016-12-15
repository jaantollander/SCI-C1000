SCI-C1000 - Loppuraportti
*************************

Tiivistelmä
===========

Ongelma
-------
Ryhmän alkuperäisenä aihealueena oli kolmiulotteisten mallien rakentaminen valokuvien pohjalta sekä selvittää teknologiaan liittyviä liiketoimintamahdollisuuksia. Useiden potentiaalisten mahdollisuuksien joukosta potentiaalisimpana ja mielenkiintoisimpana vaihtoehtona valittiin sisätilapaikannus.


Sisätilapaikannukseen liittyvä fundamentaalinen ongelman on, ettei GPS-järjestelmää voida käyttää sisätilapaikannukseen rakenteiden estäessä suoran yhteyden paikannussatelliitteihin tehden siitä epätarkan ja epäluotettavan. Tämän takia sisätilapaikannukseen on kehitetty monia vaihtoehtoisia menetelmiä kuten *WiFi-kolmiomittaus*, *Bluetooth signaalitolpat*, *Maan magneettikentän mittaus*, *Kiihtyvyysanturimittaus* ja *Valokuviin pohjautuva paikannus*.


Osa järjestelmistä kuten *Bluetooth signaalitolpat* ja *WiFi-kolmiomittaus* edellyttävät kalliin infrastruktuurin asentamista tilaan. Toisaalta infrastruktuurittomissa menetelmissä, kuten kiihtyvyysanturimittauksessa, tarkkuus on usein paikantamiseen riittämätön. `Indoor Atlas <http://www.indooratlas.com/>`_ on kehittänyt *maan magneettikentän mittaukseen* perustuvan järjestelmän, joka on toimiva ja sinällään *kuvien paikantamista* käytännöllisempi ratkaisu, mutta se ei tarjoa käyttäjän katselusuuntaa, mikä on edellytys virtuaali- tai lisätyn todellisuuden hyödyntämiseen.


Ratkaisu
--------
Ryhmän esittämä ratkaisu sisätilapaikannusongelmaan perustuu kolmiulotteisen pistepilven rakentamiseen valokuvista. Pistepilven avulla käyttäjä voidaan paikantaa, kun käyttäjän ottama kuva sijoitetaan pistepilveen vertaamalla sitä jo tunnettuihin valokuviin. Samalla olemassa olevaa mallia voidaan päivittää lähetetyillä kuvilla.


Ratkaisun **vahvuuksia** ovat tehokas ja tarkka käyttäjän paikantaminen, sekä mahdollisuus rakentaa kolmiulotteinen malli paikannettavasta alueesta. Suurena erona moneen muuhun paikannusteknologiaan on kyky ratkaista käyttäjän katseen suunta, mikä mahdollistaa teknologian käyttämisen lisätyn- ja virtuaalitodellisuuden sovelluskohteissa. Lisäksi ratkaisu perustuu puhtaasti ohjelmistoihin eikä vaadi infrastruktuurin asentamista, mikä tekee siitä paremmin *skaalautuvan* sekä pienentää *ylläpitokustannuksia*.


Ratkaisun **heikkouksia** on sen teknologinen haastavuus: mallin rakentaminen ja käyttäjän paikantaminen vaativat paljon laskentatehoa ja aikaa. Lisäksi suuria haasteita aiheuttaa tietokonenäköön pohjautuvan yksityiskohtien tunnistamisen tarkkuus. Tarkkuuteen on kuitenkin odotettavissa tulevaisuudessa merkittäviä parannuksia, sillä tietokonenäkö on nykyään erittäin suosittu tutkimuskohde.


Paikannuspalvelua myydään suurille julkisille tiloille kokonaisvaltaisena ohjelmistopalveluna. Alkuvaiheessa myynti kohdistetaan pääasiassa hypermarketeille ja kauppakeskuksille, myöhemmin laajentaen myös muihin julkisiin tiloihin, kuten kirjastoihin ja museoihin. Palvelun perushinnoittelu pohjautuu käyttäjämäärään sekä mallinnettavan tilan kokoon ja monimutkaisuuteen, mutta palveluun on mahdollista lisätä myös räätälöityjä ominaisuuksia asiakkaan toiveiden mukaan lisämaksua vastaan.


Ryhmätyö
========

Menetelmät
----------
Projektin alussa ryhmän tehtävä ja määränpää olivat vielä pimennossa. Alun epämääräinen ja laaja aiherajaus 2D kuvista 3D malleja luovaan SfM (Structure from Motion)-menetelmään antoi ryhmällemme vapautta tutkia ongelmaa tarkemmin. Päätimme, että tutustuttuamme teknologiaan ja vaihtoehtoisiin menetelmiin kykenisimme valitsemaan uuden rajauksen, jonka ympärille lopullinen liiketoimintamalli voitiin sitoa. Jo alussa oli selvää, että ryhmänä keskitymme vahvasti 3D-mallinnukseen. Tästä saatiin muodostettua ensimmäisessä ryhmätapaamisessa seitsenhenkiselle ryhmällemme nimi: **3+4Dudes**.

Alussa otimme jokainen itsenäisesti selvää teknologian perusperiaatteista, miten menetelmä toimii ja mitä muut tutkijat ja kehittäjät ovat aihealueen ympärillä tutkineet tai toteuttaneet.

Artikkeleihin, raportteihin sekä aiheeseen liittyviin blogeihin ja videoihin tutustumalla saimme alkuun muodostettua kattavan näkemyksen siitä, mitä menetelmällä voi saada aikaan.

Jo toisen viikon alussa tapasimme professori Antti Ylä-Jääsken, jolta saimme korvaamatonta tietoa heidän tutkimuksestaan menetelmään liittyen sekä kattavaa tietoa vaihtoehtoisista ohjelmistoista, joilla 3D-mallin voisi rakentaa. Aiempi tutustuminen saatavilla oleviin ohjelmistoihin oli jo antanut ymmärtää, että saatavilla oli erittäin tehokkaita ja optimoituja, vapaan lähdekoodin sekä akateemiseen käyttöön vapaita toteutuksia. Oman SfM-algoritmin rakentamisen työläyden ja aikarajoitteiden takia päädyimme käyttämään VisualSFM-ohjelmaa [visualSFM]_ 3D-mallin luomisessa.

Ryhmänä emme kuitenkaan kokeneet pelkän 3D-mallin muodostamisen tarjoavan riittävää liiketoimintapotentiaalia, joten haimme työhömme inspiraatiota professori Ylä-Jääsken tutkimusryhmän iMoon-sovelluksesta [iMoon]_. iMoon käyttää SfM-tekniikkaa vertaamalla käyttäjän ottamaa kuvaa aiemmin tilasta muodostettuun 3D-pistepilveen ja pystyy määrittämään sijainnin, jossa kamera oli kuvan ottamishetkellä. Vastaavaa paikannustekniikkaa haluttiin ideatasolla käyttää työssämme tarjoamaan lopullisen palvelumme ostaville asiakkaille konkreettista hyötyä esimerkiksi käyttäjien ja tuotteiden paikannuksella tai asiakkaiden reitityksellä kartalla.


Kommunikaatio
-------------
Ryhmämme kokoonpano kasattiin kurssihenkilökunnan puolesta samasta aiheesta, meidän tapauksessamme 3D-mallintamisesta, kiinnostuneiden opiskelijoiden joukosta eri koulutusaloilta. Näin ollen monet ryhmämme jäsenet eivät tunteneet entuudestaan toisiaan saatikka olleet olleet yhteyksissä keskenään aiemmin. Ryhmätyön onnistumisen kannalta on kuitenkin tärkeää mahdollistaa ryhmän sisäinen kommunikaatio mahdollisimman kivuttomasti. Ensimmäinen kommunikaatioon liittyvä haaste olikin saada kaikki ryhmän jäsenet kiinni ja valita jokin kaikille sopiva tapa pitää yhteyttä. Nykyisen pikaviestien aikakauden ansiosta tämä haaste selätettiin kuitenkin nopeasti, sillä jo ennen ensimmäistä yhteistä tapaamista Markus perusti Telegram-ryhmän, jonne lähetti kutsun sähköpostitse ryhmän muille jäsenille. Telegramin käyttö oli kaikille tuttua ja ryhmä olikin nopeasti koolla.

Telegram osoittautuikin nopeasti luonnolliseksi keskustelukanavaksi ryhmällemme, sillä se mahdollisti kysymysten ja kommenttien vaihtamisen reaaliaikaisesti koko ryhmän kesken. Lisäksi yhteisen kanavan kautta oli helppo tavoittaa myös yksittäisiä ryhmän jäseniä Telegramiin määriteltyjen nimimerkkien ja yksityisviestien avulla. Myös tiedostojen jakaminen ryhmän kesken onnistui kätevästi Telegramin kautta. Tärkeiden tiedostojen kokoamiseen ja jäsentelyyn käytimme lisäksi Google Driven pilvipalveluita, joskin siellä ei varsinaista kommunikaatiota ryhmän kesken tapahtunut.

Telegramin helppoudesta huolimatta oli kuitenkin selvää, että ryhmän keskinäisen sidoksen lisäämiseksi ja saatujen tuloksien kokoamiseksi yhteen oli tarpeen tavata säännöllisesti kasvotusten. Organisoinnin helpottamiseksi sovimme viikottaisen vakioajan, jolloin ryhmämme kokoontui yhteen johonkin sopivaan työtilaan koululla. Näistä torstaitapaamisista on kerrottu tarkemmin luvussa (`Kehittyminen`_). Tapaamisissa ajatuksia voitiin vaihtaa niin, että niistä syntyi keskustelua ryhmän kesken. Saatoimme välillä jutustella hetken projektin ulkopuolisistakin asioista ja näin tiivistää ryhmähenkeämme.

Pääasiassa kommunikointi toimi odotetulla tavalla. Projektiin liittyvät asiat hoidettiin yhteisellä kanavalla, jolloin kukaan ryhmän jäsenistä ei joutunut pimentoon muidenkaan tekemisistä ja kohtaamista haasteista. Torstain tapaamiset toimivat erinomaisena yhteenvetona viikon aikana saaduista tuloksista ja ponnahduslautana tulevan viikon tavoitteiden asettamiseen. Myös kurssin vaatimat palautettavat työt katsottiin säännöllisesti läpi viikoittaisissa tapaamisissa.


Kehittyminen
------------
Ryhmätyömme oli aluksi varsin rosoista: elimme varsin anarkistista unelmaa, jossa jokainen ryhmän jäsen oli samanarvoinen. Alun ideointiin tällainen työskentelytapa kenties toimiikin ja idean rajaaminen sujui varsin hyvin ilman varsinaista johtamista. Kurssin henkilökunnan puolelta vaadittiin kuitenkin yhden johtajan nimeämistä ja valitsimme tehtävään yksimielisesti Misamatin. Myöhemmissä vaiheissa johtajan määrittäminen osoittautui ensiarvoisen tärkeäksi projektin hallinnoimiseksi ja pitämiseksi aikataulussa. Työskentelytapamme mukautui hyväksi havaittuihin normeihin ja erityisesti mukaan tulivat torstaiset tapaamiset. 

Torstaiset tapaamiset olivatkin erinomainen kehityksen paikka, sillä onnistuimme ryhmänä kehittämään työskentelytapojamme viikosta toiseen vielä kurssin loppupuolellakin. Alussa keskityimme varsin vahvasti omiin osa-alueisiimme korostaen erityisesti teknistä puolta, mihin osittain kurssin aikataulutuskin ohjasi. Kurssin loppupuolella teimme huomattavasti enemmän myös ei-teknistä ideointia ja ideoiden jakamista juurikin ryhmänä. Jakauduimme lähes itsestään kahteen karkeasti jaettuun tiimiin, joista toinen keskittyi teknisen toteutuksen hiomiseen toisen huolehtiessa tukitoiminnoista ja liiketoiminnan kehittämisestä. Toki tehtäviä vaihdettiin keskenään ja ristiin, mutta nämä karkeat suuntaviivat säilyivät läpi koko projektin.

Sisäisestä tiimijaosta huolimatta kenties tärkein yhteinen oppi ryhmällemme oli kuitenkin ideoiden jakamisen voima: monesti ryhmän paras edistyminen tapahtui juuri ryhmätapaamisessa ryhmän jäsenten jakaessa omia edistymisaskeliaan. Yllättäen aivan ulkopuolinen näkemys moneen ongelmaan auttoi, jos ei suoraan ratkaisemaan ongelmaan niin vähintään viitoittamaan oikeaa tietä ongelman ratkaisemiseksi. Tästä jäikin konkreettinen oppi vietäväksi myös työelämään: kommunikaatio tiimin eri jäsenten välillä, erityisesti teknisyyden akselin poikki, voi osoittautua hedelmälliseksi monissa, yllättävissäkin asioissa. Tämä osio ryhmätyöstämme kehittyi erityisen paljon kurssin aikana, kunhan opimme puhumaan toisillemme omasta edistymisestämme.

Hyvänä harjoitteluna toimi varsin luonnollinen roolien vaihtaminen ja eri tehtävien tekeminen: fyysikko pohti liiketoimintaa ja tutalainen työsti 3D-mallia leikkikaivureista. Oli silmiä avaavaa ja toisaalta rohkaisevaa, miten paljon uusista asioista pystyi oppimaan yksinkertaisesti niitä tekemällä. Vaikka harvalla ryhmäläisellä oli kokemusta monista tekemistämme asioista, niitä tekemällä olemme saavuttaneet varsin hyvät pohjatiedot kurssilla käsitellyistä aiheista. 

Loppuvaiheessa projektia oli ryhmätyöskentelymme luovaa ja tarkoitushakuista - tosin ehkä myös lähestyvillä määräajoilla oli vaikutusta asiaan. Misamatin lempeässä ohjauksessa eri ihmiset tekivät ristiin eri tehtäviä ja tulosta todella syntyi: koostimme kasaan hyvän posterin ja vaikuttavan demon Grande Finalea varten. Ryhmätyömme oli vapaata parhaalla mahdollisella tavalla: tehtäville löytyi omat tekijänsä ja kaverit paikkasivat siinä, missä joku ei ehtinyt. Kurssin aikana ryhmän jäsenet saivatkin arvokasta kokemusta toimimisesta uusien ihmisten kanssa sekä erilaisten vuorovaikutus- ja työskentelytyylien yhteensovittamisessa.

Itse aiheestamme, 3D-mallintamisesta SfM-teknologialla, oli yllättävää huomata, että yksityishenkilöille saatavilla oleva avoimen lähdekoodin teknologia on jo nykypäivänä siinä pisteessä, että 3D-mallien laskeminen sadoista valokuvista onnistuu kohtuullisessa ajassa tavallisella pöytäkoneella. Opimme myös huomioimaan valokuvauksellisia seikkoja alkuperäisiä kuvia otettaessa ja arvioimaan erilaisten ilmiöiden, kuten heijastavien tai läpinäkyvien pintojen vaikutusta lopulliseen malliin. Liiketoimintapotentiaalin arvioiminen antoi ryhmällemme käyttökelpoiset viitekehykset erilaisten elementtien huomioimiseen ja huomasimmekin, että valmiin viitekehyksen käyttäminen helpottaa suunnitteluprosessia. Valmista kehystä käyttäen pystyttiin myös varmistamaan, että kaikki osa-alueet tulee huomioitua ennen kuin liiketoimintaa ollaan käynnistämässä suuremmassa mittakaavassa.


Henkilökohtainen kehitys
------------------------

Markus
^^^^^^
Toimin ryhmässä pääasiassa varsinaista teknistä toteutusta tukevissa osa-alueissa, kuten liiketoimintapotentiaalin analysoimisessa, projektin etenemisen organisoinnissa ja esitysten pitämisessä. Tämän vuoksi omalta osaltani osa teknisistä yksityiskohdista jäi jokseenkin pimentoon, mutta koen silti oppineeni paljon valokuviin pohjautuvasta 3D-mallintamisesta ja siihen liittyvistä haasteista. Ennen kurssia käsitykseni mallintamisen mahdollisuuksista oli varsin rajallinen, mutta pidin kuitenkin teknologiaa mielenkiintoisena ja potentiaalisena tulevaisuuden sovelluksia silmällä pitäen. Kurssin jälkeen hallitsen keskeisimmät vaiheet 3D-mallin muodostamisessa ja tiedän, mitä asioita tulee ottaa huomioon valokuvia otettaessa ja itse mallia luotaessa. Olin myös varsin positiivisesti yllättynyt avoimen lähdekoodin työkalujen tasosta ja tarjoamista mahdollisuuksista.

Mitä taas tulee tukitoimiin, koen että suurin kehitys tapahtui henkilökohtaisen esiintymisen saralla. Koen kurssin aikana saaneeni arvokasta kokemusta suurelle yleisölle esiintymisestä ja esitysten rakenteen suunnittelemisesta yleisöä silmällä pitäen. Tämän lisäksi osa liiketoimintapotentiaalin arvioimiseen käytetyistä työkaluista oli uusia, vaikka itse ajatus prosessin taustalla olikin tullut jo tutuksi aiemmilta kursseilta.


Lauri
^^^^^
Toimin ryhmässä lähinnä tukitoimissa: kirjoitin blogia ja ideoin eri tehtäviä yhdessä muiden kanssa. Uskon kuitenkin, että juuri näiden tukitoimien kautta pääsin varsin syvälle mukaan projektiin. Pääsin myös kokeilemaan paljon eri rooleja projektia tehdessä: perinteisestä kirjallisuustutkimuksesta teknologioiden vertailupostausta varten bisnesmallin kehittämispöhinään. Minusta ideamme myynnin ja liiketoiminnan pohtiminen oli mielenkiintoinen ongelma, jonka parissa en ole päässyt työskentelemään ennen tätä projektia (Tuotantotalous 1 -kurssia lukuun ottamatta). Näin fyysikkona on myönnettävä, että yllättävän paljon ajatustyötä ja ideointia tähän kuuluisaan käsienheilutteluunkin menee. Lisäksi oli yllättävää, miten paljon ulkopuolinen näkemys ryhmätapaamisissa auttoi omien ongelmien ratkaisemisessa. 

Lisäksi pääsin luonnollisesti tutustumaan varsin yksityiskohtaisesti eri sisätilapaikannusmetodeihin. Lisäksi on sanottava minunkin vaikuttuneen mahdollisuuksista, joita avoimen lähdekoodin kirjastot tarjoavat. Kuten kuulin jutellessani Grande Finalessa muiden ryhmien kanssa: miksi tehdä itse jos joku muu on jo kerran tehnyt?


Jaan
^^^^
Toimin ryhmässä blogin teknisestä puolesta vastaavana. Tähän kuului blogin visuaalisesta ilmeestä huolehtiminen, blogikirjoitusten lukeminen, editointi julkaistavaan muotoon, kuvien ja linkkien lisääminen, kirjoitusten julkaiseminen sekä 3D-mallien laittaminen nettiin. Autoin myös kirjoitusten kirjoittamisessa. 

Tarve tutustua 3D-mallintamiseen ja siihen liittyviin ohjelmistoihin kehitti taitoja tällä alueella. Ilman tätä projektia en olisi välttämättä joutunut opettelemaan näitä taitoja enkä olisi nähnyt alaan liittyviä haasteita.

Blogista huolehtiminen kehitti web-kehitystaitojani, koska käytimme staattista blogigeneraattoria valmiin alustan sijaan.


Misamatti
^^^^^^^^^
Pääasiallinen roolini oli toimia ryhmämme vetäjänä ja auttaa tarpeen mukaan projektin eri osa-alueissa, painottuen kuitenkin tukitoimiin. Ryhmänvetäjänä koin vastuukseni huolehtia siitä, että kaikilla ryhmän jäsenillä oli tasapuolinen mahdollisuus osallistua aktiivisesti projektin työstämiseen ja jokseenkin selkeä käsitys projektin kulloisestakin vaiheesta. Tämä oli kieltämättä hieman haastavaa itsellenikin, sillä projektin edetessä pienet korjausliikkeet tavoitteissamme olivat yleisiä tietojen lisääntyessä tai ongelmatilanteen kohdatessamme. Lisäksi ryhmänvetäjän tehtäviin kuului myös varmistaa viikottaisen tavoitteen täyttyminen (blogipostaus konkreettisimpana esimerkkinä kurssin puitteissa). Tässä ei kuitenkaan ollut suurta ongelmaa motivoituneen ryhmämme ansiosta.

Projektin alkaessa perehdyin vastuuopettajamme tutkimusryhmän tuloksiin ja näin sain hyvän käsityksen valokuviin pohjautuvan paikantamisen mahdollisuuksista. Projektissa autoin blogipostausten suunnittelussa, kirjoittamisessa ja materiaalin keräämisessä. Pääsin myös hyödyntämään aiempaa osaamista mm. posterin suunnittelussa, ja näin vahvistin käsitystäni siitä, että ryhmätyöskentelyn hyödyt syntyvät ryhmän keskisestä synergiasta: kun jokainen tuo soppaan omaa osaamistaan, saadaan tuloksia nopeasti ja tehokkaasti.


Antti
^^^^^
En ottanut ryhmätyössämme mitään vastuutehtävää, vaan tein kaikkia sekalaisia tehtäviä (esimerkiksi haastattelupohja, yhteiset pohdinnat ja ideoinnit). Tämän vuoksi sain hyvän läpileikkauksen pien/startup -yrityksen arjesta tehdessäni erilaisia pieniä ja suuria hommia. Kurssi on myös hyvin ajankohtainen startuppien suosion ollessa tällä hetkellä katossa, vaikkakin jotkin tehtävänannot tuntuivat jopa turhauttavilta.

Kurssin aikana sain hyvän perustietämyksen valokuviin perustuvasta mallintamisesta ja tietysti pintaraapaisun muihin vaihtoehtoihin. Kurssi myös vahvisti käsitystäni heikkouksistani ja vahvuuksistani, sekä sain pientä tuntumaa miten liiketoimintapotentiaalia kehitetään ja arvioidaan.


Juhani
^^^^^^
Tehtäväni projektissa painottui lähdemateriaalin, teknologian ja pistepilvimallin tutkimiseen. Suunnittelin ja rakensin myös Grande Finaleen esityksen, jossa kameraa lennätettiin pistepilvessä ja visualisoitiin reitti mallinnetussa tilassa. Suoritin myös yrityshaastatteluja, joiden avulla saimme inspiraatiota liiketoimintamallin suunnitteluun. Liiketoimintapotentiaalin arviointi ja -mallin suunnittelu olivat erittäin mielekkäitä ja opettavaisia. Myös esitysten pitämisestä, keskeneräisten töiden esittelystä ja yleisesti ryhmätyöskentelystä oppi kurssin aikana paljon. Myös itsenäisen työskentelyn aikataulutuksesta ryhmän osana sai hyödyllistä kokemusta.


Aapo
^^^^
Minun tehtäväni projektissa oli keskittyä ratkaisun teoreettisen taustan tutkimiseen sekä prototyypin rakentamiseen liittyviin käytännön tehtäviin. Ryhmätyöskentely on minulle entuudestaan erittäin tuttua, mutta tämä kurssi poikkesi aikaisemmista kokemuksistani eniten siinä, että työn päämäärä ei ollut aivan yhtä selkeä. Tämä mahdollisesti johtui siitä, että aikaisemmissa kokemuksissani on aina ollut selkeä asiakas/pomo ja niiden lopputulos on ollut helpommin käsitettävä tuote/raportti. Normaalisti, kun projektille asetettu tavoite on saavutettu, se on luovutusta vaille valmis. Tässä projektissa vähäisestä alkutiedosta johtuen projektitavoitteet ovat sisältäneet paljon epävarmuustekijöitä, minkä seurauksena ne ovat eläneet ryhmän edistymisen mukana. Jämäkän auktoriteetin tuominen ryhmään olisi varmasti myös selkiyttänyt työskentelyä. Pähkinänkuoressa siis opin ryhmätyöskentelemään tavallista epävarmemmissa olosuhteissa sekä ymmärtämään projektijohtajan roolin tärkeyttä. Seuraavissa kappaleissa käsittelen saamiani oppeja ryhmäni käsittelemästä teemasta.

Ennen kurssin alkua kolmiulotteisten mallien rakentaminen valokuvien pohjalta oli minulle täydellinen musta laatikko: sisään tuupattiin valokuvia ja muutaman konejumalille annetun uhrilahjan jälkeen ulos singahti lähes täydellinen digitaalinen kopio valokuvien kohteesta. Kurssin aikana kuitenkin pääsin tarkemmin tämän prosessin tekniseen toteutukseen ja nyt tiedän jokaisen tietokoneen sen aikana suorittaman laskutoimituksen merkityksen.

Laskutoimitusten sarja on kuitenkin niin monimutkainen, että rohkenen väittää tuskin kenenkään täysin ymmärtävän millaisia vaatimuksia se asettaa mallin pohjana toimiville valokuville. Internetistä löytyy eri henkilöiden hyväksi havaitsemia toimintatapoja esimerkiksi valokuvien valotukseen ja kuvakulmiin liittyen, mutta jokainen malli on täysin uniikki, joten niitä voidaan käyttää vain karkeana lähtökohtana mallin rakentamiselle. Tämä tuntemattomaan sukeltaminen ja uusien ’parhaiden’ toimintatapojen etsiminen oli varmasti yksi kurssin tärkeimpiä opetuksia. Näin jälkikäteen voin todeta järjestelmällisten ja hyvin dokumentoitujen kokeiden järjestämisen välttämättömäksi työkaluksi uuden etsimisessä. Tässä projektissa tehtyjen koejärjestelyjen ja niiden tulosten tarkemmalla analysoinnilla olisivat tulokset olleet vieläkin parempia.

Aluksi pyrittiin selvittämään, mikä toimii hyvin pienessä mittakaavassa ja sen jälkeen skaalaamaan se tavoitteeksi asetettuun mittakaavaan. Nopeasti havaittiin käytettävissä olevan laskentatehon ja täten valokuvien lukumäärään muodostuvan merkittäväksi haasteeksi. Pienellä määrällä valokuvia on hankala saada muodostettua tarkkaa mallia suuresta tilasta, mutta optimoidulla valokuvaustekniikalla päästiin kuitenkin paikannuskäytössä riittävään lopputulokseen. Tärkeänä havaintona teknologiaan yleisesti liittyen on laskentatehon tarve. Tulevaisuudessa tehokkaampien algoritmien kehittäminen erityisesti yksityiskohtien tunnistamiseen tulee olemaan tärkeä kehityskohde.


Arviointimatriisi
-----------------

.. csv-table:: *Koonti arviointilomakkeiden tulosten jakautumisesta*
   :header: "Mielestäni...", "tämä onnistui todella hyvin", "tämä sujui ihan OK", "tämä meni pieleen"

   "ymmärsimme, mitä projektissamme pitäisi tehdä samalla tavalla", "6", "1", "0"
   "ymmärsimme asiakkaamme tarpeet", "1", "6", "0"
   "keskustelimme riittävästi keskenämme", "1", "4", "2"
   "osasimme ratkaista konfliktit", "3", "4", "0"
   "meillä oli yhtenevät tavoitteet projektimme suhteen", "6", "1", "0"
   "ymmärsin hyvin, mitä muut ryhmässäni tekevät", "0", "7", "0"
   "olimme sopineet yhteisistä toimintatavoistamme", "2", "5", "0"
   "olimme laatineet yhteisen aikataulun", "2", "5", "0"
   "minulla oli hyvä käsitys, mitä muut odottavat minulta", "2", "4", "1"
   "ryhmällämme oli johtaja", "5", "2", "0"
   "kaikki ryhmän jäsenet työskentelivät tasapuolisesti", "2", "5", "0"
   "saimme projektiimme riittävästi tukea", "6", "1", "0"


Yhteenveto arviointilomakkeista
-------------------------------
Suurin haaste ryhmämme toimintatavoissa oli selkeästi kommunikaation puute. Työt tehtiin pääasiassa itsenäisesti ja tulokset koottiin yhteisesti. Tämä olisi ollut mahdollista korjata jakamalla tehtäväkokonaisuuksia alusta alkaen pienille tiimeille yksittäisten henkilöiden sijaan. Myös viikoittaisissa yhteisissä tapaamisissa oli parantamisen varaa, sillä varsinkin alkupuolella kurssia tapaamisiin osallistui ainoastaan osa ryhmästä. Ryhmätapaamiset kuitenkin sujuivat loppupuolella kurssia huomattavasti paremmin. Nämä kaksi ongelmaa aiheuttivat myös sen, että työnjako oli ajoittain hieman epäselvää osalle ryhmän jäsenistä, eikä ryhmä päässyt toimimaan tehokkaasti.


Tuloksista huomataan (`Arviointimatriisi`_), että kommunikaatiohaasteista huolimatta ryhmällämme oli kuitenkin selkeä käsitys projektin tavoitteista ja odotetusta tuloksesta. Tämä johtui luultavasti siitä, että aiheemme oli rajattu selkeästi heti ensimmäisen vastuuopettajan tapaamisen jälkeen. Mikäli aiheemme olisi dramaattisesti muuttunut kesken kurssin uuteen suuntaan, olisi mennyt luultavasti liian kauan, että ryhmälle olisi muodostunut uudestaan yhteinen ja selkeä käsitys projektin suunnasta. Onneksemme aiheen määrittely pysyi samana koko kurssin ja pystyimme keskittymään parhaan mahdollisen lopputuloksen tuottamiseen alusta alkaen.


.. [iMoon] Dong, J., Xiao, Y., Noreikis, M., Ou, Z., & Ylä-Jääski, A. (2015). iMoon : Using Smartphones for Image-based Indoor Navigation Categories and Subject Descriptors. Proceedings of the ACM Conference on Embedded Networked Sensor Systems, 85–97. http://doi.org/10.1145/2809695.2809722

.. [visualSFM] Wu, C., & others. (2011). VisualSFM: A visual structure from motion system.