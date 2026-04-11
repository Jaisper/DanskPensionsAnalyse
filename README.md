# DanskPensionsAnalyse

DanskPensionsAnalyse er et projekt til at bygge en dansk pensionsanalytiker med en spec-driven udviklingsproces ved brug af GitHub Spec Kit og GitHub Copilot.

## Formål

Projektet skal hjælpe private brugere med at forstå pensionsordninger, tilknyttede forsikringer, skattemæssige forhold og scenarier for opsparing og udbetaling.

## Arbejdsform

Projektet følger en spec-driven proces:

1. Skriv og vedligehold specifikationer i `specs/`.
2. Omsæt specifikationer til tekniske planer.
3. Bryd planen ned i opgaver.
4. Implementér trinvist med Copilot og almindelig kode-review.

## Første feature

Den første feature er en pensionsanalytiker, der kan:

- læse PensionsInfo-rapporter og pensionsoversigter,
- forklare pensionsordninger og forsikringer på dansk,
- simulere simple scenarier for opsparing og udbetaling,
- beskytte PII ved at maskere data før eksterne LLM-kald.
