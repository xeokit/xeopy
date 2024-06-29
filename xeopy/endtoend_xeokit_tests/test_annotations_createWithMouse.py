import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_if_annotations_are_added_after_click():
    browser = webdriver.Firefox()
    browser.get('https://xeokit.github.io/xeokit-sdk/examples/annotations/#annotations_createWithMouse')
    browser.set_window_size(1920, 1080)
    time.sleep(2)
    iframe = browser.find_element(By.ID, "viewer")
    browser.switch_to.frame(iframe)
    annotation_markers = browser.find_elements(By.CLASS_NAME, "annotation-marker")
    assert len(annotation_markers) == 0
    rectangle = iframe.rect
    position = iframe.location
    action = webdriver.common.action_chains.ActionChains(browser)
    action.move_by_offset(position["x"] + rectangle["width"] / 2, position["y"] + rectangle["height"] / 2)
    action.click()
    action.perform()
    time.sleep(1)
    annotation_markers = browser.find_elements(By.CLASS_NAME, "annotation-marker")
    assert len(annotation_markers) == 1

    browser.quit()
