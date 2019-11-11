import grpc_port as grpc

def get(requestData):
    if(requestData["userId"]):
        print("Received Id!")
        response = grpc.getDiscounts(requestData["userId"], "ID1")
        print("Returning from Logic")
        return(response)  
    else:
        return("Didn't receive Id!")