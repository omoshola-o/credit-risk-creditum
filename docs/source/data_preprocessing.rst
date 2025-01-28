Data Preprocessing Guidelines
=========================

Input Data Requirements
--------------------

Individual Applications
^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # Required fields and their types
    INDIVIDUAL_REQUIRED_FIELDS = {
        'credit_score': int,          # Range: 300-850
        'monthly_income': float,      # Positive value
        'monthly_debt': float,        # Positive value
        'loan_amount': float,         # Positive value
        'loan_purpose': str,          # Must be in approved purposes
        'payment_history': float,     # Range: 0-1
        'credit_utilization': float,  # Range: 0-1
    }

    # Example preprocessing function
    def preprocess_individual_application(data):
        # Convert numeric fields
        data['credit_score'] = int(data['credit_score'])
        data['monthly_income'] = float(data['monthly_income'])
        data['monthly_debt'] = float(data['monthly_debt'])
        
        # Normalize ratios to 0-1 range
        data['credit_utilization'] = min(1.0, max(0.0, data['credit_utilization']))
        data['payment_history'] = min(1.0, max(0.0, data['payment_history']))
        
        return data

Corporate Applications
^^^^^^^^^^^^^^^^^^^
.. code-block:: python

    # Required fields and their types
    CORPORATE_REQUIRED_FIELDS = {
        'years_in_business': int,     # Positive value
        'annual_revenue': float,      # Positive value
        'industry': str,              # Must be in approved industries
        'loan_amount': float,         # Positive value
        'financial_ratios': float,    # Range: 0-1
    }

Data Validation
------------

.. code-block:: python

    def validate_data(data, application_type='individual'):
        errors = []
        
        if application_type == 'individual':
            if data['credit_score'] < 300 or data['credit_score'] > 850:
                errors.append("Credit score must be between 300 and 850")
                
            if data['monthly_income'] <= 0:
                errors.append("Monthly income must be positive")
        else:
            if data['years_in_business'] < 0:
                errors.append("Years in business must be positive")
                
            if data['annual_revenue'] <= 0:
                errors.append("Annual revenue must be positive")
                
        return errors

Handling Missing Data
-----------------

.. code-block:: python

    def handle_missing_data(data):
        # Define default values
        defaults = {
            'credit_history_length': 0.0,
            'income_stability': 0.5,
            'market_position': 0.5
        }
        
        # Fill missing values
        for field, default in defaults.items():
            if field not in data or data[field] is None:
                data[field] = default
                
        return data