Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header> and <footer>
    When I add the group the list
    Then the new group list is equal to the old list with ten added group

    Examples:
    | name  | header  | footer  |
    | name1 | header1 | footer1 |
    | name2 | header2 | footer2 |

Scenario: Delete a group
    Given a non-empty group list
    Given a random group from the list
    When I delete the group from the list
    Then the new group list is equal to the old list without the deleted group


Scenario: Modification a group
    Given a non-empty group list
    Given a random group from the list
    Given a new name for edited group
    When I edit the group from the list
    Then the new group list is equal to the old list without the edit group

