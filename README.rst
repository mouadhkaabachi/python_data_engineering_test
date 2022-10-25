===========
testservier
===========


The objective is to build a data pipeline allowing to process the data defined in the previous part in order to generate the result described in part 3.
To do this, you need to set up a project in python organized in the way that seems most relevant to you to solve this problem. We expect you to identify a project structure and a separation of the necessary steps that highlight your knowledge around the development of business data in python.


environment
-------------
* python 3
* pandas


project structure
-----------------

::

        ├── AUTHORS.rst
        ├── CONTRIBUTING.rst
        ├── HISTORY.rst
        ├── MANIFEST.in
        ├── Makefile
        ├── README.rst
        ├── config
        │   └── config.yml
        ├── data
        │   ├── clinical_trials.csv
        │   ├── drugs.csv
        │   ├── pubmed.csv
        │   └── pubmed.json
        ├── docs
        │   ├── Makefile
        │   ├── authors.rst
        │   ├── conf.py
        │   ├── contributing.rst
        │   ├── history.rst
        │   ├── index.rst
        │   ├── installation.rst
        │   ├── make.bat
        │   ├── readme.rst
        │   └── usage.rst
        ├── main.py
        ├── output
        │   └── drug_out.json
        ├── requirements.in
        ├── requirements.txt
        ├── requirements_dev.txt
        ├── setup.cfg
        ├── setup.py
        ├── src
        │   ├── __init__.py
        │   ├── cli.py
        │   ├── common
        │   │   ├── __init__.py
        │   │   ├── common.py
        │   │   └── utils.py
        │   ├── export
        │   │   ├── __init__.py
        │   │   └── export.py
        │   ├── loader
        │   │   └── loader.py
        │   ├── testservier.py
        │   └── transform
        │       ├── __init__.py
        │       └── transform.py
        ├── test_python_de.pdf
        ├── tests
        │   ├── __init__.py
        │   ├── drug_out_test_file.json
        │   └── test_testservier.py
        └── tox.ini


How to use it
-------------

from command line

install
=======

*   pip install -r requirements.txt

run
===

* python main.py run-pipeline
* python main.py top-journals

run test
========

from command line run:

* py.test

pip install tox

* tox


Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* utiliser pyspark dans un cluster au lieu de pandas (pandas est tres gourmand en RAM)
* utiliser les services de GCP (bigquery par exemple)

Question sql
------------

1)

::


        SELECT
            tr.date,
            sum(tr.prod_price * tr.prod_qty) AS Ventes
        FROM
            TRANSACTIONS as tr
        where
            tr.date BETWEEN CAST("2019-01-01" AS DATE)
            and CAST("2019-12-31" AS DATE)
        GROUP BY
            tr.date
        ORDER BY
            tr.date;

2)

::

        WITH ventes_m AS (
          SELECT
            tr.client_id AS client_id,
            SUM(tr.prod_price * tr.prod_qty) AS ventes_meuble
          FROM
            TRANSACTION tr
            INNER JOIN PRODUCT_NOMENCLATURE pn ON tr.prod_id = pn.product_id
          WHERE
            tr.date BETWEEN CAST("2019-01-01" AS DATE)
            AND CAST("2019-12-31" AS DATE)
            AND pn.product_type = "MEUBLE"
          GROUP BY
            tr.client_id
        ),
        ventes_d AS (
          SELECT
            tr.client_id AS client_id,
            SUM(tr.prod_price * tr.prod_qty) AS ventes_deco
          FROM
            TRANSACTION tr
            INNER JOIN PRODUCT_NOMENCLATURE pn ON tr.prod_id = pn.product_id
          WHERE
            tr.date BETWEEN CAST("2019-01-01" AS DATE)
            AND CAST("2019-12-31" AS DATE)
            AND pn.product_type = "DECO"
          GROUP BY
            tr.client_id
        ),
        ventes AS (
          SELECT
            m.client_id as m_client_id,
            m.ventes_meuble,
            vd.client_id as d_client_id,
            vd.ventes_deco
          FROM
            ventes_m as m
            LEFT JOIN ventes_d as vd ON m.client_id = vd.client_id
          UNION
          SELECT
            m.client_id as m_client_id,
            m.ventes_meuble,
            vd.client_id as d_client_id,
            vd.ventes_deco
          FROM
            ventes_m as m
            RIGHT JOIN ventes_d as vd ON m.client_id = vd.client_id
        )

        SELECT
          IFNULL(m_client_id, d_client_id) AS client_id,
          ventes_meuble,
          ventes_deco
        FROM
          ventes;

