# Quick Start Guide - AI Context Service Recommender

## 5 Minuten Setup

### Stap 1: Download & Installeer Rivet
1. Ga naar https://rivet.ironcladapp.com/
2. Download Rivet voor je platform (Windows/Mac/Linux)
3. Installeer de applicatie

### Stap 2: Open het Project
1. Start Rivet
2. Klik op "Open Project"
3. Selecteer `consultant-recommender.rivet-project`

### Stap 3: Configureer LLM Settings
1. Klik op het settings icoon (⚙️) in Rivet
2. Ga naar "Plugins" of "Settings"
3. Voeg je OpenAI API key toe:
   ```
   API Key: sk-...your-key...
   Model: gpt-4
   ```

   **Alternatieven:**
   - Azure OpenAI: Configureer endpoint + API key
   - Anthropic Claude: Als je Claude wilt gebruiken
   - Local models: Via Ollama of LM Studio

### Stap 4: Test met Voorbeeld Data
1. Klik op de "Play" button (▶️) om de workflow te starten
2. Vul de test inputs in (zie hieronder)
3. Bekijk de outputs aan de rechterkant

**Test Input:**
```yaml
customerContext: "Een middelgrote bank met 500 medewerkers en legacy Java applicaties."

problemDescription: "Lange time-to-market (6-12 maanden) en hoge kosten. Willen digitaal transformeren."

industry: "Financial Services"
```

### Stap 5: Bekijk de Resultaten
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

💡 **Tip:** Gebruik `example-input.yaml` als template

### 2. Run de Workflow
1. Plak de klant informatie in de 3 input velden
2. Klik "Run" (▶️)
3. Wacht 30-60 seconden

### 3. Review & Refine
1. Lees de gegenereerde outputs door
2. Check of de aanbevelingen kloppen
3. Pas aan waar nodig
4. Gebruik als basis voor klantgesprek

## Tips voor Beste Resultaten

### ✅ DO's:
- Wees zo specifiek mogelijk in de input
- Vermeld concrete cijfers (team grootte, budget, impact)
- Noem de huidige tech stack
- Beschrijf constraints (tijd, budget, compliance)
- Geef context over het team en hun vaardigheden

### ❌ DON'Ts:
- Generieke input ("een bedrijf dat wil digitaliseren")
- Te kort of te lang (sweet spot: 100-300 woorden per veld)
- Vage problemen zonder business impact
- Jargon zonder uitleg

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
customerContext: "Kopieer relevante delen uit de RFP"
problemDescription: "Vat de requirements samen"
industry: "Uit RFP"
```
➡️ Gebruik als eerste draft van je proposal

### Scenario 3: Discovery Workshop Voorbereiding
```yaml
customerContext: "Wat je tot nu toe weet uit pre-sales"
problemDescription: "Hun initiële vraag/probleem"
industry: "Hun sector"
```
➡️ Gebruik om je voor te bereiden met relevante vragen en frameworks

## Aanpassen van het Systeem

### Je Eigen Services Toevoegen
1. Open `consultant-recommender.rivet-project` in een text editor
2. Zoek naar "service-recommender-agent"
3. Pas de `systemPrompt` aan met je eigen service catalog:

```json
"Service categorieën:\n
- Jouw Service 1\n
- Jouw Service 2\n
- etc."
```

### Temperature Aanpassen
Voor meer creatieve/conservatieve output:
- Zoek naar `"temperature": 0.7`
- Verlaag (0.3-0.5) voor meer consistente output
- Verhoog (0.8-0.9) voor meer creatieve output

### Andere Taal
Pas alle `systemPrompt` en `prompt` velden aan naar Engels, Frans, etc.

## Troubleshooting

**"API Key invalid"**
- Check of je key correct is ingevoerd
- Verify dat je account actief is en credits heeft

**"Timeout error"**
- Je input is mogelijk te lang
- Verhoog `maxTokens` in de agent settings
- Of splits je input op

**"Output is te generiek"**
- Voeg meer specifieke details toe aan je input
- Vermeld concrete tech stack en constraints
- Geef concrete cijfers over impact

**"Output is te technisch voor mijn klant"**
- Pas de system prompt aan van Proposal Generator Agent
- Voeg toe: "Schrijf voor een non-technical audience"

## Volgende Stappen

1. ✅ Test met 2-3 verschillende scenario's
2. ✅ Pas system prompts aan naar je organisatie
3. ✅ Bouw je eigen service catalog in
4. ✅ Verzamel feedback van collega's
5. ✅ Itereer op basis van resultaten

## Resources

- **Rivet Documentation**: https://rivet.ironcladapp.com/docs
- **Example Inputs**: Zie `example-input.yaml`
- **Full README**: Zie `README.md`

## Support

Vragen? Check eerst:
1. De README.md voor uitgebreide documentatie
2. Example inputs in example-input.yaml
3. Rivet's eigen documentation

Happy consulting! 🚀
