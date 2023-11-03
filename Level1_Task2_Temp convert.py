def deg_c_f(celcius):
    fahrenheit=(celcius * 9/5) + 32
    return fahrenheit

def deg_f_c(fahrenheit):
    celcius=(fahrenheit - 32) * 5/9
    return celcius


choice = input("Choose the conversion type (1 for c to f, 2 for f to c): ")

if choice == '1':
  celcius_value=float(input("Enter the celcius value:"))
  fahrenheit_value=deg_c_f(celcius_value)
  print(f"{celcius_value}°C is equal to {fahrenheit_value}°F")


elif choice == '2':
  fahrenheit_value=float(input("Enter the fahrenheit value:"))
  celcius_value=deg_f_c(fahrenheit_value)
  print(f"{fahrenheit_value}°F is equal to {celcius_value}°C")
  
  
else:
  print("Invalid choice:")
  
  
  
  
  
  
  
  
  
  

















