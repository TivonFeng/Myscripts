#!/usr/bin/env python3
import os
import sys	
import time

#output dir
outputdir = '/work/work/android_mr1/out/target/product/sofia3gr/system/app/'

#checkDevice
def checkDevice():
	flag = True
	while flag:
		tmp = os.popen('adb devices').readlines()
		if len(tmp) >= 3:
			flag = False
		else :
			i = 0
			if i > 3:
				os.system('adb kill-server')
				print ('killing server!')
				os.system('adb start-server')
				print ('starting server!')
			i = i + 1
		print ('check device!')
		time.sleep(1)
	print ('device is ready!')

#root & remount device
def root_remountDevice():
	flag = True
	while flag:
		tmp = os.popen('adb root').readlines()
		if len(tmp) == 0:
			time.sleep(1)
		elif tmp[0] == 'adbd is already running as root\n'	:
			flag = False
	print ('root ok!')

	tmp = os.popen('adb remount').readlines()
	for i in tmp:
		if i == 'remount succeeded\n':
			flag = False
	print ('remount ok!')
	

#install app
def installApp(argv):
	tmp = os.popen('adb  install -r \
			{0}/{1}/{2}.apk'.format(outputdir, argv, argv)).readlines()
	print (tmp[1])
	if 'Failure' in tmp[1]:
		print ('installed fail!')
		print ('pushing!')
		os.system('adb push \
			{0}/{1}/{2}.apk'.format(outputdir, argv, argv))
		print ('push ok!')
		print ('rebooting!')
		os.system('adb reboot')
		print ('reboot ok!')
	


#get argument
def getsys():
	if len(sys.argv) != 2:
		print ('please check args!')
		return False,''
	else:
		tmp = sys.argv[1]
		if tmp.find('.') != -1:
			 a = sys.argv[1].split('.')
			 tmp = a[0]
		return True,tmp


def debug(argv):
	checkDevice()
	root_remountDevice()
	installApp(argv)

def main():
	flag,argv = getsys()
	if flag:
		debug(argv)

if __name__ == "__main__":
	main()


	

