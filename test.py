v=200
w=6
if w<2 or w%2!=0 or v>=w:
    print("invalid")
else:
    fw=(w-2*v)//2
    tw=v-fw
    print(fw)
    print(tw)

