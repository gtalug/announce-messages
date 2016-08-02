# GTALUG Announce Messages

This repository contains the sources for the different GTALUG announces the 
operations team sends out. One day this process will be automated.

## Requirements

* Python 2.7 (Fabric isn't Python 3 compatible yet)
* Fabric
    * See their install docs: <http://www.fabfile.org/installing.html>
* dateutils
    * Usually in distro's package repo (`python-dateutil` in debian).
    * You can also install with `pip install dateutils`.

## Usage

* `fab new_meeting`: Generates a new meeting from the template.
* `fab send_meeting`: Send the meeting announcement.
