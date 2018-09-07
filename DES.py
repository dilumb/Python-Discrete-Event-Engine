'''
Created on Jan 5, 2011
Modified on Sep 7, 2018
@author:  = Dilum Bandara
@version:  = 0.2
@contact:  = dilumb@engr.colostate.edu
@license: Apache License v2.0

   Copyright 2011-2012 H. M. N. Dilum Bandara

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''

class Event:
    '''
    Event class. Track event information
    '''
    def __init__(self, startTime, eventType, NID = -1, data = None):
        '''
        @parm startTime: Start time of event
        @param eventType: Type of event
        @param NID: Node ID responsible for event 
        @param data: Data associated with event
        '''
        self.eventType = eventType 
        self.startTime = startTime
        self.NID = NID
        self.data = data


class DES:
    '''
    Discrete event simulation engine. Use binary search when adding an event
    '''
    def __init__(self):
        self._eventList = []
        self.now = 0.0 #Current time


    def __del__(self):
        self._eventList = []


    def addEvent(self, startTime, eventType, nid = -1, data = None, sort = True):
        '''
        Add an event to waiting event list
        @param startTime: Event start time
        @param eventType: Type of event
        @param nid: Node/customer/server responsible for event
        @param data: Any data associated with event
        @param sort: Do events need to be sorted (if they are already sorted set
        to false to speed up) 
        '''
        newEvent = Event(startTime, eventType, nid, data)
        if sort == True: #Sort according to time
            if len(self._eventList) == 0: 
                self._eventList.append(newEvent)
                return
            start = 0 
            end = len(self._eventList) - 1
            idx = -1
            while True:
                mid = int((start + end)/2)
                if startTime > self._eventList[mid].startTime: start = mid + 1
                else: end = mid -1
                if start > end:
                    idx = start 
                    break
                elif (self._eventList[mid].startTime <= startTime) and \
                    (self._eventList[mid + 1].startTime > startTime):
                    idx = mid + 1
                    break            
            self._eventList.insert(idx, newEvent)
            return
        else: #If input is already sorted
            self._eventList.append(newEvent)
            return


    def removeEvent(self, startTime, eventType, nid = -1):
        '''
        Remove given event from event list 
        @param startTime: Event start time
        @param eventType: Event type
        @param nid: Node responsible for event
        '''
        assert(len(self._eventList) != 0), 'Event list already empty.'
        for i in range(len(self._eventList)):  #Search for proper position
            if self._eventList[i].startTime == startTime and \
                self._eventList[i].eventType  == eventType and \
                self._eventList[i].NID == nid:
                del self._eventList[i]
                return
        assert(False), 'No such event in event list'


    def getNextEvent(self):
        '''
        Get next event from list
        @return: Next event in cronological order. Has format 
        [startTime, eventType, nid, data]. If no event, return None
        '''        
        if len(self._eventList) > 0:
            self.now = self._eventList[0].startTime
            return self._eventList.pop(0)
        else: return None