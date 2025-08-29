import numpy as np
import matplotlib.pyplot as plt

# loop over 5 files: cluster0.txt .. cluster4.txt
for i in range(5):
    filename = f"cluster{i}.txt"
    try:
        data = np.loadtxt(filename, delimiter=",")
    except Exception as e:
        print(f"Could not read {filename}: {e}")
        continue

    # split into x and y
    x, y = data[:, 0], data[:, 1]

    # make figure
    plt.figure()
    plt.plot(x, y, "o-", label=f"Cluster {i}")

    # formatting
    plt.title(f"Cluster {i}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.grid(True)

    # no scientific notation
    plt.ticklabel_format(style="plain", axis="both")

    # save figure
    plt.savefig(f"cluster{i}.png", dpi=200)
    plt.close()

print("Plots saved as cluster0.png .. cluster4.png")
