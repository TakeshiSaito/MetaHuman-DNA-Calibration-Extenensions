$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition

$mayapy2022 = "C:\Program Files\Autodesk\Maya2022\bin\mayapy.exe"
$mayapy2023 = "C:\Program Files\Autodesk\Maya2023\bin\mayapy.exe"

$env:PYTHONPATH = "$scriptPath\scripts"

# unittestを実行するディレクトリに移動し、mayapyでunittestを実行
cd $scriptPath\tests
& $mayapy2022 -m unittest discover -s . -p "test_*.py"
& $mayapy2023 -m unittest discover -s . -p "test_*.py"

