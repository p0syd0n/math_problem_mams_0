import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
np.set_printoptions(suppress=True, precision=0)  
# Load the dataset
# Assuming data.txt has two columns: length, shuffles
data = np.loadtxt("data.txt", delimiter=":", dtype=float)
lengths = data[:, 0]
shuffles = data[:, 1]

# Compute slope-like feature
ratios = shuffles / lengths

# Reshape for sklearn
X = ratios.reshape(-1, 1)

# Choose number of clusters (number of visible trendlines)
k = 5  # adjust depending on how many you see in the plot
kmeans = KMeans(n_clusters=k, random_state=0).fit(X)
labels = kmeans.labels_

# Plot clusters in different colors
for i in range(k):
    mask = labels == i
    plt.scatter(lengths[mask], shuffles[mask], label=f"Cluster {i}")

plt.xlabel("List Length")
plt.ylabel("Attempts to Return to Original")
plt.title("Clustered Trendlines")
plt.legend()
plt.show()

# Optionally, save separated groups
for i in range(k):
    mask = labels == i
    np.savetxt(f"cluster{i}.txt", data[mask], fmt="%.2f", delimiter=",")
