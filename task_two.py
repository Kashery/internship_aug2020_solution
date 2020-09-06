# I don't quite understand if I'm supposed to input the number IN range or the range itself,
# is range supposed to be random?
# I did all of them
def check_min(min):
    if 0 < int(min) < 150:
        return 0
    if int(min) < 0:
        return "Sorry, min is less than 0, try again"
    if int(min) > 150:
        return "Sorry, min is more than 150, try again"
def check_max(max, min):
    if 75<int(max)<200 and  int(min)<int(max):
        return 0
    if(int(min)<75):
        if(int(max)<75):
            return "Sorry, max is less than 75, input max again"
        if(int(max)>200):
            return "Sorry, max is more than 200, input max again"
    if(int(min)>75):
        if(int(max)<int(min)):
            return "Sorry min is more than max, input max again... you know that you are breaking rules that you yourself made up right?"
def check_minmax(nmbr, min, max):
    if int(min)<int(nmbr)<int(max):
        return 0
    if int(nmbr)<int(min):
        return "Sorry, given number is lower than your min, input again"
    if int(nmbr)>int(max):
        return "Sorry, given number is more than your max, input again"

def input_range():
    print("Please input the min, it should be less than 150 and more than 0")
    min = input()
    while check_min(min)!=0:
        print(check_min(min))
        min = input()

    print("Good, now input the max, it should be less than 200 and more than 75, keep in mind the max should be more than min")
    max = input()

    while check_max(max, min) !=0:
        print(check_max(max,min))
        max = input()
    print("Input number in range {0} - {1}:".format(min, max))
    nmbr = input()
    while check_minmax(nmbr, min, max)!=0:
        print(check_minmax(nmbr,min, max))
        nmbr = input()
    print("Well done your number is", nmbr)
input_range()

