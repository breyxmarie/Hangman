import random
from PIL import Image
def imagehang():
    global guesses, wrongguess
    '''if wrongguess == 0:
        none = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/none.png")
        none.show()'''
    if wrongguess == 1:
        heads = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/head.png")
        heads.show()
    elif wrongguess == 2:
        body = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/body.png")
        body.show()
    elif wrongguess == 3:
        hand = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/hand 1.png")
        hand.show()
    elif wrongguess == 4:
        hands = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/hand 2.png")
        hands.show()
    elif wrongguess == 5:
        feet = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/feet 1.png")
        feet.show()
    elif wrongguess == 6:
        feets = Image.open("/Users/AUBREY MARIE/PycharmProjects/draft/handman/feet 2.png")
        feets.show()

def getword():
    with open('/Users/AUBREY MARIE/PycharmProjects/draft/handman/mgawords.txt', 'r') as txt:
        wo = []
        scraword = txt.readlines()
        num = random.randint(0, len(scraword))
        word = str(scraword[num])
        print(word)
        txt.close()
        return word

def chckletters():
    global word, gword
    word = getword()
        #getword()

    #word = "EVAPORATE"
    gword = []
    while len(gword) + 1 < len(word):
        gword.append("_")
    x = " ".join(gword)
    print(x)
    return word, gword


def inputans():
    global guesses, wrongguess
    word, gword = chckletters()
    dup = []
    wn = []

    while guesses < 6:
        guess = input("Guess The word: ").capitalize()

        if guess not in word and guess in wn:
            print("WRONG")
            print("Opps you have already entered that letter")
            y = " ".join(gword)
            print(y)
            if guesses == 6:
                None
            else:
                imagehang()
                print("You still have " + str(6 - guesses) + " guesses left")
        elif guess not in word and guess not in wn:
            wn.append(guess)
            print("WRONG")
            y = " ".join(gword)
            print(y)
            guesses += 1
            wrongguess += 1
            if guesses == 6:
                None
            else:
                imagehang()
                print("You still have " + str(6 - guesses) + " guesses left")

        elif guess in word and guess in wn:
            print("Opps you have already entered that letter")
            y = " ".join(gword)
            print(y)
            if guesses == 6:
                None
            else:

                print("You still have " + str(6 - guesses) + " guesses left")
        elif guess in word and guess not in wn:
            for letter in word:
                if letter == guess:
                    pos = word.index(letter)
                    start = pos + 1
                    if letter in gword:
                        if letter in dup:
                            pos = word.index(letter)
                            starts = pos + len(dup) + 1
                            indices = word.index(letter, starts)
                            gword[indices] = letter
                            y = " ".join(gword)
                            dup.append(letter)
                            wn.append(guess)
                            if guesses == 6:
                                None
                            else:

                                print("You still have " + str(6 - guesses) + " guesses left")
                        elif letter not in dup:
                            indices = word.index(letter, start)
                            gword[indices] = letter
                            y = " ".join(gword)
                            dup.append(letter)
                            wn.append(guess)
                            guesses += 1
                            #print("You still have " + str(6 - guesses) + " guesses left")
                            #guesses += 1
                    elif letter not in gword:
                        pos = word.index(letter)
                        gword[pos] = letter
                        wn.append(guess)
                        y = " ".join(gword)
                        guesses += 1
                        if guesses == 6:
                            None
                        else:

                            print("You still have " + str(6 - guesses) + " guesses left")

            y = " ".join(gword)
            print(y)
       # guesses += 1
    print("Oh No! You are out of guesses")

        #return y, gword,
if __name__ == "__main__":
        #chckletters()
    guesses = 0
    wrongguess = 0
    imagehang()
    inputans()