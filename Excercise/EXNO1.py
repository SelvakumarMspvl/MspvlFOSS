#Students Detail

mainList=[

]
def getStudentDetails():
    # To get the student's detail and return as List
    while True:
        try:
            roll_no = int(input("Enter the roll number of the student:"))
            name = input("Enter the name of the student:")
            dept = input("Enter the department name:")
            precentage = float(input("Enter the precentage of Mark(with decimal value):"))
            tempList = [roll_no,name,dept,precentage]
            return tempList
        except ValueError:
            print("Invalid")
            # return None
        except TypeError:
            print("Invalid Type of Value")
        # return None


def printStudentDetails(st):
    #to print the students details
    j = 0
    print("Student Details")
    print("~~~~~~~~~~~~~~~")
    for i in range(len(st)):
        print(f"Student{i+1} Details:")
        print(f"Name:{st[i][j+1]}\n"
              f"Roll_No:{st[i][j]}\n"
              f"Department:{st[i][j+2]}\n"
              f"Percentage:{st[i][j+3]}")


def main():
    try:
        num = getNumberOfStudents()
        student = [

        ]
        for i in range(num):
            print(f"Student-{i+1} Details")
            print("~~~~~~~~~~~~~~~~~~~~~~")
            student = getStudentDetails()
            mainList.append(student)
            student = [

            ]
        printStudentDetails(mainList)
    except ValueError and TypeError:
        print("Invalid Value has been returned")


def getNumberOfStudents():
    while True:
        try:
        #to get and return the number of students in int type
            n = int(input("Enter the number of students to register:"))
            return n
        except ValueError:
            print("Invalid Value have been detected")
            #return None

if __name__ == '__main__':
    main()
