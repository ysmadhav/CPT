*** Settings ***
Force Tags  smoke
Library  SeleniumLibrary
#Library  ${CURDIR}${/}..${/}Variables${/}${SourceSystem}.py
#Resource        ${CURDIR}${/}..${/}global${/}keywords.robot
Library  ${CURDIR}${/}..${/}Library${/}Custom1.py
#Library  Library.StringOps.py

*** Variables ***
${Browser}
${SourceSystem}
${Url}  https://www.google.com
${function_Name}
${Arg1}
${Arg2}
${Val}

*** Test Cases ***
This is second first TestCase
     Given I concatinate 2 strings  Madhav   Latha
#    log to console  ${CURDIR}${/}..${/}Variables${/}${SourceSystem}.py
#    ${Val} =  join two strings  Madhav   Latha
#    log many  ${function_name}  ${Arg1}  ${Arg2}
#     ${Val} =  ${function_Name}  ${Arg1}  ${Arg2}

*** Keywords ***
I concatinate 2 strings
    [Arguments]  ${Arg1}  ${Arg2}
    ${Val} =  join two strings  ${Arg1}  ${Arg2}
    log to console  ${Val}