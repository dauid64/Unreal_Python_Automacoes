import unreal

@unreal.uclass()
class MyEditorUtility(unreal.GlobalEditorUtilityBase):
    pass

selectedActors = MyEditorUtility().get_selection_set()#actors selecionados

for actor in selectedActors:
    unreal.log(actor.get_name())  # mostra seu nome em str
    if actor.actor_has_tag("tagOne"):#se a tag do actor tiver esse nome printa
        unreal.log("[1]")
    if actor.actor_has_tag("tagTwo"):#se a tag do actor tiver esse nome printa
        unreal.log("[2]")
    if actor.actor_has_tag("tagThree"):  # se a tag do actor tiver esse nome printa
        unreal.log("[3]")
    unreal.log_warning("*" * 50)