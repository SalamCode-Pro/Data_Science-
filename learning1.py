import matplotlib.pyplot as plt
student_names = ['Abdulsalam', 'Elon', 'Bill-Gate', 'Davido', 'Wikzid']
student_marks = [20, 50, 80, 100, 120]
student_percentage = [20*100/50, 50*100/50, 80*100/50, 100*100/50, 120*100/50]

def student_name_and_student_percentage():
    plt.title('Student plot Graph')
    plt.plot(student_names, student_marks)
    plt.xlabel('student_names')
    plt.ylabel('student_marks')
    plt.xlim(xmin= 0, xmax=5)
    plt.ylim(ymin=1, ymax=150)
    
    plt.grid(True)
    plt.show()
    
def student_bar_chart_and_student_percentage():
    height = student_names
    width = student_percentage
    plt.bar(height, width)
    plt.title('Bar Chart For Students')
    plt.xlabel('Student_Name')
    plt.ylabel('Percentage Of The Student')
    
    plt.show()
student_bar_chart_and_student_percentage()
student_name_and_student_percentage()