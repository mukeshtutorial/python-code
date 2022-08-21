# Give the first term of arithmetic progression series as static input
# and store it in a variable.
fst_trm = 2
# Give the total number of terms of the A.P. series as static input and
# store it in another variable.
total_terms = 6
# Give the common difference of the A.P. series as static input and store it
# in another variable.
common_diff = 4
# Calculate the sum of the given arithmetic progression series using the above given
# mathematical formula(n/2(2a + (n – 1) d)) and store it in a variable.
sum_ap = (total_terms * (2 * fst_trm + (total_terms - 1) * common_diff)) / 2
# Calculate the nth term of the given arithmetic progression series using the above
# given mathematical formula ( Tn = a + (n – 1) d) and store it in another variable.
nth_trm_ap = fst_trm + (total_terms - 1) * common_diff
# Print the sum and nth term of the given Arithmetic Progression series.
print("Given Arithmetic Progression Series Sum with [a,n,d]:(",
      fst_trm, total_terms, common_diff, ") = ", sum_ap)
print("The Given Arithmetic Progression Series nth Term with [a,n,d]:(",
      fst_trm, total_terms, common_diff, ") = ", nth_trm_ap)