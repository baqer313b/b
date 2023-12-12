import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import sleep
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import random
import os
import sys
import time
import os,sys,time,json,random,re,string,platform,base64
#mport requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
import webbrowser
webbrowser.open('https://t.me/py_1hon')
import webbrowser
import requests,time,pyfiglet,datetime
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
J = '\x1b[1;38;5;178m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
re = requests.get("https://pastebin.com/raw/t0zNQScQ")
print ("\033[1;92m تسـجيل دخول نمࢪود")
print ("\033[1;97m--------------------")
print ("\033[1;97m ") 
password = input('          \033[1;93m ڪلمة السر حياتي: '+C)
print (E)
if password == "" :
  sys.exit()
if password in str(re.text):
  print(H+" FIRST STEP Is Done. Logged in Successfully as ")
  print ("\033[1;93m ")
  print("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
else:
  print (" Wrong Password ⌯")
  os.system('xdg-open https://t.me/SidraTools/1')
  sys.exit()
SDMi=""" \x1b[38;5;208m  \033[1;33m
   ──────────────────────────────────────────────────────
─██████████████─████████████───██████──────────██████─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒████─██▒▒██████████████▒▒██─
─██▒▒██████████─██▒▒████▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─██▒▒██─────────██▒▒██──██▒▒██─██▒▒██████▒▒██████▒▒██─
─██▒▒██████████─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒██─██▒▒██──██▒▒██──██▒▒██─
─██████████▒▒██─██▒▒██──██▒▒██─██▒▒██──██████──██▒▒██─
─────────██▒▒██─██▒▒██──██▒▒██─██▒▒██──────────██▒▒██─
─██████████▒▒██─██▒▒████▒▒▒▒██─██▒▒██──────────██▒▒██─
─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒████─██▒▒██──────────██▒▒██─
─██████████████─████████████───██████──────────██████─
────────────────────────────────────────────────────── """
Z = '\033[1;31m' 
X = '\033[1;33m' 
F = '\033[2;32m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'
J = '\x1b[1;38;5;178m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
import requests,bs4,json,os,sys,random,datetime,time,re
import threading
import urllib3,rich,base64
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # نـــمـــࢪودي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # نـــمـــࢪودي فاتح
a35 = '\x1b[38;5;246m'  # نـــمـــࢪودي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
import sys,time,os
class SDM:
    def __init__(self,z):
        for e in z+'\n':
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.0009)


def clear():
    os.system('clear')

print(J+'━━'*42)
print(" \033[1;34m  🔱 SDM 🔱 @M_T_F     ")
print(J+'━━'*42)
print()

import requests,time,pyfiglet,datetime
now = datetime.datetime.today()

now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
t=(mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)


hours = (now.hour)
x = datetime.datetime.now()
g= datetime.datetime(2023, 12, 15, 0, 0 )

if (x.strftime("%x"))>(g.strftime("%x")):
 print('\033[1;32m تم ايقاف الاداه راسل المطور نـــمـــࢪود لتفعيل ')
 time.sleep(1)
 print('\033[1;31m المطورالمبࢪمج:- @M_T_F    ')
 time.sleep(1)
 print('\033[1;32m  🔱 نمــࢪود 🔱')
 time.sleep(1)
 print('\033[1;31m 1')
 time.sleep(1)
 print('\033[1;32m 2')
 time.sleep(1)
 print('\033[1;31m 3')
 time.sleep(1)
 print('\033[1;32m 4')
 time.sleep(1)
 print('\033[1;31m 5')
 time.sleep(1)
 print('\033[1;32m 6')
 time.sleep(1)
 print('\033[1;31m 7')
 time.sleep(1)
 print('\033[1;32m 8')
 time.sleep(1)
 print('\033[1;31m 9')
 time.sleep(1)
 print('\033[1;32m@M_T_F')
 

 open(".token.txt", "w").write(' . . . .')
 print(x)
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
import threading
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
import webbrowser
webbrowser.open('https://t.me/py_1hon1')
from rich.text import Text as tekz
import os


Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
print('\n')
print('\033[1;36m')
import os
try:

	import requests
except ImportError:
    Z = '''[1;31m'''
R = '''[1;31m'''
X = '''[1;33m'''
F = '''[2;32m'''
C = '''[1;97m'''
B = '''[2;36m'''
Y = '''[1;34m'''
E = '''[1;31m'''
B = '''[2;36m'''
G = '''[1;32m'''
S = '''[1;33m'''
ses = requests.Session()
F = '''[2;32m'''
Z = '''[1;31m'''
L = '''[1;95m'''
E = '''[1;31m'''
G = '''[1;32m'''
S = '''[1;33m'''
Z = '''[1;31m'''
X = '''[1;33m'''
Z1 = '''[2;31m'''
F = '''[2;32m'''
A = '''[2;39m'''
C = '''[2;35m'''
B = '''[2;36m'''
Y = '''[1;34m'''
xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#نـــمـــࢪودي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1='\x1b[38;5;161m'#وردي جميل جدا
time1 = time.localtime()
time2 = time.strftime('''%d/%m/%Y''')
print(SDMi) 
time3 = time.strftime('''%H:%M:%S''')
print('')
print(f''' \x1b[1;93m  ༺ \x1b[1;38;5;121m  𝑆𝐷𝑀 𝐕𝐈𝐏 \x1b[1;93m ༻  ''')
print(f'''{C}: \x1b[38;5;92m 𝐓𝐇𝐄 𝐃𝐀𝐓𝐄 \x1b[1;38;5;121m ๛   \x1b[1;38;5;121m   𖣎 \x1b[1;96m{time2} \x1b[1;38;5;121m 𖣎''')
print('')
print(f'''{C}: \x1b[38;5;92m 𝑇𝐻𝐸 𝑇𝐼𝑀𝐸 \x1b[1;38;5;121m ๛   \x1b[1;38;5;121m   𖣎 \x1b[1;96m{time3} \x1b[1;38;5;121m 𖣎''')
print('')
token=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  \x1b[38;5;180m𝐓𝐎𝐊𝐄𝐍  \x1b[1;38;5;121m ๛   \x1b[38;5;117m')
print()
ID=input('  \x1b[38;5;117m{\x1b[1;32m•\x1b[38;5;117m}  𝐈𝐃 \x1b[1;38;5;121m ๛  \x1b[38;5;117m︎')
