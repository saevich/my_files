import turtle as t
def P_Zvezda(l):
	t.left(80)
	for x in range(5):
		t.fd(l)
		t.right(145)

if __name__ == "__main__":

	P_Zvezda(50)