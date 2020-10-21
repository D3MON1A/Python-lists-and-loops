all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def generate_li():
    filtered_colors= filter_colors(all_colors)
    message= "".join(list(map(lambda color: f"<li>{color['label']}</li>", filtered_colors)))
    return message
def filter_colors(colors):
    return list(filter(lambda color: color["sexy"], colors))
print(generate_li())

