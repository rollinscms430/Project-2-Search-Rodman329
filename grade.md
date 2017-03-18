# Grade

First two look good. Nice use of dictionary for state management on the word ladders.

For boggle, it looks like you have the right basic search approach. There might be an issue with how you're representing your visited
states. It looks like you're using a global list, which only allows each position on the grid to be visited one time. This is too
restrictive: you can only visit each position on the grid one time *within a single word*.

## Total

85 / 100
