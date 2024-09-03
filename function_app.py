import azure.functions as func
import logging
from indexing import create_index, populate_index

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)



@app.blob_trigger(arg_name="myblob", path="resumecontainer/source/{name}",
                               connection="AzureWebJobsStorage") 
def BlobTrigger(myblob: func.InputStream):
        # create the print statement , like start of the function
        logging.info(f"Start Of Function\n")
        logging.info(f"Blog Name: {myblob.name}")
        logging.info(f"Blob Length: {len(myblob.read())} bytes")
        create_index()
        populate_index(myblob)
        # create the print statement , like end of the function
        logging.info(f"End Of Function\n")



