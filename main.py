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

class Gradient(ThreeDScene):
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

        # SURFACES
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-4, 4],
            v_range=[-4, 4],
            resolution=(8, 8),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )

        surface2 = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-4, 4],
            v_range=[-1, 4],
            resolution=(8, 5),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )        

        surface3 = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[1, 4],
            v_range=[-4, 4],
            resolution=(3, 8),
            checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )            

        # PARTIALS
        curve_x = ParametricFunction(
            lambda t: np.array([t, -1, np.sin(t) * np.cos(-1)]),
            t_range=[-5,5],
            color=RED
        )
        vector_x = Vector([np.cos(1) * np.cos(-1), 0, 0], color=YELLOW).shift(np.array([1, -1, np.sin(1) * np.cos(-1)]))
        tan_x = ParametricFunction(
            lambda t: np.array([1 + t, -1, np.sin(1) * np.cos(-1) + np.cos(1) * np.cos(-1) * t]),
            t_range=[-6,4],
            color=YELLOW
        )

        curve_y = ParametricFunction(
            lambda t: np.array([1, t, np.sin(1) * np.cos(t)]),
            t_range=[-5,5],
            color=RED
        )
        vector_y = Vector([0, np.sin(1) * -np.sin(-1), 0], color=YELLOW).shift(np.array([1, -1, np.sin(1) * np.cos(-1)]))
        tan_y = ParametricFunction(
            lambda t: np.array([1, -1 + t, np.sin(1) * np.cos(-1) + np.sin(1) * -np.sin(-1) * t]),
            t_range=[-5,5],
            color=YELLOW
        )

        grad_vector = Vector([np.cos(1) * np.cos(-1), np.sin(1) * -np.sin(-1), 0], color=YELLOW).shift(np.array([1, -1, np.sin(1) * np.cos(-1)]))
        grad_tan = ParametricFunction(
            lambda t: np.array([1 + np.cos(1) * np.cos(-1) * t, -1 + np.sin(1) * -np.sin(-1) * t, np.sin(1) * np.cos(-1) + (np.sin(1) ** 4 + np.cos(1) ** 4) * t]),
            t_range=[-6,9],
            color=RED
        )





        # ANIMATIONS
        self.play(FadeIn(axes), Write(labels), Create(surface))        
        self.move_camera(
                    phi=45 * DEGREES, 
                    theta=-120 * DEGREES, 
                    zoom=1.2, 
                    run_time=3
                )
        self.wait(2)

        # x partials
        original_surface = surface.copy()
        self.play(Transform(surface, surface2))
        self.play(Create(curve_x))
        self.play(Create(vector_x))
        vector_x_copy = vector_x.copy()
        self.play(Transform(vector_x, tan_x))
        self.wait(1)

        # y partials
        self.play(FadeOut(curve_x), FadeOut(vector_x), Transform(surface, surface3))
        self.play(Create(curve_y))
        self.play(Create(vector_y))
        vector_y_copy = vector_y.copy()
        self.play(Transform(vector_y, tan_y))
        self.wait(1)

        # zoom on point
        self.play(FadeOut(curve_y), FadeOut(vector_y), Transform(surface, original_surface))
        self.move_camera(
            phi=20 * DEGREES,
            theta=-135 * DEGREES,
            zoom=2,
            frame_center=(1, -1, np.sin(1) * np.cos(-1)),
            run_time=2,
        )
        self.wait(1)

        # show components and gradient vector
        self.play(FadeIn(vector_x_copy), FadeIn(vector_y_copy))
        self.play(Create(grad_vector))
        self.wait(1)
        self.play(Create(grad_tan))

        # move to better angle
        self.move_camera(
            phi=80 * DEGREES,
            theta=-45 * DEGREES,
            zoom=3,
            run_time=4
        )
        self.wait(2)





def main():
    print("Hello from videoProject!")

if __name__ == "__main__":
    main()