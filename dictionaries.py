# Dictionaries

band = {"vocals": "Plant", "Guitar": "page", "Drums": "Dave", "as": "dsa"}

print(band.get("vocals"))
print(band["vocals"])
print(band.keys())
print(band.values())

# list of key value pairs as tuples
print(band.items())

band["as"] = "somethingelse"
band.update({"vocals": "giu"})
print(band)

band["newThing"] = "new"
print(band)

band.pop("as")
print(band)

band2 = band  # creates a reference
band3 = band.copy()  # now it's a new object

band.clear()
print(band)
print(band2)

print(band3)

# Sets

nums = {1, 2, 3, 4}
print(nums)
print(type(nums))

# no duplicates allowed
nums2 = {44, 2, 2, 2, 3, 33}
print(nums2)
print(1 in nums)

nums.add(8)
print(nums)
nums.update(nums2)
print(nums)

# Keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.intersection_update(two)
print(one)

# Keep everything except the duplicates
one = {1, 2, 3}
two = {2, 3, 4}
one.symmetric_difference_update(two)
print(one)
