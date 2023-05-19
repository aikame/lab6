import PySimpleGUI
import socket
import random
import math

print("awaiting for connection...")
#host = ""
#port = 5000
#sock = socket.socket()
#sock.bind((host, port))
#sock.listen(1)
#conn, addr = sock.accept()
print("connected!")

def phi(n = int()):
    result=n
    i=2
    while i*i<=n:
        if(n%i==0):
            while(n%i==0):
                n=n//i
                result-=result//i
        i+=1
    if(n>1):
        result-=result//n
    return result

def FermTest(n = int(), c = int()):
    if c**(n-1) % n == 1:
        return True
    else:
        return False

def genG(p):
    while True:
        g = random.randrange(10**5 + 1, 10**6, 2)
        c = random.randint(1, 15)
        while not FermTest(g, c):
            g = random.randrange(10**5 + 1, 10**6, 2)
            c = random.randint(1, 15)
        if g**phi(p) % p == 1:
            return g


def genP():
    p = random.randrange(10**5 + 1, 10**6, 2)
    c = random.randint(1, 15)
    while not FermTest(p, c):
        p = random.randrange(10**5 + 1, 10**6, 2)
        c = random.randint(1, 15)
    return p

def DiffieHellman (a = int(), g = int(), p = int()):
    A = g**a % p
    keysSend = str(A) + " " + str(g) + " " + str(p)
    sock.send(str(keysSend).encode("ascii"))
    B = ''
    while B != '':
        B = conn.recv(1024).decode("ascii")
    B = int(B)
    return "Key: " + str(B**a % p)

p = genP()
g = genG(p)
a = random.randint(1, 1000)