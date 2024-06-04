class End:
    def __init__(self, **kwargs):
        default_kwargs = {}
        kwargs = default_kwargs | kwargs

    def __str__(self):
        return """
    });"""

    def get_additional_styles(self):
        return {}

    def get_additional_imports(self):
        return {}

    @staticmethod
    def get_xeokit_modules_needed():
        return {}
