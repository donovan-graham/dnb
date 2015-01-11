from os import listdir
from os.path import isfile, join


# mypath = "."
# onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

# print onlyfiles
# print onlyfiles[0]
# print onlyfiles[1]


cnt = 1

for filename in listdir("."):
  if isfile(filename) and filename[-4:] == ".jpg":
    print '<img class="img" id="img_' + filename[:-4] + '" src="./img/med/' + filename + '" />'
    # os.rename(filename, filename[7:])



# for f in onlyfiles:
#   print f