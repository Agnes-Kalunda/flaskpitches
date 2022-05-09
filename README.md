# flaskpitches

## Description
This is a flask web app that allows users to post/view and comment on other users' pitches.There is also a login/sign up option in order to have these view options.


## Behavior Driven Development

Register to be a user	Your email : jane@doe.com Username : janedoe Password : doe	New user is registered
User Log in	Your email : janedoe@mail.com Password : 1234	Logged in

Create a Pitch	Click New Pitch	Authenticated User is redirected to a form page to create a pitch
View a pitch	Click on a pitch's title	Redirected to a page that has the the pitch
Comment on a pitch	Click Comment	Authenticated user is redirected to a form to comment about that pitch
Update profile	click your name while logged in	Redirected to a profile page to set your details

## Setup/Installation Requirements
$ git clone :
$ cd pitches
$ python3 -m venv virtual to create a virtual environment
$ source virtual/bin/activate to activate the virtual environment
run $ python3 -m pip install -r requirements.txt to install dependencies
In the manage.py change app = create_app('production') to app = create_app('development')
run $ chmod a+x start.sh to make the start.sh file executable
$ ./start.sh to start the application

## Technologies Used

Python3.6
Flask
Bootstrap
Postgres Database
CSS
HTML

## License
[MIT](https://choosealicense.com/licenses/mit/)
Copyright (c) 2022 **Agnes-Kalunda**
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

