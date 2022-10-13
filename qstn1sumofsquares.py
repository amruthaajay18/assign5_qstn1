class Point:

    def __init__(self,first,second,third,):
        self.first = first
        self.second = second
        self.third= third
    def sqSum(self):
        sq1=self.first*self.first
        sq2=self.second*self.second
        sq3=self.third*self.third
        tot=(sq1+sq2+sq3)
        return tot
obj=Point(1,3,5)
print (obj.sqSum())

        

        