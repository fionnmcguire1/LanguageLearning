


class Airport(object):

    def __init__(self):
        self.routeMap = dict()
    def addRoute(self,src,dest):
        if src in self.routeMap.keys():
            self.routeMap[src].append(dest)
        else:
            self.routeMap[src] = [dest]

    def printAllRoutes(self,source,destination,previous_journeys=[]):

        #Not in interview
        if source in self.routeMap.keys():
            #############
            if destination in self.routeMap[source]:

                #This if was not in the interview
                #Was just print([source]+previous_journeys+[destination])
                #Resulting in current stop off being printed before correct route
                if previous_journeys == []:
                    print([source]+previous_journeys+[destination])
                else:
                    print(previous_journeys+[destination])

            routes_to_explore = list(set(self.routeMap[source])-set(previous_journeys))
            for stop_off in routes_to_explore:
                #Did not include [source] here
                self.printAllRoutes(stop_off,destination,[source]+previous_journeys+[stop_off])

new_airport = Airport()
new_airport.addRoute("A","C")
new_airport.addRoute("B","A")
new_airport.addRoute("B","C")
new_airport.addRoute("A","B")
new_airport.printAllRoutes("A","C")
