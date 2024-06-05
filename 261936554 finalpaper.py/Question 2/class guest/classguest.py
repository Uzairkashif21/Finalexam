class Guest(User):
    def __init__(self, user_id,name,contact_details):
        super().__init__(user_id,name,contact_details)
        self.bookings=[]

    def book_property(self, _property, check_in_date, check_out_date):
        if _property.is_available(check_in_date, check_out_date):
            booking = Booking(len(self.bookings) + 1, _property, self, check_in_date, check_out_date)
            self.bookings.append(booking)
            _property.update_availability(check_in_date, check_out_date, False)
            return booking
        else:
            ("For the dates provided booking is not avaialable.")
