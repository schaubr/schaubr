# Quick Start Guide - AI Context Service Recommender

## 5 Minuten Setup

### Stap 1: Installeer Langflow
```bash
# Installeer Langflow via pip
pip install langflow

# Verificeer installatie
langflow --version
```

**Systeem Vereisten:**
- Python 3.9 of hoger
- pip package manager
- OpenAI API key

### Stap 2: Start Langflow
```bash
# Start de Langflow server
langflow run

# Langflow start op http://localhost:7860
# Open deze URL in je browser
```

### Stap 3: Importeer het Project
1. Open http://localhost:7860 in je browser
2. Klik op "Import" of het upload icoon
3. Selecteer `consultant-recommender.json`
4. De workflow wordt geladen in de visual editor

### Stap 4: Configureer OpenAI API Key
**Optie 1: Via Environment Variable (Aanbevolen)**
```bash
export OPENAI_API_KEY="sk-...your-key..."
langflow run
```

**Optie 2: Via UI**
1. Klik op elke OpenAIModel node (5 agent nodes)
2. Vul je API key in het "OpenAI API Key" veld
3. Klik "Save"

**Alternatieven:**
- Azure OpenAI: Gebruik Azure OpenAI component en configureer endpoint
- Anthropic Claude: Vervang OpenAIModel door Claude component
- Local models: Gebruik Ollama of LM Studio component

### Stap 5: Test met Voorbeeld Data
1. Klik op de "Run" button (▶️) rechtsboven
2. Vul de test inputs in (zie hieronder)
3. Bekijk de outputs in de rechter panel

**Test Input:**
```yaml
customerContext: "Een middelgrote bank met 500 medewerkers en legacy Java applicaties."

problemDescription: "Lange time-to-market (6-12 maanden) en hoge kosten. Willen digitaal transformeren."

industry: "Financial Services"
```

### Stap 6: Bekijk de Resultaten
Je krijgt 4 outputs:
- ✅ **Final Proposal** - Compleet klantvoorstel
- ✅ **Recommended Services** - Top 5 service aanbevelingen
- ✅ **Best Practices** - Relevante frameworks en methodologieën
- ✅ **Knowledge & Experience** - Case studies en lessons learned

## Eerste Echte Gebruik

### 1. Verzamel Klant Informatie
Praat met je klant en verzamel:
- **Context**: Organisatie, tech stack, team, huidige situatie
- **Problematiek**: Specifieke uitdagingen met business impact
- **Industry**: Sector waarin ze opereren

💡 **Tip:** Gebruik `example-input.yaml` als template met 6 uitgewerkte voorbeelden

### 2. Run de Workflow
1. Open Langflow in je browser
2. Plak de klant informatie in de 3 input velden
3. Klik "Run" (▶️)
4. Wacht 30-60 seconden terwijl de agents werken

**Wat gebeurt er?**
```
Input → Context Analyzer (8-15s)
         ↓
    ┌────┴────┬────────────┐
    ↓         ↓            ↓
Service   Best Practices  Knowledge  (parallel, 10-20s)
    └────┬────┴────────────┘
         ↓
    Proposal Synthesizer (15-25s)
         ↓
    4 Outputs
```

### 3. Review & Refine
1. Lees de gegenereerde outputs door
2. Check of de aanbevelingen kloppen
3. Pas aan waar nodig
4. Gebruik als basis voor klantgesprek of voorstel

## Tips voor Beste Resultaten

### ✅ DO's:
- Wees zo specifiek mogelijk in de input
- Vermeld concrete cijfers (team grootte, budget, impact)
- Noem de huidige tech stack
- Beschrijf constraints (tijd, budget, compliance)
- Geef context over het team en hun vaardigheden

**Voorbeeld (Goed):**
```
customerContext: "Retail keten met 150 winkels, 30% online verkoop.
E-commerce op Magento (5 jaar oud), 15 developers (mix intern/extern),
AWS lift-and-shift zonder cloud-native architectuur."
```

### ❌ DON'Ts:
- Generieke input ("een bedrijf dat wil digitaliseren")
- Te kort of te lang (sweet spot: 100-300 woorden per veld)
- Vage problemen zonder business impact
- Jargon zonder uitleg
- Gevoelige data (klantnamen, financiële details)

**Voorbeeld (Slecht):**
```
customerContext: "Een bedrijf"
```

## Veelvoorkomende Scenarios

### Scenario 1: Klant Belt met Vage Vraag
```yaml
customerContext: "Start met wat je weet: sector, grootte, wat je kon afleiden uit gesprek"
problemDescription: "Beschrijf hun vraag en wat je denkt dat erachter zit"
industry: "Hun sector"
```
➡️ Gebruik de output om gerichtere vragen te stellen in het volgende gesprek

### Scenario 2: RFP Response
```yaml
customerContext: "Kopieer relevante delen uit de RFP over hun organisatie"
problemDescription: "Vat de requirements en challenges samen uit de RFP"
industry: "Uit RFP"
```
➡️ Gebruik als eerste draft van je proposal

### Scenario 3: Discovery Workshop Voorbereiding
```yaml
customerContext: "Wat je tot nu toe weet uit pre-sales gesprekken"
problemDescription: "Hun initiële vraag/probleem zoals besproken"
industry: "Hun sector"
```
➡️ Gebruik om je voor te bereiden met relevante vragen en frameworks

## Aanpassen van het Systeem

### Je Eigen Services Toevoegen
1. Open de workflow in Langflow
2. Klik op de "Service Recommender Agent" node
3. Pas de System Message aan met je eigen service catalog:

