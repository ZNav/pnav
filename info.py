import datetime
import subprocess

class info:
        def info(valuesOnly = False):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_date = now.strftime('%m/%d/%Y')
                date_chrono = now.strftime('%Y/%m/%d')
                data = subprocess.check_output(['ipconfig','/all']).decode('utf-8').split('\n')
                time = ('Time. . . . . . . . . . . . . . . : '+str(current_time))
                date = ('Date. . . . . . . . . . . . . . . : '+str(current_date))
                date_chrononice = ('Date Chrono . . . . . . . . . . . : '+str(current_date))
                ip = data[17].strip()
                ip = ip.split('(')[0]
                hostname = data[3].strip()
                dictInfo = {'time': time,'date': date,'ip': ip,'hostname': hostname,'datechrono': date_chrononice, 'fulldata': data}
                if(valuesOnly == True):
                        ip = ip.split(':')
                        hostname = hostname.split(':')
                        dictInfo = {'time': current_time,'date': current_date,'ip': ip[-1].strip(),'hostname': hostname[-1].strip(),'datechrono': date_chrono, 'fulldata': data}
                return dictInfo