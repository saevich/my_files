from turtle import *
delay()
# Рисуем солнце
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(175)
    if abs(pos()) < 1:
        break
end_fill()
done()