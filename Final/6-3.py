class Professor(Lecturer):             
    def say(self, stuff): 
        return 'Prof. ' + self.name + ' says: ' + self.lecture(stuff)