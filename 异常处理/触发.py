def functionName(level):
    if level < 1:
        raise Exception("Invalid leve1!",level)
    print "Ok"

try:
    functionName(4)
except "Invalid level!":
    print "user defined exception"
else:
    print "else....."
finally:
    print "finally always run....."
    
