def get_index(elem):
    cons_count=0
    sum_digit=0

    for i in elem:
        if i not in 'aeiou1234567890ZAEIOU' :
            cons_count+=1
        elif i>='0' and i<='9':
            sum_digit+=int(i)
    
    index=(cons_count*24+sum_digit)%5

    return index

def hashing(array):
    hash_table=[None]*len(array)

    for i in array:
        index=get_index(i)
        print(index)
        if hash_table[index]==None:
            hash_table[index]=i
        else:
            st=index+1
            for j in range(len(hash_table)):
                if hash_table[st]==None:
                    hash_table[st]=i
                    break
                else:
                    st=(st+1)%len(hash_table)
    return hash_table



print(hashing(['ST1E89B8A32','ST1E89B8A33','ST1E89B8A31','ST1E89B8A40','ST1E89B8A50']))

