"""app.locations.csbs.py"""
from . import Location
from . import LocationBuilderInterface


class CSBSLocation(Location):
    """
    A CSBS (county) location.
    """

    # pylint: disable=too-many-arguments,redefined-builtin
    def __init__(self, id, state, county, coordinates, last_updated, confirmed, deaths):
        super().__init__(
            # General info.
            id,
            "US",
            state,
            coordinates,
            last_updated,
            # Statistics.
            confirmed=confirmed,
            deaths=deaths,
            recovered=0,
        )

        self.state = state
        self.county = county

    def serialize(self, timelines=False):  # pylint: disable=arguments-differ,unused-argument
        """
        Serializes the location into a dict.

        :returns: The serialized location.
        :rtype: dict
        """
        serialized = super().serialize()

        # Update with new fields.
        serialized.update(
            {"state": self.state, "county": self.county, }
        )

        # Return the serialized location.
        return serialized


class CSBSLocationBuilder(LocationBuilderInterface):
    """"    
    The Concrete Builder for CSBS
    """

    # pylint: disable=too-many-arguments,redefined-builtin
    def __init__(self, id, state, county, coordinates, last_updated, confirmed, deaths):
        super().__init__(
            # General info.
            id,
            "US",
            state,
            coordinates,
            last_updated,
            # Statistics.
            confirmed=confirmed,
            deaths=deaths,
            recovered=0,
        )

        self.state = state
        self.county = county
        self.product = CSBSProduct()

    def serialize(self, timelines=False):  # pylint: disable=arguments-differ,unused-argument
        """
        Serializes the location into a dict.

        :returns: The serialized location.
        :rtype: dict
        """
        serialized = super().serialize()

        # Update with new fields.
        serialized.update(
            {"state": self.state, "county": self.county, }
        )

        # Return the serialized location.
        return serialized

    #def build_part_a(self):
        # #this should actually puts the "part" inside the object, part being id, state, country, etc.
        # self.product.parts.append('additional parts')
        #return self

class CSBSDirector:
    """
    The Director, building a complex representation.
    """
    def construct():
        return CSBSLocationBuilder()#\
            # # build and add part_a, ie. id; part_b, ie. state; etc.
            # .build_part_a()


class CSBSProduct():
    """
    The Product
    """
    def __init__(self):
        """
        the CSBS product should be empty when the init method is first called
        containing a parts attribute
        which is of type dictionary
        """
        self.parts = {}
        pass


# # The Client
# #client code that initiates the construction process
# #this should belong where all the other client codes are 
# PRODUCT = CSBSDirector.construct()