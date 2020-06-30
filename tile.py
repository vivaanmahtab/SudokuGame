from constants import *

class Tile:

    # val is current val stored (and displayed) within box
    # answer refers to correct value for box

    def __init__(self, row, col, answer, original=False):

        self.row = row
        self.col = col

        self.original = original

        self.val = answer if original else 0
        self.answer = answer

        # if checked incorrect
        self.flagged = False

    def setValue(self, value):
        if not self.original:
            self.flagged = False
            self.val = value

    def getValue(self):
        return self.val

    def checkCorrect(self):

        if self.original:
            return True

        if self.val == 0:
            return False

        if str(self.val) == str(self.answer):
            return True
        self.flagged = True
        return False

    def draw(self, screen, font):
        if self.val != 0:
            if self.original:
                color = (0, 0, 0)
            else:
                color = (0, 0, 255) if not self.flagged else (255, 0, 0)
            val = font.render(str(self.getValue()), 1, color)
            screen.blit(val, val.get_rect().move(KERNING + 15 + WIDTH/9 * self.col, KERNING + 10 + HEIGHT/9 * self.row))


