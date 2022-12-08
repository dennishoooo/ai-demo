# Azure Functions with python tensorflow

## File structure  
📦 .vscode  
 ┗ 📜extensions.json     
📦 models  
 ┗ 📜your model.h5 locations    
📦 predictBlob  
 ┣ __init__.py  ( your main code )  
 ┣ function.json  ( API setting )  
 ┣ productions.html ( Test your code in productions )   
 ┗ test.html ( Test your code in development )       
📦 README.md    
📦 host.json (setting for Azure Func )  
📦 local.settings.json (Local setting for Azure Func, not for uploading)  
📦 requirements.txt (what Azure to install)  

## Init steps
1. Make sure you open a Azure account.  
2. Download Azure CLI, Core Tools and Azure Functions Core Tools.   
- Ref: https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=v4%2Cwindows%2Ccsharp%2Cportal%2Cbash    
3. Do ```az login``` in the terminal.    
4. Create a Funcation App in azure portal. 
5. (Skipped due to done in this repo) Do ```func new --template "Http Trigger" --name MyHttpTrigger``` to init a project 

## Main steps
1. Move your models to ```./models folder```, make sure it's from a CNN models with keras with .h5 format.  
2. Change regarding params in ```predictBlob/__init__.py```.  
3. Use ```func start```to test in local.  
4. After you have tested and ready to upload use ``` func azure functionapp publish <FunctionAppName>```.
5. Make sure the ```<FunctionAppName>``` is same as your azure function name opened in azure portal.   
e.g. ``` func azure functionapp publish my_predict_func ```

## Notes
There is a better way for uploading and storing data with Azure blob storage and other method.  
Yet, For the complexity and cost concerns, we will only use Azure Functions in this demo.

## Helper
- func new --template "Http Trigger" --name MyHttpTrigger
- func start
- func azure functionapp publish "FunctionAppName"

## Using Environment
```
Azure Functions Core Tools:
Core Tools Version:       4.0.4736 Commit hash: N/A  (64-bit)
Function Runtime Version: 4.8.1.18957

Python:
tensorflow==2.8.2
```
