from graphics import *
import time

MOVING_INTV = 0.8

def ready(win):
    t = Text(Point(600,400), "3")
    t.setSize(30)
    t.draw(win)
    time.sleep(1)
    t.setText("2")
    time.sleep(1)
    t.setText("1")
    time.sleep(1)    
    t.undraw()
    time.sleep(1) 

def run_test(win):
    # Left eye
    tt = Text(Point(600,200), "Testing left eye.")
    tt.setSize(30)
    tt.draw(win)
    c = Circle(Point(50,400), 15)
    c.setOutline("red")
    c.setFill("red")
    c.draw(win)    
    l1 = Line(Point(930,400),Point(970,400))
    l1.setOutline("black")
    l1.setWidth(3)
    l2 = Line(Point(950,380),Point(950,420))
    l2.setOutline("black")
    l2.setWidth(3)
    l1.draw(win)
    l2.draw(win)
    ready(win)
    
    c_center = 50
    while c_center <= 800:
        c.move(40,0)
        c_center += 40
        time.sleep(MOVING_INTV)

    # Right eye
    time.sleep(1)
    tt.setText("Testing right eye.")
    c.move(1150-c_center,0)
    l1.move(250-950,0)
    l2.move(250-950,0)
    time.sleep(1)
    ready(win)
    
    c_center = 1150
    while c_center >= 400:
        c.move(-40,0)
        c_center -= 40
        time.sleep(MOVING_INTV)    

    tt.setText("Test complete.")
    time.sleep(2)

def main():
    win = GraphWin("Blindspot Tester", 1200, 800)
    win.setBackground("white")
    run_test(win)
    #win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()