faces = fetch_olivetti_faces()

# set up the figure
fig, axes = plt.subplots(nrows=8, ncols=8, figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the digits: each image is 8x8 pixels
for i, ax in enumerate(np.ravel(axes)):
    ax.imshow(faces.images[i], cmap=cm.bone, interpolation='nearest')
    ax.set(xticks=[], yticks=[])