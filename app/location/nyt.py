"""app.locations.nyt.py"""
from . import TimelinedLocation
from . import TimelinedLocationBuilderInterface


class NYTLocation(TimelinedLocation):
    """
    A NYT (county) Timelinedlocation.
    """

    # pylint: disable=too-many-arguments,redefined-builtin
    def __init__(self, id, state, county, coordinates, last_updated, timelines):
        super().__init__(id, "US", state, coordinates, last_updated, timelines)

        self.state = state
        self.county = county

    def serialize(self, timelines=False):  # pylint: disable=arguments-differ,unused-argument
        """
        Serializes the location into a dict.

        :returns: The serialized location.
        :rtype: dict
        """
        serialized = super().serialize(timelines)

        # Update with new fields.
        serialized.update(
            {"state": self.state, "county": self.county,}
        )

        # Return the serialized location.
        return serialized


class NYTLocationBuilder(TimelinedLocationBuilderInterface):
    """
    The Concrete Builder for NYT
    """

    # pylint: disable=too-many-arguments,redefined-builtin
    def __init__(self, id, state, county, coordinates, last_updated, timelines):
        super().__init__(id, "US", state, coordinates, last_updated, timelines)

        self.state = state
        self.county = county
        self.product = NYTProduct()

    def serialize(self, timelines=False):  # pylint: disable=arguments-differ,unused-argument
        """
        Serializes the location into a dict.

        :returns: The serialized location.
        :rtype: dict
        """
        serialized = super().serialize(timelines)

        # Update with new fields.
        serialized.update(
            {"state": self.state, "county": self.county,}
        )

        # Return the serialized location.
        return serialized

    # def build_part_a(self):
    #     #this should actually puts the "part" inside the object, part being id, state, country, etc.
    #     self.product.parts.append('additional parts')
    #     return self

class NYTDirector:
    """
    The Director, building a complex representation.
    """
    def construct():
        return NYTLocationBuilder()#\
            # # build and add part_a, ie. id; part_b, ie. state; etc.
            # .build_part_a()


class NYTProduct():
    """
    The Product
    """
    def __init__(self):
        """
        the NYT product should be empty when the init method is first called
        containing a parts attribute
        which is of type dictionary
        """
        self.parts = {}
        pass


# # The Client
# #client code that initiates the construction process
# #this should belong where all the other client codes are 
# PRODUCT = NYTDirector.construct()