import smtplib as root
import colored
import requests
import time
import sys
from threading import Thread
import random
from termcolor import colored
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print(colored( '''

@🆃🅴🆁🅼🆄🆇@

		  
		''','magenta'))

def send_mail():
	login = input('Введите вашу почту: ')
	password = input('Введите ваш пороль от почты: ')
	U = input('URL: ' )
	toaddr = input('Кому: ' )
	topic = input('Тема: ' )
	message = input('Введите сообщение? ' )
	quantity = int(input('Кол-во: ' ) )

	for value in range( int( quantity ) ):
		msg = MIMEMultipart()

		msg[ 'Subject' ] = topic
		msg[ 'From' ] = login
		body = message
		msg.attach( MIMEText( body, 'plain' ) )

		server = root.SMTP_SSL( U, 465 )
		server.login( login, password )
		server.sendmail( login, toaddr, msg.as_string() )

		value += 1

		print('Отправить: ' + str( value ))

def main():
	send_mail()

if __name__ =='__main__':
	main()





		

