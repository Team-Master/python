Set WinScriptHost = CreateObject( "WScript.shell" )

command = "C:\Users\user00\git\python\python\screenshot.cmd"
WinScriptHost.Run Chr(34) & command & Chr(34), 0

Set WinScriptHost = Nothing
