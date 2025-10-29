# Quick Start Guide

Kom snel aan de slag met het AI Service Recommendation Flow systeem.

## 5-Minuten Setup

### Stap 1: Installeer Dependencies
```bash
pip install -r requirements.txt
```

### Stap 2: Configureer API Key
```bash
# Kopieer example naar .env
cp .env.example .env

# Edit .env en voeg je Anthropic API key toe
# ANTHROPIC_API_KEY=sk-ant-...
```

### Stap 3: Start LangFlow
```bash
langflow run
```

Dit opent LangFlow UI op http://localhost:7860

### Stap 4: Importeer de Flow
1. Open http://localhost:7860 in je browser
2. Klik op "New Flow" → "Import"
3. Selecteer `ai_service_recommendation_flow.json`
4. Flow is nu geladen en klaar voor gebruik!

### Stap 5: Test met Voorbeeld Data
```bash
python run_flow.py \
  --context-file examples/customer_context.txt \
  --problem-file examples/problem_description.txt
```

## Gebruik via UI

1. Open de geïmporteerde flow in LangFlow
2. Vul de twee input velden in:
   - **Customer Context Input**: Plak de inhoud van `examples/customer_context.txt` of schrijf je eigen context
   - **Problem Description Input**: Plak de inhoud van `examples/problem_description.txt` of beschrijf het probleem

3. Klik op "Run Flow" (▶️ button rechtsboven)

4. Wacht 30-120 seconden terwijl de agenten werken

5. Bekijk outputs:
   - **Final Proposal Output**: Het gegenereerde klantvoorstel
   - **Metadata & Analytics Output**: Analyse data en quality scores

## Gebruik via CLI

### Interactieve Modus
```bash
python run_flow.py --interactive
```
Volg de prompts om context en probleem te beschrijven.

### Direct met Argumenten
```bash
python run_flow.py \
  --customer-context "Uw klantcontext hier..." \
  --problem "Uw probleem hier..." \
  --output mijn_voorstel.json
```

### Met Input Bestanden
```bash
python run_flow.py \
  --context-file path/to/context.txt \
  --problem-file path/to/problem.txt \
  --output output/proposal.json
```

## Eerste Test: Gebruik Voorbeeld Data

We hebben complete voorbeeld input klaar staan:

```bash
# Test met voorbeeld financial services case
python run_flow.py \
  --context-file examples/customer_context.txt \
  --problem-file examples/problem_description.txt \
  --output my_first_proposal.json
```

Dit genereert een volledig voorstel voor een fictieve financial services klant met legacy modernisatie problemen.

## Aanpassen voor Eigen Gebruik

### Services Catalogus Aanpassen

Edit `ai_service_recommendation_flow.json`, zoek naar de "Service Matcher Agent" node en pas de `system_message` aan:

```json
{
  "system_message": "Je bent een service matching expert. Op basis van de klantcontext en problematiek, identificeer je:\n\n**Beschikbare Services:**\n- [VOEG HIER JE EIGEN SERVICES TOE]\n..."
}
```

### Eigen Best Practices Toevoegen

Zoek de "Best Practices Agent" node en update de categories en practices in de `system_message`.

### Temperature en Creativiteit Aanpassen

Voor elke agent kun je de temperature aanpassen:
- `0.1-0.3`: Zeer consistent, deterministisch (goed voor analyse)
- `0.4-0.6`: Gebalanceerd (goed voor recommendations)
- `0.7-0.9`: Meer creativiteit (goed voor writing, maar kan inconsistent zijn)

## Verwachte Output

Na het runnen van de flow krijg je:

### 1. Final Proposal (Markdown)
Een volledig gestructureerd voorstel met:
- Executive Summary
- Situatie Analyse
- Aanbevolen Services en Aanpak
- Best Practices
- Ervaringskennis
- Verwachte Resultaten en KPIs
- Volgende Stappen

### 2. Metadata (JSON)
```json
{
  "context_analysis": {
    "industrie": "...",
    "bedrijfsgrootte": "...",
    "maturiteit": "..."
  },
  "recommended_services": [...],
  "quality_score": 8.5
}
```

## Troubleshooting

### "API Key Error"
→ Check `.env` file en zorg dat ANTHROPIC_API_KEY correct is

### "LangFlow not found"
→ Run `pip install langflow`

### "Flow takes too long"
→ Normaal! Complexe flows kunnen 1-2 minuten duren
→ Zie de logs in LangFlow UI voor progress

### "Quality score is low (< 7)"
→ Input is mogelijk te vaag of kort
→ Geef meer specifieke details over de klant en probleem

### "Connection refused to localhost:7860"
→ LangFlow is niet running
→ Run `langflow run` in een separate terminal

## Next Steps

1. **Experimenteer met verschillende inputs**: Probeer verschillende industrieën en problemen
2. **Pas de flow aan**: Voeg je eigen services en best practices toe
3. **Integreer in je workflow**: Gebruik de Python API om het te integreren in je tools
4. **Lees de architectuur**: Zie `docs/architecture.md` voor diepgaande technische details
5. **Optimaliseer prompts**: Fine-tune de agent prompts voor betere resultaten

## Common Use Cases

### Use Case 1: Snel Voorstel voor Sales Pitch
```bash
# Snelle eerste draft voor sales team
python run_flow.py -i  # interactive mode
# Kopieer output naar Google Docs/Word voor final editing
```

### Use Case 2: Batch Processing
```python
# process_multiple.py
from run_flow import ServiceRecommendationFlow

runner = ServiceRecommendationFlow()

contexts = [
  ("customer1_context.txt", "customer1_problem.txt"),
  ("customer2_context.txt", "customer2_problem.txt"),
  # ...
]

for ctx_file, prob_file in contexts:
    with open(ctx_file) as f1, open(prob_file) as f2:
        result = runner.run_flow(f1.read(), f2.read())
        # Save result...
```

### Use Case 3: API Integration
```python
# Integreer in je bestaande applicatie
import requests

response = requests.post(
    "http://localhost:7860/api/v1/run/<flow-id>",
    json={
        "inputs": {
            "customer_context": get_customer_context_from_crm(),
            "problem_description": get_problem_from_ticket()
        }
    }
)

proposal = response.json()['outputs']['final_output']
send_to_sales_team(proposal)
```

## Tips voor Beste Resultaten

1. **Wees specifiek**: Meer detail = betere aanbevelingen
2. **Kwantificeer**: Gebruik cijfers (budget, team size, timelines)
3. **Context is key**: Industrie, bedrijfsgrootte, maturiteit zijn belangrijk
4. **Review altijd**: De AI genereert drafts, jij doet final review
5. **Itereer**: Run meerdere keren met verschillende inputs als je niet tevreden bent

## Support

- **Documentatie**: Zie `README.md` voor volledige docs
- **Architectuur**: Zie `docs/architecture.md` voor technische details
- **Voorbeelden**: Zie `examples/` directory voor meer voorbeelden

Veel succes met het systeem! 🚀
