from kivy.app import App
from kivy.uix.treeview import TreeView, TreeViewNode, TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label


class TreeViewDemo(App):
    def build(self):
        boxLayout = BoxLayout()
        tv = TreeView()
        for i in range(5):
            node = TreeViewButton()
            for i2 in range(5):
                node.add_widget(Label())
            tv.add_node(node)
        # tv.root_options.set
        #tv.add_node(TreeViewLabel(text='My first item'))
        #tv.add_node(TreeViewLabel(text='My second item'))
        boxLayout.add_widget(tv)
        return boxLayout

class TreeViewButton(Label, TreeViewNode):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    TreeViewDemo().run()
