# Architecture Documentation

## Systeem Overzicht

Het AI Context Service Recommender systeem is gebouwd als een multi-agent workflow waarbij elke agent een gespecialiseerde rol heeft in het proces van klant analyse tot voorstel generatie.

## Agent Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    INPUT LAYER                               │
│  • Customer Context  • Problem Description  • Industry       │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│               CONTEXT ANALYZER AGENT                         │
│  Role: Extract structured insights from raw input            │
│  Output: Formatted analysis (needs, challenges, factors)     │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ├──────────────┬─────────────┐
                            ▼              ▼             ▼
┌─────────────────┐  ┌─────────────┐  ┌─────────────────────┐
│   SERVICE       │  │    BEST     │  │    KNOWLEDGE        │
│  RECOMMENDER    │  │  PRACTICES  │  │      BASE           │
│     AGENT       │  │    AGENT    │  │     AGENT           │
│                 │  │             │  │                     │
│ Parallel        │  │ Parallel    │  │ Parallel            │
│ Execution       │  │ Execution   │  │ Execution           │
└────────┬────────┘  └──────┬──────┘  └──────┬──────────────┘
         │                  │                 │
         └──────────────────┼─────────────────┘
                            ▼
┌─────────────────────────────────────────────────────────────┐
│           PROPOSAL SYNTHESIZER AGENT                         │
│  Role: Combine all agent outputs into coherent proposal      │
│  Output: Professional client proposal                        │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    OUTPUT LAYER                              │
│  • Final Proposal  • Services  • Best Practices  • Knowledge │
└─────────────────────────────────────────────────────────────┘
```

## Agent Specifications

### 1. Context Analyzer Agent

**Purpose:** Foundation agent that structures unstructured client information

**Input:**
- Raw customer context (free text)
- Problem description (free text)
- Industry classification

**Processing:**
- Information extraction
- Pattern recognition
- Maturity assessment
- Prioritization of needs

**Output Structure:**
```
**Klantbehoeften:**
- Need 1 (with context)
- Need 2 (with context)
...

**Uitdagingen:**
- Challenge 1 (with impact)
- Challenge 2 (with impact)
...

**Succesfactoren:**
- Factor 1
- Factor 2
...

**Organisatie Volwassenheid:**
- Assessment across dimensions
```

**Model Settings:**
- Temperature: 0.7 (balanced)
- Max Tokens: 2000
- Reasoning: Needs accuracy but also interpretation

### 2. Service Recommender Agent

**Purpose:** Match client needs to service catalog

**Dependencies:**
- Context Analyzer output (required)

**Decision Factors:**
- Client maturity level
- Problem complexity
- Resource constraints
- Timeline requirements
- Industry specifics

**Output Structure:**
```
Top 5 Recommended Services:

1. [Service Name]
   Relevantie Score: X/10
   Rationale: [Why this service fits]
   Verwachte Impact: [Business outcomes]
   Tijdlijn: [Estimated duration]

2. ...
```

**Model Settings:**
- Temperature: 0.6 (more consistent)
- Max Tokens: 2000
- Reasoning: Needs consistency in scoring

**Extensibility:**
- Service catalog is defined in system prompt
- Easy to customize per organization
- Can be connected to external service database

### 3. Best Practices Agent

**Purpose:** Recommend methodologies and frameworks

**Dependencies:**
- Context Analyzer output
- Service Recommender output

**Knowledge Domains:**
- Agile methodologies (Scrum, SAFe, Kanban)
- ITIL/ITSM
- DevOps/SRE
- Cloud frameworks (AWS WAF, Azure CAF)
- Security standards (ISO 27001, NIST)
- Architecture patterns

**Output Structure:**
```
Aanbevolen Best Practices:

1. [Framework/Practice Name]
   Toepassing: [How it applies]
   Implementatie: [Key considerations]
   Benefits: [Expected outcomes]
   Risico's: [Watch-outs]

2. ...
```

**Model Settings:**
- Temperature: 0.7 (balanced)
- Max Tokens: 2000

### 4. Knowledge Base Agent

**Purpose:** Provide experiential wisdom and case studies

**Dependencies:**
- Context Analyzer output
- Service Recommender output

**Knowledge Sources:**
- Historical project patterns
- Industry-specific insights
- Common pitfalls database
- Success factors from past engagements

**Output Structure:**
```
Relevante Ervaringskennis:

**Vergelijkbare Cases:**
- Case 1: [Description + outcomes]
- Case 2: [Description + outcomes]

