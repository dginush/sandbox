class Grade:
    def __init__(self, gradeValue, gradeWeight):
        self.gradeValue = gradeValue
        self.gradeWeight = gradeWeight
        if self.gradeValue < 0 or self.gradeValue > 100:
            print('Grade should be 0-100')
        if self.gradeWeight < 1 or self.gradeWeight > 4:
            print('Weight should be 1-4')

    def __str__(self):
        return "Grade Value: {:.2f}\tGrade Weight: {}".format(self.gradeValue, self.gradeWeight)


class Subject:
    def __init__(self, subjectName):
        self.subjectName = subjectName
        self.gradesCollection = []

    def __str__(self):
        return "Subject Name: '{}'\n".format(self.subjectName)

    def addGradeObj(self, gradeObj):
        if isinstance(gradeObj, Grade):
            self.gradesCollection.append(gradeObj)
        else:
            print("Not a valid Grade object")

    def calcAverage(self):
        if len(self.gradesCollection) is 0:
            print("No grade yes for the {} subject".format(self.subjectName))
            return 0
        sumOfGrades = 0
        sumOfWeights = 0
        for gradeObj in self.gradesCollection:
            sumOfGrades += gradeObj.gradeValue * gradeObj.gradeWeight
            sumOfWeights += gradeObj.gradeWeight
        avg = sumOfGrades / sumOfWeights
        return avg

    def printAverage(self):
        return "The weighted average of '{}' is: {}".format(self.subjectName, self.calcAverage())


class Student:
    def __init__(self, studentName, studentID):
        self.studentName = studentName
        self.studentID = studentID
        self.subjectsCollection = {}
        self.averages = []

    def __str__(self):
        string = "Student Name: {}, ID:{}\nTook the following courses:\n".format(self.studentName, self.studentID)
        for subject in self.subjectsCollection.keys():
            string += ' - ' + subject + '\t\t(avg: {:.2f})\n'.format(self.calcAverageOfSubject(subject))
        return string

    def addNewSubject(self, subject):
        if isinstance(subject, Subject):
            self.subjectsCollection[subject.subjectName] = subject
        else:
            print("Not a valid Subject object")

    def addNewGradeToSubject(self, gradeObj, subjectName):
        if isinstance(gradeObj, Grade):
            self.subjectsCollection[subjectName].addGradeObj(gradeObj)
        else:
            print("Not a valid Grade object")

    def calcAverageOfSubject(self, subjectName):
        return self.subjectsCollection[subjectName].calcAverage()

    def calcAverageOfAllSubjects(self):
        avg = 0
        self.averages = sorted([(subject.subjectName, subject.calcAverage()) for subject in self.subjectsCollection.values()], key=lambda t: t[1], reverse=True)
        for i in self.averages:
            avg += i[1]
        return avg / len(self.averages)

    def findKBestSubject(self, k):
        self.calcAverageOfAllSubjects()
        k = max(k, len(self.averages))
        print("\nThose are the top {} subjects for {}:\n".format(k, self.studentName))
        for i in range(k):
            print("No. {}: '{}' with an average of {:.2f}".format(i + 1, self.averages[i][0], self.averages[i][1]))

    #     print functions
    def printAverageOfSubject(self, subjectName):
        return "{} got an average of {:.2f} in '{}'".format(self.studentName, self.calcAverageOfSubject(subjectName), subjectName)

    def printAverageOfAllSubject(self):
        return "{} got a total average of {:.2f}".format(self.studentName, self.calcAverageOfAllSubjects())


if __name__ == '__main__':
    gr1 = Grade(gradeValue=80, gradeWeight=4)
    gr2 = Grade(gradeValue=100, gradeWeight=1)
    gr3 = Grade(gradeValue=56, gradeWeight=3)
    gr4 = Grade(gradeValue=74, gradeWeight=2)
    gr5 = Grade(gradeValue=40, gradeWeight=1)
    gr6 = Grade(gradeValue=90, gradeWeight=3)

    sbj1 = Subject(subjectName="History")
    sbj2 = Subject(subjectName="Math")
    sbj3 = Subject(subjectName="Biology")
    sbj4 = Subject(subjectName="Chemistry")

    sbj1.addGradeObj(gradeObj=gr1)
    sbj1.addGradeObj(gradeObj=gr2)
    # sbj1: 'history' [(80,4),(100,1)] (avg=84)

    sbj2.addGradeObj(gradeObj=gr1)
    sbj2.addGradeObj(gradeObj=gr2)
    sbj2.addGradeObj(gradeObj=gr3)
    sbj2.addGradeObj(gradeObj=gr4)
    # sbj2: 'math' [(80,4),(100,1),(56,3),(74,2)] (avg=73.6)

    sbj3.addGradeObj(gradeObj=gr4)
    # sbj3: 'biology' [(74,2)]

    sbj4.addGradeObj(gradeObj=gr1)
    # sbj4: 'chemistry' [(80,4)]

    st1 = Student(studentName='Alon', studentID=10001)
    st2 = Student(studentName='Beth', studentID=10002)

    st1.addNewSubject(subject=sbj1)
    st1.addNewSubject(subject=sbj2)
    st1.addNewSubject(subject=sbj3)

    st2.addNewSubject(subject=sbj4)

    print('pre-add')
    print(st1.printAverageOfAllSubject())

    print(st1.printAverageOfSubject("History"))
    print(st1.printAverageOfSubject("Math"))
    print(st1.printAverageOfSubject("Biology"))
    st1.findKBestSubject(3)

    st1.addNewGradeToSubject(gradeObj=Grade(gradeValue=50, gradeWeight=2), subjectName="Math")
    st1.addNewGradeToSubject(gradeObj=Grade(gradeValue=99, gradeWeight=3), subjectName="Math")

    print('post-add')
    print(st1.printAverageOfAllSubject())
    print(st1.printAverageOfSubject("History"))
    print(st1.printAverageOfSubject("Math"))
    print(st1.printAverageOfSubject("Biology"))

    st2.addNewGradeToSubject(gradeObj=Grade(gradeValue=99, gradeWeight=3), subjectName="Chemistry")
    st2.addNewGradeToSubject(gradeObj=Grade(gradeValue=99, gradeWeight=3), subjectName="Chemistry")

    print(st2.printAverageOfAllSubject())
    print(st2.printAverageOfSubject("Chemistry"))

    st1.findKBestSubject(3)

    print(gr1)

    print('')
    print(sbj2)
    print('')
    print('')
    print(st1)
    print('')
    print(st2)
