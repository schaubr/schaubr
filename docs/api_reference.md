# API Reference

Complete reference voor het gebruik van de AI Service Recommendation Flow via API's en programmatisch gebruik.

## LangFlow API

### Base URL
```
http://localhost:7860/api/v1
```

Voor LangFlow Cloud:
```
https://api.langflow.astra.datastax.com
```

### Authentication

Voor local instance: Geen authenticatie vereist

Voor LangFlow Cloud:
```http
Authorization: Bearer <your-langflow-token>
```

### Run Flow Endpoint

**POST** `/run/{flow_id}`

Voert een flow uit met de opgegeven inputs.

#### Request

```json
{
  "inputs": {
    "customer_context": "string",
    "problem_description": "string"
  },
  "tweaks": {
    "node_id": {
      "parameter": "value"
    }
  }
}
```

**Parameters:**
- `inputs` (required): Object met input waarden
  - `customer_context` (string, required): Klantcontext beschrijving
  - `problem_description` (string, required): Probleem beschrijving
- `tweaks` (optional): Runtime parameters voor specifieke nodes

#### Response

```json
{
  "outputs": {
    "final_output": "string (markdown formatted proposal)",
    "metadata_output": {
      "context_analysis": {...},
      "problem_analysis": {...},
      "recommended_services": [...],
      "quality_score": {...},
      "timestamp": "ISO 8601 timestamp"
    }
  },
  "session_id": "string",
  "flow_id": "string"
}
```

#### Example

```bash
curl -X POST http://localhost:7860/api/v1/run/YOUR_FLOW_ID \
  -H "Content-Type: application/json" \
  -d '{
    "inputs": {
      "customer_context": "Middelgroot retailbedrijf met 200 medewerkers...",
      "problem_description": "E-commerce platform is verouderd..."
    }
  }'
```

### Get Flow Info

**GET** `/flows/{flow_id}`

Haalt flow metadata op.

#### Response

```json
{
  "id": "string",
  "name": "AI Service Recommendation Flow",
  "description": "string",
  "data": {
    "nodes": [...],
    "edges": [...]
  }
}
```

## Python SDK

### ServiceRecommendationFlow Class

#### Initialization

```python
from run_flow import ServiceRecommendationFlow

runner = ServiceRecommendationFlow(
    langflow_url="http://localhost:7860",  # optional
    api_token=None  # optional, for LangFlow Cloud
)
```

**Parameters:**
- `langflow_url` (str, optional): LangFlow instance URL. Default: `http://localhost:7860`
- `api_token` (str, optional): API token voor authenticatie. Default: `None`

#### Methods

##### run_flow()

Voert de flow uit met gegeven inputs.

```python
result = runner.run_flow(
    customer_context="string",
    problem_description="string"
)
```

**Parameters:**
- `customer_context` (str, required): Klantcontext beschrijving
- `problem_description` (str, required): Probleem beschrijving

**Returns:**
- `dict`: Response object met outputs en metadata

**Raises:**
- `requests.exceptions.RequestException`: Bij API fouten

**Example:**
```python
result = runner.run_flow(
    customer_context="""
    Bedrijf: TechCorp
    Industrie: SaaS
    Grootte: 150 FTE
    Uitdaging: Legacy monolith naar microservices
    """,
    problem_description="""
    Huidige monolithische applicatie kan niet schalen.
    Development cycles zijn te lang.
    Deployment is risicovol en langzaam.
    """
)

proposal = result['outputs']['final_output']
quality = result['outputs']['metadata_output']['quality_score']

print(f"Generated proposal with quality score: {quality}")
print(proposal)
```

##### load_flow()

Laadt flow definitie van JSON bestand.

```python
flow_data = runner.load_flow(flow_path="path/to/flow.json")
```

**Parameters:**
- `flow_path` (str, optional): Pad naar flow JSON. Default: `ai_service_recommendation_flow.json`

**Returns:**
- `dict`: Flow definitie

##### run_flow_cli()

Interactieve CLI voor het runnen van de flow.

```python
runner.run_flow_cli()
```

Geen parameters. Vraagt gebruiker om input via stdin.

## CLI Reference

### run_flow.py

Command-line interface voor het runnen van de flow.

#### Usage

```bash
python run_flow.py [OPTIONS]
```

#### Options

##### Interactive Mode
```bash
-i, --interactive
```
Start interactive mode waar gebruiker via prompts input kan geven.

