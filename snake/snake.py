#!/usr/bin/python3

import random
import curses



def main(stdscr):
	#window settings
	mh, mw = stdscr.getmaxyx()
	w = curses.newwin(mh,mw,0,0)
	w.keypad(1)
	w.timeout(100)

	#first food
	food = [mh/2,mw/2]
	w.addch(int(food[0]),int(food[1]), ord('b'))

	#first snake
	snk_x = mw/4
	snk_y = mh/4
	snake = [
		[snk_y, snk_x],
		[snk_y, snk_x-1],
		[snk_y, snk_x-2]
	]

	#Loop game
	key = curses.KEY_RIGHT

	while True:
		next_key = w.getch()
		key = key if next_key == -1 else next_key

		#game over
		if next_key == ord('c') or int(snake[0][0]) in [0,int(mh-1)] or int(snake[0][1]) in [0,int(mw-1)] or snake[0] in snake[1:]:
			quit()

		#movement
		new_head = [snake[0][0],snake[0][1]]

		if key == curses.KEY_UP:
			new_head[0] -= 1
		elif key == curses.KEY_DOWN:
			new_head[0] += 1
		elif key == curses.KEY_RIGHT:
			new_head[1] += 1
		elif key == curses.KEY_LEFT:
			new_head[1] -= 1

		snake.insert(0, new_head)

		if int(snake[0][0]) == int(food[0]) and int(snake[0][1]) == int(food[1]):
			#create new food, don't drop the tail
			notCreated = True
			while notCreated:
				new_food = [
						random.randint(1, mh-1),
						random.randint(1, mw-1)
				]
				if new_food not in snake:
					food = new_food
					notCreated = False
			w.addch(int(food[0]), int(food[1]), ord('b'))
		else:
			tail = snake.pop()
			w.addch(int(tail[0]),int(tail[1]), ' ')

		w.addch(int(snake[0][0]), int(snake[0][1]), ord('a'))



if __name__ == '__main__':
	curses.wrapper(main)