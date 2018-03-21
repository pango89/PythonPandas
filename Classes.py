from marshmallow import Schema, fields, post_load
class MyClass(object):
    def __init__(self,name,value):
        self.name = name
        self.value = value

class Route(object):
    def __init__(self,route_name,stop_sequence,location_id,latitude,longitude,date):
        self.route_name = route_name
        self.stop_sequence = stop_sequence
        self.location_id = location_id
        self.latitude = latitude
        self.longitude = longitude
        self.date = date



class MyClassSchema(Schema):
    name = fields.Str()
    value = fields.Int()

    @post_load
    def make_myClass(self,data):
        return MyClass(**data)

class RouteSchema(Schema):
    route_name = fields.Str(load_from="RouteName")
    stop_sequence = fields.Int(load_from="StopSequence")
    location_id = fields.Int(load_from="LocationID")
    latitude = fields.Float(load_from="Latitude")
    longitude = fields.Float(load_from="Longitude")
    date = fields.DateTime(load_from="Date")

    @post_load
    def make_route(self,data):
        return Route(**data)








