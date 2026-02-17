# Sampling Assignment

**Name:** Harsh Tanwar  
**Roll Number:** 102303812

## Project Overview

This project demonstrates the impact of different sampling techniques on the accuracy of various machine learning models using a balanced credit card fraud detection dataset. The primary objective is to analyze how different sampling methodologies affect model performance when dealing with imbalanced datasets.

## Problem Statement

Credit card fraud detection datasets are typically highly imbalanced, with fraudulent transactions representing a very small percentage of total transactions. This imbalance can lead to biased models that perform poorly on the minority class. This assignment addresses this challenge through:

1. **Dataset Balancing:** Converting the imbalanced dataset into a balanced one using advanced resampling techniques
2. **Sampling Analysis:** Applying five different sampling techniques to create representative subsets
3. **Model Evaluation:** Training and testing five different machine learning classifiers on each sample
4. **Comparative Analysis:** Determining which sampling technique yields optimal accuracy for each model

## Methodology

### 1. Data Balancing

The dataset is balanced using **SMOTE (Synthetic Minority Over-sampling Technique)**, which generates synthetic samples for the minority class rather than simply duplicating existing samples. This approach helps prevent overfitting while achieving class balance.

**Mathematical Foundation:**

For a minority class sample $x_i$, SMOTE creates synthetic samples by:

$$x_{new} = x_i + \lambda \cdot (x_{zi} - x_i)$$

where:
- $x_{zi}$ is one of the $k$ nearest neighbors of $x_i$
- $\lambda \in [0, 1]$ is a random number
- $x_{new}$ is the synthetic sample

### 2. Sample Size Calculation

The sample size is calculated using **Cochran's formula** for finite populations:

$$n = \frac{n_0}{1 + \frac{n_0 - 1}{N}}$$

where:

$$n_0 = \frac{Z^2 \cdot p \cdot (1-p)}{e^2}$$

**Parameters:**
- $Z = 1.96$ (Z-score for 95% confidence level)
- $p = 0.5$ (maximum variability assumption)
- $e = 0.05$ (margin of error, 5%)
- $N$ = population size (balanced dataset size)
- $n$ = required sample size

This ensures statistically significant sample sizes with 95% confidence and 5% margin of error.

### 3. Sampling Techniques

#### Simple Random Sampling
Each observation has an equal probability of selection. For a population of size $N$ and desired sample size $n$:

$$P(\text{selection}) = \frac{n}{N}$$

**Implementation:** Random selection without replacement using uniform random distribution.

#### Systematic Sampling
Observations are selected at regular intervals. The sampling interval $k$ is calculated as:

$$k = \left\lfloor \frac{N}{n} \right\rfloor$$

A random starting point $r \in [0, k)$ is chosen, and every $k$-th element is selected thereafter.

**Implementation:** Starting index is randomly selected, then every $k$-th observation is included.

#### Stratified Sampling
The population is divided into homogeneous subgroups (strata) based on the target variable. Sample size from each stratum $i$ is proportional to its size:

$$n_i = n \cdot \frac{N_i}{N}$$

where:
- $n_i$ = sample size from stratum $i$
- $N_i$ = population size of stratum $i$
- $N$ = total population size
- $n$ = total sample size

**Implementation:** Proportional allocation based on class distribution to maintain class balance.

#### Cluster Sampling
The population is divided into clusters, and entire clusters are randomly selected. For $C$ total clusters and desired sample size $n$:

$$\text{Clusters to select} = \left\lceil \frac{n}{\text{avg cluster size}} \right\rceil$$

**Implementation:** Dataset is divided into 20 random clusters, and sufficient clusters are selected to meet sample size requirements.

#### Bootstrap Sampling
Sampling with replacement, where each observation can be selected multiple times. The probability that an observation is selected at least once in $n$ draws:

$$P(\text{selected}) = 1 - \left(1 - \frac{1}{N}\right)^n$$

**Implementation:** Random sampling with replacement to create a sample of size $n$.

### 4. Machine Learning Models

Five classification algorithms are evaluated:

1. **Logistic Regression:** Linear model using sigmoid function for binary classification
2. **Decision Tree:** Non-parametric model using recursive binary splitting
3. **Random Forest:** Ensemble of decision trees using bagging and feature randomness
4. **Support Vector Machine (SVM):** Finds optimal hyperplane maximizing margin between classes
5. **K-Nearest Neighbors (KNN):** Instance-based learning using distance metrics

### 5. Evaluation Methodology

**Training-Testing Split:**
- The balanced dataset is split into 80% training pool and 20% test set
- Samples are created from the training pool only
- All models are evaluated on the same held-out test set for fair comparison

**Accuracy Metric:**

$$\text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}$$

**Feature Scaling:** StandardScaler is applied to normalize features to zero mean and unit variance:

$$z = \frac{x - \mu}{\sigma}$$

where $\mu$ is the mean and $\sigma$ is the standard deviation.

## Requirements

Ensure you have Python 3.7 or higher installed along with the following libraries:

```bash
pip install pandas numpy scikit-learn imbalanced-learn
```

**Required Libraries:**
- `pandas`: Data manipulation and analysis
- `numpy`: Numerical computing
- `scikit-learn`: Machine learning algorithms and utilities
- `imbalanced-learn`: SMOTE implementation for handling imbalanced datasets

## Files

- `sampling102303812.py`: Main Python script performing data processing, sampling, and model evaluation
- `Creditcard_data.csv`: Input dataset containing credit card transaction data
- `sampling_results.csv`: Output file containing accuracy matrix (models vs sampling techniques)

## Usage

Run the script using the following command:

```bash
python sampling102303812.py
```

## Output

After execution, the script will:

1. Load and balance the credit card dataset using SMOTE
2. Display class distribution before and after balancing
3. Calculate optimal sample size using Cochran's formula
4. Generate five different samples using various sampling techniques
5. Train five machine learning models on each sample
6. Evaluate all models on the held-out test set
7. Display accuracy matrix showing model performance across sampling techniques
8. Identify the best sampling technique for each model
9. Save detailed results to `sampling_results.csv`

## Results Interpretation

The output `sampling_results.csv` contains a matrix where:
- **Rows:** Machine learning models
- **Columns:** Sampling techniques
- **Values:** Accuracy scores (0 to 1)

The script also identifies which sampling technique yields the highest accuracy for each model, helping determine the most effective sampling strategy for different classifiers.

## Key Insights

Different sampling techniques can significantly impact model performance:
- **Stratified Sampling** typically performs well as it maintains class distribution
- **Bootstrap Sampling** provides good variance estimation through resampling
- **Simple Random Sampling** serves as a baseline for comparison
- **Systematic Sampling** can be efficient but may introduce bias with periodic patterns
- **Cluster Sampling** is useful when natural groupings exist in the data

The choice of sampling technique should consider both computational efficiency and the specific characteristics of the dataset and model being used.
