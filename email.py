print("venligst indtast din email")

email = input()

length = len(email)

if length > 7 and length < 30:

    if email.count("@") == 1:

        if email.endswith(".dk"):
                print("Gyldig email")

        else:
            print("ikke dansk email")

    else:
        print("mangler @ eller har mere end ét @ i email")

else:
    print("for kort eller lang email")
