import streamlit as st
from password_checker import evaluer_robustesse, compte_fuites

st.title('Testeur de mot de passe')

mdp = st.text_input('Mot de passe à tester', type='password')

if mdp:
    resultat = evaluer_robustesse(mdp)
    st.write(f"Robustesse : {resultat['niveau']} (score {resultat['score']}/7)")
    for conseil in resultat['conseils']:
        st.write('- ' + conseil)

    if st.button('Vérifier les fuites'):
        try:
            fuites = compte_fuites(mdp)
        except Exception:
            st.error('Service injoignable (vérifier la connexion).')
        else:
            if fuites:
                st.error(f'Vu {fuites} fois dans des fuites connues. À éviter.')
            else:
                st.success('Aucune fuite connue pour ce mot de passe.')