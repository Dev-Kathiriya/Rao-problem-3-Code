from datetime import datetime
with open("input.txt",'r') as file:
    lst=file.read().splitlines()
    testcase=int(lst[0])
    hashMap={}
    for i in range(1,int(lst[0])+1):
        data=lst[i].split('  ')
        emp=int(data[0][-1])
        hashMap.setdefault(emp, {})
        start= datetime.strptime(data[1], '%Y-%m-%d %H:%M:%S')
        hashMap[emp]['clockIn' if data[2]=='clock-in' else 'breakStart' if data[2]=='break-start' else 'breakStop' if data[2]=='break-stop' else 'clockOut']=start
    for emp in hashMap.keys():
        print(hashMap[emp]['clockOut']-hashMap[emp]['clockIn']+hashMap[emp]['breakStop']-hashMap[emp]['breakStart'])