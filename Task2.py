import re
def alpha_numeric():
    x=input("Enter your character:")
    cleanString = re.sub('[^A-Za-z0-9]+','', x )
    print("output list is : "+cleanString)
alpha_numeric()
