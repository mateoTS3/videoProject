import numpy as np

def recursive_points(f,df,x0,y0,h,n):
        '''
        f: function that returns float
        df: gradient of function that returns np.array of of two vector components
        x0: initial x value
        y0: initial y value
        h: step size
        n: iterate from p_0 to p_n
        '''

        # define list of points and add p_0
        points = [np.array([x0, y0, f(x0, y0)])]

        # recursively add points to the list
        for i in range(n):
            p = points[-1] # get p(n-1)
            d = df(p[0], p[1]) # get gradient value at p(n-1)
            
            p_new = np.array([p[0] + h * d[0], p[1] + h * d[1], 0]) # add new coordinates
            p_new[2] = f(p_new[0], p_new[1]) # add function value to new point

            points.append(p_new)

        return points

if __name__ == "__main__":
    points = recursive_points(lambda u, v: u*v, lambda u, v: np.array([v, u]), 1.1, -0.9, 0.1, 10)
    for i in points:
        print(i)