**Example:**
```bash
python run_flow.py --interactive
```

##### Direct Input
```bash
-c, --customer-context TEXT
```
Customer context als command-line argument.

```bash
-p, --problem TEXT
```
Problem description als command-line argument.

**Example:**
```bash
python run_flow.py \
  --customer-context "Middelgroot financieel bedrijf..." \
  --problem "Legacy systemen blokkeren innovatie..."
```

##### File Input
```bash
--context-file PATH
```
Pad naar bestand met customer context.

```bash
--problem-file PATH
```
Pad naar bestand met problem description.

**Example:**
```bash
python run_flow.py \
  --context-file examples/customer_context.txt \
  --problem-file examples/problem_description.txt
```

##### Output
```bash
-o, --output PATH
```
Output bestand pad voor resultaat (JSON format).

**Example:**
```bash
python run_flow.py \
  --context-file examples/customer_context.txt \
  --problem-file examples/problem_description.txt \
  --output results/proposal_20250129.json
```

## Agent Configuration Reference

### Model Parameters

Elke agent kan geconfigureerd worden met de volgende parameters in de flow JSON:

```json
{
  "model_name": "claude-3-5-sonnet-20241022",
  "api_key": "${ANTHROPIC_API_KEY}",
  "temperature": 0.3,
  "max_tokens": 2000,
  "top_p": 1.0,
  "top_k": -1,
  "system_message": "Agent system prompt..."
}
```

#### Parameters

**model_name** (string)
- Anthropic model identifier
- Options:
  - `claude-3-5-sonnet-20241022` (recommended)
  - `claude-3-opus-20240229`
  - `claude-3-haiku-20240307`
- Default: `claude-3-5-sonnet-20241022`

**temperature** (float, 0.0-1.0)
- Controls randomness in output
- Lower = more deterministic
- Higher = more creative
- Recommended:
  - Analysis agents: 0.3
  - Recommendation agents: 0.4-0.5
  - Generation agents: 0.6
- Default: 0.5

**max_tokens** (integer)
- Maximum tokens in response
- Range: 1-4096 (Claude 3.5 Sonnet)
- Recommended:
  - Analysis: 2000
  - Recommendations: 3000
  - Generation: 4000
- Default: 1024

**top_p** (float, 0.0-1.0)
- Nucleus sampling parameter
- Default: 1.0 (disabled)

**top_k** (integer)
- Top-k sampling parameter
- -1 = disabled
- Default: -1

**system_message** (string)
- System prompt defining agent behavior
- Critical for agent performance
- Should include:
  - Role definition
  - Task description
  - Output format specification
  - Guidelines and constraints

## Response Schema

### Final Output

```typescript
{
  final_output: string  // Markdown formatted proposal
}
```

**Structure:**
```markdown
# KLANTVOORSTEL: [Bedrijfsnaam]

## Executive Summary
...

## Situatie Analyse
...

## Voorgestelde Services en Aanpak
...

## Best Practices en Methodologie
...

## Ervaringskennis en Referenties
...

## Verwachte Resultaten en KPIs
...

## Volgende Stappen
...
```

### Metadata Output

```typescript
{
  metadata_output: {
    context_analysis: {
      industrie: string,
      bedrijfsgrootte: string,
      maturiteit: string,
      kernuitdagingen: string[],
      strategische_doelen: string[],
      technische_volwassenheid: string
    },
    problem_analysis: {
      kernproblemen: Array<{
        problem: string,
        root_cause: string,
        impact: string
      }>,
      urgentie: string,
      complexiteit: string
    },
    recommended_services: Array<{
      service: string,
      relevance: string,
      impact: string,
      complexity: string,
      timeline: string,
      priority: "hoog" | "medium" | "laag"
    }>,
    quality_review: {
      quality_score: number,  // 1-10
      strong_points: string[],
      attention_points: string[],
      improvements: string[],
      recommendation: "go" | "no-go"
    },
    timestamp: string  // ISO 8601
  }
}
```

## Error Handling

### Common Errors

#### API Key Error
```json
{
  "error": "Invalid API key",
  "code": "UNAUTHORIZED"
}
```
**Solution:** Check ANTHROPIC_API_KEY in .env

#### Timeout Error
```json
{
  "error": "Request timeout",
  "code": "TIMEOUT"
}
```
**Solution:** Increase timeout or simplify inputs

