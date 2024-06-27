import annotations_clickShowLabels
import annotations_hoverShowLabels
import time

def test_runner():
    annotations_clickShowLabels.test_if_labels_are_visible_after_click()
    time.sleep(2)
    annotations_hoverShowLabels.test_if_labels_are_visible_after_hover()
    time.sleep(2)
