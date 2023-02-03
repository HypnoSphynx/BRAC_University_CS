def bunch(source):
    count=0
    bunch=1
    max_bunch=0

    while count<len(source)-1:
        if source[count]==source[count+1]:
            bunch+=1
        else:
            if max_bunch<bunch:
                max_bunch=bunch
            bunch=1
        count+=1   
    return max_bunch





print(bunch([1,1,2, 2,2,2,2, 1, 1,1,1]))