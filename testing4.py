class Student(object):

    def __init__(self, name, number):
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self): #return the student name
        return self.name

    def setScore(self, i, score): #reset the i-th score, counting  from 1
        self.scores[i -1] = score

    def getScore(self, i): #return the i-th score, counting  from 1
        return self.scores[i -1]

    def getAverageScore(self): #return the average score
        return sum(self.scores) / len(self.scores)

    def getHighScore(self):
        return max(self.scores)

    def __str__(self):
        return "name:" + self.name + "\nScores:" + " ".join(map(str, self.scores))