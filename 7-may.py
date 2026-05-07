# name=input("enter ypur name :")
# if name:
#     print(f"My name is : {name}")
#     address=input("enter your address :")
#     if address:
#         print(f"My address is : {address}")
#         roll_number=(input("enter your roll number :"))
#         if len(roll_number) == 10:
#             print(f"My roll number is : {roll_number} ")
#             pre_marks=int(input("enter your pre marks :"))
#             if pre_marks>=500:
#                 print("you are eligible for Mains exam")
#                 mains_marks=int(input("enter your mains marks :"))
#                 if mains_marks>=800:
#                     print("you are eligible for Interview")
#                     interview_marks=int(input("enter your interview marks :"))
#                     if interview_marks>=1000:
#                         print("congratulations you are selected")
#                     else:
#                             print("you are not selected")
#                 else:
#                         print("you are not eligible for Interview")
#             else:
#                     print("you are not eligible for Mains exam")
#         else:
#                 print("roll number is not provided")
#     else:
#         print("address is not provided")
# else:
#     print("name is not provided")


#Ticket confirms

name = input("Enter your name :")
if name :
    print(f"Passenger Name : {name}")
    mob_num = (input("Enter your mob. number:"))
    if len(mob_num) == 10:
        print(f"Passenger Mobile Number : {mob_num}")
        pnr_num = (input("Enter your PNR No.:"))
        if len(pnr_num) == 9:
            print(f"PNR Number : {pnr_num}")
            seat_num = int(input("Enter your seat number :"))
            if seat_num:
                print("Ticket confirmed")
            else:
                print("Ticket not confirmed")
        else:
            print(f"PNR is wrong")
    else:
        print(f"Mobile number is not provided.")
else:
    print(f"Name is not provided")


