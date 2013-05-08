============
Introduction
============

Salt is a way to control and manage server state (files/folders/applications/etc…) as well as run commands on external machines.

Masters and Minions
-------------------

Salt manages your servers via a master/minion concept. The Master is used to store and distrbute information, tasks, etc to the minions.

States Modules and Pillars
--------------------------

Salt can be thought of as broken up in to 3 major segments.

1. States
2. Modules
3. Pillars

**States** are the "condition" or "shape" that a specific machine is in. More to the point, "state" is what applications are installed? What files are in which directories? What services are currently running (not running)?

**Modules** are functions (either built in or custom written) that can be executed via the master on each minion.

**Pillars** can be used to store minion specific, sensitive information that needs to be access via salt processes.
