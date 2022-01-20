from ast import Add, Return
from lib2to3.pgen2.driver import Driver
from operator import add
from this import d
import unittest
from django.test.runner import DiscoverRunner

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# # ====== ===============Doctor login=====================



# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/doctorlogin')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')

# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')

# user_name.send_keys('rukhsar')

# user_password.send_keys('123')

# submit.send_keys(Keys.RETURN)


# driver.close()
# if _name_ == '_main_':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='local_host'))




# =========================Patient Login======================


# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/patientlogin')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')

# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')

# user_name.send_keys('Rohit')

# user_password.send_keys('Rohit')

# submit.send_keys(Keys.RETURN)
# driver.close()




# =============================Doctor Register===============================
# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/doctorsignup')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')
# first_name = driver.find_element_by_name('first_name')
# last_name = driver.find_element_by_name('last_name')
# department_name=driver.find_element_by_name('department')
# contact_number=driver.find_element_by_name('mobile')
# address_name=driver.find_element_by_name('address')
# profilePic=driver.find_element_by_name('profile_pic')


# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')
# first_name.send_keys('Gaurav')
# user_name.send_keys('GAN423')
# last_name.send_keys('Nagpal')
# user_password.send_keys('GAN423')
# department_name.send_keys('Cradiologist')
# address_name.send_keys('Delhi')
# contact_number.send_keys('9696969696')
# profilePic.send_keys('/home/i1528/Pictures/abcd.png')

# submit.send_keys(Keys.RETURN)
# driver.close()

# ===================Patient Register===================

# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/patientsignup')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')
# first_name = driver.find_element_by_name('first_name')
# last_name = driver.find_element_by_name('last_name')
# contact_number=driver.find_element_by_name('mobile')
# address_name=driver.find_element_by_name('address')
# symptoms_name=driver.find_element_by_name('symptoms')
# past_history=driver.find_element_by_name('past_history_of_illness')
# allergy_name=driver.find_element_by_name('allergy_substance')
# profilePic=driver.find_element_by_name('profile_pic')
# immunization_name=driver.find_element_by_name('immunization')
# Name_and_department=driver.find_element_by_name('assignedDoctorId')
# problems=driver.find_element_by_name('problems_list')
# allergy_level=driver.find_element_by_name('allergy_criticality')
# history_procedure_illness=driver.find_element_by_name('history_procedure')
# Diagnostic=driver.find_element_by_name('diagnostic_results')


# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')
# first_name.send_keys('PatientGautam')
# user_name.send_keys('GAN123')
# last_name.send_keys('Nagpal')
# user_password.send_keys('GAN123')
# Name_and_department.send_keys('Rukhsar (Cradiologist)')
# address_name.send_keys('Delhi')
# contact_number.send_keys('9696969696')
# profilePic.send_keys('/home/i1528/Downloads/patient.png')
# Diagnostic.send_keys('/home/i1528/Downloads/diagnostic.jpg')
# symptoms_name.send_keys('cough')
# past_history.send_keys('None')
# allergy_name.send_keys('None')
# allergy_level.send_keys('Intermediate')
# immunization_name.send_keys('abcd')
# problems.send_keys('Nothing')
# history_procedure_illness.send_keys('Nothing')

# submit.send_keys(Keys.RETURN)
# driver.close()


# =======================Add Mediciene====================


# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/doctorlogin')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')

# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')

# user_name.send_keys('rukhsar')

# user_password.send_keys('123')
# submit.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a/span").click()
# driver.find_element_by_xpath("/html/body/main/div[2]/div/table/tbody/tr[1]/td[5]/a/span").click()
# driver.find_element_by_xpath("/html/body/main/div[2]/a").click()

# time.sleep(3)
# medication_item=driver.find_element_by_name('medicationItem')
# frequency=driver.find_element_by_name('frequency')
# dose=driver.find_element_by_name('dose')
# dose_Unit=driver.find_element_by_name('doseUnit')
# direction_duration=driver.find_element_by_name('directionDuration')
# medicine_form=driver.find_element_by_name('form')
# additional_instructions=driver.find_element_by_name('additionalInstruc')
# substance=driver.find_element_by_name('substance')
# maximum_amount=driver.find_element_by_name('safetyAmount')
# Maxiumum_dose_unit=driver.find_element_by_name('safetyDoseUnit')
# Allowed_period=driver.find_element_by_name('safetyAllowedPer')
# Order_status=driver.find_element_by_name('orderStatus')
# date_discontinued=driver.find_element_by_name('orderDateDisc')
# Date_written=driver.find_element_by_name('orderDateWritten')
# number_ofrRepeatsAllowed=driver.find_element_by_name('authRepeat')
# validity_period=driver.find_element_by_name('authValPer')
# dispense_instruction=driver.find_element_by_name('dispInstruc')
# Amount_description=driver.find_element_by_name('dispDescrip')
# Dispense_Amount=driver.find_element_by_name('dispAmount')
# dispense_units=driver.find_element_by_name('dispAmountUnits')
# Duration_of_supply=driver.find_element_by_name('dispDurution')


