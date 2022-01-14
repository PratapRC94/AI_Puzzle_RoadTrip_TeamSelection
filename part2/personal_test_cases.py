import time
import os
import unittest
import route

# Author : Tanmay Sawaji

'''
Instructions:
Don't change the name of get_route() function in your route.py file, else this file will not execute properly.
Note:
These test cases are comparing your output to the output found by my code, I DO NOT claim that my code is giving the optimal values,
but I have checked distance and time values with Google Maps and it is very close to those values. 
I repeat, DO NOT consider the results used in this file as the actual answer, I do NOT claim them to be.
The purpose of this file is just to help everyone test their assignment and compare results.
'''

class Assign_2_testing(unittest.TestCase):
    def test_case_1(self):
        start_city = 'Albany,_California'
        end_city = 'Camden,_South_Carolina'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 104, 'total-miles': 2743.0, 'total-hours': 47.4525641025641, 'total-expected-accidents': 0.003786},{'total-segments': 130, 'total-miles': 2826.0, 'total-hours': 45.024184149184165, 'total-expected-accidents': 0.002985},{'total-segments': 143, 'total-miles': 2903.0, 'total-hours': 45.672552447552455, 'total-expected-accidents': 0.002913}]
        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_2(self):
        start_city = 'Bloomington,_Indiana'
        end_city = 'Aberdeen,_Ohio'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 7, 'total-miles': 182.0, 'total-hours': 3.7051670551670552, 'total-expected-accidents': 0.00034},{'total-segments': 7, 'total-miles': 182.0, 'total-hours': 3.7051670551670552, 'total-expected-accidents': 0.00034},{'total-segments': 8, 'total-miles': 196.0, 'total-hours': 3.7666666666666666, 'total-expected-accidents': 0.000316}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_3(self):
        start_city = 'Blue_Mound,_Texas'
        end_city = 'Braham,_Minnesota'
        cost_function_list = ['distance', 'time','safe']
        result = [{'total-segments': 70, 'total-miles': 1031.0, 'total-hours': 18.929910644910645, 'total-expected-accidents': 0.001603},{'total-segments': 71, 'total-miles': 1045.0, 'total-hours': 16.913034188034192, 'total-expected-accidents': 0.001344},{'total-segments': 78, 'total-miles': 1155.0, 'total-hours': 18.754700854700857, 'total-expected-accidents': 0.001264}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1
    
    def test_case_4(self):
        start_city = 'Bloomington,_Indiana'
        end_city = 'Salem,_Indiana'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 3, 'total-miles': 49.0, 'total-hours': 1.026068376068376, 'total-expected-accidents': 9.8e-05},{'total-segments': 3, 'total-miles': 49.0, 'total-hours': 1.026068376068376, 'total-expected-accidents': 9.8e-05},{'total-segments': 3, 'total-miles': 49.0, 'total-hours': 1.026068376068376, 'total-expected-accidents': 9.8e-05}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1
            
    def test_case_5(self):
        start_city = 'Trenton,_Tennessee'
        end_city = 'Fremont,_California'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 75, 'total-miles': 2217.0, 'total-hours': 39.335295260295275, 'total-expected-accidents': 0.003384},{'total-segments': 70, 'total-miles': 2236.0, 'total-hours': 36.409751359751375, 'total-expected-accidents': 0.002727},{'total-segments': 112, 'total-miles': 2356.0, 'total-hours': 37.36577311577311, 'total-expected-accidents': 0.002382}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1
        
    def test_case_6(self):
        start_city = 'Carrollton,_Virginia'
        end_city = 'Orchard_Park,_New_York'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 26, 'total-miles': 537.0, 'total-hours': 10.78923853923854, 'total-expected-accidents': 0.001019},{'total-segments': 34, 'total-miles': 627.0, 'total-hours': 10.306526806526808, 'total-expected-accidents': 0.00094},{'total-segments': 36, 'total-miles': 681.0, 'total-hours': 11.116647241647241, 'total-expected-accidents': 0.0008}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_7(self):
        start_city = 'Pentagon_City,_Virginia'
        end_city = 'Clinton,_Michigan'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 33, 'total-miles': 529.0, 'total-hours': 10.377700077700078, 'total-expected-accidents': 0.000912},{'total-segments': 35, 'total-miles': 541.0, 'total-hours': 8.729195804195806, 'total-expected-accidents': 0.000951},{'total-segments': 42, 'total-miles': 630.0, 'total-hours': 10.633818958818962, 'total-expected-accidents': 0.00075}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_8(self):
        start_city = 'Easton,_Missouri'
        end_city = 'Vinita,_Oklahoma'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 21, 'total-miles': 249.0, 'total-hours': 5.516087801087802, 'total-expected-accidents': 0.000491},{'total-segments': 19, 'total-miles': 253.0, 'total-hours': 5.083294483294484, 'total-expected-accidents': 0.00044},{'total-segments': 20, 'total-miles': 263.0, 'total-hours': 5.214141414141415, 'total-expected-accidents': 0.000423}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_9(self):
        start_city = 'Monroe,_Louisiana'
        end_city = 'Rose_Point,_Pennsylvania'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 51, 'total-miles': 1054.0, 'total-hours': 22.056721056721056, 'total-expected-accidents': 0.002064},{'total-segments': 75, 'total-miles': 1137.0, 'total-hours': 18.14256021756021, 'total-expected-accidents': 0.001163},{'total-segments': 71, 'total-miles': 1121.0, 'total-hours': 18.18172105672104, 'total-expected-accidents': 0.001152}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_10(self):
        start_city = 'West_Lebanon,_New_Hampshire'
        end_city = 'Bridgeton,_Missouri'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 74, 'total-miles': 1168.0, 'total-hours': 20.442482517482528, 'total-expected-accidents': 0.001669},{'total-segments': 78, 'total-miles': 1178.0, 'total-hours': 19.266802641802645, 'total-expected-accidents': 0.001631},{'total-segments': 93, 'total-miles': 1251.0, 'total-hours': 20.087898212898214, 'total-expected-accidents': 0.001272}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_11(self):
        start_city = 'Rutland,_Vermont'
        end_city = 'Milan,_Minnesota'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 95, 'total-miles': 1453.0, 'total-hours': 28.061363636363623, 'total-expected-accidents': 0.002472},{'total-segments': 104, 'total-miles': 1491.0, 'total-hours': 25.601301476301455, 'total-expected-accidents': 0.002473},{'total-segments': 106, 'total-miles': 1798.0, 'total-hours': 29.27632090132089, 'total-expected-accidents': 0.002001}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1
    
    def test_case_12(self):
        start_city = 'Simpsonville,_Maryland'
        end_city = 'Locust_Grove,_Oklahoma'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 65, 'total-miles': 1188.0, 'total-hours': 19.865073815073806, 'total-expected-accidents': 0.001375},{'total-segments': 69, 'total-miles': 1212.0, 'total-hours': 19.522921522921518, 'total-expected-accidents': 0.001406},{'total-segments': 68, 'total-miles': 1224.0, 'total-hours': 19.698348873348866, 'total-expected-accidents': 0.001326}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_13(self):
        start_city = 'Attleboro_Falls,_Massachusetts'
        end_city = 'Rockvale,_Montana'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 137, 'total-miles': 2192.0, 'total-hours': 42.59739704739704, 'total-expected-accidents': 0.003775},{'total-segments': 143, 'total-miles': 2298.0, 'total-hours': 36.51122766122764, 'total-expected-accidents': 0.00319},{'total-segments': 157, 'total-miles': 2443.0, 'total-hours': 38.98187645687643, 'total-expected-accidents': 0.0025}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_14(self):
        start_city = 'Bucklin,_Missouri'
        end_city = 'Chipman,_New_Brunswick'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 107, 'total-miles': 1794.0, 'total-hours': 34.4144211344211, 'total-expected-accidents': 0.003164},{'total-segments': 133, 'total-miles': 1843.0, 'total-hours': 30.86793706293704, 'total-expected-accidents': 0.002375},{'total-segments': 128, 'total-miles': 1934.0, 'total-hours': 31.919149184149163, 'total-expected-accidents': 0.002259}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_15(self):
        start_city = 'High_Island,_Texas'
        end_city = 'Burlington,_Iowa'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 56, 'total-miles': 988.0, 'total-hours': 20.181410256410253, 'total-expected-accidents': 0.001792},{'total-segments': 55, 'total-miles': 1144.0, 'total-hours': 18.376262626262626, 'total-expected-accidents': 0.001243},{'total-segments': 56, 'total-miles': 1159.0, 'total-hours': 18.535062160062157, 'total-expected-accidents': 0.001228}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1
    
    def test_case_16(self):
        start_city = 'Capistrano_Beach,_California'
        end_city = 'Pine_Ridge,_South_Dakota'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 44, 'total-miles': 1339.0, 'total-hours': 23.245376845376835, 'total-expected-accidents': 0.001711},{'total-segments': 44, 'total-miles': 1357.0, 'total-hours': 22.695163170163166, 'total-expected-accidents': 0.001606},{'total-segments': 50, 'total-miles': 1405.0, 'total-hours': 23.4334693084693, 'total-expected-accidents': 0.001585}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_17(self):
        start_city = 'Cochrane,_Ontario'
        end_city = 'Elkhorn,_Wisconsin'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 33, 'total-miles': 984.0, 'total-hours': 20.40733877233876, 'total-expected-accidents': 0.001959},{'total-segments': 35, 'total-miles': 989.0, 'total-hours': 19.658698523698515, 'total-expected-accidents': 0.001806},{'total-segments': 68, 'total-miles': 1184.0, 'total-hours': 21.535349650349644, 'total-expected-accidents': 0.001786}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_18(self):
        start_city = 'Ligonier,_Indiana'
        end_city = 'Chambersburg,_Pennsylvania'
        cost_function_list = ['distance', 'time','safe']
        result = [{'total-segments': 22, 'total-miles': 485.0, 'total-hours': 10.364083139083139, 'total-expected-accidents': 0.000964},{'total-segments': 27, 'total-miles': 497.0, 'total-hours': 8.883760683760682, 'total-expected-accidents': 0.000994},{'total-segments': 29, 'total-miles': 562.0, 'total-hours': 9.785528360528359, 'total-expected-accidents': 0.000733}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_19(self):
        start_city = 'Breckenridge,_Minnesota'
        end_city = 'Santa_Nella,_California'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 48, 'total-miles': 1752.0, 'total-hours': 34.645299145299134, 'total-expected-accidents': 0.0029},{'total-segments': 54, 'total-miles': 1784.0, 'total-hours': 28.61010101010101, 'total-expected-accidents': 0.001944},{'total-segments': 60, 'total-miles': 1891.0, 'total-hours': 29.56703574203574, 'total-expected-accidents': 0.00194}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1

    def test_case_20(self):
        start_city = 'Lillooet,_British_Columbia'
        end_city = 'Dominguez,_California'
        cost_function_list = ['distance', 'time', 'safe']
        result = [{'total-segments': 63, 'total-miles': 1600.0, 'total-hours': 27.555064791838987, 'total-expected-accidents': 0.002348},{'total-segments': 63, 'total-miles': 1607.0, 'total-hours': 27.478141714915914, 'total-expected-accidents': 0.002355},{'total-segments': 67, 'total-miles': 1610.0, 'total-hours': 27.553471940246123, 'total-expected-accidents': 0.002006}]

        i = 0
        for cost_function in cost_function_list:
            calculated = route.get_route(start_city, end_city, cost_function)
            self.assertEqual(result[i]["total-segments"], calculated["total-segments"])
            self.assertEqual(result[i]["total-miles"], int(calculated["total-miles"]))
            self.assertEqual(round(result[i]["total-hours"], 6), round(calculated["total-hours"], 6))
            self.assertEqual(result[i]["total-expected-accidents"], calculated["total-expected-accidents"])
            i += 1
            
if __name__ == '__main__':
    unittest.main()