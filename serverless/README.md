This is a small demo of how to create you own lambda layer with shared code written by yourself. 

This demo is uses python as well as the serverless framework. You will need to have the serverless framework to deploy this to your AWS account.

To deploy the lambda layer nagivate to serverless/layer and run serverless deploy

To deploy the lambda code nagivate to serverless/code and run serverless deploy

Make sure to deploy the layer first since otherwise the code deployment wont be able to find the CFN export from the layer and will fail.

A good extension to this demo that one could do to learn more is to instlal and deploy a thrid party library to the lambda layer. 

Start with ```pip3 install -t <direct directory> <package>```