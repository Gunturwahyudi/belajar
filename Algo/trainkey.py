from json import dumps, load
from time import sleep
from random import randint,choice

# opening
print("="*41,"\nSelamat datang di TrainKey")
print("="*41)

#variabel
datatampung = {}
menu = [' 1. Login\n', '2. Register\n', '3. Delete Account\n', '4. Show user\n', "5. Exit"]
poin = 0
path_data = "database.json"
path_poin = 'leaderboard.json'
with open(path_data,'r') as data:
    datajson = load(data)

def tampil(arg1):
    print('='*19)
    print('| %0s | %-10s '%('#', 'User'))
    print('='*19)
    for i in range(len(arg1)):
        print('| %0s | %-10s '%(i+1,arg1[i]))
    print('='*19)

def leaderboard(arg1):
    print('='*25)
    print('| %0s | %-10s | %-2s|'%('#', 'User','Poin'))
    print('='*25)
    for k in range(len(arg1)):
        print('| %0s | %-10s | %-2s|'%(k+1,arg1[k],userpoin.get(arg1[k])))
    print('='*25)

#Authentication
while True:
    print(" ".join(menu))
    pilih = int(input("Pilih menu : "))
    if pilih == 1:
        login_user=input("Masukkan username : ")
        login_password = input("Masukkan password : ")
        if datajson.get(login_user)==login_password:
            print("\n\nLogin berhasil!\n\n")
            sleep(2)
            game_menu = [' 1. Play\n', '2. Leaderboard\n', '3. Tips\n', '4. Home\n','5. Exit']
            tips=["1. Pilih 1 untuk bermain\n", "2. Pilih 2 untuk melihat leaderboard\n","3. Ketika sudah bermain, silahkan masukkan input sesuai kata yang diberikan\n", "4. Jika jawaban anda benar maka poin anda akan bertambah 1\n"]

            #Looping untuk game
            while True:
                print("="*41,"\nSelamat datang di TrainKey")
                print("="*41)
                print(" ".join(game_menu))
                pilihan = int(input('Pilih menu : '))
                # print("\n\n\n")
                if pilihan == 1 :
                    with open(path_poin) as datapoin:
                        userpoin=load(datapoin)
                    while True:
                        huruf = [] #untuk menampung huruf
                        for i in range(randint(1,10)): #mengatur banyak huruf
                            a = choice('abcdefghijklmnopqrstuvwxyz') #memilih 1 huruf acak
                            huruf.append(a) #memasukkan huruf ke dalam list
                        kata = ''.join(huruf) #mengubah list huruf menjadi kata
                        print("Kata  : ",kata) # mencetak kata
                        user_kata = input("Input :  ") #meminta input user
                        if user_kata == kata: #kondisi jika input user == kata
                            poin+=1 #poin ditambah 1
                            pass #mengulangi perulangan
                        else: # kondisi jika input user salah
                            break # program berhenti
                    print("Poin anda : ",poin) #mencetak poin
                    if poin > userpoin.get(login_user): #kondisi jika mendapatkan poin tertinggi yang baru
                        userpoin[login_user]=poin #memasukkan poin ke dalam dictionary
                        with open(path_poin,'w') as outpoin: #membuka file 'leaderboard' yg ada di variabel path_poin dalam mode write agar bisa di edit menjadi variabel outpoin
                            outpoin.write(dumps(userpoin)) #mengupdate nilai leader board
                    else: #kondisi jika poin dibawah skor tertinggi
                        pass #melanjutkan perulangan
                    # input("Tekan enter untuk melanjutkan : ")
                    print("\n\n") #mencetak jarak 2 baris kosong
                    sleep(1) #memberi jeda 1 detik
                elif pilihan == 2: # kondisi jika pilihan user memilih leaderboard
                    with open(path_poin,'r') as userurutan:
                        userpoin = load(userurutan)
                    urutdenganpoin = {k:v for k,v in sorted(userpoin.items(),key=lambda v:v[1],reverse=True)}
                    print('='*25)
                    print('| %-10s | %-2s |'%('User','Poin'))
                    print('='*25)
                    for keys,nilai in urutdenganpoin.items():
                        print('| %-10s | %-2s |'%(keys,nilai))
                    input("Tekan enter untuk keluar : ")
                    sleep(1)
                elif pilihan == 3:
                    print("Tips : \n"," ".join(tips))
                    while True:
                        input("Tekan enter untuk kembali : ")
                        break
                elif pilihan==4:
                    break
                elif pilihan==5:
                    exit()
                else:pass
        else:
            sleep(2)
            print("\nPassword/username salah coba lagi!\n")
            pass
    elif pilih == 2:
        daftar_username = input("Masukkan username : ")
        daftar_password = input("Masukkan password : ")
        with open(path_data) as databaru:
            datajson=load(databaru)
        with open(path_poin,'r') as poin1:
            userpoin = load(poin1)
        userpoin[daftar_username]=poin
        datajson[daftar_username]=daftar_password
        with open(path_poin,'w') as outdatapoin:
            outdatapoin.write(dumps(userpoin))
        with open(path_data,'w') as output:
            output.write(dumps(datajson))
        pass
    elif pilih == 3:
        login_user=input("Masukkan username : ")
        login_password = input("Masukkan password : ")
        if datajson.get(login_user)==login_password:
            datajson.pop(login_user)
            with open(path_data,'w') as keluar:
                keluar.write(dumps(datajson)) #menyimpan data setelah dihapus
        else:
            sleep(2)
            print("\nPassword/username salah coba lagi!\n")
            pass
    elif pilih == 4:
        tampung = []
        for i in datajson:
            tampung.append(i)
        tampil(tampung)
        input("Tekan enter untuk keluar : ")
        sleep(1)
    elif pilih == 5:
        exit()










