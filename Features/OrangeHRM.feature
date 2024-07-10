Feature: OrangeHRM Logo

  Scenario: Logo presence on OrangeHRM Home Page
    Given  Launch chrome browser
    When  open Orane hrm homepage
    Then  verify that the logo present on page
    And close browser