import turtle as t

Zvezdy_Kovsh = ([-86,42], [-2,54], [14,46], [38,30], [42,0], [82,0], [86,36]
	)
Zvezdy_Okr = ([-68,62], [54,74], [134,38], [-134,-8], [-54,-14], [138,-2], [64,-64]
	)
Luna = ([80, 150])

def P_Mesyac(R):
	t.color((254, 254, 142), (254, 254, 142))
	t.up()
	t.goto(Luna)
	t.down()
	t.begin_fill()
	t.circle(R)
	t.end_fill()
	t.color((0, 11, 104), (0, 11, 104))
	t.begin_fill()
	t.left(90)
	t.fd(2*R)
	t.left(90)
	t.fd(R)
	t.left(90)
	t.fd(2*R)
	t.left(90)
	t.fd(R)
	t.end_fill()


def P_Zvezda(l):
	t.left(80)
	for x in range(5):
		t.fd(l)
		t.right(145)

def Set_Zv(x, y, d):
	t.up()
	t.goto(x, y)
	t.down()
	t.begin_fill()
	P_Zvezda(d)
	t.end_fill()

def P_Zvezdy():
	t.color((255, 248, 0), (255, 248, 0))
	for x, y in (Zvezdy_Okr):
		Set_Zv(x, y, 10)

def P_Kovsh():
	t.color((204, 255, 0), (204, 255, 0))
	for x, y in (Zvezdy_Kovsh):
		Set_Zv(x, y, 10)

def P_Luna():
	t.color((254, 254, 142), (254, 254, 142))
	t.up()
	t.goto(Luna)
	t.down()
	t.begin_fill()
	t.circle(20)
	t.end_fill()


if __name__ == "__main__":

	t.colormode(255)
	t.bgcolor(0, 11, 104)
	P_Zvezdy()
	P_Kovsh()
	P_Mesyac(20)
#	P_Luna()
	t.exitonclick()
