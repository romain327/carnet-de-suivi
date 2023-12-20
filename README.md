# carnet-de-suivi

Statut : en cours de developpement

## Description
Ce projet est un générateur de carnet de suivi pour les étudiants en alternance de Polytech Tours.

## Installation et lancement du programme
### Sous Windows
- Installer git : https://git-scm.com/download/win
  - Se placer dans le répertoire dans lequel on souhaite installer le programme
  - Ouvrir git bash et entrer : `git clone https://github.com/romain327/carnet-de-suivi`
- Installer Python : https://www.python.org/downloads/windows/
  - cocher la case "Add Python 3.x to PATH"
- installer pip : https://pip.pypa.io/en/stable/installing/
- installer texlive : https://tug.org/texlive/windows.html
- Lancer le programe : double cliquer sur l'exécutable app.exe. Lors du premier lancement, tkinter sera installé si vous ne l'avez pas déjà.

Si vous obtenez des erreurs à la compilation, vérifiez que texlive et tkinter sont bien installés, et que vous utilisez bien une version récente de python (3.6 ou plus).

### Sous Linux/MacOS
- Installer git : ouvrir un terminal et entrer : `sudo apt-get install git`
  - Se placer dans le répertoire dans lequel on souhaite installer le programme
  - Ouvrir un terminal et entrer : `git clone https://github.com/romain327/carnet-de-suivi`
- Installer Python : ouvrir un terminal et entrer : `sudo apt-get install python3.8`

## Utilisation
### Pré-requis
- Deux fichiers CSV au format séparateur point-virgule (;), ou séparateur virgule (,) :
  - Un fichier CSV contenant le carnet de suivi des cours
  - Un fichier CSV contenant le carnet de suivi de l'entreprise

### Première utilisation
- Lancer le programme
  - Sous Windows : double cliquer sur l'exécutable app.exe
  - Sous Linux/MacOS : ouvrir un terminal et entrer : `python3 app.py`
- Des paquets sont installés automatiquement lors de la première utilisation.
  - Sous windows, tkinter est installé automatiquement.
  - Sous linux, texlive, pip et tkinter sont installés automatiquement.
- Une fois l'installation terminée, le programme se lance automatiquement.

### Utilisation normale
- Lancer le programme, un fenêtre s'ouvre.
  - La fenêtre est divisée en deux parties :
    - en haut les champs d'import des CSV cours et entreprise,
    - en bas les paramètres du carnet.
  
- Importer les CSV cours et entreprise
- Choisir un répertoire pour l'export du PDF
- Lors de la première utilisaiton, il faudra remplir les paramètres du carnet avec vos informations personnelles. Ensuite vos choix seront enregistrés.
- Cliquer sur Lancer
- Le PDF est généré dans le répertoire choisi.

## Conseils
Pour conserver les paramètres, l'application écrit dans un fichier le path des fichiers choisis. Si vous déplacez les fichiers, il faudra les rechoisir. Il est donc conseillé de conserver tous ces fichiers dans un répertoir et de ne plus y toucher.

## Développement
Si vous souaithez cloner ce dépot pour faire des tests, des modifications ou des améliorations, des fichiers de test sont disponibles dans le répertoire test.