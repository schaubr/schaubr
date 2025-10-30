# Troubleshooting Guide

Dit document helpt bij het oplossen van veelvoorkomende problemen bij het gebruik van het AI Service Recommendation Flow systeem.

## Import Problemen

### "unhandled error: 'folder_name'" bij import

**Probleem:** LangFlow geeft een error over het ontbrekende 'folder_name' veld bij import.

**Oplossing:** Dit is opgelost in de nieuwste versie van het JSON bestand. Zorg ervoor dat je de laatste versie gebruikt:
- Het JSON bestand moet een `folder_name` veld bevatten (kan leeg zijn: `""`)
- De structuur moet `data.nodes` en `data.edges` bevatten
- Het veld `is_component` moet aanwezig zijn

**Alternatieve oplossing:** Bouw de flow handmatig in LangFlow:

1. Open LangFlow UI
2. Maak een nieuwe flow aan
3. Voeg de volgende components toe vanuit de sidebar:
   - 2x **Chat Input** nodes (voor Customer Context en Problem Description)
   - 10x **ChatAnthropic** nodes (voor de verschillende agents)
   - 1x **Chat Output** node (voor Final Output)
4. Configureer elke ChatAnthropic node met de juiste system prompts (zie JSON bestand)
5. Verbind de nodes zoals beschreven in de architectuur documentatie

### Import succesvol maar nodes zijn niet correct

**Probleem:** De flow importeert maar de nodes hebben geen configuratie.

**Oplossing:**
1. Na import, klik op elke ChatAnthropic node
2. Configureer de volgende velden:
   - **Anthropic API Key**: Voeg je API key toe
   - **Model Name**: `claude-3-5-sonnet-20241022`
   - **Temperature**: Zie per agent in JSON (meestal 0.3-0.6)
   - **Max Tokens**: Zie per agent in JSON (2000-4000)
   - **System Message**: Kopieer van JSON bestand

### "ChatAnthropic component not found"

**Probleem:** LangFlow kan de ChatAnthropic component niet vinden.

**Oplossing:**
1. Zorg dat `langchain-anthropic` is geïnstalleerd:
   ```bash
   pip install langchain-anthropic
   ```
2. Herstart LangFlow:
   ```bash
   langflow run
   ```
3. Als het probleem blijft, gebruik **OpenAI** component in plaats van ChatAnthropic en vervang later

## LangFlow Problemen

### LangFlow start niet

**Probleem:** `langflow run` geeft error of start niet op.

**Oplossing:**
```bash
# Check of langflow correct is geïnstalleerd
pip install --upgrade langflow

# Probeer met specifieke host en port
langflow run --host 127.0.0.1 --port 7860

# Check of de port niet al in gebruik is
lsof -i :7860  # Linux/Mac
netstat -ano | findstr :7860  # Windows
```

### "Connection refused" naar localhost:7860

**Probleem:** Browser kan niet verbinden met LangFlow.

**Oplossing:**
1. Check of LangFlow daadwerkelijk draait:
   ```bash
   ps aux | grep langflow  # Linux/Mac
   tasklist | findstr langflow  # Windows
   ```
2. Check firewall settings
3. Probeer `http://127.0.0.1:7860` in plaats van `localhost`
4. Check de LangFlow logs voor errors

### LangFlow UI is leeg na import

**Probleem:** Na import zie je geen nodes op het canvas.

**Oplossing:**
1. Zoom out met je muis scroll wheel
2. Klik op "Fit View" button (rechtsboven)
3. Check de viewport settings in het JSON (mogelijk verkeerde zoom level)

## API en Authentication Problemen

### "Invalid API key" error

**Probleem:** Anthropic API geeft authentication error.

**Oplossing:**
1. Verificeer je API key op https://console.anthropic.com/
2. Zorg dat de key niet verlopen is
3. Check of je usage limits niet overschreden zijn
4. Zorg dat de key correct is ingevuld in elke ChatAnthropic node
5. Als je .env gebruikt, check dat de environment variable correct geladen wordt:
   ```bash
   echo $ANTHROPIC_API_KEY  # Linux/Mac
   echo %ANTHROPIC_API_KEY%  # Windows
   ```

### "Rate limit exceeded"

**Probleem:** Te veel API requests te snel.

**Oplossing:**
1. Wacht 60 seconden en probeer opnieuw
2. Verhoog je rate limit tier bij Anthropic
3. Implementeer caching voor herhaalde queries
4. Reduceer aantal parallelle agent calls

