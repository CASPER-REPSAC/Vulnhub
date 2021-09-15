def menu():
    menu_list = """
    1. \033[31mKVE-2020-1616\033[0m                     [Gnuboard5 Stored XSS]
    2. \033[31mKISA 취약점 권고사항 (210624)\033[0m     [Gnuboard5 Stored XSS]
    3. \033[31mKVE-2020-0164\033[0m                     [Gnuboard5 SQL Injection]
    4. \033[31mKVE-2020-0013\033[0m                     [Gnuboard5 Stored XSS]
    5. \033[31mKVE-2021-0172,0329,0330\033[0m           [Gnuboard5 Stored XSS]
    """
    print(menu_list)

if __name__ == "__main__":
    menu()
    select = int(input(">>> "))
