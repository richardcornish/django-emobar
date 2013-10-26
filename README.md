# django-adminplus

Admin Plus is a Django app that enhances the [admin](https://docs.djangoproject.com/en/1.5/intro/tutorial02/) with a few light, select niceties. It's not a complete revamp of the admin, but just a few extras that I found myself adding to new projects all the time.


## Features

Admin Plus uses the [markItUp](http://markitup.jaysalvat.com/home/) toolbar for adding [Markdown](http://daringfireball.net/projects/markdown/) to textareas. It uses a (mostly) unique skin to the toolbar that complements the minimalism of the admin.

The toolbar's [emoji](http://en.wikipedia.org/wiki/Emoji) use the Apple iOS emoji image set. Although emoji became a Unicode standard, some browsers (ahem, Chrome) still do not support the emoji HTML entities. Admin Plus instead uses the [GitHub-flavored Markdown codes](http://www.emoji-cheat-sheet.com/) and a filter to replace the emoji text codes with their respective image equivalents.

Screenshot:

![Admin Plus toolbar screenshot](docs/adminplus-toolbar.png)

Other small and simple JavaScript enhancement added automatically:

- `selectFirstSite` selects the first site listed in the Sites field of a flatpage. Nothing is selected in a typical Django installation because you could have many sites, but because most people have one site, it's annoying and silly to have to keep clicking which site you want to attach the flatpage to when it's probably the first.
- `openViewLinkInNewWindow` opens objects from the admin's "View on site" button in a new (but same) window. Typically clicking that button will load the object's public view in the same window. I thought it was silly to hijack the window that was showing the admin.


## Installation

Download django-adminplus, probably with [Pip](http://www.pip-installer.org/) via GitHub. Please replace `[virtualenvironment]` with your own. You can also git clone or download the tarball, but then remember to add the `adminplus` directory to your Python path.

```
pip install -e git+https://github.com/richardcornish/django-adminplus.git#egg=django-adminplus --src ~/.virtualenvs/[virtualenvironment]/lib/python2.7/site-packages
```

Add `adminplus` to `settings.py`'s `INSTALLED_APPS` tuple.

```
INSTALLED_APPS = {
    # ...
    'adminplus',
}
```

Append `class Media` parts to admin classes in each of your apps' `admin.py`. Example:

```
from django.contrib import admin
from ... import Post

class PostAdmin(admin.ModelAdmin):

    # ...

    class Media:
        css = {
            'all': ('adminplus/css/style.min.css',)
        }
        js = ('adminplus/js/jquery.min.js', 'adminplus/js/markitup.min.js', 'adminplus/js/adminplus.min.js',)

admin.site.register(Post, PostAdmin)
```

Override the admin's `change_form.html` template for the app of your choosing.

```
# Inside /path/to/your/templates/admin/change_form.html

{% extends "admin/change_form.html" %}

{% block extrahead %}
    {{ block.super }}
    <script>
        django.jQuery(function () {
            'use strict';
            AdminPlus.addMarkItUp('#id_body'); // Selector of desired textarea
        });
    </script>
{% endblock %}
```

More at:

- [`ModelAdmin` media definitions](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-media-definitions)
- [Overriding admin templates](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates)

Run `python manage.py collectstatic` in the correct django project directory and restart the server as necessary.


## Usage

Usage in a template after installation:

```
{% load emoji_tags %}

{{ post.body|emoji }}
```


## What else?

If there is an easier way to accomplish installation (perhaps avoiding `class Media`?), do let me know.

File an issue or pull request with ideas for things you would like to see.