# img_flask_api
Interface with chrome for image forgery detection 

**Feature list**
| Feature | Description | Status |
| --- | ----------- | ----------- |
| API Endpoint | Integration of main image analysis module implemented | In Development |
| Copy-move Detection | Using SIFT and DBSCAN for passive image forgery detection | In Testing |
| Splice Detection  | Utilises ML methodologies | In research |
| Face Recognition | Flagging images that contain face(s) of persons | In research |
| GAN Detection | used to detect face manipulation, deep fakes or ai rendered faces | TBS |
| API Security | If no login then rate limits on api resource (threading) or Oath with email/gmail and more | In Testing |
| Chrome Plugin | Javascript front end to scrape images and send urls to API for report and visual detection | In testing |
| Benford Law Analysis (experimental) | Applies the statistical rules of Benfords Law to image vector analysis | In research |
| Sys admin API interface | API endpoints for database reading and  configuration settings | TBS |
| GUnicorn | Implement GUnicorn for production  concurrency | In Research |
| NGinx | Works in tandem with GUnicorn. Serves requests to GUnicorn and static to itself | In Research |
| Web Page | Create front end web page to allow user to upload or paste link and get report in response (makes call to microservices API) | TBS |

Proposed Features:
- main api at port 5001 (see other repo)
- delegation of work to other apis (passive image forensics, gan generated faces)
- when responses returned final json compiled along with compressed image mask and metadata

The above proposed features provide plenty of information for the user to consider. 
An analytical step is needed to perhapscross reference results and return a level of confidience in the 
analytical evidence.

TODO: After all components in place and testing is in final stages a metrics module is needed to show statistics in some form.
      This is needed since a range of techniques are used such as CNN, passive image analysis, various clustering.
      If possible, try and measure each of these and provide an overall confidence score.

TODO:
**For Production:**
- handle long response gaps 
- handle user change page [api payload not needed]
- handle authentication [no user log-in | token based]
- deployment configuration files [for heroku server]
- implement secret key config for client secure connection


**For Development:**
- implement current working modules and test
- implement dictionary to json conversion
- implement chunking response for each image [currently the client waits for all images to be processed]
- implement graph database for module processing env and flask authentication / sessions
- [low priority] implement sending compressed images in json response


**For Test:**
- implement tests [may require a wrapper to set configs and environment variables]


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

**Main API endpoint**
**Post example in dev environment ->**
```
curl -v -H "Content-Type: application/json" -X POST -d '{"urls": ["https://www.w3schools.com/howto/img_mountains.jpg", "https://www.oxforduniversityimages.com/images/rotate/Image_Spring_17_4.gif"]}' http://127.0.0.1:5000/imginterface/
```
**returns -> **
```
{"PAYLOAD":{"Image_Spring_17_4.gif":[["DBSCAN_CPY_MOVE",0]],"img_mountains.jpg":[["DBSCAN_CPY_MOVE",1]]}}
```






