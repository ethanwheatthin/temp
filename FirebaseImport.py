from firebase import firebase

firebase = firebase.FirebaseApplication('https://linedance-f12c4.firebaseio.com/Dance_Details', None)
result = firebase.get('/Dance_Details', None)
print (result)
#{'1': 'John Doe', '2': 'Jane Doe'}