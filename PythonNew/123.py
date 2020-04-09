phone=input("Phone: ")
digits_mapping={
    "1":"One ",
    "2":"Two ",
    "3":"Three ",
    "4":"Four ",
    "5":"Five "
}
output=""
for ch in phone:
    output=output+digits_mapping.get(ch,"!"+" ")
print(output)