Scenario Outline: Add new group
    Given a group list
    Given a group with <name>, <header> and <footer>', target_fixture="new_group
    When I add the group the list
    Then the new group list is equal to the old list with ten added group

    Examples:
    | name  | header  | footer  |
    | name1 | header1 | footer1 |
    | name2 | header2 | footer2 |
