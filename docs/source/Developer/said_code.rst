Codes Implemented by Muhammed Said Dikici
=========================================

Add City
--------
Adds city to cities table by arguments that admin inserts.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 182-209
   

Buy Ticket
----------
Allows user to buy tickets. Selects tickets that username is null from tickets table and assigns it to buyer's username.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 913-1001
   
   
Create Tickets
--------------
When a flight is added, automatically creates tickets and inserts to tickets table.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 1004-1045

View Tickets
-----------
Allows user to view his/her tickets. Selects tickets from ticket table that username attribute is corresponds to current username.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 1048-1071
   
Check-in
--------
Check-in feature that allows user to select his/her seat number.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 1074-1154
