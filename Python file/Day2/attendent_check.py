No_of_lect = int(input("Enter the number of classes : "))
att_lect = int(input("Enter the number of attended lecture : "))
medical_reason = input("Enter yes /no for medical cause : ")

att_percent = (att_lect/No_of_lect)*100

if(att_percent >=75 and medical_reason=="no"):
    print("Allowed to sit in the exam")
else:
    print("Not allowed to sit in exam") 
