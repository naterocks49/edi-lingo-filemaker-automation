from edi.edi_api import EdiApi

a = EdiApi()

commands = {
    "login": a.login_to_api,
    "logout": a.logout_of_api,
    "today": a.search_invoice_filter_by_today,
    "searchonhold": a.grab_all_search_on_hold,
    "test": a.grab_all_get_on_hold

}

request = input("Input function:")
print(f"Initiating: {request}.")

while 1==1:
    if request == 'logout':
        commands[request]
        break
    if request == 'getbyid':
        id = input('Enter ID:')
        a.get_invoice_by_id(id)
    if request in commands:
        commands[request]

