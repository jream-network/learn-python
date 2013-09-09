import os

#print os.environ
print os.getcwd()
os.chdir('../')
print os.getcwd()
#os.chdir('c:\\temp')
#print os.getcwd()

print os.getenv('OS')
 mydir = os.listdir('.')
 for i in mydir:
     print i

#os.rmdir('FAKE')
#os.chdir('../')
#os.rmdir('FAKE')
#os.mkdir('FAKE')

#os.mkdir('CAT')
#os.renames('CAT', 'PIG')
