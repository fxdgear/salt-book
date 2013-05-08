=====================================
Chapter 3: Setting up Your State Tree
=====================================

Alrighty then! We have salt master running. We have our minions running and the two can communicate. Awesome!

Now we want to setup up some salt states. I'm not going to tell you how to configure your servers but I'll give you some pointers, and I'm going to assume you're using ``git`` as your ``fileserver_backend``.

So in the root of your salt states repository should be a file called ``top.sls``. The top state is where all the states for all your minions get derived from. Inside your ``top.sls`` you'll want to break down the states for the various roles of your infrastructure. A very simple top state tree would look something like::

    base:
      '*':
        - core       # core states, to be shared across ALL minions

      'roles:dbserver':
        - match: grain    # tells salt we are going to match this group by grains, and specifically we want the roles grain, and any role that is dbserver.
        - postgres

      'roles:webserver':
        - match: grain
        - http

      'roles:redisserver':
        - match: grain
        - redis
        - supervisor

Basically in this file we are mapping out which states go to which minions. These states can be either files themselves name accordingly ``core.sls``, ``postgres.sls`` or they could be files with ``init.sls`` files inside. Any salt module which is defined as a directory must have a ``init.sls`` file.

For example, our ``top.sls`` will read::

    # core.sls

    vim:
      pkg.installed

the same as::

    # core/init.sls

    vim:
      pkg.installed

The advantage of the latter is that we can specify other "sub-states" in the core module, and they can be referenced by the ``top.sls`` via "dot-notation". For example we have our directory structure::

    top.sls
      core/
        init.sls
        symlink.sls

Then in our ``top.sls`` we could target the specific sub module by::

    base:
      '*':
        - core          # targets the init.sls
        - core.symlink  # targets the core/symlink.sls

Grain Matching
--------------

In our ``top.sls`` we are matching on grains (as witnessed by the ``-match: grain``).

Because we configured out minions to use the roles grain, we can target specific minions by their role. We could also match by any of the other grains available via salt. To see a list of all grains available you could run the ``grains.ls`` command::

    root@master-name# salt '*' grains.ls
    web1:
        - cpu_flags
        - cpu_model
        - cpuarch
        - defaultencoding
        - defaultlanguage
        - domain
        - fqdn
        - gpus
        - host
        - id
        - ipv4
        - kernel
        - kernelrelease
        - localhost
        - lsb_codename
        - lsb_description
        - lsb_id
        - lsb_release
        - mem_total
        - nodename
        - num_cpus
        - num_gpus
        - os
        - os_family
        - oscodename
        - osfullname
        - osrelease
        - path
        - ps
        - pythonpath
        - pythonversion
        - roles
        - saltpath
        - saltversion
        - server_id
        - shell
        - virtual
        - virtual_subtype
