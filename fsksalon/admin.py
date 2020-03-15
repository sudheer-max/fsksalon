from django.contrib import admin
from .models import AboutUs, Hair, Portfolio, Blog, Course, Beauty, Bridal, Tattoo, Nail

admin.site.site_title = "FSK SALON & ACADEMY"
admin.site.site_header = "FSK SALON"
admin.site.index_title = "FSK SALON & ACADEMY"


admin.site.register(AboutUs)
admin.site.register(Hair)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Course)
admin.site.register(Beauty)
admin.site.register(Bridal)
admin.site.register(Tattoo)
admin.site.register(Nail)
