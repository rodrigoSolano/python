
class Private_Class(object):
	_name_class = "private class"
	_private = "private"

	def __init__(self):
		print("This is a private class")

	def __repr__(self):
		return f"Name class: {self._name_class} , Private: {self.__private}"



object_private = Private_Class()

print(object_private._private)