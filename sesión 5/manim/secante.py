from manim import *

class SecantMethod(Scene): 
    def construct(self):
        # Title
        title = Text("Método de la Secante", color=BLUE).to_edge(UL)
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        
        
        # Function to find the root
        f = lambda x: -np.tanh(x - np.cos(x)*np.exp(x))

        # function interval [a, b]
        a = -2
        b = np.pi
        
        x = np.linspace(a, b, 200)
        minf, maxf = min(f(x)), max(f(x))

        # Create axes
        axes = Axes(x_range=[a, b], y_range=[minf, maxf, 0.2],
                    axis_config={"color": BLUE},
                    tips=False
                    ).add_coordinates()

        # Plot the function
        graph = axes.plot(lambda x: f(x), color=WHITE)

        self.play(Write(axes))
        self.play(Write(graph))
        
        # initial guest: x0, x1
        x0 = -1
        x1 = 3
        
        text_x0 = MathTex(r"x_{0} = ", color=WHITE).to_corner(UR).shift(LEFT)
        text_x0_value = MathTex(f"{x0:0.1f}", color=YELLOW
                                ).next_to(text_x0, RIGHT).align_to(text_x0, DOWN)
        
        text_x1 = MathTex(r"x_{1} = ", color=WHITE).to_corner(UR).shift(DOWN + LEFT)
        text_x1_value = MathTex(f"{x1:0.2f}", color=GOLD
                                ).next_to(text_x1, RIGHT).align_to(text_x1, DOWN)
        
        # Number of iterations
        num_iterations = 7
        
        for i in range(num_iterations):

            # Show the initial guess
            
            if i == 0:
                dot_x0 = Dot(axes.coords_to_point(x0, f(x0)), color=YELLOW,
                             z_index=3)
                dot_x1 = Dot(axes.coords_to_point(x1, f(x1)), color=GOLD,
                             z_index=2)

                self.play(Create(dot_x0), Create(dot_x1))
                self.play(Write(text_x0), Write(text_x0_value),
                          Write(text_x1), Write(text_x1_value))
            
            else:
                self.play(dot_x0.animate.move_to(axes.coords_to_point(x1, f(x1))),
                          dot_x1.animate.move_to(axes.coords_to_point(x2, f(x2))),
                          FadeOut(secant), FadeOut(secant_line_extended),
                          FadeOut(text_x0_value), FadeOut(text_x1_value))
                
                color1 = YELLOW_C if i == num_iterations - 1 else YELLOW
                color2 = YELLOW_C if i == num_iterations - 1 else GOLD
                
                text_x0_value = MathTex(f"{x1:0.2f}", color=color1
                                        ).next_to(text_x0, RIGHT).align_to(text_x0, DOWN)
                text_x1_value = MathTex(f"{x2:0.2f}", color=color2
                                        ).next_to(text_x1, RIGHT).align_to(text_x1, DOWN)

                self.play(Write(text_x0_value), Write(text_x1_value),
                          FadeOut(vertical_line),
                          dot.animate.set_fill(PURE_RED, opacity=0))
                
                if i == num_iterations - 1:
                    self.play(dot_x0.animate.set_fill(color1, opacity=1))

                x0 = x1
                x1 = x2
            
            # New guess
            x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
            
            
            # Secant line
            start_point = axes.coords_to_point(x0, f(x0))
            end_point = axes.coords_to_point(x1, f(x1))
            
            secant = Line(start_point, end_point, color=YELLOW)
            self.play(Create(secant))
            
            if x1 < x2:
                secant_line_extended = DashedLine(end_point,
                                                  axes.coords_to_point(x2, 0),
                                                  color=YELLOW)
            else:
                secant_line_extended = DashedLine(axes.coords_to_point(x2, 0),
                                                  end_point,
                                                  color=YELLOW)
            
            self.play(Create(secant_line_extended))
            
            # Show the new guess
            dot = Dot(axes.coords_to_point(x2, 0), color=PURE_RED,
                      stroke_width=5, z_index=1)
            vertical_line = axes.get_vertical_line(axes.coords_to_point(x2, f(x2)),
                                                   color=YELLOW)
            
            self.play(Create(dot))
            self.play(Create(vertical_line))
                

        # Show the plot
        self.wait()

        
