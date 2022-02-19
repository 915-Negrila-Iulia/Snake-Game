class SettingsProperties:
    def __init__(self, file_name="settings_properties.txt"):
        self._settings_data = {}
        self._load(file_name)

    @property
    def settings_data(self):
        return self._settings_data

    @property
    def dim_type(self):
        return self._settings_data["dim"]

    @property
    def count(self):
        return self._settings_data["count"]

    def _load(self,file_name):
        file = open(file_name, 'rt')
        lines = file.readlines()
        file.close()

        for line in lines:
            [property, value] = line.split('=', 1)
            property = property.strip()
            value = value.strip()
            self._settings_data[property] = value
