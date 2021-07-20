x,y,w,h = map(int, input().split())

x_diff = w-x
y_diff = h-y


print(min(x, y, x_diff, y_diff))


