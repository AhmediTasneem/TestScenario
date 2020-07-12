# Created by my at 13-07-20
Feature: Signup functionality

  Scenario: Register on Pointzi
    Given User launches the Chrome browser
    When Clicks register button
    And Enters email "email" and password "password" and confirmpwd "confirmpwd"
    And Clicks the register button
    Then User must go to the second register page
