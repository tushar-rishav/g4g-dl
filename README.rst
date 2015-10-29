g4g-dl :bookmark:
-----------------

Downloads all Geeks for Geeks Algo and Data Structures tutorials and save as PDF
                                                                                

Note: I wrote this script because my friend `Pragyaditya
das <https://github.com/Jeet1994>`__ needed it. I ain't sure if it's
legal to scrape Geeks4Geeks. In future if I come across any such
policies, I shall remove this repo without any hesitation.

Installation
~~~~~~~~~~~~

Dependency to be installed manually
                                   

`wkhtmltopdf <https://github.com/wkhtmltopdf/wkhtmltopdf>`__

Build from source
'''''''''''''''''

.. code:: sh

        git clone "https://github.com/tushar-rishav/g4g-dl.git"
        cd g4g-dl
        python setup.py install

Default config:
~~~~~~~~~~~~~~~

::

    target  : g4gPdf

Options
~~~~~~~

.. code:: sh

    usage: g4g-dl [-h] [-t TARGET] [-p POST] [-d] [-a] [-s START] [-e END]

    Downloads Geeks for Geeks DS and Algorithm tutorials and save as PDF

    optional arguments:
      -h, --help            show this help message and exit
      -t TARGET, --target TARGET
                            absolute path of target directory to save all PDFs.
                            Default is g4gPdf in current dir
      -p POST, --post POST  link for single post
      -s START, --start START
                            Position to start from. Default is 0
      -e END, --end END     Position to end at. Default is the last link

    group:
      -d, --ds              Fetch all Data Structures
      -a, --algo            Fetch all Algorithms

    Author:https://github.com/tushar-rishav

Usage
~~~~~

Fetch single post
'''''''''''''''''

To fetch single tutorial, say Topological Sorting, run this in your
shell

.. code:: sh


    g4g-dl -p http://www.geeksforgeeks.org/topological-sorting/

Note: 1. The above command will save the pdf in default directory 2. You
must specify ``-d`` (for data structure) or ``-a`` (for algo) if you
aren't fetching tutorials this way.

Fetch all data structure tutorial in your custom directory
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: sh

    g4g-dl -t my_directory_abs_path -d

Fetch tutorials in range in your custom directory
'''''''''''''''''''''''''''''''''''''''''''''''''

.. code:: sh

    g4g-dl -t my_directory_abs_path -d -s 63 -e 69

Note: The order is according to which links appear in page. Above
command will fetch some graphs turorials which exist between between
63rd and 69th positions (both inclusive). This way you can download
selected tutorials. Go ahead and try downloading just Dynamic
Programming tutorials.

Get help
''''''''

.. code:: sh

    g4g-dl -h

Contributions
~~~~~~~~~~~~~

Have an idea to make it better? Go ahead! I will be happy to see a pull
request from you! :blush:

License
~~~~~~~

.. figure:: https://cloud.githubusercontent.com/assets/7397433/9025904/67008062-3936-11e5-8803-e5b164a0dfc0.png
   :alt: gpl

   gpl

