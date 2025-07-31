score = 100
if score >= 90:
    print("A")

score = 50
if score >= 90:
    print("A")
else:
    print("F")


score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("F")

score = 50
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

score = 50
submitted_project = True
if score >= 90:
    if submitted_project:
        print("A+")
    else:
        print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

