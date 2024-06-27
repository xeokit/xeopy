import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_if_labels_are_visible_after_click():
    browser = webdriver.Firefox()
    browser.get('https://xeokit.github.io/xeokit-sdk/examples/annotations/#annotations_clickShowLabels')
    time.sleep(2)
    iframe = browser.find_element(By.ID, "viewer")
    browser.switch_to.frame(iframe)
    time.sleep(2)
    annotation_markers = browser.find_elements(By.CLASS_NAME, "annotation-marker")
    annotation_labels = browser.find_elements(By.CLASS_NAME, "annotation-label")

    for i in range(3):
        annotation_marker = annotation_markers[i]
        annotation_label = annotation_labels[i]
        assert annotation_label.is_displayed() is False
        annotation_marker.click()
        time.sleep(0.5)
        assert annotation_label.is_displayed() is True
        time.sleep(1)

    browser.quit()
