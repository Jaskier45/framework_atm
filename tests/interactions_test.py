from pages.interactions_page import SortTablePage


class TestInteractions:

    class TestSortableTest:

        def test_sort_table(self, driver):
            sort_table = SortTablePage(driver, 'https://demoqa.com/sortable')
            sort_table.open()
            list_before, list_after = sort_table.change_list_order()
            grid_before, grid_after = sort_table.change_grid_list_order()
            assert grid_before != grid_after
            assert list_before != list_after

