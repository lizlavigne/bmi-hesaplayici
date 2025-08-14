kilo = float(input("kilonuzu girin (kg): ")) 
boy = float(input("boyunuzu girin (m): "))

bmi = kilo/(boy**2)
print(f"vücut kitle indeksiniz:  {bmi} \n18,5 kg/m2 ve daha düşük değerler = Zayıf\n 18,5 ve 24,9 kg/m2 arasındaki değerler = Normal ağırlıkta\n 25,0 ve 29,9 kg/m2 arasındaki değerler = Kilolu\n 30,0 ve 34,9 kg/m2 arasındaki değerler = 1. derece obezite\n 35,0 ve 39,9 kg/m2 arasındaki değerler = 2. derece obezite\n 40 kg/m2 ve üzerindeki değerler = 3. derece obezite")