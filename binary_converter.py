def add_binary(a, b):
	num = a + b
	begin_scale = 1
	counter = 0
	empty = []
	while begin_scale <= num:
		begin_scale = begin_scale * 2
		counter += 1

	begin_scale = round(begin_scale / 2)

	while counter > 0:
		if (num - begin_scale) < 0:
			empty.append("0")
			begin_scale = round(begin_scale / 2)
			counter -= 1
			continue
		else:
			empty.append("1")
			num = num - begin_scale
			begin_scale = round(begin_scale / 2)
			counter -= 1
			continue

	print("".join(empty))


add_binary(0, 0)