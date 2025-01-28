Usage Guide
==========

Quick Start
----------

.. code-block:: python

    from credit_risk.core import CreditApplication

    # Initialize application
    app = CreditApplication()

    # Process individual application
    individual_application = {
        'credit_score': 720,
        'monthly_income': 5000,
        'monthly_debt': 1500,
        'loan_amount': 20000,
        'loan_purpose': 'home_improvement'
    }

    result = app.make_decision(individual_application, 'individual')
    print(result)

Advanced Usage
------------

Economic Indicators
^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Update economic indicators
    economic_data = {
        'cpi': 0.02,
        'gdp_growth': 0.03,
        'unemployment_rate': 0.05,
        'interest_rate': 0.04,
        'inflation_rate': 0.02
    }
    app.economic_indicators.update_indicators(economic_data)