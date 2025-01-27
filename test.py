from credit_risk.core.application import CreditApplication

def test_credit_assessment():
    # Initialize
    app = CreditApplication()
    
    # Sample economic data
    economic_data = {
        'cpi': 0.02,
        'gdp_growth': 0.03,
        'unemployment_rate': 0.05,
        'interest_rate': 0.04,
        'inflation_rate': 0.02,
        'industry_growth': {'technology': 0.08},
        'market_volatility': 0.15,
        'currency_stability': 0.85
    }
    app.economic_indicators.update_indicators(economic_data)
    
    # Sample application
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
    
    result = app.make_decision(individual_application, 'individual')
    print("Test Result:", result)

if __name__ == "__main__":
    test_credit_assessment()