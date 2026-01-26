#If a string has at least 1 symbol then it's true
# if a number is !=0 then it returns true
#Any list, tuple, set, and dictionary are True, except empty ones
print(bool("Hello"))
print(bool(15))

#see how false works
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})