import sys
print ("""
        @@@      @@@@   @@@    @   @   @@@@
        @  @     @  @   @        @     @  @
        @ @      @@@@     @      @     @@@@
        @   @    @   @  @@@      @     @  @ \n\n\n""")
# a=0
# while a <3:
#     a+=1
#     print("=== PROGRAM KOVERSI BILANGAN===")
#     print("1.Desimal ke Biner")
#     print("2.Biner ke Desimal")
#     print("3.Keluar")
#     a1=int(input("silahkan Pilih Menu: "))
#     if a1==1:
#         desimal = int(input("masukan Desimal: "))
#         if desimal ==0:
#             print(0)
#         else:
#             print("hasil bagi sisa biner")
#             bitstring=""
#         while desimal > 0:
#             sisa= desimal %2
#             desimal = desimal//2
#             bitstring= str(sisa) + bitstring
            
#             print("Binernya adalah: ",bitstring)
        
#     elif a1==2:
#         bit=input("Masukan Str Binner: ")
#         desimal=0
#         eks = len(bit)-1
#         for digit in bit:
#             desimal += int(digit)*2**eks
#             eks -= 1
#         print ("Nilai Desimal adalah :",desimal)
    
#     elif a==3:
#         print("==========Terimakasih==========\n\n\n")


aku=0
while aku==0:
    k=input('masukan list angka: ')
    
    for k in k.split():
        if int(k)%2==0:
                
                print(k,'  bilangan genap')
                
        elif int(k)%2==0:
            
            if int(k)%2==0:
                    print(k,' bilangan genap')
                    
        elif int(k)%2==1:
            print(k,' bilangan ganjil')
            
            
        else: 
            if int(k)%2==0:
                
                print(' terdapat bilangan genap')