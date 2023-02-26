
class stack():
    def __init__(self,len):
        self.stack=[None]*len
        self.size=0
    
    def push(self,elem):
        if self.size>=len(self.stack):
            print('Error: Overflow exception')
            return None
        self.stack[self.size]=elem
        self.size+=1
    def peek(self):
        if self.size==0:
            return 'Underflow exception'
        return self.stack[self.size-1]
    def pop(self):
        if self.size==0:
            return 'Underflow exception'
        temp=self.stack[self.size-1]
        self.stack[self.size-1]=None
        self.size-=1
        return temp

class paranthesisBalanacing:

    def __init__(self,input):
        length=0
        for i in input:
            if i=='(' or i=='{' or i=='[' or i==')' or i=='}' or i==']':
                length+=1
        stack_class=stack(length)
        index=0
        error=None
        for i in range(len(input)):
            if input[i]=='(' or input[i]=='{' or input[i]=='[':
                stack_class.push(input[i])  
                
            else:
                if input[i]==')' or input[i]==']' or input[i]=='}':
                    if stack_class.peek()=='Underflow exception':
                        index=i
                        error=input[i]
                    else:
                        if input[i]==')' and stack_class.peek()!='(':
                            index=i
                            error=input[i]
                            break
                        elif input[i]=='}' and stack_class.peek()!='{':
                            index=i
                            error=input[i]
                            break
                        elif input[i]==']' and stack_class.peek()!='[':
                            index=i
                            error=input[i]
                            break
                elif input[i]==')' and stack_class.peek()=='(':
                    stack_class.pop()
                elif input[i]=='}' and stack_class.peek()=='{':
                    stack_class.pop()
                elif input[i]==']' and stack_class.peek()=='[':
                    stack_class.pop()
        if stack_class.size==0:
            print('correct')
        else:
            print(index)
            print(error)
            print('Incorrect')
            
            # print(stack_class.stack)
# paranthesisBalanacing('1+2*[3*3+{4-5(6(7/8/9)+10)-11+(12*8)]+14')

# paranthesisBalanacing('1+2]*[3*3+{4-5(6(7/8/9)+10)-11+(12*8)]+14')

paranthesisBalanacing('1+2*[3*3+{4-5(6(7/8/9)+10)-11+(12*8)]+14')



