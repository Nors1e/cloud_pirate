#SYNTHESIZER 

#Iterate through the file
#get @params(price, cpu, OS) and store them in a dict
#DO NOT REPEAT TASKS
#load params into a new json file


result = {'FormatVersion': 'aws_v1', 'PriceList': ['{"product":{"productFamily":"Compute Instance","attributes":{"enhancedNetworkingSupported":"Yes","intelTurboAvailable":"No","memory":"256 GiB","dedicatedEbsThroughput":"7000 Mbps","vcpu":"64"}}}']}


#triggers if the type of addressed keyword is a Dict
#will run into issues with JSON
#Store result into variable
def dict_iterator(data,keyword):
    for key in dict_data.keys():
        #checks if keyword is equal to the iterated position
        if key == keyword:
            #checks if iterated object is applicable
            return dict_data[keyword]
        else:
            pass
            #try
            #except

#DISCONTINUED: moved to data_iterator function as if-else
def list_iterator(list_data, keyword):
    for i in list_data.:
        if i == list_data[keyword]:
            return list_data[keyword]
        else:
            pass
            #try 
            #except

#TEST CASE
def dict_iterator(data,keyword):
    if isinstance(data, dict):
        foo = data.keys()
    elif isinstance(data, list):
        foo = 
    else:

    for key in dict_data.keys():
        #checks if keyword is equal to the iterated position
        if key == keyword:
            #checks if iterated object is applicable
            return dict_data[keyword]
        else:
            pass
            #try
            #except





#MAIN
#checks if the data is dict or list
#potentially a function of it's own
if isinstance(data, dict):
    foo = data.keys()
elif isinstance(data, list):
    foo = data
    print("LIST")
else:
    pass


