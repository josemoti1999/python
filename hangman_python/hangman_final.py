import random
from cs1graphics import *

# make sure you have cs1graphics.py file on the same paths
paper = Canvas(500, 500, 'skyBlue')
# list of the words to be used
word_list = ['hurricane',
                'america',
                'european',
                'czeckoslovakia', 
                'abruptly',
                'absurd',
                'abyss',
                'affix',
                'askew',
                'avenue',
                'awkward',
                'axiom',
                'azure',
                'bagpipes',
                'bandwagon']
print(len(word_list))

# this is an event handler class from cs1graphics which helps in getting
# in time query data from the user
class BasicHandler(EventHandler):
    def __init__(self, paper):
        EventHandler.__init__(self)
        self.the_word = word()
        self.word_list = self.the_word.split()
        self.clue = len(self.the_word) * ["-"]
        self.tries = 6
        self.letters_tried = ""
        self.guesses = 0
        self.letters_right = 0
        self.letters_wrong = 0
        self.curr = ''
        self.paper = paper
        
        self.tree = Layer()
        self.tree1 = Rectangle(40,300,Point(300,200))
        self.tree1.setFillColor('brown')
        self.tree2 = Rectangle(200,40,Point(350,50))
        self.tree2.setFillColor('brown')
        self.tree.add(self.tree1)
        self.tree.add(self.tree2)
        self.rope = Path(Point(400,50),Point(400,100))
        self.rope.setBorderWidth(4)
        self.rope.setBorderColor('black')
        self.tree.add(self.rope)
        self.paper.add(self.tree)
        self.text1 = Text('Lets play Hangman!')
        self.text1.moveTo(130,20)
        self.text2 = Text("The word has {} letters.".format(len(self.the_word)))
        self.text2.moveTo(130,40)
        self.text3 = Text("".join(self.clue))
        self.text3.moveTo(130,80)
        self.text3.setFontSize(30)
        self.text3.setFontColor('red')
        self.text4 = Text("")
        self.text4.moveTo(130,120)
        self.text5 = Text('Prev Guesses: ')
        self.text5.moveTo(130,160)
        self.text5_5 = Text('Enter your guesses: ')
        self.text5_5.moveTo(130,140)
        self.text5_5.setFontColor('red')
        self.text9 = Text('Remaining chances: {}'.format(6-self.letters_wrong))
        self.text9.moveTo(400,300)
        self.paper.add(self.text9)
        self.paper.add(self.text1)
        self.paper.add(self.text2)
        self.paper.add(self.text3)
        self.paper.add(self.text4)
        self.paper.add(self.text5)
        self.paper.add(self.text5_5)
        self.game_over = False

    def handle(self, event):
        if self.game_over==True and event.getDescription( ) == 'mouse click':
            self.paper.close()
        elif self.game_over==True:
            self.paper.clear()
            self.the_word = word()
            self.word_list = self.the_word.split()
            self.clue = len(self.the_word) * ["-"]
            self.tries = 6
            self.letters_tried = ""
            self.guesses = 0
            self.letters_right = 0
            self.letters_wrong = 0
            self.curr = ''
            self.paper = paper
            self.tree = Layer()
            self.tree1 = Rectangle(40,300,Point(300,200))
            self.tree1.setFillColor('brown')
            self.tree2 = Rectangle(200,40,Point(350,50))
            self.tree2.setFillColor('brown')
            self.tree.add(self.tree1)
            self.tree.add(self.tree2)
            self.rope = Path(Point(400,50),Point(400,100))
            self.rope.setBorderWidth(4)
            self.rope.setBorderColor('black')
            self.tree.add(self.rope)
            self.paper.add(self.tree)
            self.text1 = Text('Lets play Hangman!')
            self.text1.moveTo(130,20)
            self.text2 = Text("The word has {} letters.".format(len(self.the_word)))
            self.text2.moveTo(130,40)
            self.text3 = Text("".join(self.clue))
            self.text3.moveTo(130,80)
            self.text3.setFontSize(30)
            self.text3.setFontColor('red')
            self.text4 = Text("")
            self.text4.moveTo(130,120)
            self.text5 = Text('Prev Guesses: ')
            self.text5.moveTo(130,160)
            self.text5_5 = Text('Enter your guesses: ')
            self.text5_5.moveTo(130,140)
            self.text5_5.setFontColor('red')
            self.text9 = Text('Remaining chances: {}'.format(6-self.letters_wrong))
            self.text9.moveTo(400,300)
            self.paper.add(self.text9)
            self.paper.add(self.text1)
            self.paper.add(self.text2)
            self.paper.add(self.text3)
            self.paper.add(self.text4)
            self.paper.add(self.text5)
            self.paper.add(self.text5_5)
            self.game_over = False

        elif event.getDescription( ) == 'keyboard':
            print('Event Triggered')
            self.curr = event.getKey()
            if (self.letters_wrong != self.tries) and ("".join(self.clue) != self.the_word):
    
                self.text3.setMessage("".join(self.clue))
                letter = self.curr

                if len(letter) == 1 and letter.isalpha():
                    if self.letters_tried.find(letter) != -1:
                        #print("You've already picked", letter)
                        self.text4.setMessage("You've already picked {}".format(letter))
                    else:
                        self.letters_tried += letter
                        first_index = self.the_word.find(letter)

                        if first_index == -1:
                            self.letters_wrong += 1

                            if self.letters_wrong==1:
                                face = Layer()
                                head = Circle(20, Point(400,100))
                                head.setDepth(50)
                                head.setFillColor('orange')
                                face.add(head)
                                eyes = Circle(5,Point(390,90))
                                eyes.setFillColor('black')
                                eyes.setDepth(49)
                                eyes2 = eyes.clone()
                                eyes2.moveTo(410,90)
                                face.add(eyes)
                                face.add(eyes2)
                                nose = Path(Point(400,100),Point(400,110))
                                nose.setBorderWidth(4)
                                nose.setDepth(47)
                                mouth = Path(Point(390,115),Point(410,115))
                                mouth.setBorderWidth(2)
                                mouth.setDepth(48)
                                face.add(mouth)
                                face.add(nose)
                                self.paper.add(face)

                            if self.letters_wrong==2:
                                ub = Layer()
                                ub_1 = Rectangle(20,80,Point(400,160))
                                ub_1.setFillColor('red')
                                ub.add(ub_1)
                                self.paper.add(ub)

                            if self.letters_wrong==3:
                                arm_left = Path(Point(390,160),Point(370,150),Point(365,130))
                                arm_left.setBorderWidth(10)
                                arm_left.setBorderColor('orange')
                                self.paper.add(arm_left)

                            if self.letters_wrong==4:
                                arm_right = Path(Point(410,160),Point(430,150),Point(435,130))
                                arm_right.setBorderWidth(10)
                                arm_right.setBorderColor('orange')
                                self.paper.add(arm_right)

                            if self.letters_wrong==5:
                                leg_right = Path(Point(410,200),Point(430,210),Point(435,230))
                                leg_right.setBorderWidth(10)
                                leg_right.setBorderColor('orange')
                                self.paper.add(leg_right)

                            if self.letters_wrong==6:
                                leg_left = Path(Point(390,200),Point(370,210),Point(365,230))
                                leg_left.setBorderWidth(10)
                                leg_left.setBorderColor('orange')
                                paper.add(leg_left)


                            #print("Sorry there isn't any {} in the word.".format(letter))
                            self.text4.setMessage("Sorry there isn't any {} in the word.".format(letter))
                        else:
                            #print("Yay! {} is correct.".format(letter))
                            self.text4.setMessage("Yay! {} is correct.".format(letter))
                            for i in range(len(self.the_word)):
                                if letter == self.the_word[i]:
                                    self.clue[i] = letter
                else:
                    pass
                    #print("Choose another")
                    self.text4.setMessage("{}--> is not a valid entry".format(letter))

                #print('Letters wrong so far-->',letters_wrong)
                #print("".join(clue))
                #print("Guesses :", letters_tried)
                self.text5.setMessage("Prev Guesses : {}".format(self.letters_tried))
                self.text3.setMessage("".join(self.clue))
                self.text9.setMessage('Remaining chances: {}'.format(6-self.letters_wrong))
                

                if self.letters_wrong == self.tries :
                    text6 = Text("Game Over!")
                    text6.moveTo(130,400)
                    text7 = Text("The word was - {}".format(self.the_word))
                    text7.moveTo(130,420)
                    #print("Game Over!")
                    #print("The word was - {}".format(the_word))
                    self.paper.add(text6)
                    self.paper.add(text7)
                    self.game_over=True
                    text8 = Text("Click on mouse to exit, keyboard for new game")
                    text8.moveTo(160,440)
                    self.paper.add(text8)
                if "".join(self.clue) == self.the_word:
                    text6 = Text("You Win!")
                    text6.moveTo(130,400)
                    text7 = Text("The word was - {}".format(self.the_word))
                    text7.moveTo(130,420)
                    text8 = Text("Click on mouse to exit, keyboard for new game")
                    text8.moveTo(160,440)
                    self.paper.add(text8)
                    #print("You Win!")
                    #print("The word was - {}".format(the_word))
                    self.paper.add(text6)
                    self.paper.add(text7)
                    self.game_over=True
            


# function to run the game
def game():
    paper.clear()
    simple = BasicHandler(paper)
    paper.addHandler(simple)
    return

# function to decide a random word
def word():
    random_number = random.randint(0, len(word_list)-1)
    word = word_list[random_number].rstrip()
    return word


if __name__ == "__main__":
    while game():
        pass