from switch import start_menu_switch

def __main__():

    welcome = open('./Menu/welcome.txt')

    print(welcome.read())

    start_menu_switch()

__main__()