import numpy as np
import pandas as pd

np.random.seed(42)

n_users = 10000

ab_test = pd.DataFrame({
    'user_id': range(n_users),
    'group': np.random.choice(
        ['control','treatment'],
        size=n_users
    )
})


control_ctr = 0.10
treatment_ctr = 0.115

ab_test['clicked'] = np.where(
    ab_test['group'] == 'control',
    np.random.binomial(1, control_ctr, n_users),
    np.random.binomial(1, treatment_ctr, n_users)
)


print(
    ab_test.groupby('group')['clicked']
    .mean()
)

from scipy.stats import chi2_contingency

contingency = pd.crosstab(
    ab_test['group'],
    ab_test['clicked']
)

chi2, p_value, dof, expected = chi2_contingency(contingency)

print("\nP-Value:")
print(p_value)



control_ctr = (
    ab_test[ab_test['group']=='control']
    ['clicked']
    .mean()
)

treatment_ctr = (
    ab_test[ab_test['group']=='treatment']
    ['clicked']
    .mean()
)

uplift = (
    (treatment_ctr - control_ctr)
    / control_ctr
) * 100

print("\nCTR Uplift (%):")
print(round(uplift,2))