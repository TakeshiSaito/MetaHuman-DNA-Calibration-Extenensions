$rootDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
cd $rootDir

$env:MAYA_MODULE_PATH = "$rootDir"

Start-Process -FilePath "C:\Program Files\Autodesk\Maya2022\bin\maya.exe"