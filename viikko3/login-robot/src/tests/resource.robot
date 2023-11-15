*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
### v1t3 ###
Input New Command
    Input  new

Input Login Command
    Input  login

Input Credentials
    [Arguments]  ${username}  ${password}
    Input  ${username}
    Input  ${password}
    Run Application
