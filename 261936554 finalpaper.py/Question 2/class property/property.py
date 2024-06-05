class Property():
    def __init__(self,property_id,name,location,descripton,price_per_night,avalaibilty_status)
        self.property_id = property_id
        self.name = name
        self.location = location
        self.description = description
        self.price_per_night = price_per_night
        self.avalaibilty_status = avalaibilty_status
        self.host = None

    def set_availability(self, start_date, end_date, status = True):
        for date in range (start_date, end_date):
            self.availability[date] = status

    def is_available(self, start_date, end_date):
        for date in range (start_date, end_date):
            if date in self.availability and not self.availability[date]:
                return False
        return True

    def update_availability(self, start_date, end_date, status):
        for date in range (start_date, end_date):
            self.availability[date] = status
