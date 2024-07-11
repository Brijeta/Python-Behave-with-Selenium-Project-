Feature: OrangeHRM Login

  Scenario: Login to Orange HRM with valid parameters
    Given I launch Chrome browser
    When I open orange HRM Homepage
    And Enter username "Admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Scenario Outline: Login to OrangeHRM with Multiple parameters
    Given I launch chrome browser
      When I open orange HRM Homepage
      And Enter username "<username>" and password "<password>"
      And click on login button
      Then User must successfully login to the Dashboard page

      Examples:

      |username |password|
      |Admin    |admin123|
      |admin123 |admin   |
      |Adminxyz |admin123|
      |admin    |adminzyv|
