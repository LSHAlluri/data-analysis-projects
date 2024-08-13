# 1. Declare and assign the variables here:

shuttle_name = "Determination";
shuttle_speed_mph = 17500;
Mars_distance_km = 225000000;
Moon_distance_km = 384400;
Miles_per_km = 0.621;

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttle_name));
print(type(shuttle_speed_mph));
print(type(Mars_distance_km));
print(type(Moon_distance_km));
print(type(Miles_per_km));

# Code your solution to exercises 3 and 4 here:
# 3
miles_to_Mars = Mars_distance_km * Miles_per_km;
hours_to_Mars = miles_to_Mars / shuttle_speed_mph;
days_to_Mars = hours_to_Mars/24;

#4
print(shuttle_name, " will take ", days_to_Mars, "days to reach Mars.")

# Code your solution to exercise 5 here

miles_to_moon = Moon_distance_km * Miles_per_km;
hours_to_moon = miles_to_moon / shuttle_speed_mph;
days_to_moon = hours_to_moon/24;

print(shuttle_name, " will take ", days_to_moon);
print("days to Moon.");