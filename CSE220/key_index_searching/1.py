class key_index:
    def __init__(self,array):
        max=array[0]
        self.min=array[0]

        for i in array:
            if i> max:
                max=i
            else:
                if i < self.min:
                    self.min=i
        length=int(max+(-self.min))
        self.aux_array=[0]*((length)+1)
        print(self.min)

        for i in array:
            self.aux_array[int(i+(-self.min))]+=1
        print(self.aux_array)

    def searching(self,val):
        if self.min<0:
            val+=(-self.min)
        if val<0 or val>=(len(self.aux_array)):
            return False
        if self.aux_array[val]>0:
            return True
        else:
            return False
    def sorted_array(self):
        length=0
        for i in self.aux_array:
            length+=i
        new=[None]*(length)
        print(new)
        size=0


        for i in range(len(self.aux_array)):
            if self.aux_array[i]!=0:
                for j in range(self.aux_array[i]):
                    print(i)
                    new[size]=i+self.min
                    size+=1
        print(new)
        
a=key_index([2, 5, 1.2, 6.7, 1.7, 9.3, 2.2, 7.7, 0, -4, -5.1, 2, 5, 5.2])
print(a.searching(5))
a.sorted_array()