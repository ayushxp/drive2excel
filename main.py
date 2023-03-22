import os
from google.oauth2 import service_account
from getfilelistpy import getfilelist

SCOPES = ['https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = 'client_secret.json'
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

resource = {
    "service_account": credentials,
    "id": "1YPfzAI3NVF30RmnAmL1c45mbBogfYp6k",
    "fields": "files(name,id)",
}
res = getfilelist.GetFileList(resource)
print(res)
#print(type(res))
all_keys = list(res.values())
all2=list(all_keys[1].values())
kost=list(all2[1])
print(kost)
dost=[]
for i in kost[1:]:
    dost.append(i)
print(dost)
import pandas as pd
df = pd.DataFrame(dost)
ui=list(all_keys[2])
print(ui)
kist=[]
k=1
for i in ui[1:]:
    i = ui[k]
    x1 = list(i.values())[0]
    kist.append(x1)
    k+=1

print(kist)

pot=[]
for i in kist:
    res1 = [sub['id'] for sub in i]
    #print(res)
    pot.append(res1)
print(pot)
for i in range(len(pot)):
    for j in range(len(pot[i])):
        str = pot[i][j]
        new_str = "https://drive.google.com/file/d/{}/view?usp=sharing".format(str)
        pot[i][j] = new_str
print(pot)
df2 = pd.DataFrame(pot)
result = pd.concat([df,df2], axis = 1)
#print(result)
pd.DataFrame(result).to_csv("C:/Users/Inno/Desktop/output.csv",index=False,mode='a',header=False)
os.system("C:/Users/Inno/Desktop/output.csv")
