import dropbox
import sys
import os


dbx = dropbox.Dropbox('5k8-6xgDxjAAAAAAAAAAEk5nkljypyCTfXQ7jXfFnL49NhrDZp3_NCE_GFXGoTBz')

print(dbx.users_get_current_account())

for entry in dbx.files_list_folder('').entries:
    print(entry.name)

print ("Attempting to upload...")

with open('hello.txt', 'rb') as f:
    dbx.files_upload(f.read(),'/test/hello.txt',mute=True)

   # dbx.files_delete('/test/hello.txt')
 