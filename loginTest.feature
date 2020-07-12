Feature: Login functionality

  Scenario: Login to Pointzi with valid credentials
    Given User launches the Chrome browser
    When Opens dashboard.pointzi.com
    And Enters email "email" and password "password"
    And Clicks the login button
    Then User must successfully login to the Dashboard page
