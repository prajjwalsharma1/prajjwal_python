from app_data import *
# class
data={

"hello":1

}
g=open('app_data.py','r')
print(g.appdata['key'])
a=int(input("enter number u want to inser :"))
appdata['key']=a+appdata['key']
data['hello']=appdata['key']




print(data)