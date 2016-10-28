Comparison Between Indoor Navigation Systems
============================================

:date: 2016-10-28
:slug: comparison
:tags:
:authors: Jaan Tollander de Balsch; Aapo Haavisto; Antti Karkinen; Misamatti Koistinen; Lauri Seppäläinen; Juhani Sipilä; Markus Tyrkkö,


.. figure:: figures/comparison.png
   :alt: image of comparison


On the market there exist numerous competing methods for indoor localization, some more similar with our model than others. In this blog post these methods are compared technically.


WIFI Triangulation
------------------
WiFi-positioning system builds on two things: the received signal strength of the device being positioned and the *fingerprint* of the WiFi router sending the signal. This fingerprint can be, for example, the SSID or the MAC address of the WiFi router. In order to get positioning data with this system, the indoor areas have to mapped with fingerprint/signal strength data matching some places and interpolating the data between the measured locations. Thus the accuracy of this method is dependent on the stability of the signal strength and the number of fingerprint/signal strength pairs.


The strengths of this positioning method include the fact that it relies on existing infrastructure: WiFi can be nowadays found in almost any building. This method also ensures that the device making the location query can be connected to the database enabling the positioning, as without WiFi there is no positioning system at all. This positioning system can also be used in Internet of Things objects as most of them connect to the internet wirelessly anyway.


As for weaknesses, the system needs WiFi to function, and in a world of near ubiquitous mobile networks (at least in Finland), the lack of WiFi in order to get positioning data is not that big of a problem. The accuracy of some systems is also of question, although some very accurate systems have been developed, such as the award winning `Anyplace`_, which claims accuracy of less than 2 m. The initial layout of the building has to be created externally before the system can be deployed and as everyone surely knows, WiFi signals are sometimes finicky especially in rooms with thick walls.




Bluetooth Beacons
-----------------
Another method for indoor positioning is the use of Bluetooth beacons scattered throughout the building in question. This method is in use for example at the main building here in Otaniemi in tandem with the Aalto Space app. The technique works rather simply: bluetooth low energy beacons are installed to a structure and their locations measured. As a device tries to determine its location with this technique, it simply triangulates its position using the received signal strength and individual fingerprints of the bluetooth beacons.


The system is accurate and bluetooth functionality is found on most devices. Otherwise its strengths are similar to those of the WiFi technique: bluetooth connectivity can be found on most devices which also have WiFi.


The weaknesses of this system are the need to install new hardware into the building as well as the need to maintain said hardware. Bluetooth signal range is also shorter than that of WiFi.


Magnetic Field Measurement
--------------------------
Modern smartphones have quite excellent components to measure magnetic field in order to optimise connectivity. They are so accurate, in fact, that within a scope of a building there are very detectable fluctuations in surrounding magnetic field due to Earth’s own field as well as fields created by man-made devices. Thus each building has it’s own magnetic fingerprint and if the device knows which building it’s in, it can position itself by comparing its perceived magnetic field with a magnetic map of the building.


This technique doesn’t need any infrastructure in order to function save the initial mapping of the magnetic field within the building. This process can be crowdsourced, as all one needs to map a building with an API is a smartphone with a working magnetic field strength meter. This means also that any device positioning itself with this technique can also be used to update the magnetic map, reducing the costs or altogether eliminating the need for external updates. A Finnish company, Indoor Atlas, developing this technique claims accuracy of less than 2 meters.


Pedestrian Dead Reckoning
-------------------------
Almost all smart devices come equipped with rather accurate acceleration sensors. Pedestrian dead reckoning techniques (here abbreviated PDR) use these sensors to pick up positioning from the point where GPS signal is lost i.e. when entering a building. Individual steps taken by the user produce a certain kind of acceleration pattern and by approximating step length, the distance travelled can be measured with decent accuracy. Combining the step data with readings from the devices compass, the route taken by the device indoors can be reconstructed yielding the current position of the device. This technique is utilized in for example, aircraft.


The strengths of this technique include the fact that only the end device is needed: if the device knows at some point its exact location (for example outside using GPS) it can approximate its route theoretically indefinitely even without an internet connection.


The main weakness of the system is the accumulation of error: as each movement of the device is approximated and the route is constructed using a chain of these approximations, each step building on the last, eventually the position given by the system will be useless, even with small individual errors.


Point-cloud from Images
-----------------------
The subject of this SCI-project, as one can read from previous posts, works by forming a point cloud based on images captured within the structure. When a device makes a location query by uploading a new photo of the interior of the building to the server, the image is compared with the existing point cloud, key features within the image are gathered and the location of the camera is solved as an  inversion problem. The new image is added to the point cloud.


The main selling points of this technology are similar to those of magnetic field measurement: it needs no infrastructure and the updating and initial mapping of the structure can be crowdsourced. However, with this technique a full 3D model of the structure is constructed as opposed to a simple 2D map. This offers many applications beyond simple positioning, such as augmented reality guidance overlaid on the 3D model (guiding a shopper towards a product on the aisles of a store, for example).


Summary
-------

.. csv-table::

   "**Name**", "**Accuracy**", "**Infrastructure**", "**Maintenance**", "**Power Source**", "**Other**"
   "*WIFI Triangulation*", ":math:`5-30\,\mathrm{m}` [1]_", "Usually existing", "Remapping", "Device battery + AC", "Relies on existing infrastructure"
   "*Bluetooth Beacons*", ":math:`2-30\,\mathrm{m}`", "Hardware installation, Device management", "Remapping", "Device battery + AC", ""
   "*Magnetic Field Measurement*", ":math:`2\,\mathrm{m}`", "API + initial magnetic mapping", "Crowdsourced", "Device battery", ""
   "*Pedestrian Dead Reckoning*", "Varies", "None", "Crowdsourced", "Device battery", "No additional devices / services needed"
   "*Point-cloud from Images*", ":math:`5\,\mathrm{m}`", "API + initial photoshoot", "Crowdsourced", "Device battery", "Creates 3D model to be used with AR etc."

.. Footnotes
.. [1] depending on algorithms (>2m claimed by `Anyplace`_)

.. Links
.. _Anyplace: https://anyplace.cs.ucy.ac.cy/


References
----------
.. [#] Sterling, Greg (Opus Research, I. . (2014). Magnetic Positioning, 1–8.
.. [#] Zandbergen, P. A. (2009). Accuracy of iPhone locations: A comparison of assisted GPS, WiFi and cellular positioning. Transactions in GIS, 13(SUPPL. 1), 5–25. http://doi.org/10.1111/j.1467-9671.2009.01152.x
.. [#] Bekkelien, A. (2012). Bluetooth indoor positioning. Master’s Thesis, University …, (March), 1. Retrieved from http://cui.unige.ch/~deriazm/masters/bekkelien/Bekkelien_Master_Thesis.pdf
.. [#] Beauregard, S., & Haas, H. (2006). Pedestrian dead reckoning: A basis for personal positioning. Positioning, Navigation and Communication, 27–35. http://doi.org/10.1613/jair.301
.. [#] Liu, H., Darabi, H., Banerjee, P., & Liu, J. (2007). Survey of wireless indoor positioning techniques and systems. IEEE Transactions on Systems, Man and Cybernetics Part C: Applications and Reviews, 37(6), 1067–1080. http://doi.org/10.1109/TSMCC.2007.905750
