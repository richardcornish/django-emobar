# django-adminplus

Admin Plus is a Django app that enhances the [admin](https://docs.djangoproject.com/en/1.5/intro/tutorial02/) with a few light, select niceties. It's not a complete revamp of the admin, but just a few extras that I found myself adding to new projects all the time.


## Features

Admin Plus uses the [markItUp](http://markitup.jaysalvat.com/home/) toolbar for adding Markdown to textareas. It uses a (mostly) unique skin to the toolbar that compliments the minimalism of the admin.

The toolbar's [emoji](http://en.wikipedia.org/wiki/Emoji) use the Apple iOS emoji image set. Although emoji became a Unicode standard, some browsers (ahem, Chrome) still do not support the emoji HTML entities. Admin Plus instead uses the [GitHub-flavored Markdown codes](http://www.emoji-cheat-sheet.com/) and a filter to replace the emoji text codes with their respective image equivalents.

Screenshot:

![Admin Plus toolbar screenshot](docs/adminplus-toolbar.png)

Usage in a template after installation:

    {% load emoji_tags %}
    
    {{ post.body|emoji }}

Other small and simple JavaScript enhancement added automatically:

- `selectFirstSite` selects the first site listed in the Sites field of a flatpage. Nothing is selected in a typical Django installation because you could have many sites, but because most people have one site, it's annoying and silly to have to keep clicking which site you want to attach the flatpage to when it's probably the first.
- `openViewLinkInNewWindow` opens objects from the admin's "View on site" button in a new (but same) window. Typically clicking that button will load the object's public view in the same window. I thought it was silly to hijack the window that was showing the admin.


## Installation

1. Place `adminplus` directory on Python path
2. Add `adminplus` to `settings.py`'s `INSTALLED_APPS` tuple.

    INSTALLED_APPS = {
        # ...
        'adminplus',
    }

3. Append `class Media` parts to admin classes in each of your app's `admin.py`. Example:

    from django.contrib import admin
    from ... import Post

    class PostAdmin(admin.ModelAdmin):

        # ...

        class Media:
            css = {
                'all': ('adminplus/css/style.css',)
            }
            js = ('adminplus/js/jquery.min.js', 'adminplus/js/jquery.markitup.js', 'adminplus/js/jquery.adminplus.js',)

    admin.site.register(Post, PostAdmin)

Note: The above is cleaner but a little more work because each app's `class Media` in `admin.py` has to be declared. This includes adding an additional flatpages app (with corresponding `admin.py`) if you want the enhancements to the flatpages app, plus adding that new flatpages app to your `INSTALLED_APPS`.

You could instead hijack the admin templates and stick the HTML calls to the media there. This would actually be required for adding additional WYSIWYGs to textareas not called `body` or `content`.

    # Template
    # /path/to/your/templates/admin/change_form.html
    {% extends "admin/change_form.html" %}

    {% block extrahead %}
        {{ block.super }}
        
        {% load adminmedia %}
        
        {# If you already use `class Media`, `load adminmedia` will load these below, so might not be needed #}
        <link rel="stylesheet" href="{{ STATIC_URL }}adminplus/css/style.css">
        <script src="{{ STATIC_URL }}adminplus/js/jquery.min.js"></script>
        <script src="{{ STATIC_URL }}adminplus/js/jquery.markitup.js"></script>
        <script src="{{ STATIC_URL }}adminplus/js/jquery.adminplus.js"></script>
        
        {# To target an additional textarea: #}
        <script>
            jQuery(function () {
                'use strict';
                ADMIN_PLUS.addMarkItUp('#id_then_name_of_field_in_model');
            });
        </script>
        
    {% endblock %}

More at [https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates).

4. Run `python manage.py collectstatic` in the correct django project directory.

5. Restart the server as necessary.


## What else?

If there is an easier way to accomplish installation (perhaps avoiding `class Media`?), do let me know.

File an issue or pull request with ideas for things you would like to see.