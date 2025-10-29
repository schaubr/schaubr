# AI Service Recommendation Flow

Een AI-gestuurd systeem dat automatisch relevante services, best practices en ervaringskennis aanreikt op basis van klantcontext en problematiek, waardoor consultants sneller en accurater klantvoorstellen kunnen genereren die aansluiten bij de specifieke behoeften van de klant.

## Overzicht

Dit systeem gebruikt een multi-agent architectuur gebouwd met **LangFlow** en **Anthropic's Claude API** om:

1. Klantcontext en problematiek te analyseren
2. Relevante services te matchen
3. Best practices aan te reiken
4. Ervaringskennis en case studies op te halen
5. Geïntegreerde klantvoorstellen te genereren
6. Kwaliteitscontrole uit te voeren

## Architectuur

### Agent Overzicht

Het systeem bestaat uit 10 gespecialiseerde agenten:

1. **Context Analysis Agent**: Analyseert klantcontext (industrie, bedrijfsgrootte, maturiteit, etc.)
2. **Problem Analysis Agent**: Diepgaande analyse van de problematiek
3. **Service Matcher Agent**: Matcht klantbehoeften met beschikbare services
4. **Best Practices Agent**: Identificeert relevante best practices en frameworks
5. **Experience Knowledge Agent**: Haalt vergelijkbare cases en lessons learned op
6. **Proposal Generator Agent**: Synthetiseert alle informatie tot een voorstel
7. **Quality Review Agent**: Controleert kwaliteit en consistentie
8. **Proposal Refiner**: Verfijnt het voorstel op basis van feedback

### Flow Diagram

```
┌─────────────────────┐     ┌─────────────────────┐
│ Customer Context    │     │ Problem Description │
│ Input               │     │ Input               │
└──────────┬──────────┘     └──────────┬──────────┘
           │                           │
           ▼                           ▼
    ┌──────────────────────────────────────┐
    │   Context Analysis Agent             │
    └──────────────┬───────────────────────┘
                   │
                   ├──────────┬──────────┬─────────────┐
                   ▼          ▼          ▼             ▼
            ┌──────────┐ ┌─────────┐ ┌──────────┐ ┌──────────┐
            │ Problem  │ │ Service │ │   Best   │ │Experience│
            │ Analysis │ │ Matcher │ │Practices │ │Knowledge │
            └────┬─────┘ └────┬────┘ └────┬─────┘ └────┬─────┘
                 │            │           │            │
                 └────────────┴───────────┴────────────┘
                              │
                              ▼
                   ┌──────────────────────┐
                   │ Proposal Generator   │
                   └──────────┬───────────┘
                              │
                   ┌──────────┴───────────┐
                   ▼                      ▼
            ┌─────────────┐      ┌───────────────┐
            │   Quality   │      │   Proposal    │
            │   Review    │──────▶   Refiner     │
            └─────────────┘      └───────┬───────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │Final Output │
                                  └─────────────┘
```

## Installatie

### Vereisten

- Python 3.9+
- LangFlow 0.6.0+
- Anthropic API Key

### Setup Stappen

1. **Clone de repository**
   ```bash
   git clone <repository-url>
   cd schaubr
   ```

2. **Installeer dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configureer environment variables**
   ```bash
   cp .env.example .env
   # Edit .env en voeg je Anthropic API key toe
   ```

4. **Start LangFlow**
   ```bash
   langflow run
   ```

