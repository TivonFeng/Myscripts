#!/usr/bin/env python3
import os
import sys	
import time




def debug(argv):
	
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
		time.sleep(3)
	print ('device is ready!')

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
	time.sleep(1)

	os.system('adb push \
			/work/Mandroid/out/target/product/sofia3gr/system/app/{0}/{1}.apk /system/app/{2}/'.format(argv,argv,argv))
	print ('push ok!')
	os.system('adb reboot')
	print ('rebooting!')

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

def main():
	flag,argv = getsys()
	if flag:
		debug(argv)

if __name__ == "__main__":
	main()


	

