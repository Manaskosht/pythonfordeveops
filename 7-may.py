name=input("enter ypur name :")
if name:
    print(f"My name is : {name}")
    address=input("enter your address :")
    if address:
        print(f"My address is : {address}")
        roll_number=int(input("enter your roll number :"))
        if roll_number == 10:
            print(f"My roll number is : {roll_number} ")
            pre_marks=int(input("enter your pre marks :"))
            if pre_marks>=500:
                print("you are eligible for Mains exam")
                mains_marks=int(input("enter your mains marks :"))
                if mains_marks>=800:
                    print("you are eligible for Interview")
                    interview_marks=int(input("enter your interview marks :"))
                    if interview_marks>=1000:
                        print("congratulations you are selected")
                    else:
                            print("you are not selected")
                else:
                        print("you are not eligible for Interview")
            else:
                    print("you are not eligible for Mains exam")
        else:
                print("roll number is not provided")
    else:
        print("address is not provided")
else:
    print("name is not provided")