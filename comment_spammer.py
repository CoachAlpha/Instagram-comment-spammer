from time import sleep
print("Welcome to comment spammer\nDon't forget to use this on your friends not anyone else or your bussines account to promote yourself:)\nPUBLISHER: ALPHA:) "
      "\nVERSION: 1.5.1 \nthe person that you want to spam their posts have to be followed \nor have a open account NOT CLOSED ACCOUNT")
sleep(2)
time = int(input("Please enter how many times you want to send the comment to the post!!!\n"))
post_con = int(input("Please enter how many post your victim has!!!\n"))
sleep(1)
try:
	from selenium import webdriver
	from webdriver_manager.chrome import ChromeDriverManager
	import random
except:
	print("Can't open modules make sure you install them first and then run the program")



try:
	browser = webdriver.Chrome(ChromeDriverManager().install())
	print("Opening browser ...")
except:
	print("can't open the browser!!")

try:
	comm = open("text.txt", "r")
	comm_txt = (comm.read())
except:
	print("Can't open the file to send the comment please check if you have the file and then write the program!!")

# starting and opening the browser and going to main page of instagram
def start():
	print("Getting online ...")
	browser.get('https://www.instagram.com/')
	sleep(3)
	username = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
	password = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
	username1 = input("Please enter you Username:\n")
	password1 = input("Please enter your password:\n")
	username.send_keys(username1)
	password.send_keys(password1)
	login_button = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
	login_button.click()
	sleep(4)
	# notNow = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
	# notNow.click()
	# sleep(3)
	notNow_not = browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
	notNow_not.click()
	sleep(2)


# opening the victim post and getting ready to attack
def entering_post():
    username_client = input("Please enter your victim username\n")
    browser.get('https://www.instagram.com/' + username_client + '/')
    sleep(1.5)
    post = browser.find_element_by_css_selector('#react-root > section > main > div > div._2z6nI > article > div > div > div > div.v1Nh3.kIKUG._bz0w > a > div')
    post.click()
    sleep(1)


# sending the comment and the emoji
def post_com(com_repeat):
	for i in range(1,4):
		print("Commenting in ",i)
		sleep(1)
	for i in range(com_repeat):
		sleep(3)
		emoji = browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.sH9wk._JgwE > div > form > button.wpO6b > div > svg")
		emoji.click()
		sleep(0.5)
		e100 = browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/div/div/div[2]/div/div/button[8]")
		e100.click()
		sleep(0.5)
		write = browser.find_element_by_class_name(u"Ypffh")
		write.send_keys(comm_txt)
		sleep(1.5)
		post_button = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')
		post_button.click()


# going for the next posts till it get's error only 5 posts
def next_ones(post_time):
	for i in range(post_con-1):
		try:
			next_one_post = browser.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a")
			next_one_post.click()
			sleep(1)

			post_com(time)
			sleep(1)
		except:
			print("No more story to comment")




#running the program
start()
entering_post()
post_com(time)
sleep(1.5)
next_ones(post_con)
exit()
