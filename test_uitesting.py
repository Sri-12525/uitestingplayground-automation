from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from pageObjects.hiddenlayers import HiddenLayers
from pageObjects.loaddelay import LoadDelay
from pageObjects.ajaxdata import AJAXData
from pageObjects.textinput import TextInput
from pageObjects.scrollbar import Scrollbar
from pageObjects.dynamic_table import DynamicTable
from pageObjects.verifytext import VerifyText
from pageObjects.progressbar import ProgressBar
from pageObjects.visibility import Visibility
from pageObjects.mouseover import MouseOver
from pageObjects.non_breakingspace import NonBreakingSpace
from pageObjects.overlapped_element import OverlappedElements
from pageObjects.shadow_elements import ShadowElements
from pageObjects.shadow_elements import ShadowElements
from pageObjects.alerts import Alerts
from pageObjects.file_upload import FileUpload
from pageObjects.animatedbutton import AnimatedButton
from pageObjects.disabledinput import DisabledInput
from pageObjects.autowait import AutoWait
from pageObjects.click import Click


@pytest.mark.usefixtures("setup")
class TestE2E:
    def test_launchurl(self):
        driver = self.driver
        
        print("Launching hidden layers url .. ")
        hidden_layers_launch = HiddenLayers(driver)
        hidden_layers_launch.hidden_layers()
        print("Completed hidden layers testing !!")
        driver.back()
        
    def test_load_delay(self):
        driver = self.driver
        
        print("Launching load delays url .. ")
        load_delay_test = LoadDelay(driver)
        load_delay_test.load_delays()
        print("Completed load delays testing !!")
        driver.back()
        
    def test_ajax_data(self):
        driver = self.driver
        
        print("Launching ajax data url .. ")
        ajaxdata_test = AJAXData(driver)
        ajaxdata_test.ajax_data()
        print("Completed ajax data testing !!")
        driver.back()
        
    def test_click(self):
        driver = self.driver
        print("Launching the click url...")
        click_test = Click(driver)
        click_test.clicktest()
        print("Click feature testing completed.")
        driver.back()
        
        
    def test_textinputbox(self):
        driver = self.driver
        
        print("Launching text input url .. ")
        text_input_test = TextInput(driver)
        text_input_test.text_input("Hello World")
        print("Completed Text input test !!")
        driver.back()
        
    def test_scrollbar(self):
        driver = self.driver
        print("Launching scrollbar test url")
        scrollbar_test = Scrollbar(driver)
        scrollbar_test.scrollbar_test()
        print("Completed Scrollbar test successfully !!")
        driver.back()
        
    def test_dynamic_table(self):
        driver = self.driver
        
        print("Launching the dynamic table url -- ")
        dynamic_table_test = DynamicTable(driver)
        dynamic_table_test.dynamic_table()
        print("Completed the dynamic table testing successfully !!")
        
        #extracting to excel
        extract_to_excel_test = DynamicTable(driver)
        extract_to_excel_test.extract_to_excel()
        print("Completed extracting the dynamic table testing successfully !!")
        
        
        #taking a screenshot
        print("Taking a screenshot of the current page now .. ")
        screenshot_test = DynamicTable(driver)
        screenshot_test.take_screenshots()
        print("Screenshot is taken.")
        
        driver.back()
        
    def test_verify_text(self):
        driver = self.driver
        
        print("Launching the Verify Text url ... ")
        verifytext = VerifyText(driver)
        verifytext.verify_text()
        print("Testing Verify Text url completed successfully !!")
        driver.back()
        
    def test_progressbar(self):
        driver = self.driver
        print("Launching the Progress Bar url ... ")
        progress_bar_test = ProgressBar(driver)
        progress_bar_test.progressbar_test(60)
        print("Testing Progress Bar url completed successfully !!")
        driver.back()
        
    def test_visibility(self):
        driver = self.driver
        print("Launching the visibility url ..")
        visibility = Visibility(driver)
        visibility.visibility_test()
        print("Testing of visibility completed !")
        driver.back()
        
    def test_mouseover(self):
        driver = self.driver
        print("Launching the mouse over url..")
        mouseover = MouseOver(driver)
        mouseover.mouseover_test(10)
        print("Completed testing mouse over feature !")
        driver.back()
        
        
    def test_non_breaking_space(self):
        driver= self.driver
        
        print("Launching the non-breaking space url..")
        nonbreaking_space = NonBreakingSpace(driver)
        nonbreaking_space.nonbreakingspace_test()
        print("Completed testing the non breaking space page.")
        driver.back()
        
    def test_overlapping_elements(self):
        driver = self.driver
        driver.implicitly_wait(2)
        print("Launching the overlapped elements url ..")
        overlapping_element = OverlappedElements(driver)
        overlapping_element.overlappedelems("Sri")
        print("Completed testing the overlapping elements feature.")
        driver.back()
     
    @pytest.mark.skip   
    def test_shadow_elements(self):
        driver = self.driver
        print("Launching the shadow elements url..")
        shadow_elements = ShadowElements(driver)
        shadow_elements.shadow_elements_test()
        print("Testing completed for the shadow elements feature.")
        driver.back()
        
        
    def test_alerts(self):
        driver = self.driver
        print("Launching the alerts feature url ...")
        alerts_test = Alerts(driver)
        alerts_test.check_alerts()
        print("Completed testing Alerts features.")
        # driver.back()
        
    @pytest.mark.skip
    def test_uploads(self):
        driver = self.driver
        print("Launching the upload url..")
        uploads_test = FileUpload(driver)
        uploads_test.upload_files()
        driver.back()
        
    def test_animatedbutton(self):
        driver = self.driver
        print("Launching the animated button url..")
        animated_bttn = AnimatedButton(driver)
        animated_bttn.animatedbutton_test()
        driver.back()
        
    def test_disabledInput(self):
        driver = self.driver
        print("Launching the disabled input url..")
        disabled_input_test = DisabledInput(driver)
        disabled_input_test.disabled_input()
        driver.back()
        
        
    def test_autowait(self):
        driver = self.driver
        
        print("Starting the auto wait feature test ...")
        autowait_test1 = AutoWait(driver)
        autowait_test1.auto_wait_test("Visible", 10)
        print("Completed testing the auto wait feature.")
        driver.back()