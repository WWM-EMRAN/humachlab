from django.forms.widgets import ClearableFileInput

class MultipleFileInput(ClearableFileInput):
    allow_multiple_selected = True

    def format_value(self, value):
        """Format the value for display in the widget."""
        if not value:
            return None
        if isinstance(value, list):
            return [super().format_value(v) for v in value]
        return super().format_value(value)

