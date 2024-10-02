import numpy as np
import matplotlib.pyplot as plt

class BinaryEDAPlots:
    def __init__(self, binary_columns, zeros_count_list, ones_count_list):
        self.binary_columns = binary_columns
        self.zeros_count_list = zeros_count_list
        self.ones_count_list = ones_count_list

    def plot_binary_distribution(self):
        N = len(self.binary_columns)
        ind = np.arange(N)
        width = 0.5

        plt.figure(figsize=(8, N / 6))

        p1 = plt.barh(ind, self.zeros_count_list, width, color='red')
        p2 = plt.barh(ind, self.ones_count_list, width, left=self.zeros_count_list, color='blue')

        plt.yticks(ind, self.binary_columns)

        plt.legend((p1[0], p2[0]), ('Zero count', 'One count'))

        # Added % on each bar
        for i, (z_count, o_count) in enumerate(zip(self.zeros_count_list, self.ones_count_list)):
            total = z_count + o_count
            z_percent = (z_count / total) * 100
            o_percent = (o_count / total) * 100

            plt.text(z_count / 2, i, f'{z_percent:.1f}%', va='center', ha='center', color='white', fontsize=5)
            plt.text(z_count + o_count / 2, i, f'{o_percent:.1f}%', va='center', ha='center', color='white', fontsize=5)

        plt.tight_layout()
        plt.show()