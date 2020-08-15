

def online_linear_regression(x_avg, y_avg, Sxy, Sx, n, new_x, new_y):
    """
    x_avg: average of previous x, if no previous sample, set to 0
    y_avg: average of previous y, if no previous sample, set to 0
    Sxy: covariance of previous x and y, if no previous sample, set to 0
    Sx: variance of previous x, if no previous sample, set to 0
    n: number of previous samples
    new_x: new incoming 1-D numpy array x
    new_y: new incoming 1-D numpy array x
    """
    new_n = n + len(new_x)

    new_x_avg = (x_avg*n + np.sum(new_x))/new_n
    new_y_avg = (y_avg*n + np.sum(new_y))/new_n

    if n > 0:
        x_star = (x_avg*np.sqrt(n) + new_x_avg*np.sqrt(new_n))/(np.sqrt(n)+np.sqrt(new_n))
        y_star = (y_avg*np.sqrt(n) + new_y_avg*np.sqrt(new_n))/(np.sqrt(n)+np.sqrt(new_n))
    elif n == 0:
        x_star = new_x_avg
        y_star = new_y_avg
    else:
        raise ValueError

    new_Sx = Sx + np.sum((new_x-x_star)**2)
    new_Sxy = Sxy + np.sum((new_x-x_star).reshape(-1) * (new_y-y_star).reshape(-1))

    beta = new_Sxy/new_Sx
    alpha = new_y_avg - beta * new_x_avg
    return new_Sxy, new_Sx, new_n, alpha, beta, new_x_avg, new_y_avg
