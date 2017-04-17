from firebase import firebase

url = "https://minflush.firebaseio.com/"
token ="tBiu1jrmRxgmkn2XkrFyWMjEHnid8m7qG4rwhzUu"
database = firebase.FirebaseApplication(url, token)


#for i in range(1,4):
#    #database.put('/flushes/flushInstance','{}'.format(i),{'flushDetail':'[5,6]'})
#    database.post('/flushes',{'flushDetail':'[5,6]'})


#data = database.get('/flushes')

#print data

#for i in data:
#    print data[i]['flushDetail']

def pushFlushDetail(flushTime,flushDuration):
    database.post('/flushes',{'flushDetail':'[{},{}]'.format(flushTime,flushDuration)})


