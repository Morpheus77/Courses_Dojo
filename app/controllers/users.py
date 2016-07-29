from system.core.controller import *
class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        # Note that we have to load the model before using it in the methods below
        self.load_model('User')
    # method to display registration page
    def new(self):
        return self.load_view('users/new.html')
    # method to create a user
    def create(self):
        # gather data posted to our create method and format it to pass it to the model
        user_info = {
             "name" : request.form['name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "pw_confirmation" : request.form['pw_confirmation']
        }
        # call create_user method from model and write some logic based on the returned value
        # notice how we passed the user_info to our model method
        create_status = self.models['User'].create_user(user_info)
        if create_status['status'] == True:
            # the user should have been created in the model
            # we can set the newly-created users id and name to session
            session['id'] = create_status['user']['id'] 
            session['name'] = create_status['user']['name']
            # we can redirect to the users profile page here
            return redirect('/users')
        else:
            # set flashed error messages here from the error messages we returned from the Model
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            # redirect to the method that renders the form
           return redirect('/users/new')