import pandas as pd

nutritional_value = [
    ['Natural yoghurt', 60, 4.3, 2, 6.2, 0, 63, 200, 170, 122, 17, 16, 0.03, 0.03, 0.046, 0.216, 0.14, 1],
    ['Potato', 80, 1.9, 0.1, 18.3, 1.5, 7, 443, 4, 56, 23, 1, 0, 0.05, 0.087, 0.046, 1.46, 14],
    ['Cottage chesse 5%', 133, 18.7, 4.7, 3.7, 0, 44, 113, 94, 227, 9, 39, 0.09, 0.08, 0.03, 0.45, 0.18, 0],
    ['Millet groats', 352, 10.5, 2.9, 71.6, 3.2, 5, 220, 10, 240, 100, 0, 0, 0.1, 0.73, 0.38, 2.3, 0],
    ['Pineapple', 56, 0.4, 0.2, 13.6, 1.2, 1, 220, 17, 12, 15, 7, 0, 0.1, 0.09, 0.04, 0.4, 15],
    ['Champignon', 21, 2.7, 0.4, 2.6, 2, 6, 289, 11, 165, 12, 2, 1.94, 0.11, 0.023, 0.599, 4.81, 5],
    ['Gean', 63, 1, 0.3, 14.3, 1.3, 2, 202, 13, 16, 7, 12, 0, 0.13,	0.041, 0.049, 0.33, 15],
    ['Cucumber', 14, 0.7, 0.1, 2.9, 0.5, 11, 125, 15, 23, 8, 28, 0, 0.16, 0.029, 0.038, 0.19, 8],
    ['Banana', 99, 1, 0.3, 23.5, 1.7, 1, 395, 6, 20, 33, 8, 0, 0.27, 0.04, 0.1, 0.5, 9],
    ['Chicken breast', 99, 21.5, 1.3, 0, 0, 55, 385, 5, 240, 33, 6, 0, 0.3, 0.09, 0.153, 12.44, 0],
    ['Buckwheat groats', 347, 12.6, 3.1, 69.3, 5.9, 5, 443, 25, 459, 218, 0, 0, 0.31, 0.541, 0.127, 1.95, 0],
    ['Green Peas', 87, 6.7, 0.4, 17, 6, 2, 353, 22, 122, 29, 68, 0, 0.39, 0.34, 0.16, 2.7, 34.2],
    ['Cod fish', 78, 17.7, 0.7, 0, 0, 72, 356, 9, 184, 25, 7, 1, 0.44, 0.055, 0.046, 2.3, 2],
    ['Raspberry', 42, 1.3, 0.3, 12, 6.7, 2, 203, 35, 33, 20, 3, 0, 0.48, 0.018, 0.062, 0.26, 31.4],
    ['Apple', 50, 0.4, 0.4, 12.1, 2, 2, 134, 4, 9, 3, 4, 0, 0.49, 0.034, 0.026, 0.17, 9.2],
    ['Carrot', 33, 1, 0.2, 8.7, 3.6, 82, 282, 36, 32, 16, 1656, 0, 0.51, 0.054, 0.054, 0.45, 3.4],
    ['Egg', 139, 12.5, 9.7, 0.6, 0, 141, 133, 47, 204, 12, 272, 1.7, 0.73, 0.064, 0.542, 0.06, 0],
    ['Peach', 50, 1, 0.2, 11.9, 1.9, 3, 200, 9, 24, 8, 99, 0, 0.96, 0.022, 0.054, 0.97, 2.7],
    ['Pumpkin', 33, 1.3, 0.3, 7.7, 2.8, 4, 278, 66, 43, 14, 496, 0, 1.03, 0.05, 0.12, 0.5,8],
    ['Tomato', 20, 0.9, 0.2, 4.1, 1.2, 8, 282, 9, 21, 8, 107, 0, 1.22, 0.064, 0.042, 1, 23],
    ['Broccoli', 31, 3, 0.4, 5.2, 2.5, 7, 385, 48, 66, 23, 153, 0, 1.3, 0.07, 0.12, 0.6, 83],
    ['Avocado', 166, 2, 15.3, 7.4, 3.3, 10, 600, 11, 41, 39, 7, 0, 1.3, 0.11, 0.12, 1.9, 8],
    ['Oat flakes', 379, 11.9, 7.2, 69.3, 6.9, 5, 379, 54, 433, 129, 0, 0, 1.8, 0.462, 0.151, 0.87, 0],
    ['Black berries', 51, 0.8, 0.6, 12.2, 3.2, 1, 62, 15, 14, 2, 6, 0, 1.88, 0.018, 0.018, 0.28, 14],
    ['Walnut', 657, 16, 60.3, 18, 6.5, 4, 474, 87, 332, 99, 8, 0, 2.6, 0.39, 0.12, 1.19, 5.8],
    ['Red paprika', 32, 1.3, 0.5, 6.6, 2, 3, 255, 13, 31, 11, 528, 0, 2.9, 0.04, 0.12, 1.6, 144],
    ['Olive oil', 884, 0, 99.6, 0.02, 0, 1, 0, 0, 1, 0, 0, 0, 11.96, 0, 0, 0, 0],
    ['Almonds', 597, 20, 52, 20.5, 12.9, 14, 778, 239, 454, 269, 0, 0, 24, 0.21, 0.78, 3.4, 5.6],
    ['Canola oil', 884, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26.73, 0, 0, 0, 0],
    ['Sunflower seeds', 573, 24.4, 43.7, 24.6, 6, 3, 793, 131, 784, 359, 5, 0, 27.81, 1.318, 0.263, 6.97, 0],
    ['Sunflower oil', 884, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46.71, 0, 0, 0, 0],
    ['Kale', 36, 3.3, 0.7, 6.1, 3.8, 12, 530, 157, 56, 30, 892, 0, 1.7, 0.11, 0.2, 1.6, 120],
    ['Wheat bran', 266, 16, 4.6, 61.9, 42.4, 9, 1121, 119, 1276, 490, 0, 0, 3.81, 0.96, 0.148, 8.89, 0],
    ['Pistachio nuts', 601, 20.5, 48.5, 25, 6.1, 6, 1090, 135, 500, 158, 23, 0, 5.2, 0.82, 0.17, 1.1, 0],
    ['Cacao 16%', 459, 18.2, 21.7, 50.6, 5.7, 17, 1927, 138, 666, 420, 10.7, 0, 0.37, 0.11, 0.46, 2.4, 0]
]

data_frame_nv = pd.DataFrame(nutritional_value)

nutritional_value_headers = ['Product', 'Kcal', 'Protein', 'Fat', 'Carbohydrates', 'Dietary fiber', 'Sodium', 'Potassium', 'Calcium', 'Phosphor', 'Magnesium', 'Vitamin A', 'Vitamin D', 'Vitamin E', 'Vitamin B1', 'Vitamin B2', 'Vitamin B3', 'Vitamin C']

data_frame_nv2 = pd.DataFrame(nutritional_value, columns=nutritional_value_headers)

#result = data_frame_nv2[data_frame_nv2['Kcal'] < 100]

#result = data_frame_nv2[data_frame_nv2['Protein'] > 15]

result = data_frame_nv2[
    (data_frame_nv2['Protein'] > 10)
    &
    (data_frame_nv2['Kcal'] < 200)
]

print(result)







