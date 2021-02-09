class Piece:
    def __init__(self, x, y, color):
        self.x = x 
        self.y = y
        self.color = color
    
    def __str__(self):
        if(self.color == "r"):
            return "R"
        else:
            return "B"