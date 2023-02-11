def forward(inp,st):
    output=''
    start=st
    idx=start
    for i in range(len(inp)):
        output+=inp[idx]
        idx=(idx+1)%len(inp)
    return output
print(forward('rightLeft2',5))
print(forward('rightLeft2',5))