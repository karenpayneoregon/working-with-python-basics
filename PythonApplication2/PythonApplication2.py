class SampleFromOtherApp(object):
        
        def IterateArrayWithIndex():

            presidentsLastNames = [
                "Washington", 
                "Adams", 
                "Jefferson", 
                "Madison", 
                "Monroe", 
                "Adams", 
                "Jackson"
             ]

            for index in range(len(presidentsLastNames)):
                print("President {}: {}".format(
                    index + 1, 
                    presidentsLastNames[index]))