import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

#Binomial test to evaluate the possibility of a significant difference between the expected 8% of rescue dogs against the collected data
whippet_rescue = fetchmaker.get_is_rescue('whippet')
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
pval1 = binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pval1)

#ANOVA of different dog weights followed by its tukey test
w = fetchmaker.get_weight('whippet')
t = fetchmaker.get_weight('terrier')
p = fetchmaker.get_weight('pitbull')
print(f_oneway(w, t, p).pvalue)
values = np.concatenate([w, t, p])
labels = ['whippet'] * len(w) + ['terrier'] * len(t) + ['pitbull'] * len(p)
print(pairwise_tukeyhsd(values, labels, 0.05))

#Chi-squared test to see if there is a significant difference between the color breakdown of different dog breeds
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')
color_table = [
  [
    np.count_nonzero(poodle_colors == 'black'),
    np.count_nonzero(shihtzu_colors == 'black')
  ],
  [
    np.count_nonzero(poodle_colors == 'brown'),
    np.count_nonzero(shihtzu_colors == 'brown')
  ],
  [
    np.count_nonzero(poodle_colors == 'gold'),
    np.count_nonzero(shihtzu_colors == 'gold')
  ],
  [
    np.count_nonzero(poodle_colors == 'grey'),
    np.count_nonzero(shihtzu_colors == 'grey')
  ],
  [
    np.count_nonzero(poodle_colors == 'white'),
    np.count_nonzero(shihtzu_colors == 'white')
  ]
]
print(chi2_contingency(color_table))