from manim import *

# class CircleToSquare(Scene):
#     def construct(self):
#         blue_circle = Circle(color=BLUE, fill_opacity=0.5)
#         green_square = Square(color=GREEN, fill_opacity=0.8)
#         self.play(Create(blue_circle))
        
#         self.play(Transform(blue_circle, green_square))

#         self.play(FadeOut(blue_circle))

#         self.play(Create(green_square))
#         self.play(green_square.animate.shift(UP * 2))
#         self.play(green_square.animate.rotate(PI /4))
#         self.play(green_square.animate.scale(0.5))
#         self.play(green_square.animate.set_fill(RED, opacity=0.5))

class movingCamera(ThreeDScene):
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

        

    def construct(self):

        axes = ThreeDAxes(
            x_range=[-6,6],
            y_range=[-6,6],
            z_range=[-3,3]
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y", z_label="z")
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-5, 5],
            v_range=[-5, 5],
            resolution=(10, 10),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )

        surface2 = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-5, 5],
            v_range=[-1, 5],
            resolution=(10, 6),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )        

        surface3 = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[3, 5],
            v_range=[-5, 5],
            resolution=(2, 10),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )                
        # self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        
        self.play(FadeIn(axes),Write(labels),Create(surface))
        self.play(ReplacementTransform(surface, surface2))
        self.play(ReplacementTransform(surface2, surface3))
        self.play(ReplacementTransform(surface3, surface))

        self.move_camera(
            phi=45 * DEGREES, 
            theta=-120 * DEGREES, 
            zoom=1.2, 
            run_time=3
        )
        self.wait(2)

def main():
    print("Hello from videoProject!")

if __name__ == "__main__":
    main()