# AI Context Service Recommender

Een AI-gestuurd systeem dat automatisch relevante services, best practices en ervaringskennis aanreikt op basis van klantcontext en problematiek, waardoor consultants sneller en accurater klantvoorstellen kunnen genereren.

## Overzicht

Dit systeem gebruikt een multi-agent architectuur gebouwd met Langflow om:
- Klantcontext te analyseren
- Relevante consultancy services aan te bevelen
- Best practices en frameworks voor te stellen
- Ervaringskennis en case studies te delen
- Complete klantvoorstellen te genereren

## Architectuur

Het systeem bestaat uit 5 gespecialiseerde AI agents:

### 1. Context Analyzer Agent
**Functie:** Analyseert de klantcontext en extraheert key insights
- Identificeert klantbehoeften en doelen
- Herkent uitdagingen en beperkingen
- Bepaalt kritische succesfactoren
- Schat organisatie volwassenheidsniveau in

### 2. Service Recommender Agent
**Functie:** Beveelt relevante consultancy services aan
- Matcht klantbehoeften met service catalog
- Geeft relevantie scores (1-10)
- Verklaart rationale voor elke aanbeveling
- Schat verwachte impact en tijdlijn

**Service Categorieën:**
- Digital Transformation
- Cloud Migration & Modernization
- Data & Analytics
- AI/ML Implementation
- DevOps & Automation
- Cybersecurity
- Application Development
- Infrastructure Optimization
- Change Management
- Organizational Design

### 3. Best Practices Agent
**Functie:** Adviseert over best practices en frameworks
- Agile/Scrum/SAFe methodologieën
- ITIL/ITSM frameworks
- DevOps/SRE practices
- Cloud adoption frameworks (AWS WAF, Azure CAF, Google Cloud)
- Security frameworks (ISO 27001, NIST, CIS)
- Architecture patterns

### 4. Knowledge & Experience Agent
**Functie:** Deelt relevante ervaringskennis
- Vergelijkbare case studies
- Lessons learned van eerdere projecten
- Common pitfalls en mitigatie strategieën
- Success patterns
- Industry-specifieke inzichten

### 5. Proposal Generator Agent
**Functie:** Synthetiseert alle informatie tot een compleet voorstel

**Output Structuur:**
1. Executive Summary
2. Situatie Analyse
3. Aanbevolen Aanpak
4. Services & Deliverables
5. Best Practices & Methodologie
6. Risk Mitigation
7. Success Metrics
8. Timeline & Milestones
9. Next Steps

## Installatie & Gebruik

