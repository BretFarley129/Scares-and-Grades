import random

def grade():
    for i in range(0,10):
        grade = ""
        score = (random.random()*40)+60
        if score >=90:
            grade = "A"
        elif score >=80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        else:
            grade = "D"
        print "Score: {}; Your grade is {}".format(str(score), grade)

grade()