*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi1
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  t
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  testi2
    Set Password  1
    Set Password Confirmation  1
    Click Button  Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  testi3
    Set Password  aaaaaaaaaaaa
    Set Password Confirmation  aaaaaaaaaaaa
    Click Button  Register
    Register Should Fail With Message  Password should contain other characters than letters

Register With Nonmatching Password And Password Confirmation
    Set Username  testi4
    Set Password  aaaaa1aaaaa
    Set Password Confirmation  bbbbb2aaaaa
    Click Button  Register
    Register Should Fail With Message  Passwords don't match


Register With Username That Is Already In Use
    Set Username  testi1
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Register Should Succeed
    Go To Register Page
    Set Username  testi1
    Set Password  testi123
    Set Password Confirmation  testi123
    Click Button  Register
    Register Should Fail With Message  User with username testi1 already exists
#

*** Keywords ***
#...
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    After Registration Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password2}
    Input Password  password_confirmation  ${password2}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

