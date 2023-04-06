from edi_api import EdiApi

a = EdiApi()

while 1 == 1:
    request = input("Input function:")
    print(f"Initiating: {request}.")


    if request == "login":
        a.login_to_api()
        print(a.session_id)

    elif request == "logout":
        print(a.logout_of_api())

    elif request == "today":
        print(a.search_order_filter_by_today())

    elif request == "getbyid":
        id = input('Enter ID:')
        print(a.get_order_by_id(id))

    elif request == "partners":
        print(a.check_partners())