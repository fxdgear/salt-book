===============================
Chapter 1: Introduction to Salt
===============================

States
------

What is state? State is the "condition" or "shape" that a specific machine is in. More to the point, "state" is what applications are installed? What files are in which directories? What services are currently running (not running)?

By using Salt State files (``.sls``). An ``sls`` file is a text file written in (usually) YAML, which specifies a particular unit of state for the server. For example we want to specify that apache is going to be installed and running.

    httpd:
      pkg:
        - installed
        - name: apache2
      service:
        - running
        - name: apache2
        - enable: True
        - require:
          - pkg: mod_wsgi

This very simple file will do two things:
1. ensure that the package named ``apache`` is installed
2. ensure that the service named ``apache`` is running.

Using state files we can also ensure the existence or absence files and or directories. We can ensure that specific repositories (git, svn, hg) are checked out at a specified location in the file system. We can ensure that a specified database exists, specified database users exist. We can ensure that specific public keys are in the ``authorized_keys`` directory. Just about anything that a specific machine might need in order to do its job, can be controlled via states. For a complete list of built in state modules, see `http://docs.saltstack.com/ref/states/all/index.html`__

__ http://docs.saltstack.com/ref/states/all/index.html

Modules
-------

Modules are commands that can be run on a specified machine. Salt comes bundled with a bunch of pre-written `modules`__. Modules are used for when you want to remotely execute commands on one or more remote servers. For example, you have 6 servers. Each of these servers have the apache service running. You've made a site wide change that requires the restart of apache. You can do one of two things.
1. SSH to each box individually, and issue the command ``service apache2 restart``
2. OR you can SSH to one box (Salt Master) and issue the command ``salt '*' apache.signal restart``

__ http://docs.saltstack.com/ref/modules/all/index.html

Which one seems more efficient? I hope you said #2.


Pillars
-------
