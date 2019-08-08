pretix newsletter integration for mailing lists
===============================================

This is a plugin for `pretix`_. 

Development setup
-----------------

1. Make sure that you have a working `pretix development setup`_.

2. Clone this repository, eg to ``local/pretix-newsletter-ml``.

3. Activate the virtual environment you use for pretix development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretix's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretix server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Copyright 2017 Raphael Michel

Released under the terms of the Apache License 2.0

Thanks
------

The initial development of this official pretix plugin has been funded by our friends at ERNW Insight.
Thank you very much!

.. image:: _res/logo-ernw-insight.png
   :target: https://www.ernw-insight.de/

If you also want to contribute to the development of the open pretix ecosystem by sponsoring the
development of a feature or plugin, please get in touch at support@pretix.eu!


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
