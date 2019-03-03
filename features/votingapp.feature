Feature: Voting web app

  Scenario: vote to question
    Given User accesses to voting web app
    Then On the top view: User should be able to see 1 question, "What's up?"

    When On the top view: User clicks "What's up" question
    Then On the details view: User should be able to see "What's up?" as title
    And On the details view: User should be able to see "Not much" as choice
    And On the details view: User should be able to see "The sky" as choice
    And On the details view: User should be able to see "Just hacking again" as choice

    When On the details view: User clicks "Not much" choice
    Then On the details view: User should be able to see "Not much" selected

    When On the details view: User clicks "Vote" button
    Then On the result view: User should be able to see "What's up?" as title
    And On the result view: User should be able to see "Not much" is 1 vote
    And On the result view: User should be able to see "The sky" is 0 votes
    And On the result view: User should be able to see "Just hacking again" is 0 votes

    When On the result view: User clicks "Vote again?"
    Then On the details view: User should be able to see "What's up?" as title
    And On the details view: User should be able to see "Not much" as choice
    And On the details view: User should be able to see "The sky" as choice
    And On the details view: User should be able to see "Just hacking again" as choice
