# BOB GYM – System Śledzenia Progresu Treningowego

Repozytorium zawiera koncepcję i analizę funkcjonalną aplikacji BOB GYM, dedykowanej osobom dbającym o systematyczny wzrost siły i masy mięśniowej.

---

## Problem i Grupa Docelowa

### Rozwiązywany Problem

Głównym wyzwaniem, na którym skupia się BOB GYM, jest brak struktury treningowej oraz trudność w precyzyjnym monitorowaniu progresji liniowej.

Wielu ćwiczących trenuje „na wyczucie”, co często prowadzi do stagnacji wyników.  
Aplikacja eliminuje potrzebę:
- korzystania z papierowych dzienników,
- pamiętania ciężarów z poprzednich sesji.

---

### Dla kogo?

- Trójboiści siłowi (Powerlifters)  
  → skupieni na przysiadzie, wyciskaniu i martwym ciągu

- Entuzjaści kulturystyki  
  → śledzenie objętości i parametrów siłowych

- Analitycy własnego treningu  
  → osoby opierające progres na danych (ciężar, powtórzenia, tonaż)

---

## MVP (Minimum Viable Product)

### Funkcje w MVP

- Logowanie treningu (serie, powtórzenia, ciężar)
- Baza ćwiczeń (wielostawowe + izolowane)
- Historia treningów
- Timer odpoczynku

---

### Poza MVP (na przyszłość)

- Zaawansowana analityka (np. sen vs progres)
- Moduł społecznościowy
- Personal Training AI
- Integracje (Apple Health, Google Fit, Garmin)

---

## User Stories

- Jako użytkownik chcę dodać trening, żeby śledzić progres  
- Jako użytkownik chcę zobaczyć historię treningów  
- Jako użytkownik chcę dodać ćwiczenie  
- Jako użytkownik chcę zapisać serie (ciężar, powtórzenia)  

---

## Model Danych (Data Model)

```ts
User
- id
- email

Workout
- id
- userId
- date

Exercise
- id
- name

Set
- id
- workoutId
- exerciseId
- reps
- weight