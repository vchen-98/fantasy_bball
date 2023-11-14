# fantasy_bball

- Starting with a webscraper with all the basic 9 category stats. We want the last 10 years of player data (fitting, since this is around when the 3 point revolution began in the NBA. player archetypes and positional categorical advantages changed a lot around this time)
- 
- First iteration will simply be an examination on the variance of certain stats year over year (we know steals has the higest variance)
- Pearson Correlation Coefficient:
- We'll use correlation to determine how likely it is for a player to maintain their either low or high z-score fantasy contributions based on things like position, profile, height, etc. to eventually thigns like wingspan and deflection numbers. 
- 
- Second step will be dealing with the problem of z-score and its flaws (data in basketball is often right skewed vs normally distributed)
- Looks like z-scores will still be the main driver of calculating value. However, while z-scores are important in calculating a general ranking list, I think the next step is calculating marginal utility in boosting one category over another. This is moving into the realm of drafting and streaming based on team comp, and not so much general ranking metrics. 