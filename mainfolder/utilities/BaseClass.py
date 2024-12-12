    import logging
    from datetime import datetime
    import os
    import pytest
    import allure


    @allure.story("Base class Logger and screenshot")
    @pytest.mark.usefixtures("setup")
    class BaseClass:
        def get_logger(self):
            logs = logging.getLogger(__name__)
            fileHandler = logging.FileHandler('../../logs/logfile.log')
            format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s: %(message)s")

            logs.setLevel(logging.DEBUG)
            fileHandler.setFormatter(format)
            logs.addHandler(fileHandler)
            return logs

        def takescreenshot(self, driver, result_name="screenshot"):
            # Get the current timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Ensure the screenshot directory exists
            screenshot_dir = "../../screenshot"
            os.makedirs(screenshot_dir, exist_ok=True)

            # Create the file path with result name and timestamp
            screenshot_path = os.path.join(screenshot_dir, f"{result_name}_{timestamp}.png")

            # Save the screenshot
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved at: {screenshot_path}")
