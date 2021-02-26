# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa=0.0, year=0):
        self.name = name
        self.gpa = gpa
        self.year = year
        self.courses = []
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def enroll(self,courses):
        self.courses = courses
        
    def display_courses(self):
        return("I am enrolled in:", self.courses)
        
    def years_until_graduation(self):
        return(4-int(self.year))
    
class Spartan(Student):
    
    def __init__(self,name='', motto = ''):
        Student.__init__(self)
        self.name = name
        self.motto = motto
    
    def set_motto(self, motto):
        self.motto = motto
        
    def school_spirit(self):
        print('My name is ',self.name)
        print('I am a Spartan. My motto is ', self.motto)
    
        