Bob's Ski & Snowboard Rentals - Class Library

Name- Maurice Toney
Course - CPDM 120  



Description
This is a class library for Bob's Ski and Snowboard Rentals. It has the
classes, properties, and methods needed to build the rental app in Part 2.



Classes

RentalEquipment - parent class. Holds the shared rates and inventory, plus
the best price calculation and inventory reduce/restore methods.

Ski - inherits from RentalEquipment. Sets the ski rates.

Snowboard - inherits from RentalEquipment. Sets snowboard rates.

Customer - stores the customer's name and ID.

RentalShop - owns the ski and snowboard inventory. Has the discount methods
and tracks daily totals.

Rental - one customer's rental. Calculates the estimate and final bill.



Properties and methods

get_best_price - returns the cheapest price
for the rental.

reduce_inventory(quantity) and restore_inventory(quantity) - adjusts how
much inventory is available.

RentalShop.calculate_final_price -
applies the family discount then the coupon discount.

RentalShop.add_daily_totals - tracks how many items were rented and total
revenue for the day.

Rental.calculate_estimate(rental_shop) - gets the estimated price before the
rental happens.

Rental.calculate_final_bill(rental_shop, actual_units) - gets the final
price based on how long the equipment was actually rented for.

 
OOP concepts

Encapsulation - properties have setters that validate the values so you
can't set a negative rate or negative inventory.

Inheritance - Ski and Snowboard both inherit from RentalEquipment instead
of repeating the same code.

Polymorphism - get_equipment_type() is overridden in Ski and Snowboard so
it returns something different for each one.

Abstraction - get_best_price() hides all the rate comparison logic behind
one method call.


Running the test file help

1. Open the BobsRentals_Toney folder in Visual Studio 
2. Right click test_classes.py in solution explorer and click "Set as
   Startup File."
3. Run the project and check the output.