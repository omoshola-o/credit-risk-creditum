# Credit Risk Assessment Package

A comprehensive Python package for assessing credit risk for both individual and corporate applications. This package integrates economic indicators, machine learning models, and industry-standard risk assessment practices to provide accurate credit risk evaluation.

## Features

- **Individual Credit Assessment**
  - Credit score evaluation
  - Income and debt analysis
  - Payment history assessment
  - Risk score calculation

- **Corporate Credit Assessment**
  - Business performance analysis
  - Industry risk evaluation
  - Financial ratio analysis
  - Market position assessment

- **Economic Integration**
  - Real-time economic indicator tracking
  - Industry-specific growth factors
  - Market volatility consideration
  - Automated risk adjustment

## Installation

```bash
pip install credit-risk-assessment
```

## Quick Start

```python
from credit_risk.core import CreditApplication

# Initialize application processor
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
```

## Usage Examples

### Individual Credit Assessment

```python
# Update economic indicators
economic_data = {
    'cpi': 0.02,
    'gdp_growth': 0.03,
    'unemployment_rate': 0.05,
    'interest_rate': 0.04,
    'inflation_rate': 0.02
}
app.economic_indicators.update_indicators(economic_data)

# Process application with full details
application = {
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

result = app.make_decision(application, 'individual')
```

### Corporate Credit Assessment

```python
corporate_application = {
    'years_in_business': 5,
    'annual_revenue': 1000000,
    'industry': 'technology',
    'loan_amount': 200000,
    'loan_purpose': 'expansion',
    'financial_ratios': 0.75,
    'market_position': 0.65,
    'operational_efficiency': 0.80,
    'management_quality': 0.70
}

result = app.make_decision(corporate_application, 'corporate')
```

## Documentation

For detailed documentation, visit [Read the Docs](https://credit-risk-assessment.readthedocs.io/).

### Key Components

- `CreditApplication`: Main class for processing applications
- `EconomicIndicators`: Manages economic data and impact
- `IndividualRiskAssessment`: Handles individual risk calculation
- `CorporateRiskAssessment`: Handles corporate risk calculation

## Configuration

Customize risk thresholds and weights:

```python
app = CreditApplication(
    min_credit_score=650,  # Minimum required credit score
    max_dti=0.40          # Maximum debt-to-income ratio
)
```

## Development

### Requirements

- Python 3.7+
- NumPy
- Pandas
- scikit-learn

### Setting Up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/credit-risk-assessment.git
cd credit-risk-assessment

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Documentation: [Read the Docs](https://credit-risk-assessment.readthedocs.io/)
- Issues: [GitHub Issues](https://github.com/yourusername/credit-risk-assessment/issues)
- Email: owolabi.omoshola@outlook.com