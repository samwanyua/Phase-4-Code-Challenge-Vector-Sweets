from app import app, db
from models import Vendor, Sweet, VendorSweet
from random import choice as rc, randrange

if __name__ == '__main__':
    with app.app_context():
        print("Clearing db...")
        db.drop_all()
        db.create_all()

        print("Seeding vendors...")
        vendors = [
            Vendor(name="Insomnia Cookies"),
            Vendor(name="Cookies Cream"),
            Vendor(name="Carvel"),
            Vendor(name="Gregory's Coffee"),
            Vendor(name="Duane Park Patisserie"),
            Vendor(name="Tribeca Treats"),

        ]

        db.session.add_all(vendors)

        print("Seeding sweets...")
        sweets = [
            Sweet(name="Chocolate Chip Cookie"),
            Sweet(name="Chocolate Chunk Cookie"),
            Sweet(name="M&Ms Cookie"),
            Sweet(name="White Chocolate Cookie"),
            Sweet(name="Brownie"),
            Sweet(name="Peanut Butter Icecream Cake"),
        ]

        db.session.add_all(sweets)

        print("Seeding vendor sweets...")
        vendor_sweets = []
        for sweet in sweets:
            vendor = rc(vendors)
            vendor_sweets.append(
                VendorSweet(sweet=sweet, vendor=vendor, price=randrange(50))
            )
        db.session.add_all(vendor_sweets)
        db.session.commit()

        print("Done seeding!")
