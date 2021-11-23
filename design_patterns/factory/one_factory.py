"""
Factory Method Implementation
ref link: https://realpython.com/factory-method-python/

Example for converting(converting to other type is also called serializing)
In this example we will be converting the song object to the given format mentioned by user
It can be either i.JSON ii.XML or if not them then will raise value error
"""
"""
As per my understanding factory method pattern is a 3 layer pattern
In which :
1. CLient layer which should not be modified (in this case we have serialize function)
2. Middle layer which is basically the if else ladder function(in this case we have get_serializer function)
3. Concrete layer (can be called as) it's basically for each option a separate class or function (in this case we have _serialize_to_json, _serialize_to_xml) 
"""
import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self,sid,title,artist):
        self.sid = sid
        self.title = title
        self.artist = artist

# #----------Example 1: Regular Method ----------#
# class SongSerializer:
#     # def __init__(self,song_obj,format):
#     #     if format == "json":
#     #         return json.dumps(song_obj) #cannot return from init
#
#     def __init__(self,song_obj,format):
#         self.song_obj = song_obj
#         self.format = format
#
#     def serialize(self):
#         if self.format == "json":
#             return json.dumps(self.song_obj)
#         elif self.format == "xml":
#             song_info = et.Element('song', attrib={'id': song_obj.sid})
#             title = et.SubElement(song_info,'title')
#             title.text = song_obj.title
#             artist = et.SubElement(song_info,'artist')
#             artist.text = song_obj.artist
#             return et.tostring(song_info,encoding='unicode')
#         else:
#             raise ValueError(self.format)
#
# #----------END Example 1----------#
"""
note about above example:
The Problems With Complex Conditional Code
The example above exhibits all the problems you’ll find in complex logical code. Complex logical code uses if/elif/else structures to change the behavior of an application. Using if/elif/else conditional structures makes the code harder to read, harder to understand, and harder to maintain.
"""
# #----------Example 2----------#
# #Song object will remain the same only we will change the factory method
# # in this example we will be replacing the code inside serializer function if else ladder with another function
# #so the statement inside if else ladder will be put into a separate function
#
# class SongSerializer:
#     def __init__(self,song_obj,format):
#         self.song_obj = song_obj
#         self.format = format
#
#     def serialize(self):
#         if self.format == "json":
#             return self._serialize_to_json()
#         elif self.format == "xml":
#             return self._serialize_to_xml()
#         else:
#             raise ValueError(self.format)
#
#     def _serialize_to_json(self):
#         return json.dumps(self.song_obj)
#
#     def _serialize_to_xml(self):
#         song_info = et.Element('song', attrib={'id': song_obj.sid})
#         title = et.SubElement(song_info, 'title')
#         title.text = song_obj.title
#         artist = et.SubElement(song_info, 'artist')
#         artist.text = song_obj.artist
#         return et.tostring(song_info, encoding='unicode')
# #----------End Example 2----------#


#----------Example 3----------#
class SongSerializer:
    def __init__(self,song_obj,format):
        self.song_obj = song_obj
        self.format = format

    def serialize(self): #client component
        serializer = self._get_serializer()

    def _get_serializer(self): #creator component. The creator decides which concrete implementation to use.
        if self.format == "json":
            return self._serialize_to_json()
        elif self.format == "xml":
            return self._serialize_to_xml()
        else:
            raise ValueError(self.format)

    def _serialize_to_json(self): #concrete implementation
        return json.dumps(self.song_obj)

    def _serialize_to_xml(self):# conctrete implementation
        song_info = et.Element('song', attrib={'id': song_obj.sid})
        title = et.SubElement(song_info, 'title')
        title.text = song_obj.title
        artist = et.SubElement(song_info, 'artist')
        artist.text = song_obj.artist
        return et.tostring(song_info, encoding='unicode')


    

"""
Factory Method is a good replacement because you can put the body of each logical path into separate functions or classes with a common interface, and the creator can provide the concrete implementation.
"""
if __name__ == "__main__":
    song_obj = Song(sid="1",title="titanium",artist="david_guetta",)
    serializer_obj = SongSerializer(song_obj=song_obj,format="xml")
    print(serializer_obj.serialize())
