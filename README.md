# Testeur de mot de passe

Outil en Python qui évalue la robustesse d'un mot de passe, vérifie s'il a fuité, et génère des mots de passe ou des phrases de passe solides. Utilisable en ligne de commande ou via une petite interface web.

## Fonctionnalités

- Note la robustesse d'un mot de passe (longueur, variété des caractères).
- Vérifie si le mot de passe figure dans des fuites connues, via l'API Have I Been Pwned.
- Génère un mot de passe aléatoire fort.
- Génère une phrase de passe à partir d'un dictionnaire français (méthode Diceware).
- Interface web optionnelle avec Streamlit.

## Confidentialité

Le mot de passe n'est jamais transmis en clair. Pour la vérification de fuite, seuls les 5 premiers caractères de son empreinte SHA-1 sont envoyés à l'API (principe de *k-anonymity*) ; le service renvoie une liste de suffixes dans laquelle le programme cherche localement. Rien n'est stocké ni journalisé.

## Prérequis

- Python 3.9 ou plus récent.
- Les bibliothèques `requests` et `streamlit`.
- Le fichier `wordlist_fr_5d.txt` à la racine du projet (dictionnaire Diceware français, 7776 mots).

## Installation

```bash
git clone https://github.com/<Echrac>/<password_checker>.git
cd <password_checker>
python3 -m venv .venv

# Windows (PowerShell) :
.\.venv\Scripts\Activate.ps1
# macOS / Linux :
# source .venv/bin/activate

python3 -m pip install requests streamlit
```

## Utilisation

### En ligne de commande

```bash
python3 password_checker.py
```

Le programme propose de **tester** un mot de passe existant ou d'en **générer** un nouveau (mot de passe aléatoire ou phrase de passe).

### Interface web

```bash
streamlit run app_web.py
```

Le navigateur s'ouvre sur `http://localhost:8501`.

## Structure du projet

```
.
├── password_checker.py   # logique : robustesse, fuites, génération
├── app_web.py            # interface web Streamlit
├── wordlist_fr_5d.txt    # dictionnaire Diceware français (7776 mots)
├── requirements.txt      # liste des dépendances
└── README.md
```

## Dépendances

Pour figer les dépendances du projet :

```bash
pip freeze > requirements.txt
```

Pour les réinstaller sur une autre machine :

```bash
pip install -r requirements.txt
```

## À propos

Projet d'apprentissage réalisé dans le cadre d'un portfolio (data / IA, cybersécurité). L'outil est conçu à des fins pédagogiques et de sensibilisation.

## Licence

MIT — libre de réutilisation. Ajouter un fichier `LICENSE` à la racine pour officialiser ce choix.