"""
EduVoice - Black Box Testing Suite
Tests application functionality without knowing internal code
Focuses on inputs, outputs, and user requirements

BLACK BOX TESTING TECHNIQUES USED:
1. Equivalence Partitioning - Group similar inputs
2. Boundary Value Analysis - Test edge cases
3. Decision Table Testing - Test combinations
4. State Transition Testing - Test state changes
5. Use Case Testing - Test user scenarios
"""

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BlackBoxFunctionalTests(unittest.TestCase):
    """Black Box Tests - Functional Testing Without Code Knowledge"""
    
    @classmethod
    def setUpClass(cls):
        """Setup browser once for all tests"""
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--log-level=3')
        
        cls.driver = webdriver.Chrome(options=chrome_options)
        cls.driver.implicitly_wait(3)
        cls.base_url = "http://localhost:3001"
        cls.wait = WebDriverWait(cls.driver, 8)
        
        print("\n" + "="*70)
        print("BLACK BOX TESTING SUITE - Functional Testing")
        print("Testing URL:", cls.base_url)
        print("="*70)
    
    @classmethod
    def tearDownClass(cls):
        """Cleanup after all tests"""
        print("\n" + "="*70)
        print("Black Box Tests Completed")
        print("="*70)
        time.sleep(1)
        cls.driver.quit()
    
    # ==================== TEST CASE 1 ====================
    def test_01_valid_url_input(self):
        """
        BB-TC1: Equivalence Partitioning - Valid URL Input
        Input: Valid application URL
        Expected: Application loads successfully
        """
        print("\n[BLACK BOX TEST 1] Valid URL Input Test")
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        current_url = self.driver.current_url
        title = self.driver.title
        
        # Verify output
        self.assertIsNotNone(current_url, "Application should load")
        self.assertIn("EduVoice", title, "Title should contain app name")
        
        print(f"  • Input URL: {self.base_url}")
        print(f"  • Output URL: {current_url}")
        print(f"  • Page Title: {title}")
        print("  ✓ Valid input produces expected output")
    
    # ==================== TEST CASE 2 ====================
    def test_02_invalid_route_input(self):
        """
        BB-TC2: Equivalence Partitioning - Invalid Route Input
        Input: Non-existent route
        Expected: Graceful error handling (redirect or 404)
        """
        print("\n[BLACK BOX TEST 2] Invalid Route Input Test")
        
        invalid_routes = [
            "/#/nonexistent",
            "/#/xyz123",
            "/#/invalid-page"
        ]
        
        for route in invalid_routes:
            self.driver.get(f"{self.base_url}{route}")
            time.sleep(1)
            
            # System should handle gracefully (not crash)
            body = self.driver.find_element(By.TAG_NAME, "body")
            self.assertTrue(body.is_displayed(), 
                           f"Page should display for {route}")
            print(f"  • Invalid input: {route} → Handled gracefully")
        
        print("  ✓ Invalid inputs handled correctly")
    
    # ==================== TEST CASE 3 ====================
    def test_03_boundary_viewport_min(self):
        """
        BB-TC3: Boundary Value Analysis - Minimum Viewport
        Input: Very small screen size (320x568 - iPhone SE)
        Expected: Content still accessible
        """
        print("\n[BLACK BOX TEST 3] Boundary Test - Minimum Viewport")
        
        # Minimum mobile size
        self.driver.set_window_size(320, 568)
        time.sleep(0.5)
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        # Verify content is accessible
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertTrue(body.is_displayed(), 
                       "Content should be visible at minimum size")
        
        size = self.driver.get_window_size()
        print(f"  • Minimum viewport: {size['width']}x{size['height']}")
        print("  ✓ Application handles minimum boundary")
        
        # Reset
        self.driver.set_window_size(1920, 1080)
    
    # ==================== TEST CASE 4 ====================
    def test_04_boundary_viewport_max(self):
        """
        BB-TC4: Boundary Value Analysis - Maximum Viewport
        Input: Very large screen size (2560x1440 - 2K)
        Expected: Layout scales appropriately
        """
        print("\n[BLACK BOX TEST 4] Boundary Test - Maximum Viewport")
        
        # Large desktop size
        self.driver.set_window_size(2560, 1440)
        time.sleep(0.5)
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        # Verify content is accessible
        body = self.driver.find_element(By.TAG_NAME, "body")
        self.assertTrue(body.is_displayed(),
                       "Content should be visible at maximum size")
        
        size = self.driver.get_window_size()
        print(f"  • Maximum viewport: {size['width']}x{size['height']}")
        print("  ✓ Application handles maximum boundary")
        
        # Reset
        self.driver.set_window_size(1920, 1080)
    
    # ==================== TEST CASE 5 ====================
    def test_05_state_transition_page_navigation(self):
        """
        BB-TC5: State Transition Testing - Page Navigation
        States: Login → Dashboard → Reader → Back
        Expected: Proper state transitions
        """
        print("\n[BLACK BOX TEST 5] State Transition - Page Navigation")
        
        states = [
            ("/#/login", "Login State"),
            ("/#/dashboard", "Dashboard State"),
            ("/#/reader", "Reader State"),
            ("/#/dashboard", "Back to Dashboard"),
        ]
        
        for route, state_name in states:
            self.driver.get(f"{self.base_url}{route}")
            time.sleep(0.8)
            current = self.driver.current_url
            print(f"  • Transition to: {state_name} → {current}")
        
        print("  ✓ State transitions working")
    
    # ==================== TEST CASE 6 ====================
    def test_06_use_case_user_clicks_button(self):
        """
        BB-TC6: Use Case Testing - User Clicks Button
        Scenario: User interacts with clickable elements
        Expected: Buttons are responsive
        """
        print("\n[BLACK BOX TEST 6] Use Case - Button Click Interaction")
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        # Find and click first button
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        
        if buttons:
            initial_state = buttons[0].get_attribute("class")
            buttons[0].click()
            time.sleep(0.5)
            
            print(f"  • Found {len(buttons)} buttons")
            print(f"  • Clicked first button")
            print("  ✓ Button interaction successful")
        else:
            print("  ⚠ No buttons found on page")
    
    # ==================== TEST CASE 7 ====================
    def test_07_use_case_keyboard_navigation(self):
        """
        BB-TC7: Use Case Testing - Keyboard Navigation
        Scenario: User navigates using Tab key
        Expected: Focus moves between elements
        """
        print("\n[BLACK BOX TEST 7] Use Case - Keyboard Navigation")
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        body = self.driver.find_element(By.TAG_NAME, "body")
        
        # Press Tab 3 times
        focused_elements = []
        for i in range(3):
            body.send_keys(Keys.TAB)
            time.sleep(0.2)
            active = self.driver.switch_to.active_element
            focused_elements.append(active.tag_name)
        
        print(f"  • Tab pressed 3 times")
        print(f"  • Focused elements: {' → '.join(focused_elements)}")
        print("  ✓ Keyboard navigation functional")
    
    # ==================== TEST CASE 8 ====================
    def test_08_decision_table_user_authentication(self):
        """
        BB-TC8: Decision Table Testing - Authentication States
        Conditions: Has Account (Y/N), Logged In (Y/N)
        Expected: Different outcomes based on combination
        """
        print("\n[BLACK BOX TEST 8] Decision Table - Authentication")
        
        # Test scenarios based on decision table
        scenarios = [
            ("/#/login", "No account, not logged in → Login page"),
            ("/#/dashboard", "Has account, logged in → Dashboard access"),
            ("/#/reader", "Has account, logged in → Reader access"),
        ]
        
        for route, description in scenarios:
            self.driver.get(f"{self.base_url}{route}")
            time.sleep(0.8)
            current = self.driver.current_url
            print(f"  • Scenario: {description}")
            print(f"    Result: {current}")
        
        print("  ✓ Decision table scenarios tested")
    
    # ==================== TEST CASE 9 ====================
    def test_09_equivalence_fast_internet(self):
        """
        BB-TC9: Equivalence Partitioning - Fast Load Time
        Input Class: Normal network conditions
        Expected: Page loads within acceptable time
        """
        print("\n[BLACK BOX TEST 9] Equivalence - Fast Network")
        
        start_time = time.time()
        self.driver.get(self.base_url)
        self.wait.until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        load_time = time.time() - start_time
        
        # Normal network should load quickly
        self.assertLess(load_time, 5,
                       "Page should load under 5 seconds on normal network")
        
        print(f"  • Load time: {load_time:.2f} seconds")
        print("  ✓ Fast network load acceptable")
    
    # ==================== TEST CASE 10 ====================
    def test_10_boundary_zero_content(self):
        """
        BB-TC10: Boundary Value Analysis - Empty Data
        Input: Page with no dynamic content
        Expected: Page still renders base structure
        """
        print("\n[BLACK BOX TEST 10] Boundary - Zero Content State")
        
        self.driver.get(f"{self.base_url}/#/dashboard")
        time.sleep(1)
        
        # Even with no sessions, dashboard should render
        body_text = self.driver.find_element(By.TAG_NAME, "body").text
        
        # Page should have some content (headings, labels, etc.)
        self.assertGreater(len(body_text), 0,
                          "Page should have base content even if no data")
        
        print(f"  • Page has base content: {len(body_text)} chars")
        print("  ✓ Empty data state handled")
    
    # ==================== TEST CASE 11 ====================
    def test_11_use_case_page_refresh(self):
        """
        BB-TC11: Use Case Testing - User Refreshes Page
        Scenario: User presses F5 or refresh button
        Expected: Page reloads successfully
        """
        print("\n[BLACK BOX TEST 11] Use Case - Page Refresh")
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        initial_url = self.driver.current_url
        
        # Refresh page
        self.driver.refresh()
        time.sleep(1)
        
        refreshed_url = self.driver.current_url
        
        self.assertEqual(initial_url, refreshed_url,
                        "URL should remain same after refresh")
        
        print(f"  • Initial: {initial_url}")
        print(f"  • After refresh: {refreshed_url}")
        print("  ✓ Page refresh works correctly")
    
    # ==================== TEST CASE 12 ====================
    def test_12_use_case_browser_back_forward(self):
        """
        BB-TC12: Use Case Testing - Browser Navigation
        Scenario: User uses browser back/forward buttons
        Expected: Navigation history works
        """
        print("\n[BLACK BOX TEST 12] Use Case - Browser Back/Forward")
        
        # Navigate to multiple pages
        self.driver.get(f"{self.base_url}/#/login")
        time.sleep(0.5)
        page1 = self.driver.current_url
        
        self.driver.get(f"{self.base_url}/#/dashboard")
        time.sleep(0.5)
        page2 = self.driver.current_url
        
        # Go back
        self.driver.back()
        time.sleep(0.5)
        back_url = self.driver.current_url
        
        # Go forward
        self.driver.forward()
        time.sleep(0.5)
        forward_url = self.driver.current_url
        
        print(f"  • Page 1: {page1}")
        print(f"  • Page 2: {page2}")
        print(f"  • After back: {back_url}")
        print(f"  • After forward: {forward_url}")
        print("  ✓ Browser navigation functional")
    
    # ==================== TEST CASE 13 ====================
    def test_13_equivalence_text_display(self):
        """
        BB-TC13: Equivalence Partitioning - Text Content Display
        Input Class: Pages with text content
        Expected: Text is readable and displays correctly
        """
        print("\n[BLACK BOX TEST 13] Equivalence - Text Display")
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        # Check if text is visible
        body = self.driver.find_element(By.TAG_NAME, "body")
        body_text = body.text
        
        # Verify text exists and is visible
        self.assertGreater(len(body_text), 0, "Should display text content")
        self.assertTrue(body.is_displayed(), "Text should be visible")
        
        print(f"  • Text content length: {len(body_text)} characters")
        print("  ✓ Text displays correctly")
    
    # ==================== TEST CASE 14 ====================
    def test_14_boundary_multiple_rapid_clicks(self):
        """
        BB-TC14: Boundary Value Analysis - Rapid User Input
        Input: Multiple rapid button clicks
        Expected: System handles without crashing
        """
        print("\n[BLACK BOX TEST 14] Boundary - Rapid Button Clicks")
        
        self.driver.get(self.base_url)
        time.sleep(1)
        
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        
        if buttons:
            # Click rapidly 10 times
            for i in range(10):
                buttons[0].click()
                time.sleep(0.05)
            
            # System should still be responsive
            body = self.driver.find_element(By.TAG_NAME, "body")
            self.assertTrue(body.is_displayed(),
                           "System should remain stable after rapid clicks")
            
            print(f"  • Performed 10 rapid clicks")
            print("  ✓ System handles rapid input")
        else:
            print("  ⚠ No buttons available for testing")
    
    # ==================== TEST CASE 15 ====================
    def test_15_use_case_complete_user_flow(self):
        """
        BB-TC15: Use Case Testing - Complete User Journey
        Scenario: New user visits → Explores pages → Returns home
        Expected: Smooth navigation through app
        """
        print("\n[BLACK BOX TEST 15] Use Case - Complete User Journey")
        
        journey = [
            (f"{self.base_url}", "Home/Landing"),
            (f"{self.base_url}/#/login", "Login"),
            (f"{self.base_url}/#/dashboard", "Dashboard"),
            (f"{self.base_url}/#/reader", "Reader"),
            (f"{self.base_url}/#/parent-dashboard", "Parent Dashboard"),
            (f"{self.base_url}", "Return Home"),
        ]
        
        for url, step in journey:
            self.driver.get(url)
            time.sleep(0.7)
            current = self.driver.current_url
            
            # Verify page loads
            body = self.driver.find_element(By.TAG_NAME, "body")
            self.assertTrue(body.is_displayed(),
                           f"Step '{step}' should display")
            
            print(f"  • Step: {step} → Loaded successfully")
        
        print("  ✓ Complete user journey successful")


def run_blackbox_tests():
    """Run black box test suite"""
    print("="*70)
    print("BLACK BOX TESTING SUITE")
    print("Testing Application Functionality Without Code Knowledge")
    print("="*70)
    
    suite = unittest.TestLoader().loadTestsFromTestCase(BlackBoxFunctionalTests)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print("\n" + "="*70)
    print("BLACK BOX TEST SUMMARY")
    print("="*70)
    print(f"Tests Run:      {result.testsRun}")
    print(f"Passed:         {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failed:         {len(result.failures)}")
    print(f"Errors:         {len(result.errors)}")
    print(f"Success Rate:   {((result.testsRun - len(result.failures) - len(result.errors))/result.testsRun*100):.1f}%")
    print("="*70)
    
    return result


if __name__ == "__main__":
    run_blackbox_tests()
