*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testionnistuu
    Set Password  testi1234
    Set Password Confirmation  testi1234
    Submit Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi1234
    Set Password Confirmation  testi1234
    Submit Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  testi12
    Set Password Confirmation  testi12
    Submit Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testitesti
    Set Password Confirmation  testitesti
    Submit Register
    Register Should Fail With Message  Password has to include numbers

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi1234
    Set Password Confirmation  testi0000
    Submit Register
    Register Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  testionnistuu
    Set Password  testi1234
    Set Password Confirmation  testi1234
    Submit Register
    Register Should Succeed
    Go To Register Page
    Set Username  testionnistuu
    Set Password  testi1234
    Set Password Confirmation  testi1234
    Submit Register
    Register Should Fail With Message  Username already in use

Login After Successful Registration
    Set Username  testi
    Set Password  testi1234
    Set Password Confirmation  testi1234
    Submit Register
    Register Should Succeed
    Go To Ohtu Page
    Click Button  Logout
    Go To Login Page
    Set Username  testi
    Set Password  testi1234
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
   
    Set Username  testi
    Set Password  testi1234
    Set Password Confirmation  testi0000
    Submit Register
    Register Should Fail With Message  Password and password confirmation do not match  
    Go to Login Page
    Set Username  testi
    Set Password  testi1234
    Submit Credentials
    Login Should Fail With Message  Invalid username or password



*** Keywords ***

Submit Register
    Click Button  Register

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Go To Register Page
