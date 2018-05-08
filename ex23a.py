from __future__ import print_function
#imports the print_function from the psudeo library future.
#future enables new language feauture that are not availaible in current
#definition defines a new meaning for the print function - the 3.0x print function is now needed
import pandas as pd
#imports the modudle pandas, a data science library and names it pd
import six
#impots the module six, which is a library that assits in smoothing differences betewee python versions
from apiclient.discovery import build
#discovery service provides machine readable meta data.
#will allow code to interact with google apis, like the analytics api
#access to build object which will take credentials and metadata for api access
from oauth2client.service_account import ServiceAccountCredentials
#This is a Python library for accessing resources protected by OAuth 2.0.
#import service account credenitals to create the credentials object that will be used throught all google applications

print(six.__version__)
#print the version of six that is on the machine -- could remove

ANALYTICS_SERVICE = 'analyticsreporting'
#create a varialbe called ANALYTICS_SERVICE and assign it to a string 'analyticsreporting'
ANALYTICS_SERVICE_VERSION = 'v4'
#create a variable callen ANALYTICS_SERVICE_VERSION and assign to a string 'v4'

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
#create a variable calle SCOPES and assign it to a string URL 'http://wwww.goggle....'
#allows code to 'view your Google Analytics data'

KEY_FILE = 'google_service_account_credentials.json'
#create a variable called KEY_FILE and assign it to a string 'google_service_account_credentials.json' -
#that is a json file that must be in the same folder as this python file for this file to run
#this file holds the project id, client id, client and auth uri

DATA_FILE = '/Users/alexandermclaughlin/data_requests/AP/author_benchmarks/2001-3000_author-articles_2017-09-01_2018-01-26.csv'
#create a variable named DATA_FILE and assign it to a string that is the file path
#to the file that will hold the account names and page paths that will be looped through

VIEW_IDS = {
    'Who What Wear': '1794175',
    'Byrdie': '73724826',
    'MyDomaine': '76360909'
}
#create variable called VIEW_IDS and assign it to a dictionary with the key:value pairs of brand name and GA view VIEW_IDS

DATE_RANGE = {
    'startDate': '2017-09-01',
    'endDate': '2018-01-26'
}
#create a variable called DATE_RANGE and assign it to a dictionary with the key:value pairs of
#start date and end date


METRICS = [
    'ga:users',
    'ga:pageviews',
    'ga:pageviewsPerSession',
    'ga:timeOnPage',
    'ga:avgTimeOnPage',
    'ga:bounceRate',
    'ga:avgSessionDuration'
]
#create a variable called METRICS and assign it to an array of key value pairs that are ga:[metrics]

URL_COLUMN = 'slug'
#create a variable called URL_COLUMN and assign it to a string 'slug' this is the variable that
#will be looped through
SITE_COLUMN = 'site'
#create a variable called SITE_COLUMN and assign it to a string 'stite'
OUTPUT_NAME = '2001-3000_author-articles_2017-09-01_2018-01-26_output'
#create a variable called OUTPUT_NAME and assign it to a string that will determine the output filename
INPUT_NAME = '2001-3000_author-articles_2017-09-01_2018-01-26'
#create a variable called INPUT_NAME and assign it to a string that will be used to locate input filename

