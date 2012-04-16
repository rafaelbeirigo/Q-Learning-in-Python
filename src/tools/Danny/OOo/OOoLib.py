#**********************************************************************
#
#   Danny.OOo.OOoLib.py
#
#   A module to easily work with OpenOffice.org.
#
#**********************************************************************
#   Copyright (c) 2003-2004 Danny Brewer
#   d29583@groovegarden.com
#
#   This library is free software; you can redistribute it and/or
#   modify it under the terms of the GNU Lesser General Public
#   License as published by the Free Software Foundation; either
#   version 2.1 of the License, or (at your option) any later version.
#
#   This library is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#   Lesser General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public
#   License along with this library; if not, write to the Free Software
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   See:  http://www.gnu.org/licenses/lgpl.html
#
#**********************************************************************
#   If you make changes, please append to the change log below.
#
#   Change Log
#   Danny Brewer         Revised 2004-06-07-01
#
#**********************************************************************

import string

# OOo's libraries
import uno


#------------------------------------------------------------
#   Uno ServiceManager access
#   A different version of this routine and global variable
#    is needed for code running inside a component.
#------------------------------------------------------------


# The ServiceManager of the running OOo.
# It is cached in a global variable.
goServiceManager = False
def getServiceManager( cHost="localhost", cPort="8100" ):
    """Get the ServiceManager from the running OpenOffice.org.
        Then retain it in the global variable goServiceManager for future use.
        This is similar to the GetProcessServiceManager() in OOo Basic.
    """
    global goServiceManager
    if not goServiceManager:
        # Get the uno component context from the PyUNO runtime
        oLocalContext = uno.getComponentContext()
        # Create the UnoUrlResolver on the Python side.
        oLocalResolver = oLocalContext.ServiceManager.createInstanceWithContext(
                                    "com.sun.star.bridge.UnoUrlResolver", oLocalContext )
        # Connect to the running OpenOffice.org and get its context.
        oContext = oLocalResolver.resolve( "uno:socket,host=" + cHost + ",port=" + cPort + ";urp;StarOffice.ComponentContext" )
        # Get the ServiceManager object
        goServiceManager = oContext.ServiceManager
    return goServiceManager


#------------------------------------------------------------
#   Uno convenience functions
#   The stuff in this section is just to make
#    python progrmaming of OOo more like using OOo Basic.
#------------------------------------------------------------


# This is the same as ServiceManager.createInstance( ... )
def createUnoService( cClass ):
    """A handy way to create a global objects within the running OOo.
    Similar to the function of the same name in OOo Basic.
    """
    oServiceManager = getServiceManager()
    oObj = oServiceManager.createInstance( cClass )
    return oObj


# The StarDesktop object.  (global like in OOo Basic)
# It is cached in a global variable.
StarDesktop = None
def getDesktop():
    """An easy way to obtain the Desktop object from a running OOo.
    """
    global StarDesktop
    if StarDesktop == None:
        StarDesktop = createUnoService( "com.sun.star.frame.Desktop" )
    return StarDesktop
# preload the StarDesktop variable.
getDesktop()


# The CoreReflection object.
# It is cached in a global variable.
goCoreReflection = False
def getCoreReflection():
    global goCoreReflection
    if not goCoreReflection:
        goCoreReflection = createUnoService( "com.sun.star.reflection.CoreReflection" )
    return goCoreReflection


def createUnoStruct( cTypeName ):
    """Create a UNO struct and return it.
    Similar to the function of the same name in OOo Basic.
    """
    oCoreReflection = getCoreReflection()
    # Get the IDL class for the type name
    oXIdlClass = oCoreReflection.forName( cTypeName )
    # Create the struct.
    oReturnValue, oStruct = oXIdlClass.createObject( None )
    return oStruct



#def newConnectionToOOo( cHost="localhost", cPort="8100" ):
#    """Call this to establish, or re-establish a connection to OOo."""
#    global goServiceManager
#    global StarDesktop
#    global goCoreReflection
#    goServiceManager = False
#    StarDesktop = None
#    goCoreReflection = False
#    getServiceManager( cHost, cPort )
#    getDesktop()



#------------------------------------------------------------
#   API helpers
#------------------------------------------------------------

