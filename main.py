import random
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from config import *
from loguru import logger
from utils import *

logger.add('log.log', format="<yellow>{time:YYYY-MM-DD at HH:mm:ss}</yellow> | <level>{level}</level>: <level>{message}</level>")


def main(private_key: str):
    for t in range(MAX_TRIES_FOR_ADDRESS):
        logger.info(f"{private_key[:10]}...") 
        try:
            with get_chromedriver() as driver:
                driver.get('https://www.sei20.xyz/explorer/token/seis')

                switch_to_window_title(driver, 'Compass Wallet for Sei')

                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testing-id = 'import-private-key']"))).click()
                sleep(random.uniform(0.5, 1.5))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//textarea'))).send_keys(private_key)
                sleep(random.uniform(0.5, 1.5))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testing-id = 'btn-import-wallet']"))).click()
                sleep(random.uniform(0.5, 1.5))
                inputs = driver.find_elements(By.XPATH, "//input")
                inputs[0].send_keys("SAFA!fsdf4gfsd")
                inputs[1].send_keys("SAFA!fsdf4gfsd")
                sleep(random.uniform(0.5, 1.5))
                inputs[1].send_keys(Keys.ENTER)
                sleep(random.uniform(0.5, 1.5))
                driver.close()

                switch_to_window_title(driver, 'Sei 20')

                sleep(random.uniform(0.5, 1.5))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[text() = 'Connect Wallet']"))).click()
                sleep(random.uniform(2, 3))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Compass']"))).click()
                switch_to_window_title(driver, 'Compass Wallet for Sei')
                sleep(random.uniform(2, 3))
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Connect']"))).click()
                sleep(random.uniform(2, 3))
                switch_to_window_title(driver, 'Sei 20')

                for count_mint in range(random.randrange(SELF_MINT_COUNT[0], SELF_MINT_COUNT[1])):
                    for t in range(MAX_TRIES_FOR_MINT):
                        try:
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Mint']"))).click()
                            sleep(random.uniform(0.5, 1.5))
                            switch_to_window_title(driver, 'Compass Wallet for Sei')
                            sleep(random.uniform(0.8, 1.5))
                            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[text() = 'Approve']"))).click()
                            switch_to_window_title(driver, 'Sei 20')
                            sleep(random.uniform(0.8, 1.5))
                            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//span[text() = 'Close']"))).click()
                            logger.success(f"{private_key[:10]}... | SUCCESS MINT | {count_mint+1}")
                            mint_wait_time = random.randrange(round(NEXT_MINT_MIN_WAIT_TIME), round(NEXT_MINT_MAX_WAIT_TIME))
                            with console.status(f"[bold green]Wait {mint_wait_time}s", spinner="simpleDotsScrolling") as status:
                                sleep(mint_wait_time)
                            break
                        except:
                            logger.warning(f"{private_key[:10]}... | FAIL MINT | {count_mint+1} | TRY {t+1}/{MAX_TRIES_FOR_MINT}")
            break
        except:
            ex = get_error_message()
            logger.error(f"{private_key[:10]}... Try {t+1}/{MAX_TRIES_FOR_ADDRESS} Error: {ex}")
        finally:
            try:
                driver.quit()
            except:
                pass

    
if __name__ == '__main__':
    console = Console()
    print_welcome()
    logger.info("START")

    with open("private_keys.txt", "r") as f:
        private_keys = f.read().splitlines()
        while "" in private_keys:
            private_keys.remove("")

    for private_key in private_keys:
        main(private_key)
        address_wait_time = random.randrange(round(NEXT_ADDRESS_MIN_WAIT_TIME*60), round(NEXT_ADDRESS_MAX_WAIT_TIME*60))
        with console.status(f"[bold green]Wait {address_wait_time}s", spinner="simpleDotsScrolling") as status:
            sleep(address_wait_time)

    logger.info("FINAL")

    
