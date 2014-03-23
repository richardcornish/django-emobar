# Emo

**Emo** is a [Django](http://www.djangoproject.com/) template filter that enhances the [admin](https://docs.djangoproject.com/en/1.5/intro/tutorial02/) with a [Markdown](http://daringfireball.net/projects/markdown/) and [emoji](http://en.wikipedia.org/wiki/Emoji) enhanced [WYSIWYG](http://en.wikipedia.org/wiki/WYSIWYG) for textareas.


## Features

Emo uses the [markItUp](http://markitup.jaysalvat.com/home/) toolbar for adding Markdown to textareas. Its toolbar is themed to complement the minimalism of the admin.

The toolbar's emoji icons use the Apple iOS emoji icon set. Although emoji became a [Unicode standard](http://www.fileformat.info/info/unicode/block/miscellaneous_symbols_and_pictographs/images.htm), some browsers (ahem, Chrome) still do not support the emoji HTML entities. Emo instead uses the [GitHub-flavored Markdown codes](http://www.emoji-cheat-sheet.com/) and a filter to replace the emoji text codes with their respective image equivalents.

Screenshot:

![Emo toolbar screenshot](docs/emo-toolbar.png)


## Installation

The cleaner (but more laborious) way to install is with [Virtualenv](http://www.virtualenv.org/), [Pip](http://www.pip-installer.org/), and [Git](http://git-scm.com/). After having already run workon to activate the environment:

```
pip install -e git+https://github.com/richardcornish/django-emo.git#egg=django-emo
```

Remember to add it to your requirements.txt file. In your top-level directory:

```
pip freeze > requirements.txt
```

The faster (but dirtier) way is to clone the Git repository, placing the `emo` directory on your Python path. You'll probably run the command in the directory that contains your other Django apps. [Downloading the ZIP file](https://github.com/richardcornish/django-emo/archive/master.zip) and extracting the directory into place is a similar method.

```
git clone git@github.com:richardcornish/django-emo.git
```

Then edit your `settings.py`:

```
INSTALLED_APPS = (
    'emo',
)
```

Append `class Media` parts to admin classes in each of your apps' `admin.py`. Example:

```
from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):

    # ...

    class Media:
        css = {
            'all': ('emo/css/style.min.css',)
        }
        js = ('emo/js/alias.js', 'emo/js/markitup.js', 'emo/js/emo.js',)

admin.site.register(Post, PostAdmin)
```

Override the admin's `change_form.html` template for the app of your choosing.

```
# Inside blog/templates/admin/blog/post/change_form.html

{% extends "admin/change_form.html" %}

{% block extrahead %}
    {{ block.super }}
    <script>
        django.jQuery(function () {
            'use strict';
            Emo.addToolbar('#id_body'); // Selector of desired textarea
        });
    </script>
{% endblock %}
```

More at:

- [`ModelAdmin` media definitions](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-media-definitions)
- [Overriding admin templates](https://docs.djangoproject.com/en/dev/ref/contrib/admin/#overriding-admin-templates)

Remember to add [static file handling to your local settings](https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#static-file-development-view) or run `python manage.py collectstatic` in the correct django project directory and restart the server as necessary.


## Usage

Load the template tag in your template. Run it on an attribute of a variable:

```
{% load emoji_tags %}

{{ post.body|emoji }}
```

Note that the [`django.contrib.markup`](https://docs.djangoproject.com/en/1.5/ref/contrib/markup/) module has been deprecated since Django 1.5 and that a textarea using Markdown will not render HTML. Assuming you either [bring back the module](https://github.com/django/django/blob/1.5/django/contrib/markup/templatetags/markup.py) or you install a third-party Markdown solution, the template would probably more closely resemble:

```
{% load markup emoji_tags %}

{{ post.body|markdown|emoji }}
```