# Plan: Dansk pensionsanalytiker v0.1

## Architecture overview

Løsningen opdeles i fem lag:

1. Dokumentindtag og parsing
2. Normalisering og domænemodel
3. Privacy- og redaktionslag
4. Analyse- og scenariemotor
5. Brugergrænseflade og audit

## Proposed components

### 1. Document ingestion
- Upload eller lokal filindlæsning af PDF
- Tekstudtræk via PDF-parser
- Mulig senere OCR for scannede dokumenter

### 2. Domain model
- PensionPlan
- InsuranceCoverage
- TaxProfile
- ScenarioInput
- ScenarioResult

### 3. Privacy bridge
- Identifikation af direkte identifikatorer
- Maskering/redaktion før LLM-kald
- Auditlog af saniteret input/output

### 4. Analysis engine
- Regelbaseret klassifikation af ordninger
- Simpel scenarieudregning for indbetaling, alder og udbetalingsform
- Forklaringsgenerator for antagelser og usikkerheder

### 5. User interface
- Første version som CLI eller simpel lokal webapp
- Dansk spørgsmål/svar
- Visning af dokumentudtræk, klassifikation og scenarier

## Suggested stack

- Python
- pdfplumber eller pypdf til tekstudtræk
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
- Gem struktureret mellemresultat lokalt i hukommelsen

### M3 Domain classification
- Map dokumentudtræk til ordningstyper og forsikringer
- Etabler fælles intern model

### M4 Privacy and LLM interface
- Implementer PII-maskering
- Opret wrapper til LLM-kald
- Audit-log kun saniteret payload

### M5 Scenario engine
- Opret basale scenarieberegninger
- Forklar forskelle mellem scenarier

### M6 User-facing experience
- Simpel lokal grænseflade
- Spørgsmål/svar på dansk
- Forklaringer og antagelser

## Risks

- Uens dokumentformat på tværs af pensionsselskaber
- Kompleksitet i danske skatte- og pensionsregler
- Falsk sikkerhed hvis LLM-svar ikke er tydeligt afgrænset
- Overmaskering eller undermaskering af PII

## Technical principles

- Regelmotor før fri generering, hvor det er muligt
- LLM bruges til forklaring og struktureret ekstraktion, ikke som eneste sandhedskilde
- PII må ikke forlade systemet umaskeret
- Løsningen skal være modulær, så nye dokumenttyper kan tilføjes senere
