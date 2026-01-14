# Ransomware_Python
# Projet Ransomware Pédagogique (Python)

## Objectif
Ce projet simule un ransomware éducatif pour comprendre :
- La génération de clé et chiffrement
- La communication avec un serveur C2
- L'exfiltration de données

## Structure
- `client/` : code du malware (clé, chiffrement, envoi)
- `server/` : serveur C2 recevant UUIDs et clés
- `README.md` : documentation du projet

## Lancer le projet

### Serveur
```bash
cd server
python3 main.py

