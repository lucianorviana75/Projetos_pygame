#define MyAppName "Nucleo"
#define MyAppVersion "1.0"
#define MyAppExeName "jogo_main_nucleo.exe"

[Setup]
AppId={{E9C4772B-A105-433C-88DD-AE93FB747CA8}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppName}
OutputBaseFilename=Nucleo_Setup
WizardStyle=modern
Compression=lzma
SolidCompression=yes

[Languages]
Name: "portuguese"; MessagesFile: "compiler:Languages\Portuguese.isl"

[Files]
Source: "dist\jogo_main_nucleo.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\jogo_main_nucleo.exe"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\jogo_main_nucleo.exe"

[Run]
Filename: "{app}\jogo_main_nucleo.exe"; Description: "Executar Nucleo"; Flags: nowait postinstall skipifsilent