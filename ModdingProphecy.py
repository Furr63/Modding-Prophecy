import hashlib
import time #pretty crazy thing to import
from termcolor import colored, cprint #colors are pretty
import os #no comments
import shutil
# VARIABLES (duh!)

##SETTINGS
SleepMultiplier = 0.1 #Delay time uhh how do i explain
AssemblyCsharpLocation = "C:\Program Files (x86)\Steam\steamapps\common\Cats are Liquid - A Better Place\CaL-ABP-Windows_Data\Managed"

##DO NOT CHANGE IF YOU KNOW WHAT'S GOOD FOR YOU
CurrentFolder = os.getcwd()
PureFolder = os.path.join(CurrentFolder,"Pure")
ModsFolder = os.path.join(CurrentFolder,"Mods")
PureAssembly = os.path.join(PureFolder,"Assembly-CSharp.dll")
AssemblyCsharp = "not yet known lol"
ModActive = 0

# DEFINING FUNCTIONS
def getAssemblyCsharp(path):
    global AssemblyCsharp
    AssemblyPath = os.path.join(path,"Assembly-Csharp.dll")
    print("*trying to find Assembly-CSharp.dll")
    time.sleep(0.5 * SleepMultiplier)
    try:
        print("*checking if \"" + AssemblyPath + "\" leads to Assembly-Csharp.dll")
        time.sleep(0.5 * SleepMultiplier)
        AssemblyCsharp = open(AssemblyPath, "rb")
        print('*File found!')
        time.sleep(1 * SleepMultiplier)
    except FileNotFoundError:
        try:
            print("*\""+AssemblyPath+"\" doesn't leads to Assembly-Csharp.dll")
            time.sleep(0.5 * SleepMultiplier)
            print("*checking if \""+path+"\" leads to Assembly-Csharp.dll")
            time.sleep(0.5 * SleepMultiplier)
            AssemblyCsharp = open(path, "rb")
        except FileNotFoundError:
            cprint('*ERROR File not found', 'red')
            time.sleep(0.5 * SleepMultiplier)
            print('*Your copy of Cats are Liquid - ABP seems to not be installed in the default folder')
            time.sleep(1 * SleepMultiplier)
            print('*please paste the path to the folder which contains Assembly-Csharp.dll')
            nextPath = input("")
            getAssemblyCsharp(nextPath)

def checkAvaliableMods():
    print("i gotta code this later")
    

def createBackup(pure):
    Time = time.gmtime()
    CurrentTime = str(Time[1]) + "-" + str(Time[2]) + "-" + str(Time[0]) + " " + str(Time[5]) + "h " + str(Time[4]) + "m " + str(Time[3]) + "s.dll" # current time as MM-DD-YYYY H M S
    if pure == 1:
        print("creating mod backup...")
        time.sleep(0.5 * SleepMultiplier)
        shutil.copyfile(AssemblyCsharp.name,os.path.join("Mods",CurrentTime) )
        print("BACKUP SUCCESSFUL, FILE CALLED \"" + CurrentTime + "\"")
        time.sleep(0.5 * SleepMultiplier)
    if pure == 0:
        print("creating backup...")
        time.sleep(0.5 * SleepMultiplier)
        shutil.copyfile(AssemblyCsharp.name,os.path.join("Pure","Assembly-CSharp.dll") )
        print("BACKUP SUCCESSFUL")
        time.sleep(0.5 * SleepMultiplier)

def createImpureBackup():
    print('death')
# START

cprint("MODDING PROPHECY v1.0.0", (100,0,255))
time.sleep(2 * SleepMultiplier)
getAssemblyCsharp(AssemblyCsharpLocation)

if hashlib.file_digest(AssemblyCsharp,'sha256') != '7484fb5e1e76e3761bafcdb5067e1bc04a336bda4ffe0e1f5ee13753e91a615c':
    print('*MODDED Assembly-CSharp.dll DETECTED')
    ModActive = 1
else:
    print('*VANILLA Assembly-CSharp.dll DETECTED')
    ModActive = 0
time.sleep(2 * SleepMultiplier)

print("*checking for unmodded Assembly-Csharp.dll at: " + os.path.join(PureFolder,"Assembly-CSharp.dll"))
time.sleep(0.5 * SleepMultiplier)
if os.access(os.path.join(PureFolder,"Assembly-CSharp.dll") , os.W_OK):
    print("*Backup detected!")
else:
    print("*NO BACKUP DETECTED")
    cprint("*REMOVING MODS WILL NEED TO BE DONE MANUALLY BY CHECKING FILE INTEGRITY TROUGH STEAM","red")
    time.sleep(3 * SleepMultiplier)

print("BACKUP CURRENT Assembly-CSharp.dll?")
time.sleep(0.5 * SleepMultiplier)
print("Y = YES (recommended)")
print("N = NO")
while(1==1):
    permission = input()
    match (permission.upper()):
        case "YES" | "Y" | "TRY" | "ATTEMPT":
            print("BACKUP WILL BE ATTEMPTED")
            createBackup(ModActive)
            break
        case "NO" | "N" | "DONT" | "DO NOT" | "FALSE" | "DON'T" | "NUH UH" |"YUH UH":
            print("BACKUP WON'T BE ATTEMPTED")
            break
        case _:
            print("COULDN'T UNDERSTAND, TRY AGAIN")

checkAvaliableMods()