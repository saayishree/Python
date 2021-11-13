#convert ht in feet and inches to cm
h_feet=int(input("enter the height in feet"))
h_inch=int(input("enter the height in inch:"))
tmp=h_feet*12
h_inch=h_inch+tmp
h_cm=h_inch*2.54
print(h_cm)
