#-*- coding: cp1252 -*-

import easygui
eis = easygui.choicebox("Was wollen Sie fuer eine Eissorte?", choices = ['Himbeer', 'Erdbeer', 'Kirsch', 'Waldfrüchte', 'Heidelbeere', 'Schoko', 'Vanille', 'Mokka', 'Rocher', 'Mango', 'Granatapfel', 'Cranberry', 'Sesam', 'Jne', 'Limmette', 'Karamel mit gesalzener Butter', 'Smarties', 'Casis', 'Orange', 'Mandarine', 'Malaga', 'Schlumpfeis', 'Tutti Frutti', 'Praline', 'Amarena-Kirsch', 'Zitrus-Mix', 'Kafee-eis', 'Papaya', 'Ananas', 'After-Eight', 'Milchschokolade', 'Weisseschokolade', 'Snickerseis', 'Marseis', 'Twixeis', 'Bountyeis'])


if eis:
    preis_fuers_Eis = 1.1
else: 
    preis_fuers_Eis = 0

message = "Ihre wahl war " +str(eis) + " es kostet "+ str(preis_fuers_Eis) +"E DANKE FUER IHREN EINKAUF BEI EISPARADIS LITTI!!";

easygui.msgbox (message)
print(message)
