def commandType(cmd1):
  if "push" in cmd1:
    return "C_PUSH"
  elif "pop" in cmd1:
    return "C_POP"
  elif "add" or "sub" or 'neg' or 'eq' or 'gt' or 'lt' or 'and' or 'or' or 'not' in cmd1:
    return "C_ARITHMETIC"
  elif 'label' in cmd1:
    return 'C_LABEL'
  elif 'goto' in cmd1:
    return 'C_GOTO'
  elif 'if' in cmd1:
    return 'C_IF'
  elif 'function' in cmd1:
    return 'C_FUNCTION'
  elif 'call' in cmd1:
    return 'C_CALL'
  elif 'return' in cmd1:
    return 'C_RETURN'

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



import sys
import os
import glob

from pathlib import Path 

directoryName = sys.argv[1]

daRealpath = str(Path(sys.argv[1]).resolve())

# if the input ends with .vm then the input is a file. So change the directory to the directory of that file
if(sys.argv[1].endswith(".vm")):
    daRealpath = str(daRealpath.rpartition("/")[0])
    os.chdir(daRealpath)

    ASMFileName = sys.argv[1].split("/")[-1]
    ASMFileName = ASMFileName.split(".vm")[0]
    #print(ASMFileName)
else:
    # if the input is a directory, then we change to that directory
    os.chdir(os.path.realpath(directoryName))
    # now that the cwd is correct, we get the filename
    ASMFileName = str(os.getcwd())
    ASMFileName = ASMFileName.rpartition("/")[2]

items = os.listdir(".") # gets all of the files in the directory
#print(items)
onlyVM = []
for item in items:
    if(item.endswith(".vm")):
        onlyVM.append(item)

output = open(ASMFileName+ ".asm",'w')

# this will get all the number of files we are working with, then open each one individually
for fileName in onlyVM:
    # only open .vm files
        daRealFilename = fileName
        #print(p)
        with open(fileName) as file:
            content = []
            for line in file:
                line = line.split('//', 1)[0]
                line = line.rstrip()
                content.append(line)

            content = [x.strip() for x in content]
            content[:] = [item for item in content if item != '']

            #print(content)
            filename = daRealFilename

            #1st pass
            n=0
            for command in content:

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


            #print(filename[:filename.index('.')])
output.close()