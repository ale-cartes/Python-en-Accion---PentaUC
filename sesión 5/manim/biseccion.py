from manim import *

class BisectionMethod(Scene):
    def construct(self):
        # Title
        title = Text("Método de la Bisección", color=BLUE).to_edge(UL)
        self.play(Write(title))
        self.play(FadeOut(title))
        
        # Function to find the root
        f = lambda x: x**3 - 6*x**2 + 4*x + 12

        # Initial interval [a, b]
        a = -0.5
        b = 4
        
        x = np.linspace(a, b, 200)
        minf, maxf = min(f(x)), max(f(x))

        # Create axes
        axes = Axes(x_range=[a, b], y_range=[minf, maxf, 2],
                    axis_config={"color": BLUE},
                    tips=False
                    ).add_coordinates()

        # Plot the function
        graph = axes.plot(lambda x: f(x), color=WHITE)

        self.play(Write(axes))
        self.play(Write(graph))
        
        l1 = axes.get_vertical_line(axes.c2p(a, f(a)), color=YELLOW)
        l2 = axes.get_vertical_line(axes.c2p(b, f(b)), color=YELLOW)
        
        self.play(Create(l1))
        self.play(Create(l2))
        
        text_a = MathTex(r"a = ", color=YELLOW).to_corner(UR).shift(LEFT)
        text_a_value = MathTex(f"{a:0.1f}", color=YELLOW
                               ).next_to(text_a, RIGHT).align_to(text_a, DOWN)
        
        text_b = MathTex(r"b = ", color=YELLOW).to_corner(UR).shift(DOWN + LEFT)
        text_b_value = MathTex(f"{b:0.2f}", color=YELLOW).next_to(text_b, RIGHT)
        
        self.play(Write(text_a), Write(text_a_value),
                  Write(text_b), Write(text_b_value))
        
        # Number of iterations
        num_iterations = 8
        
        for i in range(num_iterations):
            c = (a + b) / 2
            
            point_c = Dot(axes.c2p(c, f(c)), color=PURE_RED, stroke_width=5,
                          z_index=1)
            self.play(Create(point_c))
            
            text_c = MathTex(f"c = {c:0.2f}", color=PURE_RED
                             ).to_corner(UR).shift(2*DOWN)
            self.play(Write(text_c))
            self.wait()
            
            if f(c) * f(a) < 0:
                b = c
                self.remove(l2)
                l2 = axes.get_vertical_line(axes.c2p(b, f(b)), color=YELLOW)
                self.play(Create(l2))
                
                self.remove(text_b_value)
                text_b_value = MathTex(f"{b:0.2f}", color=YELLOW
                                       ).next_to(text_b, RIGHT)
                self.play(Write(text_b_value))

            else:
                a = c
                self.remove(l1)
                l1 = axes.get_vertical_line(axes.c2p(a, f(a)), color=YELLOW)
                self.play(Create(l1))
                
                self.remove(text_a_value)
                text_a_value = MathTex(f"{a:0.2f}", color=YELLOW
                                       ).next_to(text_a, RIGHT).align_to(text_a, DOWN)
                self.play(Write(text_a_value))

            if i != num_iterations - 1:
                self.play(point_c.animate.set_fill(RED, opacity=0))
                self.remove(text_c)
            
            else:
                self.play(point_c.animate.set_style(stroke_color=YELLOW,
                                                    fill_color=YELLOW))
                
                text_c = MathTex(f"c = {c:0.2f}", color=YELLOW
                                 ).to_corner(UR).shift(2*DOWN)
                self.play(Write(text_c))
                

        # Show the plot
        self.wait()
        
