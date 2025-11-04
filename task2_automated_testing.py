"""
Task 2: Automated Testing with AI
===================================
Automated test case for a login page using Selenium WebDriver.
Tests both valid and invalid credentials scenarios.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
from datetime import datetime


class LoginPageTest:
    """
    Automated test suite for a login page.
    Tests both valid and invalid credential scenarios.
    """
    
    def __init__(self, base_url, driver_path=None):
        """
        Initialize the test suite.
        
        Args:
            base_url (str): URL of the login page
            driver_path (str): Path to ChromeDriver (if not in PATH)
        """
        self.base_url = base_url
        self.driver = None
        self.results = {
            'total_tests': 0,
            'passed': 0,
            'failed': 0,
            'test_cases': [],
            'timestamp': datetime.now().isoformat()
        }
        
        # Initialize WebDriver
        try:
            options = webdriver.ChromeOptions()
            # Add options for headless mode (optional)
            # options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            # Use webdriver-manager to automatically handle ChromeDriver
            if driver_path:
                # If custom driver path provided, use it
                service = Service(executable_path=driver_path)
                self.driver = webdriver.Chrome(service=service, options=options)
            else:
                # Automatically download and manage ChromeDriver
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service, options=options)
            
            # Set implicit wait
            self.driver.implicitly_wait(10)
            self.wait = WebDriverWait(self.driver, 15)
            
            print("✓ WebDriver initialized successfully")
        except Exception as e:
            print(f"✗ Failed to initialize WebDriver: {e}")
            print("Make sure Chrome browser is installed on your system.")
            raise
    
    def test_valid_login(self, username, password):
        """
        Test successful login with valid credentials.
        
        Args:
            username (str): Valid username
            password (str): Valid password
            
        Returns:
            bool: True if test passed, False otherwise
        """
        self.results['total_tests'] += 1
        test_result = {
            'name': 'Valid Login Test',
            'status': 'FAILED',
            'message': ''
        }
        
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            time.sleep(2)
            
            # Find username field
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(username)
            
            # Find password field
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Submit form
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Wait for redirect or success message
            time.sleep(3)
            
            # Verify successful login (check for dashboard or welcome message)
            try:
                # Check if redirected to a dashboard or home page
                current_url = self.driver.current_url
                if current_url != self.base_url:
                    # Successfully redirected away from login page
                    test_result['status'] = 'PASSED'
                    test_result['message'] = f"Successfully logged in and redirected to: {current_url}"
                    self.results['passed'] += 1
                    print("✓ Valid login test PASSED")
                    return True
                else:
                    # Check for success message on same page
                    success_element = self.driver.find_element(By.CLASS_NAME, "success")
                    if success_element:
                        test_result['status'] = 'PASSED'
                        test_result['message'] = "Success message displayed"
                        self.results['passed'] += 1
                        print("✓ Valid login test PASSED")
                        return True
                    else:
                        raise Exception("No success indicator found")
            except NoSuchElementException:
                test_result['message'] = "Login failed - no success indicator found"
                raise Exception(test_result['message'])
                
        except TimeoutException as e:
            test_result['message'] = f"Timeout waiting for page elements: {str(e)}"
            self.results['failed'] += 1
            print(f"✗ Valid login test FAILED: {test_result['message']}")
            
        except Exception as e:
            test_result['message'] = str(e)
            self.results['failed'] += 1
            print(f"✗ Valid login test FAILED: {test_result['message']}")
            
        finally:
            self.results['test_cases'].append(test_result)
        
        return False
    
    def test_invalid_username(self, username, password):
        """
        Test login with invalid username.
        
        Args:
            username (str): Invalid username
            password (str): Password (can be valid or invalid)
            
        Returns:
            bool: True if test passed, False otherwise
        """
        self.results['total_tests'] += 1
        test_result = {
            'name': 'Invalid Username Test',
            'status': 'FAILED',
            'message': ''
        }
        
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            time.sleep(2)
            
            # Fill in credentials
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(username)
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Submit form
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Wait for error message
            time.sleep(2)
            
            # Check for error message
            try:
                error_element = self.wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "error"))
                )
                error_text = error_element.text.lower()
                
                if "invalid" in error_text or "incorrect" in error_text:
                    test_result['status'] = 'PASSED'
                    test_result['message'] = f"Correctly displayed error: {error_text}"
                    self.results['passed'] += 1
                    print("✓ Invalid username test PASSED")
                    return True
                else:
                    test_result['message'] = f"Unexpected error message: {error_text}"
                    raise Exception(test_result['message'])
                    
            except TimeoutException:
                # Check if still on login page (should be)
                if self.driver.current_url == self.base_url:
                    test_result['status'] = 'PASSED'
                    test_result['message'] = "Login prevented, remained on login page"
                    self.results['passed'] += 1
                    print("✓ Invalid username test PASSED")
                    return True
                else:
                    test_result['message'] = "Login succeeded when it should have failed"
                    raise Exception(test_result['message'])
                    
        except Exception as e:
            test_result['message'] = str(e)
            self.results['failed'] += 1
            print(f"✗ Invalid username test FAILED: {test_result['message']}")
            
        finally:
            self.results['test_cases'].append(test_result)
        
        return False
    
    def test_invalid_password(self, username, password):
        """
        Test login with invalid password.
        
        Args:
            username (str): Valid username
            password (str): Invalid password
            
        Returns:
            bool: True if test passed, False otherwise
        """
        self.results['total_tests'] += 1
        test_result = {
            'name': 'Invalid Password Test',
            'status': 'FAILED',
            'message': ''
        }
        
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            time.sleep(2)
            
            # Fill in credentials
            username_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            username_field.clear()
            username_field.send_keys(username)
            
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Submit form
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Wait for error message
            time.sleep(2)
            
            # Check for error message
            try:
                error_element = self.wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "error"))
                )
                error_text = error_element.text.lower()
                
                if "invalid" in error_text or "incorrect" in error_text or "password" in error_text:
                    test_result['status'] = 'PASSED'
                    test_result['message'] = f"Correctly displayed error: {error_text}"
                    self.results['passed'] += 1
                    print("✓ Invalid password test PASSED")
                    return True
                else:
                    test_result['message'] = f"Unexpected error message: {error_text}"
                    raise Exception(test_result['message'])
                    
            except TimeoutException:
                # Check if still on login page
                if self.driver.current_url == self.base_url:
                    test_result['status'] = 'PASSED'
                    test_result['message'] = "Login prevented, remained on login page"
                    self.results['passed'] += 1
                    print("✓ Invalid password test PASSED")
                    return True
                else:
                    test_result['message'] = "Login succeeded when it should have failed"
                    raise Exception(test_result['message'])
                    
        except Exception as e:
            test_result['message'] = str(e)
            self.results['failed'] += 1
            print(f"✗ Invalid password test FAILED: {test_result['message']}")
            
        finally:
            self.results['test_cases'].append(test_result)
        
        return False
    
    def test_empty_credentials(self):
        """
        Test login with empty credentials.
        
        Returns:
            bool: True if test passed, False otherwise
        """
        self.results['total_tests'] += 1
        test_result = {
            'name': 'Empty Credentials Test',
            'status': 'FAILED',
            'message': ''
        }
        
        try:
            # Navigate to login page
            self.driver.get(self.base_url)
            time.sleep(2)
            
            # Try to submit without filling credentials
            submit_button = self.driver.find_element(By.ID, "submit")
            submit_button.click()
            
            # Wait for validation error
            time.sleep(2)
            
            # Check for HTML5 validation or error message
            try:
                error_element = self.wait.until(
                    EC.presence_of_element_located((By.CLASS_NAME, "error"))
                )
                test_result['status'] = 'PASSED'
                test_result['message'] = "Empty credentials rejected"
                self.results['passed'] += 1
                print("✓ Empty credentials test PASSED")
                return True
            except TimeoutException:
                # Check if still on login page (expected with HTML5 validation)
                if self.driver.current_url == self.base_url:
                    test_result['status'] = 'PASSED'
                    test_result['message'] = "Empty credentials rejected (stayed on login page)"
                    self.results['passed'] += 1
                    print("✓ Empty credentials test PASSED")
                    return True
                else:
                    test_result['message'] = "Empty credentials accepted"
                    raise Exception(test_result['message'])
                    
        except Exception as e:
            test_result['message'] = str(e)
            self.results['failed'] += 1
            print(f"✗ Empty credentials test FAILED: {test_result['message']}")
            
        finally:
            self.results['test_cases'].append(test_result)
        
        return False
    
    def save_results(self, filename='test_results.json'):
        """Save test results to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.results, f, indent=2)
        print(f"\n✓ Test results saved to {filename}")
    
    def print_summary(self):
        """Print a summary of test results."""
        print("\n" + "="*80)
        print("TEST RESULTS SUMMARY")
        print("="*80)
        print(f"Total Tests: {self.results['total_tests']}")
        print(f"Passed: {self.results['passed']}")
        print(f"Failed: {self.results['failed']}")
        
        success_rate = (self.results['passed'] / self.results['total_tests'] * 100) if self.results['total_tests'] > 0 else 0
        print(f"Success Rate: {success_rate:.1f}%")
        
        print("\nDetailed Results:")
        for test_case in self.results['test_cases']:
            status_symbol = "✓" if test_case['status'] == 'PASSED' else "✗"
            print(f"  {status_symbol} {test_case['name']}: {test_case['status']}")
            if test_case['message']:
                print(f"      {test_case['message']}")
        
        print("="*80)
    
    def cleanup(self):
        """Close the browser and clean up resources."""
        if self.driver:
            self.driver.quit()
            print("\n✓ Browser closed")


