*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  mikko
    Set Password  mikko123
    Set Password Confirmation  mikko123
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Registration
    Registration Should Fail With Message  Username need to be at least 3 characters

Register With Valid Username And Invalid Password
    Set Username  kajsa
    Set Password  kajsakajsa
    Set Password Confirmation  kajsakajsa
    Submit Registration
    Registration Should Fail With Message  Password can not contain only characters between a-z

Register With Nonmatching Password And Password Confirmation
    Set Username  kajsa
    Set Password  kajsa123
    Set Password Confirmation  kajsa111
    Submit Registration
    Registration Should Fail With Message  Password and Password Confirmation Nonmatching


*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}