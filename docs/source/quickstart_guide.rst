Quick Start Guide
=============================

Installation
-----------

Install the package using pip:

.. code-block:: python

    !pip install credit-risk-assessment

Basic Usage
----------

1. Import Required Modules
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    from credit_risk.core import CreditApplication
    from credit_risk.models import IndividualRiskAssessment, CorporateRiskAssessment

2. Initialize the Application
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Create application instance
    app = CreditApplication(
        min_credit_score=600,  # Minimum required credit score
        max_dti=0.43          # Maximum debt-to-income ratio
    )

3. Update Economic Indicators (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Current economic data
    economic_data = {
        'cpi': 0.02,
        'gdp_growth': 0.03,
        'unemployment_rate': 0.05,
        'interest_rate': 0.04,
        'inflation_rate': 0.02,
        'industry_growth': {
            'technology': 0.08,
            'manufacturing': 0.03,
            'retail': 0.02
        },
        'market_volatility': 0.15,
        'currency_stability': 0.85
    }

    app.economic_indicators.update_indicators(economic_data)

4. Process Individual Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Prepare individual application data
    individual_application = {
        'credit_score': 720,
        'monthly_income': 5000,
        'monthly_debt': 1500,
        'loan_amount': 20000,
        'loan_purpose': 'home_improvement',
        'payment_history': 0.95,
        'credit_utilization': 0.30,
        'credit_history_length': 0.80,
        'income_stability': 0.90
    }

    # Get decision
    result = app.make_decision(individual_application, 'individual')

    # Print results
    print("Decision:", result['decision'])
    print("Risk Score:", result['risk_score'])
    print("Risk Category:", result['risk_category'])
    print("Maximum Loan Amount: $", result['max_loan_amount'])

5. Process Corporate Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

    # Prepare corporate application data
    corporate_application = {
        'years_in_business': 5,
        'annual_revenue': 1000000,
        'industry': 'technology',
        'loan_amount': 200000,
        'loan_purpose': 'expansion',
        'financial_ratios': 0.75,
        'market_position': 0.65,
        'operational_efficiency': 0.80,
        'management_quality': 0.70,
        'business_model': 0.85,
        'regulatory_compliance': 0.90
    }

    # Get decision
    result = app.make_decision(corporate_application, 'corporate')

    # Print results
    print("Decision:", result['decision'])
    print("Risk Score:", result['risk_score'])
    print("Risk Category:", result['risk_category'])
    print("Maximum Loan Amount: $", result['max_loan_amount'])

Example Google Colab Notebook
-------------------------

Here's a complete example you can copy into a Google Colab notebook:

.. code-block:: python

    # Install package
    !pip install credit-risk-assessment

    # Import required modules
    from credit_risk.core import CreditApplication

    # Initialize application
    app = CreditApplication()

    # Create sample application
    application = {
        'credit_score': 720,
        'monthly_income': 5000,
        'monthly_debt': 1500,
        'loan_amount': 20000,
        'loan_purpose': 'home_improvement',
        'payment_history': 0.95,
        'credit_utilization': 0.30
    }

    # Get decision
    result = app.make_decision(application, 'individual')

    # Display results
    for key, value in result.items():
        print(f"{key}: {value}")

Common Issues and Solutions
------------------------

1. Installation Issues
   - Make sure you're running the latest version of pip
   - Try: !pip install --upgrade pip
   - Then: !pip install credit-risk-assessment

2. Import Errors
   - Restart the runtime after installation
   - Make sure all dependencies are installed

3. Data Format Issues
   - All numerical values should be floats
   - Text values should be strings
   - Check required fields are present