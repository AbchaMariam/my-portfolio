from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    data = {
        "name": "Meriam ABCHA",
        "title": "Business Analytics Student & Data Enthusiast",
        "email": "maryem.abcha@gmail.com",
        "phone": "+216 29237171",
        "location": "Ariana, La Soukra, Tunisie",
        "linkedin": "Meriam ABCHA",
        "about": "Étudiante en Master Business Analytics à Esprit School of Business, passionnée par la data, l'intelligence artificielle et la transformation digitale. Curieuse et ambitieuse, je conçois des solutions innovantes qui créent de la valeur à travers l'analyse de données et l'automatisation.",
        "skills": {
            "soft": ["Leadership", "Gestion de projet", "BPM", "Stratégie Marketing", "ERP / CRM"],
            "data": ["Power BI", "MySQL / SQL Server / NoSQL", "Talend / SSIS (ETL)"],
            "dev": ["Python (Pandas, NumPy, Scikit-learn, BeautifulSoup, Selenium)", "PHP / C#.net / SpringBoot", "Angular / HTML / CSS / JavaScript", "n8n / Docker"]
        },
        "languages": [
            {"name": "Arabe", "level": "Langue maternelle", "percent": 100},
            {"name": "Français", "level": "B2", "percent": 75},
            {"name": "Anglais", "level": "B2", "percent": 75},
        ],
        "education": [
            {"degree": "Master en Business Analytics", "school": "Esprit School of Business, Tunis", "year": "2025–2027"},
            {"degree": "Licence en Informatique de Gestion (BIS)", "school": "Esprit School of Business, Tunis", "year": "2022–2025"},
            {"degree": "Bac Économie et Gestion", "school": "Lycée 1, Bengarden", "year": "2022"},
        ],
        "experiences": [
            {
                "title": "Stage PFE – Siège d'assurance",
                "company": "Assurances Maghrebia",
                "period": "Février 2025 – Juillet 2025",
                "tasks": [
                    "Conception d'un système automatisé de web scraping depuis des rapports PDF, avec structuration des données en JSON.",
                    "Création de tableaux de bord interactifs sous Power BI pour la visualisation des indicateurs clés.",
                    "Automatisation des tâches via cron jobs et conteneurisation avec Docker."
                ]
            },
            {
                "title": "Stage d'été – Cabinet d'assurances",
                "company": "Assurances Maghrebia",
                "period": "Juillet 2024 – Août 2024",
                "tasks": [
                    "Gestion de dossiers clients, utilisation d'un logiciel métier.",
                    "Suivi de réclamations et sinistres."
                ]
            },
            {
                "title": "Stage d'été – Cabinet d'assurances",
                "company": "Cabinet d'assurances",
                "period": "Juillet 2023 – Août 2023",
                "tasks": [
                    "Relation client, logiciel assurance.",
                    "Gestion de dossiers et processus métier."
                ]
            },
        ],
        "projects": [
            {
                "title": "VIP Concierge — Chatbot IA & Automatisation",
                "year": "2026",
                "type": "Personnel",
                "tags": ["Python", "n8n", "Power BI", "ETL"],
                "description": "Orchestration d'un chatbot IA assistant VIP capable d'identifier les clients, gérer les commandes multi-produits et appliquer automatiquement une réduction de 15% aux clients ≥ 1000€. Dashboard analytique temps réel."
            },
            {
                "title": "Application de Gestion des Salles",
                "year": "2024",
                "type": "Académique",
                "tags": [".NET", "Angular", "SQL"],
                "description": "Développement en équipe d'une application complète de gestion des salles avec interface graphique en .NET/Angular."
            },
            {
                "title": "Site Web de Gestion des Événements",
                "year": "2024",
                "type": "Académique",
                "tags": ["PHP", "PhpMyAdmin", "Marketing"],
                "description": "Conception et développement d'un site web dynamique de gestion des événements à ESB. Travail en équipe avec stratégie marketing intégrée."
            },
            {
                "title": "Application de Gestion de Location de Voitures",
                "year": "2024",
                "type": "Académique",
                "tags": ["Java", "CRUD"],
                "description": "Développement en binôme d'une application de gestion de location avec interface graphique en Java."
            },
            {
                "title": "Application de Gestion de Cabinet Médical",
                "year": "2023",
                "type": "Académique",
                "tags": ["Python", "CRUD"],
                "description": "Développement en binôme d'une application de gestion médicale avec maîtrise du CRUD en Python Avancé."
            },
            {
                "title": "Mimi's Trinkets — Projet Bijoux",
                "year": "2023–2024",
                "type": "Personnel",
                "tags": ["Marketing", "Finance", "Commerce"],
                "description": "Mini projet entrepreneurial de création de bijoux. Optimisation des coûts, acquisition et fidélisation client via marketing, finance et relation commerciale."
            },
        ]
    }
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)
