from edi_api import EdiApi

a = EdiApi()

while 1 == 1:
    request = input("Input function:")
    print(f"Initiating: {request}.")


    if request == "login":
        a.login_to_api()
        print(a.session_id)

    elif request == "logout":
        a.logout_of_api()
        print(a.session_id)