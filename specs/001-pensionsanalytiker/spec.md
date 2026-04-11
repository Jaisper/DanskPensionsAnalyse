# Spec: Dansk pensionsanalytiker v0.1

## Problem statement

Mange private brugere i Danmark har pensionsordninger på tværs af flere pensionsselskaber, banker og arbejdsmarkedspensioner. De har adgang til PensionsInfo-rapporter og selskabsspecifikke oversigter, men mangler et enkelt værktøj, der kan samle oplysningerne og forklare dem i almindeligt dansk.

Brugeren skal kunne forstå:

- hvilke ordninger vedkommende har,
- hvilke forsikringer der er knyttet til ordningerne,
- hvordan forskellige ordninger beskattes,
- hvordan ændringer i opsparing eller udbetaling påvirker pensionen.

## Users

Primær bruger er en privatperson i Danmark med en eller flere pensionsordninger.

## Goals

Systemet skal kunne:

- modtage pensionsdata fra PensionsInfo-rapporter og pensionsoversigter,
- identificere pensionsordninger og tilknyttede forsikringer,
- besvare spørgsmål på dansk om ordninger, skat, udbetaling og scenarier,
- simulere simple scenarier for fortsat opsparing og udbetaling,
- beskytte persondata ved at maskere PII før eksterne LLM-kald.

## Non-goals

Systemet skal ikke:

- agere juridisk eller finansiel rådgiver,
- udføre handler eller ændre pensionsordninger,
- dække generel privatøkonomisk rådgivning uden for pension og tilknyttede forsikringer.

## Inputs

- PDF fra PensionsInfo
- PDF fra pensionsselskaber
- PDF eller dokumenter om forsikringsdækninger
- Brugerens spørgsmål på dansk

## Functional requirements

### FR1 Dokumentforståelse
Systemet skal kunne læse og udtrække relevante oplysninger fra pensionsdokumenter.

### FR2 Domæneforståelse
Systemet skal kunne klassificere ordninger som fx ratepension, livrente, aldersopsparing og relevante forsikringsdækninger.

### FR3 Spørgsmål og svar
Systemet skal kunne besvare naturlige spørgsmål på dansk om brugerens pensionsforhold baseret på de dokumenter, der er stillet til rådighed.

### FR4 Scenarier
Systemet skal kunne simulere simple scenarier for ændret opsparing, pensioneringstidspunkt og udbetalingstype.

### FR5 Forklaringer
Systemet skal kunne forklare sine svar i et forståeligt sprog og tydeliggøre usikkerheder og antagelser.

### FR6 Privacy pipeline
Systemet skal maskere eller fjerne direkte identifikatorer før data sendes til en ekstern LLM.

### FR7 Audit
Systemet skal kunne logge den maskerede payload, der sendes til en LLM, samt modelsvaret, så audit og debugging er muligt uden at lagre rå PII.

## Privacy requirements

- Rå PII må gerne vises i den lokale session.
- Navne, adresser, CPR-numre, e-mailadresser, telefonnumre og andre direkte identifikatorer må ikke sendes umaskeret til eksterne LLM'er.
- Logger må kun indeholde maskerede eller anonymiserede data.
- Persistens af rå persondata skal som udgangspunkt undgås.

## Success criteria

- Brugeren kan få et samlet og forståeligt overblik over sine pensionsordninger.
- Brugeren kan stille mindst 10 forskellige typer spørgsmål om pension, forsikring og scenarier og få konsistente svar.
- Systemet kan demonstrere, at umaskeret PII ikke sendes til en ekstern LLM.
