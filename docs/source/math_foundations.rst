Mathematical Foundations
======================

Credit Risk Scoring System
------------------------

Core Risk Assessment Components
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Base Risk Score Calculation
""""""""""""""""""""""""
The base risk score is calculated using a weighted combination of factors:

.. math::

   R_{base} = \sum_{i=1}^{n} w_i \times f_i

where:
* :math:`R_{base}` is the base risk score
* :math:`w_i` are the feature weights
* :math:`f_i` are the normalized feature values
* :math:`n` is the number of features

Individual Assessment Weights
"""""""""""""""""""""""""
.. code-block:: python

   INDIVIDUAL_WEIGHTS = {
       'payment_history': 0.30,
       'credit_utilization': 0.25,
       'credit_history_length': 0.15,
       'income_stability': 0.15,
       'debt_to_income': 0.15
   }

Corporate Assessment Weights
""""""""""""""""""""""""
.. code-block:: python

   CORPORATE_WEIGHTS = {
       'financial_ratios': 0.25,
       'market_position': 0.20,
       'operational_efficiency': 0.15,
       'management_quality': 0.15,
       'business_model': 0.15,
       'regulatory_compliance': 0.10
   }

Economic Impact Integration
^^^^^^^^^^^^^^^^^^^^^^^

Economic Risk Factor
"""""""""""""""""
The economic risk factor is calculated using:

.. math::

   E_f = \sum_{j=1}^{m} e_j \times w_j

where:
* :math:`E_f` is the economic risk factor
* :math:`e_j` are economic indicators
* :math:`w_j` are indicator weights
* :math:`m` is the number of economic indicators

Final Risk Score
"""""""""""""
The final risk score incorporates economic factors:

.. math::

   R_{final} = R_{base} \times (1 - E_f \times \alpha)

where:
* :math:`R_{final}` is the final risk score
* :math:`\alpha` is the economic adjustment coefficient (default 0.3)

Machine Learning Models
--------------------

Random Forest Implementation
^^^^^^^^^^^^^^^^^^^^^^^^
Default configuration:

.. code-block:: python

   RF_CONFIG = {
       'n_estimators': 100,
       'max_depth': 10,
       'random_state': 42
   }

Key metrics calculated:
* Feature importance using SHAP values
* Out-of-bag error estimation
* Cross-validation scores

Logistic Regression
^^^^^^^^^^^^^^^
Probability calibration using Platt Scaling:

.. math::

   P(y=1|x) = \frac{1}{1 + e^{-(ax + b)}}

where:
* :math:`a` and :math:`b` are learned parameters
* :math:`x` is the model's raw output

Model Performance Metrics
---------------------

ROC AUC Calculation
^^^^^^^^^^^^^^^
Area Under the Receiver Operating Characteristic curve:

.. math::

   AUC = \int_0^1 TPR(FPR^{-1}(t))dt

where:
* TPR is True Positive Rate
* FPR is False Positive Rate

Gini Coefficient
^^^^^^^^^^^^^
Calculated from AUC:

.. math::

   Gini = 2 \times AUC - 1

Validation Methods
--------------

K-Fold Cross Validation
^^^^^^^^^^^^^^^^^^
Model performance is validated using k-fold cross-validation:

.. math::

   CV_{score} = \frac{1}{k}\sum_{i=1}^{k} score_i

Feature Importance Analysis
^^^^^^^^^^^^^^^^^^^^^
SHAP (SHapley Additive exPlanations) values:

.. math::

   \phi_i = \sum_{S\subseteq F\setminus\{i\}} \frac{|S|!(|F|-|S|-1)!}{|F|!}[f_S\cup\{i\}(x_{S\cup\{i\}})-f_S(x_S)]

where:
* F is the set of all features
* S is a subset of features
* f is the model

Decision Making
------------

Risk Categories
^^^^^^^^^^^^
Risk thresholds for categorization:

.. code-block:: python

   RISK_THRESHOLDS = {
       'low': 0.3,    # R_final <= 0.3
       'medium': 0.6, # 0.3 < R_final <= 0.6
       'high': 0.8    # R_final > 0.6
   }

Maximum Loan Amount
^^^^^^^^^^^^^^
For individuals:

.. math::

   L_{max} = M_i \times 36 \times (1 - R_{final})

where:
* :math:`L_{max}` is maximum loan amount
* :math:`M_i` is monthly income

For corporations:

.. math::

   L_{max} = A_r \times 0.5 \times (1 - R_{final})

where:
* :math:`A_r` is annual revenue

Implementation Details
------------------

Feature Normalization
^^^^^^^^^^^^^^^^^
Min-max scaling for numerical features:

.. math::

   f_{normalized} = \frac{f - f_{min}}{f_{max} - f_{min}}

Missing Value Handling
^^^^^^^^^^^^^^^^^
Default value assignment based on feature type:
* Numerical: Median of non-missing values
* Categorical: Mode of non-missing values