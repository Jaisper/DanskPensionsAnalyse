# Tasks: Dansk pensionsanalytiker v0.2

## Phase 1: Bootstrap
- [x] Opret Python-projektstruktur med `src/` og `tests/`
- [x] Tilføj dependencies til PDF-parsing, datamodeller og test
- [x] Opret basis README med lokal kørsel

## Phase 2: Document parsing
- [x] Implementer modul til at læse PDF-filer
- [ ] Udvid parseren, så den returnerer sidevis ekstraktionsdata
- [ ] Definér et `ExtractionReport`-objekt med samlet status og sidevis statistik
- [ ] Markér sider med tomt eller mistænkeligt lavt output
- [ ] Skriv tests for dokumenter, hvor nogle sider giver tekst og andre ikke gør

## Phase 3: Normalization
- [ ] Definér datamodeller for ordninger, forsikringer, scenarier og ekstraktionsstatus
- [ ] Implementer parser, der mapper rå tekst til interne modeller
- [ ] Markér usikre felter og manglende data
- [ ] Lad downstream-komponenter kende forskel på komplet og delvis ekstraktion

## Phase 4: Privacy
- [x] Implementer PII-detektor for CPR, e-mail og telefon
- [ ] Udvid PII-detektor med navn, adresse og kontonumre
- [x] Implementer maskering/redaktion før LLM-kald
- [ ] Implementer auditlog af saniteret prompt og svar
- [x] Skriv tests, der beviser at rå PII ikke sendes videre

## Phase 5: Q&A
- [ ] Implementer spørgeinterface på dansk
- [ ] Opret prompt-template med tydelige begrænsninger
- [ ] Tilføj forklaringer med antagelser og usikkerheder
- [ ] Sørg for at svar nævner, hvis dokumentgrundlaget er delvist

## Phase 6: Scenario engine
- [ ] Definér inputmodel for scenarier
- [ ] Implementer første scenarier for ændret indbetaling og pensionsalder
- [ ] Returnér både tal og forklaringer
- [ ] Blokér eller nedton scenariesvar ved utilstrækkeligt inputgrundlag

## Phase 7: UX
- [ ] Byg en simpel CLI eller lokal webapp
- [ ] Vis udtrukne ordninger og forsikringer
- [ ] Vis hvad der er maskeret før LLM-kald
- [ ] Vis audit-log for saniteret trafik
- [ ] Vis ekstraktionsstatus pr. dokument og side

## Definition of done
- [ ] Systemet kan indlæse mindst ét pensionsdokument
- [ ] Systemet kan forklare, om dokumentet er fuldt, delvist eller usikkert udtrukket
- [ ] Systemet kan udtrække mindst én pensionsordning og én forsikringsdækning
- [ ] Systemet kan besvare mindst ét spørgsmål på dansk om dokumentet
- [ ] Systemet dokumenterer, at umaskeret PII ikke sendes til LLM
