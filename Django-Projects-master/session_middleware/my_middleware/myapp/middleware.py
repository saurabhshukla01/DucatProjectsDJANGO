class My_first():

    def process_request(self,request):
        print ('Middleware executed')
        #request.info=Info.objects.all()
        #print request.user
        return request
        

    def process_response(self, request, response):
        print ("My_first process_response executed")
        return response
    

class Another_middleware():

    def process_request(self,request):
        print ('Another middleware executed')
        #print request.user
        return request
        
    def process_response(self, request, response):
        print ("Another_middleware process_response executed")	
        return response
