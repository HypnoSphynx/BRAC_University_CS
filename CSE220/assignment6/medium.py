def hocBuilder(h):
    if h==1:
        return 8
    return 5+hocBuilder(h-1)
print(hocBuilder(3))
