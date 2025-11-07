import turtle

class LSystem2D:
    def __init__(self, t, axiom, width, length, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.length = length
        self.angle = angle
        self.t = t
        self.rules = {}
        self.t.pensize(self.width)

    def add_rules(self, *rules):
        for key, value in rules:
            self.rules[key] = value

    def generate_path(self, n_iter):
        for _ in range(n_iter):
            next_state = ""
            for ch in self.state:
                next_state += self.rules.get(ch, ch)
            self.state = next_state

    def draw_turtle(self, start_pos, start_angle, repetitions=1, turn=0):
        turtle.tracer(0, 0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.setheading(start_angle)
        self.t.down()

        for _ in range(repetitions):
            for move in self.state:
                if move == 'F':
                    self.t.forward(self.length)
                elif move == '+':
                    self.t.left(self.angle)
                elif move == '-':
                    self.t.right(self.angle)
            self.t.right(turn)

        turtle.update()
        turtle.done()


screen = turtle.Screen()
screen.setup(700, 700, 0, 0)

t = turtle.Turtle()
t.speed(0)
t.ht()

pen_width = 2
f_len = 3
angle = 60
axiom = "F--F--F"

l_sys = LSystem2D(t, axiom, pen_width, f_len, angle)
l_sys.add_rules(("F", "F+F--F+F"))
l_sys.generate_path(4)

l_sys.draw_turtle(start_pos=(-300, 100), start_angle=0, repetitions=3, turn=120)
