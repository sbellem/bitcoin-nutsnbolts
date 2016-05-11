Bitcoin: Some Nuts & Bolts
==========================
Presentation slides and html version, along with source code used to generate
them.

Slides can be viewed at

* https://sbellem.github.io/bitcoin-nutsnbolts/slides/

and the html version at

* https://sbellem.github.io/bitcoin-nutsnbolts/html/


Building and viewing locally
----------------------------
Clone the repo, ``cd`` into it, and run

.. code-block:: bash

    $ docker-compose run --rm docs bash
    root@ffef6f7a52c8:/usr/src# cd docs
    root@ffef6f7a52c8:/usr/src/docs# make html slides

In another shell, run

.. code-block:: bash

    $ docker-compose up -d html slides

The html can then be viewed at http://localhost:48080/ and the slides at
http://localhost:58080/.
