import time
import logging
import json
import requests
import SocketServer
import SimpleHTTPServer
import thread, threading
import Config
import collections
import random
FileLockCat = threading.Lock()
FileLockHoliday = threading.Lock()



def GetStatusFromFirstAPI():
    r = requests.get('https://holidayapi.com')
    if 200 <= r.status_code < 299:
        return 'running'
    return 'not running'


def logInTheFile(content, file_name,time_response,request):
    hashMap=dict()
    hashMap['response']=content
    hashMap['time_response']=time_response
    hashMap['headers']=str(request.headers)
    hashMap['method']=request.method
    print(hashMap)
    f = open(file_name, "at")
    f.write(json.dumps(hashMap))
    f.write('\n')
    f.close()


def SendRequestsForHolidaytAPI(lock, threadId):
    url = "https://holidayapi.com/v1/holidays"
    for i in range(0, 10):
        r = requests.get(url, params={'key': Config.HolidayAPI.API_KEY, 'country': 'US', 'year': random.randint(2010,2016),'month':random.randint(1,12),'day':random.randint(1,30)})
        with lock: logInTheFile(r.content, Config.HolidayAPI.FILE_NAME,r.elapsed.total_seconds(),r.request)
        print (r.content)
        print (r.elapsed.total_seconds())
        print (" Thread id: "+str(threadId))
        print (r.headers)


def SendRequestsForCatAPI(lock, threadId):
    url = "https://api.thecatapi.com/v1/images/search"
    for i in range(0, 50):
        r = requests.get(url)
        with lock: logInTheFile(r.content[1:-1], Config.CatsAPI.FILE_NAME,r.elapsed.total_seconds(),r.request)
        print (r.elapsed.total_seconds())
        print (" Thread id: "+str(threadId))


def runConcurentRequests():
     for i in range(0, 10):
         thread.start_new_thread(SendRequestsForHolidaytAPI, (FileLockCat, i,))

     for i in range(0, 10):
       thread.start_new_thread(SendRequestsForCatAPI, (FileLockHoliday, i,))


def GetStatusFromSecondAPI():
    r = requests.get('https://api.thecatapi.com/')
    if 200 <= r.status_code < 299:
        return 'running'
    return 'not running'


def RetriveDataFromLogsCats():
    json_data_list = open(Config.CatsAPI.FILE_NAME,"rt").readlines()
    toReturnInUI={}
    times_list=[]
    link_list=[]
    for i in json_data_list:
        whole_json=json.loads(i)
        response_json=json.loads(whole_json['response'])
        print(whole_json['response'])
        times_list.append(whole_json['time_response'])
        link_list.append(response_json['url'])
    toReturnInUI['time_response']=times_list
    toReturnInUI['response']=link_list
    return toReturnInUI

def RetriveDataFromLogsHoliday():
    json_data_list = open(Config.HolidayAPI.FILE_NAME,"rt").readlines()
    toReturnInUI={}
    times_list=[]
    days_list=[]
    for i in json_data_list:
        whole_json=json.loads(i)
        response_json=json.loads(whole_json['response'])
        if len(response_json['holidays'])>0:
            print(whole_json['response'])
            print(response_json['holidays'][0])
            times_list.append(whole_json['time_response'])
            days_list.append(response_json['holidays'][0])
    toReturnInUI['time_response']=times_list
    toReturnInUI['response']=days_list
    #print toReturnInUI['response']
    return toReturnInUI

class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        return self.send_head()

    def send_head(self):
        if self.path == "/status":
            first_status = GetStatusFromFirstAPI()
            second_status = GetStatusFromSecondAPI()
            print(first_status + second_status)
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({'HolidayAPIStatus': first_status,
                                         'CatAPIStatus': second_status}))
        elif self.path == "/runScripts":
            runConcurentRequests()
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps({'ServiceStatus1': '',
                                         'ServiceStatus2': ''}))
        elif self.path == "/metricsCat":
            toReturn=RetriveDataFromLogsCats()
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(toReturn))
        elif self.path == "/metricsHoliday":
            toReturn=RetriveDataFromLogsHoliday()
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(toReturn))


if __name__ == "__main__":
    PORT = 31338

    Handler = CORSHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print ("serving at port", PORT)
    httpd.serve_forever()
