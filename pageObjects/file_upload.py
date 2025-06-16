from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, os

class FileUpload:
    def __init__(self, driver):
        self.driver = driver

    def upload_files(self):
        driver = self.driver
        wait = WebDriverWait(driver, 10)

        # Step 1: Navigate to File Upload page
        fileupload_url = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div/h3/a[.='File Upload']")))
        fileupload_url.click()
        time.sleep(2)

        # Step 2: Switch into the iframe
        iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        driver.switch_to.frame(iframe)

        # Step 3: Find (hidden) file input
        file_input = wait.until(EC.presence_of_element_located((By.ID, "uploadFile")))
        driver.execute_script("arguments[0].style.display = 'block';", file_input)

        # Step 4: Upload your file
        file_path = os.path.abspath("alerts.py")
        assert os.path.exists(file_path), f"❌ {file_path} not found — make sure alerts.py exists!"
        file_input.send_keys(file_path)
        print("✅ File path sent.")

        # Step 5: Confirm upload by reading displayed file name
        uploaded_file = wait.until(EC.visibility_of_element_located((By.ID, "fileName")))
        print("📁 Displayed upload:", uploaded_file.text)
        assert "alerts.py" in uploaded_file.text, "❌ Upload failed: filename mismatch"

        time.sleep(1)

        # Step 6: Return context to main page (optional but safer)
        driver.switch_to.default_content()
        print("✅ Upload confirmed inside iframe.")

