import sys


FIN=""
FOUT=""
COL=""
DIR=""
nargs=len(sys.argv)
skip=False
for i in range(1,nargs):
   if not skip:
      arg=sys.argv[i]
      print "INFO: processing",arg
      if arg == "--fin":
         if i != nargs-1:
            FIN=sys.argv[i+1]
            skip=True
      elif arg == "--fout":
         if i != nargs-1:
            FOUT=sys.argv[i+1]
            skip=True
      elif arg == "--col":
         if i != nargs-1:
            COL=sys.argv[i+1]
            skip=True
      elif arg == "--dir":
         if i != nargs-1:
            DIR=sys.argv[i+1]
            skip=True
      else:
         print "ERR: unknown arg:",arg
   else:
      skip=False

print "INFO: FIN",FIN
print "INFO: FOUT",FOUT
#1,1,2,3,5,8

try:
    f= open(FIN, 'r')
    lines = f.readlines()
    for line in lines:
        print line.split('\n')[0]
    f.close()
    try:
        g = open('dataout', 'w')
        g.write('This is content\n')
        g.write('This is more content\n')
    except:
        print 'ERR: cannot write to file "dataout"'

except:
    print 'ERR: file DO NOT EXIST.'
