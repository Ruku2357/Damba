
import datetime

def memo_write(word):
    now = datetime.datetime.now()
    file_name = "/home/pi/dammemo" + now.strftime("%Y/%m/%d_%H時") + ".txt"
    log_damba = open(file_name,"a")
    log_damba.write(now.strftime("%m/%d_%H:%M:%S") + ":  " + str(word))
    log_damba.close()
