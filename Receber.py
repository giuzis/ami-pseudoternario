import re
import os
from socket import *
import matplotlib.pyplot as plt
import numpy as np
from multiprocessing import Process
import pickle

# imprime linhas do gráfico
def my_lines(ax, pos, *args, **kwargs):
    if ax == 'x':
        for p in pos:
            plt.axvline(p, *args, **kwargs)
    else:
        for p in pos:
            plt.axhline(p, *args, **kwargs)

def plot_graph():
	plt.show()

#host = ""
#port = 13000
#buf = 1024
#addr = (host, port)
#UDPSock = socket(AF_INET, SOCK_DGRAM)
#UDPSock.bind(addr)

#print("Esperando receber a mensagem...")
#(cod, addr) = UDPSock.recvfrom(buf)
#print("Mensagem recebida: " + cod)

#data = pickle.loads(cod)

data = ['A', 0.5, -0.5, 0.5, 0, 0, -0.5, 0.5, -0.5]

if(data[0] == 'A'):
	data.pop(0)
	codfic = "AMI"
	mensagem = []
	i = 0
	while i != len(data):
		if data[i] == 0:
			mensagem.append(0)
		if data[i] == 0.5 or data[i] == -0.5:
			mensagem.append(1)
		i += 1
else:
	data.pop(0)
	codfic = "Pseudoternário"
	mensagem = []
	i = 0
	while i != len(data):
		if data[i] == 0:
			mensagem.append(1)
		if data[i] == 0.5 or data[i] == -0.5:
			mensagem.append(0)
		i += 1

strbits = ''
for bit in mensagem:
	if bit == 0:
		strbits = strbits + '0' 
	else:
		strbits = strbits + '1'

data1 = np.repeat(mensagem, 2)
data2 = np.repeat(data, 2)
t = 0.5 * np.arange(len(data1))

my_lines('y', [0, 4], color='.5', linewidth = 1)
plt.step(t, data1 + 4, 'r', linewidth = 1, where='post')
plt.step(t, data2, 'r', linewidth = 1, where='post')
plt.ylim([-1,6])

for tbit, bit in enumerate(mensagem):
	plt.text(tbit + 0.5, 5.5, str(bit))

texto = bytes(int(b, 2) for b in re.split('(........)', strbits) if b).decode('latin_1')

print(texto)

plt.text(0.1, 6.1, "Mensagem: ")
plt.text(0.1, 1, codfic)

plt.gca().axis('off')

p = Process(target=plot_graph)
p.start()

#UDPSock.close()
os._exit(0)