# Made by Rajveer Chauhan

from big_ol_pile_of_manim_imports import *


class part1(Scene):
    CONFIG={
        "object_1":TextMobject("Lecture Number"),
        "object_2":Square(),
        "number":3,
        "vector":[1,1,0]
    }
    def construct(self):

        # Create TextMobjects
        first_line = TextMobject('Digital Signal Processing and its application')
        second_line = TextMobject('Sub Topic : Linearity and Shift - Invariance Property', color = GREEN)
        third_line = TextMobject('')
        forth_line = TextMobject('5',color = YELLOW)
        forth_line.scale(2)

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text
 
        self.play(Write(first_line), Write(second_line))
        
        self.wait(1)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.play(Write(self.object_1))
        self.play(self.object_1.scale,self.number)
        self.play(ReplacementTransform(self.object_1,self.object_2))
        self.play(Write(forth_line))
        
        self.wait()
        self.wait(2)


class part2(Scene):
    def construct(self):
        line1 = TextMobject('Summary of the previous lecture :', color = RED)
        line2 = TextMobject('What do we want from a discrete system?')
        line3 = TextMobject('The answer was completely captured by the following three experiments:')
        line4 = TextMobject('Exp 1,2 : ')

        line5 = TextMobject('Discrete', color = YELLOW)
        line6 = TextMobject('System', color = YELLOW)

        line7 = TextMobject('Observations :', color = RED)
        line8 = TextMobject('1) We give a complex exponential or phasor to the discrete sytsem and we',color=YELLOW)
        line9 = TextMobject(' expect that the output should also be phasor of the same frequency.',color=YELLOW)
        line10 = TextMobject('2) We will use a short-hand notation i.e Experiment 1,2 which will be',color=YELLOW)
        line11 = TextMobject('used for capturing two experiments of very similar nature in one drawing.',color=YELLOW)


        line5.move_to(UP*0.3)
        line6.move_to(DOWN*0.3)
        # ///////////////////////////////////
        line7.shift(UP*2)
        
        line8.next_to(line7, DOWN)
        line9.next_to(line8, DOWN)
        line10.next_to(line9, DOWN)
        line11.next_to(line10, DOWN)

        line9.shift(UP*0.3)
        line10.shift(UP*0.3)
        line11.shift(UP*0.6)
       
        line7.scale(0.7)
        line8.scale(0.7)
        line9.scale(0.7)
        line10.scale(0.7)
        line11.scale(0.7)
        # ///////////////////////////////////


        # FORMULA

        formula_tex = TexMobject(r"{A}_{1,2}.{e}^{j({\Omega}_{1,2}*t+{\phi}_{1,2}*t)}", color = YELLOW)
        formula_tex.scale(0.7)
        formula_tex.shift(LEFT*3.7)

        formula_tex1 = TexMobject(r"{B}_{1,2}.{e}^{j({\Omega}_{1,2}*t+{\phi}_{1,2}*t)}", color = YELLOW)
        formula_tex1.scale(0.7)
        formula_tex1.shift(RIGHT*3.7)


        # Shapes

        square = Square()
        arrow = Arrow(DOWN)
        arrow.shift(LEFT), arrow.shift(UP*0.5)
        arrow.rotate(45*DEGREES)

        arrow1 = Arrow(DOWN)
        arrow1.shift(RIGHT*2), arrow1.shift(UP*0.5)
        arrow1.rotate(45*DEGREES)

       
        
        line2.next_to(line1, DOWN)
        line2.scale(0.7)
        line3.scale(0.7)
        line3.to_edge(UP) 
        line4.to_edge(UP), line4.next_to(line3, DOWN)
                          # use FadeInFromDown(line4)



        self.play(GrowFromCenter(line1))
        self.wait(2)
        self.play(GrowFromCenter(line2))
        self.wait(2)
        self.play(ReplacementTransform(line1, line3), FadeOut(line2))
        self.wait(2)
        self.play(FadeIn(square), Write(line4))
        self.play(FadeIn(line5), FadeIn(line6)) # , square.move_to(UP*2+RIGHT)
        self.play(FadeIn(arrow), FadeIn(arrow1), FadeIn(formula_tex), FadeIn(formula_tex1))
        self.wait(5)
        self.play(FadeOut(arrow),FadeOut(arrow1),FadeOut(formula_tex),FadeOut(formula_tex1),FadeOut(square))


        square.shift(DOWN*2)
        line5.shift(DOWN*2)
        line6.shift(DOWN*2)
        arrow.shift(DOWN*2)
        arrow1.shift(DOWN*2)
        formula_tex.shift(DOWN*2)
        formula_tex1.shift(DOWN*2)


        self.play(FadeIn(square), FadeIn(line5), FadeIn(line6), FadeIn(arrow), FadeIn(arrow1), FadeIn(formula_tex), FadeIn(formula_tex1), FadeIn(line7), FadeIn(line8), FadeIn(line9), FadeIn(line10), FadeIn(line11))
        self.wait(4)

