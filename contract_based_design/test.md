# Deploy new Add-In to Enterprise Architekt

3. **Erzeugen einer Registrierungsdatei für die AddIns dll-Datei**
   - 🔧 Benötigt wird:
     -  fertig kompilierte .dll-Datei vom Add-In (z. B. MulticToolingIndustrial.dll)
     -  Den Pfad zum .dll-File
     -  Einen gewünschten Speicherort für die .reg-Datei, z. B. auf dem Desktop
    
   - 🔍 Anleitung:
     - Angenommen, das Add-In wurde bereits kompiliert und die DLL liegt unter: ```C:\Projects\MULTIC\bin\Release\MULTIC.Tooling.Industrial.dll```
     - Und die Registry-Datei soll auf dem Desktop als Addin.reg gespeichert werden. Der Befehl sieht so aus: ```C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe "C:\Projects\MULTIC\bin\Release\MULTIC.Tooling.Industrial.dll" /codebase /regfile:"C:\Users\<YOUR-NAME>\Desktop\Addin.reg"```
    
4. **Anwendung der vorgeschlagenen Änderungen auf https://stackoverflow.com/questions/37193356/registering-net-com-dlls-without-admin-rights-regasm**
   - 🔍 Anleitung:
     - Check whether the file contains CodeBase entries
Open your .reg file with a text editor (e.g. Notepad++).

Search for CodeBase

	
