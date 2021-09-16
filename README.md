# Vulnhub
KVE 및 CVE 취약점 테스트 Box

## # Contributors

- [Universe](https://github.com/Universe1122)
- [Pongchi](https://github.com/Pongchi)
- [root-dove](https://github.com/root-dove)

## # Requirement

다음과 같은 프로그램이 설치되어 있어야 합니다.
```
docker
docker-compose
python3
```

## # How to Use

[아래 설명은 gnuboard5 기준 입니다.]

1. Docker를 실행할 수 있는 계정으로 start.py 파일을 실행합니다.

```
# python3 start.py 
1. KVE-2020-1616                    [Gnuboard5 Stored XSS]
2. KISA 취약점 권고사항 (210624)    [Gnuboard5 Stored XSS]
3. KVE-2020-0164                    [Gnuboard5 SQL Injection]
4. KVE-2020-0013                    [Gnuboard5 Stored XSS]
5. KVE-2021-0172,0329,0330          [Gnuboard5 Stored XSS]

>>> 
```

2. 테스트 하고자 하는 취약점 번호를 입력합니다.
3. 아래 결과 처럼 접속할 수 있는 주소가 출력됩니다. (기본 포트는 8081 입니다.)

```
...
Creating vulnhub_kisa_210604 ... done

=======================

[*] KVE-2020-0164 Done
[*] You can access to 'http://yourip:8081/' 

=======================
```

4. 생성된 container에 접속하여 다음과 같은 명령어를 입력합니다. 아래 명령어는 mysql 초기 설정을 위한 과정 입니다.

```
> docker exec -it vulnhub_kisa_210604 /bin/bash
# service mysql start
# mysql

mysql> use mysql;
mysql> alter user 'root'@'localhost' identified with mysql_native_password by 'root';
mysql> create database test;
```

5. http://yourip:8081 로 접속하게 되면, 아래 사진처럼 정상적으로 접속되는 것을 볼 수 있습니다.

![image](https://user-images.githubusercontent.com/38517436/133544642-15e5f299-7dbb-42af-84b3-793a169beef5.png)


## # Vuln List
- KVE-2020-1616
- KISA 취약점 권고사항 (210624)
- KVE-2020-0164
- KVE-2020-0013
- KVE-2021-0172,0329,0330