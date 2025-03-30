# Sammanfattning  

- Löste alla delar utom osannolika värden på rabattfunktionen.  
- Tyckte den var klurig och hade tidsbrist.  
- Går att hitta på fler scenarion, framförallt felfall.  
- Svårt för min del var att tänka i BDD.  
- Del två googlade jag runt, men det gjordes även för del 1.  

# Testresultat för Varukorg och Beställningsfunktioner

```bash
(.venv) PS C:\Users\MagnusHansson\PycharmProjects\Week4TA> behave features/
Feature: Varukorg och beställningsfunktioner i webbutik # features/cart.feature:1

  Scenario: Lägg till en bok i varukorgen                          # features/cart.feature:3
    Given varukorgen är tom                                        # features/steps/cart_steps.py:4
    When användaren lägger till en bok "Clean Code" med priset 200 # features/steps/cart_steps.py:19
    Then varukorgen ska innehålla 1 bok                            # features/steps/cart_steps.py:40
    And den totala summan ska vara 200                             # features/steps/cart_steps.py:45

  Scenario: Ta bort en bok från varukorgen                          # features/cart.feature:9
    Given varukorgen innehåller en bok "Refactoring" med priset 250 # features/steps/cart_steps.py:8
    When användaren tar bort boken "Refactoring"                    # features/steps/cart_steps.py:23
    Then varukorgen ska vara tom                                    # features/steps/cart_steps.py:35

  Scenario: Visa aktuell summa och antal böcker                             # features/cart.feature:14
    Given varukorgen innehåller en bok "Python Crash Course" med priset 300 # features/steps/cart_steps.py:8
    When användaren lägger till en bok "Clean Code" med priset 200          # features/steps/cart_steps.py:19
    Then varukorgen ska innehålla 2 böcker                                  # features/steps/cart_steps.py:40
    And den totala summan ska vara 500                                      # features/steps/cart_steps.py:45

  Scenario: Öka antal om samma bok läggs till igen                 # features/cart.feature:20
    Given varukorgen innehåller en bok "Clean Code" med priset 200 # features/steps/cart_steps.py:8
    When användaren lägger till en bok "Clean Code" med priset 200 # features/steps/cart_steps.py:19
    Then varukorgen ska innehålla 1 unik bok                       # features/steps/cart_steps.py:49
    And antalet av "Clean Code" ska vara 2                         # features/steps/cart_steps.py:53
    And den totala summan ska vara 400                             # features/steps/cart_steps.py:45

  Scenario: Tömma varukorgen helt            # features/cart.feature:27
    Given varukorgen innehåller flera böcker # features/steps/cart_steps.py:13
    When användaren tömmer varukorgen        # features/steps/cart_steps.py:27
    Then varukorgen ska vara tom             # features/steps/cart_steps.py:35

  Scenario: Rabatt vid köp av fler än tre böcker                                    # features/cart.feature:32
    Given varukorgen innehåller 4 böcker "Python Crash Course" med totalt pris 1000 # features/steps/cart_steps.py:61
    When användaren slutför köpet                                                   # features/steps/cart_steps.py:31
    Then den totala summan ska vara 900 efter rabatt                                # features/steps/cart_steps.py:57

  Scenario: Lagerhantering vid köp                                # features/cart.feature:37
    Given en bok "Design Patterns" finns i lager med 2 exemplar   # features/steps/cart_steps.py:67
    When användaren försöker köpa 3 exemplar av "Design Patterns" # features/steps/cart_steps.py:72
    Then ett meddelande visas "Endast 2 exemplar finns i lager"   # features/steps/cart_steps.py:76
    And varukorgen innehåller 2 exemplar av "Design Patterns"     # features/steps/cart_steps.py:80

  Scenario Outline: Användarinloggning -- @1.1                                         # features/cart.feature:50
    Given användaren försöker logga in med användarnamn "admin" och lösenord "korrekt" # features/steps/cart_steps.py:84
    When inloggning behandlas                                                          # features/steps/cart_steps.py:89
    Then inloggningen ska vara "lyckad"                                                # features/steps/cart_steps.py:93

  Scenario Outline: Användarinloggning -- @1.2                                       # features/cart.feature:51
    Given användaren försöker logga in med användarnamn "user2" och lösenord "wrong" # features/steps/cart_steps.py:84
    When inloggning behandlas                                                        # features/steps/cart_steps.py:89
    Then inloggningen ska vara "misslyckad"                                          # features/steps/cart_steps.py:93

  Scenario: Beställningshistorik                  # features/cart.feature:53
    Given en användare har tidigare beställningar # features/steps/cart_steps.py:97
    When användaren tittar på sin orderhistorik   # features/steps/cart_steps.py:102
    Then beställningarna ska visas korrekt        # features/steps/cart_steps.py:106

  Scenario: Kvitto skickas efter köp           # features/cart.feature:58
    Given en användare slutför ett köp         # features/steps/cart_steps.py:110
    When systemet behandlar beställningen      # features/steps/cart_steps.py:116
    Then ett kvitto ska skapas                 # features/steps/cart_steps.py:120
    And ett kvitto ska skickas till användaren # features/steps/cart_steps.py:120

1 feature passed, 0 failed, 0 skipped  
11 scenarios passed, 0 failed, 0 skipped  
39 steps passed, 0 failed, 0 skipped, 0 undefined  
Took 0m0.000s  
(.venv) PS C:\Users\MagnusHansson\PycharmProjects\Week4TA>  
