# plane_seating.py
There are several ethical issues that come up in writing this program. They exist in every situation of buying plane tickets, though. Here are the main ones present in my code.
### Family Separation
Families are not grouped together by default. This is because of the pricing model, which allows economy plus customers (who have theoretically paid more for the ability to choose a seat) get to choose, and then the algorithm randomly places all of the remaining economy members. That is a decision made by the plane company that would be difficult to defend ethically. While it is best for families to be placed together, normally plane companies let tickets purchased together sit together provided that there is enough room in the plane and that the tickets are purchased with enough room in the plane to allow the sitting togther. If a family purchases seats together before another family, there is a higher chance that they sit together, but it is not promised. This is because of the program giving higher priority to the economy plus customers than to keeping families together. I implemented this in the `seat_economy_family` function that is used for economy families of size > 1. Unlucky families will be separated (on average, one to two families are separated on each flight. It's worth noting that this program does simulate a significantly higher chance of a family flying than an individual flying, through). Families are also seated before individuals are seated.
### Miscellaneous Potential Ethical Issues
1. __Overselling__ - The flight cannot be oversold - people are only inserted into the economy list if there is room for them.
2. __Plane Safety__ - The plane does not fly until full. Due to the nature of the family seating, rows are filled methodically back to front and left to right, so the plane will be seated evenly by default.
### Overall
As far as I can tell, given the constraints, this seating algorithm performs according to the ethical constraints placed upon it (passengers who pay more get to choose first, families can be sat together, economy passengers are sat after economy plus have chosen.)
### Opportunities for Further Ethical Discussion
1. Do individuals have a higher chance of being relegated to a window? To the middle? How should this be addressed?
2. Should families get preference to be sat together (as it is right now), or should it be first-come, first-serve? What do customers who are all paying the same for economy think?
3. Should economy plus pay more for windows than for middle seats? Should there be a price incentive that aligns with seats rather than just the ability to choose?
4. How can a program like this accomodate customers who don't pay for disability accomodations but need them?
5. What if an exit row is assigned to a child that is part of a family?
Such issues would be beyond the scope of this activity but present rich opportunities for further discussions on the ethical implications of algorithm choices in this program.
