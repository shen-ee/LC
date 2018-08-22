str1 = "11dd4468"


def show(ostr,rstr):
    rstr = str(rstr)
    print("Original string:"+ostr)
    print("Return string:"+rstr)

# usage of find
rstr = str1.find("1")
show(str1,rstr)

# usage of replace
rstr = str1.replace("1","")
show(str1,rstr)

rstr = str1.replace(str1[0],"")
show(str1,rstr)

# usage of count
rstr = str1.count(str('1'))
show(str1,rstr)