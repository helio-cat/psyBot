# psyBot
bot to handle dice rolling commands:
EXAMPLE

	Chase@rondeau MINGW64 /d/GitHub/psyBot
	$ C:/Python38/python.exe d:/GitHub/psyBot/psybot.py
	Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)
	0 to exit
	---------
	command: $ !1d6
	3 = 3    d6
	_________

	Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)
	0 to exit
	---------
	command: $ !2d8
	7 8 = 15         d8
	_________

	Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)
	0 to exit
	---------
	command: $ !1d100
	83 = 83  d100
	_________

	Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)
	0 to exit
	---------
	command: $ !9d12
	3 6 9 3 4 4 3 2 1 = 35   d12
	_________

	Roll the dice! syntax: '!2d12', '!1D6' (dice < 9 &&0 sides > 1)
	0 to exit
	---------
	command: $ exit

and to automatically do a d100 skill check against the desired skill via JSON lookup:
EXAMPLE

	str lvl 65 check: rolled: 75 -> Succeed!
	18 = 18  d100
	_________

	str lvl 50 check: rolled: 18 -> Fail.
	22 = 22  d100
	_________

	dodge lvl 50 check: rolled: 22 -> Fail.
	49 = 49  d100
	_________

	computeruse lvl 45 check: rolled: 49 -> Succeed!
