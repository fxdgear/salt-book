==========================
Chapter 2: Getting Started
==========================

So obviously the reason you're here is cause you want to know how to provision a server or group of servers. You want to be able to deploy code. You want to be able to play video games and drink coffee while the computers do all the work.

Installation and Configuration
------------------------------

First you need to have an understanding of your network or what you want your network to be. In this post we are going to have a network which contains 2 web nodes, 1 db node, and 1 redis node. That's 4 minions. We will also have 1 separate node which will be the salt master. It will exist only and solely for the purpose of being the salt master. Though this does not have to be the case. Any of the 4 minions could **also** be the master.

Salt Master
^^^^^^^^^^^

Installation
~~~~~~~~~~~~

Assuming we are using Ubuntu the installation of salt-master is as simple as::

    root@master-name# apt-get install software-properties-common
    root@master-name# add-apt-repository ppa:saltstack/salt
    root@master-name# apt-get update
    root@master-name# apt-get install salt-master

For more detailed instructions of installing salt (for example in different OS please see the `official documentation`__).

__ http://docs.saltstack.com/topics/installation/index.html)

Configuration
~~~~~~~~~~~~~

After salt has been installed we need to configure the salt master. Assuming you've installed salt using the above mentioned method, the configuration file for the salt-master will be located at ``/etc/salt/master``. Now it's time to edit this file::

    root@master-name# vim /etc/salt/master

First thing you'll probably notice is how large this file is. There are a lot of settings that are commented out, meaning that salt is taking the default action or using the default setting.

The one setting we're going to have to take care of is telling the salt master where to find the state files. This can be done via one of two methods (or a combination of the two).

#. specify the ``file_roots``
#. specify the ``fileserver_backend`` to be ``git`` and use a git repository as the place to look for salt state files.

If you're going to go with option 1 then you should create a location on the server that will be the "root" directory. The default location is ``/srv/salt``. An example of how to specify the file_roots setting::

    file_roots:
      base:
        - /srv/salt

Personally I prefer option 2. Which will require the additional setting of ``fileserver_backend``. In option 1, the salt configuration file defaults the ``fileserver_backed`` to ``roots`` which requires specifying where the ``file_roots`` directory will be. In option 2, you have to specify the ``fileserver_backed`` to be ``git``. Then you will have to set the ``gitfs_remotes`` settings.

An example of what this would all look like would be::

    fileserver_backend:
      - git

    gitfs_remotes:
      - git://github.com/saltstack/salt-states.git

Additionally you could in theory specify both. In which salt would look at the order of your ``fileserver_backends`` as the order in which to apply states::

    fileserver_backend:
      - git
      - roots

    gitfs_remotes:
      - git://github.com/saltstack/salt-states.git

    file_roots:
      base:
        - /srv/salt

In this instance Salt will look **first** at the git repo, and **second** at the file_roots directory.

Once you've got your configuration setting finished, you must restart the salt-master for the settings to take effect::

    root@master-name# service salt-master restart

Salt Minion
^^^^^^^^^^^

Installation
~~~~~~~~~~~~

Similarly to the salt-master installation you would install salt by::

    root@minion-name# apt-get install software-properties-common
    root@minion-name# add-apt-repository ppa:saltstack/salt
    root@minion-name# apt-get update
    root@minion-name# apt-get install salt-minion

Configuration
~~~~~~~~~~~~~

The salt minion is configuration is located at ``/etc/salt/minion``

Configuring the minion is just as simple as configuring the master. First you must specify the ``master`` to communicate to. This could be an IP address a domain name, a host name, etc… Any FQDN (Fully Qualified Domain Name) will suffice::

    master: 123.123.123.123

Next since we have 4 minions (web1, web2, db and redis) we should define some roles. The role that a your minion has can be defined by setting the ``roles`` ``grain``. (We will cover grains in more depth later).

To specify your webservers you could do something like::

    grains:
      roles:
        - webserver

To specify your database server you could do something like::

    grains:
      roles:
        - dbserver

And to specify your redis server you could do something like::

    grains:
      roles:
        - redis-server

In order for the configurations to take effect you must restart the minions::

    root@minion-name# service salt-minion restart

Communication Between Minions and Master
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Once the minions and master have been installed and configured it's time to have the master "accept" the minions. This is done by the ``salt-key`` command on the master.

``salt-key`` will return a list of all "Accepted", "Rejected" and "Pending" minions. To accept all pending minions just run the ``salt-key -A`` command, or to accept them one by one run ``salt-key -a <minion-name>`` where ``<minion-name>`` is a name of a minion listed in the pending list.

To test the communication between your master and minion you can run the following command::

    root@minion-name# salt '*' test.ping

It should return with something like::

    web1:
        True
    web2:
        True
    redis:
        True
    db:
        True
