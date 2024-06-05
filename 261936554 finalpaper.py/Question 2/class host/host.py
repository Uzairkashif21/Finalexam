class Host(User):
    def __init__(self, userid, name, contact_details):
        super().__init__(userid, name, contact_details)
        self.properties = []


   def list_property(self, _property):
        self.properties.append(_property)
        property.host = self
