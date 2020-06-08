*** Settings ***
Force Tags  robotkeywords
Library  Library.StringOps

*** Variables ***
${string_one}  Welcome to
${String_two}  Demo


*** Test Cases ***
TestCase to Concatinate 2 strings using custom method
     Given I concatinate 2 strings  ${string_one}   ${string_two}


*** Keywords ***
I concatinate 2 strings
    [Arguments]  ${Arg1}  ${Arg2}
    ${Val} =  join two strings  ${Arg1}  ${Arg2}
    log to console  ${Val}