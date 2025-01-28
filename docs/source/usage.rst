Usage Guide
==========

Quick Start
----------

Basic Example
^^^^^^^^^^^

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
        'loan_purpose': 'home_improvement',
        'payment_history': 0.95,
        'credit_utilization': 0.30
    }

    result = app.make_decision(individual_application, 'individual')
    print(result)

Corporate Assessment
^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Process corporate application
    corporate_application = {
        'years_in_business': 5,
        'annual_revenue': 1000000,
        'industry': 'technology',
        'loan_amount': 200000,
        'loan_purpose': 'expansion',
        'financial_ratios': 0.75
    }

    result = app.make_decision(corporate_application, 'corporate')

Advanced Usage
------------

Economic Indicators Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Update economic indicators
    economic_data = {
        'cpi': 0.02,
        'gdp_growth': 0.03,
        'unemployment_rate': 0.05
    }
    app.economic_indicators.update_indicators(economic_data)

Custom Risk Models
^^^^^^^^^^^^^^

.. code-block:: python

    from credit_risk.models import BaseRiskAssessment

    class CustomRiskModel(BaseRiskAssessment):
        def __init__(self, economic_indicators):
            super().__init__(economic_indicators)
            self.risk_thresholds = {
                'low': 0.25,
                'medium': 0.50,
                'high': 0.75
            }

Advanced Usage Examples
-------------------

Economic Factor Integration
^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # Calculate economic impact
    economic_impact = app.calculate_economic_impact({
        'gdp_growth': 0.03,
        'unemployment': 0.05,
        'inflation': 0.02
    })

Custom Scoring Models
^^^^^^^^^^^^^^^^^
.. code-block:: python

    class CustomScorer(BaseScorer):
        def calculate_score(self, features):
            base_score = self.calculate_base_score(features)
            economic_factor = self.get_economic_factor()
            return self.adjust_score(base_score, economic_factor)

Model Performance Analysis
^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # Get detailed model performance metrics
    metrics = model.evaluate({
        'gini': True,
        'ks_statistic': True,
        'roc_auc': True
    })