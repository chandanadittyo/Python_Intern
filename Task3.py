def string_count():
    string_1 = input("String 1 here: ")
    string_2 = input("string 2 here: ")
    if (string_2 in string_1):
        times = string_1.count(string_2)
        print("Here string_2 occur in string_1" +" "+ str(times)+" " + "times")
string_count()

