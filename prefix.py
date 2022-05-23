import unreal

#/Game/Mannequin/Animations/ThirdPersonJump_End.ThirdPersonJump_End
#/Game/Mannequin/Animations/anim_ThirdPersonJump_End.anim_ThirdPersonJump_End

prefixAnimationBlueprint    = "animBP"
prefixAnimationSequence     = "anim"
prefixAnimation             = "anim"
prefixBlendSpace            = "animBlnd"
prefixBlueprint             = "bp"
prefixCurveFloat            = "crvF"
prefixCurveLinearColor      = "crvL"
prefixLevel                 = "lvl"
prefixMaterial              = "mat"
prefixMaterialFunction      = "mat_func"
prefixMaterialInstance      = "mat_inst"
prefixParticleSystem        = "fx"
prefixPhysicsAsset          = "phsx"
prefixSkeletalMesh          = "sk"
prefixSkeleton              = "skln"
prefixSoundCue              = "cue"
prefixSoundWave             = "wv"
prefixStaticMesh            = "sm"
prefixTexture2D             = "tex"
prefixTextureCube           = "HDRI"

workingPath = "/Game/"

@unreal.uclass()
class MyEditorAssetLIbrary(unreal.EditorAssetLibrary):
    pass

def GetProperPrefix(className):
    _prefix = ""
    if className == "AnimBlueprint":
        _prefix = prefixAnimationBlueprint
    elif className == "AnimSequence":
        _prefix = prefixAnimationSequence
    elif className == "Animation":
        _prefix = prefixAnimation
    elif className == "BlendSpace1D":
        _prefix = prefixBlendSpace
    elif className == "Blueprint":
        _prefix = prefixBlueprint
    elif className == "CurveFloat":
        _prefix = prefixCurveFloat
    elif className == "CurveLinearColor":
        _prefix = prefixCurveLinearColor
    elif className == "Material":
        _prefix = prefixMaterial
    elif className == "MaterialFunction":
        _prefix = prefixMaterialFunction
    elif className == "MaterialInstance":
        _prefix = prefixMaterialInstance
    elif className == "ParticleSystem":
        _prefix = prefixParticleSystem
    elif className == "PhysicsAsset":
        _prefix = prefixPhysicsAsset
    elif className == "SkeletalMesh":
        _prefix = prefixSkeletalMesh
    elif className == "Skeleton":
        _prefix = prefixSkeleton
    elif className == "SoundCue":
        _prefix = prefixSoundCue
    elif className == "SoundWave":
        _prefix = prefixSoundWave
    elif className == "StaticMesh":
        _prefix = prefixStaticMesh
    elif className == "Texture2D":
        _prefix = prefixTexture2D
    elif className == "TextureCube":
        _prefix = prefixTextureCube
    else:
        _prefix = ""
    return  _prefix

editorAssetLib = MyEditorAssetLIbrary()

allAssets = editorAssetLib.list_assets(workingPath, True, False)
allAssetsCount = len(allAssets)

selectedAssetPath = workingPath

with unreal.ScopedSlowTask(allAssetsCount, selectedAssetPath) as ST:
    ST.make_dialog(True)

    for asset in allAssets:
        _assetData = editorAssetLib.find_asset_data(asset)
        _assetName = _assetData.get_asset().get_name()
        _assetPathName = _assetData.get_asset().get_path_name()
        _assetPathOnly = _assetPathName.replace((_assetName + "." + _assetName), "")
        _assetClassName = _assetData.get_asset().get_class().get_name()
        _assetPrefix = GetProperPrefix(_assetClassName)

        if _assetPrefix in _assetName:
            continue
        elif _assetPrefix == "":
            continue
        else:
            _targetPathName = _assetPathOnly + ("%s%s%s%s%s%s%s" % (_assetPrefix, "_", _assetName, ".", _assetPrefix, "_", _assetName))

            editorAssetLib.rename_asset(_assetPathName, _targetPathName)
            unreal.log(">>>>>> Renaming [%s] to [%s]" %(_assetPathName, _targetPathName))

        if ST.should_cancel():
            break
        ST.enter_progress_frame(1, asset)
