well_lst = ['PRK014','PRK028','PRK045','PRK052','PRK060','PRK061'
         ,'PRK083','PRK084','PRK085','PWILDC']

nr_icvs_well_dic = {'PRK014':3,'PRK028':2,'PRK045':3,'PRK052':2,'PRK060':2,'PRK061':3
        ,'PRK083':3,'PRK084':2,'PRK085':3,'PWILDC':0}


completion_dic = {}
completion_dic['PRK014'] = '''
25 10 01 1.0 *OPEN
25 10 02 1.0 *OPEN
25 10 03 1.0 *OPEN
25 10 04 1.0 *OPEN
25 10 05 1.0 *OPEN
25 10 06 1.0 *OPEN
25 10 07 1.0 *OPEN
25 10 08 1.0 *OPEN
25 10 09 1.0 *OPEN
25 10 10 1.0 *OPEN
25 10 11 1.0 *OPEN
25 10 12 1.0 *CLOSED
25 10 13 1.0 *CLOSED
25 10 14 1.0 *OPEN
25 10 15 1.0 *OPEN
25 10 16 1.0 *OPEN
25 10 17 1.0 *OPEN
25 10 18 1.0 *OPEN
25 10 19 1.0 *OPEN
25 10 20 1.0 *CLOSED
25 10 21 1.0 *CLOSED
25 10 22 1.0 *OPEN
25 10 23 1.0 *OPEN
25 10 24 1.0 *OPEN
25 10 25 1.0 *OPEN
25 10 26 1.0 *OPEN
25 10 27 1.0 *OPEN
25 10 28 1.0 *OPEN
25 10 29 1.0 *OPEN
25 10 30 1.0 *OPEN
'''
completion_dic['PRK028'] = '''
23 17 01 1.0 *OPEN
23 17 02 1.0 *OPEN
23 17 03 1.0 *OPEN
23 17 04 1.0 *OPEN
23 17 05 1.0 *OPEN
23 17 06 1.0 *OPEN
23 17 07 1.0 *OPEN
23 17 08 1.0 *OPEN
23 17 09 1.0 *OPEN
23 17 10 1.0 *OPEN
23 17 11 1.0 *OPEN
23 17 12 1.0 *OPEN
23 17 13 1.0 *OPEN
23 17 14 1.0 *OPEN
23 17 15 1.0 *OPEN
23 17 16 1.0 *OPEN
23 17 17 1.0 *OPEN
23 17 18 1.0 *OPEN
23 17 19 1.0 *CLOSED
23 17 20 1.0 *CLOSED
23 17 21 1.0 *OPEN
23 17 22 1.0 *OPEN
23 17 23 1.0 *OPEN
23 17 24 1.0 *OPEN
23 17 25 1.0 *OPEN
23 17 26 1.0 *OPEN
23 17 27 1.0 *OPEN
23 17 28 1.0 *OPEN
23 17 29 1.0 *OPEN
23 17 30 1.0 *OPEN
'''
completion_dic['PRK045'] = '''
19 28 01 1.0 *OPEN
19 28 02 1.0 *OPEN
19 28 03 1.0 *OPEN
19 28 04 1.0 *OPEN
19 28 05 1.0 *OPEN
19 28 06 1.0 *OPEN
19 28 07 1.0 *OPEN
19 28 08 1.0 *OPEN
19 28 09 1.0 *OPEN
19 28 10 1.0 *OPEN
19 28 11 1.0 *CLOSED
19 28 12 1.0 *CLOSED
19 28 13 1.0 *OPEN
19 28 14 1.0 *OPEN
19 28 15 1.0 *OPEN
19 28 16 1.0 *OPEN
19 28 17 1.0 *OPEN
19 28 18 1.0 *CLOSED
19 28 19 1.0 *CLOSED
19 28 20 1.0 *OPEN
19 28 21 1.0 *OPEN
19 28 22 1.0 *OPEN
19 28 23 1.0 *OPEN
19 28 24 1.0 *OPEN
19 28 25 1.0 *OPEN
19 28 26 1.0 *OPEN
19 28 27 1.0 *OPEN
19 28 28 1.0 *OPEN
19 28 29 1.0 *OPEN
19 28 30 1.0 *OPEN
'''
completion_dic['PRK052'] = '''
13 40 01 1.0 *OPEN
13 40 02 1.0 *OPEN
13 40 03 1.0 *OPEN
13 40 04 1.0 *OPEN
13 40 05 1.0 *OPEN
13 40 06 1.0 *OPEN
13 40 07 1.0 *OPEN
13 40 08 1.0 *OPEN
13 40 09 1.0 *OPEN
13 40 10 1.0 *OPEN
13 40 11 1.0 *OPEN
13 40 12 1.0 *OPEN
13 40 13 1.0 *OPEN
13 40 14 1.0 *OPEN
13 40 15 1.0 *OPEN
13 40 16 1.0 *CLOSED
13 40 17 1.0 *CLOSED
13 40 18 1.0 *OPEN
13 40 19 1.0 *OPEN
13 40 20 1.0 *OPEN
13 40 21 1.0 *OPEN
13 40 22 1.0 *OPEN
13 40 23 1.0 *OPEN
13 40 24 1.0 *OPEN
13 40 25 1.0 *OPEN
13 40 26 1.0 *OPEN
13 40 27 1.0 *OPEN
13 40 28 1.0 *OPEN
13 40 29 1.0 *OPEN
13 40 30 1.0 *OPEN
'''
completion_dic['PRK060'] = '''
25 45 01 1.0 *OPEN
25 45 02 1.0 *OPEN
25 45 03 1.0 *OPEN
25 45 04 1.0 *OPEN
25 45 05 1.0 *OPEN
25 45 06 1.0 *OPEN
25 45 07 1.0 *OPEN
25 45 08 1.0 *OPEN
25 45 09 1.0 *OPEN
25 45 10 1.0 *OPEN
25 45 11 1.0 *OPEN
25 45 12 1.0 *CLOSED
25 45 13 1.0 *CLOSED
25 45 14 1.0 *OPEN
25 45 15 1.0 *OPEN
25 45 16 1.0 *OPEN
25 45 17 1.0 *OPEN
25 45 18 1.0 *OPEN
25 45 19 1.0 *OPEN
25 45 20 1.0 *OPEN
25 45 21 1.0 *OPEN
25 45 22 1.0 *OPEN
25 45 23 1.0 *OPEN
25 45 24 1.0 *OPEN
25 45 25 1.0 *OPEN
25 45 26 1.0 *OPEN
25 45 27 1.0 *OPEN
25 45 28 1.0 *OPEN
25 45 29 1.0 *OPEN
25 45 30 1.0 *OPEN
'''
completion_dic['PRK061'] = '''
26 34 01 1.0 *OPEN
26 34 02 1.0 *OPEN
26 34 03 1.0 *OPEN
26 34 04 1.0 *OPEN
26 34 05 1.0 *OPEN
26 34 06 1.0 *OPEN
26 34 07 1.0 *OPEN
26 34 08 1.0 *OPEN
26 34 09 1.0 *OPEN
26 34 10 1.0 *OPEN
26 34 11 1.0 *OPEN
26 34 12 1.0 *CLOSED
26 34 13 1.0 *CLOSED
26 34 14 1.0 *OPEN
26 34 15 1.0 *OPEN
26 34 16 1.0 *OPEN
26 34 17 1.0 *OPEN
26 34 18 1.0 *CLOSED
26 34 19 1.0 *CLOSED
26 34 20 1.0 *OPEN
26 34 21 1.0 *OPEN
26 34 22 1.0 *OPEN
26 34 23 1.0 *OPEN
26 34 24 1.0 *OPEN
26 34 25 1.0 *OPEN
26 34 26 1.0 *OPEN
26 34 27 1.0 *OPEN
26 34 28 1.0 *OPEN
26 34 29 1.0 *OPEN
26 34 30 1.0 *OPEN
'''
completion_dic['PRK083'] = '''
11 60 01 1.0 *OPEN
11 60 02 1.0 *OPEN
11 60 03 1.0 *OPEN
11 60 04 1.0 *OPEN
11 60 05 1.0 *OPEN
11 60 06 1.0 *OPEN
11 60 07 1.0 *OPEN
11 60 08 1.0 *OPEN
11 60 09 1.0 *CLOSED
11 60 10 1.0 *CLOSED
11 60 11 1.0 *OPEN
11 60 12 1.0 *OPEN
11 60 13 1.0 *OPEN
11 60 14 1.0 *OPEN
11 60 15 1.0 *OPEN
11 60 16 1.0 *OPEN
11 60 17 1.0 *CLOSED
11 60 18 1.0 *CLOSED
11 60 19 1.0 *OPEN
11 60 20 1.0 *OPEN
11 60 21 1.0 *OPEN
11 60 22 1.0 *OPEN
11 60 23 1.0 *OPEN
11 60 24 1.0 *OPEN
11 60 25 1.0 *OPEN
11 60 26 1.0 *OPEN
11 60 27 1.0 *OPEN
11 60 28 1.0 *OPEN
11 60 29 1.0 *OPEN
11 60 30 1.0 *OPEN
'''
completion_dic['PRK084'] = '''
23 55 01 1.0 *OPEN
23 55 02 1.0 *OPEN
23 55 03 1.0 *OPEN
23 55 04 1.0 *OPEN
23 55 05 1.0 *OPEN
23 55 06 1.0 *OPEN
23 55 07 1.0 *OPEN
23 55 08 1.0 *OPEN
23 55 09 1.0 *OPEN
23 55 10 1.0 *OPEN
23 55 11 1.0 *OPEN
23 55 12 1.0 *CLOSED
23 55 13 1.0 *CLOSED
23 55 14 1.0 *OPEN
23 55 15 1.0 *OPEN
23 55 16 1.0 *OPEN
23 55 17 1.0 *OPEN
23 55 18 1.0 *OPEN
23 55 19 1.0 *OPEN
23 55 20 1.0 *OPEN
23 55 21 1.0 *OPEN
23 55 22 1.0 *OPEN
23 55 23 1.0 *OPEN
23 55 24 1.0 *OPEN
23 55 25 1.0 *OPEN
23 55 26 1.0 *OPEN
23 55 27 1.0 *OPEN
23 55 28 1.0 *OPEN
23 55 29 1.0 *OPEN
23 55 30 1.0 *OPEN
'''
completion_dic['PRK085'] = '''
24 60 01 1.0 *OPEN
24 60 02 1.0 *OPEN
24 60 03 1.0 *OPEN
24 60 04 1.0 *OPEN
24 60 05 1.0 *OPEN
24 60 06 1.0 *OPEN
24 60 07 1.0 *OPEN
24 60 08 1.0 *OPEN
24 60 09 1.0 *OPEN
24 60 10 1.0 *CLOSED
24 60 11 1.0 *CLOSED
24 60 12 1.0 *OPEN
24 60 13 1.0 *OPEN
24 60 14 1.0 *OPEN
24 60 15 1.0 *OPEN
24 60 16 1.0 *OPEN
24 60 17 1.0 *CLOSED
24 60 18 1.0 *CLOSED
24 60 19 1.0 *OPEN
24 60 20 1.0 *OPEN
24 60 21 1.0 *OPEN
24 60 22 1.0 *OPEN
24 60 23 1.0 *OPEN
24 60 24 1.0 *OPEN
24 60 25 1.0 *OPEN
24 60 26 1.0 *OPEN
24 60 27 1.0 *OPEN
24 60 28 1.0 *OPEN
24 60 29 1.0 *OPEN
24 60 30 1.0 *OPEN
'''
completion_dic['PWILDC'] = '''
16 36 01 1.0 *OPEN
16 36 02 1.0 *OPEN
16 36 03 1.0 *OPEN
16 36 04 1.0 *OPEN
16 36 05 1.0 *OPEN
16 36 06 1.0 *OPEN
16 36 07 1.0 *OPEN
16 36 08 1.0 *OPEN
16 36 09 1.0 *OPEN
16 36 10 1.0 *OPEN
16 36 11 1.0 *OPEN
16 36 12 1.0 *OPEN
16 36 13 1.0 *OPEN
16 36 14 1.0 *OPEN
16 36 15 1.0 *OPEN
16 36 16 1.0 *OPEN
16 36 17 1.0 *OPEN
16 36 18 1.0 *OPEN
16 36 19 1.0 *OPEN
16 36 20 1.0 *OPEN
16 36 21 1.0 *OPEN
16 36 22 1.0 *OPEN
16 36 23 1.0 *OPEN
16 36 24 1.0 *OPEN
16 36 25 1.0 *OPEN
16 36 26 1.0 *OPEN
16 36 27 1.0 *OPEN
16 36 28 1.0 *OPEN
16 36 29 1.0 *OPEN
'''

