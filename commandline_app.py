import json
import urllib.request

url = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY'#the url to the JSON api

data = urllib.request.urlopen(url)#request for an http response
if data.status == 200:#check tthe status of the response so as to continue in accordance to it
	test1 = data.read()#read the data embeded on the HTTP response
	test2 = test1.decode("utf-8")#Decode it to a formart easily formatable
	head = data.getheader("content_type")#check for the details on the content in the response
	data2 = json.loads(test2)#convert the JSON string to a python dictinary object
	print (data2)
	print (data.status)
	#print (test1)
	print (head)
	#print (type(test1))
	#print (test2)
	#print (type(test2))
	print (type(data2))

else:
	print(data.status,"Sorry try again")
