# Using a property to (indirectly) access data in an object

class Student():

    def __init__(self, name, starting_grade=0):
        self.name = name
        self.grade = starting_grade

    # Getter method
    @property
    def grade(self):
        # Private intance variable
        return self.__grade

    # Setter method
    @grade.setter
    def grade(self, newGrade):
        try:
            newGrade = int(newGrade)
        except (TypeError, ValueError) as e:
            raise type(e)('New grade: ' + str(newGrade) + ', is an invalid type.')
        if (newGrade < 0) or (newGrade > 100):
            raise ValueError('New grade ' + str(newGrade) + ', must be between 0 and 100.')
        self.__grade = newGrade

