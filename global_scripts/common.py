# -*- coding: utf-8 -*-

import names
import sys

def for_each_call(frame, event, arg):
    snooze(0.1)
 
def init():
    sys.setprofile(for_each_call)

def login():
    startBrowser("https://192.168.1.22:8443")
    activateBrowserTab(waitForObject(names.jSonar_Login_Simplifying_Security_Login_BrowserTab))
    setFocus(waitForObject(names.jSonar_Login_Simplifying_Security_Login_username_text))
    typeText(waitForObject(names.jSonar_Login_Simplifying_Security_Login_username_text), "admin")
    setFocus(waitForObject(names.jSonar_Login_Simplifying_Security_Login_password_password))
    typeText(waitForObject(names.jSonar_Login_Simplifying_Security_Login_password_password), "jS0nar$")
    clickButton(waitForObject(names.jSonar_Login_Simplifying_Security_Login_Sign_In_submit))
    test.compare(waitForObjectExists(names.jSonar_SonarG_Simplifying_Security_jSonar_Simplifying_Security_DIV).simplifiedInnerText, "jSonar Simplifying Security")
