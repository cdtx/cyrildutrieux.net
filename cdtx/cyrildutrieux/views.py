from django.template import Context
from django.shortcuts import render
from django.utils.html import format_html

# Create your views here.
def homePage(request):
    content = {
        'name': 'Cyril DUTRIEUX',
        'function': {
            'fr': 'Développeur logiciel indépendant',
            'en': 'Freelance software developper',
        },
        'cards': [
            {
                'title': {
                    'fr': 'Systèmes embarqués',
                    'en': 'Embedded systems',
                },
                'body' : {
                    'fr': format_html('''
                        <p>Objets connectés, communicants, domotique, etc.</p>    
                        <p>Je développe le logiciel embarqué pour ces systèmes à microcontroleurs</p>
                        <ul>
                            <li>Micro firmware</li>
                            <li>Installation de systèmes d'exploitation</li>
                        </ul>
                        <p>Je peux également créer des cartes électroniques de prototypage</p>
                    '''),
                },
            },
            {
                'title': {
                    'fr': 'Sécurité numérique',
                    'en': 'Digital security',
                },
                'body': {
                    'fr': format_html('''
                        <p>J'ai travaillé 4 ans pour <a href="http://www.insidesecure.com">Inside Secure</a>, un acteur du marché de la sécurité digitale</p>
                        <p>J'y ai construit des compétences dans les domaines :</p>
                        <ul>
                            <li>Carte à puce, protocole ISO 7816, PC/SC</li>
                            <li>Java Card, GlobalPlatform</li>
                            <li>Crypographie (DES/AES, RSA)</li>
                        </ul>
                        <p>Je peux être un atout sur du développement d'OS pour carte à puce, d'applet Java Card, de l'aide à la certification, écriture de scénarios de tests et déploiement.</p>
                        '''),
                },
            },
            {
                'title': {
                    'fr': 'Outils et productivité',
                    'en': 'Productivity and tools',
                },
                'body': {
                    'fr': format_html('''
                        <ul>
                            <li>Automatisation de tâches par script</li>
                            <li>Logiciel sur mesure</li>
                            <li>Organisation de travail en équipe</li>
                            <li>Source control management (Git, Subversion, etc.)</li>
                            <li>Utilisation de Linux</li>
                        </ul>
                        '''),
                },
            },
            {
                'title': 'Web',
                'body':{
                    'fr': format_html('''
                            <p>Pages web statiques (HTML, CSS, JavaScript, etc.)</p>
                            <p>Sites web dynamiques :</p>
                            <ul>
                                <li>Serveur python (Django, Flask)</li>
                                <li>Base de données</li>
                                <li>REST API</li>
                            </ul>
                        '''),
                },
            },
        ],
    }
    return render(request, 'cyrildutrieux/index.html', {'content': content, 'lang':request.GET.get('lang', 'fr')})
