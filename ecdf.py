def ecdf(data):
    """Compute ECDF for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1, 1+n) / n

    return x, y



# plot ecdf
# Compute ECDF for data: x, y
x, y = ecdf(arr)

# Generate plot
plt.plot(x, y, marker='.', linestyle='none')

# Label the axes
_ = plt.ylabel('ECDF')
#_ = plt.xlabel('x')

# Display the plot
plt.show()