### "Model not found: claude-3-5-sonnet-20241022"

**Probleem:** Het model is niet beschikbaar.

**Oplossing:**
1. Check of je Anthropic account toegang heeft tot dit model
2. Gebruik een alternatief model:
   - `claude-3-opus-20240229` (meest capabel)
   - `claude-3-sonnet-20240229` (gebalanceerd)
   - `claude-3-haiku-20240307` (snelst en goedkoopst)
3. Update het model_name veld in alle agent nodes

## Runtime Problemen

### Flow execution timeout

**Probleem:** De flow duurt te lang en timed out.

**Oplossing:**
1. Dit is normaal voor complexe flows met veel agents (kan 2-3 minuten duren)
2. Verhoog timeout in run_flow.py:
   ```python
   response = requests.post(..., timeout=600)  # 10 minuten
   ```
3. Reduceer max_tokens voor agents die te veel tekst genereren
4. Verwijder optionele agents (zoals Experience Knowledge)

### Agents geven inconsistente output

**Probleem:** Output varieert sterk tussen runs met dezelfde input.

**Oplossing:**
1. Verlaag temperature settings (naar 0.1-0.2) voor meer consistentie
2. Voeg meer specifieke instructies toe aan system prompts
3. Gebruik structured output formats (JSON) waar mogelijk
4. Implementeer output validation

### "Out of memory" errors

**Probleem:** LangFlow crasht met memory errors.

**Oplossing:**
1. Reduceer max_tokens in de agents
2. Verhoog het geheugen beschikbaar voor Python:
   ```bash
   # Verhoog Python heap size (Linux/Mac)
   export PYTHONMAXMEM=4096
   ```
3. Run minder agents parallel
4. Restart LangFlow regelmatig bij intensief gebruik

### JSON parsing errors in agent outputs

**Probleem:** Agents geven geen valide JSON terug.

**Oplossing:**
1. Update system prompts om te benadrukken:
   ```
   BELANGRIJK: Geef ALLEEN valide JSON terug, zonder markdown formatting of extra tekst.
   ```
2. Voeg JSON validation toe in de flow
3. Gebruik een "JSON fixer" agent die invalide JSON repareert
4. Check of max_tokens niet te laag is (agent kan afgekapt worden mid-JSON)

## Flow Design Problemen

### Agents krijgen verkeerde inputs

**Probleem:** Een agent krijgt output van verkeerde voorgaande agent.

**Oplossing:**
1. Check de edges (verbindingen) in de flow
2. Zorg dat source en target handles correct zijn:
   - ChatInput → ChatAnthropic: `message` → `input_value`
   - ChatAnthropic → ChatAnthropic: `text` → `input_value`
   - ChatAnthropic → ChatOutput: `text` → `input_value`
3. Gebruik duidelijke node namen om verwarring te voorkomen

### Multiple inputs worden geconcateneerd

**Probleem:** Wanneer een agent meerdere inputs heeft, worden ze allemaal aan elkaar geplakt.

**Oplossing:**
1. Dit is normaal gedrag in LangFlow
2. Gebruik een "Prompt Template" node om inputs te structureren:
   ```
   Customer Context: {customer_context}

   Problem Analysis: {problem_analysis}

   Service Recommendations: {services}
   ```
3. Of gebruik een custom Python node om inputs te combineren

### Circular dependencies detected

**Probleem:** LangFlow detecteert een circulaire afhankelijkheid.

**Oplossing:**
1. Check je edges voor loops (A → B → C → A)
2. Herstructureer de flow zodat data altijd in één richting stroomt
3. Als je feedback loops nodig hebt, implementeer met conditional logic

## Python Script Problemen

### "ModuleNotFoundError: No module named 'langflow'"

**Probleem:** Python kan langflow niet vinden.

