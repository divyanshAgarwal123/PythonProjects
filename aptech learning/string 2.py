def sfow():
    string1="welcome to SSSIT"
    substring1="SSSIT"
    substring2="to"
    substring3="me"
    print(string1.endswith(substring1))
    print(string1.endswith(substring2,2,16))
    print(string1.endswith(substring3,2,19))
def display():
    string1="welcome to SSSIT"
    substring1="SSSIT"
    substring2="to"
    substring3="me"
    print(string1.find(substring1))
    print(string1.find(substring2))
    print(string1.find(substring3))
sfow()
display()