def run_login_tests():
    """
    Main function to run all login page tests.
    
    Note: This uses a demo login page at https://the-internet.herokuapp.com/login
    Replace with your actual login page URL.
    """
    
    print("\n" + "="*80)
    print("TASK 2: AUTOMATED LOGIN PAGE TESTING")
    print("="*80)
    
    # Configuration
    # Using The Internet herokuapp login page for demonstration
    base_url = "https://the-internet.herokuapp.com/login"
    
    # Note: In a real scenario, replace selectors and credentials as needed
    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"
    invalid_username = "invalid_user"
    invalid_password = "wrong_password"
    
    try:
        # Initialize test suite
        test_suite = LoginPageTest(base_url)
        
        # Run test cases
        print("\nRunning test cases...")
        
        test_suite.test_valid_login(valid_username, valid_password)
        test_suite.test_invalid_username(invalid_username, valid_password)
        test_suite.test_invalid_password(valid_username, invalid_password)
        test_suite.test_empty_credentials()
        
        # Print summary
        test_suite.print_summary()
        
        # Save results
        test_suite.save_results('task2_test_results.json')
        
        # Clean up
        test_suite.cleanup()
        
        return test_suite.results
        
    except Exception as e:
        print(f"\n✗ Test execution failed: {e}")
        print("\nNote: Make sure you have:")
        print("  1. Installed Selenium: pip install selenium")
        print("  2. ChromeDriver installed and in PATH")
        print("  3. Internet connection for accessing test page")
        return None


if __name__ == "__main__":
    results = run_login_tests()

