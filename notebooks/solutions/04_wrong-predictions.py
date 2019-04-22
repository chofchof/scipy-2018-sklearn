for i in incorrect_idx:
    print('%d: Predicted %d True label %d' % (i, pred_y[i], test_y[i]))

# Plot two dimensions

_, ax = plt.subplots()
for n in np.unique(test_y):
    idx = np.where(test_y == n)[0]
    ax.scatter(test_X[idx, 1], test_X[idx, 2], color=f"C{n}", label=f"Class {str(n)}")

for i, marker in zip(incorrect_idx, ['x', 's', 'v']):
    ax.scatter(test_X[i, 1], test_X[i, 2], color="darkred", marker=marker, s=40, label=i)

ax.set(xlabel='sepal width [cm]', ylabel='petal length [cm]', title="Iris Classification results")
plt.legend(loc=1, scatterpoints=1);