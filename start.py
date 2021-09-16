import os

vuln_list = [
    {"vuln_id" : "KVE-2020-1616",                   "describe" : "[Gnuboard5 Stored XSS]",      "path" : "gnuboard5/KVE-2020-1616/docker-compose.yml"},
    {"vuln_id" : "KISA 취약점 권고사항 (210624)",   "describe" : "[Gnuboard5 Stored XSS]",      "path" : "gnuboard5/KISA 210624/docker-compose.yml"},
    {"vuln_id" : "KVE-2020-0164",                   "describe" : "[Gnuboard5 SQL Injection]",   "path" : "gnuboard5/KVE-2020-0164/docker-compose.yml"},
    {"vuln_id" : "KVE-2020-0013",                   "describe" : "[Gnuboard5 Stored XSS]",      "path" : "gnuboard5/KVE-2020-0013/docker-compose.yml"},
    {"vuln_id" : "KVE-2021-0172,0329,0330",         "describe" : "[Gnuboard5 Stored XSS]",      "path" : "gnuboard5/KVE-2020-0172,0329,0330/docker-compose.yml"}
]


def menu():
    menu_list = ""
    for i, v in enumerate(vuln_list):
        menu_list += "{}. \033[31m{}\033[0m\t\t{}\n".format(i+1, v["vuln_id"], v["describe"])

    print(menu_list)

def executeDocker(select):
    path = vuln_list[select-1]["path"]
    os.system("docker-compose -f '{}' up -d".format(path))

if __name__ == "__main__":
    menu()
    select = int(input(">>> "))

    if select > len(vuln_list) or select < 1:
        print("[!] Error")
    else:
        executeDocker(select)
        print("\n\n\n\n=======================\n")
        print("[*] {} Done".format(vuln_list[select]["vuln_id"]))
        print("[*] You can access to 'http://yourip:8081/' ");
        print("\n=======================\n")