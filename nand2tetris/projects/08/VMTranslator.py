def commandType(cmd1):
  if "push" in cmd1:
    return "C_PUSH"
  elif "pop" in cmd1:
    return "C_POP"
  elif 'label' in cmd1:
    return 'C_LABEL'
  elif 'if' in cmd1:
    return 'C_IF'
  elif 'goto' in cmd1:
    return 'C_GOTO'
  elif 'function' in cmd1:
    return 'C_FUNCTION'
  elif 'call' in cmd1:
    return 'C_CALL'
  elif 'return' in cmd1:
    return 'C_RETURN'
  elif "add" or "sub" or 'neg' or 'eq' or 'gt' or 'lt' or 'and' or 'or' or 'not' in cmd1:
    return "C_ARITHMETIC"

def getarg0(cmdarg0):

  arg0r = cmdarg0.split(' ')
  if len(arg0r) > 0:
    return arg0r[0]

def getarg1(cmdarg1):

  arg1r = cmdarg1.split(' ')
  if len(arg1r) > 1:
    return arg1r[1]

def getarg2(cmdarg2):

  arg2r = cmdarg2.split(' ')
  if len(arg2r) > 2:

    return int(arg2r[2])

    # open the file and remove white space and comments

def printarray(array1):
  for i in array1:
    output.write(i)
    output.write('\n')
  return

def pushASM():
  pushASMarray= ["@SP",'A=M','M=D','@SP','M=M+1']
  printarray(pushASMarray)

  return

def addASM():
  addASMarray= ["@SP",'M=M-1','A=M-1','D=M','@SP','A=M','D=D+M','@SP','A=M-1','M=D']
  printarray(addASMarray)

  return

def subASM():
  subASMarray= ["@SP",'M=M-1','A=M-1','D=M','@SP','A=M','D=D-M','@SP','A=M-1','M=D']
  printarray(subASMarray)

  return

def negASM():
  negASMarray= ["@SP",'A=M-1','D=-M','@SP','A=M-1','M=D']
  printarray(negASMarray)

  return

def eqASM(i):
  eqASMarray= [
  "@SP",
  'M=M-1',
  "@SP",
  'A=M-1',
  'D=M',
  '@SP',
  'A=M',
  'D=D-M',
  '@TRUE'+str(i),
  'D;JEQ',
  '@SP',
  'A=M-1',
  'M=0',
  '@END'+str(i),
  '0;JMP',
  '(TRUE'+str(i)+')',
  '@SP',
  'A=M-1',
  'M=-1',
  '(END'+str(i)+')'
  ]
  printarray(eqASMarray)

  return

def gtASM(i):
  gtASMarray= [
  "@SP",
  'M=M-1',
  "@SP",
  'A=M-1',
  'D=M',
  '@SP',
  'A=M',
  'D=D-M',
  '@TRUE'+str(i),
  'D;JGT',
  '@SP',
  'A=M-1',
  'M=0',
  '@END'+str(i),
  '0;JMP',
  '(TRUE'+str(i)+')',
  '@SP',
  'A=M-1',
  'M=-1',
  '(END'+str(i)+')'
  ]
  printarray(gtASMarray)

  return

def ltASM(i):
  ltASMarray= [
  "@SP",
  'M=M-1',
  "@SP",
  'A=M-1',
  'D=M',
  '@SP',
  'A=M',
  'D=D-M',
  '@TRUE'+str(i),
  'D;JLT',
  '@SP',
  'A=M-1',
  'M=0',
  '@END'+str(i),
  '0;JMP',
  '(TRUE'+str(i)+')',
  '@SP',
  'A=M-1',
  'M=-1',
  '(END'+str(i)+')'
  ]
  printarray(ltASMarray)

  return

def andASM():
  andASMarray= [
  "@SP",
  'M=M-1',
  "@SP",
  'A=M-1',
  'D=M',
  '@SP',
  'A=M',
  'D=D&M',
  '@SP',
  'A=M-1',
  'M=D'
  ]
  printarray(andASMarray)

  return

def orASM():
  orASMarray= [
  "@SP",
  'M=M-1',
  "@SP",
  'A=M-1',
  'D=M',
  '@SP',
  'A=M',
  'D=D|M',
  '@SP',
  'A=M-1',
  'M=D'
  ]
  printarray(orASMarray)

  return

def notASM():
  notASMarray= [
  "@SP",
  'A=M-1',
  'D=M',
  'D=!D',
  '@SP',
  'A=M-1',
  'M=D'
  ]
  printarray(notASMarray)

  return

