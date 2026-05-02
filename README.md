# Portfolio — Meriam ABCHA

Portfolio personnel développé avec **Python Flask** + **CSS** personnalisé.

## 🚀 Lancer en local

```bash
# 1. Installer Flask
pip install flask

# 2. Lancer l'application
python app.py

# 3. Ouvrir dans le navigateur
http://localhost:5000
```

## 📁 Structure
```
portfolio/
├── app.py                  # Application Flask principale
├── requirements.txt        # Dépendances Python
├── templates/
│   └── index.html          # Template HTML Jinja2
└── static/
    ├── css/
    │   └── style.css       # Styles CSS
    └── js/
        └── main.js         # Animations JavaScript
```

## 🌐 Hébergement gratuit sur Render.com

1. Créez un compte sur **render.com**
2. Connectez votre GitHub
3. Créez un **Web Service**
4. Start Command : `python app.py`
5. Votre site sera en ligne sur `monportfolio.onrender.com`

## ✏️ Personnaliser

Toutes les données sont dans `app.py` dans la variable `data`.
Modifiez simplement les valeurs pour mettre à jour le portfolio.
