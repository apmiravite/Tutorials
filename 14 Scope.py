  # Add your code here
    def computeDifference(self):
        highest=0
        lowest=200
        
        for i in self.__elements:
            if i>highest:
                highest=i
            if i<lowest:
                lowest=i
        self.maximumDifference=highest-lowest
