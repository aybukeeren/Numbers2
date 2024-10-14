class Numbers:
    
    number_list = []
    def __init__(self, number):
        self.number = number
        self.number_list.append(number)
    
    def __str__(self):
        return "List =" + str(self.number_list)
    
    def total_list():
        total = sum(Numbers.number_list)
        return "List total =" + str(total)