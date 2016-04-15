class ArrogantProfessor(Professor): 
    def say(self, stuff): 
        return Person(self.name).say('It is obvious that ' + Person(self.name).say(stuff))
    def lecture(self, stuff):
        return 'It is obvious that ' + Person(self.name).say(stuff)