on_time_dic = {}
on_time_dic['PRK085'] = 1.0
on_time_dic['PRK084'] = 1.0
on_time_dic['PRK045'] = 1.0
on_time_dic['PRK083'] = 1.0
on_time_dic['PRK060'] = 1.0
on_time_dic['PRK028'] = 1.0
on_time_dic['PRK061'] = 1.0
on_time_dic['PRK014'] = 1.0
on_time_dic['PRK052'] = 1.0
on_time_dic['PWILDC'] = 1.0

opening_dic = {}
opening_dic['PRK085'] = 1247.0
opening_dic['PRK084'] = 1308.0
opening_dic['PRK045'] = 1369.0
opening_dic['PRK083'] = 1431.0
opening_dic['PRK060'] = 1492.0
opening_dic['PRK028'] = 1612.0
opening_dic['PRK061'] = 1673.0
opening_dic['PRK014'] = 1704.0
opening_dic['PRK052'] = 1765.0
opening_dic['PWILDC'] = 1553.0

layerclump_dic = {}
layerclump_dic['PRK085'] = ['24 60 01:09','24 60 12:16','24 60 19:30']
layerclump_dic['PRK084'] = ['23 55 01:11','23 55 14:30']
layerclump_dic['PRK045'] = ['19 28 01:10','19 28 13:17','19 28 20:30']
layerclump_dic['PRK083'] = ['11 60 01:08','11 60 11:16','11 60 19:30']
layerclump_dic['PRK060'] = ['25 45 01:11','25 45 14:30']
layerclump_dic['PRK028'] = ['23 17 01:18','23 17 21:30']
layerclump_dic['PRK061'] = ['26 34 01:11','26 34 14:17','26 34 20:30']
layerclump_dic['PRK014'] = ['25 10 01:11','25 10 14:19','25 10 22:30']
layerclump_dic['PRK052'] = ['13 40 01:15','13 40 18:30']
layerclump_dic['PWILDC'] = []

