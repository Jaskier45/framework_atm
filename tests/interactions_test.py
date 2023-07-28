from pages.interactions_page import SortTablePage, SelectablePage


class TestInteractions:

    class TestSortableTest:

        def test_sort_table(self, driver):
            sort_table = SortTablePage(driver, 'https://demoqa.com/sortable')
            sort_table.open()
            list_before, list_after = sort_table.change_list_order()
            grid_before, grid_after = sort_table.change_grid_list_order()
            assert grid_before != grid_after
            assert list_before != list_after

    class TestSelectablePage:
        def test_selectable(self, driver):
            selectable_page = SelectablePage(driver, 'https://demoqa.com/selectable')
            selectable_page.open()
            item_list = selectable_page.select_list_item()
            item_grid = selectable_page.select_grid_item()
            assert len(item_list) > 0
            assert len(item_grid) > 0
            