FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TERM=linux

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install apache2 php mysql-server php-mysql git -y

RUN git clone https://github.com/gnuboard/gnuboard5
WORKDIR /gnuboard5
RUN git checkout d0b2d6811e024ca21f5dbbd61e389d5375134796

RUN sed -i "s#/var/www/html#/gnuboard5#g" /etc/apache2/sites-enabled/000-default.conf
RUN sed -i "s#/var/www/#/gnuboard5#g" /etc/apache2/apache2.conf
RUN mkdir data
RUN chmod 707 ./data

RUN service apache2 restart

EXPOSE 80
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]