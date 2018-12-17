linkable-py
===========

.. image:: https://travis-ci.org/meyt/linkable-py.svg?branch=master
    :target: https://travis-ci.org/meyt/linkable-py

.. image:: https://coveralls.io/repos/github/meyt/linkable-py/badge.svg?branch=master
    :target: https://coveralls.io/github/meyt/linkable-py?branch=master

Detect URL, Email, Hashtag and Mention from plain-text and convert into HTML hyperlink.


Install
-------

.. code-block:: bash

    $ pip install linkable


Usage
=====

Basic:

.. code-block:: python

      from linkable import Linkable

      text = 'This is test with a #hashtag from @linkable on github.com'
      print(Linkable(text))


Output:

.. code-block:: html

    This is test with <a href="/hashtag/#hashtag">#hashtag</a> from <a href="/@linkable">@linkable</a> on <a href="http://github.com">github.com</a>



Links list:

.. code-block:: python

      from linkable import LinkableList

      text = 'This is test with a #hashtag from @linkable on github.com'
      print(LinkableList(text).links)

Output:

.. code-block::

    ['#hashtag', '@linkable', 'github.com']
