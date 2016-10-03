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
                        <p>J'ai travaillé 4 ans pour Inside Secure, un acteur du marché de la sécurité digitale</p>
                        <p>J'y ai développé des compétences dans les domaines :</p>
                        <ul>
                            <li>Carte à puce, protocole ISO 7816</li>
                            <li>Java Card, GlobalPlatform</li>
                            <li>Crypographie (DES/AES, RSA)</li>
                        </ul>
                        '''),
                    'en': format_html(''''''),
                },
            },
            {
                'title': {
                    'fr': 'Outils et productivité',
                    'en': 'Productivity and tools',
                },
                'body': {
                    'fr': format_html(''''''),
                    'en': format_html(''''''),
                },
            },
            {
                'title': 'Web',
                'body': {
                    'fr': format_html(''''''),
                    'en': format_html(''''''),
                },
            },
        ],
    }
    return render(request, 'cyrildutrieux/index.html', {'content': content, 'lang':request.GET.get('lang', 'fr')})
