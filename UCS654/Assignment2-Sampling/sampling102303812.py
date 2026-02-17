import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
import warnings

warnings.filterwarnings("ignore")

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        return None

def balance_data(df, target_col='Class'):
    X = df.drop(columns=[target_col])
    y = df[target_col]
    
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X, y)
    
    df_balanced = pd.concat([pd.DataFrame(X_resampled, columns=X.columns), 
                             pd.DataFrame(y_resampled, columns=[target_col])], axis=1)
    
    return df_balanced

def simple_random_sampling(df, sample_size, random_state=42):
    return df.sample(n=int(sample_size), random_state=random_state)

def systematic_sampling(df, sample_size, random_state=42):
    n = int(sample_size)
    k = len(df) // n
    start = np.random.randint(0, k)
    indices = np.arange(start, len(df), k)
    return df.iloc[indices[:n]]

def stratified_sampling(df, target_col='Class', random_state=42):
    n = calculate_sample_size(df)
    return df.groupby(target_col, group_keys=False).apply(lambda x: x.sample(n=int(round(n * len(x)/len(df))), random_state=random_state))

def cluster_sampling(df, n_clusters=20, random_state=42):
    df_temp = df.copy()
    df_temp['cluster'] = np.random.randint(0, n_clusters, size=len(df))
    
    avg_cluster_size = len(df) / n_clusters
    n_samples = calculate_sample_size(df)
    clusters_needed = max(1, int(round(n_samples / avg_cluster_size)))
    
    selected_clusters = np.random.choice(range(n_clusters), size=clusters_needed, replace=False)
    sample = df_temp[df_temp['cluster'].isin(selected_clusters)].drop(columns=['cluster'])
    return sample

def bootstrap_sampling(df, random_state=42):
    n = calculate_sample_size(df)
    return df.sample(n=n, replace=True, random_state=random_state)

def calculate_sample_size(df, confidence_level=0.95, margin_of_error=0.05):
    Z = 1.96
    p = 0.5
    e = margin_of_error
    N = len(df)
    
    n_0 = (Z**2 * p * (1-p)) / (e**2)
    n = n_0 / (1 + (n_0 - 1) / N)
    
    return int(max(math.ceil(n), 100))

def get_models():
    return {
        "Logistic Regression": LogisticRegression(max_iter=1000, random_state=42),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42),
        "SVM": SVC(random_state=42),
        "KNN": KNeighborsClassifier()
    }

def evaluate_models(samples, models, original_test_data):
    results = {}
    
    X_test = original_test_data.drop(columns=['Class'])
    y_test = original_test_data['Class']
    
    scaler = StandardScaler()
    
    for sample_name, sample_df in samples.items():
        results[sample_name] = {}
        
        X_train = sample_df.drop(columns=['Class'])
        y_train = sample_df['Class']
        
        if X_train.empty:
            continue

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        for model_name, model in models.items():
            try:
                model.fit(X_train_scaled, y_train)
                y_pred = model.predict(X_test_scaled)
                acc = accuracy_score(y_test, y_pred)
                results[sample_name][model_name] = acc
            except Exception as e:
                results[sample_name][model_name] = np.nan
            
    return pd.DataFrame(results)

def main():
    df = load_data('Creditcard_data.csv')
    if df is None: return

    df_balanced = balance_data(df)
    
    train_pool, test_set = train_test_split(df_balanced, test_size=0.2, random_state=42)
    
    sample_size_approx = calculate_sample_size(train_pool)

    samples = {
        "Simple Random": simple_random_sampling(train_pool, sample_size_approx),
        "Systematic": systematic_sampling(train_pool, sample_size_approx),
        "Stratified": stratified_sampling(train_pool),
        "Cluster": cluster_sampling(train_pool),
        "Bootstrap": bootstrap_sampling(train_pool)
    }
    
    models = get_models()
    results_df = evaluate_models(samples, models, test_set)
    
    print(results_df) 
    
    results_df.to_csv("sampling_results.csv")
    
    print(results_df.idxmax(axis=1))

if __name__ == "__main__":
    main()
