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

Login After Successful Registration
    Set Username  pekka
    Set Password  pekka123
    Set Password Confirmation  pekka123
    Submit Registration
    Registration Should Succeed
    Continue To Main Page
    Log Out
    Set Username  pekka
    Set Password  pekka123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  kajsa
    Set Password  kajsa123
    Set Password Confirmation  kajsa111
    Submit Registration
    Registration Should Fail With Message  Password and Password Confirmation Nonmatching
    Continue To Login
    Set Username  kajsa
    Set Password  kajsa123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

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

Continue To Main Page
    Click Link  Continue to main page

Log Out
    Click Button  Logout

Submit Credentials
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Continue To Login
    Click Link  Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
