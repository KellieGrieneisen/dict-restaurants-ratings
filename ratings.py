"""Restaurant rating lister."""
def restaurant_scores(path):
    pull_scores = sorted(open(path))

    restaurants_and_rating= { }
    
    for line in pull_scores:

        restaurant_rate_data = line.split(":")
        key = restaurant_rate_data[0]
        value = restaurant_rate_data[1].rstrip('\n,')
        restaurants_and_rating[key]= restaurants_and_rating.get(key, value)
        

        print(f'{key} is rated at {value}')
        #print(line)

    
    
    

restaurant_scores('scores.txt')        





# put your code here
