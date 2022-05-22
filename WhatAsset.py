import unreal

#1 unreal classes
@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedAssets = MyEditorUtility().get_selected_assets()#pega nas classes unreal e na adicionada global o get selected assets que nada mais é que capturar os assets selecionados

for asset in selectedAssets:
    unreal.log(asset.get_full_name())#mostrando seu nome e sua pasta
    unreal.log(asset.get_fname())#mostrando seu nome na forma FName
    unreal.log(asset.get_name())#mostra seu nome em str
    unreal.log(asset.get_path_name())#nome na pasta
    unreal.log(asset.get_class())#mostra a classe
    unreal.log_warning("*"*50)