# time.sleep(3)
# AddM=driver.find_element_by_name('submit')
# medication_item.send_keys('peracetamol')
# frequency.send_keys('2')
# dose.send_keys('2.0')
# dose_Unit.send_keys('mg')
# direction_duration.send_keys('7Days')
# medicine_form.send_keys('Capsule')
# additional_instructions.send_keys('Nothing')
# substance.send_keys('None')
# maximum_amount.send_keys('2')
# Maxiumum_dose_unit.send_keys('4')
# Allowed_period.send_keys('5')
# Order_status.send_keys('Active')
# date_discontinued.send_keys('31/01/2022'+Keys.TAB+'05:05')
# Date_written.send_keys('19/01/2022'+Keys.TAB+'05:05')
# number_ofrRepeatsAllowed.send_keys('3')
# validity_period.send_keys('22/08/2023'+Keys.TAB+'05:05')
# dispense_instruction.send_keys('None')
# Amount_description.send_keys('0')
# Dispense_Amount.send_keys('0')
# dispense_units.send_keys('0')
# Duration_of_supply.send_keys('None')


# AddM.send_keys(Keys.RETURN)


# =======================Delete Medicine====================

# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/doctorlogin')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')

# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')

# user_name.send_keys('rukhsar')

# user_password.send_keys('123')
# submit.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a/span").click()
# driver.find_element_by_xpath("/html/body/main/div[2]/div/table/tbody/tr[1]/td[5]/a/span").click()
# driver.maximize_window()
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

# driver.find_element_by_xpath("/html/body/main/div[2]/table/tbody/tr[35]/td[2]/a").click()
# deletemedicine=driver.find_element_by_name('submit')
# deletemedicine.send_keys(Keys.RETURN)
# time.sleep(3)
# driver.close()

# =====================Update Medicine================

# driver = webdriver.Chrome()

# driver.get('http://127.0.0.1:8000/doctorlogin')

# time.sleep(3)

# user_name = driver.find_element_by_name('username')
# user_password = driver.find_element_by_name('password')

# time.sleep(3)

# submit = driver.find_element_by_class_name('btnSubmit')

# user_name.send_keys('rukhsar')

# user_password.send_keys('123')
# submit.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a/span").click()
# driver.find_element_by_xpath("/html/body/main/div[2]/div/table/tbody/tr[1]/td[5]/a/span").click()
# driver.maximize_window()
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
# driver.find_element_by_xpath("/html/body/main/div[2]/table/tbody/tr[35]/td[1]/a").click()

# update=driver.find_element_by_name('submit')
# medication_item=driver.find_element_by_name('medicationItem')
# frequency=driver.find_element_by_name('frequency')
# dose=driver.find_element_by_name('dose')
# dose_Unit=driver.find_element_by_name('doseUnit')
# direction_duration=driver.find_element_by_name('directionDuration')
# medicine_form=driver.find_element_by_name('form')
# additional_instructions=driver.find_element_by_name('additionalInstruc')
# substance=driver.find_element_by_name('substance')
# maximum_amount=driver.find_element_by_name('safetyAmount')
# Maxiumum_dose_unit=driver.find_element_by_name('safetyDoseUnit')
# Allowed_period=driver.find_element_by_name('safetyAllowedPer')
# Order_status=driver.find_element_by_name('orderStatus')
# date_discontinued=driver.find_element_by_name('orderDateDisc')
# Date_written=driver.find_element_by_name('orderDateWritten')
# number_ofrRepeatsAllowed=driver.find_element_by_name('authRepeat')
# validity_period=driver.find_element_by_name('authValPer')
# dispense_instruction=driver.find_element_by_name('dispInstruc')
# Amount_description=driver.find_element_by_name('dispDescrip')
# Dispense_Amount=driver.find_element_by_name('dispAmount')
# dispense_units=driver.find_element_by_name('dispAmountUnits')
# Duration_of_supply=driver.find_element_by_name('dispDurution')


# time.sleep(3)

# medication_item.send_keys('peracetamol')
# frequency.send_keys('2')
# dose.send_keys('2.0')
# dose_Unit.send_keys('mg')
# direction_duration.send_keys('7Days')
# medicine_form.send_keys('Capsule')
# additional_instructions.send_keys('Nothing')
# substance.send_keys('None')
# maximum_amount.send_keys('2')
# Maxiumum_dose_unit.send_keys('4')
# Allowed_period.send_keys('5')
# Order_status.send_keys('Active')
# date_discontinued.send_keys('31/01/2022'+Keys.TAB+'05:05')
# Date_written.send_keys('19/01/2022'+Keys.TAB+'05:05')
# number_ofrRepeatsAllowed.send_keys('3')
# validity_period.send_keys('22/08/2023'+Keys.TAB+'05:05')
# dispense_instruction.send_keys('None')
# Amount_description.send_keys('0')
# Dispense_Amount.send_keys('0')
# dispense_units.send_keys('0')
# Duration_of_supply.send_keys('None')
# update.send_keys(Keys.RETURN)
# time.sleep(3)
# driver.close()


# ====================View Document-Diagnostic Report===================

driver = webdriver.Chrome()

driver.get('http://127.0.0.1:8000/doctorlogin')

time.sleep(3)

user_name = driver.find_element_by_name('username')
user_password = driver.find_element_by_name('password')

time.sleep(3)

submit = driver.find_element_by_class_name('btnSubmit')

user_name.send_keys('rukhsar')

user_password.send_keys('123')
submit.send_keys(Keys.RETURN)
driver.find_element_by_xpath("/html/body/nav/ul/li[2]/a/span").click()
driver.find_element_by_xpath("/html/body/main/div[2]/div/table/tbody/tr[1]/td[7]/a/span").click()

driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.find_element_by_xpath("/html/body/main/div[2]/table/tbody/tr[16]/td/div/a").click()
time.sleep(15)
driver.close()




