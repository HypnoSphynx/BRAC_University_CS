def bunch(source):
    count=0
    bunch=1
    max_bunch=0

    while count<len(source)-1:
        if source[count]==source[count+1]:
            bunch+=1
            if max_bunch<bunch:
                max_bunch=bunch
        else:
            bunch=1
        count+=1   
    return max_bunch


print(bunch([1, 2, 2, 3, 4, 4, 4,2,2,2,2,2,2,4,3,2,3]))