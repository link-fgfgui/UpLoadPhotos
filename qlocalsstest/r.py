import os,threading,sys
i,l=int(sys.argv[1]),[]
for _ in range(i):
    l.append(threading.Thread(target=lambda:os.startfile('.\client.py')))
for j in range(i):
    l[j].start()
for j in range(i):
    l[j].join()