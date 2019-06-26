# notes on curses
import curses

window = curses.initscr()

# window.nodelay(flag) # non-blocking if flag is true
window.refresh()