def hasUnoInterface( oObject, cInterfaceName ):
    """Similar to Basic's HasUnoInterfaces() function, but singular not plural."""

    # Get the Introspection service.
    oIntrospection = createUnoService( "com.sun.star.beans.Introspection" )

    # Now inspect the object to learn about it.   
    oObjInfo = oIntrospection.inspect( oObject )
   
    # Obtain an array describing all methods of the object.
    oMethods = oObjInfo.getMethods( uno.getConstantByName( "com.sun.star.beans.MethodConcept.ALL" ) )
    # Now look at every method.
    for oMethod in oMethods:
        # Check the method's interface to see if
        #  these aren't the droids you're looking for.
        cMethodInterfaceName = oMethod.getDeclaringClass().getName()
        if cMethodInterfaceName == cInterfaceName:
            return True
    return False

def hasUnoInterfaces( oObject, *cInterfaces ):
    """Similar to the function of the same name in OOo Basic."""
    for cInterface in cInterfaces:
        if not hasUnoInterface( oObject, cInterface ):
            return False
    return True



#------------------------------------------------------------
#   High level general purpose functions
#------------------------------------------------------------


def makePropertyValue( cName=None, uValue=None, nHandle=None, nState=None ):
    """Create a com.sun.star.beans.PropertyValue struct and return it.
    """
    oPropertyValue = createUnoStruct( "com.sun.star.beans.PropertyValue" )

    if cName != None:
        oPropertyValue.Name = cName
    if uValue != None:
        oPropertyValue.Value = uValue
    if nHandle != None:
        oPropertyValue.Handle = nHandle
    if nState != None:
        oPropertyValue.State = nState

    return oPropertyValue


def makePoint( nX, nY ):
    """Create a com.sun.star.awt.Point struct."""
    oPoint = createUnoStruct( "com.sun.star.awt.Point" )
    oPoint.X = nX
    oPoint.Y = nY
    return oPoint


def makeSize( nWidth, nHeight ):
    """Create a com.sun.star.awt.Size struct."""
    oSize = createUnoStruct( "com.sun.star.awt.Size" )
    oSize.Width = nWidth
    oSize.Height = nHeight
    return oSize


def makeRectangle( nX, nY, nWidth, nHeight ):
    """Create a com.sun.star.awt.Rectangle struct."""
    oRect = createUnoStruct( "com.sun.star.awt.Rectangle" )
    oRect.X = nX
    oRect.Y = nY
    oRect.Width = nWidth
    oRect.Height = nHeight
    return oRect


def Array( *args ):
    """This is just sugar coating so that code from OOoBasic which
    contains the Array() function can work perfectly in python."""
    tArray = ()
    for arg in args:
        tArray += (arg,)
    return tArray


def loadComponentFromURL( cUrl, tProperties=() ):
    """Open or Create a document from it's URL.
    New documents are created from URL's such as:
        private:factory/sdraw
        private:factory/swriter
        private:factory/scalc
        private:factory/simpress
    """
    StarDesktop = getDesktop()
    oDocument = StarDesktop.loadComponentFromURL( cUrl, "_blank", 0, tProperties )
    return oDocument



#def makeWriterDocument():
#    """Create a new OOo Writer document."""
#    return loadComponentFromURL( "private:factory/swriter" )
#
#
#def makeCalcDocument():
#    """Create a new OOo Calc document."""
#    return loadComponentFromURL( "private:factory/scalc" )




#------------------------------------------------------------
#   Styles
#------------------------------------------------------------


def defineStyle( oDrawDoc, cStyleFamily, cStyleName, cParentStyleName=None ):
    """Add a new style to the style catalog if it is not already present.
    This returns the style object so that you can alter its properties.
    """

    oStyleFamily = oDrawDoc.getStyleFamilies().getByName( cStyleFamily )

    # Does the style already exist?
    if oStyleFamily.hasByName( cStyleName ):
        # then get it so we can return it.
        oStyle = oStyleFamily.getByName( cStyleName )
    else:
        # Create new style object.
        oStyle = oDrawDoc.createInstance( "com.sun.star.style.Style" )

        # Set its parent style
        if cParentStyleName != None:
            oStyle.setParentStyle( cParentStyleName )

        # Add the new style to the style family.
        oStyleFamily.insertByName( cStyleName, oStyle )

    return oStyle


def getStyle( oDrawDoc, cStyleFamily, cStyleName ):
    """Lookup and return a style from the document.
    """
    return oDrawDoc.getStyleFamilies().getByName( cStyleFamily ).getByName( cStyleName )





#------------------------------------------------------------
#   General Utility functions
#------------------------------------------------------------


def convertToURL( cPathname ):
    """Convert a Windows or Linux pathname into an OOo URL."""
    if len( cPathname ) > 1:
        if cPathname[1:2] == ":":
            cPathname = "/" + cPathname[0] + "|" + cPathname[2:]
    cPathname = string.replace( cPathname, "\\", "/" )
    cPathname = "file://" + cPathname
    return cPathname
