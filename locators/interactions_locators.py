import random

from selenium.webdriver.common.by import By


class SortTableLocators:
    List_tab = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    List_item = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

    Grid_tab = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    Grid_item = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectableLocators:
    TAB_LIST = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
    LIST_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item list-group-item-action"]')
    LIST_ACTIVE_ITEM = (By.CSS_SELECTOR, 'li[class="mt-2 list-group-item active list-group-item-action"]')
    TAB_GRID = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
    GRID_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item list-group-item-action"]')
    GRID_ACTIVE_ITEM = (By.CSS_SELECTOR, 'li[class="list-group-item active list-group-item-action"]')


class ResizablePageLocators:
    RESIZABLE_BOX_HANDLE = (
        By.CSS_SELECTOR, 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE_BOX = (By.CSS_SELECTOR, 'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR,
                        'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')


class Simple_dragLocators:
    Simple_button = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    Simple_drag_button = (By.CSS_SELECTOR, 'div[id="draggable"]')
    Simple_drag_here = (By.CSS_SELECTOR, '#simpleDropContainer #droppable')

    #Accept
    Accept_button = (By.CSS_SELECTOR, "a[id='droppableExample-tab-accept']")
    Acceptable_button = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    Not_Acceptable_button = (By.CSS_SELECTOR, '#notAcceptable')
    Accept_drop_here = (By.CSS_SELECTOR, '#acceptDropContainer #droppable')

    #Prevent
    Prevent_button = (By.CSS_SELECTOR, '#droppableExample-tab-preventPropogation')
    Prevent_drag_me = (By.CSS_SELECTOR, '#dragBox')
    Prevent_first_box = (By.CSS_SELECTOR, '#notGreedyDropBox')
    Prevent_second_box = (By.CSS_SELECTOR, '#greedyDropBoxInner')
    Prevent_third_box = (By.CSS_SELECTOR, '#greedyDropBox > p')

    #Revert
    Revert_button = (By.CSS_SELECTOR, '#droppableExample-tab-revertable')
    Will_revert = (By.CSS_SELECTOR, '#revertable')
    Not_revert = (By.CSS_SELECTOR, '#notRevertable')
    Revert_area = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')

