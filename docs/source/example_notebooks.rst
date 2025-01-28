Example Notebooks
==============

Individual Credit Assessment
------------------------

.. code-block:: python

    # Complete example for individual credit assessment
    
    import pandas as pd
    from credit_risk.core import CreditApplication
    
    # 1. Initialize application
    app = CreditApplication()
    
    # 2. Set up economic data
    economic_data = {
        'cpi': 0.02,
        'gdp_growth': 0.03,
        'unemployment_rate': 0.05,
        'interest_rate': 0.04,
    }
    app.economic_indicators.update_indicators(economic_data)
    
    # 3. Process multiple applications
    applications = pd.DataFrame([
        {
            'credit_score': 720,
            'monthly_income': 5000,
            'monthly_debt': 1500,
            'loan_amount': 20000,
        },
        {
            'credit_score': 680,
            'monthly_income': 4000,
            'monthly_debt': 1200,
            'loan_amount': 15000,
        }
    ])
    
    # 4. Process each application
    results = []
    for _, app_data in applications.iterrows():
        # Preprocess
        processed_data = preprocess_individual_application(app_data.to_dict())
        
        # Get decision
        result = app.make_decision(processed_data, 'individual')
        results.append(result)
    
    # 5. Analyze results
    results_df = pd.DataFrame(results)
    print("Approval Rate:", (results_df['decision'] == 'approved').mean())

Corporate Portfolio Analysis
------------------------

.. code-block:: python

    # Complete example for corporate portfolio analysis
    
    import pandas as pd
    import numpy as np
    from credit_risk.core import CreditApplication
    
    # 1. Initialize application
    app = CreditApplication()
    
    # 2. Load corporate portfolio
    portfolio = pd.DataFrame([
        {
            'years_in_business': 5,
            'annual_revenue': 1000000,
            'industry': 'technology',
            'loan_amount': 200000,
        },
        {
            'years_in_business': 8,
            'annual_revenue': 2000000,
            'industry': 'manufacturing',
            'loan_amount': 500000,
        }
    ])
    
    # 3. Process portfolio
    results = []
    for _, company in portfolio.iterrows():
        result = app.make_decision(company.to_dict(), 'corporate')
        results.append(result)
    
    # 4. Analyze portfolio risk
    results_df = pd.DataFrame(results)
    print("Portfolio Risk Profile:")
    print(results_df['risk_category'].value_counts())
    print("\nTotal Exposure:", results_df['max_loan_amount'].sum())

Batch Processing Example
--------------------

.. code-block:: python

    # Example of batch processing with progress tracking
    
    from tqdm import tqdm
    import pandas as pd
    from credit_risk.core import CreditApplication
    
    def batch_process(applications, batch_size=100):
        app = CreditApplication()
        results = []
        
        for i in tqdm(range(0, len(applications), batch_size)):
            batch = applications[i:i+batch_size]
            
            for _, application in batch.iterrows():
                result = app.make_decision(
                    application.to_dict(),
                    'individual'
                )
                results.append(result)
                
        return pd.DataFrame(results)

Model Performance Analysis
----------------------

.. code-block:: python

    # Example of analyzing model performance
    
    import matplotlib.pyplot as plt
    from credit_risk.utils.analysis import calculate_metrics
    
    def analyze_performance(predictions, actual):
        # Calculate performance metrics
        metrics = calculate_metrics(predictions, actual)
        
        # Plot ROC curve
        plt.figure(figsize=(10, 6))
        plt.plot(metrics['fpr'], metrics['tpr'])
        plt.title('ROC Curve')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.show()
        
        # Print metrics
        print(f"AUC: {metrics['auc']:.3f}")
        print(f"Gini: {metrics['gini']:.3f}")
        print(f"KS Statistic: {metrics['ks_stat']:.3f}")