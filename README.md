# Kontor-ål Hjemmeside

En sjov og informativ hjemmeside om fordelene ved at have ål i dit kontormiljø. Dette projekt er bygget med Flask og bruger Bootstrap til styling.

## Funktioner

- Responsivt design
- Moderne UI med animationer
- Information om kontor-ål og deres fordele
- Fokus på dyrevelfærd og miljømæssige fordele

## Installation

1. Opret et virtuelt miljø (anbefalet):
```bash
python -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate
```

2. Installer afhængigheder:
```bash
pip install -r requirements.txt
```

3. Start applikationen:
```bash
python app.py
```

4. Åbn din browser og besøg `http://localhost:1331`

## Projektstruktur

```
office-eels/
├── app.py              # Hoved Flask applikation
├── requirements.txt    # Projekt afhængigheder
├── static/             # Statiske filer (CSS, billeder)
│   └── style.css
│   └── images/
│       └── memes/     # Mappe til åle memes
└── templates/         # HTML templates
    └── index.html
    └── eksempler.html
```

## Brugte Teknologier

- Flask
- Jinja2