Parts Implemented by Sercan Yetkin
==================================

Flights Table
--------------

Fields of Flights Table
^^^^^^^^^^^^^^^^^^^^^^^^
	
==============	=========	=======================	===========	================
FIELD NAME	TYPE		DETAILS			PRIMARY KEY	FOREIGN KEY REF.
==============	=========	=======================	===========	================
flight_id	INTEGER		Flight id		X		
destination_id	INTEGER		Destination city			Airports			
departure_id	INTEGER		Departure city id			Airports
plane_id	INTEGER		Plane id 				Planes		 			
departure_time	TIMESTAMP	Departure time		 			
arrival_time	TIMESTAMP	Arrival time			
==============	=========  	=======================	===========	================

	
Flights Table Create Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: /../../dbinit.py
   :language: sql
   :linenos:
   :caption: Flights Table
   :name: Flights
   :lines: 102-122

Airports Table
--------------

Fields of Airports Table
^^^^^^^^^^^^^^^^^^^^^^^^
	
============	=========	=======================	===========	================
FIELD NAME	TYPE		DETAILS			PRIMARY KEY	FOREIGN KEY REF.
============	=========	=======================	===========	================
airport_id	INTEGER		Airport id		X		
airport_name	VARCHAR		Airport name						
city_id		INTEGER		City id					Cities		
============	=========  	=======================	===========	================

	
Airports Table Create Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: /../../dbinit.py
   :language: sql
   :linenos:
   :caption: Airports Table
   :name: Airports
   :lines: 89-99

Planes Table
--------------

Fields of Planes Table
^^^^^^^^^^^^^^^^^^^^^^^^
	
==============	=========	=======================	===========	================
FIELD NAME	TYPE		DETAILS			PRIMARY KEY	FOREIGN KEY REF.
==============	=========	=======================	===========	================
plane_id	INTEGER		Plane id		X		
plane_model	VARCHAR		Plane model						
bsn_capacity	INTEGER		Busines capacity			
eco_capacity	INTEGER		Economy capacity 					 				
==============	=========  	=======================	===========	================

	
Planes Table Create Statement
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: /../../dbinit.py
   :language: sql
   :linenos:
   :caption: Planes Table
   :name: Planes
   :lines: 81-86
