Simulation-Based ML Model Analysis

## Project Overview:
This project focuses on generating simulation data and applying machine learning models to analyze system performance.
A custom simulator is used to generate data based on predefined parameters, followed by training multiple ML models to predict performance metrics.


## Objectives:
- Simulate system behavior using random parameters
- Generate a dataset of 1000 simulations
- Train and compare multiple ML models
- Identify the best-performing model


## Methodology:

1. Parameter Selection:
The following parameters were used to simulate the system:
- n: Number of nodes (5 – 100)
- r: Data rate (1 – 100)
- d: Delay (1 – 50)
- l: Packet loss (0 – 0.3)
- t: Time (5 – 50)


2. Simulation:
- Random values are generated within given bounds
- Outputs calculated:
  - Throughput (th)
  - Latency (la)
- Total simulations: 1000


3. Dataset:
- Input features: n, r, d, l, t
- Target: throughput
- Data stored using DataFrame


4. Machine Learning Models:
The following models were used:
- Linear Regression
- Decision Tree
- Random Forest
- Support Vector Machine
- K-Nearest Neighbors


5. Evaluation Metrics:
- Mean Squared Error (MSE)
- R² Score


6. Results:
- Random Forest performed the best
- It achieved lowest error and highest R² score


## Conclusion:
This project demonstrates how simulation data can be combined with machine learning to predict system performance and select the most efficient model.



- Pandas
- Scikit-learn
- Google Colab