```
Service categorieën:
- Jouw Custom Service 1
- Jouw Custom Service 2
- Cloud Native Development
- etc.
```

### Temperature Aanpassen
Voor meer creatieve/conservatieve output:
1. Open een agent node
2. Zoek het "Temperature" veld
3. Verlaag (0.3-0.5) voor meer consistente output
4. Verhoog (0.8-0.9) voor meer creatieve output

**Huidige Settings:**
- Context Analyzer: 0.7 (balanced)
- Service Recommender: 0.6 (consistent)
- Best Practices: 0.7 (balanced)
- Knowledge Base: 0.8 (creative)
- Proposal Synthesizer: 0.7 (balanced)

### Andere Taal
Pas alle System Messages aan naar Engels, Frans, etc.:
1. Open elke agent node
2. Vertaal de "System Message"
3. Pas de prompt templates aan
4. Save

### Export naar API
Langflow heeft ingebouwde API support:

```bash
# Verkrijg de flow ID uit de URL of settings
curl -X POST http://localhost:7860/api/v1/run/{flow_id} \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {
      "customer_context": "Een middelgrote bank...",
      "problem_description": "Digitale transformatie...",
      "industry": "Financial Services"
    }
  }'
```

## Troubleshooting

**"Module not found" of "Import error"**
```bash
# Herinstalleer Langflow
pip install --upgrade langflow

# Of in een clean environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install langflow
```

**"API Key invalid"**
- Check of je key correct is ingevoerd
- Verify dat je OpenAI account actief is en credits heeft
- Test je key: https://platform.openai.com/playground

**"Timeout error" of "Too many tokens"**
- Je input is mogelijk te lang (max ~3000 woorden)
- Verhoog `Max Tokens` in de agent settings
- Of splits je input op in kleinere delen

**"Output is te generiek"**
- Voeg meer specifieke details toe aan je input
- Vermeld concrete tech stack en constraints
- Geef concrete cijfers over impact en budget
- Gebruik voorbeelden uit `example-input.yaml` als referentie

**"Output is te technisch voor mijn klant"**
- Open de "Proposal Synthesizer Agent" node
- Pas de System Message aan:
  - Voeg toe: "Schrijf voor een business audience zonder technische achtergrond"
  - Of: "Gebruik eenvoudige taal en vermijd jargon"

**"Agents lopen niet parallel"**
- Dit is normaal in Langflow - parallellisatie gebeurt automatisch
- Service, Best Practices en Knowledge agents kunnen parallel werken
- Je ziet het verschil vooral bij grotere workflows

**"Can't connect to Langflow server"**
```bash
# Check of Langflow draait
ps aux | grep langflow

# Check of port 7860 vrij is
lsof -i :7860

# Herstart Langflow
pkill -f langflow
langflow run
```

## Advanced Usage

### Docker Deployment
```bash
# Run Langflow in Docker
docker run -it -p 7860:7860 \
  -e OPENAI_API_KEY="sk-..." \
  logspace/langflow

# Met persistent storage
docker run -it -p 7860:7860 \
  -e OPENAI_API_KEY="sk-..." \
  -v $(pwd)/flows:/app/flows \
  logspace/langflow
```

### Production Deployment
Zie `ARCHITECTURE.md` sectie "Deployment Considerations" voor:
- Kubernetes deployment
- Cloud hosting (AWS, Azure, GCP)
- Scaling strategies
- Monitoring & logging

### Batch Processing
```python
from langflow import load_flow_from_json

# Load de flow
flow = load_flow_from_json("consultant-recommender.json")

# Process meerdere klanten
customers = [...]  # Your customer data
for customer in customers:
    result = flow.run(inputs={
        "customer_context": customer["context"],
        "problem_description": customer["problem"],
        "industry": customer["industry"]
    })
    print(result)
```

## Cost Tracking

**Per Run (met GPT-4):**
- Context Analyzer: ~€0.10-€0.20
- Service Recommender: ~€0.15-€0.25
- Best Practices: ~€0.15-€0.25
- Knowledge Base: ~€0.15-€0.25
- Proposal Synthesizer: ~€0.30-€0.45
- **Totaal: €0.85-€1.40 per complete run**

**Tips voor kosten besparing:**
1. Gebruik GPT-3.5-turbo voor non-critical agents (€0.10-€0.20 per run)
2. Cache Context Analyzer output voor dezelfde klant
3. Verlaag Max Tokens waar mogelijk
4. Gebruik Langflow's rate limiting

## Volgende Stappen

1. ✅ Test met alle 6 scenario's uit `example-input.yaml`
2. ✅ Pas system prompts aan naar je organisatie
3. ✅ Bouw je eigen service catalog in
4. ✅ Verzamel feedback van collega's
5. ✅ Itereer op basis van resultaten
6. ✅ Overweeg RAG integratie voor interne kennis
7. ✅ Setup API access voor integratie met andere tools

## Resources

- **Langflow Documentation**: https://docs.langflow.org/
- **Langflow GitHub**: https://github.com/logspace-ai/langflow
- **Example Inputs**: Zie `example-input.yaml` (6 uitgewerkte scenarios)
- **Full README**: Zie `README.md`
- **Architecture Details**: Zie `ARCHITECTURE.md`
- **Migration Guide**: Zie `LANGFLOW_MIGRATION.md`

## Support

Vragen? Check eerst:
1. De README.md voor uitgebreide documentatie
2. ARCHITECTURE.md voor technische details
3. Example inputs in example-input.yaml
4. Langflow documentation: https://docs.langflow.org/
5. Langflow Discord: https://discord.gg/EqksyE2EX9

Happy consulting! 🚀
