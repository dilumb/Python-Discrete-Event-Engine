# Python-Discrete-Event-Engine
Python Discrete Event Engine (DES) can be use to build many discrete event simulators. It supports any data type or object and is capable of handling large event lists (use binary search to sort events). See source code for details.

Usage:
from DES import Event

events = DES()

#Add set of events
#event time, event type, node/customer/server ID, data
events.addEvent(5.5, 'Type1', 1, 'Test data 1')
events.addEvent(3.3, 'Type2', 2, [1, 2, 3, 4])
events.addEvent(1.5, 'Type3', 3, 567890)
events.addEvent(9.9, 'Type4')
events.addEvent(8.6, 'Type3', 1, 'Test data 5')

#remove event
#Provide at least event time & type
events.removeEvent(3.3, 'Type2', 2)

#Get remaining events in chronological order
event = events.getNextEvent()
print event.startTime, event.eventType
event = events.getNextEvent()
print event.startTime, event.eventType
event = events.getNextEvent()
print event.startTime, event.eventType

#Current simulation time
print 'Current time', events.now

event = events.getNextEvent()
print event.startTime, event.eventType
event = events.getNextEvent()
print event #No more events
 
Returns:
1.5 Type3
5.5 Type1
8.6 Type3
Current time 8.6
9.9 Type4
None
