# EDA-FIB-PlayerEvaluator
Programa que executa múltiples vegades el joc de les assignatures EDA (GEI FIB-UPC) i d'Algorísmia (FME-UPC), permetent comparar jugadors i valorar quin convé més.

Un problema habitual dels estudiants és valorar quin dels jugadors que han programat és millor. Aquest programa resol això, permetent executar partides de manera automatitzada, desant una sèrie de mètriques i donant-nos-en el resultat. 

El programa no inclou el joc, sinó que l'estudiant l'ha de descarregar a banda i enllaçar-lo, com s'explica més endavant. 

## Instal·lació i posada a punt
1. Descarregar aquest repositori
2. Posar la carpeta "game" dins del directori
  * Opció 1: copiar-lo directament. Pot fer-se des de l'explorador, o amb la comanda:
  `cp -r [directori_joc]/game`
  * Opció 2: per no haver de tenir dues carpetes, es pot fer un enllaç:
  `ln -s [directori_joc]/game`
3. Comprovar que tinguem python3 disponible. Provar les opcions `python --version` i `python3 --version`, i si és 3.* ja serveix. Aquest serà el que utilitzarem per executar el programa
  * Si no el tenim, podem instal·lar-lo utilitzant el gestor de paquets habitual (apt, pacman...)

## Sobre el joc
Aquest programa està pensat per poder executar el joc de l'assignatura EDA del Grau en Enginyeria Informàtica de la FIB-UPC, així com el de l'assignatura Algorísmia del Grau en Matemàtiques de la FME-UPC. El joc, però, no ve inclòs al repositori, sinó que cal tenir accés al problema del Jutge o que algú t'hagi passat el zip.

El programa automatitza la crida al joc. És a dir, cal poder executar el joc de la manera habitual, tal com es descriu a l'enunciat. En particular, i de manera no exhaustiva:
* Els noms dels nostres jugadors: com diu l'enunciat, el nom de l'arxiu ha de ser AI[NOM].cc, on [NOM] és el nom que hem triat, i amb el que hi farem referència. Dins de l'arxiu cal haver definit el nom del jugador com a [NOM] (sense "AI")
* Els jugadors d'altres persones, dels quals tenim el .o, han d'estar inclosos al Makefile. Per exemple: `EXTRA_OBJ = AIOriol.o`
* Cal haver compilat abans d'executar el programa. Es pot fer amb `make`

## Ús
La comanda bàsica executarà 100 proves dels jugadors, amb seeds consecutives, desant la informació completa en arxius csv i mostrant per la sortida estàndard un resum de les diverses mètriques.

`python3 PlayerEvaluator.py jugador1 jugador2 jugador3 jugador4`

Per exemple, un cas hipotètic seria:

`python3 PlayerEvaluator.py Oriol Dummy Dummy Dummy`

```
Partides guanyades:
        Oriol: 99/100
        Dummy: 0/100
        Dummy: 0/100
        Dummy: 1/100
Mínims:
        score_0: 7920
        score_1: 1749
        score_2: 1751
        score_3: 1461
        scr_acc_0: 6700
        scr_acc_1: 1700
        scr_acc_2: 1650
        scr_acc_3: 1370
        strength_0: 39
        strength_1: 176
        strength_2: 13
        strength_3: 40
        status_0: 0
        status_1: 0
        status_2: 0
        status_3: 0
Màxims:
        score_0: 12152
        score_1: 9294
        score_2: 9897
        score_3: 9056
        scr_acc_0: 10330
        scr_acc_1: 8540
        scr_acc_2: 9180
        scr_acc_3: 8400
        strength_0: 3365
        strength_1: 1551
        strength_2: 1287
        strength_3: 1381
        status_0: 0
        status_1: 0
        status_2: 0
        status_3: 0
Mitjans:
        score_0: 10744.47
        score_1: 4349.82
        score_2: 4362.86
        score_3: 4348.74
        scr_acc_0: 8934.2
        scr_acc_1: 4160.5
        scr_acc_2: 4177.1
        scr_acc_3: 4154.3
        strength_0: 1742.83
        strength_1: 684.47
        strength_2: 655.82
        strength_3: 708.89
        status_0: 0.0
        status_1: 0.0
        status_2: 0.0
        status_3: 0.0

```

Podem variar el nombre de proves, la seed inicial, i desar les partides per poder-les visualitzar utilitzant flags del programa. Podeu executar `python3 PlayerEvaluator.py --help`per veure les opcions

Els resultats seran desats a la carpeta "resultats" (que serà creada si no existeix), i en cas d'activar el flag "--desa-partides" les partides completes seran desades a la carpeta "partides" (que també serà creada si no existeix). El programa no tocarà res de la carpeta del joc, i tampoc escriurà enlloc més.

El programa escriu per la sortida estàndard (STDOUT) el resum de les mètriques, i per la sortida d'errors (STDERR) ens indica els arxius que està escrivint.

## Sobre les mètriques
El programa agafa les mètriques existents en la última versió. En aquest moment n'hi ha una, status, que no és utilitzada, així que dóna sempre 0. Pot ser que jocs posteriors no utilitzin alguna altra, o bé que n'afegeixin de noves.

Si s'afegeixen noves mètriques, podeu modificar el codi per afegir-les (i fer una pull request), o bé crear una *issue* per sol·licitar-ho.

## Llicència
Aquest programa està sota la llicència [GNU GPLv3](LICENSE). En resum:
* Podeu executar el programa, sense limitacions
* Podeu redistribuir el programa, sempre que conserveu la mateixa llicència
* Podeu modificar el programa, sempre que conserveu la mateixa llicència. 
* Podeu redistribuir el programa modificat, amb el mateix nom o un altre, sempre que conserveu la mateixa llicència.
