# Tasks: Dansk pensionsanalytiker v0.1

## Phase 1: Bootstrap
- [ ] Opret Python-projektstruktur med `src/` og `tests/`
- [ ] Tilføj dependencies til PDF-parsing, datamodeller og test
- [ ] Opret basis README med lokal kørsel

## Phase 2: Document parsing
- [ ] Implementer modul til at læse PDF-filer
- [ ] Ekstraher rå tekst fra PensionsInfo-rapport
- [ ] Ekstraher rå tekst fra pensionsselskabsoversigt
- [ ] Skriv tests med eksempeldokumenter

## Phase 3: Normalization
- [ ] Definér datamodeller for ordninger, forsikringer og scenarier
- [ ] Implementer parser, der mapper rå tekst til interne modeller
- [ ] Markér usikre felter og manglende data

## Phase 4: Privacy
- [ ] Implementer PII-detektor for navn, CPR, adresse, e-mail, telefon og kontonumre
- [ ] Implementer maskering/redaktion før LLM-kald
- [ ] Implementer auditlog af saniteret prompt og svar
- [ ] Skriv tests, der beviser at rå PII ikke sendes videre

## Phase 5: Q&A
- [ ] Implementer spørgeinterface på dansk
- [ ] Opret prompt-template med tydelige begrænsninger
- [ ] Tilføj forklaringer med antagelser og usikkerheder

## Phase 6: Scenario engine
- [ ] Definér inputmodel for scenarier
- [ ] Implementer første scenarier for ændret indbetaling og pensionsalder
- [ ] Returnér både tal og forklaringer

## Phase 7: UX
- [ ] Byg en simpel CLI eller lokal webapp
- [ ] Vis udtrukne ordninger og forsikringer
- [ ] Vis hvad der er maskeret før LLM-kald
- [ ] Vis audit-log for saniteret trafik

## Definition of done
- [ ] Systemet kan indlæse mindst ét pensionsdokument
- [ ] Systemet kan udtrække mindst én pensionsordning og én forsikringsdækning
- [ ] Systemet kan besvare mindst ét spørgsmål på dansk om dokumentet
- [ ] Systemet dokumenterer, at umaskeret PII ikke sendes til LLM