#### Validation Error
```json
{
  "error": "Invalid input",
  "code": "VALIDATION_ERROR",
  "details": {
    "field": "customer_context",
    "message": "Required field missing"
  }
}
```
**Solution:** Provide all required inputs

#### Rate Limit Error
```json
{
  "error": "Rate limit exceeded",
  "code": "RATE_LIMIT"
}
```
**Solution:** Wait and retry, or upgrade API plan

## Best Practices

### Input Optimization

1. **Structure your context:**
   ```
   Bedrijf: [Naam]
   Industrie: [Industrie]
   Grootte: [FTE, Revenue]
   Locatie: [Waar]

   Huidige Situatie:
   - [Punt 1]
   - [Punt 2]

   Doelen:
   - [Doel 1]
   - [Doel 2]
   ```

2. **Be specific in problem description:**
   - Include metrics
   - Mention impact
   - Specify constraints
   - Define success criteria

### Performance Optimization

1. **Reuse connections:**
   ```python
   runner = ServiceRecommendationFlow()
   for context, problem in inputs:
       result = runner.run_flow(context, problem)
   ```

2. **Batch processing:**
   ```python
   results = []
   for ctx_file, prob_file in file_pairs:
       result = runner.run_flow(
           open(ctx_file).read(),
           open(prob_file).read()
       )
       results.append(result)
   ```

3. **Async processing (future):**
   ```python
   # Future enhancement
   async with ServiceRecommendationFlow() as runner:
       tasks = [runner.run_flow_async(c, p) for c, p in inputs]
       results = await asyncio.gather(*tasks)
   ```

## Integration Examples

### CRM Integration (Salesforce)

```python
from simple_salesforce import Salesforce
from run_flow import ServiceRecommendationFlow

sf = Salesforce(username='...', password='...', security_token='...')
runner = ServiceRecommendationFlow()

# Get opportunity
opp = sf.Opportunity.get('006...')

# Extract context from CRM
context = f"""
Bedrijf: {opp['Account']['Name']}
Industrie: {opp['Account']['Industry']}
Grootte: {opp['Account']['NumberOfEmployees']} FTE
...
"""

problem = opp['Description']

# Generate proposal
result = runner.run_flow(context, problem)

# Update opportunity with proposal
sf.Opportunity.update(opp['Id'], {
    'AI_Generated_Proposal__c': result['outputs']['final_output']
})
```

### Slack Integration

```python
from slack_sdk import WebClient
from run_flow import ServiceRecommendationFlow

slack = WebClient(token=os.environ["SLACK_TOKEN"])
runner = ServiceRecommendationFlow()

@app.command("/generate-proposal")
def generate_proposal(ack, command, say):
    ack()

    # Run flow
    result = runner.run_flow(
        customer_context=command['text'],
        problem_description="..."  # from additional prompt
    )

    # Post to channel
    say(result['outputs']['final_output'])
```

### REST API Wrapper

```python
from fastapi import FastAPI
from run_flow import ServiceRecommendationFlow

app = FastAPI()
runner = ServiceRecommendationFlow()

@app.post("/api/generate-proposal")
async def generate_proposal(request: ProposalRequest):
    result = runner.run_flow(
        customer_context=request.customer_context,
        problem_description=request.problem_description
    )
    return result

# Run with: uvicorn api:app --reload
```

## Rate Limits & Costs

### Anthropic API Limits

- Claude 3.5 Sonnet:
  - Rate limit: 50 requests/minute (tier 1)
  - Context window: 200k tokens
  - Output: 8k tokens max

### Estimated Costs per Run

- Input tokens: ~5,000-10,000 → $0.015-0.030
- Output tokens: ~8,000-15,000 → $0.120-0.225
- **Total: ~$0.15-0.30 per proposal**

### Cost Optimization

1. Use prompt caching (future Anthropic feature)
2. Batch similar requests
3. Cache analysis results for similar contexts
4. Use smaller models for simple tasks

## Version Compatibility

- Python: 3.9+
- LangFlow: 0.6.0+
- Anthropic SDK: 0.18.0+
- Tested on: Linux, macOS, Windows

## Support & Resources

- **GitHub Issues**: [Report bugs and issues]
- **LangFlow Docs**: https://docs.langflow.org
- **Anthropic Docs**: https://docs.anthropic.com
- **Claude API Docs**: https://docs.anthropic.com/claude/reference
