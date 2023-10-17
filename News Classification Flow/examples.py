from promptflow import tool


@tool
def prepare_examples():
    return [
        {"category": "PARENTING", "headline": "Can We Allow Children to be Children?", "authors": "Dr. Michele Nealon, Contributor\nPresident, The Chicago School of Professional Psychology", "link": "https://www.huffingtonpost.com/entry/can-we-allow-children-to-be-children_us_5b9d9adae4b03a1dcc8a120e", "short_description": "Have the days passed when children can simply be children and not be asked to or allowed to grow up before their time?", "date": "2013-10-16"},
        {"category": "SPORTS", "headline": "Matt Schaub Injury Leads To T.J. Yates Pick Six And Cheers From Texans Fans (VIDEOS)", "authors": "Chris Greenberg", "link": "https://www.huffingtonpost.com/entry/matt-schaub-injury-tj-yates-interception_us_5bb715cee4b097869fd42147", "short_description": "Entering Week 6, Schaub had tossed a pick six in four straight games. Although Texans coach Gary Kubiak kept the beleaguered", "date": "2013-10-13"},
        {"category": "ENVIRONMENT", "headline": "Corporations Have Personhood. Why Not Dogs? (UPDATED)", "authors": "Arin Greenwood", "link": "https://www.huffingtonpost.com/entry/dogs-personhood_us_5bb14486e4b09bbe9a5d9fa6", "short_description": "\"We already knew that dogs were special,\" he said, adding that we know that they are \"attuned to us,\" as well as being able", "date": "2013-10-12"},
        {"link": "https://www.huffpost.com/entry/wisconsin-police-wild-turkey-chase_n_62f4951ee4b0288b61a18acc", "headline": "Feathers Fly As Wild Turkey Dodges Cops In Slapstick Apartment Chase", "category": "WEIRD NEWS", "short_description": "One officer used a net in an attempt to nab the turkey as it shuffled around an apartment on Friday.", "authors": "Ben Blanchet", "date": "2022-08-11"}
    ]