class part3(Scene):
    def construct(self):
        line1 = TextMobject('Exp 3:')
        line2 = TextMobject('Discrete',color = YELLOW)
        line3 = TextMobject('System', color = YELLOW)
        # ////////// LHS /////////////////
        line4 = TexMobject(r'{C}_{1}.{e}^{j(\Omega_{1}t+\alpha_{1})}',color=ORANGE)
        line5 = TextMobject('+', color = YELLOW)
        line6 = TexMobject(r'{C}_{2}.{e}^{j(\Omega_{2}t+\alpha_{2})}',color=ORANGE)
        # ///////// RHS /////////////////
        line7 = TexMobject(r'D_{1}.{e}^{j(\Omega_{1}t+\beta_{1})}',color=ORANGE)
        line8 = TextMobject('+', color = YELLOW)
        line9 = TexMobject(r'D_{2}.{e}^{j(\Omega_{2}t+\beta_{2})}',color=ORANGE)

        line10 = TextMobject('Observations:', color = RED)
        line11 = TextMobject('1) Same discrete system, in which we give a combination of complex',color =YELLOW)
        line12 = TextMobject('exponential or phasor to the discrete system as an input and we',color =YELLOW)
        line13 = TextMobject('expect to get the similar combination at the output as shown in figure.',color=YELLOW)
        
        line14 = TextMobject('2) The figure gives the relationship :',color=YELLOW)
        line15 = TexMobject(r'\frac{{D}_{1,2}}{{C}_{1,2}}\quad=\quad\frac{{B}_{1,2}}{A_{1,2}}\quad(1,2\quad is\quad used\quad for\quad shorthand\quad notation)',color = YELLOW)
        line16 = TextMobject('and')
        line17 = TexMobject(r'\beta_{1,2}-\alpha_{1,2}\quad=\quad\psi_{1,2}-\phi_{1,2}',color = YELLOW)

        lastline = TextMobject('''In a verbal discription we can say that, when we have a combination 
                                  of rotating complex numbers applied to a system, we get a combination
                                  of same rotating complex numbers , appropriately changed in amplitude and 
                                  phase.And change in amplitude and phase is independent of the original 
                                  amplitude and phase, i.e it is described by the system and not by the 
                                  previous amplitude and phase.''', color = GREEN)
        # /////// LHS Eqn. /////////////
        line4.shift(LEFT*3.5 + UP*0.4)
        line5.next_to(line4, DOWN)
        line6.next_to(line5, DOWN)
        # /////// RHS Eqn. /////////////
        line7.shift(RIGHT*3.5 + UP*0.4)
        line8.next_to(line7, DOWN)
        line9.next_to(line8, DOWN)

        #///////////// observation //////////////////
        line10.shift(UP*2.5)
        line11.next_to(line10,DOWN)
        line12.next_to(line11,DOWN)
        line13.next_to(line12,DOWN)

        line14.next_to(line10, DOWN)
        line15.next_to(line14, DOWN)
        line16.next_to(line15, DOWN)
        line17.next_to(line16, DOWN)

        
        
        line1.to_edge(UP)
        line3.next_to(line2, DOWN)

        line10.scale(0.7)
        line11.scale(0.7)
        line12.scale(0.7)
        line13.scale(0.7)
        line14.scale(0.7)
        line15.scale(0.7)
        line16.scale(0.7)
        line17.scale(0.7)

        line16.shift(UP*0.5)
        line17.shift(UP*0.6)

        lastline.scale(0.8)

       # //////////// SHAPES //////////////// 
        square = Square()
        square.shift(DOWN*0.3)

        arrow = Arrow(DOWN)
        arrow.shift(LEFT), arrow.shift(UP*0.2)
        arrow.rotate(45*DEGREES)

        arrow1 = Arrow(DOWN)
        arrow1.shift(RIGHT*2), arrow1.shift(UP*0.2)
        arrow1.rotate(45*DEGREES)
        
        self.play(Write(line1))
        # print block diagram
        self.play(FadeIn(square),FadeIn(line2),FadeIn(line3),FadeIn(arrow),
                  FadeIn(arrow1),FadeIn(line4),FadeIn(line5),FadeIn(line6),
                  FadeIn(line7),FadeIn(line8),FadeIn(line9))
        self.wait(3)   
        self.play(FadeOut(square),FadeOut(line2),FadeOut(line3),FadeOut(arrow),
                  FadeOut(arrow1),FadeOut(line4),FadeOut(line5),FadeOut(line6),
                  FadeOut(line7),FadeOut(line8),FadeOut(line9))    

        square.shift(DOWN*2), line2.shift(DOWN*2), line3.shift(DOWN*2),
        arrow.shift(DOWN*2), arrow1.shift(DOWN*2), line4.shift(DOWN*2), 
        line5.shift(DOWN*2), line6.shift(DOWN*2), line7.shift(DOWN*2),
        line8.shift(DOWN*2), line9.shift(DOWN*2)

        # Print block diagram again
        self.play(FadeIn(square),FadeIn(line2),FadeIn(line3),FadeIn(arrow),
                  FadeIn(arrow1),FadeIn(line4),FadeIn(line5),FadeIn(line6),
                  FadeIn(line7),FadeIn(line8),FadeIn(line9),FadeIn(line10), FadeIn(line11),FadeIn(line12),FadeIn(line13))


  
        self.wait(8)  
        self.play(FadeOut(line11),FadeOut(line12),FadeOut(line13))
        self.play(FadeIn(line14), FadeIn(line15), FadeIn(line16), FadeIn(line17))
        self.wait(8)
        self.play(FadeOut(line10),FadeOut(line14),FadeOut(line15),FadeOut(line16),FadeOut(line17),FadeOut(square),FadeOut(line2),FadeOut(line3),FadeOut(arrow),
                  FadeOut(arrow1),FadeOut(line4),FadeOut(line5),FadeOut(line6),
                  FadeOut(line7),FadeOut(line8),FadeOut(line9))
        self.play(FadeInFromDown(lastline))
        self.wait(10)


