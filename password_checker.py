import hashlib
import requests
import getpass
import secrets
import string

def evaluer_robustesse(mdp):
    longueur = len(mdp)
    a_min = any(c.islower() for c in mdp)
    a_maj = any(c.isupper() for c in mdp)
    a_chiffre = any(c.isdigit() for c in mdp)
    a_special = any(not c.isalnum() for c in mdp)

    familles = sum([a_min, a_maj, a_chiffre, a_special])
    score = (longueur >= 8) + (longueur >= 12) + (longueur >= 16) + familles

    if score <= 2:
        niveau = 'Faible'
    elif score <= 4:
        niveau = 'Moyen'
    else:
        niveau = 'Fort'

    conseils = []
    if longueur < 12:
        conseils.append('Allonger à au moins 12 caractères.')
    if familles < 3:
        conseils.append('Mélanger minuscules, majuscules, chiffres et symboles.')

    return {'niveau': niveau, 'score': score, 'conseils': conseils}

def compte_fuites(mdp):
    sha1 = hashlib.sha1(mdp.encode('utf-8')).hexdigest().upper()
    prefixe, suffixe = sha1[:5], sha1[5:]

    url = f'https://api.pwnedpasswords.com/range/{prefixe}'
    reponse = requests.get(url, timeout=10)
    reponse.raise_for_status()

    for ligne in reponse.text.splitlines():
        suffixe_trouve, nombre = ligne.split(':')
        if suffixe_trouve == suffixe:
            return int(nombre)
    return 0

def charger_mots(chemin='wordlist_fr_5d.txt'):
    mots = []
    with open(chemin, encoding='utf-8') as f:
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                mots.append(ligne.split()[1])   # chaque ligne : numéro puis mot
    return mots

def generer_mot_de_passe(longueur=16):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*-_'
    return ''.join(secrets.choice(alphabet) for _ in range(longueur)) #secrets reste conçu pour la sécurité, contrairement à random

def generer_phrase(nb_mots=6):
    mots = charger_mots()
    return '-'.join(secrets.choice(mots) for _ in range(nb_mots))

def main():
    if input('Tester un mot de passe (1) ou en générer un (2) ? ') == '2':
        print('Mot de passe :', generer_mot_de_passe())
        print('Phrase de passe :', generer_phrase())
        return
    mdp = getpass.getpass('Mot de passe à tester (saisie masquée) : ')
    if not mdp:
        print('Aucun mot de passe saisi.')
        return

    resultat = evaluer_robustesse(mdp)
    niveau = resultat['niveau']
    score = resultat['score']
    print(f'\nRobustesse : {niveau} (score {score}/7)')
    for conseil in resultat['conseils']:
        print(f'  - {conseil}')

    try:
        fuites = compte_fuites(mdp)
    except requests.RequestException:
        print('\nImpossible de contacter le service (vérifier la connexion).')
        return

    if fuites:
        print(f'\nATTENTION : ce mot de passe apparaît {fuites} fois dans des fuites connues.')
    else:
        print('\nOK : aucune fuite connue pour ce mot de passe.')

if __name__ == '__main__':
    main()