Creating the Prototype
======================

:date: 2016-11-11
:slug: prototype
:tags: prototype
:authors: Jaan Tollander de Balsch; Aapo Haavisto; Antti Karkinen; Misamatti Koistinen; Lauri Seppäläinen; Juhani Sipilä; Markus Tyrkkö,

.. :status: draft


Creating 3D models with VisualSFM
---------------------------------
Creating a 3D model from images with VisualSFM consists of three steps. [VisualSFM]_


1. Feature Detection & (Full) Pairwise Image Matching
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/vsfm/match.PNG
   :alt: match
   :width: 100%

Feature detection of the images finds similar features from each image in order to perform the pairwise image mathing. This operation determines where images are positioned in respect to one another

Full pairwise image matching compares every image with every other image in order to do the matching. Full pairwise matching is the only way if we have completely random images but it is computationally expensive.


2. Sparse Reconstruction
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/vsfm/sparse_cloud.PNG
   :alt: sparse cloud
   :width: 100%

Sparse reconstruction constructs the point cloud from the matched images. It finds the spatial positions the images in the 3D space. Point cloud is required for indoor navigation.


3. Dense Reconstruction
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: images/vsfm/giphy.gif
   :alt: dense reconstruction
   :width: 100%
   :target: https://jaantollander.github.io/3D-models/kaivuri/examples/kaivuri.html

Dense reconstruction builds the full 3D model with textures from the sparse reconstruction. This is optional step for the indoor navigation but required for additional features that require 3D model such as *alternate reality (AR)*.

Live 3D model can be accessed by clicking the gif image above or `this link`_. It is displayed and rendered with Potree. [Potree]_

.. _this link: https://jaantollander.github.io/3D-models/kaivuri/examples/kaivuri.html


----


3D Model of Learning Center Beta
--------------------------------
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

asd


----

References
----------
.. [VisualSFM] Wu, Changchang. "VisualSFM: A visual structure from motion system." (2011).
.. [Potree] Potree | WebGL pointcloud renderer http://www.potree.org/
