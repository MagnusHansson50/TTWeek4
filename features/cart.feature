Feature: Varukorg och beställningsfunktioner i webbutik

  Scenario: Lägg till en bok i varukorgen
    Given varukorgen är tom
    When användaren lägger till en bok "Clean Code" med priset 200
    Then varukorgen ska innehålla 1 bok
    And den totala summan ska vara 200

  Scenario: Ta bort en bok från varukorgen
    Given varukorgen innehåller en bok "Refactoring" med priset 250
    When användaren tar bort boken "Refactoring"
    Then varukorgen ska vara tom

  Scenario: Visa aktuell summa och antal böcker
    Given varukorgen innehåller en bok "Python Crash Course" med priset 300
    When användaren lägger till en bok "Clean Code" med priset 200
    Then varukorgen ska innehålla 2 böcker
    And den totala summan ska vara 500

  Scenario: Öka antal om samma bok läggs till igen
    Given varukorgen innehåller en bok "Clean Code" med priset 200
    When användaren lägger till en bok "Clean Code" med priset 200
    Then varukorgen ska innehålla 1 unik bok
    And antalet av "Clean Code" ska vara 2
    And den totala summan ska vara 400

  Scenario: Tömma varukorgen helt
    Given varukorgen innehåller flera böcker
    When användaren tömmer varukorgen
    Then varukorgen ska vara tom

  Scenario: Rabatt vid köp av fler än tre böcker
    Given varukorgen innehåller 4 böcker "Python Crash Course" med totalt pris 1000
    When användaren slutför köpet
    Then den totala summan ska vara 900 efter rabatt

  Scenario: Lagerhantering vid köp
    Given en bok "Design Patterns" finns i lager med 2 exemplar
    When användaren försöker köpa 3 exemplar av "Design Patterns"
    Then ett meddelande visas "Endast 2 exemplar finns i lager"
    And varukorgen innehåller 2 exemplar av "Design Patterns"

  Scenario Outline: Användarinloggning
    Given användaren försöker logga in med användarnamn "<username>" och lösenord "<password>"
    When inloggning behandlas
    Then inloggningen ska vara "<result>"

    Examples:
      | username | password | result  |
      | admin    | korrekt  | lyckad  |
      | user2    | wrong    | misslyckad |

  Scenario: Beställningshistorik
    Given en användare har tidigare beställningar
    When användaren tittar på sin orderhistorik
    Then beställningarna ska visas korrekt

  Scenario: Kvitto skickas efter köp
    Given en användare slutför ett köp
    When systemet behandlar beställningen
    Then ett kvitto ska skapas
    And ett kvitto ska skickas till användaren
