from django.conf.urls import patterns, include, url
urlpatterns = patterns('captcha.views',
    url(r'image/(?P<key>\w+)/$', 'captcha_image', name='captcha-image'),
    url(r'refresh/$','captcha_refresh',name='captcha-refresh'),
    url(r'verify/$','captcha_verify',name='captcha-verify'),
)
