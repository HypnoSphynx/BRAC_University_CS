enter=input('Enter')
class paranthesisBalanacing:    
    def __init__(self,input):
            self.length=0
            for i in input:
                if i=='(' or i=='{' or i=='[' or i==')' or i=='}' or i==']':
                    self.length+=1
            self.stack_class=stack(self.length)
            self.input=input
            self.index_stack=stack(self.length)
    def paranthesis(self):
        index=1
        error=None
        for i in range(len(self.input)):
            if self.input[i]=='(' or self.input[i]=='{' or self.input[i]=='[':
                self.stack_class.push(self.input[i]) 
                self.index_stack.push(i) 
            else:
                if self.input[i]==')':
                    temp=self.stack_class.pop()
                    temp1=self.index_stack.pop()
                    if temp=='(':
                        pass
                    elif temp!='(':
                        if self.stack_class.top()=='Underflow exception':
                            index=i
                            error='('
                        else:
                            index=temp1
                            error=temp
                            break
                elif self.input[i]==']':
                    temp=self.stack_class.pop()
                    temp1=self.index_stack.pop()
                    if temp=='[':
                        pass
                    elif temp!='[':
                        if self.stack_class.top()=='Underflow exception':
                            index=i
                            error='['
                        else:
                            index=temp1
                            error=temp
                        break

                elif self.input[i]=='}':
                    temp=self.stack_class.pop()
                    temp1=self.index_stack.pop()
                    if temp=='{':
                        pass
                    elif temp!='{':
                        if self.stack_class.top()=='Underflow exception':
                            index=i
                            error=temp
                        else:
                            index=temp1
                            error=temp
                        break
        print(index+1)
        print(error)
