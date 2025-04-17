def life_in_weeks(age):
    age_weeks = age * 52
    age_weeks_90 = 90 * 52
    final_age = age_weeks_90 - age_weeks

    print(f'You have {final_age} weeks left.')

life_in_weeks(56)
