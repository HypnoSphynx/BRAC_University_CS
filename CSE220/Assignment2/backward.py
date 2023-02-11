def backward(inp,start):
    output=''
    start=start
    idx=start
    for i in range(len(inp)):
        output+=inp[idx]
        if idx==0:
            idx=len(inp)
        idx-=1
    return output
print(backward('giRtfel2th',9))