**Oplossing:**
```bash
pip install langflow
# Of gebruik een virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### "ConnectionRefusedError" in run_flow.py

**Probleem:** Script kan niet verbinden met LangFlow API.

**Oplossing:**
1. Zorg dat LangFlow draait (`langflow run`)
2. Check of de URL klopt in .env of script:
   ```python
   LANGFLOW_API_URL=http://localhost:7860
   ```
3. Check firewall/antivirus settings

### "Flow ID not found"

**Probleem:** De flow_id is niet correct.

**Oplossing:**
1. In LangFlow UI, klik op Settings → API
2. Kopieer de flow ID
3. Update de flow_id in je script of config
4. Of gebruik flow name in plaats van ID

## Performance Problemen

### Flow is te langzaam (>5 minuten)

**Probleem:** Execution duurt onacceptabel lang.

**Oplossing:**
1. Reduceer aantal agents (verwijder optionele zoals Experience Knowledge)
2. Verlaag max_tokens voor elke agent
3. Gebruik sneller model (claude-3-haiku)
4. Implementeer parallellisatie waar mogelijk
5. Cache herhaalde analyses

### High API costs

**Probleem:** Kosten lopen op door frequent gebruik.

**Oplossing:**
1. Implementeer caching voor herhaalde inputs
2. Gebruik goedkopere modellen waar mogelijk:
   - Analysis agents: Claude 3 Haiku ($0.25/$1.25 per 1M tokens)
   - Critical agents: Claude 3.5 Sonnet ($3/$15 per 1M tokens)
3. Batch vergelijkbare requests
4. Monitor usage via Anthropic console
5. Implementeer usage limits in je applicatie

## Handmatige Flow Setup

Als de JSON import blijft falen, hier is de stap-voor-stap handleiding om de flow handmatig te bouwen:

### Stap 1: Input Nodes
1. Add → Input → **Chat Input** (naam: "Customer Context Input")
2. Add → Input → **Chat Input** (naam: "Problem Description Input")

### Stap 2: Analysis Agents
3. Add → Models → **ChatAnthropic** (naam: "Context Analysis Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.3
   - Max Tokens: 2000

4. Add → Models → **ChatAnthropic** (naam: "Problem Analysis Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.3
   - Max Tokens: 2000

### Stap 3: Recommendation Agents
5. Add → Models → **ChatAnthropic** (naam: "Service Matcher Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.4
   - Max Tokens: 3000

6. Add → Models → **ChatAnthropic** (naam: "Best Practices Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.4
   - Max Tokens: 3000

7. Add → Models → **ChatAnthropic** (naam: "Experience Knowledge Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.5
   - Max Tokens: 3000

### Stap 4: Generation Agents
8. Add → Models → **ChatAnthropic** (naam: "Proposal Generator Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.6
   - Max Tokens: 4000

9. Add → Models → **ChatAnthropic** (naam: "Quality Review Agent")
   - System Message: [kopieer van JSON]
   - Temperature: 0.3
   - Max Tokens: 2000

10. Add → Models → **ChatAnthropic** (naam: "Proposal Refiner")
    - System Message: [kopieer van JSON]
    - Temperature: 0.5
    - Max Tokens: 4000

### Stap 5: Output Node
11. Add → Output → **Chat Output** (naam: "Final Proposal Output")

### Stap 6: Verbind de Nodes
Verbind volgens dit patroon (sleep van output handle naar input handle):

1. Customer Context Input → Context Analysis Agent
2. Problem Description Input → Problem Analysis Agent
3. Context Analysis Agent → Service Matcher Agent
4. Problem Analysis Agent → Service Matcher Agent
5. Context Analysis Agent → Best Practices Agent
6. Problem Analysis Agent → Best Practices Agent
7. Service Matcher Agent → Best Practices Agent
8. Context Analysis Agent → Experience Knowledge Agent
9. Problem Analysis Agent → Experience Knowledge Agent
10. Service Matcher Agent → Experience Knowledge Agent
11. Customer Context Input → Proposal Generator Agent
12. Problem Description Input → Proposal Generator Agent
13. Context Analysis Agent → Proposal Generator Agent
14. Problem Analysis Agent → Proposal Generator Agent
15. Service Matcher Agent → Proposal Generator Agent
16. Best Practices Agent → Proposal Generator Agent
17. Experience Knowledge Agent → Proposal Generator Agent
18. Proposal Generator Agent → Quality Review Agent
19. Proposal Generator Agent → Proposal Refiner
20. Quality Review Agent → Proposal Refiner
21. Proposal Refiner → Final Proposal Output

## Hulp Krijgen

Als je problemen blijft ervaren:

1. **Check de LangFlow logs**: `~/.langflow/langflow.log`
2. **Enable debug mode**:
   ```bash
   export LANGFLOW_LOG_LEVEL=DEBUG
   langflow run
   ```
3. **LangFlow Community**: https://github.com/logspace-ai/langflow/discussions
4. **Anthropic Support**: https://support.anthropic.com
5. **Create een GitHub Issue** met:
   - Error message (volledig)
   - LangFlow versie (`pip show langflow`)
   - Python versie (`python --version`)
   - OS en versie
   - Stappen om het probleem te reproduceren
