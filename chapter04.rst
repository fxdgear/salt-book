=====================================
Chapter 4: Setting up Your Modules
=====================================

Salt comes with a HUGE list of built in modules, which is massively beneficial. But sometimes you might want to write your own modules. To include your own modules, just create a directory called ``_modules`` in the root of your salt states repository. And inside your ``_modules`` directory will be all the python files which are your custom salt modules.

In my case, I wrote some modules (file named ``myproject.py``) specific to my web site deployment which were essentially just wrappers of existing salt modules, that had specific arguments already declared. For example, I wrote a module that runs collect static for the specific instance of my website.

In order to run the collectstatic module in salt you would need to specify the settings module, the python path, and the virtualenv (if running inside a virtualenv).

This can be a very large command::

    salt 'web1' django.collectstatic myproject.settings.prod /path/to/virtualenv /path/to/be/on/pythonpath

This can be a pain to write out every time. I use helper modules which would look something like this::

    def collectstatic():
        SETTINGS = "myproject.settings.prod"
        BIN_ENV = "/path/to/virtualenv"
        PYTHONPATH = "/path/to/be/on/pythonpath"

        return __salt__['django.collectstatic'](
            SETTINGS, BIN_ENV, pythonpath=PYTHONPATH)

so now if I wanted to run collectstatic on web1 I could do::

    root@master-name# salt 'web1' myproject.collectstaic

The ``myproject`` comes from the name of the ``.py`` file in the  ``_modules`` dir (ie ``myproject.py``) and the ``collectstatic`` comes from the name of the function in the ``myproject.py`` file.

Grain Matching
--------------

Similarly to how we matched grains in the states we can do the same thing when calling salt modules. By using the ``-G`` flag we can specify the grain and the grain name we want to match by.

So to expand on our previous example say we wanted to run collect static on all web nodes (web1 and web2). This is simply done by::

    root@master-name# salt -G 'roles:webserver' myproject.collectstatic
