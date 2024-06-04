
class SectionPlane:
    def __init__(self, **kwargs):
        default_kwargs = {"variable_name": "sectionPlane",
                          "section_planes_plugin_variable_name": "sectionPlanes",
                          "id": "mySectionPlane",
                          "position": [10.95, 1.95, -10.35],
                          "direction": [0.0, -1.0, 0.0],
                          "show_control": True}
        kwargs = default_kwargs | kwargs
        self.variable_name = kwargs["variable_name"]
        self.section_planes_plugin_variable_name = kwargs["section_planes_plugin_variable_name"]
        self.id = kwargs["id"]
        self.position = kwargs["position"]
        self.direction = kwargs["direction"]
        self.show_control = kwargs["show_control"]

    def __str__(self):
        show_control_line = ""
        if self.show_control:
            show_control_line = "".join(["\n", self.section_planes_plugin_variable_name, ".showControl(", "\"", self.id, "\"", ")", "\n"])

        return "".join(
            ["const ", self.variable_name, " = ", self.section_planes_plugin_variable_name, ".createSectionPlane({", "\n",
             "id: \"", self.id, "\",", "\n",
             "pos: ", str(self.position), ",", "\n",
             "dir: ", str(self.direction), ",", "\n",
             "});", show_control_line])

    def get_additional_styles(self):
        return {}

    def get_additional_imports(self):
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {}