def handle():
#define a function called handle, define no parameters
    # LOAD DATA FRAME
    articles = pd.read_csv(DATA_FILE)
    #indent and define variable that will be used as the article
    #list. this will be a pandas data frame object and uses the read_csv method
    #to create the pandas data frame from the csv devined as the DATA_FILE variable above

    # AUTHENTICATE GA API CLIENT
    analytics_api = authenticate_service(
    #create a variable called analytics_api and pass it the service_name
    #parameter and the api_version parameter
        service_name=ANALYTICS_SERVICE,
        #ANALYTICS_SERVICE is a variable that we defined above
        #and is passed here as a parameter of the GA API call
        api_version=ANALYTICS_SERVICE_VERSION
        #api_version is a variable that we defined above
        #and is passed here as a paramter of the GA API call

    )

    for index, row in articles.iterrows():
    #loop to accomidate getting the slug from the data frame and then passing the slug as a filters
    #loop also handles adding the metrics per slug back to the data frame
        # GET SLUG FROM URL
        clean_url = row[URL_COLUMN].split('?')[0]
        #create a variable and assign to the value of the URL_COLUMN row, call the split method on it.
        #split value of URL_COLUMN at the ?, pass the string to the left of the question mark to clean_url
        article_url = clean_url.split('/slide')[0].strip('/')
        #create a variable and assign to the value of clean_url, call the split method on it.
        #split value of clean_url at the /, pass the string to the left of the question to article_url
        #remove the left hand / to clean URL again
        slug = article_url[article_url.rfind('/') + 1:]
        #create a variable and assign to the value of article_url, retun a portion of the url string using an index method
        #find the position of the first slash, add one to that position and return the remainder of string (URL)
        print('slug: {0}'.format(slug))
        #as a check to the above logic - print out the slug: SLUG VARIABLE

        filters = 'ga:sourceMedium!~jungroup|Instant|keywee|taboola|' \
          'outbrain|vip-social|aka-pinterest|paid|^tpc|rpm-api;' \
          'ga:country==United States;' \
          'ga:pagePath=~{0}'
        #set filter parameters to be passed to the analytics api

        # CREATE REQUEST BODY
        body = {
        #create a variable named body with a data type of dictionary
            'reportRequests': [{
            #key:value where key is named reportRequests as per google and value is another dictionary
                'viewId': VIEW_IDS[row[SITE_COLUMN]],
                #key:value where key is viewId and values are the result of a key lookup of using the
                #values in the SITE_COLUMN that map to the VIEW_IDS dictionary defined above.
                #QUESTIOn about how the row look up works
                'dateRanges': [DATE_RANGE],
                #key:value pair that dateRanges is returned a dictionary of key:value pairs that are
                #start and end date strings
                'metrics': [{'expression': metric} for metric in METRICS],
                #key:value pair where metric key has a value that is an array or list comprehension.
                #list comprehension is a loop that creates a key:value pair for each metric in METRICS
                'filtersExpression': filters.format(slug)
                #key:value pair where filtersExpression key has value using the filters variable
                #using .format, slug is passed in as the loop interates
                #question about how the line breaks <\> interact with the key:value pairings
            }]
        }

        # MAKE REQUEST
        response = analytics_api.reports().batchGet(
            body=body
        ).execute()
        #create a variable called response and set it equal to the analytics_api variable with the .reports()
        #and the .batchGet() methods applied. Pass in the body variable as the required body parameter
        #syntax that google requires to make a response

        # GET RESULTS
        report = response['reports'][0]
        #create a variable called report and assign it the value found at the reports key, at position zero
        #question about what 0 returns
        metric_header_entries = report['columnHeader']['metricHeader']['metricHeaderEntries']
        #create a variable called metric_header_entries and assign it to the values at the keys listed above
        metric_headers = [entry['name'] for entry in metric_header_entries]
        #create a variable called metric_headers
        metric_values = report['data']['totals'][0]['values']
        results = dict(zip(metric_headers, metric_values))

        # ADD RESULTS TO DATAFRAME
        for metric in metric_headers:
            articles.loc[index, metric] = results[metric]
            articles.loc[index, 'slug'] = slug

    articles.to_csv(
        DATA_FILE.replace(INPUT_NAME, OUTPUT_NAME),
        index=False
    )


def authenticate_service(service_name, api_version):
    '''authenticate google analytics service using service account'''

    # CREATE CREDENTIALS OBJECT
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        filename=KEY_FILE,
        scopes=SCOPES
    )

    service = build(
        ANALYTICS_SERVICE,
        ANALYTICS_SERVICE_VERSION,
        credentials=credentials
    )
    return service


if __name__ == '__main__':
    handle()
