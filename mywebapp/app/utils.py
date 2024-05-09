# mywebapp/core/utils.py

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from .models import ProductUpdateHistory, ProductMaster


def add_to_cart(asin_list):
    # Configure Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    try:
        for asin_number in asin_list:
            # Navigate to Amazon product page
            product_url = f'https://www.amazon.com/dp/{asin_number}'
            driver.get(product_url)

            # Perform action: Add to cart
            add_to_cart_button = driver.find_element_by_id('add-to-cart-button')
            add_to_cart_button.click()

            # Record the current count in the database
            current_count_element = driver.find_element_by_id('nav-cart-count')
            current_count = int(current_count_element.text)

            # Save the current count in the database
            ProductUpdateHistory.objects.create(
                asin=asin_number,
                current_count=current_count
            )
    finally:
        driver.quit()


def navigate_asin_list(asin_list):
    driver = webdriver.Chrome()  # Initialize WebDriver
    try:
        for asin in asin_list:
            driver.get(f"https://www.amazon.com/dp/{asin}")  # Navigate to Amazon product page
            time.sleep(2)  # Wait for page to load
            # Perform actions such as adding the product to cart, recording counts, etc.
            print(f"Product with ASIN {asin} added to cart successfully.")
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    finally:
        driver.quit()  # Close the browser window
def view_product():
    # Fetch all products from the database
    return ProductMaster.objects.all()