# plane_seating.py algorithm

As described by the code, the algorithm to seat the plane is as follows:

Seat the economy plus passengers, then seat the economy passengers. They prefer the windows and front of the plane. 
As you seat economy plus passengers, add a random amount (1-4) of economy passengers to a *dictionary* that is keeping track of amount of seats that are spoken for. 
When you finally have a full flight worth of claimed seats, only then do you begin to randomly seat the economy passengers in the remaining seats. 

The only code that I modified was the code to have the economy plus passengers prefer the front of the plane, as specified in the assignment. 