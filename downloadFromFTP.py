from ftplib import FTP 
import time
username = "xxxxx"
password = "xxxxx"
ftp = FTP("xxxxx")
# ftp.set_debuglevel(2)
CONST_BUFFER_SIZE = 2048
ftp.login(username,password)
t = time.strftime("%Y%m%d", time.localtime())
direct = "/keyarea/"+t
ftp.cwd(direct)
ftp.retrlines('LIST')
a = ftp.pwd()
print(a,type(a))
filename = "lte_poor_cell_"+t+".csv"
print(filename)
with open(filename,"wb") as fp:
    try:
        ftp.retrbinary('RETR %s' %filename,fp.write)
    except Exception:
        print(Exception)
        
        
ftp.quit()