### Vereisten
- [Langflow](https://www.langflow.org/) (installeer via `pip install langflow`)
- OpenAI API key of Azure OpenAI endpoint

### Setup
1. Installeer Langflow: `pip install langflow`
2. Start Langflow: `langflow run`
3. Importeer `consultant-recommender.json` via de Langflow UI
4. Configureer je OpenAI API key in de agent nodes
5. Test de workflow met voorbeelddata uit `example-input.yaml`

### Input Parameters

Het systeem verwacht 3 input parameters:

**1. customerContext**
```
Beschrijving van de klant organisatie, hun huidige situatie,
technologie stack, team grootte, etc.
```

**2. problemDescription**
```
Gedetailleerde beschrijving van de problematiek of uitdaging
waar de klant mee worstelt.
```

**3. industry**
```
De sector/industrie waarin de klant opereert
(bijv. "Financial Services", "Retail", "Healthcare")
```

### Voorbeeld Input

```yaml
customerContext: |
  Een middelgrote bank met 500 medewerkers die nog grotendeels
  on-premise infrastructure heeft. Ze hebben een legacy monolithische
  applicatie voor hun core banking, gebouwd in Java. Het team bestaat
  uit 20 developers die vooral waterfall gewend zijn.

problemDescription: |
  De bank wil digitaal transformeren om beter te kunnen concurreren
  met fintechs. Ze hebben last van lange time-to-market voor nieuwe
  features (6-12 maanden), hoge operational costs, en beperkte
  schaalbaarheid. Ook willen ze AI gebruiken voor fraud detection
  en customer insights.

industry: "Financial Services"
```

### Output

Het systeem genereert 4 outputs:

1. **Final Proposal** - Compleet klantvoorstel klaar voor review
2. **Recommended Services** - Gedetailleerde service aanbevelingen met scores
3. **Best Practices** - Appliceerbare best practices en frameworks
4. **Knowledge & Experience** - Relevante case studies en lessons learned

## Workflow Visualisatie

```
┌─────────────────┐
│ Input: Context  │
│ Input: Problem  │───┐
│ Input: Industry │   │
└─────────────────┘   │
                      ▼
              ┌───────────────────┐
              │ Context Analyzer  │
              │      Agent        │
              └─────────┬─────────┘
                        │
            ┌───────────┼───────────┐
            │           │           │
            ▼           ▼           ▼
    ┌──────────┐ ┌──────────┐ ┌──────────┐
    │ Service  │ │   Best   │ │Knowledge │
    │Recomm.   │ │Practices │ │  Base    │
    │  Agent   │ │  Agent   │ │  Agent   │
    └────┬─────┘ └────┬─────┘ └────┬─────┘
         │            │            │
         └────────────┼────────────┘
                      ▼
              ┌───────────────┐
              │   Proposal    │
              │  Synthesizer  │
              │     Agent     │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Final Outputs │
              └───────────────┘
```

## Aanpassing & Extensies

### Custom Services Toevoegen
Pas de system prompt van de Service Recommender Agent aan om je eigen service catalog toe te voegen.

### Knowledge Base Integratie
Verbind de Knowledge Base Agent met een vector database of RAG systeem voor organisatie-specifieke kennis.

### Extra Agents
Voeg extra gespecialiseerde agents toe voor:
- Budget estimation
- Resource planning
- Risk assessment
- Compliance checking

### Model Configuratie
Pas per agent de volgende parameters aan:
- `model`: GPT-4, Claude, of andere LLMs
- `temperature`: Creativiteit vs consistentie (0.0-1.0)
- `maxTokens`: Output lengte limiet

## Best Practices voor Gebruik

1. **Specifieke Input**: Hoe gedetailleerder de input, hoe beter de aanbevelingen
2. **Iteratief Proces**: Gebruik de output als startpunt en verfijn verder met de klant
3. **Human Review**: Valideer altijd de gegenereerde voorstellen voordat je ze naar klanten stuurt
4. **Feedback Loop**: Verzamel feedback op de kwaliteit van aanbevelingen om het systeem te verbeteren
5. **Customization**: Pas system prompts aan op basis van je organisatie's specifieke services en ervaring

## Technische Details

### Model Settings
- **Default Model**: GPT-4
- **Temperature Range**: 0.6-0.8 (balanced creativity)
- **Max Tokens**: 2000-4000 per agent
- **Prompts**: Nederlands (aanpasbaar naar andere talen)

### Performance
- Geschatte runtime: 30-60 seconden voor volledige workflow
- Parallel execution: Service, Best Practices en Knowledge agents kunnen parallel draaien
- Token efficiency: ~12700-18600 tokens per complete run
- Geschatte kosten: €0.85-€1.40 per run (met GPT-4)

## Troubleshooting

**Probleem:** Agent geeft generieke aanbevelingen
- **Oplossing:** Verstrek meer specifieke context in de input

**Probleem:** Timeout errors
- **Oplossing:** Verhoog maxTokens of splits complexe inputs op

**Probleem:** Output te technisch/te oppervlakkig
- **Oplossing:** Pas temperature en system prompts aan per agent

## Roadmap

- [ ] Vector database integratie voor org-specifieke kennis
- [ ] Budget estimation agent
- [ ] Multi-language support
- [ ] Export naar Word/PDF
- [ ] Feedback & learning mechanisme
- [ ] Integration met CRM systemen

## Licentie

Dit project is beschikbaar voor intern gebruik binnen je organisatie.

## Contact & Support

Voor vragen of feedback over dit systeem, neem contact op met het development team.
