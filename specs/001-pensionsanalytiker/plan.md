# Plan: Dansk pensionsanalytiker v0.2

## Architecture overview

Løsningen opdeles i seks lag:

1. Dokumentindtag og parsing
2. Ekstraktionsobservation og kvalitetssignaler
3. Normalisering og domænemodel
4. Privacy- og redaktionslag
5. Analyse- og scenariemotor
6. Brugergrænseflade og audit

## Proposed components

### 1. Document ingestion
- Upload eller lokal filindlæsning af PDF
- Tekstudtræk via primær parser
- Mulighed for alternative ekstraktionsstrategier senere

### 2. Extraction observability
- Sidevis statistik over udtrukket tekst
- Markering af sider med tomt eller mistænkeligt lavt output
- Samlet vurdering af ekstraktionskvalitet pr. dokument

### 3. Domain model
- PensionPlan
- InsuranceCoverage
- TaxProfile
- ScenarioInput
- ScenarioResult
- ExtractionReport

### 4. Privacy bridge
- Identifikation af direkte identifikatorer
- Maskering/redaktion før LLM-kald
- Auditlog af saniteret input/output

### 5. Analysis engine
- Regelbaseret klassifikation af ordninger
- Simpel scenarieudregning for indbetaling, alder og udbetalingsform
- Forklaringsgenerator for antagelser og usikkerheder
- Respekt for ekstraktionskvalitet i svar og forklaringer

### 6. User interface
- Første version som CLI eller simpel lokal webapp
- Dansk spørgsmål/svar
- Visning af dokumentudtræk, klassifikation og scenarier
- Visning af ekstraktionsrapport og advarsler

## Suggested stack

- Python
- pypdf som første parser
- Mulighed for senere fallback-parser
- Pydantic til datamodeller
- FastAPI eller Streamlit til første UI
- Pytest til tests

## Milestones

### M1 Repository and project skeleton
- Opret Python-projektstruktur
- Opret tests
- Opret config for LLM-provider og privacy-lag

### M2 Document extraction
- Indlæs PDF
- Udtræk tekst og relevante sektioner
- Registrér sidevis output og kvalitetssignaler

### M3 Domain classification
- Map dokumentudtræk til ordningstyper og forsikringer
- Etabler fælles intern model
- Tag højde for delvist eller usikkert input

### M4 Privacy and LLM interface
- Implementer PII-maskering
- Opret wrapper til LLM-kald
- Audit-log kun saniteret payload

### M5 Scenario engine
- Opret basale scenarieberegninger
- Forklar forskelle mellem scenarier
- Begræns svar, hvis inputkvaliteten er lav

### M6 User-facing experience
- Simpel lokal grænseflade
- Spørgsmål/svar på dansk
- Forklaringer og antagelser
- Synlig ekstraktionsstatus

## Risks

- Uens dokumentformat på tværs af pensionsselskaber
- Kompleksitet i danske skatte- og pensionsregler
- Falsk sikkerhed hvis LLM-svar ikke er tydeligt afgrænset
- Overmaskering eller undermaskering af PII
- Tavse parserfejl, hvor nogle sider fejler uden tydelig fejlmeddelelse

## Technical principles

- Regelmotor før fri generering, hvor det er muligt
- LLM bruges til forklaring og struktureret ekstraktion, ikke som eneste sandhedskilde
- PII må ikke forlade systemet umaskeret
- Løsningen skal være modulær, så nye dokumenttyper kan tilføjes senere
- Ekstraktionskvalitet skal være en første-klasses del af datamodellen, ikke bare debug-output
