# Author: Woosung Lim wml5207@psu.edu
# Collaborator: Yuxin Kang yjk5152@psu.edu
# Collaborator: Luke Bowman lkb5453@psu.edu
# Collaborator: Kelly Wolfe knw5289@psu.edu
# Section: 2
# Breakout: 3

def getLetterGrade():
  grade = input("Enter your CMPSC 131 grade: ")
  grade = float(grade)
  if grade >= 93.0:
    return "A"
  elif grade < 93.0 and grade >= 90.0:
    return "A-"
  elif grade < 90.0 and grade >= 87.0:
    return "B+"
  elif grade < 87.0 and grade >= 83.0:
    return "B"
  elif grade < 83.0 and grade >= 80.0:
    return "B-"
  elif grade < 80.0 and grade >= 77.0:
    return "C+"
  elif grade < 77.0 and grade >= 70.0:
    return "C"
  elif grade < 70.0 and grade >= 60.0:
    return "D"
  else:
    return "F"
def run():
  grade = getLetterGrade()
  print(f"Your letter grade for CMPSC 131 is {grade}.")

if __name__ == "__main__":
  run()