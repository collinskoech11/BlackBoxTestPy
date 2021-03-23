List = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 14, 14, 16, 17, 18, 19]

lengthlist = len(List)

if (lengthlist == 0):
    print("None")
    
else: 
    def recentTrend(listOfElems):
        ''' Check if given list contains any duplicates '''
        if len(listOfElems) == len(set(List)):
            return False
        else:
            def most_frequent(List): 
                counter = 0
                num = List[0] 
                
                for i in List: 
                    curr_frequency = List.count(i) 
                    if(curr_frequency> counter): 
                        counter = curr_frequency 
                        num = i 
            
                return (num, "The most frequently repeated element")