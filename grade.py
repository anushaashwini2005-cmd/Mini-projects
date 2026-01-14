sub1=int(input("enter subject 1 marks: "))
sub2=int(input("enter subject 2 marks: "))
sub3=int(input("enter subject 3 marks: "))
sub4=int(input("enter subject 4 marks: "))
sub5=int(input("enter subject 5 marks: "))
total=sub1+sub2+sub3+sub4+sub5
print("TOTAL MARKS: ",total)
avg=(total/5)
if total==0 or total>500:
    print("INVALID OR ABSENT")
else:
    print("PERCENTAGE: ",avg,"%")
    match avg:
        case avg if avg<0 or avg>100:
            print("Invalid marks")
        case avg if avg>=90:
            print("GRADE: A+")
        case avg if avg<90 or avg >=80:
             print(" GRADE: A")
        case avg if avg<80 or avg>=70:
             print("GRADE: B+")
        case avg if avg<70 or avg>=60:
            print("GRADE: B")
        case avg if avg<60 or avg>=50:
            print("GRADE: C+")
        case avg if avg<50 or avg>=40:
            print("GRADE: C")
        case avg if avg<40:
            print("FAIL")
        