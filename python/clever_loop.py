list1 = [x**2 for x in range(10)]
# let's do a loop over loop to get values in a dictionary of dictionaries
color_dict = {'Dou':{'Red':0,'Blue':10,'Yellow':5}, 'Bao':{'Red':5,'Blue':8,'Yellow':6}}
# Here I want to get what's Bao and Dou's rating for Blue
Dou_Blue, Bao_Blue = [person['Blue'] for person in [color_dict[key] for key in ['Dou','Bao']]]



# Function enumerate(list/array) wrap index and element together
for i, item in enumerate(list1):
    print i, item
