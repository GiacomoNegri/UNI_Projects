# Title: Wordle Guesser Description
## Author: Giacomo Negri
## Date: 23/02/2024

# Introduction

This document describes a Wordle-solving algorithm that uses **information entropy** to select optimal guesses. The algorithm iteratively refines the set of possible words based on feedback from previous guesses, improving efficiency in finding the correct word.

# Information Entropy in Wordle

To choose the best guess, we compute the **information entropy** of each possible word, based on how it partitions the remaining word list. Given a word list \$W\$ and a potential guess \$g\$, the entropy is computed as:

$$H(g) = - \sum_{r \in R} P(r) \log_2 P(r)$$

where:

- \$R\$ is the set of possible response patterns based on Wordle's feedback system (green, yellow, gray letters).
- \$P(r)\$ is the probability of receiving a specific response \$r\$ when guessing \$g\$.

A word with higher entropy is preferred, as it maximally reduces the uncertainty in subsequent rounds.

In the given dataset, the word with the highest expected entropy was **'soane'**, making it the optimal first guess based on this approach.

# Two-Step Entropy Optimization

The base entropy approach is extended with a **two-step lookahead** strategy. Instead of selecting the word with the highest immediate entropy, the algorithm evaluates the expected entropy after an additional guess. The expected entropy of a first guess \$g\_1\$ is calculated as:

$$E(H | g_1) = \sum_{r \in R} P(r) \max_{g_2} H(g_2 | r)$$

where \$H(g\_2 | r)\$ is the entropy of the best second guess \$g\_2\$ after observing response \$r\$ to \$g\_1\$. The algorithm selects \$g\_1\$ that minimizes this expected entropy.

While this method theoretically improves performance, it is **computationally intense**, significantly increasing the time required for each decision. As a result, it may not always be practical for real-time gameplay.

# Execution

To run 500 Wordle games using this solver, execute the following command in the console:

```bash
!python game.py --r 500
```

This will simulate multiple rounds and provide statistics on the performance of the guessing strategy.

# Conclusion

By leveraging entropy-based selection, this Wordle solver efficiently reduces the candidate word space, leading to a faster solution. The two-step lookahead further enhances the performance by considering the long-term impact of each guess, though at the cost of increased computation time.

<!--  -->
