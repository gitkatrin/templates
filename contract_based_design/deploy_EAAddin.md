# Deploy a new Add-In to Enterprise Architekt

## 3. Erzeugen einer Registrierungsdatei für die AddIns dll-Datei
 - 🔧 Benötigt wird:
	-  fertig kompilierte .dll-Datei vom Add-In (z. B. MulticToolingIndustrial.dll)
	-  Den Pfad zum .dll-File
	-  Einen gewünschten Speicherort für die .reg-Datei, z. B. auf dem Desktop
    
 - 🔍 Anleitung:
	- Angenommen, das Add-In wurde bereits kompiliert und die DLL liegt unter: ```C:\Projects\MULTIC\bin\Release\MULTIC.Tooling.Industrial.dll```
	- Und die Registry-Datei soll auf dem Desktop als Addin.reg gespeichert werden. Der Befehl sieht so aus:
		```
		C:\Windows\Microsoft.NET\Framework\v4.0.30319\RegAsm.exe "C:\Projects\MULTIC\bin\Release\MULTIC.Tooling.Industrial.dll" /codebase /regfile:"C:\Users\<YOUR-NAME>\Desktop\Addin.reg"
		```
    
## 4. Anwendung der vorgeschlagenen Änderungen auf https://stackoverflow.com/questions/37193356/registering-net-com-dlls-without-admin-rights-regasm
 - **4.1 Prüfe, ob die Datei CodeBase-Einträge enthält**
   - Öffne die .reg-Datei mit einem Texteditor (z. B. Notepad++).
   - Suche nach ```CodeBase``` → Beispiel: ```"CodeBase"="file:///C:/Pfad/zu/deiner/DLL/MULTIC.Tooling.Industrial.dll"```
      
 - **4.2 Prüfe, ob dein Interface registriert wurde**
    - Suche nach ```MTI.MTI_AddInInterface``` in der Datei.
    - Beispiel: 
		```
		[HKEY_CLASSES_ROOT\MTI.MTI_AddInInterface]
		@="MTI.MTI_AddInInterface"
		```
     	- Wenn es fehlt: → Wahrscheinlich ist „Assembly COM sichtbar machen“ nicht gesetzt (siehe Schritt [1.1]).
 - **4.3 Suchen & Ersetze ```HKEY_CLASSES_ROOT``` mit ```HKEY_CURRENT_USER\Software\Classes```**
   - → Dadurch werden die Einträge nur für deinen Benutzer registriert – keine Adminrechte nötig!
    
 - **4.4 Erstelle eine Kopie der Registry-Datei**
   - Speichere sie z. B. als Addin_copy.reg. Sie wird für die nächsten Schritte benötigt.
       
 - **4.5 Aus der Kopie ALLES löschen, was NICHT „\CLSID\“ enthält**
   - In Addin_copy.reg: Lösche alle Blöcke und Einträge, die nicht „\CLSID\“ im Pfad enthalten.
    
 - **4.6 In der Kopie „Classes\CLSID“ suchen und durch „Classes\Wow6432Node\CLSID“ ersetzen**
   - → Das ist notwendig für 32-Bit COM-Kompatibilität, da Enterprise Architect 32-Bit ist.
    
 - **4.7 Kopiere alle Registry-Blöcke aus Addin_copy.reg (jetzt nur Wow6432Node\CLSID-Einträge) unten an die Originaldatei dran.**
 - **4.8 (Aus der stack overflow Anleitung) Entfernen Sie die Registrierungseinträge ```HKLM``` mithilfe von regasm: ```Regasm YourDLL.dll /unregister```**

## 5. (Optional) Lösche die Kopie der .reg-Datei.

## 6. .reg-Datei ausführen
   - Doppelklick auf deine fertig bearbeitete .reg-Datei
   - Bestätige die Nachfrage vom Registry-Editor mit „Ja“, um die Einträge hinzuzufügen
   - Folgende Meldung sollte aufploppen: „Die Schlüssel und Werte wurden erfolgreich in die Registrierung eingetragen.“

## 7. Manuelles Einfügen einenes Verweis auf den Eintragspunkt des Add-Ins in der Registrierung.
 - **7.1 Regedit öffnen**
	- ```Win + R``` drücken → Eingeben: regedit → Enter
	- Du brauchst keine Adminrechte, da du mit HKEY_CURRENT_USER arbeitest
 - **7.2 Zu EA-AddIns-Zweig navigieren**
 	- Pfad: ```HKEY_CURRENT_USER\SOFTWARE\Sparx Systems\EAAddins```
  	- Wenn EAAddins noch nicht existiert: Rechtsklick auf "Sparx Systems" → Neu > Schlüssel → nenne ihn "EAAddins"
 - **7.3 dd-In-Schlüssel erstellen**
	- Rechtsklick auf "EAAddins" → Neu > "Zeichenfolgenwert"
	- Name:```MULTIC-Tooling```
 	- Wert: ```MTI.MTI_AddInInterface``` → der Wert muss exakt der Name deiner COM-Klasse sein
  - **7.4 Regedit schließen**


## 8. Starte Enterprise Architect und vergewissern Sie sich, dass ein neuer Eintrag „MULTIC-Tooling“ auf der Registerkarte „Spezialisierung“ des Ribbons hinzugefügt wurde.
 - Starte Enterprise Architect
 - Wechsle zum Reiter „Specialize“ (oder „Erweitern“ auf Deutsch)
 - Suche nach dem Eintrag „MULTIC-Tooling“
 - Falls es nicht erscheint:
	- Gehe zu „Erweiterungen > Add-In-Manager“
 	- Dort siehst du Ob dein Add-In geladen wurde oder eventuelle Fehlermeldungen (z. B. Interface nicht gefunden)




