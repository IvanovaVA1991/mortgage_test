from BaseApp import BasePage
from selenium.webdriver.common.by import By
import yaml


with open('./testdata.yaml', encoding='utf-8') as f:
    testdata = yaml.safe_load(f)


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])


class OperationsHelper(BasePage):

    def enter_sum(self, credit):
        credit_field = self.find_element(TestSearchLocators.ids['LOCATOR_CREDIT_FIELD'])
        credit_field.clear()
        credit_field.send_keys(credit)

    def enter_age(self, age):
        age_field = self.find_element(TestSearchLocators.ids['LOCATOR_AGE_FIELD'])
        age_field.clear()
        age_field.send_keys(age)

    def object_choice(self, object_type):
        self.find_element(TestSearchLocators.ids['LOCATOR_OBJECT_ARROW']).click()
        if object_type == 'flat':
                self.find_element(TestSearchLocators.ids['LOCATOR_FLAT']).click()
        elif object_type == 'house':
                        self.find_element(TestSearchLocators.ids['LOCATOR_HOUSE']).click()
        elif object_type == 'room':
                            self.find_element(TestSearchLocators.ids['LOCATOR_ROOM']).click()
        else:
                            self.find_element(TestSearchLocators.ids['LOCATOR_APARTMENT']).click()


    def sex_choice(self, sex):
        self.find_element(TestSearchLocators.ids['LOCATOR_SEX_ARROW']).click()
        if sex == 'Male':
                self.find_element(TestSearchLocators.ids['LOCATOR_MALE']).click()
        else:
                self.find_element(TestSearchLocators.ids['LOCATOR_FEMALE']).click()


    def bank_choice(self, bank):
        LOCATOR_BANK = (By.XPATH, f"""//*[@id="main"]/div/section[1]/div/div/div[5]/div[2]/form/div[1]/div[3]/div/div[2]/div[2]/div[{bank + 1}]/span""")
        self.find_element(TestSearchLocators.ids['LOCATOR_BANK_ARROW']).click()
        self.find_element(LOCATOR_BANK).click()



    def click_count_button(self):
               self.find_element(TestSearchLocators.ids['LOCATOR_COUNT_BTN']).click()

    def get_choice_text(self):
        choice_field = self.find_element(TestSearchLocators.ids['LOCATOR_CHOICE'], time=5)
        text = choice_field.text
        return text