# get the item to push to stack
def pushitem(s,name):
  arg1 = getarg1(s)
  arg2 = getarg2(s)
  if arg1 == 'constant':
    output.write('@'+str(arg2))
    output.write('\nD=A\n')
  elif arg1 == 'argument':
    argumentarray = [
      '@'+str(arg2),
      'D=A',
      '@ARG',
      'A=M+D',
      'D=M'
      ]
    printarray(argumentarray)
  elif arg1 == 'local':
    localarray = [
      '@'+str(arg2),
      'D=A',
      '@LCL',
      'A=M+D',
      'D=M'
      ]
    printarray(localarray)
  elif arg1 == 'this':
    thisarray = [
      '@'+str(arg2),
      'D=A',
      '@THIS',
      'A=M+D',
      'D=M'
      ]
    printarray(thisarray)
  elif arg1 == 'that':
    thatarray = [
      '@'+str(arg2),
      'D=A',
      '@THAT',
      'A=M+D',
      'D=M'
      ]
    printarray(thatarray)
  elif arg1 == 'static':
    staticarray = [
      '@'+name+'.'+str(arg2),
      'D=M'
      ]
    printarray(staticarray)
  elif arg1 == 'pointer':
    pointerarray = [
      '@'+str(arg2),
      'D=A',
      '@THIS',
      'A=A+D',
      'D=M'
      ]
    printarray(pointerarray)
  elif arg1 == 'temp':
    temparray = [
      '@'+str(arg2),
      'D=A',
      '@5',
      'A=A+D',
      'D=M'
      ]
    printarray(temparray)


  return

def popASM(s,name):

  arg1 = getarg1(s)
  arg2 = getarg2(s)

  if arg1 != 'static':
    popASMarray= ["@SP",'A=M-1','D=M','@R15','M=D','@'+str(arg2),'D=A']
    printarray(popASMarray)


  if arg1 == 'constant':
    output.write('@'+str(arg2))
    output.write('\nM=D\n')
  elif arg1 == 'argument':
    argumentarray = ['@ARG']
    printarray(argumentarray)
  elif arg1 == 'local':
    localarray = ['@LCL']
    printarray(localarray)
  elif arg1 == 'this':
    thisarray = ['@THIS']
    printarray(thisarray)
  elif arg1 == 'that':
    thatarray = ['@THAT']
    printarray(thatarray)
  elif arg1 == 'static':
    staticarray = ["@SP",'A=M-1','D=M',
      '@'+name+'.'+str(arg2),'M=D'
      ]
    printarray(staticarray)
  elif arg1 == 'pointer':
    pointerarray = [
      '@THIS',
      'D=A+D'
      ]
    printarray(pointerarray)
  elif arg1 == 'temp':
    temparray = [
      '@5',
      'D=A+D'
      ]
    printarray(temparray)

  popASMarrayend= [
      'D=M+D',
      '@R14',
      'M=D',
      '@R15',
      'D=M',
      '@R14',
      'A=M',
      'M=D',
      '@SP',
      'M=M-1'
      ]


  if arg1 == 'pointer' or arg1 =='temp':

    printarray(['@R14','M=D','@R15','D=M','@R14','A=M','M=D','@SP','M=M-1'])
  elif arg1 == 'static':
    printarray(['@SP','M=M-1'])
  else:
    printarray(popASMarrayend)
  return


def writeInit():
  Initarray = [
      '@256',
      'D=A',
      '@SP',
      'M=D'

      ]
  printarray(Initarray)
  writeCall('Sys.init',0,0)
  return

def writeLabel(currentFunction,label):
  labelarray = [
      '('+str(currentFunction)+'$'+str(label)+')'
      ]
  printarray(labelarray)
  return

def writeLabelF(label):
  labelarray = [
      '('+str(label)+')'
      ]
  printarray(labelarray)
  return

def writeGoto(currentFunction,label):
  Gotoarray = [
      '@'+str(currentFunction)+'$'+str(label),
      '0;JMP'
      ]
  printarray(Gotoarray)
  return

def writeGotoF(label):
  Gotoarray = [
      '@'+str(label),
      '0;JMP'
      ]
  printarray(Gotoarray)
  return

def writeIf(currentFunction,label):
  Ifarray = [
      '@SP',
      'M=M-1',
      '@SP',
      'A=M',
      'D=M',
      '@'+str(currentFunction)+'$'+str(label),
      'D;JNE'
      ]
  printarray(Ifarray)
  return

def writeIfF(label):
  Ifarray = [
      '@SP',
      'M=M-1',
      '@SP',
      'A=M',
      'D=M',
      '@'+str(label),
      'D;JNE'
      ]
  printarray(Ifarray)
  return

def writeCall(functionName,numArgs,i):


  printarray(['@'+'return-address'+str(i),'D=A',"@SP",'A=M','M=D','@SP','M=M+1'])
  pushM('LCL')
  pushM('ARG')
  pushM('THIS')
  pushM('THAT')
  callarray = [
      '@SP',
      'D=M',
      '@5',
      'D=D-A',
      '@'+str(numArgs),
      'D=D-A',
      '@ARG',
      'M=D',
      '@SP',
      'D=M',
      '@LCL',
      'M=D'
      ]
  printarray(callarray)
  writeGotoF(functionName)
  writeLabelF('return-address'+str(i))

  return

