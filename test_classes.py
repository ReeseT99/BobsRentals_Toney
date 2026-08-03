#tests

from ski import Ski
from snowboard import Snowboard
from customer import Customer
from rental_shop import RentalShop
from rental import Rental

#-----------------------------------------------------------------------
# Main
#-----------------------------------------------------------------------
def main():

    test_ski = Ski(10)
    test_snowboard = Snowboard(8)
    print("Ski hourly rate:", test_ski.hourly_rate)
    print("Snowboard hourly rate:", test_snowboard.hourly_rate)

    print("Ski get_equipment_type():", test_ski.get_equipment_type())
    print("Snowboard get_equipment_type():", test_snowboard.get_equipment_type())

    test_ski.display_info()
    test_ski.display_info(False)

    best_price = test_ski.get_best_price(1, "hourly", 4)
    print("Bestprice for 4 hour ski rental:", best_price)

    test_customer = Customer("Maurice Toney", "1")
    print("Customer name:", test_customer.name)
    print("Customer ID:", test_customer.id_number)

    shop = RentalShop(20, 15)
    print("Available skis before rental:", shop.ski_inventory.quantity_available)
    shop.rent_skis(3)
    print("Available skis after renting 3:", shop.ski_inventory.quantity_available)
    shop.return_skis(1)
    print("Available skis after returning 1:", shop.ski_inventory.quantity_available)

    family_price = shop.calculate_family_discount(200, 4)
    print("Price after family discount:", family_price)
    coupon_price = shop.calculate_coupon_discount(200, "SAVE10BBP")
    print("Price after coupon discount:", coupon_price)
    both_price = shop.calculate_final_price(200, 4, "SAVE10BBP")
    print("Price after both discounts:", both_price)

    rental = Rental(test_customer, "hourly", 4, "SAVE10BBP")
    rental.add_skis(2)
    rental.add_snowboards(1)
    estimate = rental.calculate_estimate(shop)
    print("Rental estimate:", estimate)
    final_bill = rental.calculate_final_bill(shop, 6)
    print("Final bill after 6 hours:", final_bill)

    shop.add_daily_totals(2, 1, final_bill)
    print("Daily skis rented:", shop.daily_skis_rented)
    print("Daily snowboards rented:", shop.daily_snowboards_rented)
    print("Daily revenue:", shop.daily_revenue)


main()