# myanmar font conversion functions for QGIS 3.X
# prerequisites - python-myanmar module
#-------------------------------------------------------------------
# written by 
#           Kyaw Naing Win
#           GIS Program Manager, OneMap Technical Unit
#           kyawnaingwinknw@gmail.com
# date: 2019 - 03 - 21
#--------------------------------------------------------------------
# Disclaimer: This script is as-is and its accuracy is not evaluated.
#--------------------------------------------------------------------
from myanmar.converter import convert as mc

@qgsfunction(args='auto', group='FontConversion')
def win2zg(value1, feature, parent):
    """
    Convert from Win font to Zawgyi
    <h2>Example usage:</h2>
    <ul>
      <li>win2zg(string)</li>
      <li>win2zg(text_field)</li>
    </ul>
    """
    return mc(value1, 'wininnwa', 'zawgyi')

@qgsfunction(args='auto', group='FontConversion')
def win2uni(value1, feature, parent):
    """
    Convert from Win font to Unicode
    <h2>Example usage:</h2>
    <ul>
      <li>win2uni(string)</li>
      <li>win2uni(text_field)</li>
    </ul>
    """
    return mc(value1, 'wininnwa', 'unicode')
   
@qgsfunction(args='auto', group='FontConversion')
def uni2win(value1, feature, parent):
    """
    Convert from Unicode to Win font
    <h2>Example usage:</h2>
    <ul>
      <li>uni2win(string)</li>
      <li>uni2win(text_field)</li>
    </ul>
    """
    return mc(value1, 'unicode', 'wininnwa')

@qgsfunction(args='auto', group='FontConversion')
def uni2zg(value1, feature, parent):
    """
    Convert from Unicode to Zawgyi
    <h2>Example usage:</h2>
    <ul>
      <li>uni2zg(string)</li>
      <li>uni2zg(text_field)</li>
    </ul>
    """
    return mc(value1, 'unicode', 'zawgyi')
    
@qgsfunction(args='auto', group='FontConversion')
def zg2win(value1, feature, parent):
    """
    Convert from Zawgyi to Win font
    <h2>Example usage:</h2>
    <ul>
      <li>zg2win(string)</li>
      <li>zg2win(text_field)</li>
    </ul>
    """
    return mc(value1, 'zawgyi', 'wininnwa')
 
@qgsfunction(args='auto', group='FontConversion')
def zg2uni(value1, feature, parent):
    """
    Convert from Zawgyi to Unicode
    <h2>Example usage:</h2>
    <ul>
      <li>zg2uni(string)</li>
      <li>zg2uni(text_field)</li>
    </ul>
    """
    return mc(value1, 'zawgyi', 'unicode')
