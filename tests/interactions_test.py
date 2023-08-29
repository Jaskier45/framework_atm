from pages.interactions_page import SortTablePage, SelectablePage, ResizablePage, Simple_drag


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

    class TestResizablePage:
        def test_resizable(self, driver):
            resize_page = ResizablePage(driver, 'https://demoqa.com/resizable')
            resize_page.open()
            max_box, min_box = resize_page.change_size_resizable_box()
            max_resize, min_resize = resize_page.change_size_resizable()
            assert ('500px', '300px') == max_box
            assert ('150px', '150px') == min_box
            assert min_resize != max_resize

    class TestDropTablePage:
        def test_simple(self, driver):
            simple_page = Simple_drag(driver, 'https://demoqa.com/droppable')
            simple_page.open()
            simple_text = simple_page.drag_simple_form()
            assert simple_text == 'Dropped!', 'The element has not been dropped!'

        def test_accept(self, driver):
            accept_page = Simple_drag(driver, 'https://demoqa.com/droppable')
            accept_page.open()
            not_accept, accept = accept_page.drag_accept_form()
            assert not_accept == 'Drop here', 'The dropped element has been accepted!'
            assert accept == 'Dropped!', 'The dropped element has not been accepted!'


        def test_prevent(self, driver):
            prevent_page = Simple_drag(driver, 'https://demoqa.com/droppable')
            prevent_page.open()
            first_text, second_text, third_text = prevent_page.drag_prevent_form()
            assert first_text == 'Dropped!Dropped!'
            assert second_text == 'Dropped!'
            assert third_text == 'Dropped!'

        def test_revert(self, driver):
            revent_page = Simple_drag(driver, 'https://demoqa.com/droppable')
            revent_page.open()
            after_move, after_revent, after_not_move, after_not_revent = revent_page.drop_will_revert()
            assert after_move != after_revent
            assert after_not_revent == after_not_move
