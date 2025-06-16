🚀 Features
✅ Clean Code: Organized into feature-based classes under tests/ for clarity and maintainability.

💡 Examples Covered:

Auto Wait dropdown interactions
Handling JavaScript alerts (accept, dismiss, prompt)
Docker-ready Shadow DOM GUID generator
File upload inside an iframe with hidden input
Animated button stability check
Scrolling and visibility 
tests

🧭 Uses WebDriverWait + intuitive locator strategies for robust and reliable automation.

🧪 Tech Stack
Python 3.8+
Selenium WebDriver (Chrome)
PyTest for test execution
Optional: pyperclip, pyautogui for advanced clipboard scenarios

📥 Installation
Clone your repo:


git clone https://github.com/Sri-12525/uitestingplayground-automation.git
cd uitestingplayground-automation
💻 Activate your virtual environment & install requirements:


python -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows

pip install -r requirements.txt
Install optional clipboard support for Shadow DOM test:


pip install pyperclip
▶️ Running Tests
To execute all automated tests:


pytest -v
To run a single test file:


pytest -q tests/test_shadow_dom.py
To skip clipboard-based Shadow DOM test (if pyperclip isn’t installed):


pytest -m "not clipboard"


🛠️ Project Structure

uitestingplayground-automation/
├── tests/
│   ├── test_auto_wait.py
│   ├── test_alerts.py
│   ├── test_shadow_dom.py
│   ├── test_file_upload.py
│   └── test_animated_button.py
├── pages/
│   └── page_classes.py        # page object classes for each feature
├── requirements.txt
└── README.md
tests/: PyTest files — each corresponds to one Playground scenario.

pages/: Contains reusable page objects and helper methods.

📚 Test Coverage Overview
✅ Auto‑Wait
Selects "Input", checks associated behavior visibility, and captures screenshot.

✅ Alerts
Handles basic alert, confirm, prompt interactions with validation and logging.

✅ Shadow DOM
Generates a GUID, copies to clipboard, and verifies clipboard value (if supported).

✅ File Upload
Uploaded a file via hidden input within an iframe — uses JavaScript unhiding technique.

✅ Animated Button
Clicks Start Animation, waits for spin class removal, then clicks Moving Target button.

📝 Notes & Tips
Make sure Chrome browser and chromedriver are compatible versions.
The Shadow DOM clipboard feature requires real browser (not headless) + clipboard access.
All file paths (like alerts.py) should exist relative to the working directory.
Screenshots are saved under each feature’s directory (e.g., autowait_screenshots/).


