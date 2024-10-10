import xml.dom.minidom


doc = xml.dom.minidom.parse("sample.xml")


staff_list = doc.getElementsByTagName("staff")

# Duyệt qua từng phần tử <staff> và in ra thông tin
for staff in staff_list:
    staff_id = staff.getAttribute("id")
    name = staff.getElementsByTagName("name")[0].firstChild.data
    salary = staff.getElementsByTagName("salary")[0].firstChild.data
    print(f"Staff ID: {staff_id}")
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print("------------------------")

