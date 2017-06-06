import random

def scoresAndGrades(score):
    s = "Score: "
    g = "Your grade is "
    sp = " "
    if score >= 90:
        print s+str(score)+sp+g+"A\n"
    if score >= 80 and score < 90:
        print s+str(score)+sp+g+"B\n"
    if score >= 70 and score < 80:
        print s+str(score)+sp+g+"C\n"
    if score >= 60 and score < 70:
        print s+str(score)+sp+g+"D\n"

scoresAndGrades(random.randint(60, 100))