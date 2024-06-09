from pprint import pprint
import json
import xmlschema
import os
import re
from pyproj import Transformer, transform
import pandas as pd
from shapely.geometry import Polygon
import folium
from decimal import Decimal
from pyproj.transformer import TransformerGroup
from shapely.geometry import LineString, Point, Polygon
from pyproj import CRS, Transformer
import xmltodict

def aboba():
    return 1



# Обработка полученного файла
# Файлы валидации лежат в папке cad_scheme

def definition(file):
    with open('KVZU_v07.xsd', 'r', encoding='utf-8') as f:
        KVZU_v07 = f.read()
    with open('KVZU_v06.xsd', 'r', encoding='utf-8') as f:
        KVZU_v06 = f.read()
    with open('KVOKS_v03.xsd', 'r', encoding='utf-8') as f:
        KVOKS_v03 = f.read()
    with open('KVOKS_v02.xsd', 'r', encoding='utf-8') as f:
        KVOKS_v02 = f.read()    
        
    if print(KVZU_v07.is_valid(file))==True:
        FUNC_KVZU_07()
    if print(KVZU_v06.is_valid(file))==True:
        FUNC_KVZU_06()
    if print(KVOKS_v03.is_valid(file))==True:
        FUNC_KVOKS_v03()
    if print(KVOKS_v02.is_valid(file))==True:
        FUNC_KVOKS_v02()
    


def FUNC_KVZU_07(file, scheme):   
    # scheme - xml-схема документа
    # file - выписка
    xml_dict = xmltodict.parse(file)
       
    return 'Abeb'

def FUNC_KVZU_06():
    pass

def FUNC_KVOKS_v03():
    pass

def FUNC_KVOKS_v02():
    pass