from typing import Dict, Any, Optional

class EconomicIndicators:
    """
    Handle economic indicators and their impact on credit risk
    """
    def __init__(self):
        self.indicators = {}
        
    def update_indicators(self, indicator_data: Dict[str, Any]) -> None:
        """Update economic indicators with current data"""
        self.indicators.update({
            'cpi': indicator_data.get('cpi', None),
            'gdp_growth': indicator_data.get('gdp_growth', None),
            'unemployment_rate': indicator_data.get('unemployment_rate', None),
            'interest_rate': indicator_data.get('interest_rate', None),
            'inflation_rate': indicator_data.get('inflation_rate', None),
            'industry_growth': indicator_data.get('industry_growth', {}),
            'market_volatility': indicator_data.get('market_volatility', None),
            'currency_stability': indicator_data.get('currency_stability', None)
        })
    
    def calculate_economic_risk_factor(self, entity_type: str = 'individual', 
                                     industry: Optional[str] = None) -> float:
        """Calculate economic risk factor based on entity type and industry"""
        weights = self._get_economic_weights(entity_type)
        
        risk_factor = 0.0
        for indicator, weight in weights.items():
            if indicator == 'industry_growth' and industry:
                value = self.indicators.get(indicator, {}).get(industry, 0.5)
            else:
                value = self.indicators.get(indicator, 0.5)
            risk_factor += value * weight
            
        return min(max(risk_factor, 0), 1)
    
    def _get_economic_weights(self, entity_type: str) -> Dict[str, float]:
        """Get economic factor weights based on entity type"""
        if entity_type == 'individual':
            return {
                'cpi': 0.3,
                'unemployment_rate': 0.3,
                'interest_rate': 0.2,
                'inflation_rate': 0.2
            }
        return {
            'gdp_growth': 0.2,
            'industry_growth': 0.3,
            'interest_rate': 0.2,
            'market_volatility': 0.15,
            'currency_stability': 0.15
        }