class part4(Scene):
    def construct(self):
        #COnstructing animation 
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        line1 = TextMobject('To get this kind of outputs in a system,\r\n we generally need the following 3 properties:')
        line2 = TextMobject('1. Linearity', color = RED)
        line3 = TextMobject('2. Shift-Invariance', color = GREEN)
        line4 = TextMobject('3. Stability', color = BLUE)

        line1.shift(UP)
        line2.next_to(line1, DOWN)
        line3.next_to(line2, DOWN)
        line3.shift(RIGHT*0.75)
        line4.next_to(line3, DOWN)
        line4.shift(LEFT*0.8)


        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        self.wait(1)
        self.play(FadeInFromDown(line1))
        self.play(FadeInFromDown(line2))
        self.play(FadeInFromDown(line3))
        self.play(FadeInFromDown(line4))
        self.wait(3)
        self.play(FadeOut(line1))
        self.play(FadeOut(line2))
        self.play(FadeOut(line3))
        self.play(FadeOut(line4))


class part5(Scene):
    CONFIG={
        "object_1":TextMobject("Thanks for watching",color = ORANGE),
        "object_2":Circle(),
        "number":3,
        "vector":[1,1,0]
    }
    def construct(self):
        line1 = TextMobject('Shift-Invariance:',color=GREEN)
        line2 = TextMobject('To test a system for shift-invariance, we need to perform only two experiments...')        
        line3 = TextMobject('Exp 1:')
        line4 = TextMobject('We first apply an input to the system','x[n]','and study the output','y[n]')
        line5 = TextMobject('System',color = YELLOW)
        line6 = TextMobject('x[n]',color=YELLOW)
        line7 = TextMobject('y[n]',color=YELLOW)
        line8 = TextMobject('Exp 2:')
        line9 = TextMobject("Then we take a very same system (S), Apply to it an input","x[n-n0]",
                              "\r\n, where ","n0", "is an integer and constant. And the system is shift-invariance",
                              "\r\n if and only if the output is also","y[n-n0]",".")

        line10 = TexMobject(r'y[n-n_{0}]',color = YELLOW)
        line11 = TexMobject(r'x[n-n_{0}]',color = YELLOW)
        line12 = TexMobject(r'**Should\quad hold\quad for\quad all\quad x[n]',color = YELLOW)
        line13 = TexMobject(r'**Should\quad hold\quad for\quad all\quad n_{0}',color = YELLOW)
        line14 = TextMobject('''So, when we shift the input by an integer number of samples,\r\n 
                                the only consequence on the output is that the output is shifted \r\n
                                and by the same number of samples.\r\n
                                (This holds for every possible input and every such shift)''',color=GREEN)

        #
        line4[1].set_color(PINK) 
        line4[3].set_color(PINK)
        line9[1].set_color(PINK)
        line9[3].set_color(PINK)
        line9[6].set_color(PINK)
        # //////////////////////////////////////
        line1.to_edge(UP)
        line1.scale(1.5)
        line2.next_to(line1,DOWN)
        line3.next_to(line1,DOWN)
        line4.next_to(line3,DOWN)
        line8.next_to(line1,DOWN)
        line9.next_to(line8,DOWN)
        line14.next_to(line1, DOWN)


        #Shapes//////////////////////////////////
        square = Square()
        square.shift(DOWN*0.3)

        arrow = Arrow(DOWN)
        arrow.shift(LEFT), arrow.shift(UP*0.2)
        arrow.rotate(45*DEGREES)
        # shape mods//////////////////////////////
        arrow1 = Arrow(DOWN)
        arrow1.shift(RIGHT*2), arrow1.shift(UP*0.2)
        arrow1.rotate(45*DEGREES)



        # line mods///////////////////////////////
        line2.scale(0.7)
        line4.scale(0.7)
        line5.shift(DOWN*0.3)
        line6.shift(LEFT*2.5+DOWN*0.3)
        line7.shift(RIGHT*2.5+DOWN*0.3)
        line9.scale(0.7)
        line14.scale(0.8)

        line11.shift(LEFT*3+DOWN*2.3)
        line10.shift(RIGHT*3+DOWN*2.3)

        line12.shift(UP*0.2)
        line13.shift(DOWN*0.2)
        line12.scale(0.9), line13.scale(0.9)





        self.play(FadeIn(line1),FadeInFromDown(line2))
        self.wait(6)
        self.play(FadeOut(line2))
        self.play(FadeInFromDown(line3),FadeInFromDown(line4),FadeInFromDown(square),FadeInFromDown(arrow),FadeInFromDown(arrow1),FadeInFromDown(line5),FadeInFromDown(line6),FadeInFromDown(line7))
        self.wait(6)
        self.play(FadeOut(line3),FadeOut(line4),FadeOut(square),FadeOut(arrow),FadeOut(arrow1),FadeOut(line5),FadeOut(line6),FadeOut(line7))
        self.play(FadeIn(line9),FadeIn(line8))

        square.shift(DOWN*2), line5.shift(DOWN*2), arrow.shift(DOWN*2), arrow1.shift(DOWN*2)

        self.play(FadeInFromDown(square),FadeInFromDown(line5),FadeInFromDown(arrow),FadeInFromDown(arrow1),FadeInFromDown(line11),FadeInFromDown(line10))
        self.play(FadeIn(line12),FadeIn(line13))
        self.wait(8)
        self.play(FadeOut(line9),FadeOut(line12),FadeOut(line13),FadeOut(line8))
        

        self.play(FadeInFromDown(line14))
        self.wait(10)
        self.play(FadeOut(line14), FadeOut(square),FadeOut(arrow), FadeOut(arrow1),FadeOut(line11),FadeOut(line10),FadeOut(line5))

        l1 = TextMobject('Examples :')
        l2 = TexMobject(r'Q1.\quad If\quad y[n]=3x[n]+4x[n-1]',color =YELLOW)
        l3 = TexMobject(r'then\quad x[n-n_{0}]\quad input\quad would\quad give\quad ?',color = YELLOW)
        l4 = TextMobject('Ans.')
        l5 = TexMobject(r'3x[n-n_{0}]+4x[n-{n}_{0}-1]=y[n-n_{0}]',color = GREEN)
        l6 = TextMobject("Explanation : At every point in the output you are taking 3 times the present \r\n",
                            "input samples and 4 times the past input samples. Thus it is", "Shift-Invariant", color = YELLOW).scale(0.7)
        l7 = TexMobject(r'Q2.\quad If\quad y[n]=n.x[n]\quad and\quad x[n]=\quad unit\quad impulse\quad sequence(\delta[n])', color = YELLOW).scale(0.7)
        l8 = TexMobject(r'where,\quad \delta [n]=1,\quad n=0\quad \\ \delta [n]=0,\quad n\neq 0', color = YELLOW).scale(0.7)
        l9 = TexMobject(r'y[n]=0\quad for\quad all\quad n\quad when\quad x[n]=\delta [n]',color = GREEN)
        l10 = TextMobject("Explanation : The place where impulse value is 1, is at n=0. So it gets multiplied by 0 \r\n",
                          "everywhere else in the output because it is zero everywhere else in the input, thus the \r\n",
                          "system is", "not shift-invariant",".",color=YELLOW).scale(0.7)



        l10[3].set_color(PINK)
        l10.to_edge(DOWN)

        l1.to_corner(UL, buff = 1.5)
        l2.next_to(l1, RIGHT)
        l3.next_to(l2, DOWN)

        l4.to_edge(LEFT, buff = 1.5)
        l5.next_to(l4, RIGHT*4.5)
        l6.to_edge(DOWN)
        l6[2].set_color(PINK)

        l7.next_to(l1, RIGHT)

        l8.next_to(l7, DOWN)
        l9.next_to(l4,RIGHT*4.5)


        self.play(Write(l1))
        self.play(Write(l2),Write(l3))
        self.wait(4)
        self.play(Write(l4))
        self.play(Write(l5))
        self.wait(4)
        self.play(Write(l6))
        self.wait(5)
        self.play(FadeOut(l2),FadeOut(l3),FadeOut(l5),FadeOut(l6))
        self.wait(1)

        l1.to_edge(LEFT,buff = 0.5)
        l7.next_to(l1, RIGHT)
        self.play(Write(l7),Write(l8),Write(l9))
        self.wait(4)
        self.play(Write(l10))
        self.wait(5)
        self.play(FadeOut(l7),FadeOut(l8),FadeOut(l9),FadeOut(l10),FadeOut(l1),FadeOut(l4),FadeOut(line1))
        self.wait(1)


        # ///////////////////////////////////////////////////
        ln1 = TextMobject('What if a system is linear and shift-invariant?',color = RED).scale(0.7)
        ln2 = TextMobject('Linear and Shift-Invariance', color = GREEN).scale(1.5)
        ln3 = TextMobject('Only one experiment required to characterize the system completely!').scale(0.7)
        ln4 = TextMobject('''Theorem : A linear shift-invariance system is completely characterized by its \r\n
                             response to a UNIT IMPULSE SEQUENCE.''',color = YELLOW).scale(0.7)
        ln5 = TextMobject('Characterization means being able to determine the output, given any input.',color = PINK).scale(0.7)

        ln2.shift(UP)
        ln3.next_to(ln2, DOWN)
        ln4.next_to(ln1,DOWN)
        ln5.next_to(ln4, DOWN)



        self.play(FadeIn(ln1))
        self.wait(4)
        self.play(ReplacementTransform(ln1,ln2))
        self.wait(3)
        self.play(FadeIn(ln3))
        self.wait(5)
        self.play(FadeOut(ln3))
        self.wait(1)
        self.play(FadeIn(ln4))
        self.wait(6)
        self.play(Write(ln5))
        self.wait(6)
        self.play(FadeOut(ln2),FadeOut(ln4),FadeOut(ln5))

        self.play(Write(self.object_2))
        self.play(self.object_2.scale,self.number)
        self.play(ReplacementTransform(self.object_2,self.object_1))
        self.wait(2)
        














        
