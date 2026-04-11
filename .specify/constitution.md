# Constitution

## Purpose

DanskPensionsAnalyse udvikles som en sikker, lokal-først pensionsanalytiker for private brugere i Danmark.

## Core principles

### 1. Privacy first
- Umaskeret PII må ikke sendes til eksterne LLM-tjenester.
- Al ekstern modeltrafik skal gå gennem et sanitiseringslag.
- Audit må kun indeholde saniteret input og output.

### 2. Explainability over confidence
- Systemet skal forklare antagelser, usikkerheder og begrænsninger.
- Hvis data er uklare eller mangler, skal systemet sige det tydeligt.
- Svar må ikke fremstilles som juridisk bindende rådgivning.

### 3. Rule-assisted AI
- Regelbaseret behandling skal bruges, hvor domænelogik er kendt.
- LLM bruges til strukturering, forklaring og sproglig hjælp; ikke som eneste sandhedskilde.
- Beregninger og klassifikationer skal kunne spores til inputdata eller regler.

### 4. Modular architecture
- Dokumentparsing, normalisering, privacy, scenariemotor og UI skal være adskilte moduler.
- Nye dokumenttyper og pensionsselskaber skal kunne tilføjes uden at omskrive hele systemet.

### 5. Local-first workflow
- Første version skal kunne køres lokalt.
- Persistens af rå persondata skal undgås som standard.
- Udvikling og test skal kunne ske på anonymiserede eller syntetiske data.

### 6. Danish domain clarity
- Systemet skal bruge danske begreber konsekvent.
- Ordninger, forsikringer og skatteforhold skal beskrives i klart dansk.

## Delivery standards
- Alle features skal have en tydelig specifikation, plan og task-opdeling.
- Alle privacykritiske flows skal testes.
- Alle LLM-kald skal gå gennem én fælles adapter.
