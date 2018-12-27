Codes Implemented by Sercan Yetkin
==================================

Add Plane
---------
Get required arguments from admin and add them into planes table.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 152-180
   
   
Add Airport
-----------
Get required arguments from admin and add them into airports table.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 211-253

Add Flights
-----------
If airports and planes tables are filled before, get required arguments from admin and add them into flights table to create one.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 770-823
   
List All Flights
----------------
Read flights, airports, cities and planes tables, then join each other, then display filghts information.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 92-112
   
Delete Flights
--------------
Choose a flight from flight list, then delete its data from flights table, but tickets table should be deleted before due to reference key.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 826-876
   
Set discount for a flight
-------------------------
Choose a flight from flight list, then update its discount rate with its price from tickets table.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 255-308
   
Search oneway flight
--------------------
Get date, destination city and departure city from user,then check it if there is a flight with this information. If yes, list them.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 66-90

Search roundtrip flight
-----------------------
Get date, destination city and departure city from user,then check it if there is a roundtrip flight with this information. If yes, list them.

.. literalinclude:: /../../server.py
   :language: python
   :linenos:
   :lines: 114-150

   
