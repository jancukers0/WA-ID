import os, sys

print ("\033[1;32mSilahkan Masukkan Username & Password Anda")

print ("\033[1;32matau silahkan Hubungi Assembly696")

username = 'Wahyudi ID'      

password = 'n007'



def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mAlhmdllh sudah masuk juga..", 

			sys.exit()



		else:

			print "\033[1;32mPassword salah cok... [?]\033[00m"

			print "silahkan login kembali...kalau susah tanya pembuatnya...!!\n"

			restart()



	else:

		print "\033[1;32mMasukkan username yang bener Cok!!... [?]\033[00m"

		print "Silahkan segera log-in kembali cok...!!\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
