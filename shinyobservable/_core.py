class Observable(object):
    def __init__(self, notebook):
        self.notebook = notebook

    def to_dict(self):
        return dict(notebook=self.notebook)
