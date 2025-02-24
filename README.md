# Carnet de suivi
![GitHub](https://img.shields.io/badge/License-MIT-blue) ![GitHub](https://img.shields.io/badge/Statut-Opérationnel-dark_green) ![GitHub](https://img.shields.io/badge/Tests_Linux-Opérationnel-green) ![GitHub](https://img.shields.io/badge/Tests_Windows-Inconnu-red)


## Description
Ce projet est un générateur de carnet de suivi pour les étudiants en alternance de Polytech Tours.

Les tests Linux ont été réalisés sous Debian avec une installation vierge.
Les tests Windows n'ont pas encore été faits.
## Installation
### Sous Windows
- Installer git : https://git-scm.com/download/win
  - Se placer dans le répertoire dans lequel on souhaite installer le programme
  - Ouvrir git bash et entrer : `git clone https://github.com/romain327/carnet-de-suivi`
- Installer Python : https://www.python.org/downloads/windows/
  - cocher la case "Add Python 3.x to PATH"
- installer pip : https://pip.pypa.io/en/stable/installing/
- Lancer le fichier install.bat
- Texlive et tkinter seront installés.

Si vous obtenez des erreurs à la compilation, vérifiez que texlive et tkinter sont bien installés, et que vous utilisez bien une version récente de python (3.6 ou plus).

### Sous Linux
- Installer git : ouvrir un terminal et entrer : `sudo apt-get install git`
  - Se placer dans le répertoire dans lequel on souhaite installer le programme
  - Ouvrir un terminal et entrer : `git clone https://github.com/romain327/carnet-de-suivi`
- Installer Python : ouvrir un terminal et entrer : `sudo apt-get install python3`
- Se placer dans le dossier du projet et entrer lancer le script install.sh : `chmod +x install.sh && ./install.sh`
- texlive, pip et tkinter seront installés si vous ne les avez pas déjà.

## Utilisation
### Pré-requis
Vous devez avoir les fichiers nécessaires au carnet de suivi :
- Deux fichiers CSV au format séparateur point-virgule (;), ou séparateur virgule (,) :
  - Un fichier CSV contenant le carnet de suivi des cours
  - Un fichier CSV contenant le carnet de suivi de l'entreprise
- Un fichier txt contenant votre introduction
- Un fichier txt contenant votre conclusion
- un dossier dans lequel vous mettrez vos end of course un fichier txt par end of course) ⚠️ le txt doit avoir le nom de la matière)
- un dossier dans lequel vous mettrez vos synthèses entreprise
- un dossier dans lequel vous mettrez vos annexes (formats png, jpg ou pdf)

### Utilisation
- Lancer le programme
  - Sous Windows : double cliquez sur l'exécutable app.exe ou lancer le programme : `python suivi.py`
  - Sous Linux/MacOS : ouvrir un terminal et entrer : `python3 suivi.py`
- Remplir les champs demandés

Après avoir rempli les champs, cliquez sur le bouton "générer". Cela vous génèrera votre carnet mais également un fichier de configuration contenant les chemins vers vos fichiers. Si vous ne changez pas vos fichiers de place, vous n'avez donc pas besoin de remplir les champs à chaque fois.

## Développement
Si vous souhaitez cloner ce dépot pour faire des tests, des modifications ou des améliorations, des fichiers de test sont disponibles dans le répertoire test.
Vous pouvez activer le mode test en lançant le programme avec le flag -t : `python3 suivi.py -t`
