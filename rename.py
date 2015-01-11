from os import listdir
from os.path import isfile, join

path = "./img/med"

for filename in listdir(path):
  if isfile(join(path,filename)) and filename[-4:] == ".jpg":
    print '<a class="img" rel="dnb_wedding_2014" href="./img/med/' + filename + '"><img src="./img/low/' + filename + '" alt=""/></a>'
    # os.rename(filename, filename[7:])


      


# for f in onlyfiles:
#   print f