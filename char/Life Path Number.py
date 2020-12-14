def life_path_number(birthdate):
    date = birthdate.split("-")
    year = date[0]
    month = date[1]
    day = date[2]
    res = sum_digits(year) + sum_digits(month) + sum_digits(day)

    return sum_digits(str(res))

def sum_digits(number):
	number = list(number)
	flag = True
	res = 0
	while flag:
		res = sum([int(n) for n in number ])
		if res > 9:
			number = list(str(res))
		else:
			break
	return res



print(life_path_number("1955-10-28"))