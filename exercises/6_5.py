str = 'X-DSPAM-Confidence: 0.8475'
i = str.find(':');
sub_str = str[i+1:]
print(float(sub_str))
