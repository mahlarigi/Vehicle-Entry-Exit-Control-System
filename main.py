from vehicle import Vehicle
from gate import Gate
from access_permission import AccessPermission

vehicles = []
gates = []
permissions = AccessPermission()

while True:
    print("\n===== سیستم کنترل ورود و خروج خودرو =====")
    print("1. تعریف خودرو")
    print("2. تعریف راهبند")
    print("3. تعیین سطح دسترسی")
    print("4. بررسی مجوز ورود")
    print("5. نمایش خودروها")
    print("6. نمایش راهبندها")
    print("7. خروج")

    choice = input("انتخاب کنید: ")

    if choice == "1":
        plate = input("پلاک: ")
        model = input("مدل خودرو: ")
        owner = input("نام مالک: ")
        vehicles.append(Vehicle(plate, model, owner))
        print("خودرو ثبت شد.")

    elif choice == "2":
        gate_id = input("شناسه راهبند: ")
        gate_name = input("نام راهبند: ")
        location = input("محل راهبند: ")
        gates.append(Gate(gate_id, gate_name, location))
        print("راهبند ثبت شد.")

    elif choice == "3":
        plate = input("پلاک خودرو: ")
        gate_id = input("شناسه راهبند: ")
        permissions.add_permission(plate, gate_id)
        print("دسترسی ثبت شد.")

    elif choice == "4":
        plate = input("پلاک خودرو: ")
        gate_id = input("شناسه راهبند: ")

        if permissions.check_access(plate, gate_id):
            print("ورود مجاز است.")
        else:
            print("ورود غیرمجاز است.")

    elif choice == "5":
        for v in vehicles:
            print(v.plate, "-", v.model, "-", v.owner_name)

    elif choice == "6":
        for g in gates:
            print(g.gate_id, "-", g.gate_name, "-", g.location)

    elif choice == "7":
        print("خروج از برنامه")
        break

    else:
        print("گزینه نامعتبر است.")
