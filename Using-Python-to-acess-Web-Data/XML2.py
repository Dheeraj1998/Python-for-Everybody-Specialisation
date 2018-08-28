import xml.etree.ElementTree as ET

data = '''
<commentinfo> <note>This file contains the actual data for your 
assignment - good luck!</note> <comments> <comment> 
<name>Samatar</name> <count>100</count> </comment> <comment> 
<name>Bernadette</name> <count>99</count> </comment> <comment> 
<name>Murren</name> <count>99</count> </comment> <comment> 
<name>Ailish</name> <count>97</count> </comment> <comment> 
<name>Sofia</name> <count>89</count> </comment> <comment> 
<name>Mohamed</name> <count>88</count> </comment> <comment> 
<name>Leen</name> <count>88</count> </comment> <comment> 
<name>Shaw</name> <count>87</count> </comment> <comment> 
<name>Xida</name> <count>86</count> </comment> <comment> 
<name>Kaysha</name> <count>86</count> </comment> <comment> 
<name>Curtis</name> <count>85</count> </comment> <comment> 
<name>Alphonse</name> <count>84</count> </comment> <comment> 
<name>Alea</name> <count>84</count> </comment> <comment> 
<name>Jillian</name> <count>82</count> </comment> <comment> 
<name>Lula</name> <count>79</count> </comment> <comment> 
<name>Regina</name> <count>79</count> </comment> <comment> 
<name>Summer</name> <count>74</count> </comment> <comment> 
<name>Conrad</name> <count>74</count> </comment> <comment> 
<name>Jael</name> <count>73</count> </comment> <comment> 
<name>Niki</name> <count>68</count> </comment> <comment> 
<name>Hariot</name> <count>66</count> </comment> <comment> 
<name>Kaydyne</name> <count>64</count> </comment> <comment> 
<name>Kasi</name> <count>62</count> </comment> <comment> 
<name>Aamna</name> <count>61</count> </comment> <comment> 
<name>Heyden</name> <count>61</count> </comment> <comment> 
<name>Peaches</name> <count>57</count> </comment> <comment> 
<name>Macy</name> <count>53</count> </comment> <comment> 
<name>Anselm</name> <count>49</count> </comment> <comment> 
<name>Eljay</name> <count>44</count> </comment> <comment> 
<name>Charley</name> <count>43</count> </comment> <comment> 
<name>Damian</name> <count>43</count> </comment> <comment> 
<name>Evie</name> <count>36</count> </comment> <comment> 
<name>Rihan</name> <count>36</count> </comment> <comment> 
<name>Niven</name> <count>35</count> </comment> <comment> 
<name>Roman</name> <count>33</count> </comment> <comment> 
<name>Saranna</name> <count>32</count> </comment> <comment> 
<name>Shazina</name> <count>31</count> </comment> <comment> 
<name>Melville</name> <count>28</count> </comment> <comment> 
<name>Awais</name> <count>27</count> </comment> <comment> 
<name>Nikki</name> <count>26</count> </comment> <comment> 
<name>Meerab</name> <count>23</count> </comment> <comment> 
<name>Yasin</name> <count>19</count> </comment> <comment> 
<name>Dearbhail</name> <count>18</count> </comment> <comment> 
<name>Keiryn</name> <count>10</count> </comment> <comment> 
<name>Georgia</name> <count>7</count> </comment> <comment> 
<name>Nash</name> <count>6</count> </comment> <comment> 
<name>Kalum</name> <count>5</count> </comment> <comment> 
<name>Ruben</name> <count>3</count> </comment> <comment> 
<name>Hadjar</name> <count>2</count> </comment> <comment> 
<name>Cacie</name> <count>1</count> </comment> </comments> 
</commentinfo>'''

tree = ET.fromstring(data)
counts = tree.findall('.//count')
total_sum = 0

for count in counts:
	total_sum = total_sum + int(count.text)

print(total_sum)
