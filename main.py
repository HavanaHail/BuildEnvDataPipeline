import csv
import struct
import matplotlib.pyplot as plt
import numpy as np
import sys, os
from numpy import nan


# starting struct
participantsCount = 0


class Participant:
    def __init__(self,idNum, o2Csv,eegEdf,eegCsv,video,panas1, panas2, date, recorder, room, universalTime):
        self.idNum = idNum
        self.o2Csv = o2Csv
        self.eegEdf = eegEdf
        self.eegCsv = eegCsv
        self.video = video
        self.panas1 = panas1
        self.panas2 = panas2
        self. date = date
        self.recorder = recorder
        self.room = room
        self.univeralTime = universalTime
        #participantsCount+=1


    rows = []
    heartRate = []
    clock = []
    ave = []
    with open("sebastian 11-18/O2Ring_20230213132922.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print(header)
    #Way to specify which column we are using
    mean = 0
    count = 0
    watch = 0
    lastbmp = 0
    #Check for motion
    for time, sp02, pulse, motion, sp02reminder, pulseReminder in rows:
        #Turn each row into a list of each thing in row
    # print (time, sp02, pulse, motion, sp02reminder, pulseReminder)
        if int(pulse)>60 and int(pulse)<100:
            #if int(pulse)<= lastbmp+7 and int(pulse)>=lastbmp-7 or lastbmp == 0:
                print(watch, pulse)
                mean += int(pulse)
                count +=1
                heartRate.append(int(pulse))
                clock.append(watch)
            #else:
            #   heartRate.append(np.nan)
            #  clock.append(watch)
        else:
            heartRate.append(np.nan)
            clock.append(watch)
        watch +=4
        lastbmp = int(pulse)
    #  paresedRow = row.split(",")
        #print(row)
    ave = int(mean/count)
    #writing in new cleaned data
    #fields = ['time','heartrate']
    #name = "CleanedData" + ".csv"
    #with open(name,'w') as csvfile:
    #    for pulse in heartRate:

    #Put NA when the number bad don't cut it
    print("Pulse average is: ", ave)
    plt.plot(clock,heartRate, label = 'Pulse')
    plt.axhline(y=ave, color = 'r', linestyle = 'dashed', label = 'Average')
    #plt.axvline(x=120,color ='g',linestyle ='dashed')
    #plt.axvline(x=300,color ='g',linestyle ='dashed')
    # plt.axvline(x=800,color ='g',linestyle ='dashed')
    plt.xlabel('time (secs)')
    plt.ylabel('heartrate')
    plt.xticks(rotation=90,fontsize='small')
    plt.title('participant #')
    plt.show()

import asyncio
# import configparser
# from graph import Graph
#
# async def main():
#     print('Python Graph Tutorial\n')
#
#     # Load settings
#     config = configparser.ConfigParser()
#     config.read(['config.cfg', 'config.dev.cfg'])
#     azure_settings = config['azure']
#
#     graph: Graph = Graph(azure_settings)
#
#     await greet_user(graph)
#
#     choice = -1
#
#     while choice != 0:
#         print('Please choose one of the following options:')
#         print('0. Exit')
#         print('1. Display access token')
#         print('2. List my inbox')
#         print('3. Send mail')
#         print('4. Make a Graph call')
#
#         try:
#             choice = int(input())
#         except ValueError:
#             choice = -1
#
#         if choice == 0:
#             print('Goodbye...')
#         elif choice == 1:
#             await display_access_token(graph)
#         elif choice == 2:
#             await list_inbox(graph)
#         elif choice == 3:
#             await send_mail(graph)
#         elif choice == 4:
#             await make_graph_call(graph)
#         else:
#             print('Invalid choice!\n')
#
# async def greet_user(graph: Graph):
#     user = await graph.get_user()
#     if user is not None:
#         print('Hello,', user.display_name)
#         # For Work/school accounts, email is in mail property
#         # Personal accounts, email is in userPrincipalName
#         print('Email:', user.mail or user.user_principal_name, '\n')
#
# async def display_access_token(graph: Graph):
#     token = await graph.get_user_token()
#     print('User token:', token, '\n')
#     #eyJ0eXAiOiJKV1QiLCJub25jZSI6Il9wZzRTZXFSdmtiaGtsbVJIMEp4T3pBRkc5LVR4T0FJYXhOOWlmbFVOZTQiLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC81ODljNzZmNS1jYTE1LTQxZjktODg0Yi01NWVjMTVhMDY3MmEvIiwiaWF0IjoxNjc3NTQ3MDY4LCJuYmYiOjE2Nzc1NDcwNjgsImV4cCI6MTY3NzYzMzc2OCwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFWUUFxLzhUQUFBQVdUQk1UT1Z2YXdQTExJcXZ5K29UNlRsOEtsMXRpQWRKcVZlQ1JRRTFBTnVJZE9iQTRWeUluNGx1UmdJZDUwS0ErTVVVVDVRWnJIb1BrL0F6VExUemxTc0F3V0dJK0hrcDhhUUM4cEdzaHk0PSIsImFtciI6WyJwd2QiLCJtZmEiXSwiYXBwX2Rpc3BsYXluYW1lIjoiQnVpbHRFbnZNUVAiLCJhcHBpZCI6IjNkOTBhMWIwLWQ2OGQtNDczMy1hNGEyLWI1NGIxZDEwYjYwNyIsImFwcGlkYWNyIjoiMCIsImNhcG9saWRzX2xhdGViaW5kIjpbImNhNzg3NDExLTdjYjYtNDEwMy05OGE3LTAwMWM4MmU3MDdkZiJdLCJmYW1pbHlfbmFtZSI6IldoYWxlbiIsImdpdmVuX25hbWUiOiJOaWNob2xhcyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjEwOC43Ljc1LjIwNiIsIm5hbWUiOiJXaGFsZW4sIE5pY2hvbGFzIiwib2lkIjoiOGExN2IwNjItZTA5NS00ZTEzLWI0ZmUtY2MyNDE5YzViNmFkIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTEwMjk5ODcxNTQtMTMzMDczMzExMC0zMjY1NjkxNDctMTQzNjY3IiwicGxhdGYiOiIxNCIsInB1aWQiOiIxMDAzMDAwMEFDMjNFRUZFIiwicmgiOiIwLkFVVUE5WGFjV0JYSy1VR0lTMVhzRmFCbktnTUFBQUFBQUFBQXdBQUFBQUFBQUFCRkFLRS4iLCJzY3AiOiJNYWlsLlJlYWQgTWFpbC5TZW5kIG9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInN1YiI6Ik43Y0hkejV0cmwyM1Y0R0xrVVcyTG9TOVpDemxXREFYdjF0QW9fOUVpQTQiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiTkEiLCJ0aWQiOiI1ODljNzZmNS1jYTE1LTQxZjktODg0Yi01NWVjMTVhMDY3MmEiLCJ1bmlxdWVfbmFtZSI6Im53aGFsZW5Ad3BpLmVkdSIsInVwbiI6Im53aGFsZW5Ad3BpLmVkdSIsInV0aSI6ImNZUVJmRkhjSWt1YnotMWdOdDRiQVEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2MiOlsiQ1AxIl0sInhtc19zc20iOiIxIiwieG1zX3N0Ijp7InN1YiI6Iks0U3ZCaWkwX09rUUU3bFo4OS1lWFlUMi03Ykk0ZWlVb21YTm9BOEVfVzgifSwieG1zX3RjZHQiOjE0MTE0MDMzMzl9.Tp1OFdRJ1FFkaqgargf7Fd4iKzyZPLrHQBk540bTj1EwLyW6fZjxtX3N2cMc1g7XPzmtDXLjUuUQwI1yvdeOHP1vEDWyvUZA0t6m3XRH2aMLXmWa5vfKl8JyUoVetiQVK1RdBLersPm-Y-JOtzhNC8g4gxDIzyWYkePkp8E3YiSVBcH4r-5u6NXY83uvCk3CYMj4qXiifRx3cKlugxmLiZHUvIWsXi9aNENJ_eTPO2v0784rRrP7d5eSA0zfuc4AX0o0gsXhZdILBZRhj6SamwHrycGrxX1OsJGiNp2ogkC7jVAIHyjhIPWkw9x8HOPo8WFsXPHe2KPQTr6HDhnFWA
#
# async def list_inbox(graph: Graph):
#     # TODO
#     return
#
# async def send_mail(graph: Graph):
#     # TODO
#     return
#
# async def make_graph_call(graph: Graph):
#     # TODO
#     return
#
# # Run main
# asyncio.run(main())