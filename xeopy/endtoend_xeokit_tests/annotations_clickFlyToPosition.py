import pytest
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import cv2
from ImageTools.ImageTools import *

def test_if_after_click_on_label_camera_flies_to_it():
    browser = webdriver.Firefox()
    browser.get('https://xeokit.github.io/xeokit-sdk/examples/annotations/#annotations_clickFlyToPosition')
    browser.set_window_size(1920, 1080)
    time.sleep(2)
    iframe = browser.find_element(By.ID, "viewer")
    browser.switch_to.frame(iframe)
    time.sleep(2)
    browser.save_screenshot(os.path.join("annotations_clickFlyToPosition", "actual_before_click.png"))
    annotation_markers = browser.find_elements(By.CLASS_NAME, "annotation-marker")
    annotation_marker = annotation_markers[5]
    annotation_marker.click()
    time.sleep(1)
    browser.save_screenshot(os.path.join("annotations_clickFlyToPosition", "actual_after_click.png"))

    assert ImageTools.calculate_mean_squared_error(cv2.imread(os.path.join("annotations_clickFlyToPosition", "actual_before_click.png")),
                                                   cv2.imread(os.path.join("annotations_clickFlyToPosition", "expected_before_click.png"))) < 0.5

    assert ImageTools.calculate_mean_squared_error(cv2.imread(os.path.join("annotations_clickFlyToPosition", "actual_after_click.png")),
                                                   cv2.imread(os.path.join("annotations_clickFlyToPosition", "expected_after_click.png"))) < 0.5

    browser.quit()
