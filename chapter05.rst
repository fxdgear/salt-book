==============================================
Chapter 5: Deployment with the Salt Client API
==============================================

So now we have a large collection of states to manage all our different nodes. We have a collection of modules so we can run specific tasks, now we want to be able to have a very simple deployment strategy.

Sure we could in theory log on to the salt master and start typing out a bunch of ``salt -G 'roles:webserver' myproject.dosomthing`` but that would be time consuming and prone to error if you happened to forget a step.

Here is where we can utilize the salt client API. The salt client api is just a very simple way to run salt modules, programatically.

Lets say we want to have a "quick_deploy" (the updated code doesn't make any DB changes, it doesn't make any changes to the installed apps or requirements).

A typical flow for doing a quick deploy could be like this:

1. update the code
2. collectstatic
3. restart apache
4. restart supervisor (assuming your're using supervisor to manage celery)

We can make a very simple python script called ``quick_deploy.py`` where we essnetially run all these steps in order::

    import salt.client
    client = salt.client.LocalClient()

    ret = client.cmd(
        'G@roles:webserver or G@roles:redisserver',
        'myproject.update_code',
        [],
        expr_form="compound")
    print ret

    ret = client.cmd('web1', 'myproject.collectstatic')
    print ret

    ret = client.cmd(
        'roles:webserver',
        'myproject.restart_apache',
        [],
        expr_form="grain")
    print ret

    ret = client.cmd(
        'roles:redisserver',
        'myproject.restart_supervisord',
        [],
        expr_form="grain")
    print ret

This very simple script does the following steps:

#. It does a "compound" target of multiple roles: ``'G@roles:webserver or G@roles:redisserver'`` and it updates the code.
#. It does a simple "hostname" match on ``web1`` to run collectstatic. Since we are hosting our static media on S3, we only need to run collectstatic once, there's no need to target multiple webservers and repeat the job.
#. It does a "grain" match on the webservers and restarts apache on both.
#. it does a "grain" match on the redisserver and restarts supervisor.
