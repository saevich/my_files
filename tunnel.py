import turtle as t 

# Рисует квадрат размером stor
def kvadr(stor):
    t.down()
    for i in range(4):
        t.forward(stor)
        t.left(90)
    t.right(90)
    t.up()

def paint_tunnel():
	for i in range(20):
		kvadr(50 + i*20)
		t.forward(10)
		t.right(90)
		t.forward(10)
		t.right(180)

if __name__ == "__main__":

	paint_tunnel()
	t.exitonclick()