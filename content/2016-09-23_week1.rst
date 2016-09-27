Week 1: Starting Up
===================

:date: 2016-09-23
:category: Starting up
:tags: Week 1
:slug:
:authors: Jaan Tollander de Balsch
:summary: Plans, goals, ...


Plans and Goals for the first week
----------------------------------
- Contacts
   - Meeting up with our contact professor

- Project Branding
   - Creating a project blog
   - Name the project
   - Design a logo and icon

- Project Managment
   - Planning the allocation of time
   - Keeping track of workhours
   - Flowchart of the project

- Project
   - Defining the problem and how to approach it
   - Limiting the size of the solution to the problem
   - Figuring out the possible customers for this technology
   - Defining the main goal of the project
   - List of open source technologies that can create 3D models from photographs


Creating the Project Blog
-------------------------
Created the project blog *(the one you are reading right now)*.

- **About** page contains some general information about the project
- **Contact** page contains information about the authors of the project.

Source code of this blog is hosted at `GitHub`_ and the blog it self is in the project `GitHub pages`_.

.. _GitHub: https://github.com/jaantollander/SCI-C1000
.. _GitHub pages: https://jaantollander.github.io/SCI-C1000/


3D Reconstruction from Photos
-----------------------------
When taking traditional photos of 3-dimensional world, it is projected into 2-dimensional surface and the depth is lost. In order to restore this lost dimension, one way to reconstuct it is as inversion problem, meaning reconstruction from multiple images [1]_.


Comparison with Other Technologies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*LIDAR is a surveying method that measures distance to a target by illuminating that target with a laser light* [2]_

Pros and cons comparing 3D recostruction from images versus LIDAR

- Pros
   - Cheaper than LIDAR
   - More available to consumers
   - Is able to create texture and colors for the surfaces
   - Images can be analysed without visiting the place.

- Cons
   - A lot less accurate


Potential Uses and Customers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Industry
   - Not accurate enough to replace LIDAR

- Constumers
   - Decoration app
   - Games
   - Navigation with smart glasses inside buildings

- Architects
   - Creating quick drafts when full precision is not needed
   - Displaying different choices for decoration in virtual or alternate reality

- Other
   - Building safety design
   - Virtual models of existing buildings


References
----------
.. [1] https://en.wikipedia.org/wiki/3D_reconstruction_from_multiple_images
.. [2] https://en.wikipedia.org/wiki/Lidar
