"""
    pandajob.columns_config

"""

COLUMNS = {}
ORDER_COLUMNS = {}
COL_TITLES = {}
FILTERS = {}


def skimColumns(myColumnsID, allColumnsID):
    """
        skimColumns(myColumnsID, allColumnsID): 
        get intersection of columns listed in COLUMNS[myColumnsID]
            and             columns listed in COLUMNS[allColumnsID]
    
    """
    cols = []
    try:
        cols = COLUMNS[myColumnsID]
    except:
        return cols

    try:
        COLUMNS[allColumnsID]
    except:
        return cols

    cols = filter(lambda itm:itm in COLUMNS[myColumnsID], COLUMNS[allColumnsID])

    return cols


def getTitles(myColumnsID, allColumnsID):
    """
        getTitles(myColumnsID, allColumnsID)
        get column titles for columns in COLUMNS[myColumnsID]
        
    """
    titles = []
    try:
        myCols = ORDER_COLUMNS[myColumnsID]
        titles = [ x for colname in myCols for x in COL_TITLES[allColumnsID] if x['c'] == colname ]
    except:
        return titles
    return titles



### PanDAjob - all
COLUMNS['PanDAjob-all'] = [\
        'pandaid', 'jobdefinitionid', 'schedulerid', 'pilotid', 'creationtime', \
        'creationhost', 'modificationtime', 'modificationhost', 'atlasrelease', \
        'transformation', 'homepackage', 'prodserieslabel', 'prodsourcelabel', \
        'produserid', 'assignedpriority', 'currentpriority', 'attemptnr', \
        'maxattempt', 'jobstatus', 'jobname', 'maxcpucount', 'maxcpuunit', \
        'maxdiskcount', 'maxdiskunit', 'ipconnectivity', 'minramcount', \
        'minramunit', 'starttime', 'endtime', 'cpuconsumptiontime', \
        'cpuconsumptionunit', 'commandtopilot', 'transexitcode', \
        'piloterrorcode', 'piloterrordiag', 'exeerrorcode', 'exeerrordiag', \
        'superrorcode', 'superrordiag', 'ddmerrorcode', 'ddmerrordiag', \
        'brokerageerrorcode', 'brokerageerrordiag', 'jobdispatchererrorcode', \
        'jobdispatchererrordiag', 'taskbuffererrorcode', 'taskbuffererrordiag', \
        'computingsite', 'computingelement', 'jobparameters', 'metadata', \
        'proddblock', 'dispatchdblock', 'destinationdblock', 'destinationse', \
        'nevents', 'grid', 'cloud', 'cpuconversion', 'sourcesite', \
        'destinationsite', 'transfertype', 'taskid', 'cmtconfig', \
        'statechangetime', 'proddbupdatetime', 'lockedby', 'relocationflag', \
        'jobexecutionid', 'vo', 'pilottiming', 'workinggroup', 'processingtype', \
        'produsername', 'ninputfiles', 'countrygroup', 'batchid', 'parentid', \
        'specialhandling', 'jobsetid', 'corecount', 'ninputdatafiles', \
        'inputfiletype', 'inputfileproject', 'inputfilebytes', \
        'noutputdatafiles', 'outputfilebytes', 'jobmetrics', 'workqueue_id', \
        'jeditaskid' \
]
ORDER_COLUMNS['PanDAjob-all'] = [\
            'pandaid', 'jobdefinitionid', 'creationtime', 'modificationtime', \
            'jobstatus', 'currentpriority', 'cloud', \
#            'produserid', 'destinationsite'\
]
COL_TITLES['PanDAjob-all'] = [ \
    {'sort': True, 'vis': True, 'c': 'pandaid', 't': 'PanDA ID'}, \
    {'sort': True, 'vis': True, 'c': 'jobdefinitionid', 't': 'Job Definition ID'}, \
    {'sort': True, 'vis': True, 'c': 'creationtime', 't': 'Creation Time'}, \
    {'sort': True, 'vis': True, 'c': 'modificationtime', 't': 'Modification Time'}, \
    {'sort': True, 'vis': True, 'c': 'jobstatus', 't': 'Job Status'}, \
    {'sort': True, 'vis': True, 'c': 'currentpriority', 't': 'Current Priority'}, \
    {'sort': True, 'vis': True, 'c': 'cloud', 't': 'Cloud'}, \
    {'sort': True, 'vis': False, 'c': 'schedulerid', 't': 'Scheduler ID'}, \
    {'sort': True, 'vis': False, 'c': 'pilotid', 't': 'Pilot ID'}, \
    {'sort': True, 'vis': False, 'c': 'creationhost', 't': 'Creation Host'}, \
    {'sort': True, 'vis': False, 'c': 'modificationhost', 't': 'Modification Host'}, \
    {'sort': True, 'vis': False, 'c': 'atlasrelease', 't': 'ATLAS release'}, \
    {'sort': True, 'vis': False, 'c': 'transformation', 't': 'Transformation'}, \
    {'sort': True, 'vis': False, 'c': 'homepackage', 't': 'Home package'}, \
    {'sort': True, 'vis': False, 'c': 'prodserieslabel', 't': 'prodserieslabel'}, \
    {'sort': True, 'vis': False, 'c': 'prodsourcelabel', 't': 'prodsourcelabel'}, \
    {'sort': True, 'vis': False, 'c': 'produserid', 't': 'Prod User ID'}, \
    {'sort': True, 'vis': False, 'c': 'assignedpriority', 't': 'Assigned Priority'}, \
    {'sort': True, 'vis': False, 'c': 'attemptnr', 't': 'Attempt #'}, \
    {'sort': True, 'vis': False, 'c': 'maxattempt', 't': 'Max Attempt'}, \
    {'sort': True, 'vis': False, 'c': 'jobname', 't': 'Job name'}, \
    {'sort': True, 'vis': False, 'c': 'maxcpucount', 't': 'Max CPU count'}, \
    {'sort': True, 'vis': False, 'c': 'maxcpuunit', 't': 'Unit of Max CPU count'}, \
    {'sort': True, 'vis': False, 'c': 'maxdiskcount', 't': 'Max Disk count'}, \
    {'sort': True, 'vis': False, 'c': 'maxdiskunit', 't': 'Unit of Max Disk count'}, \
    {'sort': True, 'vis': False, 'c': 'ipconnectivity', 't': 'IP Connectivity'}, \
    {'sort': True, 'vis': False, 'c': 'minramcount', 't': 'Min RAM count'}, \
    {'sort': True, 'vis': False, 'c': 'minramunit', 't': 'Unit of Min RAM count'}, \
    {'sort': True, 'vis': True, 'c': 'starttime', 't': 'Start Time'}, \
    {'sort': True, 'vis': True, 'c': 'endtime', 't': 'End Time'}, \
    {'sort': True, 'vis': False, 'c': 'cpuconsumptiontime', 't': 'CPU Consumption time'}, \
    {'sort': True, 'vis': False, 'c': 'cpuconsumptionunit', 't': 'Unit of CPU Consumption time'}, \
    {'sort': True, 'vis': False, 'c': 'commandtopilot', 't': 'Command to pilot'}, \
    {'sort': True, 'vis': False, 'c': 'transexitcode', 't': 'Trans Exit Code'}, \
    {'sort': True, 'vis': False, 'c': 'piloterrorcode', 't': 'Pilot Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'piloterrordiag', 't': 'Pilot Error Diag'}, \
    {'sort': True, 'vis': False, 'c': 'exeerrorcode', 't': 'Exe Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'exeerrordiag', 't': 'Exe Error Diag'}, \
    {'sort': True, 'vis': False, 'c': 'superrorcode', 't': 'Sup Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'superrordiag', 't': 'Sup Error Diag'}, \
    {'sort': True, 'vis': False, 'c': 'ddmerrorcode', 't': 'DDM Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'ddmerrordiag', 't': 'DDM Error Diag'}, \
    {'sort': True, 'vis': False, 'c': 'brokerageerrorcode', 't': 'Brokerage Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'brokerageerrordiag', 't': 'Brokerage Error Diag'}, \
    {'sort': True, 'vis': False, 'c': 'jobdispatchererrorcode', 't': 'Job Dispatcher Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'jobdispatchererrordiag', 't': 'Job Dispatcher Error Diag'}, \
    {'sort': True, 'vis': False, 'c': 'taskbuffererrorcode', 't': 'Taskbuffer Error Code'}, \
    {'sort': True, 'vis': False, 'c': 'taskbuffererrordiag', 't': 'Taskbuffer Error Diag'}, \
    {'sort': True, 'vis': True, 'c': 'computingsite', 't': 'Computing Site'}, \
    {'sort': True, 'vis': False, 'c': 'computingelement', 't': 'Computing Element'}, \
    {'sort': True, 'vis': False, 'c': 'jobparameters', 't': 'Job Parameters'}, \
    {'sort': True, 'vis': False, 'c': 'metadata', 't': 'Metadata'}, \
    {'sort': True, 'vis': False, 'c': 'proddblock', 't': 'proddblock'}, \
    {'sort': True, 'vis': False, 'c': 'dispatchdblock', 't': 'dispatchdblock'}, \
    {'sort': True, 'vis': False, 'c': 'destinationdblock', 't': 'destinationdblock'}, \
    {'sort': True, 'vis': False, 'c': 'destinationse', 't': 'destinationse'}, \
    {'sort': True, 'vis': False, 'c': 'nevents', 't': 'N events'}, \
    {'sort': True, 'vis': False, 'c': 'grid', 't': 'Grid'}, \
    {'sort': True, 'vis': False, 'c': 'cpuconversion', 't': 'CPU Conversion'}, \
    {'sort': True, 'vis': False, 'c': 'sourcesite', 't': 'Source Site'}, \
    {'sort': True, 'vis': False, 'c': 'destinationsite', 't': 'Destination Site'}, \
    {'sort': True, 'vis': False, 'c': 'transfertype', 't': 'Transfer Type'}, \
    {'sort': True, 'vis': False, 'c': 'taskid', 't': 'Task ID'}, \
    {'sort': True, 'vis': False, 'c': 'cmtconfig', 't': 'CMT config'}, \
    {'sort': True, 'vis': False, 'c': 'statechangetime', 't': 'State Change Time'}, \
    {'sort': True, 'vis': False, 'c': 'proddbupdatetime', 't': 'Prod DB Update Time'}, \
    {'sort': True, 'vis': False, 'c': 'lockedby', 't': 'Locked By'}, \
    {'sort': True, 'vis': False, 'c': 'relocationflag', 't': 'Relocation Flag'}, \
    {'sort': True, 'vis': False, 'c': 'jobexecutionid', 't': 'Job Execution ID'}, \
    {'sort': True, 'vis': False, 'c': 'vo', 't': 'VO'}, \
    {'sort': True, 'vis': False, 'c': 'pilottiming', 't': 'Pilot timing'}, \
    {'sort': True, 'vis': True, 'c': 'workinggroup', 't': 'Working Group'}, \
    {'sort': True, 'vis': False, 'c': 'processingtype', 't': 'Processing Type'}, \
    {'sort': True, 'vis': True, 'c': 'produsername', 't': 'Owner'}, \
    {'sort': True, 'vis': False, 'c': 'ninputfiles', 't': 'N input files'}, \
    {'sort': True, 'vis': False, 'c': 'countrygroup', 't': 'Country Group'}, \
    {'sort': True, 'vis': False, 'c': 'batchid', 't': 'Batch ID'}, \
    {'sort': True, 'vis': False, 'c': 'parentid', 't': 'Parent ID'}, \
    {'sort': True, 'vis': False, 'c': 'specialhandling', 't': 'Special Handling'}, \
    {'sort': True, 'vis': False, 'c': 'jobsetid', 't': 'Jobset ID'}, \
    {'sort': True, 'vis': False, 'c': 'corecount', 't': 'Core Count'}, \
    {'sort': True, 'vis': False, 'c': 'ninputdatafiles', 't': 'N input data files'}, \
    {'sort': True, 'vis': False, 'c': 'inputfiletype', 't': 'Input file type'}, \
    {'sort': True, 'vis': False, 'c': 'inputfileproject', 't': 'Input file project'}, \
    {'sort': True, 'vis': False, 'c': 'inputfilebytes', 't': 'Input file bytes'}, \
    {'sort': True, 'vis': False, 'c': 'noutputdatafiles', 't': 'N output data files'}, \
    {'sort': True, 'vis': False, 'c': 'outputfilebytes', 't': 'Output file bytes'}, \
    {'sort': True, 'vis': False, 'c': 'jobmetrics', 't': 'Job Metrics'}, \
    {'sort': True, 'vis': False, 'c': 'workqueue_id', 't': 'Work queue ID'}, \
    {'sort': True, 'vis': True, 'c': 'jeditaskid', 't': 'JEDI Task ID'}, \
]
FILTERS['PanDAjob-all'] = [ \
#            # .starttime
#            { 'name': 'fStartFrom', 'field': 'starttime', 'filterField': 'starttime__gte', 'type': 'datetime' }, \
#            { 'name': 'fStartTo', 'field': 'starttime', 'filterField': 'starttime__lte', 'type': 'datetime'}, \
            # .creationtime
    { 'name': 'fCrFrom', 'field': 'creationtime', 'filterField': 'creationtime__gte', 'type': 'datetime' }, \
    { 'name': 'fCrTo', 'field': 'creationtime', 'filterField': 'creationtime__lte', 'type': 'datetime'}, \
]


### reverse URL: 'api-datatables-jedi-jobs-in-task'
COLUMNS['api-datatables-jedi-jobs-in-task'] = [\
        'pandaid', 'jeditaskid', 'produsername', 'workinggroup', \
        'creationtime', 'modificationtime', 'starttime', 'endtime', \
        'jobstatus', 'currentpriority', 'computingsite', 'cloud' \
    ]
ORDER_COLUMNS['api-datatables-jedi-jobs-in-task'] = [\
        'produsername', 'workinggroup', 'jeditaskid', 'pandaid', \
        'jobstatus', \
        'creationtime', 'modificationtime', 'starttime', 'endtime', \
        'cloud', 'computingsite', 'currentpriority' \
    ]
COL_TITLES['api-datatables-jedi-jobs-in-task'] = \
    getTitles('api-datatables-jedi-jobs-in-task', 'PanDAjob-all')
FILTERS['api-datatables-jedi-jobs-in-task'] = FILTERS['PanDAjob-all']


