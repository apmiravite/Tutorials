class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idnumber, scores):
        super().__init__(firstName,lastName, idnumber)
        self.scores=scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        totalscore=0
        
        for score in self.scores:
            totalscore=totalscore+score
        
        average=totalscore/(len(self.scores))
        
        if 90<=average:
            return "O"
        elif 80<=average:
            return "E"
        elif 70<=average:
            return "A"
        elif 55<=average:
            return "P"
        elif 40<=average:
            return "D"
        else: return "T"
