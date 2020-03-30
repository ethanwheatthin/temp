from random import randint

import firebase_admin
from firebase_admin import db

from firebase_admin import credentials

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == "__main__":
    usedKeys = open('UsedKeys.txt', 'a')
    usedKeysList = []
    cred = credentials.Certificate("/Users/EthanCC/Downloads/linedance-f12c4-firebase-adminsdk-aizzs-a0fcca8688.json")
    #firebase_admin.initialize_app(cred)
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://linedance-f12c4.firebaseio.com/'
    })

    # As an admin, the app has access to read and write all data, regradless of Security Rules
    counter = 1
    for i in range(3):
        newKey = random_with_N_digits(5)
        usedKeysList.append(newKey)

        if not newKey not in usedKeysList:
            usedKeys.write(str(newKey) + "\n")
            ref = db.reference('Dance_Details').child("DanceID_"+str(newKey))
            ref.set({
                'Dance_Name': 'TEST NEW DANCE NAME ' + str(counter),
                'Dance_Difficulty': 'TEST MEDIUM DIFFICULTY ' + str(counter),
                'Dance_Music': 'NEW test music' + str(counter),

            })
            counter += 1
            print(ref.get())
        else:
            newKey = random_with_N_digits(5)
