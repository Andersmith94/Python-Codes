from testing4 import Student

s = Student("Maria", 5)
print(s)

s.setScore(1, 100)
s.setScore(3, 85)
print(s)

print("High score:", s.getHighScore())
print("Average score:", s.getAverageScore())
print("Score at position 1:", s.getScore(1))
print("Students name:", s.getName())