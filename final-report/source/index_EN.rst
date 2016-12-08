.. SCI-C1000 documentation master file, created by
   sphinx-quickstart on Fri Nov 25 10:00:36 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SCI-C1000 - Final Report
========================
.. SCI-projektikurssin tavoitteena on, että jokainen ryhmä omassa tehtävässään huomaa kehittyvänsä epämääräisen haasteen selkeyttämisessä, toimintasuunnitelmansa toteuttamisessa, ideansa liiketoimintapotentiaalin kartoittamisessa, ideansa kommunikoinnissa sekä ennen kaikkea ryhmänä työskentelemisessä.

.. Loppuraportin tavoitteena on kuvata saavuttamanne tulos, mutta ennen kaikkea dokumentoida ryhmänne oppimis- ja kehittymispolun reflektointi ryhmänä sekä ryhmän jäsenittäin. Loppuraportti on pohdinta prosessista ja edistymisestänne, jonka ryhmänä kävitte läpi:

.. 1) tiivistetty kuvaus haasteestanne ja ratkaisusta, johon päädyitte;

.. 2) miten kehityitte ryhmänä esim. yhteisten 'pelisääntöjen', työskentelytapojen, kommunikointitapojen suhteen, konfliktien ratkaisuissa;

.. 3) mitä opitte ryhmänä haasteeseenne ja ratkaisun liiketoimintamahdollisuuden arvioimiseen liittyen, mitä opitte ryhmänä toimimisesta sekä

.. 4) miten kukin ryhmän jäsen koki kehittyvänsä kurssin aikana ryhmän jäsenenä sekä mitä koki oppivansa ryhmän käsittelemästä teemasta. Hyödyntäkää esim. alla olevaa toiminnan arviointilomaketta.

.. Loppuraportin laajuus on noin 5-7 sivua riippuen. ryhmän jäsenten määrästä. Loppuraportti on oma erillinen dokumentti, joka voi olla linkitettynä ryhmän blogiin. Määräaika 16.12 klo 23.59.

Abstract
--------

.. csv-table::

   "Group", "*3+4Dudes*"
   "Topic", "*Indoor navigation using multiple images*"
   "Blog", "`https://jaantollander.github.io/SCI-C1000/ <https://jaantollander.github.io/SCI-C1000/>`_"


Problem
^^^^^^^
GPS cannot be used for *indoor navigation*, because it is inaccurate and unreliable in indoor environments due to obstructed line of sight to satellites. For this reason alternative solutions have been developed, such as:

- *WIFI Triangulation*
- *Bluetooth Beacons*
- *Magnetic Field Measurement*
- *Pedestrian Dead Reckoning*
- *Point-cloud from Images*

Some of these solutions such as *bluetooth beacons* or *WIFI triangulation* requires expensive infrastructure to be installed in the space. For *Pedestrian dead reckoning* the error is cumulative and cannot be used alone.

*Magnetic Field Measurement* have been implemented successfully by `Indoor Atlas <http://www.indooratlas.com/>`_ and on it self purely for navigation is better than our solution, but it doesn't offer the possibility for augmented or virtual reality applications.


.. Possible applications and customers for indoor navigation system that uses multiple crowd sourced images to build 3D point cloud and potentially 3D model for augmented reality and virtual reality applications.

.. Analysing weaknesses and strengths of our technology compared to competition currently on the market.


Solution
^^^^^^^^
Our solution *Indoor navigation using multiple images* is based on building 3D point cloud using multiple crowd sources images. The point cloud allows us to locate the position of new images of that space using existing ones.

Pros

- Because this technology is based on images we can also reconstruct the 3D model fully with textures which then can be applied to augmented/virtual reality applications.
- Based on existing infrastructure, e.g. mobile phone cameras and existing super computing clusters.
- *Software* based solution (contrary to *hardware* based) making it more *scalable* and lowering *maintenance costs*.
- Is able to tell you which direction of your line of sight (contrary to magnetic field measurements).


Cons

- Technologically quite challenging
- Convenient use requires that technology that enables taking photos of your visual field seamlessly such smart glasses becomes common.

Business and monetization models propose

* Initial fixed costs and monthly maintenance and update fees
* Initial cost is based on size and complexity of the area to be modelled
* Maintenance costs are based on estimated amount of end users and additional customer specific features.

In conclusion




Teamwork
--------

Methods
^^^^^^^
.. Rules
.. Resolving conflicts
.. Working methods
.. Groupd meetings, distributed tasks,

The group had meetings in learning hub every thursday from *10am* to around *12am*. In the meetings we usually discussed about the tasks for the next week and made scetches. Tasks were distributed according to the skills of each member.

.. csv-table:: Distribution of tasks between group members
   :header: "**Name**", "**Tasks**"

   "Lauri", "Compared techologies, blog posts, contacted competitors"
   "Markus", "Presentations, blog posts, organizing"
   "Misamatti", "Reading about related technologies, blog posts, email interviews"
   "Aapo", "Photographing, building 3D models and prototype, reading about related technologies"
   "Jaan", "Managing and writing the blog, 3D models"
   "Juhani", "Acquiring source material, interviewing companies, 3D models"
   "Antti", "Interview base, general planning"


Usually tasks were finished at home and the files were shared through *Google Drive*. Texts for the blog posts were written in a *google docs* file and them transferred in to *ReStructuredText* format to be compiled in to the blog. Similarly the steps to create the 3D models, photographing, constructing, visualizing and creating a website, were done in cooperation. Markus was the main speaker in the presentations.


Communication
^^^^^^^^^^^^^
- Weekly meeting
- **Telegram** our main communication channel
- **Google Drive** for sharing files.
- **Email** was used only for the most important announcements


Development of Teamwork Skills
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Teamwork Evaluation Matrix
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. csv-table:: Teamwork Evaluation Matrix
   :header-rows: 1
   :file: teamwork-evaluation-matrix.csv


.. Reasons
