# Simulation-Based Machine Learning Analysis

## Assignment Details
- **Name**: Harsh Tanwar
- **Roll Number**: 102303812
- **Task**: Data Generation using Modelling and Simulation

## Overview
This project demonstrates how simulation data can be combined with machine learning to analyze and predict system performance.  
A custom simulator is used to generate synthetic data, which is then used to train and evaluate multiple ML models.

---

## Objectives
- Generate simulation data using random parameters  
- Perform 1000 simulations  
- Train multiple machine learning models  
- Compare models using evaluation metrics  
- Identify the best-performing model  

---

## Methodology

### 1. Parameter Selection
The system is defined using the following parameters:

| Parameter | Description | Range |
|----------|------------|-------|
| n | Number of nodes | 5 – 100 |
| r | Data rate | 1 – 100 |
| d | Delay | 1 – 50 |
| l | Packet loss | 0 – 0.3 |
| t | Simulation time | 5 – 50 |

---

### 2. Simulation Process
- Random values are generated within the defined bounds  
- A mathematical model simulates system behavior  
- Outputs generated:
  - Throughput (th)
  - Latency (la)  
- Total simulations performed: **1000**

---

### 3. Dataset Preparation
- Features: n, r, d, l, t  
- Target variable: throughput  
- Data stored using Pandas DataFrame  
- Dataset split into training and testing sets  

---

### 4. Machine Learning Models
The following models were trained and evaluated:

- Linear Regression  
- Decision Tree Regressor  
- Random Forest Regressor  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

---

### 5. Evaluation Metrics
Models were evaluated using:

- Mean Squared Error (MSE)  
- R² Score  

---

### 6. Results

| Model | Performance |
|------|------------|
| Linear Regression | Moderate |
| Decision Tree | Good |
| Random Forest | Best |
| SVM | Moderate |
| KNN | Good |

---

### 7. Conclusion
Random Forest outperformed all other models due to its ability to handle non-linear relationships and provide better generalization with lower error.

---

## 8. Colab Link
https://colab.research.google.com/drive/1HPOwsi-AMsPwf49ElIZptOfiGYAvpuwn?usp=sharing

---

## Tools & Technologies
- Python  
- Pandas  
- Scikit-learn  
- Google Colab  


---
