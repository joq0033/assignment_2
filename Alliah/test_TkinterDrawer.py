import unittest
from tkinter_drawer import TkinterDrawer
from parsers import ArgumentParser
from source_reader import ArgumentSourceReader
from turtle_drawer import TurtleDrawer


class TestTkinterDrawer(unittest.TestCase):

    def setUp(self):
        self.tkinterDrawer = TkinterDrawer()
        self.Drawer = TkinterDrawer()

    def test_select_pen(self):
        raised = False
        try:
            self.tkinterDrawer.select_pen(1)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    # def test_pen_down(self):
    #     self.tkinterDrawer.pen_down()
    #     self.assertTrue(self.tkinterDrawer.pen_state)

    def test_pen_down(self):
        raised = False
        try:
            self.tkinterDrawer.pen_down(250, 50)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    # def test_pen_up(self):
    #     self.tkinterDrawer.pen_up()
    #     self.assertFalse(self.tkinterDrawer.pen_state)

    def test_pen_up(self):
        raised = False
        try:
            self.tkinterDrawer.pen_down(50, 250)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_go_along(self):
        raised = False
        try:
            self.tkinterDrawer.go_along(self.tkinterDrawer.x(50))
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_go_down(self):
        raised = False
        try:
            self.tkinterDrawer.go_down(self.tkinterDrawer.y(50))
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_line(self):
        raised = False
        try:
            self.tkinterDrawer.draw_line(90)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_square(self):
        raised = False
        try:
            self.tkinterDrawer.draw_square(0, 90, 180, 270)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_circle(self):
        raised = False
        try:
            self.tkinterDrawer.draw_circle(self.tkinterDrawer.c.create_oval())
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")

    def test_draw_triangle(self):
        raised = False
        try:
            self.Drawer.draw_triangle(self.Drawer.c.create_line())
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")


class TestArgumentSourceReader(unittest.TestCase):

    def setUp(self):
        self.Reader = ArgumentSourceReader(ArgumentParser(TurtleDrawer()))
        self.source = ['-e', '-t', '-k', '-g']

    def test_go(self):
        raised = False
        try:
            self.Reader.go(self.source)
        except:
            raised = True
        self.assertTrue(raised, "Error Raised")


class TestArgumentParser(unittest.TestCase):

    def setUp(self):
        self.tkinterParser = ArgumentParser(TurtleDrawer())
        self.source = ['-c', '-e', '-t', '-k', '-g', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    def test_parse(self):
        raised = False
        try:
            self.tkinterParser.parse(self.source)
        except:
            raised = True
        self.assertFalse(raised, "Error Raised")

#
# class TestIntegerParser(unittest.TestCase):
#         def setUp(self):
#             self.tkinterIntParser = IntegerParser(TurtleDrawer())
#             self.source = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#         def test_parse(self):
#             raised = False
#             try:
#                 self.tkinterIntParser.parse(self.source)
#             except:
#                 raised = True
#             self.assertTrue(raised, "Error Raised")
#
#
# class TestStringParser(unittest.TestCase):
#
#         def setUp(self):
#             self.tkinterStrParser = StringParser(TurtleDrawer())
#             self.source = ['-c', '-e', '-t', '-k', '-g']
#
#         def test_parse(self):
#             raised = False
#             try:
#                 self.tkinterStrParser.parse(self.source)
#             except:
#                 raised = True
#             self.assertFalse(raised, "Error Raised")

if __name__ == '__main__':
    unittest.main()