icv_start_dic = {}
icv_start_dic['PRK085'] = (2008.0, 183, 200)
icv_start_dic['PRK084'] = (2008.0, 183, 200)
icv_start_dic['PRK045'] = (2008.0, 183, 200)
icv_start_dic['PRK083'] = (2008.0, 183, 200)
icv_start_dic['PRK060'] = (2008.0, 183, 200)
icv_start_dic['PRK028'] = (2008.0, 183, 200)
icv_start_dic['PRK061'] = (2008.0, 183, 200)
icv_start_dic['PRK014'] = (2008.0, 183, 200)
icv_start_dic['PRK052'] = (2008.0, 183, 200)
icv_start_dic['PWILDC'] = ()

icv_control_dic = {}
icv_control_dic['PRK085'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK085']
icv_control_dic['PRK084'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK084']
icv_control_dic['PRK045'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK045']
icv_control_dic['PRK083'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK083']
icv_control_dic['PRK060'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK060']
icv_control_dic['PRK028'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK028']
icv_control_dic['PRK061'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK061']
icv_control_dic['PRK014'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK014']
icv_control_dic['PRK052'] = [(('*ON_CTRLLUMP _LAYER_ *GOR > 250','AND','*ON_CTRLLUMP _LAYER_ *GOR < 500',0.0),('*ON_CTRLLUMP _LAYER_ *WCUT > 0.95',0.0))]*nr_icvs_well_dic['PRK052']
icv_control_dic['PWILDC'] = []
