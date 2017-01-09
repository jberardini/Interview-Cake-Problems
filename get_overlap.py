
"""Notes
left_x: 1
botton_y: 5
width: 10
height: 4

left_x: 4
bottom_y: 2
width: 4
height: 10

Need to find:
bottom corner
width
height

bottom corner is the same as the taller rectangle

width is the distance between the bottom corner and the height of the left rectangle

nope, width is  

steps:
1. figure out which rectangle's bottom left corner is farther left (left_x)
2. calculate the top right corner (subtract xs to get width, ys to get height)
2. save the bottom left corner of the opposite rectangle
3. 

Figure out 
"""

rec1 = {'left_x': 5, 'bottom_y': 5, 'width': 10, 'height': 4}
rec2 = {'left_x': 4, 'bottom_y': 2, 'width': 4, 'height': 10}

def get_overlap(rec1, rec2):
	overlap = {}

	if rec1['left_x'] > rec2['left_x']:
		overlap['left_x'] = rec1['left_x']
		overlap['bottom_y'] = rec1['bottom_y']

		rec2_right_x = rec2['left_x'] + rec2['width']
		rec2_top_y = rec2['bottom_y'] + rec2['height']

		overlap['height'] = rec2_right_x - rec1['left_x']
		overlap['width'] = rec2_top_y - rec1['bottom_y']

	else:
		overlap['left_x'] = rec2['left_x']
		overlap['bottom_y'] = rec2['bottom_y']

		rec1_right_x = rec1['left_x'] + rec1['width']
		rec1_top_y = rec1['bottom_y'] + rec1['height']

		overlap['height'] = rec1_right_x - rec2['left_x']
		overlap['width'] = rec1_top_y - rec2['bottom_y']

	print overlap

get_overlap(rec1, rec2)