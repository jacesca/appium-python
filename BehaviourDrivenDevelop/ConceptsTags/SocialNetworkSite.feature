# This is a feature file
# Run
# ```
# $ cd BehaviourDrivenDevelop/ConceptsTags
    # $ behave SocialNetworkSite.feature
    # or
    # $ behave SocialNetworkSite.feature --no-capture -f plain --tags group
    # or (any profile or group tagged scecnario)
    # $ behave SocialNetworkSite.feature --no-capture -f plain --tags profile,group
    # or (only scenario tagged with profile and group)
    # $ behave SocialNetworkSite.feature --no-capture -f plain --tags profile --tags group
    # or (excluding profile tagged scenario)
    # $ behave SocialNetworkSite.feature --no-capture -f plain --tags=-profile
    # $ behave SocialNetworkSite.feature --no-capture -f plain --tags=~profile
# or
# $ behave
#
# Summary
# --tags=tag1,tag2    --> Only scenarios tagged with any value of the `tags` list
# --tags=-tag1        --> All scenarios minus tag1
# --tags=t1 --tags=t2 --> Only scenrios tagged with t1 and t2
# ```

Feature: SocialNetwork WebPage Tools

    @profile @login @logout
    Scenario: Profile related casses

        Given Launch the profile page
        When Change profile pic
        Then Verify profile pic

    @feed @login
    Scenario: Feed related cases

        Given Launch the feed page
        When Publish the feed
        Then Verify feed

    @pages
    Scenario: Pages related cases

        Given Launch the page
        When Update the page data
        Then Verify page

    @group @profile
    Scenario: Group related cases

        Given Launch the group
        When Update the group details
        Then Verify group
