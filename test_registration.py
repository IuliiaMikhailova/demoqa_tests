from selene import browser
import os
from selene import have



def test_successful_registration():

browser.open('/automation-practice-form')
browser.element('[id = firstName]').type('Julia')
browser.element('[id = lastName]').type('Mikhailova')
browser.element('[id = userEmail]').type('chernova-91@mail.ru')
browser.element('[name=gender] [value=Female]').click()
browser.element('[id = userNumber]').type('9991641109')

browser.element('[id = dateOfBirthInput]').type
browser.element('.react-datepicker-wrapper').click()
browser.element('.react-datepicker__year-select').click()
browser.element('option[value="1991"]').click()
browser.element('.react-datepicker__month-select').click()
browser.element('option[value="8"]').click()
browser.element('.react-datepicker__day--011').click()

browser.element('.subjects-auto-complete__value-container').type('test')
browser.element('[title for="hobbies-checkbox-3"]').click()

browser.element('#uploadPicture').send_keys(os.getcwd() + "/picture_one.jpg")

browser.element('#currentAddress').type('Kazan, Teregulova str.')

browser.element('#state').click()
browser.element('#react-select-3-input').type('Har').press_enter()
browser.element('#react-select-4-input').type('Kar').press_enter()

browser.element('#submit').press_enter()

browser.element('.modal-title h4').should(have.text('Thanks for submitting the form'))

browser.all('tbody tr').should(have.exact_texts(
    'Student Name Julia Mikhailova', 'Student Email chernova-91@mail.ru', 'Gender Female',
    'Mobile 9991641109', 'Date of Birth 11 September,1991', 'Subjects test',
    'Hobbies Music', 'Picture picture_one.jpg', 'Address Kazan, Teregulova str.',
    'State and City Haryana Karnal'))