**Key Lessons Learned:**
- Lesson 1: [Context + learning]
- Lesson 2: [Context + learning]

**Potentiële Uitdagingen:**
- Challenge 1: [Description + mitigation]
- Challenge 2: [Description + mitigation]

**Success Patterns:**
- Pattern 1: [What works well]
- Pattern 2: [What works well]
```

**Model Settings:**
- Temperature: 0.8 (more creative)
- Max Tokens: 2000
- Reasoning: Benefits from creative connections

**Future Enhancement:**
- RAG integration with vector database
- Organization-specific case study database
- Continuous learning from closed projects

### 5. Proposal Synthesizer Agent

**Purpose:** Create coherent, professional client proposal

**Dependencies:**
- ALL previous agent outputs (required)
- Original inputs (for context)

**Synthesis Tasks:**
- Information integration
- Narrative construction
- Prioritization and sequencing
- Risk/benefit balancing
- Professional formatting

**Output Structure:**
```
# KLANTVOORSTEL: [Client Name]

## 1. Executive Summary
[High-level overview + key recommendations]

## 2. Situatie Analyse
[Synthesized from Context Analyzer]

## 3. Aanbevolen Aanpak
[Strategic approach + reasoning]

## 4. Services & Deliverables
[From Service Recommender + details]

## 5. Methodologie & Best Practices
[From Best Practices Agent]

## 6. Ervaringskennis & Risk Mitigation
[From Knowledge Base Agent]

## 7. Success Metrics
[Measurable outcomes]

## 8. Timeline & Milestones
[Phased approach]

## 9. Next Steps
[Clear action items]
```

**Model Settings:**
- Temperature: 0.7
- Max Tokens: 4000 (longest output)
- Reasoning: Needs synthesis capability

## Data Flow

### Sequential Dependencies
```
Context Analyzer (MUST complete first)
    ↓
Service Recommender ──┐
Best Practices Agent ─┼─→ (Can run in parallel)
Knowledge Base Agent ─┘
    ↓
Proposal Synthesizer (MUST wait for all above)
```

### Parallel Execution
The three specialized agents (Service, Best Practices, Knowledge) can execute in parallel after Context Analyzer completes, reducing total execution time from ~120s to ~60s.

## Token Economics

### Per Agent Token Usage (Estimated)

| Agent | Input Tokens | Output Tokens | Total |
|-------|-------------|---------------|-------|
| Context Analyzer | 500-1000 | 800-1500 | 1300-2500 |
| Service Recommender | 1000-1500 | 800-1200 | 1800-2700 |
| Best Practices | 1500-2000 | 800-1200 | 2300-3200 |
| Knowledge Base | 1500-2000 | 800-1200 | 2300-3200 |
| Proposal Synthesizer | 3000-4000 | 2000-3000 | 5000-7000 |
| **TOTAL** | | | **12700-18600** |

### Cost Estimation (GPT-4)
- Input: $0.03 per 1K tokens
- Output: $0.06 per 1K tokens
- Average cost per run: **$0.85 - $1.40**

### Optimization Strategies
1. **Caching:** Reuse Context Analyzer output for iterations
2. **Model Selection:** Use GPT-3.5 for some agents to reduce cost
3. **Token Limits:** Stricter limits on input to avoid over-processing
4. **Prompt Optimization:** Shorter, more efficient prompts

## Performance Characteristics

### Latency
- Context Analyzer: 8-15s
- Parallel Agents: 10-20s (parallel execution)
- Proposal Synthesizer: 15-25s
- **Total: 33-60 seconds**

### Throughput
- Single workflow: 1-2 per minute
- Parallel workflows: Limited by API rate limits

### Scalability
- Bottleneck: LLM API rate limits
- Horizontal scaling: Run multiple Rivet instances
- Queue management: Implement job queue for high volume

## Error Handling

### Agent Failure Scenarios

1. **Context Analyzer Fails**
   - Impact: Pipeline cannot proceed
   - Mitigation: Retry with simplified prompt
   - Fallback: Manual context structuring

2. **Specialized Agent Fails**
   - Impact: Missing one dimension in final proposal
   - Mitigation: Continue with available agents
   - Fallback: Generic recommendations for failed agent

3. **Proposal Synthesizer Fails**
   - Impact: No final output
   - Mitigation: Retry with reduced token limit
   - Fallback: Present individual agent outputs

### Input Validation

```javascript
// Pseudo-code for input validation
validate_input(customerContext, problemDescription, industry) {
  if (customerContext.length < 50)
    warn("Context may be too short for quality analysis")

  if (problemDescription.length < 50)
    warn("Problem description may be too vague")

  if (customerContext.length > 3000)
    warn("Context too long - may hit token limits")

  if (!industry || industry.length < 3)
    error("Industry must be specified")
}
```

## Security & Privacy

### Data Handling
- All inputs are sent to LLM API (OpenAI/Azure/etc.)
- No data is stored by default in Rivet
- Logs may contain customer information

### Recommendations
1. Use Azure OpenAI for EU data residency
2. Implement data anonymization pre-processing
3. Clear sensitive info before sending to LLM
4. Use organization-specific deployment for isolation

### Compliance Considerations
- GDPR: Customer data processing
- NDA: Confidential client information
- Export controls: Some AI models have restrictions

## Extension Points

### 1. Custom Knowledge Base
```
Knowledge Base Agent
    ↓