def writeReturn():
  # R13 is FRAME
  # R14 is RET
  returnarray = [
      '@LCL',
      'D=M',
      '@R13',
      'M=D',
      '@5',
      'A=D-A',
      'D=M',
      '@R14',
      'M=D',

      "@SP",'A=M-1','D=M','@ARG','A=M','M=D',
      '@SP',
      'M=M-1',

      '@ARG',
      'D=M+1',
      '@SP',
      'M=D',

      '@R13',
      'A=M-1',
      'D=M',
      '@THAT',
      'M=D',

      '@R13',
      'A=M-1',
      'A=A-1',
      'D=M',
      '@THIS',
      'M=D',

      '@R13',
      'A=M-1',
      'A=A-1',
      'A=A-1',
      'D=M',
      '@ARG',
      'M=D',

      '@R13',
      'A=M-1',
      'A=A-1',
      'A=A-1',
      'A=A-1',
      'D=M',
      '@LCL',
      'M=D',

      '@14',
      'A=M',
      '0;JMP'

      ]
  printarray(returnarray)

  return

def writeFunction(functionName,numLocals):
  writeLabelF(functionName)
  i=0
  while i < numLocals:
    printarray(['@0','D=A',"@SP",'A=M','M=D','@SP','M=M+1'])
    i+=1

  return

def pushM(item):
  pushMASMarray= ['@'+str(item),'D=M',"@SP",'A=M','M=D','@SP','M=M+1']
  printarray(pushMASMarray)

  return

import sys
import os
import glob
from pathlib import Path
directoryName = sys.argv[1]
#print(directoryName)
#os.chdir(Path(directoryName).resolve())


daRealpath = str(Path(sys.argv[1]).resolve())
#print(os.path.normpath(daRealpath))
#print(os.path.dirname(Path(sys.argv[1]).resolve()))
#daRealpath = str(daRealpath.rpartition("/")[0])
#print(daRealpath)
#os.chdir(daRealpath) # changes the directory to the StaticsTest folder
# if the input ends with .vm then the input is a file. So change the directory to the directory of that file
InitVM = False
if(sys.argv[1].endswith(".vm")):
    #print("run for your life")
    #print(os.path.dirname(Path(sys.argv[1]).resolve()))
    daRealpath = str(daRealpath.rpartition("/")[0])
    #print(daRealpath)
    os.chdir(daRealpath)
else:
    # if the input is a directory, then we change to that directory
    os.chdir(os.path.realpath(directoryName))
    InitVM = True
ASMFileName = str(os.getcwd())
#print(os.getcwd())
#print(os.getcwd())
ASMFileName = ASMFileName.rpartition("/")[2]

items = os.listdir(".") # gets all of the files in the directory

items = os.listdir(".") # gets all of the files in the directory
onlyVM = []
for item in items:
    if(item.endswith(".vm")):
        onlyVM.append(item)



#output = open('StaticsTest.asm','w')
output = open(ASMFileName+ ".asm",'w')

if(InitVM):
    currentFunction1 = 'Sys.init'
    writeInit()

#for filename in glob.glob('*.vm'):
for filename in onlyVM:

  content = []
  #print(filename)
  with open(filename) as f:
      for line in f:
          line = line.split('//', 1)[0]
          line = line.rstrip()
          content.append(line)

  content = [x.strip() for x in content]
  content[:] = [item for item in content if item != '']

  print(content)

  #1st pass
  n=2
  currentFunction1 = 'main'

  for command in content:
    arg0 = getarg0(command)
    arg1 = getarg1(command)
    arg2 = getarg2(command)
    #print(commandType(command))
    #print(command)
    #print(arg0)
    #print(arg1)
    #print(arg2)
    #print(arg1find(command))
    #print(arg2find(command))

    # push assembly
    if commandType(command) == 'C_PUSH':
      # get arg to push onto stack

      pushitem(command,filename[:filename.index('.')])

      pushASM()

    elif commandType(command) == 'C_ARITHMETIC':
      if 'add' in command:
        addASM()
      elif 'sub' in command:
        subASM()
      elif 'neg' in command:
        negASM()
      elif 'eq' in command:
        eqASM(n)
        n+=1
      elif 'gt' in command:
        gtASM(n)
        n+=1
      elif 'lt' in command:
        ltASM(n)
        n+=1
      elif 'and' in command:
        andASM()
      elif 'or' in command:
        orASM()
      elif 'not' in command:
        notASM()
    elif commandType(command) == 'C_POP':
      popASM(command,filename[:filename.index('.')])
    elif commandType(command) == 'C_GOTO':
      writeGoto(currentFunction1,arg1)
    elif commandType(command) == 'C_IF':
      writeIf(currentFunction1,arg1)
    elif commandType(command) == 'C_RETURN':
      writeReturn()
    elif commandType(command) == 'C_CALL':
      writeCall(arg1,arg2,n)
      n+=1
    elif commandType(command) == 'C_FUNCTION':
      currentFunction1 = arg1
      writeFunction(arg1,arg2)
    elif commandType(command) == 'C_LABEL':
      writeLabel(currentFunction1,arg1)
      #print(arg1)
  #print(filename[:filename.index('.')])



output.close()
