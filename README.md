# 🍽️ Zomato Product Analytics, A/B Testing & LTV Modeling

## Project Overview

This project combines Product Analytics, Experimentation, and Customer Lifetime Value (LTV) Modeling using Bengaluru restaurant data from Zomato.

The objective was to understand restaurant success drivers, evaluate a ranking algorithm through A/B testing, and predict customer lifetime value for business decision-making.

---

## Business Problem

Food delivery platforms face three major challenges:

* Improving restaurant discovery
* Increasing user engagement
* Maximizing customer lifetime value

Traditional ranking systems often prioritize ratings alone, which can lead to less trustworthy recommendations.

Example:

Restaurant A:

* Rating: 4.8
* Reviews: 5

Restaurant B:

* Rating: 4.6
* Reviews: 5000

A rating-only system may incorrectly rank Restaurant A above Restaurant B.

---

## Dataset

Bangalore Zomato Restaurant Dataset

Dataset Size:

* 8,923 Restaurants
* 19 Features

Key Features:

* Restaurant Name
* Cuisine Type
* Area
* Dinner Ratings
* Dinner Reviews
* Delivery Ratings
* Delivery Reviews
* Average Cost
* Delivery Availability

---

## Product Sense Analysis

### Key Findings

* South Indian cuisine dominates Bengaluru's restaurant ecosystem.
* Cost and ratings show a moderate positive relationship (0.376).
* Reviews and ratings show a moderate positive relationship (0.422).
* 99.78% of restaurants offer home delivery.
* Home delivery is a hygiene factor rather than a differentiator.

---

## Experiment Design

### Hypothesis

A weighted ranking algorithm based on ratings and review strength will improve user engagement.

### Control

* Ranking based on ratings only

### Treatment

Restaurant Score:

70% Rating + 30% Review Strength

### Success Metric

* Click Through Rate (CTR)

---

## A/B Testing Results

Control CTR:

* 10.03%

Treatment CTR:

* 11.89%

CTR Improvement:

* 18.51%

P-value:

* 0.0033

### Conclusion

The weighted ranking system produced a statistically significant improvement in engagement and should be considered for deployment.

---

## LTV Modeling

### Features

* Orders
* Average Order Value
* Days Since Last Order

### Model

Linear Regression

### Performance

R² Score:

* 0.744

The model explains approximately 74% of future customer revenue variation.

---

## Customer Segmentation

### Low Value Customers

Average Predicted LTV:

* ₹802.88

### Medium Value Customers

Average Predicted LTV:

* ₹1422.54

### High Value Customers

Average Predicted LTV:

* ₹2108.41

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* SciPy
* Jupyter Notebook

---

## Business Impact

* Identified restaurant success drivers
* Designed a statistically significant A/B test
* Built a customer lifetime value prediction model
* Created actionable customer segments
* Proposed business recommendations for growth and retention
