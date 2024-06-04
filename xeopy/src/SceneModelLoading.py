class SceneModelLoading:
    def __init__(self, **kwargs):
        default_kwargs = {"variable_name": "sceneModel",
                          "loader_variable_name": "loader",
                          "path": "Duplex.ifc",
                          "edges": True,
                          }
        kwargs = default_kwargs | kwargs
        self.variable_name = kwargs["variable_name"]
        self.loader_variable_name = kwargs["loader_variable_name"]
        self.path = kwargs["path"]
        self.edges = kwargs["edges"]

    def __str__(self):
        return """
        const """ + self.variable_name + """ = """ + self.loader_variable_name + """.load({
            src: \"""" + self.path + """\",
            edges: """ + str(self.edges).lower() + """
        });
"""

    def get_additional_styles(self):
        return {}

    def get_additional_imports(self):
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {}
