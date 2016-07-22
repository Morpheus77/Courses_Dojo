"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact witkkkkkh the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)




        self.load_model('Course')
        self.db = self._app.db


       



   
    def index(self):
    	return self.load_view('index.html')

    def show(self,id):
    	course = self.models['course'].get_course_by_id(id)
	return self.load_view('show.html', course=course)
	
    def add(self):
    	course_details = {
		'course_name': 'course_name',
		'description': 'description'
	}
	self.models['course'].create_course(course_details)
	return redirect('/')



