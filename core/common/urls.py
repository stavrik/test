from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
### #FIXME admin.autodiscover()
from django.views.generic import TemplateView

import views as common_views
import views as lsstmon_views
#from ..table import views as table_views
#from ..pandajob import views as pandajob_views
#from ..htcondor import views as htcondor_views
#from ..resource import views as resource_views
#from ..table import views as table_views
#from ..graphics import views as graphics_views
#from ..task import views as task_views

from ..pandajob import views_support as pandajob_support_views

common_patterns = patterns('',
    ### robots.txt
    url('^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    ### the front page
    url(r'^$', common_views.index, name='index'),

    ### Applications
    url(r'^htcondorjobs', include('core.htcondor.urls')),
    #url(r'^job', include('core.pandajob.urls')),
    url(r'^resource', include('core.resource.urls')),
    url(r'^api-auth', include('core.api.urls')),
#    url(r'^lsst', include('lsst.urls')),

    ### api
    url(r'^api/$', pandajob_support_views.maxpandaid, name='supportRoot'),
    url(r'^api/reprocessing/$', include('core.api.reprocessing.urls')),

    ### UI elements
    url(r'^api/datatables', include('core.table.urls')),
#    url(r'^graphics/', include('core.graphics.urls')),
#    url(r'^task/', include('core.task.urls')),

    ### Common views from LSST
    url(r'^$', lsstmon_views.mainPage, name='mainPage'),
    url(r'^$', lsstmon_views.mainPage, name='index'),
    url(r'^help/$', lsstmon_views.helpPage, name='helpPage'),
    url(r'^jobs/$', lsstmon_views.jobList, name='jobList'),
    url(r'^jobs/(.*)/$', lsstmon_views.jobList, name='jobList'),
    url(r'^jobs/(.*)/(.*)/$', lsstmon_views.jobList, name='jobList'),
    url(r'^job$', lsstmon_views.jobInfo, name='jobInfo'),
    url(r'^job/(.*)/$', lsstmon_views.jobInfo, name='jobInfo'),
    url(r'^job/(.*)/(.*)/$', lsstmon_views.jobInfo, name='jobInfo'),
    url(r'^users/$', lsstmon_views.userList, name='userList'),
    url(r'^user/(?P<user>.*)/$', lsstmon_views.userInfo, name='userInfo'),
    url(r'^user/$', lsstmon_views.userInfo, name='userInfo'),
    url(r'^sites/$', lsstmon_views.siteList, name='siteList'),
    url(r'^site/(?P<site>.*)/$', lsstmon_views.siteInfo, name='siteInfo'),
    url(r'^site/$', lsstmon_views.siteInfo, name='siteInfo'),
    url(r'^wns/(?P<site>.*)/$', lsstmon_views.wnInfo, name='wnInfo'),
    url(r'^wn/(?P<site>.*)/(?P<wnname>.*)/$', lsstmon_views.wnInfo, name='wnInfo'),
    url(r'^tasks/$', lsstmon_views.taskList, name='taskList'),
    url(r'^task$', lsstmon_views.taskInfo, name='taskInfo'),
    url(r'^task/$', lsstmon_views.taskInfo, name='taskInfo'),
    url(r'^errors/$', lsstmon_views.errorSummary, name='errorSummary'),
    url(r'^incidents/$', lsstmon_views.incidentList, name='incidentList'),
    url(r'^logger/$', lsstmon_views.pandaLogger, name='pandaLogger'),
    url(r'^task/(?P<jeditaskid>.*)/$', lsstmon_views.taskInfo, name='taskInfo'),
    url(r'^dash/$', lsstmon_views.dashboard, name='dashboard'),
    url(r'^dash/analysis/$', lsstmon_views.dashAnalysis, name='dashAnalysis'),
    url(r'^dash/production/$', lsstmon_views.dashProduction, name='dashProduction'),
    url(r'^workingGroups/$', lsstmon_views.workingGroups, name='workingGroups'),
    url(r'^fileInfo/$', lsstmon_views.fileInfo, name='fileInfo'),
    url(r'^fileList/$', lsstmon_views.fileList, name='fileList'),
    url(r'^datasetInfo/$', lsstmon_views.datasetInfo, name='datasetInfo'),
    url(r'^datasetList/$', lsstmon_views.datasetList, name='datasetList'),
    url(r'^workQueues/$', lsstmon_views.workQueues, name='workQueues'),

    ### support views for LSST
    url(r'^support/$', pandajob_support_views.maxpandaid, name='supportRoot'),
    url(r'^support/maxpandaid/$', pandajob_support_views.maxpandaid, name='supportMaxpandaid'),
    url(r'^support/jobinfouservohrs/(?P<vo>[-A-Za-z0-9_.+ @]+)/(?P<nhours>\d+)/$', pandajob_support_views.jobUserOrig, name='supportJobUserVoHrs'),
    url(r'^support/jobinfouservo/(?P<vo>[-A-Za-z0-9_.+ @]+)/(?P<ndays>\d+)/$', pandajob_support_views.jobUserDaysOrig, name='supportJobUserVo'),


#    ### TEST/Playground
#    url(r'^test_playground/$', common_views.testing, name='testing'),
#    url(r'^htc4/$', htcondor_views.list3HTCondorJobs, name='htc4'),
#    url(r'^pan4/$', pandajob_views.list3PandaJobs, name='pan4'),


    ### Django Admin
    ### Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    ### Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),



) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = patterns('',)
urlpatterns += common_patterns