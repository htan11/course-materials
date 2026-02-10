import numpy as np
import pandas as pd

class Topsis:
    def __init__(self, data, weights, impacts):
        """
        data: pandas DataFrame or numpy array (numeric data only)
        weights: list of weights for each criterion
        impacts: list of impacts ('+' for beneficial, '-' for non-beneficial)
        """
        self.data = np.array(data, dtype=float)
        self.weights = np.array(weights, dtype=float)
        self.impacts = impacts
        self.n_alternatives, self.n_criteria = self.data.shape
        
        if len(self.weights) != self.n_criteria or len(self.impacts) != self.n_criteria:
            raise ValueError("Dimensions of weights/impacts must match number of criteria")

    def step1_normalize(self):
        # Vector normalization
        sq_sum = np.sqrt(np.sum(self.data**2, axis=0))
        self.normalized_data = self.data / sq_sum

    def step2_weighted_normalize(self):
        self.weighted_normalized_data = self.normalized_data * self.weights

    def step3_ideal_best_worst(self):
        self.ideal_best = np.zeros(self.n_criteria)
        self.ideal_worst = np.zeros(self.n_criteria)

        for i in range(self.n_criteria):
            if self.impacts[i] == '+':
                self.ideal_best[i] = np.max(self.weighted_normalized_data[:, i])
                self.ideal_worst[i] = np.min(self.weighted_normalized_data[:, i])
            else:
                self.ideal_best[i] = np.min(self.weighted_normalized_data[:, i])
                self.ideal_worst[i] = np.max(self.weighted_normalized_data[:, i])

    def step4_separation_measures(self):
        self.separation_best = np.sqrt(np.sum((self.weighted_normalized_data - self.ideal_best)**2, axis=1))
        self.separation_worst = np.sqrt(np.sum((self.weighted_normalized_data - self.ideal_worst)**2, axis=1))

    def step5_calculate_scores(self):
        # Topsis Score = Worst Dist / (Best Dist + Worst Dist)
        self.scores = self.separation_worst / (self.separation_best + self.separation_worst)
        return self.scores

    def run(self):
        self.step1_normalize()
        self.step2_weighted_normalize()
        self.step3_ideal_best_worst()
        self.step4_separation_measures()
        return self.step5_calculate_scores()
