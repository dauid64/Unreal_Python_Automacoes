import unreal

info = dir(unreal)
for i in info:#imprimindo todos os unreal modulos
    unreal.log("unreal." + str(i))#unreal. é uma struct
