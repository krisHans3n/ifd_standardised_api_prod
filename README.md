# img_flask_api
Interface with chrome for image forgery detection 

TODO:
For Production:
- handle long response gaps 
- handle user change page [api payload not needed]
- handle authentication [no user log-in | token based]
- deployment configuration files [for heroku server]
- implement secret key config for client secure connection

For Development:
- implement current working modules and test
- implement dictionary to json conversion
- implement chunking response for each image [currently the client waits for all images to be processed]
- implement graph database for module processing env and flask authentication / sessions
- [low priority] implement sending compressed images in json response


For Test:
- implement tests [may require a wrapper to set configs and environment variables]







