class Student:
    collage_name = "Ramanashree medico legal college of arts"

    def __init__(self, stream, dept):
        self.stream = stream
        self.dept = dept

    def print_details(self):
        print(Student.collage_name)
        print("Stream: ", self.stream)
        print("Dept: ", self.dept)


getDetails = Student("Medico_Engineering", "Technical")
getDetails.print_details()
