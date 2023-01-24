class buttons():
    def __init__(self,word,spaces,border):
        self.word = word
        self.spaces = spaces
        self.border = border
        self.num_of_bord = 1 + self.spaces + len(self.word) + self.spaces + 1
        print(self.word,"Button Specifications:")
        print("Button name:",self.word)        
        print("Number of the border characters for the top and the bottom:",self.num_of_bord)
        print('Number of spaces between the left side border and the first character of the button name:',self.spaces)
        print("Number of spaces between the right side border and the last character of the button name:",self.spaces)
        print("Characters representing the borders:",self.border)
        print(self.border*self.num_of_bord)
        print(self.border,end="")
        print(" "*self.spaces,end="")
        print(self.word,end="")
        print(" "*self.spaces,end="")
        print(self.border)
        print(self.border*self.num_of_bord)        
word = "CANCEL" 
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')