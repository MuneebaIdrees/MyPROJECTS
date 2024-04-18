# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:11:28 2020

@author: munee
"""
import cv2
up=&quot;ABCDEFGHIJKLMNOPQRSTUVWXYZ&quot;
lp=&quot;abcdefghijklmnopqrstuvwxyz&quot;

print(&quot;&quot;&quot;
Enter tha case of your Entered text:
1 for UPPER_CASE
2 for lower_case

&quot;&quot;&quot;)
case=int(input())
input_string=input(&quot;Enter the encoded string: &quot;)
lenght=len(input_string)

print(&quot;&quot;&quot;

Enter Your Choice (in the form of 1, 2, 3)
1. Replace most frequent letter with &quot;E&quot;
2. Replace most frequent letter with &quot;T&quot;

3. Replace most frequent letter with &quot;R&quot;
&quot;&quot;&quot;)
Choice=int(input())

count =[0 for x in range(26)]

#counting frequencies
if(lenght!=0):
for x in range(lenght):
if (input_string[x]==&#39;a&#39; or input_string[x]==&#39;A&#39; ):
count[0]=count[0]+1
elif (input_string[x]==&#39;b&#39; or input_string[x]==&#39;B&#39; ):
count[1]=count[1]+1
elif (input_string[x]==&#39;c&#39; or input_string[x]==&#39;C&#39; ):
count[2]=count[2]+1
elif (input_string[x]==&#39;d&#39; or input_string[x]==&#39;D&#39; ):
count[3]=count[3]+1
elif (input_string[x]==&#39;e&#39; or input_string[x]==&#39;E&#39; ):
count[4]=count[4]+1
elif (input_string[x]==&#39;f&#39; or input_string[x]==&#39;F&#39; ):
count[5]=count[5]+1
elif (input_string[x]==&#39;g&#39; or input_string[x]==&#39;G&#39; ):
count[6]=count[6]+1
elif (input_string[x]==&#39;h&#39; or input_string[x]==&#39;H&#39; ):
count[7]=count[7]+1
elif (input_string[x]==&#39;i&#39; or input_string[x]==&#39;I&#39; ):
count[8]=count[8]+1
elif (input_string[x]==&#39;j&#39; or input_string[x]==&#39;J&#39; ):

count[9]=count[9]+1
elif (input_string[x]==&#39;k&#39; or input_string[x]==&#39;K&#39; ):
count[10]=count[10]+1
elif (input_string[x]==&#39;l&#39; or input_string[x]==&#39;L&#39; ):
count[11]=count[11]+1
elif (input_string[x]==&#39;m&#39; or input_string[x]==&#39;M&#39; ):
count[12]=count[12]+1
elif (input_string[x]==&#39;n&#39; or input_string[x]==&#39;N&#39; ):
count[13]=count[13]+1
elif (input_string[x]==&#39;o&#39; or input_string[x]==&#39;O&#39; ):
count[14]=count[14]+1
elif (input_string[x]==&#39;p&#39; or input_string[x]==&#39;P&#39; ):
count[15]=count[15]+1
elif (input_string[x]==&#39;q&#39; or input_string[x]==&#39;Q&#39; ):
count[16]=count[16]+1
elif (input_string[x]==&#39;r&#39; or input_string[x]==&#39;R&#39; ):
count[17]=count[17]+1
elif (input_string[x]==&#39;s&#39; or input_string[x]==&#39;S&#39; ):
count[18]=count[18]+1
elif (input_string[x]==&#39;t&#39; or input_string[x]==&#39;T&#39; ):
count[19]=count[19]+1
elif (input_string[x]==&#39;u&#39; or input_string[x]==&#39;U&#39; ):
count[20]=count[20]+1
elif (input_string[x] ==&#39;v&#39; or input_string[x]==&#39;V&#39; ):
count[21]=count[21]+1
elif (input_string[x]==&#39;w&#39; or input_string[x]==&#39;W&#39; ):
count[22]=count[22]+1
elif (input_string[x]==&#39;x&#39; or input_string[x]==&#39;X&#39; ):
count[23]=count[23]+1
elif (input_string[x]==&#39;y&#39; or input_string[x]==&#39;Y&#39; ):
count[24]=count[24]+1

elif (input_string[x]==&#39;z&#39; or input_string[x]==&#39;Z&#39; ):
count[25]=count[25]+1

# finding first highest and second highest frequency
maxx = count[0]
secmax = count[0]
number1 = 0
number2 = 0

for k in range (1, 26):
if maxx &lt; (count[k]):
maxx = (count[k])
number1 = k
for i in range (1, 26):
if (secmax &lt; (count[i]) and count[i] != maxx):
secmax = (count[i])
number2 = i

#print(maxx, secmax)
#print(number1, number2)

highest_f = int(0)

#replacing first highest frequency alphabet with E
#replacing values in original string
output_string = &quot;&quot;
diff=int(0)
assign = &#39;a&#39;

if (Choice == 1):

if (case == 1):
highest_f = 65 + number1
key_UC = abs(highest_f - ord(&quot;E&quot;))
#print(key_UC)
for j in range (lenght):
diff=ord(input_string[j]) - key_UC
#print(diff)
diff = diff - 65
diff = diff % 26
assign = up[diff]
output_string = output_string + assign

else:
highest_f = 97 + number1
key_LC = abs(highest_f - ord(&quot;e&quot;))
#print(key_LC)
for l in range (lenght):
diff=ord(input_string[l]) - key_LC
print(diff)
diff = diff - 97
diff = diff % 26
assign = lp[diff]
#print(assign)
output_string = output_string + assign

elif (Choice == 2):
if (case == 1):
highest_f = 65 + number1
key_UC = abs(highest_f - ord(&quot;T&quot;))
#print(key_UC)

for j in range (lenght):
diff=ord(input_string[j]) - key_UC
#print(diff)
diff = diff - 65
diff = diff % 26
assign = up[diff]
output_string = output_string + assign

else:
highest_f = 97 + number1
key_LC = abs(highest_f - ord(&quot;t&quot;))
#print(key_LC)
for l in range (lenght):
diff=ord(input_string[l]) - key_LC
#print(diff)
diff = diff - 97
diff = diff % 26
assign = lp[diff]
#print(assign)
output_string = output_string + assign

elif (Choice == 3):
if (case == 1):
highest_f = 65 + number1
key_UC = abs(highest_f - ord(&quot;T&quot;))
#print(key_UC)
for j in range (lenght):
diff=ord(input_string[j]) - key_UC

#print(diff)
diff = diff - 65
diff = diff % 26
assign = up[diff]
output_string = output_string + assign

else:
highest_f = 97 + number1
key_LC = abs(highest_f - ord(&quot;t&quot;))
#print(key_LC)
for l in range (lenght):
diff=ord(input_string[l]) - key_LC
#print(diff)
diff = diff - 97
diff = diff % 26
assign = lp[diff]
#print(assign)
output_string = output_string + assign

print(&quot;Decoded String is: &quot;)
print(output_string)