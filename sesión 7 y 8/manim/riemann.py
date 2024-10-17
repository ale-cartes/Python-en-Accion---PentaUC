from manim import *
import numpy as np

class RiemannSum(Scene):
    def construct(self):
        # Define the function
        title = Text("Suma de Riemann", color=BLUE).to_edge(UL)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        
        func = lambda x: 0.2 * x**2 + 2

        x_min, x_max = 0, 6
        x = np.linspace(x_min, x_max, 200)
        minf, maxf = min(func(x)), max(func(x))
        
		# Create axes
        axes = Axes(x_range=[x_min, x_max, 1],
                    y_range=[0, maxf, 2],
                    axis_config={"color": BLUE},
                    tips=False
                    ).add_coordinates()
        
        # labels = axes.get_axis_labels(x_label="x", y_label="f(x)")

		# Plot the function
        graph = axes.plot(func, color=WHITE)

		# Create Riemann rectangles
        self.play(Create(axes))
        self.play(Create(graph))

        n_s = [1, 2, 4, 10, 50, 100, 250, 500]
        for n in n_s:
            dx = (x_max - x_min) / n
            
            riemann_right = axes.get_riemann_rectangles(graph,
                                                        x_range=[x_min, x_max],
                                                        dx=dx,
                                                        input_sample_type="right",
                                                        stroke_width=0.5,
                                                        stroke_color=WHITE,
                                                        color=PURPLE
                                                        )
            riemann_left = axes.get_riemann_rectangles(graph,
                                                       x_range=[x_min, x_max],
                                                       dx=dx,
                                                       input_sample_type="left",
                                                       stroke_width=0.5,
                                                       stroke_color=WHITE,
                                                       color=GREEN
                                                       )
            
            dx_line = Line(
                start=axes.c2p(x_min, 0),
                end=axes.c2p(x_min + dx, 0),
                color=YELLOW, stroke_width=10
                )

            # Create a Text object to label dx
            dx_label = MathTex(r"\Delta x",
                               font_size=44,
                               color=YELLOW)
            dx_label.next_to(dx_line, UP)
            
            n_label = MathTex(f"n = {n}",
                              font_size=44,
                              color=WHITE).to_corner(UL)

            # Add everything to the scene
            
            riemann_right.set_z_index(-2)
            riemann_left.set_z_index(-1)
            self.play(Write(n_label),
                      Create(dx_line),
                      Write(dx_label))
            
            
            self.play(Create(riemann_right))
            # self.play(Create(riemann_left))
            
            self.wait(3)
            
            if n != n_s[-1]:
                self.play(FadeOut(riemann_right),
                        #   FadeOut(riemann_left),
                          FadeOut(n_label),
                          FadeOut(dx_line),
                          FadeOut(dx_label))

# To render the video, run the following command in the terminal:
# manim -pql riemann.py RiemannSum