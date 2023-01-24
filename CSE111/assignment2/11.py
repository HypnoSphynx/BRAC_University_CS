class Wadiya():
    def __init__(self):
        self.name = 'Aladeen'
        self.designation = 'President Prime Minister Admiral General'
        self.num_of_wife = 100
        self.dictator = True
wadiya = Wadiya()
print("Part1:")
print("Name of President:",wadiya.name)
print("Designation:",wadiya.designation)
print("Number of wife:",wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)
print("Part2:")
wadiya.name="Donald Trump"
wadiya.designation="President"
wadiya.num_of_wife=1
wadiya.dictator = False
print("Name of President:",wadiya.name)
print("Designation:",wadiya.designation)
print("Number of wife:",wadiya.num_of_wife)
print("Is he/she a dictator:", wadiya.dictator)
print("Previous information lost")