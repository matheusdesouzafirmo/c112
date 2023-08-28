import os
import shutil


from_dir='c:/Users/legal/Downloads'
to_dir='c:/Users/legal/desktop/novasdocumentos'

list_of_files=os.listdir(from_dir)
#print(list_of_files)

#mover imagem de dowlond para outras pastas
for file_name in list_of_files:

     name,extension = os.path.splitext(file_name)
     print(name)
     print(extension)

     if extension == '':
        continue
     if extension in ['.txt', '.doc', '.docx','.pdf']:
        path1 = from_dir + '/'+file_name
        path2 = to_dir + '/'+'documents_files'
        path3 = to_dir + '/'+'documents_files'+'/'+file_name
        print('path1 ',path1)
        print('path3 ',path3)
        
        if os.path.exists(path2):
            print('movendo '+ file_name +'...')

            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('movendo '+ file_name +'...')
            shutil.move(path1,path3)

