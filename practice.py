name = input("type you email: ")

if name == "rishavsharma7745@gmail.com":
    print("You email is correct")
    tic = int(input("Enter your reservation code so we can check your tickets: "))
    if tic == 123:
        print("You have reserved a premium suite. Please wait while we prepare your room for a comfortable rest.")
        tea = input("Please type Y if you want drink:")
        if tea == "Y":
            print("You will get a bed tea")
        else:
            print("Day without tea is not good, no worries, you can give us a call with 9 to order")
    else:
        print("please start over and enter the right key")
else:
    print("you have entered a wrong name")
