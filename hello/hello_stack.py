import json
from aws_cdk import (
    core,
    aws_lambda as lambda_,
    aws_logs as logs_,
    aws_apigateway as gateway_ 
      
)

class MyStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
                
        with open("lambda-handler.py",encoding="utf8") as fp:
            handler_code = fp.read()
        
        lambdaFn = lambda_.Function(
            self, "Singleton",
            code=lambda_.InlineCode(handler_code),
            description="My function",
            function_name="mylambdafn2",
            handler="index.handler",
            memory_size=int(128),
            timeout=core.Duration.seconds(10),
            runtime=lambda_.Runtime.PYTHON_2_7,
        )

    
        rest_api: gateway_.RestApi = gateway_.RestApi(
            self,
            "MyRestAPI",
            rest_api_name="my-api1",
            description="My API",
            )
            
        rest_api.root.add_resource('send')
        #badrequestResponse: gateway_.IntegrationResponse = { 'statusCode': "400" }
        #internalServerResponse: gateway_.IntegrationResponse = { 'statusCode': "500" }
        okResponse: gateway_.IntegrationResponse = { 'statusCode': '200' }
                
        integration: gateway_.LambdaIntegration = gateway_.LambdaIntegration(handler=lambdaFn,
                                                                          proxy=False,
                                                                          passthrough_behavior=gateway_.PassthroughBehavior.WHEN_NO_TEMPLATES,
                                                                          content_handling=gateway_.ContentHandling.CONVERT_TO_TEXT,
                                                                          #integration_responses=gateway_.IntegrationResponse.status_code
                                                                          request_templates=["{\"mnumber\": \"$input.params('mnumber')\"}"],
                                                                          integration_responses=[okResponse]
                                                                          
                                                                           )

        rest_api.root.add_method(
            http_method="GET",            
            integration=integration,
            request_parameters={"method.request.querystring.mumber":True},
            method_responses=[okResponse]
           )





