

print(" -- Erzurumlu Talha Ustanın Yemekleri -- ")



ymkkayıt = open("yemektarifleri.txt", "w") 
ymkkayıt.write(input(  "Yemek Adı Giriniz = " )) 
ymkkayıt.write(input( "Yemek Tarifi Giriniz = " ))
ymkkayıt.close()

dosya = open("yemektarifleri.txt","r")
oku = dosya.read()
print("Yemek Adı ve Tarifiniz = " ,oku)