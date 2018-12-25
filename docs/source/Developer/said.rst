Parts Implemented by Muhammed Said Dikici
=========================================

*Tickets Table*
--------------

A - Fields of Tickets Table
^^^^^^^^^^^^^^^^^^^^^^^^
	
	===========	=========	=======================	===========	================
	FIELD NAME	TYPE		DETAILS			PRIMARY KEY	FOREIGN KEY REF.
	===========	=========	=======================	===========	================
	FLIGHT_ID	INTEGER		ID of flight		X		FLIGHTS - FLIGHT_ID
	TICKET_ID	INTEGER		ID of ticket		X	
	USERNAME	VARCHAR		Owner of the ticket			USERS
	PRICE		NUMERIC		Price after discount		 			
	CLASS		CHARACTER	Economy-Business class		 			
	SEAT_NUMBER	INTEGER		Seat number of ticket			
	RATE		NUMERIC		1 - Discount rate				
	BASE_PRICE	NUMERIC		Price without discount	
	===========	=========  	=======================	===========	================

		
B - Tickets Table Create Statement
^^^^^^^^^^^^^^^^^^^^^^^^^
	.. literalinclude:: /../../dbinit.py
	   :language: sql
	   :linenos:
	   :caption: Tickets Table
	   :name: Tickets
	   :lines: 126-146

*Cities Table*
--------------

A - Fields of Cities Table
^^^^^^^^^^^^^^^^^^^^^^^^

	===========	=========	=======================	===========	================
	FIELD NAME	TYPE		DETAILS			PRIMARY KEY	FOREIGN KEY REF.
	===========	=========	=======================	===========	================
	CITY_ID		INTEGER		ID of city		X		
	CITY		VARCHAR		City			
	===========	=========  	=======================	===========	================

	
B - Cities Table Create Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
	.. literalinclude:: /../../dbinit.py
	   :language: sql
	   :linenos:
	   :caption: Cities Table
	   :name: Cities
	   :lines: 75-78

*Users Table*
--------------

A - Fields of Users Table
^^^^^^^^^^^^^^^^^^^^^^^^
	
	===========	=========	=======================	===========	================
	FIELD NAME	TYPE		DETAILS			PRIMARY KEY	FOREIGN KEY REF.
	===========	=========	=======================	===========	================
	USERNAME	VARCHAR		User's name		X		
	PASSWORD	VARCHAR		User's password				
	===========	=========  	=======================	===========	================

		
B - Users Table Create Statement
^^^^^^^^^^^^^^^^^^^^^^^^^
	.. literalinclude:: /../../dbinit.py
	   :language: sql
	   :linenos:
	   :caption: Users Table
	   :name: Users
	   :lines: 10-14
