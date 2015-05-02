bat file starts the database.
needs mongoDB
needs folder C:\data\db
needs environmental variables set for mongo and mongod to be run.

Alternately you can start mongoDB however you wish.

dataStorage.py writes information to database big_data

So far only did it for dailymotion information

TODO: implement to keep information for youtube.
TODO: implement function to check if a video was already put in database and update instead of insert.