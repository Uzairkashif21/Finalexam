host1=Host(1, "Uzair Kashif", "Uzair@gmail.com")
guest1=Guest(2, "Ahmed Rana", "Ahmed@gmail.com")

#property
property1 = Property(1, "mm alam", "LHR", "Commercial area", 999.0)
property1.set_availability(date(2024, 6, 6), date(2024, 6, 11))

#Hostproperty
host1.list_property(property1)

#Guestbookingproperty
booking1 = guest1.book_property(property1, date(2024,6 3), date(2024, 6, 5))
    print(f"Booking confirmed: {booking1.booking_id}")


# Checking avail after booking
is_available = property1.is_available(date(2024,6,6), date(2024, 6, 8))
print(f"Is property available from June 3 to June 5: {is_available}")
