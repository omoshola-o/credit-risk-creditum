.. Creditum - Credit Risk Assessment documentation master file, created by
   sphinx-quickstart on Tue Jan 28 00:11:44 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Credit Risk Assessment's documentation!
===============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   api

Introduction
-----------

The Credit Risk Assessment package provides tools for evaluating credit risk for both
individual and corporate applications.

Quick Start
----------

Installation
~~~~~~~~~~~

.. code-block:: bash

   pip install credit-risk-assessment

Basic Usage
~~~~~~~~~~

.. code-block:: python

   from credit_risk_assessment import CreditApplication

   # Initialize application processor
   credit_app = CreditApplication()

   # Process application
   application_data = {
       'credit_score': 720,
       'monthly_income': 5000,
       'monthly_debt': 1500,
       'loan_amount': 20000,
       'loan_purpose': 'home_improvement'
   }

   result = credit_app.make_decision(application_data)
   print(result)

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`