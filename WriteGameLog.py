import unreal
import sys


file = open(r"D:\Codigos\unreal\ScriptingPython\ScriptingPython\ScriptingPython_Log.txt", "a+")

file.write(sys.argv[1])

file.close()