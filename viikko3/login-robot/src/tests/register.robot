*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  kai  ja1kooka
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  ela  cheek123
    Output Should Contain  User with username ela already exists

Register With Too Short Username And Valid Password
    Input Credentials  el  astinen_2
    Output Should Contain  Username need to be at least 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  el2  astinen_2
    Output Should Contain  Use characters between a-z for username

Register With Valid Username And Too Short Password
    Input Credentials  emi  nem1
    Output Should Contain  Password need to be 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  too  pacpacpac
    Output Should Contain  Password can not contain only characters between a-z

*** Keywords ***
Input New Command And Create User
    Create User  ela  stinen_1
    Input New Command