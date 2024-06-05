class User:
    def __init__(self, name, user_id, contact_details):
        self.name = name
        self.userid = user_id
        self.contact_details = contact_details


class Host(User):
    def __init__(self, userid, name, contact_details):
        super().__init__(userid, name, contact_details)
        self.properties = []


    def list_property(self, _property):
        self.properties.append(_property)
        property.host = self

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



class Property():
    def __init__(self,property_id,name,location,descripton,price_per_night,avalaibilty_status):
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


class Booking():
    def __init__(self,booking_ID,_property,guest,check_indate, check_out_date):
        self.booking_ID = booking_ID
        self._property =  _property
        self.guest = guest
        self.checkin_date = check_indate
        self.check_out_date  = check_out_date
        self.status = "confirmed"
class Review:
    def __init__(self, review_id, _property, guest, rating, comment):
        self.review_id = review_id
        self.property = _property
        self.guest = guest
        self.rating = rating
        self.comment = comment        
        
    

host1=Host(1, "Uzair Kashif", "Uzair@gmail.com")
guest1=Guest(2, "Ahmed Rana", "Ahmed@gmail.com")

#property
property1 = Property(1, "mm alam", "LHR", "Commercial area", 999.0)
property1.set_availability(date(2024, 6, 6), date(2024, 6, 11))

#Hostproperty
host1.list_property(property1)

#Guestbookingproperty
booking1 = guest1.book_property(property1, date(2024,6, 3), date(2024, 6, 5))
print(f"Booking confirmed: {booking1.booking_id}")


# Checking avail after booking
is_available = property1.is_available(date(2024,6,6), date(2024, 6, 8))
print(f"Is property available from June 3 to June 5: {is_available}")





























