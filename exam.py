import uuid
app_data={'fidler':True}
print(app_data)
app_data['android_uuid']=str(uuid.uuid4())
print(app_data)