5. **Importeer de flow in LangFlow**
   - Open LangFlow UI (standaard: http://localhost:7860)
   - Klik op "Import Flow"
   - Selecteer `ai_service_recommendation_flow.json`

## Gebruik

### Via LangFlow UI

1. Open LangFlow UI
2. Selecteer de "AI Service Recommendation Flow"
3. Vul de inputs in:
   - **Customer Context**: Beschrijving van klant (industrie, grootte, uitdagingen, etc.)
   - **Problem Description**: Specifieke problematiek en behoeften
4. Klik op "Run Flow"
5. Bekijk het gegenereerde voorstel en metadata

### Via Python Script

#### Interactieve Modus

```bash
python run_flow.py --interactive
```

#### Met Command-line Arguments

```bash
python run_flow.py \
  --customer-context "Middelgroot financieel bedrijf met 500 medewerkers..." \
  --problem "Verouderde legacy systemen die integratie belemmeren..." \
  --output proposal.json
```

#### Met Input Bestanden

```bash
python run_flow.py \
  --context-file examples/customer_context.txt \
  --problem-file examples/problem_description.txt \
  --output proposal.json
```

### Via LangFlow API

```python
import requests

url = "http://localhost:7860/api/v1/run/<flow-id>"
payload = {
    "inputs": {
        "customer_context": "Uw klantcontext hier...",
        "problem_description": "Uw probleem beschrijving hier..."
    }
}

response = requests.post(url, json=payload)
result = response.json()

print(result['outputs']['final_output'])
```

## Voorbeelden

### Voorbeeld Input

**Customer Context:**
```
Bedrijf: TechCorp Financial Services
Industrie: Financiële dienstverlening
Grootte: 750 medewerkers, €150M omzet
Locaties: 5 kantoren in Nederland

Huidige situatie:
- Voornamelijk on-premise infrastructuur
- Mix van legacy en moderne applicaties
- Beperkte cloud adoptie
- Sterke focus op compliance en security

Strategische doelen:
- Moderniseren van IT infrastructuur
- Verbeteren van customer experience
- Verhogen van operationele efficiëntie
- Accelereren van digitale transformatie
```

**Problem Description:**
```
Kernproblemen:
1. Legacy mainframe systemen blokkeren innovatie
2. Langzame time-to-market voor nieuwe features
3. Hoge operationele IT kosten
4. Moeilijkheden met naleving van nieuwe regelgeving
5. Siloed data architecture beperkt analytics mogelijkheden

Business Impact:
- Verlies van marktaandeel aan fintech concurrenten
- Customer satisfaction scores dalen
- IT budget groeit sneller dan revenue
- Compliance risico's nemen toe

Gewenste outcomes:
- Moderniseren van core banking systemen
- Cloud migration strategie
- Implementatie van DevOps praktijken
- Verbetering van data governance
- Snellere innovatie cycles
```

### Voorbeeld Output Structuur

```json
{
  "outputs": {
    "final_output": "# KLANTVOORSTEL: TechCorp Financial Services\n\n## Executive Summary\n...",
    "metadata_output": {
      "context_analysis": {
        "industrie": "Financiële dienstverlening",
        "bedrijfsgrootte": "Middelgroot (750 FTE)",
        "maturiteit": "Transitie (van Traditional naar Cloud-native)",
        "technische_volwassenheid": "Medium-low"
      },
      "recommended_services": [
        {
          "service": "Cloud Migration & Modernization",
          "priority": "Hoog",
          "rationale": "Essentieel voor het moderniseren van legacy systemen"
        }
      ],
      "quality_score": 8.5
    }
  }
}
```

## Configuratie

### Services Catalogus

De Service Matcher Agent werkt met de volgende services (pas aan in de flow JSON):

- Cloud Migration & Modernization
- DevOps & CI/CD Implementation
- Data Analytics & AI/ML Solutions
- Cybersecurity & Compliance
- Application Development & Integration
- Infrastructure Optimization
- Digital Transformation Consulting
- Agile & Process Optimization
- Training & Change Management

### Model Configuratie

Standaard wordt Claude 3.5 Sonnet gebruikt voor alle agenten. Je kunt dit aanpassen per agent in de flow JSON:

```json
{
  "model_name": "claude-3-5-sonnet-20241022",
  "temperature": 0.3,
  "max_tokens": 2000
}
```

**Aanbevolen temperature settings:**
- Analysis agents: 0.3 (meer deterministisch)
- Creative agents (Proposal Generator): 0.6 (meer creativiteit)
- Quality Review: 0.3 (consistente beoordeling)

## Customization

### Eigen Services Toevoegen

1. Open `ai_service_recommendation_flow.json`
2. Zoek de "Service Matcher Agent" node
3. Update de `system_message` met je services

### Best Practices Uitbreiden

1. Update de "Best Practices Agent" system message
2. Voeg je eigen frameworks en methodologieën toe

### Ervaringskennis Integreren

Voor echte ervaringskennis, integreer met:
- Vector database (Pinecone, Weaviate)
- Knowledge base (Confluence, SharePoint)
- CRM systeem (Salesforce)

Voeg een RAG (Retrieval-Augmented Generation) node toe voor de Experience Knowledge Agent.

## Ontwikkeling

### Project Structuur

```
schaubr/
├── ai_service_recommendation_flow.json  # Hoofdflow definitie
├── run_flow.py                         # Python runner script
├── requirements.txt                    # Python dependencies
├── .env.example                        # Environment variables template
├── README.md                           # Deze documentatie
├── examples/                           # Voorbeeld inputs
│   ├── customer_context.txt
│   └── problem_description.txt
└── docs/                               # Extra documentatie
    ├── architecture.md
    └── api_reference.md
```

### Testing

```bash
# Test met voorbeeld data
python run_flow.py \
  --context-file examples/customer_context.txt \
  --problem-file examples/problem_description.txt
```

### Debugging

LangFlow heeft ingebouwde debugging tools:
- Bekijk intermediate outputs van elke agent
- Inspect prompt templates
- Monitor API calls en kosten

## Best Practices

### Input Kwaliteit

Voor beste resultaten, zorg voor:
- **Specifieke context**: Concrete details over bedrijf, industrie, grootte
- **Kwantificeerbare problemen**: Meetbare impact en KPIs
- **Duidelijke doelen**: Wat wil de klant bereiken
- **Constraints**: Budget, tijdlijnen, technische beperkingen

### Output Optimalisatie

- **Review altijd de quality score**: < 7 betekent mogelijk herwerking nodig
- **Pas aan op basis van feedback**: Gebruik de refiner output
- **Valideer aanbevelingen**: Check of services echt beschikbaar zijn
- **Personaliseer verder**: Voeg specifieke team/contact informatie toe

## Kosten en Performance

### API Kosten

Geschatte kosten per run (met Claude 3.5 Sonnet):
- Input: ~5,000-10,000 tokens → $0.015-0.030
- Output: ~8,000-15,000 tokens → $0.120-0.225
- **Totaal per voorstel: ~$0.15-0.30**

### Performance

Typische executietijd:
- Eenvoudig voorstel: 30-60 seconden
- Complex voorstel: 60-120 seconden

Optimalisatie tips:
- Gebruik caching voor herhaalde analyses
- Parallelliseer onafhankelijke agenten waar mogelijk
- Overweeg kleinere modellen voor eenvoudige taken

## Roadmap

Toekomstige verbeteringen:
- [ ] RAG integratie voor echte ervaringskennis
- [ ] Multi-language support
- [ ] Template library voor voorstellen
- [ ] A/B testing van verschillende agent prompts
- [ ] Integration met CRM systemen
- [ ] Automated proposal versioning
- [ ] Export naar PDF/DOCX formats
- [ ] Analytics dashboard voor proposal success rates

## Troubleshooting

### Veelvoorkomende Problemen

**"API Key Error"**
- Check of ANTHROPIC_API_KEY correct is ingesteld in .env
- Verifieer dat de API key nog geldig is

**"Flow niet gevonden"**
- Importeer de flow opnieuw in LangFlow
- Check of de flow ID correct is

**"Timeout errors"**
- Verhoog de timeout in run_flow.py
- Overweeg minder complexe inputs

**"Lage quality scores"**
- Verbeter input kwaliteit en specificiteit
- Pas agent prompts aan
- Review intermediate outputs voor inconsistenties

## Support

Voor vragen en support:
- Documentatie: Dit README bestand
- Issues: GitHub Issues
- LangFlow docs: https://docs.langflow.org
- Anthropic docs: https://docs.anthropic.com

## Licentie

[Voeg hier je licentie informatie toe]

## Credits

Gebouwd met:
- [LangFlow](https://github.com/logspace-ai/langflow)
- [Anthropic Claude](https://www.anthropic.com/claude)
- [LangChain](https://www.langchain.com)
