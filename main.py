from manim import *

def main():
    print("Hello from videoproject!")

if __name__ == "__main__":
    main()

class CircleToSquare(Scene):
    def construct(self):
        blue_circle = Circle(color=BLUE, fill_opacity=0.5)
        green_square = Square(color=GREEN, fill_opacity=0.8)
        self.play(Create(blue_circle))
        
        self.play(Transform(blue_circle, green_square))

        self.play(FadeOut(blue_circle))

        self.play(Create(green_square))
        self.play(green_square.animate.shift(UP * 2))
        self.play(green_square.animate.rotate(PI /4))
        self.play(green_square.animate.scale(0.5))
        self.play(green_square.animate.set_fill(RED, opacity=0.5))

class movingCamera(ThreeDScene):
    def construct(self):

        axes = ThreeDAxes()
        surface = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.sin(u) * np.cos(v)
            ]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(10, 10),
            # checkerboard_colors=[BLUE_D, BLUE_E],
            fill_opacity=0.8
        )
        # self.set_camera_orientation(phi=45 * DEGREES, theta=-45 * DEGREES)
        
        self.play(FadeIn(axes))
        self.play(Create(surface))

        self.move_camera(
            phi=45 * DEGREES, 
            theta=-120 * DEGREES, 
            zoom=1.2, 
            run_time=3
        )
        self.wait(2)
