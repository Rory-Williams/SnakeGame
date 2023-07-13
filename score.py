from turtle import Turtle
ALIGN = "center"
FONT = ('Arial', 24, 'normal')
COLOUR = 'white'

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0,260)
        with open('Hiscore.txt', 'r') as hiscore:
            self.highscore = int(hiscore.read())
        self.color(COLOUR)
        self.score = 0
        self.print_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('Hiscore.txt', 'w') as hiscore:
                hiscore.write(str(self.highscore))
        self.score = 0
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f'Score: {self.score} Hiscore: {self.highscore}', align=ALIGN, font=FONT)

