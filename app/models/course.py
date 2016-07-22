""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class course(Model):
    def __init__(self):
        super(course, self).__init__()

    def create_course(self,course):
    	
    	query ="insert into courses (course_name, course_description, created_at, updated_at) values (:course, :description, now(), now()"
	data = {'course_name':course['course_name'], 'course_description':course['course_description']}
	return self.db.query_db(query,data)

    def get_course_by_id(self,id):
    	query ="select * from courses where id = :id"
	data ={ 'id' : id}
	return self.db.query_db(query, data)
    
    def delete(self,id):
    	query = "delete from courses where id = :id"
	data = {"id": id}
