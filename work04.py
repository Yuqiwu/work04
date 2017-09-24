from flask import Flask

my_app = Flask(__name__)

@my_app.route('/') #127.0.0.1:5000
def root():
    print 'Printing!!!' #Printed in the terminal each time the either page is accessed.
    return 'Hi, Everybody!' #actual html output

@my_app.route('/route1') #127.0.0.1:5000/route1
def route1():
    return 'This is route1'

@my_app.route('/route2') #127.0.0.1:5000/route2
def route2():
    return 'This is route2'

@my_app.route('/route3') #127.0.0.1:5000/route3
def route3():
    return 'This is route3'
	
if __name__ == '__main__':
   my_app.debug = True
   my_app.run() #run the web app