[Vector Database]
    - Internal case studies
    - Lessons learned docs
    - Project retrospectives
    - Client feedback
```

### 2. Budget Estimation Agent
```
Add new agent:
├─ Input: Services + estimated effort
├─ Processing: Pricing model + historical data
└─ Output: Budget range + breakdown
```

### 3. CRM Integration
```
Pre-processing:
[Salesforce/HubSpot] → Extract account data → Input Layer

Post-processing:
Output Layer → Format + Attach → [CRM System]
```

### 4. Feedback Loop
```
User rates proposal quality
    ↓
Feedback stored
    ↓
Periodic retraining of prompts
    ↓
Improved recommendations
```

## Monitoring & Observability

### Key Metrics to Track
1. **Quality Metrics**
   - User satisfaction score (1-5)
   - Proposal acceptance rate
   - Time saved vs manual creation

2. **Performance Metrics**
   - End-to-end latency
   - Per-agent execution time
   - Token usage per run
   - Cost per proposal

3. **Reliability Metrics**
   - Success rate (%)
   - Agent failure rate
   - Retry frequency
   - Error types distribution

### Logging Strategy
```
Log levels:
- INFO: Workflow start/complete
- DEBUG: Each agent input/output
- WARN: Unusual patterns (too short input, etc.)
- ERROR: Agent failures, API errors
```

## Testing Strategy

### Unit Testing (Per Agent)
- Test each agent with fixed inputs
- Verify output structure
- Check edge cases (empty input, very long input)

### Integration Testing
- Test full workflow end-to-end
- Verify data flow between agents
- Check parallel execution

### Quality Testing
- Human evaluation of proposals
- A/B testing different prompts
- Comparison with manually created proposals

## Deployment Considerations

### Development Environment
- Local Rivet installation
- Development API keys
- Sample test data

### Production Environment
- Shared Rivet instance or API deployment
- Production API keys with rate limits
- Input validation and sanitization
- Output storage and retrieval
- User access control

### Scaling Considerations
1. **Vertical:** More powerful API tier (higher rate limits)
2. **Horizontal:** Multiple Rivet instances behind load balancer
3. **Caching:** Cache context analysis for similar customers
4. **Batch Mode:** Queue multiple requests for off-peak processing

## Future Roadmap

### Phase 1 (Current)
- ✅ Basic multi-agent workflow
- ✅ 5 specialized agents
- ✅ Dutch language support
- ✅ Manual input via Rivet UI

### Phase 2 (Next 3 months)
- [ ] Web interface for easy access
- [ ] Vector database integration for knowledge base
- [ ] Export to Word/PDF
- [ ] Multi-language support
- [ ] User feedback collection

### Phase 3 (6-12 months)
- [ ] Budget estimation agent
- [ ] CRM integration (Salesforce, HubSpot)
- [ ] A/B testing framework for prompt optimization
- [ ] Analytics dashboard
- [ ] API for programmatic access

### Phase 4 (Long-term)
- [ ] Fine-tuned models on organization data
- [ ] Real-time collaboration features
- [ ] Version control for proposals
- [ ] Template management system
- [ ] Automated follow-up recommendations

## References

- Rivet Documentation: https://rivet.ironcladapp.com/docs
- Multi-agent systems: https://arxiv.org/abs/2308.08155
- Prompt engineering best practices: https://platform.openai.com/docs/guides/prompt-engineering

---

**Document Version:** 1.0
**Last Updated:** 2025-10-29
**Maintained By:** Development Team
