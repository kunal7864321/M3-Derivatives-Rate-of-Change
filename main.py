
from manim import *

class DerivativesRateOfChange(Scene):

    def construct(self):
        self.camera.background_color = "#101820"

        # SCENE 1: INTRODUCTION

        title = Text(
            "DERIVATIVES",
            font_size=64,
            color=YELLOW,
            weight=BOLD
        )

        subtitle = Text(
            "Understanding the Rate of Change",
            font_size=32,
            color=WHITE
        ).next_to(title, DOWN, buff=0.5)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(8)

        self.play(FadeOut(title), FadeOut(subtitle))

        question = Text(
            "How fast is something changing?",
            font_size=40,
            color=BLUE
        )

        self.play(Write(question))
        self.wait(10)
        self.play(FadeOut(question))

        example = Text(
            "Imagine a car moving along a road.",
            font_size=34
        )

        self.play(FadeIn(example))
        self.wait(8)
        self.play(FadeOut(example))

        # SCENE 2: INTRODUCING THE FUNCTION

        heading = Text(
            "1. INTRODUCING THE FUNCTION",
            font_size=36,
            color=YELLOW
        ).to_edge(UP)

        function = MathTex(
            "f(x)=x^2",
            font_size=66,
            color=GREEN
        )

        explanation = Text(
            "This function creates a curved graph.",
            font_size=30
        ).next_to(function, DOWN, buff=0.7)

        self.play(Write(heading))
        self.play(Write(function))
        self.play(FadeIn(explanation))
        self.wait(10)

        self.play(FadeOut(function), FadeOut(explanation))

        meaning = Text(
            "A derivative tells us how quickly a function changes.",
            font_size=32,
            color=BLUE
        ).scale_to_fit_width(12)

        self.play(FadeIn(meaning))
        self.wait(10)

        self.play(FadeOut(heading), FadeOut(meaning))

        # SCENE 3: VISUALISING THE GRAPH

        heading = Text(
            "2. VISUALISING THE CURVE",
            font_size=36,
            color=YELLOW
        ).to_edge(UP)

        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 9, 1],
            x_length=9,
            y_length=5,
            axis_config={"color": WHITE}
        ).shift(DOWN * 0.3)

        graph = axes.plot(
            lambda x: x**2,
            x_range=[-3, 3],
            color=GREEN
        )

        graph_label = MathTex(
            "f(x)=x^2",
            color=GREEN
        ).to_corner(UR)

        self.play(Write(heading))
        self.play(Create(axes))
        self.play(Create(graph))
        self.play(Write(graph_label))
        self.wait(10)

        point_a = Dot(axes.c2p(2, 4), color=YELLOW)
        point_b = Dot(axes.c2p(3, 9), color=RED)

        self.play(FadeIn(point_a), FadeIn(point_b))
        self.wait(5)

        point_text = Text(
            "We choose two points: x = 2 and x = 3.",
            font_size=27
        ).to_edge(DOWN)

        self.play(FadeIn(point_text))
        self.wait(10)

        self.play(
            FadeOut(heading),
            FadeOut(axes),
            FadeOut(graph),
            FadeOut(graph_label),
            FadeOut(point_a),
            FadeOut(point_b),
            FadeOut(point_text)
        )

        # SCENE 4: AVERAGE RATE OF CHANGE

        heading = Text(
            "3. AVERAGE RATE OF CHANGE",
            font_size=36,
            color=YELLOW
        ).to_edge(UP)

        self.play(Write(heading))

        formula1 = MathTex(
            "f(x)=x^2",
            font_size=48
        )

        self.play(Write(formula1))
        self.wait(8)
        self.play(FadeOut(formula1))

        formula2 = MathTex(
            "f(2)=2^2=4",
            font_size=48
        )

        self.play(Write(formula2))
        self.wait(6)
        self.play(FadeOut(formula2))

        formula3 = MathTex(
            "f(3)=3^2=9",
            font_size=48
        )

        self.play(Write(formula3))
        self.wait(6)
        self.play(FadeOut(formula3))

        formula4 = MathTex(
            "\\frac{f(3)-f(2)}{3-2}",
            font_size=50
        )

        self.play(Write(formula4))
        self.wait(8)
        self.play(FadeOut(formula4))

        formula5 = MathTex(
            "\\frac{9-4}{3-2}=5",
            font_size=58,
            color=GREEN
        )

        self.play(Write(formula5))
        self.wait(10)

        result = Text(
            "The average rate of change is 5.",
            font_size=32,
            color=GREEN
        ).next_to(formula5, DOWN, buff=0.7)

        self.play(FadeIn(result))
        self.wait(10)

        self.play(
            FadeOut(heading),
            FadeOut(formula5),
            FadeOut(result)
        )

        # SCENE 5: DERIVATIVE USING LIMITS

        heading = Text(
            "4. FINDING THE INSTANTANEOUS RATE",
            font_size=33,
            color=YELLOW
        ).to_edge(UP)

        self.play(Write(heading))
        self.wait(5)

        formulas = [
            MathTex(
                "\\lim_{h\\to0}\\frac{f(2+h)-f(2)}{h}",
                font_size=39
            ),
            MathTex(
                "=\\lim_{h\\to0}\\frac{(2+h)^2-4}{h}",
                font_size=39
            ),
            MathTex(
                "=\\lim_{h\\to0}\\frac{4+4h+h^2-4}{h}",
                font_size=36
            ),
            MathTex(
                "=\\lim_{h\\to0}\\frac{4h+h^2}{h}",
                font_size=40
            ),
            MathTex(
                "=\\lim_{h\\to0}(4+h)",
                font_size=44
            )
        ]

        for formula in formulas:
            formula.scale_to_fit_width(12)
            self.play(FadeIn(formula))
            self.wait(8)
            self.play(FadeOut(formula))

        answer = MathTex(
            "f'(2)=4",
            font_size=75,
            color=GREEN
        )

        self.play(Write(answer))
        self.wait(12)

        explanation = Text(
            "The instantaneous rate of change at x = 2 is 4.",
            font_size=29
        ).scale_to_fit_width(12)

        explanation.next_to(answer, DOWN, buff=0.7)

        self.play(FadeIn(explanation))
        self.wait(12)

        self.play(
            FadeOut(heading),
            FadeOut(answer),
            FadeOut(explanation)
        )

        # SCENE 6: INTERPRETATION AND SUMMARY

        heading = Text(
            "5. WHAT DOES THE ANSWER MEAN?",
            font_size=35,
            color=YELLOW
        ).to_edge(UP)

        self.play(Write(heading))

        interpretation = Text(
            "At x = 2, the slope of the curve is 4.",
            font_size=32,
            color=GREEN
        )

        self.play(FadeIn(interpretation))
        self.wait(12)
        self.play(FadeOut(interpretation))

        summary_title = Text(
            "KEY TAKEAWAYS",
            font_size=42,
            color=YELLOW
        )

        self.play(Write(summary_title))
        self.wait(5)
        self.play(FadeOut(summary_title))

        points = VGroup(
            Text("1. Derivatives measure change.", font_size=29),
            Text("2. The derivative represents slope.", font_size=29),
            Text("3. Limits find instantaneous change.", font_size=29),
            Text("4. For f(x) = x², f'(2) = 4.", font_size=29, color=GREEN)
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.55
        )

        points.scale_to_fit_width(12)

        self.play(FadeIn(points, lag_ratio=0.4))
        self.wait(15)

        self.play(FadeOut(heading), FadeOut(points))

        # FINAL CREDITS: FIXED SPACING

        thanks = Text(
            "THANK YOU!",
            font_size=58,
            color=GREEN,
            weight=BOLD
        )

        name = Text(
            "Created by Kunal Kumar Jha",
            font_size=27,
            color=WHITE
        )

        student_id = Text(
            "Student ID: E25B070616",
            font_size=23,
            color=GRAY
        )

        credits = VGroup(
            name,
            student_id
        ).arrange(
            DOWN,
            buff=0.4
        )

        credits.next_to(
            thanks,
            DOWN,
            buff=0.8
        )

        self.play(Write(thanks))
        self.play(FadeIn(credits, shift=UP))
        self.wait(15)

        self.play(
            FadeOut(thanks),
            FadeOut(credits)
        )
