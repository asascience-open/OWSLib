# Do not import zope.interfaces

class IWebMapService:
    """Abstraction for an OGC Web Map Service (WMS).

    Properties
    ----------
    url : string
        Online resource URL.
    version : string
        WMS protocol version.
    capabilities : object
        Describes the capabilities metadata of the WMS.
    """

    def getcapabilities():
        """Make a request to the WMS, returns an XML document."""

    def getmap(**kw):
        """Make a request to the WMS, returns an image."""

    def getfeatureinfo(**kw):
        """Make a request to the WMS, returns data."""


class IServiceIdentificationMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    service : string
        "WMS", "WFS".
    version : string
        Version of service protocol.
    title : string
        Human-targeted title of service.
    abstract : string
        Text describing the service.
    keywords : list
        List of strings.
    rights : list
        Explanation of rights associated with service.
    """
    
class IServiceProviderMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    provider : string
        Organization name.
    url : string
        URL for provider web site.
    contact : string
        How to contact the service provider.
    """

class IServiceOperationsMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    operations : list
        List of operation descriptors.
    """
    
class IOperationMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    name : string
        "GetCapabilities", for example.
    methods : dict
        Array of method descriptors, keyed to HTTP verbs.
    """

class IMethodMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    url : string
        Method URL.
    
    TODO: constraint
    """

class IServiceContentsMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    contents : list
        List of content descriptors.
    """

class IContentMetadata:
    """OO-interface to WMS metadata.

    Properties
    ----------
    id : string
        Unique identifier.
    title : string
        Human-targeted title.
    boundingBox : 5-tuple
        Four bounding values and a coordinate reference system identifier.
    boundingBoxWGS84 : 4-tuple
        Four bounding values in WGS coordinates.
    formatOptions : list
        List of available formats, each a string.
    crsOptions : list
        List of available coordinate/spatial reference systems.
    """

class IServiceMetadata(IServiceIdentificationMetadata, IServiceProvideMetadata,
                       IServiceOperationsMetadata, IServiceContentsMetadata):
    """OWS Metadata.
    """
