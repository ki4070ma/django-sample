Feature: Voting web app

  Scenario: vote to question
    Given User accesses to voting web app
    And On the top view: User should be able to see 1 question, "What's up?"
    When On the top view: User clicks "What's up" question
    And On the details view: Use should be able to see "What's up?" as title
    And On the details view: User should be able to see "Not much" as choise
    And On the details view: User should be able to see "The sky" as choise
    And On the details view: User should be able to see "Just hacking again" as choise
    And On the details view: User clicks "Not much" choise
    And On the details view: User clicks "Vote" button
    Then On the result view: User shoud be able to see "What's up?" as title
    And On the result view: User should be able to see "Not much" is "1" vote
    And On the result view: User should be able to see "The sky" is "0" vote
    And On the result view: User should be able to see "Just hacking again" is "0" vote
    And On the result view: User clicks "Vote again?"
    And On the details view: Use should be able to see "What's up?" as title
    And On the details view: User should be able to see "Not much" as choise
    And On the details view: User should be able to see "The sky" as choise
    And On the details view: User should be able to see "Just hacking again" as choise
